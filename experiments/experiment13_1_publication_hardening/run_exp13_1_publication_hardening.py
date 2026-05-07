#!/usr/bin/env python3
"""Experiment 13.1: publication-hardening route-field memory audit.

This is a self-contained successor to Experiment 13. It keeps the same mechanistic
question but separates controls that were previously easy to conflate: recurrence at
execution vs throughout training, live plasticity vs formed structure, clean vs
corrupted context, targeted route-field lesions vs matched random lesions, and local
vs global plasticity budgets.

The script is intentionally deterministic and table based. It writes analysis
artifacts when executed, but importing this file does not run the experiment.
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import math
import random
import shutil
import sqlite3
import time
from datetime import datetime, timezone
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


EXPERIMENT_NAME = "exp13_1_publication_hardening"
ANALYSIS_ID = "exp13_1"
NO_CONTEXT = -1
NO_LESION = "none"
NO_FREEZE = "none"
SCHEMA_VERSION = "exp13_1_metrics_v1"

EdgeKey = Tuple[int, int, int, int]  # context slot, source node, mode slot, target node
TransitionKey = Tuple[int, int, int]  # world, source node, mode


@dataclass(frozen=True)
class Variant:
    name: str
    description: str
    structural_plasticity: bool = True
    recurrence_training: bool = True
    recurrence_evaluation: bool = True
    world_context: bool = True
    context_binding: bool = True
    world_gated_plasticity: bool = True
    consolidation_strength: float = 0.25
    context_binding_strength: float = 1.0
    learning_rate: float = 1.0
    comparison_note: str = ""

    @property
    def recurrence_setting(self) -> str:
        if self.recurrence_training and self.recurrence_evaluation:
            return "train_and_eval"
        if self.recurrence_training and not self.recurrence_evaluation:
            return "eval_disabled_only"
        if not self.recurrence_training and not self.recurrence_evaluation:
            return "disabled_throughout"
        return "training_disabled_eval_enabled"

    @property
    def plasticity_setting(self) -> str:
        return "live_structural" if self.structural_plasticity else "no_structural_plasticity"

    @property
    def consolidation_setting(self) -> str:
        if self.consolidation_strength <= 0.0:
            return "none"
        if self.consolidation_strength < 0.18:
            return "weak"
        if self.consolidation_strength > 0.55:
            return "aggressive"
        return "default"

    def to_metadata(self) -> Dict[str, Any]:
        payload = dataclasses.asdict(self)
        payload["experiment_name"] = EXPERIMENT_NAME
        payload["recurrence_setting"] = self.recurrence_setting
        payload["plasticity_setting"] = self.plasticity_setting
        payload["consolidation_setting"] = self.consolidation_setting
        return payload


FULL_VARIANT = Variant(
    name="exp13_1_full_model",
    description=(
        "Structural plasticity, recurrence, world context, mode/context binding, "
        "world-gated plasticity, and default consolidation."
    ),
    comparison_note="Main model for publication-hardening contrasts.",
)


VARIANTS: Dict[str, Variant] = {
    FULL_VARIANT.name: FULL_VARIANT,
    "exp13_1_no_recurrence_at_eval": dataclasses.replace(
        FULL_VARIANT,
        name="exp13_1_no_recurrence_at_eval",
        description="Full training, then recurrent traversal disabled only at evaluation.",
        recurrence_evaluation=False,
        comparison_note="Compare to full model for execution dependence after route-field formation.",
    ),
    "exp13_1_no_recurrence_throughout": dataclasses.replace(
        FULL_VARIANT,
        name="exp13_1_no_recurrence_throughout",
        description="Recurrence disabled throughout training metadata and evaluation.",
        recurrence_training=False,
        recurrence_evaluation=False,
        comparison_note=(
            "Tests broader training-and-execution dependence. In this local one-step "
            "update harness, formation is expected to be less affected than execution."
        ),
    ),
    "exp13_1_no_structural_plasticity": dataclasses.replace(
        FULL_VARIANT,
        name="exp13_1_no_structural_plasticity",
        description="No structural route-field updates are stored.",
        structural_plasticity=False,
        consolidation_strength=0.0,
        comparison_note="Tests whether route-memory behavior requires plastic structure.",
    ),
    "exp13_1_no_context_binding": dataclasses.replace(
        FULL_VARIANT,
        name="exp13_1_no_context_binding",
        description=(
            "World context remains available, but mode/context binding is collapsed into "
            "an explicit unbound mode slot."
        ),
        context_binding=False,
        context_binding_strength=0.25,
        comparison_note="Tests route collisions when binding is weakened without out-of-bounds mode indexing.",
    ),
    "exp13_1_no_world_gated_plasticity": dataclasses.replace(
        FULL_VARIANT,
        name="exp13_1_no_world_gated_plasticity",
        description="Plastic updates are not given the active-world selectivity advantage.",
        world_gated_plasticity=False,
        context_binding_strength=0.9,
        comparison_note="Tests world-gated plasticity while preserving other full-model mechanisms.",
    ),
    "exp13_1_no_consolidation": dataclasses.replace(
        FULL_VARIANT,
        name="exp13_1_no_consolidation",
        description="Full mechanism without consolidation.",
        consolidation_strength=0.0,
        comparison_note="Budget/consolidation dose-response control.",
    ),
    "exp13_1_weak_consolidation": dataclasses.replace(
        FULL_VARIANT,
        name="exp13_1_weak_consolidation",
        description="Full mechanism with weak consolidation.",
        consolidation_strength=0.10,
        comparison_note="Budget/consolidation dose-response control.",
    ),
    "exp13_1_aggressive_consolidation": dataclasses.replace(
        FULL_VARIANT,
        name="exp13_1_aggressive_consolidation",
        description="Full mechanism with aggressive consolidation.",
        consolidation_strength=0.75,
        context_binding_strength=1.10,
        comparison_note="Budget/consolidation dose-response control.",
    ),
}


CORE_VARIANTS: Tuple[str, ...] = (
    "exp13_1_full_model",
    "exp13_1_no_recurrence_at_eval",
    "exp13_1_no_recurrence_throughout",
    "exp13_1_no_structural_plasticity",
    "exp13_1_no_context_binding",
    "exp13_1_no_world_gated_plasticity",
)

CONSOLIDATION_VARIANTS: Tuple[str, ...] = (
    "exp13_1_full_model",
    "exp13_1_no_consolidation",
    "exp13_1_weak_consolidation",
    "exp13_1_aggressive_consolidation",
)


@dataclass(frozen=True)
class Config:
    profile: str
    seeds: Tuple[int, ...]
    nodes: int
    modes: int
    world_count: int
    routes_per_world: int
    route_lengths: Tuple[int, ...]
    composition_route_length: int
    context_levels: Tuple[float, ...]
    budget_world_count: int
    budget_route_length: int
    global_budget_ratios: Tuple[float, ...]
    local_budget_ratios: Tuple[float, ...]
    freeze_world_count: int
    lesion_world_count: int
    lesion_route_length: int
    lesion_fraction: float
    structure_audit_world_count: int
    structure_audit_route_length: int


def make_config(profile: str) -> Config:
    if profile == "smoke":
        return Config(
            profile=profile,
            seeds=(0, 1),
            nodes=16,
            modes=3,
            world_count=6,
            routes_per_world=12,
            route_lengths=(1, 3, 5),
            composition_route_length=5,
            context_levels=(0.0, 0.35, 0.70),
            budget_world_count=8,
            budget_route_length=5,
            global_budget_ratios=(0.50, 1.00),
            local_budget_ratios=(0.50, 1.00),
            freeze_world_count=4,
            lesion_world_count=6,
            lesion_route_length=5,
            lesion_fraction=0.12,
            structure_audit_world_count=6,
            structure_audit_route_length=5,
        )
    if profile == "standard":
        return Config(
            profile=profile,
            seeds=tuple(range(5)),
            nodes=32,
            modes=3,
            world_count=16,
            routes_per_world=36,
            route_lengths=(1, 4, 8, 12),
            composition_route_length=8,
            context_levels=(0.0, 0.10, 0.25, 0.50, 0.75, 0.90),
            budget_world_count=24,
            budget_route_length=8,
            global_budget_ratios=(0.375, 0.50, 0.75, 1.00),
            local_budget_ratios=(0.375, 0.50, 0.75, 1.00),
            freeze_world_count=8,
            lesion_world_count=16,
            lesion_route_length=8,
            lesion_fraction=0.08,
            structure_audit_world_count=16,
            structure_audit_route_length=8,
        )
    if profile == "full":
        return Config(
            profile=profile,
            seeds=tuple(range(20)),
            nodes=32,
            modes=3,
            world_count=32,
            routes_per_world=72,
            route_lengths=(1, 2, 4, 8, 12, 16),
            composition_route_length=12,
            context_levels=(0.0, 0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.99),
            budget_world_count=48,
            budget_route_length=12,
            global_budget_ratios=(0.25, 0.375, 0.50, 0.75, 1.00, 1.25),
            local_budget_ratios=(0.25, 0.375, 0.50, 0.75, 1.00),
            freeze_world_count=12,
            lesion_world_count=24,
            lesion_route_length=12,
            lesion_fraction=0.08,
            structure_audit_world_count=24,
            structure_audit_route_length=12,
        )
    raise ValueError(f"Unknown profile: {profile}")


def context_corruption_unit_count(config: Config) -> int:
    clean = 1
    corrupted_levels = len([level for level in config.context_levels if level > 0.0])
    return clean + 3 * corrupted_levels


def estimate_phase_units(config: Config) -> Dict[str, int]:
    return {
        "variant_comparison": len(config.seeds) * len(CORE_VARIANTS) * len(config.route_lengths),
        "structure_audit": len(config.seeds) * len(CORE_VARIANTS),
        "freeze_plasticity": len(config.seeds) * 4,
        "context_corruption": len(config.seeds) * 4 * context_corruption_unit_count(config),
        "lesion_test": len(config.seeds) * 4,
        "budget_consolidation": len(config.seeds) * len(CONSOLIDATION_VARIANTS) * 3,
    }


def estimate_total_units(config: Config) -> int:
    return int(sum(estimate_phase_units(config).values()))


def make_run_id(profile: str) -> str:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{ANALYSIS_ID}_{profile}_{stamp}"


class ProgressLogger:
    """Console + JSONL progress logger with rate and ETA estimates.

    The experiment is row/evaluation oriented. Each completed evaluation row is treated
    as one progress unit, which gives a stable ETA without over-logging every sampled
    route inside an evaluation.
    """

    def __init__(self, path: Path, total_units: int = 0, progress_every: int = 10):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._fh = self.path.open("w", encoding="utf-8")
        self.total_units = int(total_units)
        self.progress_every = max(1, int(progress_every))
        self.started = time.time()
        self.completed_units = 0
        self.phase = "not_started"
        self.phase_total = 0
        self.phase_completed = 0

    @staticmethod
    def _fmt_seconds(seconds: Optional[float]) -> str:
        if seconds is None or not math.isfinite(seconds) or seconds < 0:
            return "unknown"
        seconds = int(seconds)
        hours, rem = divmod(seconds, 3600)
        minutes, sec = divmod(rem, 60)
        if hours:
            return f"{hours}h {minutes}m {sec}s"
        if minutes:
            return f"{minutes}m {sec}s"
        return f"{sec}s"

    def _payload_with_progress(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        elapsed = max(1e-9, time.time() - self.started)
        rate = self.completed_units / elapsed
        remaining = max(0, self.total_units - self.completed_units) if self.total_units else 0
        eta = remaining / rate if rate > 0 and self.total_units else None
        percent = (100.0 * self.completed_units / self.total_units) if self.total_units else None
        payload.setdefault("time", time.time())
        payload.setdefault("iso_time", datetime.now(timezone.utc).isoformat())
        payload.setdefault("experiment_name", EXPERIMENT_NAME)
        payload.setdefault("completed_units", self.completed_units)
        payload.setdefault("total_units", self.total_units)
        payload.setdefault("phase", self.phase)
        payload.setdefault("phase_completed", self.phase_completed)
        payload.setdefault("phase_total", self.phase_total)
        payload.setdefault("elapsed_seconds", elapsed)
        payload.setdefault("rate_units_per_second", rate)
        payload.setdefault("eta_seconds", eta)
        payload.setdefault("percent_complete", percent)
        return payload

    def write(self, **payload: Any) -> None:
        payload = self._payload_with_progress(dict(payload))
        self._fh.write(json.dumps(payload, sort_keys=True) + "\n")
        self._fh.flush()
        msg = payload.get("message") or payload.get("phase") or "progress"
        if payload.get("event") in {"phase_start", "phase_complete", "run_start", "run_complete", "artifact"}:
            eta = self._fmt_seconds(payload.get("eta_seconds"))
            pct = payload.get("percent_complete")
            pct_text = f"{pct:5.1f}%" if pct is not None else "  n/a"
            print(f"[{time.strftime('%H:%M:%S')}] {msg} | {pct_text} | ETA {eta}", flush=True)
        else:
            print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)

    def start_phase(self, phase: str, total_units: int) -> None:
        self.phase = phase
        self.phase_total = int(total_units)
        self.phase_completed = 0
        self.write(event="phase_start", message=f"Starting {phase}")

    def step(self, detail: str = "") -> None:
        self.completed_units += 1
        self.phase_completed += 1
        should_print = (
            self.completed_units == 1
            or self.completed_units == self.total_units
            or self.phase_completed == self.phase_total
            or self.phase_completed % self.progress_every == 0
        )
        payload: Dict[str, Any] = {"event": "progress", "message": f"{self.phase}: {self.phase_completed}/{self.phase_total}"}
        if detail:
            payload["detail"] = detail
        payload = self._payload_with_progress(payload)
        self._fh.write(json.dumps(payload, sort_keys=True) + "\n")
        self._fh.flush()
        if should_print:
            eta = self._fmt_seconds(payload.get("eta_seconds"))
            pct = payload.get("percent_complete")
            pct_text = f"{pct:5.1f}%" if pct is not None else "  n/a"
            print(
                f"[{time.strftime('%H:%M:%S')}] {self.phase}: {self.phase_completed}/{self.phase_total} "
                f"(overall {self.completed_units}/{self.total_units}, {pct_text}, ETA {eta})",
                flush=True,
            )

    def complete_phase(self, rows: int) -> None:
        self.write(event="phase_complete", message=f"Completed {self.phase}", rows=rows)

    def close(self) -> None:
        self._fh.close()


class WorldTransitions:
    """Random incompatible route worlds over a shared node/mode substrate."""

    def __init__(self, world_count: int, nodes: int, modes: int, seed: int):
        self.world_count = int(world_count)
        self.nodes = int(nodes)
        self.modes = int(modes)
        self.seed = int(seed)
        rng = np.random.default_rng(seed + 1009 * world_count + 9173 * nodes + 431 * modes)
        self.transitions = rng.integers(0, nodes, size=(world_count, nodes, modes), endpoint=False)
        for w in range(world_count):
            for n in range(nodes):
                for m in range(modes):
                    if self.transitions[w, n, m] == n:
                        self.transitions[w, n, m] = (n + m + w + 1) % nodes

    def target(self, world: int, node: int, mode: int) -> int:
        return int(self.transitions[int(world), int(node), int(mode)])

    def final_after_modes(self, world: int, start_node: int, modes: Sequence[int]) -> int:
        node = int(start_node)
        for mode in modes:
            node = self.target(world, node, int(mode))
        return node

    def all_transition_keys(self, worlds: Optional[Iterable[int]] = None) -> Iterable[TransitionKey]:
        eval_worlds = range(self.world_count) if worlds is None else worlds
        for w in eval_worlds:
            for n in range(self.nodes):
                for m in range(self.modes):
                    yield (int(w), n, m)


@dataclass
class QueryContext:
    condition: str = "clean"
    level: float = 0.0
    wrong_world: Optional[int] = None

    @property
    def is_clean(self) -> bool:
        return self.condition == "clean" or self.level <= 0.0


@dataclass
class Edge:
    key: EdgeKey
    score: float
    created_step: int
    last_update_step: int
    updates: int = 1


class RouteMemoryModel:
    """Inspectable route-field structure with explicit context and mode slots."""

    def __init__(
        self,
        variant: Variant,
        world_count: int,
        nodes: int,
        modes: int,
        global_edge_budget: Optional[int],
        local_edge_budget_per_world: Optional[int],
        rng: random.Random,
    ):
        self.variant = variant
        self.world_count = int(world_count)
        self.nodes = int(nodes)
        self.modes = int(modes)
        # Guard inherited from the Exp11/Exp13 lineage: when context/mode binding is
        # disabled, _mode_slot returns the extra slot `modes`, so valid slots are
        # [0, modes]. This prevents the historical n_modes allocation bug.
        self.mode_slot_count = self.modes + 1
        self.global_edge_budget = global_edge_budget
        self.local_edge_budget_per_world = local_edge_budget_per_world
        self.rng = rng
        self.edges: Dict[EdgeKey, Edge] = {}
        self.step = 0
        self.plasticity_frozen = False
        self._best_cache: Optional[Dict[Tuple[int, int, int], Tuple[int, float, float, bool]]] = None

    def clone(self) -> "RouteMemoryModel":
        clone = RouteMemoryModel(
            variant=self.variant,
            world_count=self.world_count,
            nodes=self.nodes,
            modes=self.modes,
            global_edge_budget=self.global_edge_budget,
            local_edge_budget_per_world=self.local_edge_budget_per_world,
            rng=random.Random(0),
        )
        clone.edges = {key: dataclasses.replace(edge) for key, edge in self.edges.items()}
        clone.step = self.step
        clone.plasticity_frozen = self.plasticity_frozen
        clone._best_cache = None
        return clone

    def freeze_plasticity(self) -> None:
        self.plasticity_frozen = True

    def _context_key(self, world: int) -> int:
        return int(world) if self.variant.world_context else NO_CONTEXT

    def _mode_slot(self, mode: int) -> int:
        slot = self.modes if not self.variant.context_binding else int(mode)
        if slot < 0 or slot >= self.mode_slot_count:
            raise IndexError(
                f"Invalid mode slot {slot}; mode_slot_count={self.mode_slot_count}, "
                f"mode={mode}, context_binding={self.variant.context_binding}"
            )
        return slot

    def train_world(
        self,
        transitions: WorldTransitions,
        world: int,
        withheld: Optional[set[TransitionKey]] = None,
    ) -> None:
        withheld = withheld or set()
        if self.plasticity_frozen or not self.variant.structural_plasticity:
            self.step += transitions.nodes * transitions.modes
            self._best_cache = None
            return

        for node in range(transitions.nodes):
            for mode in range(transitions.modes):
                tk = (int(world), node, mode)
                if tk in withheld:
                    continue
                target = transitions.target(world, node, mode)
                ctx = self._context_key(world)
                mslot = self._mode_slot(mode)
                key = (ctx, node, mslot, target)
                self.step += 1
                delta = self.variant.learning_rate
                if self.variant.world_gated_plasticity and ctx != NO_CONTEXT:
                    delta *= 1.08
                if key in self.edges:
                    edge = self.edges[key]
                    edge.score += delta
                    edge.updates += 1
                    edge.last_update_step = self.step
                else:
                    self.edges[key] = Edge(
                        key=key,
                        score=delta,
                        created_step=self.step,
                        last_update_step=self.step,
                    )

        self._consolidate_existing_edges(current_world=int(world))
        self._prune_if_needed()
        self._best_cache = None

    def _consolidate_existing_edges(self, current_world: int) -> None:
        strength = max(0.0, self.variant.consolidation_strength)
        if strength <= 0.0 or not self.edges:
            return
        for edge in self.edges.values():
            edge_world = edge.key[0]
            if edge_world == NO_CONTEXT:
                age_worlds = 0
            else:
                age_worlds = max(0, current_world - edge_world)
            age_bonus = min(1.0, age_worlds / max(1, self.world_count - 1))
            edge.score = min(25.0, edge.score * (1.0 + 0.06 * strength + 0.16 * strength * age_bonus))

    def consolidate_now(self) -> None:
        if self.variant.consolidation_strength <= 0.0:
            return
        self._consolidate_existing_edges(current_world=self.world_count - 1)
        self._prune_if_needed()
        self._best_cache = None

    def _edge_priority(self, edge: Edge) -> Tuple[float, float]:
        recency = edge.last_update_step / max(1, self.step)
        jitter = self.rng.random() * 1e-6
        return (edge.score + 0.004 * recency + jitter, recency)

    def _prune_if_needed(self) -> None:
        if self.local_edge_budget_per_world is not None and self.local_edge_budget_per_world >= 0:
            grouped: Dict[int, List[Edge]] = defaultdict(list)
            for edge in self.edges.values():
                grouped[edge.key[0]].append(edge)
            remove: List[EdgeKey] = []
            for ctx, group in grouped.items():
                if ctx == NO_CONTEXT:
                    continue
                excess = len(group) - self.local_edge_budget_per_world
                if excess > 0:
                    remove.extend(edge.key for edge in sorted(group, key=self._edge_priority)[:excess])
            for key in remove:
                self.edges.pop(key, None)

        if self.global_edge_budget is not None and self.global_edge_budget >= 0:
            excess = len(self.edges) - self.global_edge_budget
            if excess > 0:
                for edge in sorted(self.edges.values(), key=self._edge_priority)[:excess]:
                    self.edges.pop(edge.key, None)
        self._best_cache = None

    def context_scores(self, true_world: int, qctx: QueryContext) -> np.ndarray:
        if not self.variant.world_context:
            return np.ones(self.world_count, dtype=float) * 0.5

        strength = max(0.0, self.variant.context_binding_strength)
        scores = np.zeros(self.world_count, dtype=float)
        if qctx.is_clean:
            scores[int(true_world)] = strength
            return scores

        level = float(np.clip(qctx.level, 0.0, 1.0))
        wrong_world = qctx.wrong_world
        if wrong_world is None or wrong_world == true_world:
            wrong_world = (int(true_world) + 1) % self.world_count

        if qctx.condition == "context_dropout":
            scores[int(true_world)] = strength * (1.0 - level)
            if self.world_count > 1:
                scores += strength * level / self.world_count
        elif qctx.condition == "context_bleed":
            scores[int(true_world)] = strength * (1.0 - 0.50 * level)
            wrong_mass = strength * level
            if self.world_count > 1:
                for w in range(self.world_count):
                    if w != true_world:
                        scores[w] = wrong_mass / (self.world_count - 1)
        elif qctx.condition == "wrong_world_injection":
            scores[int(true_world)] = strength * (1.0 - level)
            scores[int(wrong_world)] = strength * level
        else:
            raise ValueError(f"Unknown context condition: {qctx.condition}")
        return scores

    def select_world(self, true_world: int, qctx: QueryContext) -> Dict[str, float]:
        if not self.variant.world_context:
            return {
                "selected_world": float(NO_CONTEXT),
                "world_margin": 0.0,
                "correct_world_activation": 0.5,
                "wrong_world_activation": 0.5,
                "top1_world_accuracy": 0.0,
                "context_confusion": 1.0,
            }

        scores = self.context_scores(true_world, qctx)
        max_score = float(np.max(scores))
        candidates = np.flatnonzero(np.isclose(scores, max_score))
        if len(candidates) == 1:
            selected = int(candidates[0])
        else:
            selected = int(candidates[self.rng.randrange(len(candidates))])
        wrong = float(np.max(np.delete(scores, int(true_world)))) if self.world_count > 1 else 0.0
        correct = float(scores[int(true_world)])
        return {
            "selected_world": float(selected),
            "world_margin": float(correct - wrong),
            "correct_world_activation": correct,
            "wrong_world_activation": wrong,
            "top1_world_accuracy": 1.0 if selected == int(true_world) else 0.0,
            "context_confusion": 1.0 if wrong >= correct and self.world_count > 1 else 0.0,
        }

    def _fallback_target(self, node: int, mode: int, selected_world: int) -> int:
        return int((node * 17 + mode * 31 + (selected_world + 5) * 13 + 7) % self.nodes)

    def _ensure_best_cache(self) -> None:
        if self._best_cache is not None:
            return
        grouped: Dict[Tuple[int, int, int], List[Tuple[int, float]]] = defaultdict(list)
        for edge in self.edges.values():
            ctx, node, mslot, target = edge.key
            grouped[(ctx, node, mslot)].append((target, edge.score))
        cache: Dict[Tuple[int, int, int], Tuple[int, float, float, bool]] = {}
        for key, candidates in grouped.items():
            candidates.sort(key=lambda item: (item[1], item[0]), reverse=True)
            pred, best = candidates[0]
            second = candidates[1][1] if len(candidates) > 1 else 0.0
            cache[key] = (int(pred), float(best), float(best - second), True)
        self._best_cache = cache

    def edge_score(self, ctx: int, node: int, mslot: int, target: int) -> float:
        edge = self.edges.get((int(ctx), int(node), int(mslot), int(target)))
        return float(edge.score) if edge else 0.0

    def predict_one_step(self, selected_world: int, node: int, mode: int) -> Tuple[int, float, float, bool]:
        if not self.variant.structural_plasticity:
            return self._fallback_target(node, mode, selected_world), 0.0, 0.0, False
        ctx = selected_world if self.variant.world_context else NO_CONTEXT
        mslot = self._mode_slot(mode)
        self._ensure_best_cache()
        assert self._best_cache is not None
        cached = self._best_cache.get((ctx, int(node), mslot))
        if cached is None:
            return self._fallback_target(node, mode, selected_world), 0.0, 0.0, False
        return cached

    def predict_route(self, true_world: int, start_node: int, modes: Sequence[int], qctx: QueryContext) -> Dict[str, float]:
        selection = self.select_world(true_world, qctx)
        selected_world = int(selection["selected_world"])
        node = int(start_node)
        used_edges = 0
        edge_scores: List[float] = []
        edge_margins: List[float] = []
        executable_modes = list(modes) if self.variant.recurrence_evaluation else list(modes[:1])
        for mode in executable_modes:
            node, score, margin, found = self.predict_one_step(selected_world, node, int(mode))
            edge_scores.append(score)
            edge_margins.append(margin)
            used_edges += int(found)
        return {
            "pred_node": float(node),
            "selected_world": selection["selected_world"],
            "world_margin": selection["world_margin"],
            "correct_world_activation": selection["correct_world_activation"],
            "wrong_world_activation": selection["wrong_world_activation"],
            "top1_world_accuracy": selection["top1_world_accuracy"],
            "context_confusion": selection["context_confusion"],
            "mean_edge_score": float(np.mean(edge_scores)) if edge_scores else 0.0,
            "mean_edge_margin": float(np.mean(edge_margins)) if edge_margins else 0.0,
            "min_edge_margin": float(np.min(edge_margins)) if edge_margins else 0.0,
            "used_edge_fraction": used_edges / max(1, len(modes)),
        }

    def edge_diagnostics(
        self,
        selected_world: int,
        true_world: int,
        node: int,
        mode: int,
        target: int,
    ) -> Dict[str, float]:
        ctx = selected_world if self.variant.world_context else NO_CONTEXT
        true_ctx = self._context_key(true_world)
        mslot = self._mode_slot(mode)
        correct = self.edge_score(ctx, node, mslot, target)
        wrong_route = 0.0
        structural_wrong_world = 0.0
        wrong_mode = 0.0
        for edge in self.edges.values():
            ectx, enode, emode, etarget = edge.key
            if enode != int(node):
                continue
            if ectx == ctx and emode == mslot and etarget != int(target):
                wrong_route = max(wrong_route, float(edge.score))
            if ectx != true_ctx and emode == mslot and etarget == int(target):
                structural_wrong_world = max(structural_wrong_world, float(edge.score))
            if ectx == ctx and emode != mslot and etarget == int(target):
                wrong_mode = max(wrong_mode, float(edge.score))
        route_margin = correct - wrong_route
        world_margin = correct - structural_wrong_world
        mode_margin = correct - wrong_mode
        return {
            "correct_edge_score": correct,
            "route_margin": route_margin,
            "mode_margin": mode_margin,
            "structural_world_margin": world_margin,
            "wrong_route_activation": wrong_route,
            "structural_wrong_world_activation": structural_wrong_world,
            "wrong_mode_activation": wrong_mode,
            "structure_transition_correct": 1.0 if correct > wrong_route and correct > 0.0 else 0.0,
        }

    def critical_edge_key(self, world: int, node: int, mode: int, target: int) -> EdgeKey:
        return (self._context_key(world), int(node), self._mode_slot(mode), int(target))

    def remove_edges(self, keys: Iterable[EdgeKey]) -> int:
        removed = 0
        for key in keys:
            if self.edges.pop(key, None) is not None:
                removed += 1
        self._best_cache = None
        return removed


def build_model(
    transitions: WorldTransitions,
    variant: Variant,
    seed: int,
    train_worlds: Optional[Sequence[int]] = None,
    global_budget_ratio: Optional[float] = 1.0,
    local_budget_ratio: Optional[float] = None,
    withheld: Optional[set[TransitionKey]] = None,
) -> RouteMemoryModel:
    train_worlds = list(range(transitions.world_count)) if train_worlds is None else list(train_worlds)
    full_edge_count = len(train_worlds) * transitions.nodes * transitions.modes
    global_budget = None
    if global_budget_ratio is not None:
        global_budget = max(0, int(math.ceil(global_budget_ratio * full_edge_count)))
    local_budget = None
    if local_budget_ratio is not None:
        local_budget = max(0, int(math.ceil(local_budget_ratio * transitions.nodes * transitions.modes)))
    model = RouteMemoryModel(
        variant=variant,
        world_count=transitions.world_count,
        nodes=transitions.nodes,
        modes=transitions.modes,
        global_edge_budget=global_budget,
        local_edge_budget_per_world=local_budget,
        rng=random.Random(seed + 77),
    )
    for world in train_worlds:
        model.train_world(transitions, int(world), withheld=withheld)
    return model


def route_samples(
    transitions: WorldTransitions,
    seed: int,
    route_length: int,
    routes_per_world: int,
    worlds: Optional[Sequence[int]] = None,
    require_withheld: Optional[set[TransitionKey]] = None,
    require_no_withheld: Optional[set[TransitionKey]] = None,
) -> Iterable[Tuple[int, int, List[int]]]:
    rng = np.random.default_rng(seed + 911 + 23 * route_length)
    eval_worlds = list(range(transitions.world_count)) if worlds is None else list(worlds)
    attempts_limit = max(10_000, routes_per_world * len(eval_worlds) * 100)
    for world in eval_worlds:
        produced = 0
        attempts = 0
        while produced < routes_per_world and attempts < attempts_limit:
            attempts += 1
            start = int(rng.integers(0, transitions.nodes))
            modes = [int(x) for x in rng.integers(0, transitions.modes, size=route_length)]
            node = start
            used: set[TransitionKey] = set()
            for mode in modes:
                used.add((int(world), node, int(mode)))
                node = transitions.target(world, node, int(mode))
            if require_withheld is not None and used.isdisjoint(require_withheld):
                continue
            if require_no_withheld is not None and not used.isdisjoint(require_no_withheld):
                continue
            produced += 1
            yield int(world), start, modes
        while produced < routes_per_world:
            start = int(rng.integers(0, transitions.nodes))
            modes = [int(x) for x in rng.integers(0, transitions.modes, size=route_length)]
            produced += 1
            yield int(world), start, modes


METRIC_COLUMNS: Tuple[str, ...] = (
    "composition_accuracy",
    "route_table_accuracy",
    "transition_accuracy",
    "structure_transition_accuracy",
    "composition_route_gap",
    "route_margin",
    "world_margin",
    "mode_margin",
    "wrong_route_activation",
    "wrong_world_activation",
    "wrong_mode_activation",
    "structural_wrong_world_activation",
    "context_confusion",
    "top1_world_accuracy",
    "used_edge_fraction",
    "stored_edge_count",
    "lesion_sensitivity",
    "route_table_lesion_sensitivity",
)


def base_row(
    phase: str,
    model: RouteMemoryModel,
    seed: int,
    route_length: int,
    qctx: QueryContext,
    *,
    world: str | int = "all",
    mode: str | int = "all",
    budget_ratio: Optional[float] = None,
    local_budget_ratio: Optional[float] = None,
    budget_setting: str = "default",
    lesion_condition: str = NO_LESION,
    freeze_condition: str = NO_FREEZE,
    plasticity_setting: Optional[str] = None,
    phase_detail: str = "none",
) -> Dict[str, Any]:
    variant = model.variant
    return {
        "experiment_name": EXPERIMENT_NAME,
        "schema_version": SCHEMA_VERSION,
        "phase": phase,
        "phase_detail": phase_detail,
        "variant_name": variant.name,
        "seed": seed,
        "world": world,
        "mode": mode,
        "world_count": model.world_count,
        "nodes": model.nodes,
        "modes": model.modes,
        "mode_slot_count": model.mode_slot_count,
        "route_length": route_length,
        "recurrence_training": variant.recurrence_training,
        "recurrence_evaluation": variant.recurrence_evaluation,
        "recurrence_setting": variant.recurrence_setting,
        "structural_plasticity": variant.structural_plasticity,
        "world_context": variant.world_context,
        "context_binding": variant.context_binding,
        "world_gated_plasticity": variant.world_gated_plasticity,
        "plasticity_setting": plasticity_setting or variant.plasticity_setting,
        "context_condition": qctx.condition,
        "context_corruption_level": qctx.level,
        "lesion_condition": lesion_condition,
        "freeze_condition": freeze_condition,
        "budget_setting": budget_setting,
        "budget_ratio": budget_ratio,
        "local_budget_ratio": local_budget_ratio,
        "consolidation_setting": variant.consolidation_setting,
        "consolidation_strength": variant.consolidation_strength,
        "stored_edge_count": len(model.edges),
        "global_edge_budget": model.global_edge_budget,
        "local_edge_budget_per_world": model.local_edge_budget_per_world,
    }


def evaluate_model(
    phase: str,
    transitions: WorldTransitions,
    model: RouteMemoryModel,
    seed: int,
    route_length: int,
    routes_per_world: int,
    *,
    qctx: QueryContext = QueryContext(),
    worlds: Optional[Sequence[int]] = None,
    budget_ratio: Optional[float] = None,
    local_budget_ratio: Optional[float] = None,
    budget_setting: str = "default",
    lesion_condition: str = NO_LESION,
    freeze_condition: str = NO_FREEZE,
    plasticity_setting: Optional[str] = None,
    phase_detail: str = "none",
    require_withheld: Optional[set[TransitionKey]] = None,
    require_no_withheld: Optional[set[TransitionKey]] = None,
) -> Dict[str, Any]:
    route_correct = 0
    route_total = 0
    route_table_correct = 0
    route_table_total = 0
    route_world_top1: List[float] = []
    route_world_margins: List[float] = []
    route_wrong_world: List[float] = []
    route_context_confusion: List[float] = []
    route_used_edges: List[float] = []
    diag_values: Dict[str, List[float]] = defaultdict(list)
    table_diag_values: Dict[str, List[float]] = defaultdict(list)

    samples = route_samples(
        transitions,
        seed=seed,
        route_length=route_length,
        routes_per_world=routes_per_world,
        worlds=worlds,
        require_withheld=require_withheld,
        require_no_withheld=require_no_withheld,
    )
    for world, start, modes in samples:
        truth = transitions.final_after_modes(world, start, modes)
        pred = model.predict_route(world, start, modes, qctx)
        route_correct += int(int(pred["pred_node"]) == truth)
        route_total += 1
        route_world_top1.append(pred["top1_world_accuracy"])
        route_world_margins.append(pred["world_margin"])
        route_wrong_world.append(pred["wrong_world_activation"])
        route_context_confusion.append(pred["context_confusion"])
        route_used_edges.append(pred["used_edge_fraction"])
        selected_world = int(pred["selected_world"])
        node = int(start)
        for mode in modes:
            target = transitions.target(world, node, int(mode))
            diag = model.edge_diagnostics(selected_world, world, node, int(mode), target)
            for key, value in diag.items():
                diag_values[key].append(float(value))
            node = target

    eval_worlds = list(range(transitions.world_count)) if worlds is None else list(worlds)
    for world, node, mode in transitions.all_transition_keys(eval_worlds):
        truth = transitions.target(world, node, mode)
        pred = model.predict_route(world, node, [mode], qctx)
        route_table_correct += int(int(pred["pred_node"]) == truth)
        route_table_total += 1
        selected_world = int(pred["selected_world"])
        diag = model.edge_diagnostics(selected_world, world, node, mode, truth)
        for key, value in diag.items():
            table_diag_values[key].append(float(value))

    composition_accuracy = route_correct / max(1, route_total)
    route_table_accuracy = route_table_correct / max(1, route_table_total)
    row = base_row(
        phase,
        model,
        seed,
        route_length,
        qctx,
        world="all" if worlds is None else ",".join(str(w) for w in worlds),
        mode="all",
        budget_ratio=budget_ratio,
        local_budget_ratio=local_budget_ratio,
        budget_setting=budget_setting,
        lesion_condition=lesion_condition,
        freeze_condition=freeze_condition,
        plasticity_setting=plasticity_setting,
        phase_detail=phase_detail,
    )
    row.update(
        {
            "composition_accuracy": composition_accuracy,
            "route_table_accuracy": route_table_accuracy,
            "transition_accuracy": route_table_accuracy,
            "structure_transition_accuracy": float(np.mean(table_diag_values["structure_transition_correct"]))
            if table_diag_values["structure_transition_correct"]
            else 0.0,
            "composition_route_gap": route_table_accuracy - composition_accuracy,
            "route_margin": float(np.mean(table_diag_values["route_margin"])) if table_diag_values["route_margin"] else 0.0,
            "world_margin": float(np.mean(route_world_margins)) if route_world_margins else 0.0,
            "mode_margin": float(np.mean(table_diag_values["mode_margin"])) if table_diag_values["mode_margin"] else 0.0,
            "wrong_route_activation": float(np.mean(table_diag_values["wrong_route_activation"]))
            if table_diag_values["wrong_route_activation"]
            else 0.0,
            "wrong_world_activation": float(np.mean(route_wrong_world)) if route_wrong_world else 0.0,
            "wrong_mode_activation": float(np.mean(table_diag_values["wrong_mode_activation"]))
            if table_diag_values["wrong_mode_activation"]
            else 0.0,
            "structural_wrong_world_activation": float(np.mean(table_diag_values["structural_wrong_world_activation"]))
            if table_diag_values["structural_wrong_world_activation"]
            else 0.0,
            "context_confusion": float(np.mean(route_context_confusion)) if route_context_confusion else 0.0,
            "top1_world_accuracy": float(np.mean(route_world_top1)) if route_world_top1 else 0.0,
            "used_edge_fraction": float(np.mean(route_used_edges)) if route_used_edges else 0.0,
            "lesion_sensitivity": 0.0,
            "route_table_lesion_sensitivity": 0.0,
            "composition_mean_route_margin": float(np.mean(diag_values["route_margin"])) if diag_values["route_margin"] else 0.0,
            "composition_mean_mode_margin": float(np.mean(diag_values["mode_margin"])) if diag_values["mode_margin"] else 0.0,
        }
    )
    return row


def progress_phase(logger: ProgressLogger, phase: str, total_units: int, **extra: Any) -> None:
    logger.start_phase(phase, total_units=total_units)
    if extra:
        logger.write(event="phase_metadata", message=f"{phase} metadata", **extra)


def run_variant_comparison(config: Config, logger: ProgressLogger) -> List[Dict[str, Any]]:
    progress_phase(logger, "variant_comparison", len(config.seeds) * len(CORE_VARIANTS) * len(config.route_lengths))
    rows: List[Dict[str, Any]] = []
    for seed in config.seeds:
        transitions = WorldTransitions(config.world_count, config.nodes, config.modes, seed)
        for variant_name in CORE_VARIANTS:
            variant = VARIANTS[variant_name]
            model = build_model(transitions, variant, seed, global_budget_ratio=1.0)
            for route_length in config.route_lengths:
                rows.append(
                    evaluate_model(
                        "variant_comparison",
                        transitions,
                        model,
                        seed,
                        route_length,
                        config.routes_per_world,
                        budget_ratio=1.0,
                        budget_setting="default_exact_global",
                    )
                )
                logger.step(f"seed={seed}; variant={variant_name}; route_length={route_length}")
    logger.complete_phase(len(rows))
    return rows


def run_structure_audit(config: Config, logger: ProgressLogger) -> List[Dict[str, Any]]:
    progress_phase(logger, "structure_audit", len(config.seeds) * len(CORE_VARIANTS))
    rows: List[Dict[str, Any]] = []
    for seed in config.seeds:
        transitions = WorldTransitions(config.structure_audit_world_count, config.nodes, config.modes, seed)
        for variant_name in CORE_VARIANTS:
            variant = VARIANTS[variant_name]
            model = build_model(transitions, variant, seed, global_budget_ratio=1.0)
            rows.append(
                evaluate_model(
                    "structure_audit",
                    transitions,
                    model,
                    seed,
                    config.structure_audit_route_length,
                    config.routes_per_world,
                    budget_ratio=1.0,
                    budget_setting="structure_audit_exact_global",
                    phase_detail="structure_only_decoding",
                )
            )
            logger.step(f"seed={seed}; variant={variant_name}")
    logger.complete_phase(len(rows))
    return rows


def run_context_corruption(config: Config, logger: ProgressLogger) -> List[Dict[str, Any]]:
    progress_phase(logger, "context_corruption", len(config.seeds) * 4 * context_corruption_unit_count(config))
    rows: List[Dict[str, Any]] = []
    variants = (
        "exp13_1_full_model",
        "exp13_1_no_recurrence_at_eval",
        "exp13_1_no_context_binding",
        "exp13_1_no_world_gated_plasticity",
    )
    corruption_sweeps = (
        ("clean", (0.0,)),
        ("context_dropout", config.context_levels),
        ("context_bleed", config.context_levels),
        ("wrong_world_injection", config.context_levels),
    )
    for seed in config.seeds:
        transitions = WorldTransitions(config.world_count, config.nodes, config.modes, seed)
        for variant_name in variants:
            model = build_model(transitions, VARIANTS[variant_name], seed, global_budget_ratio=1.0)
            for condition, levels in corruption_sweeps:
                for level in levels:
                    if condition != "clean" and level <= 0.0:
                        continue
                    rows.append(
                        evaluate_model(
                            "context_corruption",
                            transitions,
                            model,
                            seed,
                            config.composition_route_length,
                            config.routes_per_world,
                            qctx=QueryContext(condition=condition, level=float(level)),
                            budget_ratio=1.0,
                            budget_setting="context_exact_global",
                        )
                    )
                    logger.step(f"seed={seed}; variant={variant_name}; condition={condition}; level={level}")
    logger.complete_phase(len(rows))
    return rows


def run_freeze_plasticity(config: Config, logger: ProgressLogger) -> List[Dict[str, Any]]:
    progress_phase(logger, "freeze_plasticity", len(config.seeds) * 4)
    rows: List[Dict[str, Any]] = []
    freeze_points = (
        ("freeze_after_world_a", 0),
        ("freeze_after_world_b", 1),
    )
    for seed in config.seeds:
        transitions = WorldTransitions(config.freeze_world_count, config.nodes, config.modes, seed)
        for freeze_name, freeze_after in freeze_points:
            model = RouteMemoryModel(
                variant=FULL_VARIANT,
                world_count=transitions.world_count,
                nodes=transitions.nodes,
                modes=transitions.modes,
                global_edge_budget=transitions.world_count * transitions.nodes * transitions.modes,
                local_edge_budget_per_world=None,
                rng=random.Random(seed + 77),
            )
            for world in range(transitions.world_count):
                model.train_world(transitions, world)
                if world == freeze_after:
                    model.freeze_plasticity()
            rows.append(
                evaluate_model(
                    "freeze_plasticity",
                    transitions,
                    model,
                    seed,
                    config.composition_route_length,
                    config.routes_per_world,
                    budget_ratio=1.0,
                    budget_setting="freeze_exact_global",
                    freeze_condition=freeze_name,
                    plasticity_setting=f"frozen_structural_after_world_{freeze_after}",
                    phase_detail="post_freeze_world_schedule",
                )
            )
            logger.step(f"seed={seed}; freeze_condition={freeze_name}")

        extended = WorldTransitions(config.freeze_world_count + 1, config.nodes, config.modes, seed)
        model = build_model(
            extended,
            FULL_VARIANT,
            seed,
            train_worlds=list(range(config.freeze_world_count)),
            global_budget_ratio=1.0,
        )
        model.consolidate_now()
        model.freeze_plasticity()
        adaptation_world = config.freeze_world_count
        model.train_world(extended, adaptation_world)
        rows.append(
            evaluate_model(
                "freeze_plasticity",
                extended,
                model,
                seed,
                config.composition_route_length,
                config.routes_per_world,
                worlds=list(range(config.freeze_world_count)),
                budget_ratio=1.0,
                budget_setting="freeze_exact_global",
                freeze_condition="freeze_after_consolidation_old_worlds",
                plasticity_setting="frozen_structural_after_consolidation",
                phase_detail="old_world_retention_after_frozen_adaptation_attempt",
            )
        )
        logger.step(f"seed={seed}; freeze_condition=freeze_after_consolidation_old_worlds")
        rows.append(
            evaluate_model(
                "freeze_plasticity",
                extended,
                model,
                seed,
                config.composition_route_length,
                config.routes_per_world,
                worlds=[adaptation_world],
                budget_ratio=1.0,
                budget_setting="freeze_exact_global",
                freeze_condition="freeze_after_consolidation_new_world",
                plasticity_setting="frozen_structural_after_consolidation",
                phase_detail="new_world_adaptation_blocked_by_freeze",
            )
        )
        logger.step(f"seed={seed}; freeze_condition=freeze_after_consolidation_new_world")
    logger.complete_phase(len(rows))
    return rows


def collect_route_critical_edges(
    transitions: WorldTransitions,
    model: RouteMemoryModel,
    seed: int,
    route_length: int,
    routes_per_world: int,
) -> List[EdgeKey]:
    critical: set[EdgeKey] = set()
    for world, start, modes in route_samples(transitions, seed, route_length, routes_per_world):
        node = start
        for mode in modes:
            target = transitions.target(world, node, int(mode))
            key = model.critical_edge_key(world, node, int(mode), target)
            if key in model.edges:
                critical.add(key)
            node = target
    return list(critical)


def matched_weight_random_edges(
    model: RouteMemoryModel,
    targeted_keys: Sequence[EdgeKey],
    rng: random.Random,
) -> List[EdgeKey]:
    available = [key for key in model.edges if key not in set(targeted_keys)]
    if not available:
        return []
    by_score = sorted(available, key=lambda key: model.edges[key].score)
    chosen: List[EdgeKey] = []
    used: set[EdgeKey] = set()
    for target_key in targeted_keys:
        target_score = model.edges[target_key].score if target_key in model.edges else 0.0
        nearest = [
            key
            for key in sorted(by_score, key=lambda key: abs(model.edges[key].score - target_score))[: max(8, len(targeted_keys))]
            if key not in used
        ]
        if nearest:
            choice = nearest[rng.randrange(len(nearest))]
        else:
            remaining = [key for key in available if key not in used]
            if not remaining:
                break
            choice = remaining[rng.randrange(len(remaining))]
        used.add(choice)
        chosen.append(choice)
    return chosen


def run_lesion_tests(config: Config, logger: ProgressLogger) -> List[Dict[str, Any]]:
    progress_phase(logger, "lesion_test", len(config.seeds) * 4)
    rows: List[Dict[str, Any]] = []
    for seed in config.seeds:
        transitions = WorldTransitions(config.lesion_world_count, config.nodes, config.modes, seed)
        base_model = build_model(transitions, FULL_VARIANT, seed, global_budget_ratio=1.25)
        baseline = evaluate_model(
            "lesion_test",
            transitions,
            base_model,
            seed,
            config.lesion_route_length,
            config.routes_per_world,
            budget_ratio=1.25,
            budget_setting="lesion_surplus_global",
            lesion_condition="clean_unlesioned_baseline",
        )
        rows.append(baseline)
        logger.step(f"seed={seed}; lesion_condition=clean_unlesioned_baseline")

        critical = collect_route_critical_edges(
            transitions,
            base_model,
            seed,
            config.lesion_route_length,
            config.routes_per_world,
        )
        count = max(1, int(math.ceil(config.lesion_fraction * max(1, len(critical)))))
        targeted = sorted(critical, key=lambda key: base_model.edges[key].score if key in base_model.edges else 0.0, reverse=True)[:count]
        rng = random.Random(seed + 1313)
        all_keys = list(base_model.edges.keys())
        random_count = rng.sample(all_keys, k=min(count, len(all_keys))) if all_keys else []
        random_weight = matched_weight_random_edges(base_model, targeted, rng)

        lesion_sets = {
            "targeted_critical_edges": targeted,
            "random_count_matched_edges": random_count,
            "random_weight_distribution_matched_edges": random_weight,
        }
        for condition, keys in lesion_sets.items():
            model = base_model.clone()
            removed = model.remove_edges(keys)
            row = evaluate_model(
                "lesion_test",
                transitions,
                model,
                seed,
                config.lesion_route_length,
                config.routes_per_world,
                budget_ratio=1.25,
                budget_setting="lesion_surplus_global",
                lesion_condition=condition,
                phase_detail=f"removed_edges={removed}",
            )
            row["lesion_sensitivity"] = baseline["composition_accuracy"] - row["composition_accuracy"]
            row["route_table_lesion_sensitivity"] = baseline["route_table_accuracy"] - row["route_table_accuracy"]
            row["lesioned_edge_count"] = removed
            rows.append(row)
            logger.step(f"seed={seed}; lesion_condition={condition}; removed_edges={removed}")
    logger.complete_phase(len(rows))
    return rows


def run_budget_consolidation(config: Config, logger: ProgressLogger) -> List[Dict[str, Any]]:
    progress_phase(logger, "budget_consolidation", len(config.seeds) * len(CONSOLIDATION_VARIANTS) * 3)
    rows: List[Dict[str, Any]] = []
    budget_settings = (
        ("default_global_budget", 1.0, None),
        ("constrained_global_budget", 0.50, None),
        ("constrained_local_budget", None, 0.50),
    )
    for seed in config.seeds:
        transitions = WorldTransitions(config.budget_world_count, config.nodes, config.modes, seed)
        for variant_name in CONSOLIDATION_VARIANTS:
            variant = VARIANTS[variant_name]
            for budget_setting, global_ratio, local_ratio in budget_settings:
                model = build_model(
                    transitions,
                    variant,
                    seed,
                    global_budget_ratio=global_ratio,
                    local_budget_ratio=local_ratio,
                )
                rows.append(
                    evaluate_model(
                        "budget_consolidation",
                        transitions,
                        model,
                        seed,
                        config.budget_route_length,
                        config.routes_per_world,
                        budget_ratio=global_ratio,
                        local_budget_ratio=local_ratio,
                        budget_setting=budget_setting,
                    )
                )
                logger.step(f"seed={seed}; variant={variant_name}; budget={budget_setting}")
    logger.complete_phase(len(rows))
    return rows


def flatten_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [
        "_".join([str(part) for part in col if part != ""]).rstrip("_") if isinstance(col, tuple) else str(col)
        for col in df.columns
    ]
    return df


def summarize(df: pd.DataFrame, group_cols: Sequence[str]) -> pd.DataFrame:
    available_groups = [col for col in group_cols if col in df.columns]
    metric_cols = [col for col in METRIC_COLUMNS if col in df.columns]
    if not metric_cols:
        return pd.DataFrame()
    agg = {col: ["mean", "std", "count"] for col in metric_cols}
    return df.groupby(available_groups, dropna=False).agg(agg).reset_index().pipe(flatten_columns)


def save_plot_line(
    df: pd.DataFrame,
    out: Path,
    x: str,
    y: str,
    hue: str,
    title: str,
    xlabel: str,
    ylabel: str,
) -> None:
    if df.empty or any(col not in df.columns for col in (x, y, hue)):
        return
    plt.figure(figsize=(12, 7))
    for name, group in df.groupby(hue, dropna=False):
        group = group.sort_values(x)
        plt.plot(group[x], group[y], marker="o", label=str(name))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True, alpha=0.35)
    plt.legend(loc="best")
    plt.tight_layout()
    out.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out, dpi=150)
    plt.close()


def save_plot_bar(
    df: pd.DataFrame,
    out: Path,
    x: str,
    y: str,
    title: str,
    xlabel: str,
    ylabel: str,
) -> None:
    if df.empty or x not in df.columns or y not in df.columns:
        return
    data = df.sort_values(y, ascending=False)
    plt.figure(figsize=(12, 7))
    plt.bar(data[x].astype(str), data[y])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=30, ha="right")
    plt.grid(True, axis="y", alpha=0.35)
    plt.tight_layout()
    out.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out, dpi=150)
    plt.close()


def create_summaries_and_plots(analysis_dir: Path, metrics_df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    summaries: Dict[str, pd.DataFrame] = {}
    plots_dir = analysis_dir / "plots"
    plots_dir.mkdir(parents=True, exist_ok=True)

    summary_specs: Dict[str, Tuple[str, Sequence[str]]] = {
        f"{ANALYSIS_ID}_summary.csv": (
            "all",
            (
                "phase",
                "variant_name",
                "route_length",
                "context_condition",
                "lesion_condition",
                "budget_setting",
                "consolidation_setting",
                "freeze_condition",
            ),
        ),
        f"{ANALYSIS_ID}_variant_metrics.csv": (
            "variant_comparison",
            ("phase", "variant_name", "route_length", "recurrence_setting", "plasticity_setting"),
        ),
        f"{ANALYSIS_ID}_ablation_metrics.csv": (
            "ablation",
            ("phase", "variant_name", "route_length", "recurrence_setting", "context_binding", "world_gated_plasticity"),
        ),
        f"{ANALYSIS_ID}_context_corruption.csv": (
            "context_corruption",
            ("phase", "variant_name", "context_condition", "context_corruption_level", "recurrence_setting"),
        ),
        f"{ANALYSIS_ID}_lesion_metrics.csv": (
            "lesion_test",
            ("phase", "variant_name", "lesion_condition", "route_length", "budget_setting"),
        ),
        f"{ANALYSIS_ID}_budget_consolidation.csv": (
            "budget_consolidation",
            (
                "phase",
                "variant_name",
                "budget_setting",
                "consolidation_setting",
                "consolidation_strength",
                "budget_ratio",
                "local_budget_ratio",
            ),
        ),
        f"{ANALYSIS_ID}_freeze_plasticity.csv": (
            "freeze_plasticity",
            ("phase", "variant_name", "freeze_condition", "plasticity_setting", "phase_detail"),
        ),
    }

    for filename, (phase, groups) in summary_specs.items():
        if phase == "all":
            subset = metrics_df
        elif phase == "ablation":
            subset = metrics_df[metrics_df["phase"].isin(["variant_comparison", "structure_audit", "freeze_plasticity"])]
        else:
            subset = metrics_df[metrics_df["phase"] == phase]
        if subset.empty:
            continue
        summary = summarize(subset, groups)
        summaries[filename] = summary
        summary.to_csv(analysis_dir / filename, index=False)

    variant_summary = summaries.get(f"{ANALYSIS_ID}_variant_metrics.csv", pd.DataFrame())
    if not variant_summary.empty:
        save_plot_line(
            variant_summary,
            plots_dir / f"{ANALYSIS_ID}_composition_accuracy.png",
            x="route_length",
            y="composition_accuracy_mean",
            hue="variant_name",
            title="Experiment 13.1: composition accuracy by variant",
            xlabel="route length",
            ylabel="composition accuracy",
        )
        save_plot_line(
            variant_summary,
            plots_dir / f"{ANALYSIS_ID}_route_table_accuracy.png",
            x="route_length",
            y="route_table_accuracy_mean",
            hue="variant_name",
            title="Experiment 13.1: route-table accuracy by variant",
            xlabel="route length",
            ylabel="route-table accuracy",
        )
        rec = variant_summary[
            variant_summary["variant_name"].isin(
                ["exp13_1_full_model", "exp13_1_no_recurrence_at_eval", "exp13_1_no_recurrence_throughout"]
            )
        ]
        save_plot_line(
            rec,
            plots_dir / f"{ANALYSIS_ID}_recurrence_ablation.png",
            x="route_length",
            y="composition_accuracy_mean",
            hue="variant_name",
            title="Experiment 13.1: recurrence ablation",
            xlabel="route length",
            ylabel="composition accuracy",
        )

    context_summary = summaries.get(f"{ANALYSIS_ID}_context_corruption.csv", pd.DataFrame())
    if not context_summary.empty:
        full_context = context_summary[context_summary["variant_name"] == "exp13_1_full_model"]
        save_plot_line(
            full_context,
            plots_dir / f"{ANALYSIS_ID}_context_confusion.png",
            x="context_corruption_level",
            y="context_confusion_mean",
            hue="context_condition",
            title="Experiment 13.1: context confusion under corruption",
            xlabel="corruption level",
            ylabel="context confusion",
        )

    lesion_summary = summaries.get(f"{ANALYSIS_ID}_lesion_metrics.csv", pd.DataFrame())
    if not lesion_summary.empty:
        save_plot_bar(
            lesion_summary,
            plots_dir / f"{ANALYSIS_ID}_lesion_sensitivity.png",
            x="lesion_condition",
            y="lesion_sensitivity_mean",
            title="Experiment 13.1: lesion sensitivity",
            xlabel="lesion condition",
            ylabel="composition sensitivity",
        )

    budget_summary = summaries.get(f"{ANALYSIS_ID}_budget_consolidation.csv", pd.DataFrame())
    if not budget_summary.empty:
        save_plot_line(
            budget_summary,
            plots_dir / f"{ANALYSIS_ID}_budget_consolidation.png",
            x="consolidation_strength",
            y="composition_accuracy_mean",
            hue="budget_setting",
            title="Experiment 13.1: budget and consolidation controls",
            xlabel="consolidation strength",
            ylabel="composition accuracy",
        )

    return summaries


def dataframe_snapshot(df: pd.DataFrame, query: Optional[str] = None, limit: int = 10) -> str:
    if df.empty:
        return "_No rows produced._"
    data = df.query(query) if query else df
    if data.empty:
        return "_No matching rows produced._"
    return "```text\n" + data.head(limit).to_string(index=False) + "\n```"


def write_report(analysis_dir: Path, config: Config, elapsed: float, run_id: str, sqlite_path: Optional[Path]) -> None:
    metrics_path = analysis_dir / "metrics.csv"
    df = pd.read_csv(metrics_path)
    summary_path = analysis_dir / f"{ANALYSIS_ID}_summary.csv"
    summary = pd.read_csv(summary_path) if summary_path.exists() else pd.DataFrame()
    plots_dir = analysis_dir / "plots"
    lines: List[str] = []
    lines.append("# Experiment 13.1 Report - Publication-Hardening Route-Field Memory Audit")
    lines.append("")
    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "Experiment 13.1 tests whether memory-like behavior is partly encoded in plastic recurrent "
        "route-field structure rather than only in static learned weights or symbolic lookup tables."
    )
    lines.append("")
    lines.append("## Run Metadata")
    lines.append("")
    lines.append(f"- run_id: `{run_id}`")
    lines.append(f"- profile: `{config.profile}`")
    lines.append(f"- seeds: `{list(config.seeds)}`")
    lines.append(f"- nodes: `{config.nodes}`")
    lines.append(f"- modes: `{config.modes}`")
    lines.append(f"- elapsed seconds: `{elapsed:.2f}`")
    lines.append(f"- metrics rows: `{len(df)}`")
    lines.append(f"- progress log: `{(analysis_dir / 'progress.jsonl').as_posix()}`")
    if sqlite_path is not None:
        lines.append(f"- SQLite run database: `{sqlite_path.as_posix()}`")
    lines.append("")
    lines.append("## Safety Checks Baked Into The Implementation")
    lines.append("")
    lines.append(
        "- The mode-slot table has `modes + 1` slots. When context/mode binding is disabled, "
        "the unbound mode uses the extra slot, preventing the historical out-of-bounds bug."
    )
    lines.append("- Corruption diagnostics pass the corrupted `QueryContext` into both composition and route-table evaluation.")
    lines.append("- Recurrence-disabled-at-evaluation and recurrence-disabled-throughout are represented as separate variants.")
    lines.append("- Lesions include targeted route-critical edges and matched random controls.")
    lines.append("- Every generated run is written under `analysis/<run_id>/`; the optional SQLite record is written under `runs/<run_id>.sqlite3`.")
    lines.append("")
    lines.append("## Summary Snapshot")
    lines.append("")
    lines.append(dataframe_snapshot(summary, limit=12))
    lines.append("")
    lines.append("## Interpretation Guide")
    lines.append("")
    lines.append(
        "Expected patterns only: if the route field is mechanistically meaningful, route-table accuracy may remain "
        "locally high when recurrence is disabled, while multi-step composition should fall. Targeted lesions should "
        "impair composed traversal more than matched random lesions when the learned structure is route-critical."
    )
    lines.append("")
    lines.append("## Caveats")
    lines.append("")
    lines.append("- These artifacts are internal ablations and controls, not external baselines.")
    lines.append("- Route-table accuracy is local transition knowledge and must not be treated as composed traversal.")
    lines.append("- Small problem sizes can saturate; use `standard` or `full` for manuscript-facing analysis.")
    lines.append("- Random seeds can produce unstable deltas; interpret mean effects with dispersion.")
    lines.append("- Figures are summaries; raw CSVs remain the evidence source.")
    lines.append("- This report should not be read as proof or as a causal claim without the validation report.")
    lines.append("")
    lines.append("## Source Paths")
    lines.append("")
    lines.append(f"- Metrics: `{metrics_path.as_posix()}`")
    lines.append(f"- Compatibility metrics copy: `{(analysis_dir / f'{ANALYSIS_ID}_metrics.csv').as_posix()}`")
    lines.append(f"- Summary: `{summary_path.as_posix()}`")
    lines.append(f"- Plots: `{plots_dir.as_posix()}`")
    lines.append(f"- Validation pending source: `{(analysis_dir / 'validation_report.md').as_posix()}`")
    text = "\n".join(lines)
    (analysis_dir / "experiment_report.md").write_text(text, encoding="utf-8")
    (analysis_dir / f"{ANALYSIS_ID}_report.md").write_text(text, encoding="utf-8")


def write_run_metadata(analysis_dir: Path, config: Config, run_id: str, sqlite_path: Optional[Path], total_units: int) -> Dict[str, Any]:
    manifest = {
        "experiment_name": EXPERIMENT_NAME,
        "analysis_id": ANALYSIS_ID,
        "schema_version": SCHEMA_VERSION,
        "run_id": run_id,
        "profile": config.profile,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "analysis_dir": analysis_dir.as_posix(),
        "sqlite_path": sqlite_path.as_posix() if sqlite_path is not None else None,
        "total_progress_units": total_units,
        "config": dataclasses.asdict(config),
        "variants": [variant.to_metadata() for variant in VARIANTS.values()],
    }
    (analysis_dir / "run_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    (analysis_dir / f"{ANALYSIS_ID}_config.json").write_text(
        json.dumps(dataclasses.asdict(config), indent=2, sort_keys=True),
        encoding="utf-8",
    )
    pd.DataFrame([variant.to_metadata() for variant in VARIANTS.values()]).to_csv(
        analysis_dir / f"{ANALYSIS_ID}_runs.csv",
        index=False,
    )
    return manifest


def write_sqlite(sqlite_path: Path, metrics_df: pd.DataFrame, manifest: Dict[str, Any]) -> None:
    sqlite_path.parent.mkdir(parents=True, exist_ok=True)
    if sqlite_path.exists():
        sqlite_path.unlink()
    with sqlite3.connect(sqlite_path) as conn:
        metrics_df.to_sql("metrics", conn, index=False, if_exists="replace")
        pd.DataFrame([{"key": "manifest", "value": json.dumps(manifest, sort_keys=True)}]).to_sql(
            "metadata", conn, index=False, if_exists="replace"
        )
        pd.DataFrame(manifest["variants"]).to_sql("variants", conn, index=False, if_exists="replace")


def run_all(config: Config, analysis_dir: Path, run_id: str, runs_dir: Path, *, write_sqlite_db: bool, progress_every: int) -> None:
    started = time.time()
    analysis_dir.mkdir(parents=True, exist_ok=True)
    runs_dir.mkdir(parents=True, exist_ok=True)
    sqlite_path = (runs_dir / f"{run_id}.sqlite3") if write_sqlite_db else None
    total_units = estimate_total_units(config)
    logger = ProgressLogger(analysis_dir / "progress.jsonl", total_units=total_units, progress_every=progress_every)
    rows: List[Dict[str, Any]] = []
    phases = (
        run_variant_comparison,
        run_structure_audit,
        run_freeze_plasticity,
        run_context_corruption,
        run_lesion_tests,
        run_budget_consolidation,
    )
    try:
        logger.write(event="run_start", message="Starting Experiment 13.1", profile=config.profile, run_id=run_id)
        manifest = write_run_metadata(analysis_dir, config, run_id, sqlite_path, total_units)
        for phase_fn in phases:
            phase_rows = phase_fn(config, logger)
            rows.extend(phase_rows)
            logger.write(event="artifact", message=f"Accumulated {len(rows)} rows", phase_function=phase_fn.__name__)
        metrics_df = pd.DataFrame(rows)
        metrics_df.insert(0, "run_id", run_id)
        metrics_df.to_csv(analysis_dir / "metrics.csv", index=False)
        metrics_df.to_csv(analysis_dir / f"{ANALYSIS_ID}_metrics.csv", index=False)
        create_summaries_and_plots(analysis_dir, metrics_df)
        if sqlite_path is not None:
            write_sqlite(sqlite_path, metrics_df, manifest)
        write_report(analysis_dir, config, elapsed=time.time() - started, run_id=run_id, sqlite_path=sqlite_path)
        logger.write(event="run_complete", message="Experiment 13.1 artifacts written", analysis_dir=str(analysis_dir), sqlite_path=str(sqlite_path) if sqlite_path else None)
    finally:
        logger.close()


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Experiment 13.1 publication-hardening audit.")
    parser.add_argument("--profile", choices=("smoke", "standard", "full"), default="standard")
    parser.add_argument("--run-id", default=None, help="Stable run identifier. Defaults to exp13_1_<profile>_<timestamp>.")
    parser.add_argument("--experiment-dir", default=str(Path(__file__).resolve().parent), help="Experiment directory containing runs/ and analysis/.")
    parser.add_argument("--analysis-dir", default=None, help="Exact analysis output directory. Defaults to <experiment-dir>/analysis/<run-id>.")
    parser.add_argument("--runs-dir", default=None, help="Directory for SQLite run databases. Defaults to <experiment-dir>/runs.")
    parser.add_argument("--progress-every", type=int, default=10, help="Print progress every N completed evaluation units within a phase.")
    parser.add_argument("--no-sqlite", action="store_true", help="Do not write runs/<run_id>.sqlite3.")
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove the output directory before running. Use only when intentionally discarding an incomplete local run.",
    )
    args = parser.parse_args()

    config = make_config(args.profile)
    run_id = args.run_id or make_run_id(args.profile)
    experiment_dir = Path(args.experiment_dir).resolve()
    analysis_dir = Path(args.analysis_dir).resolve() if args.analysis_dir else experiment_dir / "analysis" / run_id
    runs_dir = Path(args.runs_dir).resolve() if args.runs_dir else experiment_dir / "runs"
    if analysis_dir.exists() and any(analysis_dir.iterdir()):
        if args.clean:
            shutil.rmtree(analysis_dir)
        else:
            raise FileExistsError(
                f"Output directory {analysis_dir} is not empty. Choose a new --run-id/--analysis-dir or pass --clean "
                "only if the existing contents are not a completed historical run."
            )
    sqlite_path = runs_dir / f"{run_id}.sqlite3"
    if sqlite_path.exists() and not args.no_sqlite:
        if args.clean:
            sqlite_path.unlink()
        else:
            raise FileExistsError(f"SQLite run database already exists: {sqlite_path}. Choose a new --run-id or pass --clean.")
    run_all(config, analysis_dir, run_id, runs_dir, write_sqlite_db=not args.no_sqlite, progress_every=args.progress_every)
    print(f"Experiment 13.1 complete. Run ID: {run_id}")
    print(f"Analysis directory: {analysis_dir}")
    if not args.no_sqlite:
        print(f"SQLite database: {sqlite_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
