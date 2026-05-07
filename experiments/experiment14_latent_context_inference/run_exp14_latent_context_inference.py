#!/usr/bin/env python3
"""Experiment 14: latent context inference for Context-Indexed Route Memory.

This successor experiment starts after Exp13.2's baseline suite. Exp13.2 showed
that an oracle context-gated lookup table can solve the clean symbolic route task
as well as CIRM when the correct world label is supplied. Exp14 therefore removes
that oracle label at evaluation time and asks whether the route-memory system can
select the correct world/context from partial transition evidence before executing
a route.

Scientific target:
- separate context-indexed storage from oracle context labels;
- quantify latent world selection under clean and stochastically corrupted cues;
- compare against transparent selector baselines under the same route benchmark;
- produce seed-level uncertainty, effect sizes, plots, SQLite records, and a
  validation report suitable for manuscript triage.

Importing this file does not run the experiment. Use the PowerShell wrappers or:

    python run_exp14_latent_context_inference.py --profile smoke
    python validate_exp14.py --analysis-root analysis
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import math
import os
import platform
import random
import shutil
import sqlite3
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


EXPERIMENT_NAME = "exp14_latent_context_inference"
ANALYSIS_ID = "exp14"
SCHEMA_VERSION = "exp14_metrics_v1"
NO_CAPACITY = "none"

TransitionKey = Tuple[int, int, int]  # world, source node, mode
SharedTransitionKey = Tuple[int, int]  # source node, mode
Cue = Tuple[int, int, int]  # source node, mode, observed target
RouteEndpointKey = Tuple[int, int, Tuple[int, ...]]  # world, start node, mode sequence
Query = Dict[str, Any]
MetricRow = Dict[str, Any]


@dataclass(frozen=True)
class Config:
    profile: str
    seeds: Tuple[int, ...]
    world_counts: Tuple[int, ...]
    route_lengths: Tuple[int, ...]
    routes_per_world: int
    modes: int
    cue_counts: Tuple[int, ...]
    corruption_rates: Tuple[float, ...]
    hash_slot_divisors: Tuple[int, ...]
    progress_every: int
    sample_suffixes_per_route: int


@dataclass(frozen=True)
class RouteBenchmark:
    seed: int
    world_count: int
    route_length: int
    routes_per_world: int
    modes: int
    node_count: int
    transitions: Dict[TransitionKey, int]
    shared_first_keys: List[Tuple[int, int]]
    route_paths: Dict[Tuple[int, int], Tuple[int, ...]]
    route_modes: Dict[int, Tuple[int, ...]]
    seen_route_queries: List[Query]
    suffix_route_queries: List[Query]
    primitive_queries_by_world: Dict[int, List[Query]]

    @property
    def total_transitions(self) -> int:
        return len(self.transitions)


def stable_hash_int(*parts: Any) -> int:
    text = "|".join(str(p) for p in parts)
    return int(hashlib.sha256(text.encode("utf-8")).hexdigest()[:16], 16)


def make_config(profile: str, progress_every: Optional[int] = None) -> Config:
    """Return deterministic profile configuration."""
    profile = profile.lower().strip()
    if profile == "smoke":
        cfg = Config(
            profile="smoke",
            seeds=(0, 1),
            world_counts=(4,),
            route_lengths=(4, 8),
            routes_per_world=8,
            modes=4,
            cue_counts=(1, 2),
            corruption_rates=(0.0, 0.5),
            hash_slot_divisors=(2,),
            progress_every=10,
            sample_suffixes_per_route=1,
        )
    elif profile == "validation":
        cfg = Config(
            profile="validation",
            seeds=tuple(range(5)),
            world_counts=(4, 8),
            route_lengths=(4, 8),
            routes_per_world=12,
            modes=4,
            cue_counts=(1, 2, 4),
            corruption_rates=(0.0, 0.25, 0.5),
            hash_slot_divisors=(2, 4),
            progress_every=25,
            sample_suffixes_per_route=1,
        )
    elif profile == "full":
        cfg = Config(
            profile="full",
            seeds=tuple(range(20)),
            world_counts=(4, 8, 16, 32),
            route_lengths=(4, 8, 12, 16),
            routes_per_world=24,
            modes=4,
            cue_counts=(1, 2, 4, 8),
            corruption_rates=(0.0, 0.10, 0.25, 0.50),
            hash_slot_divisors=(2, 4, 8),
            progress_every=50,
            sample_suffixes_per_route=1,
        )
    else:
        raise ValueError(f"Unknown profile '{profile}'. Expected smoke, validation, or full.")

    if progress_every is not None:
        cfg = dataclasses.replace(cfg, progress_every=max(1, int(progress_every)))
    return cfg


class ProgressLogger:
    """Verbose JSONL + console progress logger with ETA estimates."""

    def __init__(self, path: Path, total_units: int, *, progress_every: int = 25) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.total_units = max(1, int(total_units))
        self.progress_every = max(1, int(progress_every))
        self.start_time = time.time()
        self.last_console_time = 0.0
        self.completed_units = 0
        self.current_phase = "init"
        self.phase_units: Dict[str, int] = defaultdict(int)
        self.path.write_text("", encoding="utf-8")

    def _eta_seconds(self) -> Optional[float]:
        if self.completed_units <= 0:
            return None
        elapsed = time.time() - self.start_time
        rate = self.completed_units / max(elapsed, 1e-9)
        return max(0.0, (self.total_units - self.completed_units) / max(rate, 1e-9))

    @staticmethod
    def _format_seconds(seconds: Optional[float]) -> str:
        if seconds is None or not math.isfinite(seconds):
            return "unknown"
        seconds = int(round(seconds))
        h, rem = divmod(seconds, 3600)
        m, s = divmod(rem, 60)
        if h:
            return f"{h}h {m}m {s}s"
        if m:
            return f"{m}m {s}s"
        return f"{s}s"

    def event(self, event: str, **payload: Any) -> None:
        now = time.time()
        eta = self._eta_seconds()
        record = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "event": event,
            "phase": payload.pop("phase", self.current_phase),
            "completed_units": self.completed_units,
            "total_units": self.total_units,
            "percent_complete": round(100.0 * self.completed_units / self.total_units, 3),
            "elapsed_seconds": round(now - self.start_time, 3),
            "eta_seconds": None if eta is None else round(float(eta), 3),
            **payload,
        }
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, sort_keys=True) + "\n")

    def phase_start(self, phase: str, planned_units: int, **payload: Any) -> None:
        self.current_phase = phase
        self.event("phase_start", phase=phase, planned_units=planned_units, **payload)
        print(
            f"\n[{EXPERIMENT_NAME}] Starting phase '{phase}' "
            f"({planned_units} units planned). Overall {self.completed_units}/{self.total_units}."
        )

    def unit_done(self, phase: Optional[str] = None, **payload: Any) -> None:
        phase = phase or self.current_phase
        self.current_phase = phase
        self.completed_units += 1
        self.phase_units[phase] += 1
        self.event("unit_complete", phase=phase, **payload)
        should_print = (
            self.completed_units == 1
            or self.completed_units % self.progress_every == 0
            or self.completed_units == self.total_units
            or time.time() - self.last_console_time > 15.0
        )
        if should_print:
            self.last_console_time = time.time()
            elapsed = time.time() - self.start_time
            rate = self.completed_units / max(elapsed, 1e-9)
            print(
                f"[{EXPERIMENT_NAME}] {self.completed_units}/{self.total_units} "
                f"({100.0 * self.completed_units / self.total_units:5.1f}%) | "
                f"phase={phase} | elapsed={self._format_seconds(elapsed)} | "
                f"rate={rate:.2f} units/s | eta={self._format_seconds(self._eta_seconds())}"
            )

    def finish(self, **payload: Any) -> None:
        elapsed = time.time() - self.start_time
        self.event("run_complete", elapsed_seconds=round(elapsed, 3), phase_units=dict(self.phase_units), **payload)
        print(
            f"\n[{EXPERIMENT_NAME}] Complete: {self.completed_units}/{self.total_units} units in "
            f"{self._format_seconds(elapsed)}."
        )


def make_benchmark(seed: int, world_count: int, route_length: int, routes_per_world: int, modes: int) -> RouteBenchmark:
    """Generate a benchmark with incompatible first-step transitions across worlds.

    Start nodes and mode sequences are shared across worlds; the first transition
    and all continuation nodes are world-specific. A correct latent world choice is
    therefore necessary for full-route execution, while suffix probes test whether
    stored one-step primitives can be reused after a world has been inferred.
    """
    rng = random.Random(seed * 1_000_003 + world_count * 1009 + route_length * 917 + routes_per_world)
    shared_start_offset = 1
    continuation_offset = shared_start_offset + routes_per_world + 10
    nodes_needed = continuation_offset + world_count * routes_per_world * route_length + 10

    transitions: Dict[TransitionKey, int] = {}
    route_paths: Dict[Tuple[int, int], Tuple[int, ...]] = {}
    route_modes: Dict[int, Tuple[int, ...]] = {}
    seen_queries: List[Query] = []
    suffix_queries: List[Query] = []
    primitive_by_world: Dict[int, List[Query]] = {w: [] for w in range(world_count)}
    shared_first_keys: List[Tuple[int, int]] = []

    for route_id in range(routes_per_world):
        seq = tuple(rng.randrange(modes) for _ in range(route_length))
        if len(set(seq)) == 1 and route_length > 1:
            seq = tuple((seq[i] + i) % modes for i in range(route_length))
        route_modes[route_id] = seq
        shared_first_keys.append((shared_start_offset + route_id, seq[0]))

    for world in range(world_count):
        for route_id in range(routes_per_world):
            start = shared_start_offset + route_id
            path = [start]
            for step in range(route_length):
                path.append(continuation_offset + world * routes_per_world * route_length + route_id * route_length + step)
            modes_seq = route_modes[route_id]
            route_paths[(world, route_id)] = tuple(path)
            for step, mode in enumerate(modes_seq):
                src = path[step]
                tgt = path[step + 1]
                key = (world, src, mode)
                if key in transitions and transitions[key] != tgt:
                    raise AssertionError(f"Conflicting transition unexpectedly generated: {key}")
                transitions[key] = tgt
                primitive_by_world[world].append(
                    {
                        "world": world,
                        "route_id": route_id,
                        "query_type": "primitive",
                        "source": src,
                        "mode": mode,
                        "target": tgt,
                        "step": step,
                        "route_length": route_length,
                    }
                )
            seen_queries.append(
                {
                    "world": world,
                    "route_id": route_id,
                    "query_type": "seen_route",
                    "start": start,
                    "modes": modes_seq,
                    "target": path[-1],
                    "route_length": route_length,
                }
            )
            # One deterministic suffix per route keeps full runs bounded while still
            # testing composition from a sub-route never presented as a whole route.
            if route_length >= 4:
                suffix_start_step = max(1, route_length // 2)
            else:
                suffix_start_step = 1
            suffix_modes = modes_seq[suffix_start_step:]
            if len(suffix_modes) >= 2:
                suffix_queries.append(
                    {
                        "world": world,
                        "route_id": route_id,
                        "query_type": "suffix_route",
                        "start": path[suffix_start_step],
                        "modes": suffix_modes,
                        "target": path[-1],
                        "route_length": len(suffix_modes),
                        "parent_route_length": route_length,
                        "suffix_start_step": suffix_start_step,
                    }
                )

    return RouteBenchmark(
        seed=seed,
        world_count=world_count,
        route_length=route_length,
        routes_per_world=routes_per_world,
        modes=modes,
        node_count=nodes_needed,
        transitions=transitions,
        shared_first_keys=shared_first_keys,
        route_paths=route_paths,
        route_modes=route_modes,
        seen_route_queries=seen_queries,
        suffix_route_queries=suffix_queries,
        primitive_queries_by_world=primitive_by_world,
    )


class LatentContextModel:
    name = "latent_context_model"
    family = "abstract"
    description = "abstract latent-context model"
    is_oracle_baseline = False

    def fit(self, benchmark: RouteBenchmark) -> None:
        raise NotImplementedError

    def select_world(self, cues: Sequence[Cue], true_world: int, query: Query, rng: random.Random) -> Tuple[Optional[int], float, float]:
        raise NotImplementedError

    def predict_step(self, selected_world: Optional[int], source: int, mode: int) -> Optional[int]:
        raise NotImplementedError

    def predict_route(self, selected_world: Optional[int], start: int, modes: Sequence[int]) -> Optional[int]:
        node: Optional[int] = start
        for mode in modes:
            if node is None:
                return None
            node = self.predict_step(selected_world, node, int(mode))
            if node is None:
                return None
        return node

    @property
    def context_slots(self) -> Optional[int]:
        return None

    @property
    def capacity_used(self) -> int:
        return 0

    @property
    def hash_collisions(self) -> int:
        return 0


class CirmLatentSelector(LatentContextModel):
    name = "exp14_cirm_latent_selector"
    family = "context_indexed_route_memory"
    description = "CIRM-style world-indexed structural table with latent context selection from transition cues."
    is_oracle_baseline = False

    def fit(self, benchmark: RouteBenchmark) -> None:
        self.benchmark = benchmark
        self.table = dict(benchmark.transitions)
        self.worlds = tuple(range(benchmark.world_count))

    @property
    def capacity_used(self) -> int:
        return len(self.table)

    def _world_scores(self, cues: Sequence[Cue]) -> Dict[int, float]:
        scores: Dict[int, float] = {}
        for world in self.worlds:
            score = 0.0
            for source, mode, observed_target in cues:
                if self.table.get((world, source, mode)) == observed_target:
                    score += 1.0
            scores[world] = score
        return scores

    def select_world(self, cues: Sequence[Cue], true_world: int, query: Query, rng: random.Random) -> Tuple[Optional[int], float, float]:
        scores = self._world_scores(cues)
        best_score = max(scores.values()) if scores else 0.0
        best_worlds = [world for world, score in scores.items() if score == best_score]
        # Deterministic tie-breaker that does not favor the true world.
        tie_index = stable_hash_int("cirm_tie", query["query_type"], query["world"], query["route_id"], query["start"], len(cues)) % len(best_worlds)
        selected = best_worlds[tie_index]
        ordered_scores = sorted(scores.values(), reverse=True)
        second = ordered_scores[1] if len(ordered_scores) > 1 else 0.0
        margin = (best_score - second) / max(1, len(cues))
        confidence = best_score / max(1, len(cues))
        return selected, confidence, margin

    def predict_step(self, selected_world: Optional[int], source: int, mode: int) -> Optional[int]:
        if selected_world is None:
            return None
        return self.table.get((int(selected_world), int(source), int(mode)))


class OracleContextGatedTable(CirmLatentSelector):
    name = "baseline_oracle_context_gated_table"
    family = "oracle_context_gated_lookup"
    description = "Upper-bound context-gated transition table supplied with the true world label at evaluation."
    is_oracle_baseline = True

    def select_world(self, cues: Sequence[Cue], true_world: int, query: Query, rng: random.Random) -> Tuple[Optional[int], float, float]:
        return int(true_world), 1.0, 1.0


class SharedNoContextTable(LatentContextModel):
    name = "baseline_shared_no_context_table"
    family = "shared_lookup"
    description = "No-context transition table keyed only by source and mode, using majority target under conflicts."
    is_oracle_baseline = False

    def fit(self, benchmark: RouteBenchmark) -> None:
        self.benchmark = benchmark
        buckets: Dict[SharedTransitionKey, Counter[int]] = defaultdict(Counter)
        for (_world, source, mode), target in benchmark.transitions.items():
            buckets[(source, mode)][target] += 1
        self.table: Dict[SharedTransitionKey, int] = {}
        self.conflicting_keys = 0
        for key, counter in buckets.items():
            if len(counter) > 1:
                self.conflicting_keys += 1
            # Deterministic majority/tie choice.
            self.table[key] = sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]

    @property
    def capacity_used(self) -> int:
        return len(self.table)

    def select_world(self, cues: Sequence[Cue], true_world: int, query: Query, rng: random.Random) -> Tuple[Optional[int], float, float]:
        return None, 0.0, 0.0

    def predict_step(self, selected_world: Optional[int], source: int, mode: int) -> Optional[int]:
        return self.table.get((int(source), int(mode)))


class RandomContextSelector(CirmLatentSelector):
    name = "baseline_random_context_selector"
    family = "latent_context_baseline"
    description = "Random world selector followed by the same per-world table."
    is_oracle_baseline = False

    def select_world(self, cues: Sequence[Cue], true_world: int, query: Query, rng: random.Random) -> Tuple[Optional[int], float, float]:
        idx = stable_hash_int("random_selector", self.benchmark.seed, query["query_type"], query["world"], query["route_id"], len(cues)) % self.benchmark.world_count
        return int(idx), 1.0 / max(1, self.benchmark.world_count), 0.0


class RecencyContextSelector(CirmLatentSelector):
    name = "baseline_recency_context_selector"
    family = "latent_context_baseline"
    description = "Always selects the most recently learned world, then uses the per-world table."
    is_oracle_baseline = False

    def select_world(self, cues: Sequence[Cue], true_world: int, query: Query, rng: random.Random) -> Tuple[Optional[int], float, float]:
        return self.benchmark.world_count - 1, 1.0 if true_world == self.benchmark.world_count - 1 else 0.0, 0.0


class HashSlotLatentSelector(LatentContextModel):
    family = "compact_context_hash_lookup"
    description = "Compact context-conditioned hash-slot selector; worlds sharing a slot overwrite or collide."
    is_oracle_baseline = False

    def __init__(self, divisor: int) -> None:
        self.divisor = max(1, int(divisor))
        self.name = f"baseline_hash_slot_selector_div{self.divisor}"

    def fit(self, benchmark: RouteBenchmark) -> None:
        self.benchmark = benchmark
        self.slots = max(1, math.ceil(benchmark.world_count / self.divisor))
        self.table: Dict[Tuple[int, int, int], int] = {}
        self.slot_to_worlds: Dict[int, List[int]] = defaultdict(list)
        self.collision_count = 0
        for world in range(benchmark.world_count):
            slot = self._slot(world)
            self.slot_to_worlds[slot].append(world)
        for (world, source, mode), target in benchmark.transitions.items():
            key = (self._slot(world), source, mode)
            if key in self.table and self.table[key] != target:
                self.collision_count += 1
            self.table[key] = target

    def _slot(self, world: int) -> int:
        return int(world) % self.slots

    @property
    def context_slots(self) -> int:
        return self.slots

    @property
    def hash_collisions(self) -> int:
        return self.collision_count

    @property
    def capacity_used(self) -> int:
        return len(self.table)

    def _slot_scores(self, cues: Sequence[Cue]) -> Dict[int, float]:
        scores: Dict[int, float] = {}
        for slot in range(self.slots):
            score = 0.0
            for source, mode, observed_target in cues:
                if self.table.get((slot, source, mode)) == observed_target:
                    score += 1.0
            scores[slot] = score
        return scores

    def select_world(self, cues: Sequence[Cue], true_world: int, query: Query, rng: random.Random) -> Tuple[Optional[int], float, float]:
        scores = self._slot_scores(cues)
        best_score = max(scores.values()) if scores else 0.0
        best_slots = [slot for slot, score in scores.items() if score == best_score]
        slot_index = stable_hash_int("hash_slot_tie", self.divisor, query["query_type"], query["world"], query["route_id"], len(cues)) % len(best_slots)
        selected_slot = int(best_slots[slot_index])
        worlds_in_slot = self.slot_to_worlds.get(selected_slot, [])
        # The predictor uses the slot itself. For world-selection accuracy, choose a deterministic representative world.
        representative_world = worlds_in_slot[0] if worlds_in_slot else None
        ordered = sorted(scores.values(), reverse=True)
        second = ordered[1] if len(ordered) > 1 else 0.0
        margin = (best_score - second) / max(1, len(cues))
        confidence = best_score / max(1, len(cues))
        # Encode slots as negative integers so predict_step can distinguish them from real worlds.
        encoded_slot = -1 - selected_slot
        return encoded_slot if representative_world is not None else None, confidence, margin

    def predict_step(self, selected_world: Optional[int], source: int, mode: int) -> Optional[int]:
        if selected_world is None:
            return None
        if selected_world >= 0:
            slot = self._slot(int(selected_world))
        else:
            slot = -1 - int(selected_world)
        return self.table.get((slot, int(source), int(mode)))

    def selected_world_matches_true(self, selected_world: Optional[int], true_world: int) -> bool:
        if selected_world is None:
            return False
        slot = -1 - int(selected_world) if selected_world < 0 else self._slot(int(selected_world))
        return self._slot(true_world) == slot


class RouteEndpointMemorizer(LatentContextModel):
    name = "baseline_route_endpoint_memorizer_with_latent_selector"
    family = "whole_route_memorizer"
    description = "Infers context from cues but predicts only memorized whole-route endpoints; suffix probes should fail."
    is_oracle_baseline = False

    def fit(self, benchmark: RouteBenchmark) -> None:
        self.benchmark = benchmark
        self.selector = CirmLatentSelector()
        self.selector.fit(benchmark)
        self.endpoints: Dict[RouteEndpointKey, int] = {}
        for query in benchmark.seen_route_queries:
            self.endpoints[(int(query["world"]), int(query["start"]), tuple(int(m) for m in query["modes"]))] = int(query["target"])

    @property
    def capacity_used(self) -> int:
        return len(self.endpoints)

    def select_world(self, cues: Sequence[Cue], true_world: int, query: Query, rng: random.Random) -> Tuple[Optional[int], float, float]:
        return self.selector.select_world(cues, true_world, query, rng)

    def predict_step(self, selected_world: Optional[int], source: int, mode: int) -> Optional[int]:
        # This model has no reusable one-step transitions.
        return None

    def predict_route(self, selected_world: Optional[int], start: int, modes: Sequence[int]) -> Optional[int]:
        if selected_world is None or selected_world < 0:
            return None
        return self.endpoints.get((int(selected_world), int(start), tuple(int(m) for m in modes)))


def build_models(hash_slot_divisors: Sequence[int]) -> List[LatentContextModel]:
    models: List[LatentContextModel] = [
        CirmLatentSelector(),
        OracleContextGatedTable(),
        SharedNoContextTable(),
        RouteEndpointMemorizer(),
        RandomContextSelector(),
        RecencyContextSelector(),
    ]
    models.extend(HashSlotLatentSelector(divisor) for divisor in hash_slot_divisors)
    return models


def sample_cues(
    benchmark: RouteBenchmark,
    *,
    true_world: int,
    exclude_route_id: int,
    cue_count: int,
    corruption_rate: float,
    seed_parts: Sequence[Any],
) -> List[Cue]:
    """Sample context cues from the true world with optional wrong-world corruption.

    Cues are primitive one-step observations. They avoid the queried route where
    possible so context inference is not just a direct replay of the target route.
    Corruption replaces individual cues with a transition from a different world.
    """
    rng = random.Random(stable_hash_int("cue", *seed_parts))
    clean_pool = [q for q in benchmark.primitive_queries_by_world[true_world] if int(q["route_id"]) != int(exclude_route_id)]
    if not clean_pool:
        clean_pool = list(benchmark.primitive_queries_by_world[true_world])
    wrong_worlds = [w for w in range(benchmark.world_count) if w != true_world]
    cues: List[Cue] = []
    for i in range(cue_count):
        use_wrong = bool(wrong_worlds) and rng.random() < corruption_rate
        if use_wrong:
            wrong_world = wrong_worlds[rng.randrange(len(wrong_worlds))]
            wrong_pool = benchmark.primitive_queries_by_world[wrong_world]
            q = wrong_pool[rng.randrange(len(wrong_pool))]
        else:
            q = clean_pool[rng.randrange(len(clean_pool))]
        cues.append((int(q["source"]), int(q["mode"]), int(q["target"])))
    return cues


def evaluate_route_set(
    model: LatentContextModel,
    benchmark: RouteBenchmark,
    queries: Sequence[Query],
    *,
    cue_count: int,
    corruption_rate: float,
    query_type: str,
) -> Dict[str, Any]:
    total = len(queries)
    composition_correct = 0
    world_correct = 0
    first_step_correct = 0
    first_step_total = 0
    margin_sum = 0.0
    confidence_sum = 0.0
    route_table_selected_correct = 0
    route_table_selected_total = 0

    for query in queries:
        true_world = int(query["world"])
        route_id = int(query["route_id"])
        cues = sample_cues(
            benchmark,
            true_world=true_world,
            exclude_route_id=route_id,
            cue_count=cue_count,
            corruption_rate=corruption_rate,
            seed_parts=(benchmark.seed, query_type, true_world, route_id, cue_count, corruption_rate, int(query["start"])),
        )
        rng = random.Random(stable_hash_int("eval", benchmark.seed, model.name, query_type, true_world, route_id, cue_count, corruption_rate))
        selected_world, confidence, margin = model.select_world(cues, true_world, query, rng)

        if hasattr(model, "selected_world_matches_true"):
            selected_correct = bool(getattr(model, "selected_world_matches_true")(selected_world, true_world))
        else:
            selected_correct = selected_world == true_world
        world_correct += int(selected_correct)
        confidence_sum += float(confidence)
        margin_sum += float(margin)

        predicted = model.predict_route(selected_world, int(query["start"]), tuple(int(m) for m in query["modes"]))
        composition_correct += int(predicted == int(query["target"]))

        if query_type == "seen_route":
            first_mode = int(query["modes"][0])
            expected_first = benchmark.transitions.get((true_world, int(query["start"]), first_mode))
            predicted_first = model.predict_step(selected_world, int(query["start"]), first_mode)
            first_step_total += 1
            first_step_correct += int(predicted_first == expected_first)

        # Route-table-under-selected-context samples the primitive table for the true world.
        primitive_pool = benchmark.primitive_queries_by_world[true_world]
        probe = primitive_pool[stable_hash_int("primitive_probe", benchmark.seed, query_type, true_world, route_id) % len(primitive_pool)]
        predicted_step = model.predict_step(selected_world, int(probe["source"]), int(probe["mode"]))
        route_table_selected_correct += int(predicted_step == int(probe["target"]))
        route_table_selected_total += 1

    return {
        f"composition_correct_{query_type}": composition_correct,
        f"composition_total_{query_type}": total,
        f"composition_accuracy_{query_type}": composition_correct / max(1, total),
        f"world_selection_correct_{query_type}": world_correct,
        f"world_selection_total_{query_type}": total,
        f"world_selection_accuracy_{query_type}": world_correct / max(1, total),
        f"mean_world_confidence_{query_type}": confidence_sum / max(1, total),
        f"mean_world_margin_{query_type}": margin_sum / max(1, total),
        f"route_table_selected_correct_{query_type}": route_table_selected_correct,
        f"route_table_selected_total_{query_type}": route_table_selected_total,
        f"route_table_selected_accuracy_{query_type}": route_table_selected_correct / max(1, route_table_selected_total),
        "first_step_context_correct": first_step_correct,
        "first_step_context_total": first_step_total,
        "first_step_context_accuracy": (first_step_correct / first_step_total) if first_step_total else np.nan,
    }


def evaluate_model_condition(
    model: LatentContextModel,
    benchmark: RouteBenchmark,
    *,
    cue_count: int,
    corruption_rate: float,
    phase: str,
) -> MetricRow:
    seen = evaluate_route_set(
        model,
        benchmark,
        benchmark.seen_route_queries,
        cue_count=cue_count,
        corruption_rate=corruption_rate,
        query_type="seen_route",
    )
    suffix = evaluate_route_set(
        model,
        benchmark,
        benchmark.suffix_route_queries,
        cue_count=cue_count,
        corruption_rate=corruption_rate,
        query_type="suffix_route",
    )
    suffix_total = max(1, int(suffix["composition_total_suffix_route"]))
    seen_total = max(1, int(seen["composition_total_seen_route"]))
    return {
        "experiment_name": EXPERIMENT_NAME,
        "analysis_id": ANALYSIS_ID,
        "schema_version": SCHEMA_VERSION,
        "phase": phase,
        "seed": benchmark.seed,
        "world_count": benchmark.world_count,
        "route_length": benchmark.route_length,
        "routes_per_world": benchmark.routes_per_world,
        "modes": benchmark.modes,
        "node_count": benchmark.node_count,
        "total_transitions": benchmark.total_transitions,
        "variant": model.name,
        "variant_family": model.family,
        "variant_description": model.description,
        "is_oracle_baseline": bool(model.is_oracle_baseline),
        "cue_count": cue_count,
        "corruption_rate": corruption_rate,
        "context_slots": model.context_slots if model.context_slots is not None else np.nan,
        "capacity_used": model.capacity_used,
        "hash_collisions": model.hash_collisions,
        "composition_accuracy_seen_route": seen["composition_accuracy_seen_route"],
        "composition_correct_seen_route": seen["composition_correct_seen_route"],
        "composition_total_seen_route": seen_total,
        "composition_accuracy_suffix_route": suffix["composition_accuracy_suffix_route"],
        "composition_correct_suffix_route": suffix["composition_correct_suffix_route"],
        "composition_total_suffix_route": suffix_total,
        "world_selection_accuracy_seen_route": seen["world_selection_accuracy_seen_route"],
        "world_selection_correct_seen_route": seen["world_selection_correct_seen_route"],
        "world_selection_total_seen_route": seen["world_selection_total_seen_route"],
        "world_selection_accuracy_suffix_route": suffix["world_selection_accuracy_suffix_route"],
        "world_selection_correct_suffix_route": suffix["world_selection_correct_suffix_route"],
        "world_selection_total_suffix_route": suffix["world_selection_total_suffix_route"],
        "route_table_selected_accuracy_seen_route": seen["route_table_selected_accuracy_seen_route"],
        "route_table_selected_accuracy_suffix_route": suffix["route_table_selected_accuracy_suffix_route"],
        "first_step_context_accuracy": seen["first_step_context_accuracy"],
        "first_step_context_correct": seen["first_step_context_correct"],
        "first_step_context_total": seen["first_step_context_total"],
        "mean_world_confidence_seen_route": seen["mean_world_confidence_seen_route"],
        "mean_world_confidence_suffix_route": suffix["mean_world_confidence_suffix_route"],
        "mean_world_margin_seen_route": seen["mean_world_margin_seen_route"],
        "mean_world_margin_suffix_route": suffix["mean_world_margin_suffix_route"],
        "suffix_generalization_gap": seen["composition_accuracy_seen_route"] - suffix["composition_accuracy_suffix_route"],
    }


def mean_ci95(values: Sequence[float]) -> Tuple[float, float, float, float, int]:
    arr = np.asarray([v for v in values if pd.notna(v)], dtype=float)
    n = int(arr.size)
    if n == 0:
        return (np.nan, np.nan, np.nan, np.nan, 0)
    mean = float(np.mean(arr))
    if n <= 1:
        return (mean, 0.0, mean, mean, n)
    std = float(np.std(arr, ddof=1))
    half = 1.96 * std / math.sqrt(n)
    return (mean, std, mean - half, mean + half, n)


def summarize_metrics(metrics: pd.DataFrame) -> pd.DataFrame:
    group_cols = [
        "phase",
        "variant",
        "variant_family",
        "world_count",
        "route_length",
        "cue_count",
        "corruption_rate",
        "context_slots",
    ]
    metric_cols = [
        "composition_accuracy_seen_route",
        "composition_accuracy_suffix_route",
        "world_selection_accuracy_seen_route",
        "world_selection_accuracy_suffix_route",
        "route_table_selected_accuracy_seen_route",
        "route_table_selected_accuracy_suffix_route",
        "first_step_context_accuracy",
        "mean_world_confidence_seen_route",
        "mean_world_confidence_suffix_route",
        "mean_world_margin_seen_route",
        "mean_world_margin_suffix_route",
        "suffix_generalization_gap",
        "capacity_used",
        "hash_collisions",
    ]
    rows: List[Dict[str, Any]] = []
    grouped = metrics.groupby(group_cols, dropna=False, sort=True)
    for key, group in grouped:
        row = dict(zip(group_cols, key))
        row["seed_count"] = int(group["seed"].nunique())
        row["row_count"] = int(len(group))
        for metric in metric_cols:
            mean, std, low, high, n = mean_ci95(group[metric].tolist())
            row[f"{metric}_mean"] = mean
            row[f"{metric}_std"] = std
            row[f"{metric}_ci95_low"] = low
            row[f"{metric}_ci95_high"] = high
            row[f"{metric}_n"] = n
        rows.append(row)
    return pd.DataFrame(rows)


def cohen_d(a: Sequence[float], b: Sequence[float]) -> float:
    aa = np.asarray([x for x in a if pd.notna(x)], dtype=float)
    bb = np.asarray([x for x in b if pd.notna(x)], dtype=float)
    if aa.size == 0 or bb.size == 0:
        return float("nan")
    if aa.size == 1 and bb.size == 1:
        denom = 0.0
    else:
        va = np.var(aa, ddof=1) if aa.size > 1 else 0.0
        vb = np.var(bb, ddof=1) if bb.size > 1 else 0.0
        denom = math.sqrt(((aa.size - 1) * va + (bb.size - 1) * vb) / max(1, aa.size + bb.size - 2))
    diff = float(np.mean(aa) - np.mean(bb))
    if denom == 0.0:
        if diff == 0.0:
            return 0.0
        return math.copysign(float("inf"), diff)
    return diff / denom


def compute_effect_sizes(metrics: pd.DataFrame) -> pd.DataFrame:
    baseline = "exp14_cirm_latent_selector"
    metric_cols = [
        "composition_accuracy_seen_route",
        "composition_accuracy_suffix_route",
        "world_selection_accuracy_seen_route",
        "world_selection_accuracy_suffix_route",
        "first_step_context_accuracy",
        "mean_world_margin_seen_route",
    ]
    rows: List[Dict[str, Any]] = []
    group_cols = ["phase", "world_count", "route_length", "cue_count", "corruption_rate"]
    for key, group in metrics.groupby(group_cols, dropna=False, sort=True):
        base_group = group[group["variant"] == baseline]
        if base_group.empty:
            continue
        for variant, comp in group.groupby("variant"):
            if variant == baseline:
                continue
            for metric in metric_cols:
                base_values = base_group[metric].tolist()
                comp_values = comp[metric].tolist()
                rows.append(
                    {
                        **dict(zip(group_cols, key)),
                        "baseline_variant": baseline,
                        "comparison_variant": variant,
                        "metric": metric,
                        "mean_difference_cirm_minus_comparison": float(np.nanmean(base_values) - np.nanmean(comp_values)),
                        "cohen_d_cirm_minus_comparison": cohen_d(base_values, comp_values),
                        "n_cirm": int(pd.Series(base_values).dropna().shape[0]),
                        "n_comparison": int(pd.Series(comp_values).dropna().shape[0]),
                    }
                )
    return pd.DataFrame(rows)


def plot_metric_vs_corruption(summary: pd.DataFrame, out: Path, metric: str, title: str, ylabel: str) -> None:
    if summary.empty:
        return
    hardest_world = int(summary["world_count"].max())
    hardest_route = int(summary["route_length"].max())
    cue = int(summary["cue_count"].max())
    subset = summary[
        (summary["world_count"] == hardest_world)
        & (summary["route_length"] == hardest_route)
        & (summary["cue_count"] == cue)
    ].copy()
    if subset.empty:
        return
    fig, ax = plt.subplots(figsize=(10, 6))
    for variant, group in subset.groupby("variant", sort=True):
        g = group.sort_values("corruption_rate")
        y = g[f"{metric}_mean"]
        low = g[f"{metric}_ci95_low"]
        high = g[f"{metric}_ci95_high"]
        ax.plot(g["corruption_rate"], y, marker="o", label=variant)
        ax.fill_between(g["corruption_rate"], low, high, alpha=0.12)
    ax.set_title(f"{title}\nworlds={hardest_world}, route_length={hardest_route}, cue_count={cue}")
    ax.set_xlabel("cue corruption rate")
    ax.set_ylabel(ylabel)
    ax.set_ylim(-0.05, 1.05)
    ax.grid(True, alpha=0.25)
    ax.legend(fontsize=7, loc="best")
    fig.tight_layout()
    fig.savefig(out, dpi=160)
    plt.close(fig)


def plot_metric_vs_cues(summary: pd.DataFrame, out: Path, metric: str, title: str, ylabel: str, corruption_rate: float) -> None:
    if summary.empty:
        return
    hardest_world = int(summary["world_count"].max())
    hardest_route = int(summary["route_length"].max())
    available = sorted(float(x) for x in summary["corruption_rate"].dropna().unique())
    chosen = min(available, key=lambda x: abs(x - corruption_rate)) if available else corruption_rate
    subset = summary[
        (summary["world_count"] == hardest_world)
        & (summary["route_length"] == hardest_route)
        & (summary["corruption_rate"] == chosen)
    ].copy()
    if subset.empty:
        return
    fig, ax = plt.subplots(figsize=(10, 6))
    for variant, group in subset.groupby("variant", sort=True):
        g = group.sort_values("cue_count")
        y = g[f"{metric}_mean"]
        low = g[f"{metric}_ci95_low"]
        high = g[f"{metric}_ci95_high"]
        ax.plot(g["cue_count"], y, marker="o", label=variant)
        ax.fill_between(g["cue_count"], low, high, alpha=0.12)
    ax.set_title(f"{title}\nworlds={hardest_world}, route_length={hardest_route}, corruption={chosen}")
    ax.set_xlabel("cue count")
    ax.set_ylabel(ylabel)
    ax.set_ylim(-0.05, 1.05)
    ax.grid(True, alpha=0.25)
    ax.legend(fontsize=7, loc="best")
    fig.tight_layout()
    fig.savefig(out, dpi=160)
    plt.close(fig)


def make_plots(summary: pd.DataFrame, plots_dir: Path) -> List[str]:
    plots_dir.mkdir(parents=True, exist_ok=True)
    paths = [
        plots_dir / "exp14_world_selection_vs_corruption.png",
        plots_dir / "exp14_seen_composition_vs_corruption.png",
        plots_dir / "exp14_suffix_composition_vs_corruption.png",
        plots_dir / "exp14_margin_vs_corruption.png",
        plots_dir / "exp14_cue_count_selection_sensitivity.png",
        plots_dir / "exp14_cue_count_composition_sensitivity.png",
    ]
    plot_metric_vs_corruption(
        summary,
        paths[0],
        "world_selection_accuracy_seen_route",
        "Latent world selection under stochastic context-cue corruption",
        "world selection accuracy",
    )
    plot_metric_vs_corruption(
        summary,
        paths[1],
        "composition_accuracy_seen_route",
        "Seen-route composition after latent context selection",
        "seen-route composition accuracy",
    )
    plot_metric_vs_corruption(
        summary,
        paths[2],
        "composition_accuracy_suffix_route",
        "Suffix-route composition after latent context selection",
        "suffix-route composition accuracy",
    )
    plot_metric_vs_corruption(
        summary,
        paths[3],
        "mean_world_margin_seen_route",
        "World-selection margin under context-cue corruption",
        "mean world-selection margin",
    )
    plot_metric_vs_cues(
        summary,
        paths[4],
        "world_selection_accuracy_seen_route",
        "Cue-count sensitivity for latent world selection",
        "world selection accuracy",
        corruption_rate=0.25,
    )
    plot_metric_vs_cues(
        summary,
        paths[5],
        "composition_accuracy_seen_route",
        "Cue-count sensitivity for seen-route composition",
        "seen-route composition accuracy",
        corruption_rate=0.25,
    )
    return [str(p) for p in paths if p.exists()]


def device_metadata() -> Dict[str, Any]:
    return {
        "python_version": sys.version,
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "cpu_count": os.cpu_count(),
        "numpy_version": np.__version__,
        "pandas_version": pd.__version__,
        "matplotlib_version": matplotlib.__version__,
        "gpu_used": False,
        "gpu_note": "This experiment is symbolic/table-based and runs on CPU; no GPU is required.",
    }


def write_sqlite(db_path: Path, metrics: pd.DataFrame, summary: pd.DataFrame, effects: pd.DataFrame, manifest: Dict[str, Any]) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()
    with sqlite3.connect(db_path) as conn:
        metrics.to_sql("metrics", conn, index=False)
        summary.to_sql("summary", conn, index=False)
        effects.to_sql("effect_sizes", conn, index=False)
        pd.DataFrame([{"manifest_json": json.dumps(manifest, sort_keys=True)}]).to_sql("manifest", conn, index=False)


def write_report(run_dir: Path, manifest: Dict[str, Any], summary: pd.DataFrame) -> None:
    hardest_world = int(summary["world_count"].max())
    hardest_route = int(summary["route_length"].max())
    max_cue = int(summary["cue_count"].max())
    clean = summary[
        (summary["world_count"] == hardest_world)
        & (summary["route_length"] == hardest_route)
        & (summary["cue_count"] == max_cue)
        & (summary["corruption_rate"] == 0.0)
    ]
    corrupt_rate = max(float(x) for x in summary["corruption_rate"].dropna().unique())
    corrupt = summary[
        (summary["world_count"] == hardest_world)
        & (summary["route_length"] == hardest_route)
        & (summary["cue_count"] == max_cue)
        & (summary["corruption_rate"] == corrupt_rate)
    ]

    def metric_for(df: pd.DataFrame, variant: str, metric: str) -> float:
        row = df[df["variant"] == variant]
        if row.empty:
            return float("nan")
        return float(row.iloc[0][f"{metric}_mean"])

    lines = [
        "# Experiment 14 Report: Latent Context Inference",
        "",
        "## Run identity",
        "",
        f"- Experiment: `{EXPERIMENT_NAME}`",
        f"- Run ID: `{manifest['run_id']}`",
        f"- Profile: `{manifest['profile']}`",
        f"- Seeds: `{manifest['config']['seeds']}`",
        f"- World counts: `{manifest['config']['world_counts']}`",
        f"- Route lengths: `{manifest['config']['route_lengths']}`",
        f"- Cue counts: `{manifest['config']['cue_counts']}`",
        f"- Corruption rates: `{manifest['config']['corruption_rates']}`",
        f"- Metrics rows: `{manifest['row_counts']['metrics_rows']}`",
        f"- SQLite DB: `{manifest['artifact_paths'].get('sqlite_db', 'not written')}`",
        "",
        "## Executive summary",
        "",
        "This run removes the oracle world label used by the clean context-gated lookup baseline and asks each selector to infer the active world from partial transition cues before route composition.",
        "",
        f"At the hardest clean setting available in this run (worlds={hardest_world}, route_length={hardest_route}, cue_count={max_cue}):",
        f"- CIRM latent selector world-selection accuracy: {metric_for(clean, 'exp14_cirm_latent_selector', 'world_selection_accuracy_seen_route'):.4f}.",
        f"- CIRM latent selector seen-route composition accuracy: {metric_for(clean, 'exp14_cirm_latent_selector', 'composition_accuracy_seen_route'):.4f}.",
        f"- Oracle context-gated table seen-route composition accuracy: {metric_for(clean, 'baseline_oracle_context_gated_table', 'composition_accuracy_seen_route'):.4f}.",
        f"- Shared no-context table seen-route composition accuracy: {metric_for(clean, 'baseline_shared_no_context_table', 'composition_accuracy_seen_route'):.4f}.",
        f"- Route endpoint memorizer suffix-route composition accuracy: {metric_for(clean, 'baseline_route_endpoint_memorizer_with_latent_selector', 'composition_accuracy_suffix_route'):.4f}.",
        "",
        f"At the same hardest setting with the highest corruption rate ({corrupt_rate}):",
        f"- CIRM latent selector world-selection accuracy: {metric_for(corrupt, 'exp14_cirm_latent_selector', 'world_selection_accuracy_seen_route'):.4f}.",
        f"- CIRM latent selector seen-route composition accuracy: {metric_for(corrupt, 'exp14_cirm_latent_selector', 'composition_accuracy_seen_route'):.4f}.",
        "",
        "## Interpretation guardrails",
        "",
        "- This is still a symbolic route-memory benchmark, not end-to-end perception or solved continual learning.",
        "- The oracle context-gated table remains an upper bound, not a fair latent-selector baseline.",
        "- Clean cue success supports context selection from observed transition evidence, not autonomous discovery of worlds from raw sensory streams.",
        "- Corrupted cue collapse should be framed as context-evidence sensitivity, not generic robustness failure unless paired with richer noise models.",
        "",
        "## Generated plots",
        "",
    ]
    for plot in manifest["artifact_paths"]["plots"]:
        lines.append(f"- `{plot}`")
    lines.extend(
        [
            "",
            "## Source artifacts",
            "",
            "- `exp14_metrics.csv`",
            "- `metrics.csv`",
            "- `exp14_summary.csv`",
            "- `exp14_effect_sizes.csv`",
            "- `run_manifest.json`",
            "- `progress.jsonl`",
        ]
    )
    text = "\n".join(lines) + "\n"
    (run_dir / "exp14_report.md").write_text(text, encoding="utf-8")
    (run_dir / "experiment_report.md").write_text(text, encoding="utf-8")


def run_experiment(profile: str, *, output_root: Path, runs_dir: Path, no_sqlite: bool, progress_every: Optional[int]) -> Path:
    cfg = make_config(profile, progress_every=progress_every)
    run_id = f"{ANALYSIS_ID}_{cfg.profile}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    run_dir = output_root / run_id
    plots_dir = run_dir / "plots"
    run_dir.mkdir(parents=True, exist_ok=True)
    plots_dir.mkdir(parents=True, exist_ok=True)

    phase = "latent_context_inference"
    models_count = 6 + len(cfg.hash_slot_divisors)
    total_units = len(cfg.seeds) * len(cfg.world_counts) * len(cfg.route_lengths) * len(cfg.cue_counts) * len(cfg.corruption_rates) * models_count
    progress = ProgressLogger(run_dir / "progress.jsonl", total_units, progress_every=cfg.progress_every)
    progress.event("run_start", profile=cfg.profile, run_id=run_id, config=dataclasses.asdict(cfg))
    print(f"[{EXPERIMENT_NAME}] Run ID: {run_id}")
    print(f"[{EXPERIMENT_NAME}] Output: {run_dir}")
    print(f"[{EXPERIMENT_NAME}] Planned units: {total_units}")
    progress.phase_start(phase, total_units, profile=cfg.profile)

    rows: List[MetricRow] = []
    for seed in cfg.seeds:
        for world_count in cfg.world_counts:
            for route_length in cfg.route_lengths:
                benchmark = make_benchmark(seed, world_count, route_length, cfg.routes_per_world, cfg.modes)
                models = build_models(cfg.hash_slot_divisors)
                for model in models:
                    model.fit(benchmark)
                for cue_count in cfg.cue_counts:
                    for corruption_rate in cfg.corruption_rates:
                        for model in models:
                            row = evaluate_model_condition(
                                model,
                                benchmark,
                                cue_count=int(cue_count),
                                corruption_rate=float(corruption_rate),
                                phase=phase,
                            )
                            rows.append(row)
                            progress.unit_done(
                                phase=phase,
                                seed=seed,
                                world_count=world_count,
                                route_length=route_length,
                                cue_count=cue_count,
                                corruption_rate=corruption_rate,
                                variant=model.name,
                            )

    metrics = pd.DataFrame(rows)
    summary = summarize_metrics(metrics)
    effects = compute_effect_sizes(metrics)

    metrics_path = run_dir / "exp14_metrics.csv"
    summary_path = run_dir / "exp14_summary.csv"
    effects_path = run_dir / "exp14_effect_sizes.csv"
    metrics.to_csv(metrics_path, index=False)
    shutil.copyfile(metrics_path, run_dir / "metrics.csv")
    summary.to_csv(summary_path, index=False)
    effects.to_csv(effects_path, index=False)

    plot_paths_abs = make_plots(summary, plots_dir)
    relative_plots = [str(Path("analysis") / run_id / "plots" / Path(p).name) for p in plot_paths_abs]

    manifest: Dict[str, Any] = {
        "experiment_name": EXPERIMENT_NAME,
        "analysis_id": ANALYSIS_ID,
        "schema_version": SCHEMA_VERSION,
        "run_id": run_id,
        "profile": cfg.profile,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "config": dataclasses.asdict(cfg),
        "row_counts": {
            "metrics_rows": int(len(metrics)),
            "summary_rows": int(len(summary)),
            "effect_size_rows": int(len(effects)),
        },
        "artifact_paths": {
            "analysis_dir": str(Path("analysis") / run_id),
            "metrics_csv": str(Path("analysis") / run_id / "exp14_metrics.csv"),
            "summary_csv": str(Path("analysis") / run_id / "exp14_summary.csv"),
            "effect_sizes_csv": str(Path("analysis") / run_id / "exp14_effect_sizes.csv"),
            "plots": relative_plots,
            "runs_dir": str(runs_dir),
        },
        "device": device_metadata(),
        "scientific_guardrails": [
            "Clean cue success is latent context selection from symbolic transition evidence, not raw sensory inference.",
            "The oracle context-gated table is an upper bound, not a fair non-oracle selector.",
            "Corruption-rate sweeps test cue-evidence sensitivity, not all forms of context noise.",
        ],
    }

    if not no_sqlite:
        db_path = runs_dir / f"{run_id}.sqlite3"
        manifest["artifact_paths"]["sqlite_db"] = str(Path("runs") / f"{run_id}.sqlite3")
        write_sqlite(db_path, metrics, summary, effects, manifest)
    else:
        manifest["artifact_paths"]["sqlite_db"] = None

    (run_dir / "run_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    (run_dir / "exp14_config.json").write_text(json.dumps(dataclasses.asdict(cfg), indent=2, sort_keys=True), encoding="utf-8")
    write_report(run_dir, manifest, summary)
    progress.finish(run_id=run_id, metrics_rows=len(metrics), summary_rows=len(summary), effect_size_rows=len(effects))
    return run_dir


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Experiment 14 latent context inference.")
    parser.add_argument("--profile", default="smoke", choices=("smoke", "validation", "full"), help="Run profile.")
    parser.add_argument("--analysis-root", default="analysis", help="Directory for analysis outputs.")
    parser.add_argument("--runs-dir", default="runs", help="Directory for SQLite run records.")
    parser.add_argument("--no-sqlite", action="store_true", help="Skip SQLite database creation.")
    parser.add_argument("--progress-every", type=int, default=None, help="Override console progress interval.")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    output_root = Path(args.analysis_root)
    runs_dir = Path(args.runs_dir)
    try:
        run_dir = run_experiment(
            args.profile,
            output_root=output_root,
            runs_dir=runs_dir,
            no_sqlite=bool(args.no_sqlite),
            progress_every=args.progress_every,
        )
    except Exception as exc:
        print(f"[{EXPERIMENT_NAME}] ERROR: {exc}", file=sys.stderr)
        raise
    print(f"[{EXPERIMENT_NAME}] Wrote artifacts to {run_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
