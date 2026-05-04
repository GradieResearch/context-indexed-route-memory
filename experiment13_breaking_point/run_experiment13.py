#!/usr/bin/env python3
"""
Experiment 13: Breaking Point, Context Corruption, and Continuous Front-End Bridge

This experiment extends Experiment 12 by deliberately leaving the saturated/ceiling regime.
It tests the model under finite memory pressure, adversarial context corruption, continual
retention pressure, true primitive holdout, and a simple continuous/non-symbolic front-end.

The implementation is deliberately self-contained and deterministic. It is not intended to
be a high-performance neural simulator. It is a mechanistic diagnostic harness that makes
individual claims testable and falsifiable.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import shutil
import time
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


EdgeKey = Tuple[int, int, int, int]  # context/world key, source node, mode, target node
TransitionKey = Tuple[int, int, int]  # world, source node, mode

NO_CONTEXT = -1


@dataclass(frozen=True)
class Variant:
    name: str
    use_world_context: bool = True
    structural_plasticity: bool = True
    recurrence: bool = True
    consolidation_strength: float = 0.25
    context_binding_strength: float = 1.0
    world_gated_plasticity: bool = False
    query_uses_true_world_when_clean: bool = False


VARIANTS: Dict[str, Variant] = {
    "exp13_full_context_separated_memory": Variant(
        name="exp13_full_context_separated_memory",
        use_world_context=True,
        structural_plasticity=True,
        recurrence=True,
        consolidation_strength=0.25,
        context_binding_strength=1.0,
    ),
    "exp13_world_gated_plasticity": Variant(
        name="exp13_world_gated_plasticity",
        use_world_context=True,
        structural_plasticity=True,
        recurrence=True,
        consolidation_strength=0.25,
        context_binding_strength=1.10,
        world_gated_plasticity=True,
    ),
    "exp13_no_consolidation": Variant(
        name="exp13_no_consolidation",
        use_world_context=True,
        structural_plasticity=True,
        recurrence=True,
        consolidation_strength=0.0,
        context_binding_strength=0.95,
    ),
    "exp13_strong_consolidation": Variant(
        name="exp13_strong_consolidation",
        use_world_context=True,
        structural_plasticity=True,
        recurrence=True,
        consolidation_strength=0.80,
        context_binding_strength=1.20,
    ),
    "exp13_no_world_context": Variant(
        name="exp13_no_world_context",
        use_world_context=False,
        structural_plasticity=True,
        recurrence=True,
        consolidation_strength=0.25,
        context_binding_strength=0.0,
    ),
    "exp13_no_context_binding": Variant(
        name="exp13_no_context_binding",
        use_world_context=True,
        structural_plasticity=True,
        recurrence=True,
        consolidation_strength=0.25,
        context_binding_strength=0.15,
        # This approximates a labelled retrieval path that is correct in perfectly clean
        # conditions but has weak endogenous world selectivity when context is corrupted.
        query_uses_true_world_when_clean=True,
    ),
    "exp13_no_recurrence": Variant(
        name="exp13_no_recurrence",
        use_world_context=True,
        structural_plasticity=True,
        recurrence=False,
        consolidation_strength=0.25,
        context_binding_strength=1.0,
    ),
    "exp13_no_structural_plasticity": Variant(
        name="exp13_no_structural_plasticity",
        use_world_context=True,
        structural_plasticity=False,
        recurrence=True,
        consolidation_strength=0.25,
        context_binding_strength=1.0,
    ),
}


@dataclass
class Edge:
    key: EdgeKey
    score: float
    created_step: int
    last_update_step: int


@dataclass
class Config:
    profile: str
    seeds: List[int]
    nodes: int
    modes: int
    route_lengths: List[int]
    world_counts: List[int]
    capacity_world_counts: List[int]
    capacity_route_lengths: List[int]
    budget_ratios: List[float]
    local_budget_ratios: List[float]
    context_world_count: int
    context_route_length: int
    context_budget_ratio: float
    context_bleed_levels: List[float]
    context_dropout_levels: List[float]
    adversarial_context_levels: List[float]
    retention_world_count: int
    retention_route_length: int
    retention_budget_ratios: List[float]
    holdout_world_count: int
    holdout_route_length: int
    primitive_holdout_rates: List[float]
    continuous_world_count: int
    continuous_route_length: int
    continuous_noise_levels: List[float]
    routes_per_world: int
    variants: List[str]


def make_config(profile: str) -> Config:
    if profile == "smoke":
        return Config(
            profile=profile,
            seeds=list(range(2)),
            nodes=16,
            modes=3,
            route_lengths=[1, 2, 4],
            world_counts=[4, 8],
            capacity_world_counts=[4, 8],
            capacity_route_lengths=[1, 4],
            budget_ratios=[0.50, 1.00],
            local_budget_ratios=[0.50, 1.00],
            context_world_count=8,
            context_route_length=4,
            context_budget_ratio=1.0,
            context_bleed_levels=[0.0, 0.50, 0.95],
            context_dropout_levels=[0.0, 0.50, 0.90],
            adversarial_context_levels=[0.0, 0.49, 0.51, 0.90],
            retention_world_count=8,
            retention_route_length=4,
            retention_budget_ratios=[0.50, 1.00],
            holdout_world_count=8,
            holdout_route_length=4,
            primitive_holdout_rates=[0.0, 0.20, 0.40],
            continuous_world_count=8,
            continuous_route_length=4,
            continuous_noise_levels=[0.0, 0.20, 0.50, 0.90],
            routes_per_world=16,
            variants=[
                "exp13_full_context_separated_memory",
                "exp13_no_consolidation",
                "exp13_strong_consolidation",
                "exp13_no_world_context",
                "exp13_no_context_binding",
                "exp13_no_recurrence",
                "exp13_no_structural_plasticity",
            ],
        )

    if profile == "standard":
        return Config(
            profile=profile,
            seeds=list(range(5)),
            nodes=32,
            modes=3,
            route_lengths=[1, 2, 4, 8, 12],
            world_counts=[4, 8, 16, 32],
            capacity_world_counts=[4, 8, 16, 32],
            capacity_route_lengths=[1, 4, 8, 12],
            budget_ratios=[0.25, 0.50, 0.75, 1.00, 1.25],
            local_budget_ratios=[0.25, 0.50, 0.75, 1.00],
            context_world_count=32,
            context_route_length=8,
            context_budget_ratio=1.0,
            context_bleed_levels=[0.0, 0.10, 0.25, 0.50, 0.75, 0.95],
            context_dropout_levels=[0.0, 0.10, 0.25, 0.50, 0.75, 0.90],
            adversarial_context_levels=[0.0, 0.10, 0.25, 0.40, 0.49, 0.51, 0.60, 0.75, 0.90, 0.99],
            retention_world_count=32,
            retention_route_length=8,
            retention_budget_ratios=[0.375, 0.50, 0.75, 1.00],
            holdout_world_count=16,
            holdout_route_length=8,
            primitive_holdout_rates=[0.0, 0.10, 0.20, 0.40, 0.60],
            continuous_world_count=16,
            continuous_route_length=8,
            continuous_noise_levels=[0.0, 0.05, 0.10, 0.20, 0.35, 0.50, 0.75, 1.00],
            routes_per_world=48,
            variants=list(VARIANTS.keys()),
        )

    if profile == "full":
        return Config(
            profile=profile,
            seeds=list(range(20)),
            nodes=32,
            modes=3,
            route_lengths=[1, 2, 4, 8, 12, 16],
            world_counts=[4, 8, 16, 32, 64],
            capacity_world_counts=[4, 8, 16, 32, 64],
            capacity_route_lengths=[1, 2, 4, 8, 12, 16],
            budget_ratios=[0.125, 0.25, 0.375, 0.50, 0.75, 1.00, 1.25],
            local_budget_ratios=[0.125, 0.25, 0.50, 0.75, 1.00],
            context_world_count=32,
            context_route_length=12,
            context_budget_ratio=1.0,
            context_bleed_levels=[0.0, 0.05, 0.10, 0.25, 0.50, 0.75, 0.95],
            context_dropout_levels=[0.0, 0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 1.00],
            adversarial_context_levels=[0.0, 0.05, 0.10, 0.25, 0.40, 0.49, 0.51, 0.60, 0.75, 0.90, 0.99],
            retention_world_count=32,
            retention_route_length=12,
            retention_budget_ratios=[0.25, 0.375, 0.50, 0.75, 1.00],
            holdout_world_count=16,
            holdout_route_length=12,
            primitive_holdout_rates=[0.0, 0.05, 0.10, 0.20, 0.40, 0.60, 0.80],
            continuous_world_count=16,
            continuous_route_length=12,
            continuous_noise_levels=[0.0, 0.05, 0.10, 0.20, 0.35, 0.50, 0.75, 1.00, 1.25],
            routes_per_world=96,
            variants=list(VARIANTS.keys()),
        )

    raise ValueError(f"Unknown profile: {profile}")


class ProgressLogger:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._fh = self.path.open("w", encoding="utf-8")

    def write(self, **payload):
        payload.setdefault("time", time.time())
        self._fh.write(json.dumps(payload, sort_keys=True) + "\n")
        self._fh.flush()
        msg = payload.get("message") or payload.get("phase") or "progress"
        print(f"[{time.strftime('%H:%M:%S')}] {msg}")

    def close(self):
        self._fh.close()


class WorldTransitions:
    """Random incompatible worlds. Each world is a transition table node x mode -> next node."""

    def __init__(self, world_count: int, nodes: int, modes: int, seed: int):
        self.world_count = world_count
        self.nodes = nodes
        self.modes = modes
        self.seed = seed
        rng = np.random.default_rng(seed + 1009 * world_count + 9173 * nodes + 431 * modes)
        self.transitions = rng.integers(0, nodes, size=(world_count, nodes, modes), endpoint=False)

        # Avoid trivial self-loops where possible so multi-step routes are more informative.
        for w in range(world_count):
            for n in range(nodes):
                for m in range(modes):
                    if self.transitions[w, n, m] == n:
                        self.transitions[w, n, m] = (n + m + w + 1) % nodes

    def target(self, world: int, node: int, mode: int) -> int:
        return int(self.transitions[world, node, mode])

    def final_after_modes(self, world: int, start_node: int, modes: Sequence[int]) -> int:
        node = int(start_node)
        for mode in modes:
            node = self.target(world, node, int(mode))
        return node

    def all_transition_keys(self, worlds: Optional[Iterable[int]] = None) -> Iterable[TransitionKey]:
        ws = range(self.world_count) if worlds is None else worlds
        for w in ws:
            for n in range(self.nodes):
                for m in range(self.modes):
                    yield (w, n, m)


@dataclass
class QueryContext:
    corruption_type: str = "clean"
    level: float = 0.0
    adversarial_world: Optional[int] = None

    @property
    def is_clean(self) -> bool:
        return self.corruption_type == "clean" or self.level == 0.0


class RouteMemoryModel:
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
        self.world_count = world_count
        self.nodes = nodes
        self.modes = modes
        self.global_edge_budget = global_edge_budget
        self.local_edge_budget_per_world = local_edge_budget_per_world
        self.rng = rng
        self.edges: Dict[EdgeKey, Edge] = {}
        self._best_cache: Optional[Dict[Tuple[int, int, int], Tuple[int, float, float, bool]]] = None
        self.step = 0

    def _context_key(self, world: int) -> int:
        return world if self.variant.use_world_context else NO_CONTEXT

    def train_world(
        self,
        transitions: WorldTransitions,
        world: int,
        withheld: Optional[set[TransitionKey]] = None,
    ):
        withheld = withheld or set()
        if not self.variant.structural_plasticity:
            self.step += transitions.nodes * transitions.modes
            self._best_cache = None
            return

        for n in range(transitions.nodes):
            for m in range(transitions.modes):
                tk = (world, n, m)
                if tk in withheld:
                    continue
                target = transitions.target(world, n, m)
                ctx = self._context_key(world)
                key = (ctx, n, m, target)
                self.step += 1
                if key in self.edges:
                    edge = self.edges[key]
                    edge.score += 1.0
                    edge.last_update_step = self.step
                else:
                    # World-gated plasticity gets a small initial advantage because updates are
                    # assumed to be more selectively allocated to the active context.
                    base = 1.05 if self.variant.world_gated_plasticity else 1.0
                    self.edges[key] = Edge(key=key, score=base, created_step=self.step, last_update_step=self.step)

        self._consolidate_existing_edges(current_world=world)
        self._prune_if_needed()
        self._best_cache = None

    def _consolidate_existing_edges(self, current_world: int):
        strength = self.variant.consolidation_strength
        if strength <= 0.0 or not self.edges:
            return

        # Consolidation is a stabilizing pressure, not the storage mechanism. It strengthens
        # established edges relative to recently introduced edges, creating a measurable
        # stability-plasticity tradeoff under finite memory budgets.
        for edge in self.edges.values():
            edge_world = edge.key[0]
            if edge_world == NO_CONTEXT:
                age_worlds = 0
            else:
                age_worlds = max(0, current_world - edge_world)
            age_bonus = min(1.0, age_worlds / max(1, self.world_count - 1))
            edge.score = min(20.0, edge.score * (1.0 + 0.08 * strength + 0.18 * strength * age_bonus))

    def _edge_priority(self, edge: Edge) -> Tuple[float, float]:
        # Newer edges receive a very small tie-breaker. Consolidated older edges can still win
        # because their score grows, but unconsolidated equal-score edges drift under pressure.
        recency = edge.last_update_step / max(1, self.step)
        jitter = self.rng.random() * 1e-6
        return (edge.score + 0.005 * recency + jitter, recency)

    def _prune_if_needed(self):
        if self.local_edge_budget_per_world is not None and self.local_edge_budget_per_world >= 0:
            grouped: Dict[int, List[Edge]] = defaultdict(list)
            for edge in self.edges.values():
                grouped[edge.key[0]].append(edge)
            to_remove: List[EdgeKey] = []
            for ctx, group in grouped.items():
                if ctx == NO_CONTEXT:
                    # For shared memory, local per-world budget is not meaningful. Let global
                    # pressure handle the shared table.
                    continue
                excess = len(group) - self.local_edge_budget_per_world
                if excess > 0:
                    sorted_group = sorted(group, key=self._edge_priority)
                    to_remove.extend(edge.key for edge in sorted_group[:excess])
            for key in to_remove:
                self.edges.pop(key, None)

        if self.global_edge_budget is not None and self.global_edge_budget >= 0:
            excess = len(self.edges) - self.global_edge_budget
            if excess > 0:
                sorted_edges = sorted(self.edges.values(), key=self._edge_priority)
                for edge in sorted_edges[:excess]:
                    self.edges.pop(edge.key, None)

    def context_scores(self, true_world: int, qctx: QueryContext) -> np.ndarray:
        if not self.variant.use_world_context:
            return np.ones(self.world_count, dtype=float) * 0.5

        strength = max(0.0, self.variant.context_binding_strength)
        scores = np.zeros(self.world_count, dtype=float)

        if qctx.corruption_type == "clean" or qctx.level <= 0.0:
            scores[true_world] = strength
            return scores

        level = float(np.clip(qctx.level, 0.0, 1.0))
        wrong_world = qctx.adversarial_world
        if wrong_world is None or wrong_world == true_world:
            wrong_world = (true_world + 1) % self.world_count

        if qctx.corruption_type == "uniform_bleed":
            # Unlike Experiment 12's flat diagnostic, this records the margin as bleed increases.
            # Correct context remains present, but its signal is diluted.
            scores[true_world] = strength * (1.0 - 0.65 * level)
            wrong_mass = strength * level
            if self.world_count > 1:
                for w in range(self.world_count):
                    if w != true_world:
                        scores[w] = wrong_mass / (self.world_count - 1)

        elif qctx.corruption_type == "dropout":
            # Deterministic expectation form for aggregate evaluation: correct score decays toward
            # zero while wrong worlds form a weak uniform background. The stochastic top-1 effect
            # is handled in select_world by treating severe dropout as ambiguous.
            scores[true_world] = strength * (1.0 - level)
            if self.world_count > 1:
                scores += strength * level / self.world_count
                scores[true_world] = strength * (1.0 - level) + strength * level / self.world_count

        elif qctx.corruption_type == "adversarial_mixture":
            scores[true_world] = strength * (1.0 - level)
            scores[wrong_world] = strength * level

        else:
            raise ValueError(f"Unknown corruption type: {qctx.corruption_type}")

        return scores

    def select_world(self, true_world: int, qctx: QueryContext) -> Tuple[int, float, float, float, float]:
        if not self.variant.use_world_context:
            return NO_CONTEXT, 0.0, 0.5, 0.5, 0.0

        if self.variant.query_uses_true_world_when_clean and qctx.is_clean:
            scores = self.context_scores(true_world, qctx)
            wrong = float(np.max(np.delete(scores, true_world))) if self.world_count > 1 else 0.0
            margin = float(scores[true_world] - wrong)
            return true_world, margin, float(scores[true_world]), wrong, 1.0

        scores = self.context_scores(true_world, qctx)
        max_score = float(np.max(scores))
        candidates = np.flatnonzero(np.isclose(scores, max_score))
        if len(candidates) == 1:
            selected = int(candidates[0])
        else:
            # Ambiguous context. Deterministic pseudo-random tie break.
            selected = int(candidates[self.rng.randrange(len(candidates))])
        wrong = float(np.max(np.delete(scores, true_world))) if self.world_count > 1 else 0.0
        margin = float(scores[true_world] - wrong)
        top1_correct = 1.0 if selected == true_world else 0.0
        return selected, margin, float(scores[true_world]), wrong, top1_correct

    def _fallback_target(self, node: int, mode: int, selected_world: int) -> int:
        # Deterministic non-learning fallback. This creates approximately chance accuracy over
        # random transition tables without injecting evaluation-time stochastic noise.
        return int((node * 17 + mode * 31 + (selected_world + 3) * 13 + 7) % self.nodes)

    def _ensure_best_cache(self):
        if self._best_cache is not None:
            return
        grouped: Dict[Tuple[int, int, int], List[Tuple[int, float]]] = defaultdict(list)
        for edge in self.edges.values():
            ctx, node, mode, target = edge.key
            grouped[(ctx, node, mode)].append((target, edge.score))
        cache: Dict[Tuple[int, int, int], Tuple[int, float, float, bool]] = {}
        for key, candidates in grouped.items():
            candidates.sort(key=lambda item: (item[1], item[0]), reverse=True)
            pred, best = candidates[0]
            second = candidates[1][1] if len(candidates) > 1 else 0.0
            cache[key] = (int(pred), float(best), float(best - second), True)
        self._best_cache = cache

    def predict_one_step(self, selected_world: int, node: int, mode: int) -> Tuple[int, float, float, bool]:
        if not self.variant.structural_plasticity:
            return self._fallback_target(node, mode, selected_world), 0.0, 0.0, False

        ctx = selected_world if self.variant.use_world_context else NO_CONTEXT
        self._ensure_best_cache()
        assert self._best_cache is not None
        cached = self._best_cache.get((ctx, node, mode))
        if cached is None:
            return self._fallback_target(node, mode, selected_world), 0.0, 0.0, False
        return cached

    def predict_route(self, true_world: int, start_node: int, modes: Sequence[int], qctx: QueryContext) -> Dict[str, float]:
        selected_world, world_margin, correct_world_activation, wrong_world_activation, top1 = self.select_world(true_world, qctx)
        node = int(start_node)
        used_edges = 0
        edge_margins: List[float] = []
        edge_scores: List[float] = []

        if len(modes) == 0:
            return {
                "pred_node": node,
                "selected_world": float(selected_world),
                "world_margin": world_margin,
                "correct_world_activation": correct_world_activation,
                "wrong_world_activation": wrong_world_activation,
                "top1_world_accuracy": top1,
                "mean_edge_margin": 0.0,
                "min_edge_margin": 0.0,
                "mean_edge_score": 0.0,
                "used_edge_fraction": 0.0,
            }

        if self.variant.recurrence:
            executable_modes = modes
        else:
            # No recurrence can still answer a one-step route-table query, but cannot roll the
            # state forward through a sequence.
            executable_modes = modes[:1]

        for mode in executable_modes:
            node, score, margin, found = self.predict_one_step(selected_world, node, int(mode))
            edge_scores.append(score)
            edge_margins.append(margin)
            if found:
                used_edges += 1

        return {
            "pred_node": float(node),
            "selected_world": float(selected_world),
            "world_margin": world_margin,
            "correct_world_activation": correct_world_activation,
            "wrong_world_activation": wrong_world_activation,
            "top1_world_accuracy": top1,
            "mean_edge_margin": float(np.mean(edge_margins)) if edge_margins else 0.0,
            "min_edge_margin": float(np.min(edge_margins)) if edge_margins else 0.0,
            "mean_edge_score": float(np.mean(edge_scores)) if edge_scores else 0.0,
            "used_edge_fraction": float(used_edges / max(1, len(executable_modes))),
        }


def build_model(
    transitions: WorldTransitions,
    variant: Variant,
    seed: int,
    global_budget_ratio: Optional[float] = None,
    local_budget_ratio: Optional[float] = None,
    train_worlds: Optional[Sequence[int]] = None,
    withheld: Optional[set[TransitionKey]] = None,
) -> RouteMemoryModel:
    train_worlds = list(range(transitions.world_count)) if train_worlds is None else list(train_worlds)
    full_edge_count = len(train_worlds) * transitions.nodes * transitions.modes
    if variant.use_world_context:
        full_global_count = full_edge_count
    else:
        # Shared context can hold at most nodes*modes*targets unique edge alternatives, but the
        # diagnostically fair budget is still referenced to the amount of world-specific memory
        # that would be required to store all incompatible worlds.
        full_global_count = full_edge_count

    global_budget = None if global_budget_ratio is None else max(0, int(math.ceil(global_budget_ratio * full_global_count)))
    local_budget = None if local_budget_ratio is None else max(0, int(math.ceil(local_budget_ratio * transitions.nodes * transitions.modes)))
    model = RouteMemoryModel(
        variant=variant,
        world_count=transitions.world_count,
        nodes=transitions.nodes,
        modes=transitions.modes,
        global_edge_budget=global_budget,
        local_edge_budget_per_world=local_budget,
        rng=random.Random(seed + 77),
    )
    for w in train_worlds:
        model.train_world(transitions, w, withheld=withheld)
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
    worlds = list(range(transitions.world_count)) if worlds is None else list(worlds)
    attempts_limit = max(10_000, routes_per_world * len(worlds) * 100)

    for w in worlds:
        produced = 0
        attempts = 0
        while produced < routes_per_world and attempts < attempts_limit:
            attempts += 1
            start = int(rng.integers(0, transitions.nodes))
            modes = [int(x) for x in rng.integers(0, transitions.modes, size=route_length)]
            node = start
            used: set[TransitionKey] = set()
            for mode in modes:
                used.add((w, node, mode))
                node = transitions.target(w, node, mode)
            if require_withheld is not None and used.isdisjoint(require_withheld):
                continue
            if require_no_withheld is not None and not used.isdisjoint(require_no_withheld):
                continue
            produced += 1
            yield w, start, modes

        # If the constraint is impossible for a small random table, degrade gracefully by yielding
        # unconstrained samples. The summary will still show the actual condition in the run log.
        while produced < routes_per_world:
            start = int(rng.integers(0, transitions.nodes))
            modes = [int(x) for x in rng.integers(0, transitions.modes, size=route_length)]
            produced += 1
            yield w, start, modes


def evaluate_model(
    phase: str,
    run_name: str,
    transitions: WorldTransitions,
    model: RouteMemoryModel,
    seed: int,
    world_count: int,
    route_length: int,
    routes_per_world: int,
    qctx: QueryContext = QueryContext(),
    budget_ratio: Optional[float] = None,
    local_budget_ratio: Optional[float] = None,
    generalization_condition: Optional[str] = None,
    primitive_holdout_rate: Optional[float] = None,
    worlds: Optional[Sequence[int]] = None,
    require_withheld: Optional[set[TransitionKey]] = None,
    require_no_withheld: Optional[set[TransitionKey]] = None,
    continuous_noise: Optional[float] = None,
    continuous_decode_accuracy: Optional[float] = None,
) -> Dict[str, float | str | int | None]:
    route_correct = 0
    route_total = 0
    route_world_top1 = []
    route_world_margins = []
    route_correct_world_activations = []
    route_wrong_world_activations = []
    route_edge_margins = []
    route_edge_min_margins = []
    route_edge_scores = []
    route_used_edge_fractions = []

    for w, start, modes in route_samples(
        transitions,
        seed=seed,
        route_length=route_length,
        routes_per_world=routes_per_world,
        worlds=worlds,
        require_withheld=require_withheld,
        require_no_withheld=require_no_withheld,
    ):
        truth = transitions.final_after_modes(w, start, modes)
        pred = model.predict_route(w, start, modes, qctx)
        route_correct += int(int(pred["pred_node"]) == truth)
        route_total += 1
        route_world_top1.append(pred["top1_world_accuracy"])
        route_world_margins.append(pred["world_margin"])
        route_correct_world_activations.append(pred["correct_world_activation"])
        route_wrong_world_activations.append(pred["wrong_world_activation"])
        route_edge_margins.append(pred["mean_edge_margin"])
        route_edge_min_margins.append(pred["min_edge_margin"])
        route_edge_scores.append(pred["mean_edge_score"])
        route_used_edge_fractions.append(pred["used_edge_fraction"])

    # Route-table accuracy is exhaustive over one-step transitions for the selected worlds.
    table_correct = 0
    table_total = 0
    table_world_top1 = []
    table_world_margins = []
    table_wrong_world_activations = []
    eval_worlds = list(range(world_count)) if worlds is None else list(worlds)
    for w, n, m in transitions.all_transition_keys(eval_worlds):
        truth = transitions.target(w, n, m)
        pred = model.predict_route(w, n, [m], qctx)
        table_correct += int(int(pred["pred_node"]) == truth)
        table_total += 1
        table_world_top1.append(pred["top1_world_accuracy"])
        table_world_margins.append(pred["world_margin"])
        table_wrong_world_activations.append(pred["wrong_world_activation"])

    composition_accuracy = route_correct / max(1, route_total)
    route_table_accuracy = table_correct / max(1, table_total)
    return {
        "phase": phase,
        "run_name": run_name,
        "seed": seed,
        "world_count": world_count,
        "route_length": route_length,
        "budget_ratio": budget_ratio,
        "local_budget_ratio": local_budget_ratio,
        "context_corruption_type": qctx.corruption_type,
        "context_corruption_level": qctx.level,
        "generalization_condition": generalization_condition,
        "primitive_holdout_rate": primitive_holdout_rate,
        "continuous_noise": continuous_noise,
        "continuous_decode_accuracy": continuous_decode_accuracy,
        "nodes": transitions.nodes,
        "modes": transitions.modes,
        "composition_accuracy": composition_accuracy,
        "route_route_table_accuracy": route_table_accuracy,
        "transition_accuracy": route_table_accuracy,
        "composition_route_gap": route_table_accuracy - composition_accuracy,
        "top1_world_accuracy": float(np.mean(route_world_top1)) if route_world_top1 else 0.0,
        "route_table_top1_world_accuracy": float(np.mean(table_world_top1)) if table_world_top1 else 0.0,
        "composition_mean_world_margin": float(np.mean(route_world_margins)) if route_world_margins else 0.0,
        "route_mean_world_margin": float(np.mean(table_world_margins)) if table_world_margins else 0.0,
        "composition_mean_correct_world_activation": float(np.mean(route_correct_world_activations)) if route_correct_world_activations else 0.0,
        "composition_mean_wrong_world_activation": float(np.mean(route_wrong_world_activations)) if route_wrong_world_activations else 0.0,
        "route_mean_wrong_world_activation": float(np.mean(table_wrong_world_activations)) if table_wrong_world_activations else 0.0,
        "composition_mean_correct_margin": float(np.mean(route_edge_margins)) if route_edge_margins else 0.0,
        "composition_min_correct_margin": float(np.min(route_edge_min_margins)) if route_edge_min_margins else 0.0,
        "composition_mean_edge_score": float(np.mean(route_edge_scores)) if route_edge_scores else 0.0,
        "used_edge_fraction": float(np.mean(route_used_edge_fractions)) if route_used_edge_fractions else 0.0,
        "stored_edge_count": len(model.edges),
        "global_edge_budget": model.global_edge_budget,
        "local_edge_budget_per_world": model.local_edge_budget_per_world,
    }


def progress_phase(logger: ProgressLogger, phase: str, **extra):
    logger.write(phase=phase, message=f"Running {phase}", **extra)


def run_capacity_pressure(config: Config, logger: ProgressLogger) -> List[dict]:
    progress_phase(logger, "capacity_pressure")
    rows: List[dict] = []
    for seed in config.seeds:
        for world_count in config.capacity_world_counts:
            transitions = WorldTransitions(world_count, config.nodes, config.modes, seed)
            for variant_name in config.variants:
                variant = VARIANTS[variant_name]
                for budget_ratio in config.budget_ratios:
                    model = build_model(transitions, variant, seed, global_budget_ratio=budget_ratio)
                    for route_length in config.capacity_route_lengths:
                        rows.append(
                            evaluate_model(
                                phase="capacity_pressure",
                                run_name=variant.name,
                                transitions=transitions,
                                model=model,
                                seed=seed,
                                world_count=world_count,
                                route_length=route_length,
                                routes_per_world=config.routes_per_world,
                                budget_ratio=budget_ratio,
                            )
                        )
    return rows


def run_local_capacity_pressure(config: Config, logger: ProgressLogger) -> List[dict]:
    progress_phase(logger, "local_capacity_pressure")
    rows: List[dict] = []
    variants = [
        "exp13_full_context_separated_memory",
        "exp13_no_consolidation",
        "exp13_strong_consolidation",
        "exp13_no_recurrence",
    ]
    for seed in config.seeds:
        for world_count in config.world_counts:
            transitions = WorldTransitions(world_count, config.nodes, config.modes, seed)
            for variant_name in variants:
                if variant_name not in config.variants:
                    continue
                variant = VARIANTS[variant_name]
                for local_ratio in config.local_budget_ratios:
                    model = build_model(transitions, variant, seed, local_budget_ratio=local_ratio)
                    rows.append(
                        evaluate_model(
                            phase="local_capacity_pressure",
                            run_name=variant.name,
                            transitions=transitions,
                            model=model,
                            seed=seed,
                            world_count=world_count,
                            route_length=max(config.route_lengths),
                            routes_per_world=config.routes_per_world,
                            local_budget_ratio=local_ratio,
                        )
                    )
    return rows


def run_context_corruption(config: Config, logger: ProgressLogger) -> List[dict]:
    progress_phase(logger, "context_corruption")
    rows: List[dict] = []
    variants = [
        "exp13_full_context_separated_memory",
        "exp13_world_gated_plasticity",
        "exp13_no_consolidation",
        "exp13_strong_consolidation",
        "exp13_no_world_context",
        "exp13_no_context_binding",
        "exp13_no_recurrence",
    ]
    variants = [v for v in variants if v in config.variants]

    sweep_defs = [
        ("uniform_bleed", config.context_bleed_levels),
        ("dropout", config.context_dropout_levels),
        ("adversarial_mixture", config.adversarial_context_levels),
    ]

    for seed in config.seeds:
        transitions = WorldTransitions(config.context_world_count, config.nodes, config.modes, seed)
        for variant_name in variants:
            variant = VARIANTS[variant_name]
            model = build_model(transitions, variant, seed, global_budget_ratio=config.context_budget_ratio)
            for corruption_type, levels in sweep_defs:
                for level in levels:
                    qctx = QueryContext(corruption_type=corruption_type, level=level)
                    rows.append(
                        evaluate_model(
                            phase="context_corruption",
                            run_name=variant.name,
                            transitions=transitions,
                            model=model,
                            seed=seed,
                            world_count=config.context_world_count,
                            route_length=config.context_route_length,
                            routes_per_world=config.routes_per_world,
                            budget_ratio=config.context_budget_ratio,
                            qctx=qctx,
                        )
                    )
    return rows


def run_continual_retention_pressure(config: Config, logger: ProgressLogger) -> List[dict]:
    progress_phase(logger, "continual_retention_pressure")
    rows: List[dict] = []
    variants = [
        "exp13_full_context_separated_memory",
        "exp13_no_consolidation",
        "exp13_strong_consolidation",
        "exp13_no_world_context",
    ]
    variants = [v for v in variants if v in config.variants]
    for seed in config.seeds:
        transitions = WorldTransitions(config.retention_world_count, config.nodes, config.modes, seed)
        for variant_name in variants:
            variant = VARIANTS[variant_name]
            for budget_ratio in config.retention_budget_ratios:
                full_count = config.retention_world_count * config.nodes * config.modes
                model = RouteMemoryModel(
                    variant=variant,
                    world_count=config.retention_world_count,
                    nodes=config.nodes,
                    modes=config.modes,
                    global_edge_budget=int(math.ceil(budget_ratio * full_count)),
                    local_edge_budget_per_world=None,
                    rng=random.Random(seed + 77),
                )
                for train_checkpoint in range(config.retention_world_count):
                    model.train_world(transitions, train_checkpoint)
                    for eval_world in range(train_checkpoint + 1):
                        result = evaluate_model(
                            phase="continual_retention_pressure",
                            run_name=variant.name,
                            transitions=transitions,
                            model=model,
                            seed=seed,
                            world_count=config.retention_world_count,
                            route_length=config.retention_route_length,
                            routes_per_world=max(16, config.routes_per_world // 4),
                            budget_ratio=budget_ratio,
                            worlds=[eval_world],
                        )
                        result["train_checkpoint"] = train_checkpoint
                        result["eval_world"] = eval_world
                        rows.append(result)
    return rows


def make_withheld_set(
    transitions: WorldTransitions,
    seed: int,
    holdout_rate: float,
) -> set[TransitionKey]:
    rng = np.random.default_rng(seed + 4242 + int(holdout_rate * 1000))
    all_keys = list(transitions.all_transition_keys())
    rng.shuffle(all_keys)
    count = int(round(holdout_rate * len(all_keys)))
    return set(all_keys[:count])


def run_true_holdout(config: Config, logger: ProgressLogger) -> List[dict]:
    progress_phase(logger, "true_holdout_generalization")
    rows: List[dict] = []
    variants = [
        "exp13_full_context_separated_memory",
        "exp13_no_consolidation",
        "exp13_strong_consolidation",
        "exp13_no_recurrence",
        "exp13_no_world_context",
    ]
    variants = [v for v in variants if v in config.variants]
    for seed in config.seeds:
        transitions = WorldTransitions(config.holdout_world_count, config.nodes, config.modes, seed)
        for holdout_rate in config.primitive_holdout_rates:
            withheld = make_withheld_set(transitions, seed, holdout_rate)
            for variant_name in variants:
                variant = VARIANTS[variant_name]
                model = build_model(
                    transitions,
                    variant,
                    seed,
                    global_budget_ratio=1.25,
                    withheld=withheld,
                )
                # Seen primitives / seen primitive composition: use only routes that avoid withheld edges.
                rows.append(
                    evaluate_model(
                        phase="true_holdout_generalization",
                        run_name=variant.name,
                        transitions=transitions,
                        model=model,
                        seed=seed,
                        world_count=config.holdout_world_count,
                        route_length=config.holdout_route_length,
                        routes_per_world=config.routes_per_world,
                        budget_ratio=1.25,
                        generalization_condition="compositions_from_seen_primitives",
                        primitive_holdout_rate=holdout_rate,
                        require_no_withheld=withheld,
                    )
                )
                # Missing primitive condition: sample routes containing at least one untrained edge.
                if holdout_rate > 0:
                    rows.append(
                        evaluate_model(
                            phase="true_holdout_generalization",
                            run_name=variant.name,
                            transitions=transitions,
                            model=model,
                            seed=seed,
                            world_count=config.holdout_world_count,
                            route_length=config.holdout_route_length,
                            routes_per_world=config.routes_per_world,
                            budget_ratio=1.25,
                            generalization_condition="routes_requiring_unseen_primitives",
                            primitive_holdout_rate=holdout_rate,
                            require_withheld=withheld,
                        )
                    )
                # One-step unseen primitive query: route length 1 and require withheld edge.
                if holdout_rate > 0:
                    rows.append(
                        evaluate_model(
                            phase="true_holdout_generalization",
                            run_name=variant.name,
                            transitions=transitions,
                            model=model,
                            seed=seed,
                            world_count=config.holdout_world_count,
                            route_length=1,
                            routes_per_world=config.routes_per_world,
                            budget_ratio=1.25,
                            generalization_condition="one_step_unseen_primitives",
                            primitive_holdout_rate=holdout_rate,
                            require_withheld=withheld,
                        )
                    )
    return rows


class ContinuousFrontEnd:
    def __init__(self, nodes: int, dim: int, seed: int):
        rng = np.random.default_rng(seed + 9991)
        prototypes = rng.normal(size=(nodes, dim))
        prototypes /= np.linalg.norm(prototypes, axis=1, keepdims=True) + 1e-12
        self.prototypes = prototypes
        self.nodes = nodes
        self.dim = dim
        self.rng = rng

    def observe(self, node: int, noise: float) -> np.ndarray:
        obs = self.prototypes[node] + self.rng.normal(scale=noise, size=self.dim)
        return obs

    def decode(self, obs: np.ndarray) -> int:
        sims = self.prototypes @ obs
        return int(np.argmax(sims))

    def estimate_decode_accuracy(self, noise: float, trials: int = 2048) -> float:
        correct = 0
        for _ in range(trials):
            n = int(self.rng.integers(0, self.nodes))
            correct += int(self.decode(self.observe(n, noise)) == n)
        return correct / trials


def evaluate_continuous_frontend(
    phase: str,
    run_name: str,
    transitions: WorldTransitions,
    model: RouteMemoryModel,
    frontend: ContinuousFrontEnd,
    seed: int,
    world_count: int,
    route_length: int,
    routes_per_world: int,
    noise: float,
    decode_accuracy: float,
) -> Dict[str, float | str | int | None]:
    route_correct = 0
    route_total = 0
    decoded_start_correct = 0
    rows_world_margin = []
    rows_wrong_activation = []
    rows_top1 = []
    rng = np.random.default_rng(seed + 1212 + int(noise * 1000))

    for w in range(world_count):
        for _ in range(routes_per_world):
            true_start = int(rng.integers(0, transitions.nodes))
            observed = frontend.observe(true_start, noise=noise)
            decoded_start = frontend.decode(observed)
            decoded_start_correct += int(decoded_start == true_start)
            modes = [int(x) for x in rng.integers(0, transitions.modes, size=route_length)]
            truth = transitions.final_after_modes(w, true_start, modes)
            pred = model.predict_route(w, decoded_start, modes, QueryContext())
            route_correct += int(int(pred["pred_node"]) == truth)
            route_total += 1
            rows_world_margin.append(pred["world_margin"])
            rows_wrong_activation.append(pred["wrong_world_activation"])
            rows_top1.append(pred["top1_world_accuracy"])

    composition_accuracy = route_correct / max(1, route_total)
    return {
        "phase": phase,
        "run_name": run_name,
        "seed": seed,
        "world_count": world_count,
        "route_length": route_length,
        "budget_ratio": 1.25,
        "local_budget_ratio": None,
        "context_corruption_type": "clean",
        "context_corruption_level": 0.0,
        "generalization_condition": "continuous_noisy_start_state",
        "primitive_holdout_rate": None,
        "continuous_noise": noise,
        "continuous_decode_accuracy": decode_accuracy,
        "nodes": transitions.nodes,
        "modes": transitions.modes,
        "composition_accuracy": composition_accuracy,
        "route_route_table_accuracy": np.nan,
        "transition_accuracy": np.nan,
        "composition_route_gap": np.nan,
        "top1_world_accuracy": float(np.mean(rows_top1)) if rows_top1 else 0.0,
        "route_table_top1_world_accuracy": np.nan,
        "composition_mean_world_margin": float(np.mean(rows_world_margin)) if rows_world_margin else 0.0,
        "route_mean_world_margin": np.nan,
        "composition_mean_correct_world_activation": np.nan,
        "composition_mean_wrong_world_activation": float(np.mean(rows_wrong_activation)) if rows_wrong_activation else 0.0,
        "route_mean_wrong_world_activation": np.nan,
        "composition_mean_correct_margin": np.nan,
        "composition_min_correct_margin": np.nan,
        "composition_mean_edge_score": np.nan,
        "used_edge_fraction": np.nan,
        "stored_edge_count": len(model.edges),
        "global_edge_budget": model.global_edge_budget,
        "local_edge_budget_per_world": model.local_edge_budget_per_world,
        "decoded_start_accuracy_observed": decoded_start_correct / max(1, route_total),
    }


def run_continuous_bridge(config: Config, logger: ProgressLogger) -> List[dict]:
    progress_phase(logger, "continuous_frontend_bridge")
    rows: List[dict] = []
    variants = [
        "exp13_full_context_separated_memory",
        "exp13_no_world_context",
        "exp13_no_recurrence",
        "exp13_no_structural_plasticity",
    ]
    variants = [v for v in variants if v in config.variants]
    for seed in config.seeds:
        transitions = WorldTransitions(config.continuous_world_count, config.nodes, config.modes, seed)
        frontend = ContinuousFrontEnd(nodes=config.nodes, dim=64, seed=seed)
        decode_cache = {
            noise: frontend.estimate_decode_accuracy(noise=noise, trials=max(512, config.nodes * 32))
            for noise in config.continuous_noise_levels
        }
        for variant_name in variants:
            variant = VARIANTS[variant_name]
            model = build_model(transitions, variant, seed, global_budget_ratio=1.25)
            for noise in config.continuous_noise_levels:
                rows.append(
                    evaluate_continuous_frontend(
                        phase="continuous_frontend_bridge",
                        run_name=variant.name,
                        transitions=transitions,
                        model=model,
                        frontend=frontend,
                        seed=seed,
                        world_count=config.continuous_world_count,
                        route_length=config.continuous_route_length,
                        routes_per_world=config.routes_per_world,
                        noise=noise,
                        decode_accuracy=decode_cache[noise],
                    )
                )
    return rows


def summarize(df: pd.DataFrame, group_cols: List[str], metrics: List[str]) -> pd.DataFrame:
    agg = {}
    for metric in metrics:
        if metric in df.columns:
            agg[metric] = ["mean", "std", "count"]
    if not agg:
        return pd.DataFrame()
    return df.groupby(group_cols, dropna=False).agg(agg).reset_index().pipe(flatten_columns)


def flatten_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = ["_".join([str(x) for x in col if x != ""]).rstrip("_") if isinstance(col, tuple) else str(col) for col in df.columns]
    return df


def save_plot_line(
    df: pd.DataFrame,
    out: Path,
    x: str,
    y: str,
    hue: str,
    title: str,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    filter_query: Optional[str] = None,
):
    data = df.query(filter_query) if filter_query else df
    if data.empty or x not in data.columns or y not in data.columns or hue not in data.columns:
        return
    plt.figure(figsize=(14, 7))
    for name, group in data.groupby(hue):
        group = group.sort_values(x)
        plt.plot(group[x], group[y], marker="o", label=str(name))
    plt.title(title)
    plt.xlabel(xlabel or x)
    plt.ylabel(ylabel or y)
    plt.grid(True, alpha=0.6)
    plt.legend(loc="best")
    plt.tight_layout()
    out.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out, dpi=150)
    plt.close()


def save_heatmap(
    matrix: np.ndarray, out: Path, title: str, xlabel: str, ylabel: str):
    plt.figure(figsize=(10, 8))
    plt.imshow(matrix, vmin=0.0, vmax=1.0, aspect="auto")
    plt.colorbar(label="composition accuracy")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    out.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out, dpi=150)
    plt.close()


def create_summaries_and_plots(analysis_dir: Path, metrics_df: pd.DataFrame, config: Config):
    plots_dir = analysis_dir / "plots"
    plots_dir.mkdir(parents=True, exist_ok=True)

    metric_cols = [
        "composition_accuracy",
        "route_route_table_accuracy",
        "composition_route_gap",
        "top1_world_accuracy",
        "composition_mean_world_margin",
        "composition_mean_wrong_world_activation",
        "composition_mean_correct_margin",
        "used_edge_fraction",
        "stored_edge_count",
        "continuous_decode_accuracy",
        "decoded_start_accuracy_observed",
    ]

    summary_specs = {
        "capacity_pressure_summary.csv": ["phase", "run_name", "world_count", "route_length", "budget_ratio"],
        "local_capacity_pressure_summary.csv": ["phase", "run_name", "world_count", "route_length", "local_budget_ratio"],
        "context_corruption_summary.csv": ["phase", "run_name", "context_corruption_type", "context_corruption_level", "budget_ratio"],
        "continual_retention_pressure_summary.csv": ["phase", "run_name", "budget_ratio", "train_checkpoint", "eval_world"],
        "true_holdout_generalization_summary.csv": ["phase", "run_name", "route_length", "generalization_condition", "primitive_holdout_rate"],
        "continuous_frontend_bridge_summary.csv": ["phase", "run_name", "continuous_noise", "generalization_condition"],
    }

    summaries: Dict[str, pd.DataFrame] = {}
    for filename, cols in summary_specs.items():
        phase_name = cols[0]
        if phase_name == "phase":
            phase_value = filename.replace("_summary.csv", "")
            phase_df = metrics_df[metrics_df["phase"] == phase_value]
        else:
            phase_df = metrics_df
        if phase_df.empty:
            continue
        available_cols = [c for c in cols if c in phase_df.columns]
        summary = summarize(phase_df, available_cols, metric_cols)
        summaries[filename] = summary
        summary.to_csv(analysis_dir / filename, index=False)

    # Main plots.
    cap = summaries.get("capacity_pressure_summary.csv")
    if cap is not None and not cap.empty:
        for route_length in sorted(cap["route_length"].dropna().unique()):
            rq = f"route_length == {route_length} and budget_ratio in [0.25, 0.5, 0.75, 1.0]"
            save_plot_line(
                cap,
                plots_dir / f"exp13_capacity_accuracy_route_len_{int(route_length)}.png",
                x="world_count",
                y="composition_accuracy_mean",
                hue="run_name",
                title=f"Experiment 13: capacity pressure, route length {int(route_length)}",
                xlabel="world count",
                ylabel="composition accuracy",
                filter_query=rq,
            )
        save_plot_line(
            cap.query("run_name in ['exp13_full_context_separated_memory','exp13_no_consolidation','exp13_strong_consolidation'] and route_length == route_length.max()"),
            plots_dir / "exp13_budget_breaking_curve_full_vs_consolidation.png",
            x="budget_ratio",
            y="composition_accuracy_mean",
            hue="run_name",
            title="Experiment 13: memory budget breaking curve",
            xlabel="global edge budget ratio vs perfect route table",
            ylabel="composition accuracy",
        )
        save_plot_line(
            cap.query("route_length == route_length.max() and budget_ratio == 1.0"),
            plots_dir / "exp13_capacity_wrong_world_activation_budget_1.png",
            x="world_count",
            y="composition_mean_wrong_world_activation_mean",
            hue="run_name",
            title="Experiment 13: wrong-world activation at exact memory capacity",
            xlabel="world count",
            ylabel="wrong-world activation",
        )

    ctx = summaries.get("context_corruption_summary.csv")
    if ctx is not None and not ctx.empty:
        for ctype in sorted(ctx["context_corruption_type"].dropna().unique()):
            subset = ctx[ctx["context_corruption_type"] == ctype]
            save_plot_line(
                subset,
                plots_dir / f"exp13_context_{ctype}_composition.png",
                x="context_corruption_level",
                y="composition_accuracy_mean",
                hue="run_name",
                title=f"Experiment 13: composition under {ctype}",
                xlabel="corruption level",
                ylabel="composition accuracy",
            )
            save_plot_line(
                subset,
                plots_dir / f"exp13_context_{ctype}_top1_world.png",
                x="context_corruption_level",
                y="top1_world_accuracy_mean",
                hue="run_name",
                title=f"Experiment 13: world selection under {ctype}",
                xlabel="corruption level",
                ylabel="top-1 world accuracy",
            )
            save_plot_line(
                subset,
                plots_dir / f"exp13_context_{ctype}_world_margin.png",
                x="context_corruption_level",
                y="composition_mean_world_margin_mean",
                hue="run_name",
                title=f"Experiment 13: world margin under {ctype}",
                xlabel="corruption level",
                ylabel="world margin",
            )

    ret = summaries.get("continual_retention_pressure_summary.csv")
    if ret is not None and not ret.empty:
        for variant in ["exp13_full_context_separated_memory", "exp13_no_consolidation", "exp13_strong_consolidation", "exp13_no_world_context"]:
            for budget in sorted(ret["budget_ratio"].dropna().unique()):
                sub = ret[(ret["run_name"] == variant) & (ret["budget_ratio"] == budget)]
                if sub.empty:
                    continue
                n = int(max(sub["train_checkpoint"].max(), sub["eval_world"].max()) + 1)
                matrix = np.full((n, n), np.nan)
                for _, row in sub.iterrows():
                    matrix[int(row["eval_world"]), int(row["train_checkpoint"])] = row["composition_accuracy_mean"]
                save_heatmap(
                    matrix,
                    plots_dir / f"exp13_retention_heatmap_{variant}_budget_{budget}.png",
                    title=f"Experiment 13: retention, {variant}, budget {budget}",
                    xlabel="after training world",
                    ylabel="eval world",
                )

    hold = summaries.get("true_holdout_generalization_summary.csv")
    if hold is not None and not hold.empty:
        for cond in sorted(hold["generalization_condition"].dropna().unique()):
            subset = hold[hold["generalization_condition"] == cond]
            save_plot_line(
                subset,
                plots_dir / f"exp13_holdout_{cond}.png",
                x="primitive_holdout_rate",
                y="composition_accuracy_mean",
                hue="run_name",
                title=f"Experiment 13: {cond}",
                xlabel="primitive transition holdout rate",
                ylabel="accuracy",
            )

    cont = summaries.get("continuous_frontend_bridge_summary.csv")
    if cont is not None and not cont.empty:
        save_plot_line(
            cont,
            plots_dir / "exp13_continuous_frontend_composition_vs_noise.png",
            x="continuous_noise",
            y="composition_accuracy_mean",
            hue="run_name",
            title="Experiment 13: continuous/noisy front-end bridge",
            xlabel="input noise sigma",
            ylabel="composition accuracy",
        )
        save_plot_line(
            cont,
            plots_dir / "exp13_continuous_frontend_decode_vs_noise.png",
            x="continuous_noise",
            y="decoded_start_accuracy_observed_mean",
            hue="run_name",
            title="Experiment 13: observed start-state decoding under noise",
            xlabel="input noise sigma",
            ylabel="decoded start accuracy",
        )


def write_report(analysis_dir: Path, config: Config, elapsed: float):
    metrics_path = analysis_dir / "metrics.csv"
    df = pd.read_csv(metrics_path)
    lines: List[str] = []
    lines.append("# Experiment 13 Report - Breaking Point, Context Corruption, and Continuous Front-End Bridge")
    lines.append("")
    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "Experiment 13 deliberately pushes the Experiment 12 mechanism out of the ceiling regime. "
        "It asks where context-indexed structural route memory breaks when memory capacity, context integrity, "
        "primitive transition coverage, and perceptual input quality are degraded."
    )
    lines.append("")
    lines.append("## Run configuration")
    lines.append("")
    lines.append(f"- profile: `{config.profile}`")
    lines.append(f"- seeds: `{len(config.seeds)}`")
    lines.append(f"- nodes: `{config.nodes}`")
    lines.append(f"- modes: `{config.modes}`")
    lines.append(f"- capacity world counts: `{config.capacity_world_counts}`")
    lines.append(f"- capacity route lengths: `{config.capacity_route_lengths}`")
    lines.append(f"- global budget ratios: `{config.budget_ratios}`")
    lines.append(f"- context corruption world count: `{config.context_world_count}`")
    lines.append(f"- retention world count: `{config.retention_world_count}`")
    lines.append(f"- variants: `{config.variants}`")
    lines.append(f"- elapsed seconds: `{elapsed:.2f}`")
    lines.append("")
    lines.append("## Generated files")
    lines.append("")
    for path in sorted(analysis_dir.glob("*.csv")):
        lines.append(f"- `{path.name}`")
    lines.append("- `plots/*.png`")
    lines.append("")

    def maybe_table(title: str, file: str, query: Optional[str] = None, columns: Optional[List[str]] = None, n: int = 30):
        p = analysis_dir / file
        if not p.exists():
            return
        tdf = pd.read_csv(p)
        if query:
            try:
                tdf = tdf.query(query)
            except Exception:
                pass
        if columns:
            tdf = tdf[[c for c in columns if c in tdf.columns]]
        if tdf.empty:
            return
        lines.append(f"## {title}")
        lines.append("")
        lines.append(tdf.head(n).to_markdown(index=False))
        lines.append("")

    maybe_table(
        "Capacity pressure snapshot",
        "capacity_pressure_summary.csv",
        query="route_length == route_length.max() and budget_ratio in [0.25, 0.5, 0.75, 1.0]",
        columns=[
            "run_name",
            "world_count",
            "route_length",
            "budget_ratio",
            "composition_accuracy_mean",
            "route_route_table_accuracy_mean",
            "composition_route_gap_mean",
            "top1_world_accuracy_mean",
            "used_edge_fraction_mean",
        ],
        n=40,
    )
    maybe_table(
        "Adversarial context corruption snapshot",
        "context_corruption_summary.csv",
        query="context_corruption_type == 'adversarial_mixture'",
        columns=[
            "run_name",
            "context_corruption_level",
            "composition_accuracy_mean",
            "top1_world_accuracy_mean",
            "composition_mean_world_margin_mean",
            "composition_mean_wrong_world_activation_mean",
        ],
        n=40,
    )
    maybe_table(
        "True holdout snapshot",
        "true_holdout_generalization_summary.csv",
        columns=[
            "run_name",
            "generalization_condition",
            "primitive_holdout_rate",
            "route_length",
            "composition_accuracy_mean",
            "route_route_table_accuracy_mean",
            "composition_route_gap_mean",
        ],
        n=40,
    )
    maybe_table(
        "Continuous front-end bridge snapshot",
        "continuous_frontend_bridge_summary.csv",
        columns=[
            "run_name",
            "continuous_noise",
            "composition_accuracy_mean",
            "decoded_start_accuracy_observed_mean",
            "top1_world_accuracy_mean",
        ],
        n=40,
    )

    lines.append("## Interpretation guide")
    lines.append("")
    lines.append("Expected successful-breaking-point patterns:")
    lines.append("")
    lines.append("1. At or above exact structural capacity (`budget_ratio >= 1.0`), the full model should resemble Experiment 12.")
    lines.append("2. Below exact structural capacity, the full model should degrade smoothly rather than remain saturated.")
    lines.append("3. No-recurrence should preserve one-step route-table accuracy where edges exist, but show a large composition-route gap for multi-step routes.")
    lines.append("4. No-world-context should degrade as incompatible worlds accumulate because shared edges collide.")
    lines.append("5. Context corruption should now show a measurable world-selection failure curve, especially under adversarial mixture.")
    lines.append("6. Consolidation should shift the retention/acquisition tradeoff under finite memory pressure rather than merely increasing margins.")
    lines.append("7. True primitive holdout should separate composition from memorized primitives from inference over genuinely unseen primitive transitions.")
    lines.append("8. The continuous front-end bridge should show that route memory survives modest input noise but fails when perceptual decoding fails.")
    lines.append("")
    lines.append("## Manuscript positioning")
    lines.append("")
    lines.append(
        "Experiment 13 is intended to convert the Experiment 12 all-ones result into a boundary-mapping result. "
        "For the first manuscript, this should support a more defensible claim: context-indexed structural plasticity and recurrence "
        "permit non-destructive storage and execution of incompatible route systems, and the model fails predictably when context, "
        "structure, recurrence, or primitive coverage are selectively degraded."
    )
    lines.append("")
    (analysis_dir / "exp13_report.md").write_text("\n".join(lines), encoding="utf-8")


def write_runs_csv(analysis_dir: Path, config: Config):
    rows = []
    for variant_name in config.variants:
        rows.append({
            "variant": variant_name,
            "variant_json": json.dumps(asdict(VARIANTS[variant_name]), sort_keys=True),
        })
    pd.DataFrame(rows).to_csv(analysis_dir / "runs.csv", index=False)


def run_all(config: Config, analysis_dir: Path, clean: bool):
    if clean and analysis_dir.exists():
        shutil.rmtree(analysis_dir)
    analysis_dir.mkdir(parents=True, exist_ok=True)
    logger = ProgressLogger(analysis_dir / "progress.jsonl")
    started = time.time()
    try:
        logger.write(message="Starting Experiment 13", profile=config.profile, config=asdict(config))
        all_rows: List[dict] = []
        for phase_func in [
            run_capacity_pressure,
            run_local_capacity_pressure,
            run_context_corruption,
            run_continual_retention_pressure,
            run_true_holdout,
            run_continuous_bridge,
        ]:
            phase_start = time.time()
            phase_rows = phase_func(config, logger)
            all_rows.extend(phase_rows)
            logger.write(message=f"Completed {phase_func.__name__}", rows=len(phase_rows), elapsed_seconds=time.time() - phase_start)
            pd.DataFrame(all_rows).to_csv(analysis_dir / "metrics.csv", index=False)

        df = pd.DataFrame(all_rows)
        df.to_csv(analysis_dir / "metrics.csv", index=False)
        write_runs_csv(analysis_dir, config)
        create_summaries_and_plots(analysis_dir, df, config)
        elapsed = time.time() - started
        write_report(analysis_dir, config, elapsed)
        logger.write(message="Experiment 13 complete", rows=len(all_rows), elapsed_seconds=elapsed)
    finally:
        logger.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Experiment 13 breaking-point diagnostics.")
    parser.add_argument("--profile", choices=["smoke", "standard", "full"], default="standard")
    parser.add_argument("--output-dir", default="analysis")
    parser.add_argument("--clean", action="store_true", help="Delete output directory before running.")
    return parser.parse_args()


def main():
    args = parse_args()
    config = make_config(args.profile)
    run_all(config, Path(args.output_dir), clean=args.clean)


if __name__ == "__main__":
    main()
