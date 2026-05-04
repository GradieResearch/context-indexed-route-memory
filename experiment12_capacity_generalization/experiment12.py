#!/usr/bin/env python3
"""
Experiment 12: Capacity, Interference, and Compositional Generalization of
Context-Separated Route Memory.

This experiment extends Experiment 11 from a two-/four-world demonstration into a
capacity and robustness study.  It deliberately keeps the synthetic route-world
substrate small enough to run locally while producing the analyses needed for a
first manuscript draft:

1. many-world capacity scaling;
2. continual retention matrices after each newly learned world;
3. held-out multi-step compositional generalization from trained one-step routes;
4. context bleed/dropout robustness;
5. consolidation pressure sweep.

The model is a mechanistic plastic route-memory simulator rather than a gradient-
trained neural net.  That is intentional for this stage: the aim is to isolate the
computational roles discovered in Experiment 11 before moving to larger image or
multimodal substrates.
"""
from __future__ import annotations

import argparse
import dataclasses
import json
import math
import os
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# -----------------------------
# Configuration objects
# -----------------------------


@dataclass(frozen=True)
class Variant:
    name: str
    structural_plasticity: bool = True
    world_context: bool = True
    context_binding: bool = True
    recurrence: bool = True
    inhibition: bool = True
    shared_edges_only: bool = False
    world_gated_plasticity: bool = False
    learning_rate: float = 1.0
    world_update_fraction: float = 1.0
    shared_update_fraction: float = 0.04
    consolidation_strength: float = 0.12
    consolidation_pull: float = 0.025
    wrong_mode_inhibition: float = 0.05
    wrong_world_inhibition: float = 0.05
    clip_min: float = -2.0
    clip_max: float = 6.0
    homeostasis: bool = True

    def to_json(self) -> str:
        return json.dumps(dataclasses.asdict(self), sort_keys=True)


@dataclass(frozen=True)
class RunConfig:
    out_dir: Path
    profile: str
    seeds: int
    world_counts: Tuple[int, ...]
    route_lengths: Tuple[int, ...]
    nodes: int
    modes: int
    variants: Tuple[str, ...]
    context_bleeds: Tuple[float, ...]
    context_dropouts: Tuple[float, ...]
    consolidation_strengths: Tuple[float, ...]
    consolidation_world_counts: Tuple[int, ...]
    default_eval_steps: int
    verbose: bool = True


def build_variants() -> Dict[str, Variant]:
    base = Variant(name="exp12_full_context_separated_memory")
    return {
        base.name: base,
        "exp12_world_gated_plasticity": dataclasses.replace(
            base,
            name="exp12_world_gated_plasticity",
            learning_rate=1.2,
            consolidation_strength=0.05,
            shared_update_fraction=0.0,
            world_gated_plasticity=True,
        ),
        "exp12_no_consolidation": dataclasses.replace(
            base,
            name="exp12_no_consolidation",
            consolidation_strength=0.0,
            consolidation_pull=0.0,
        ),
        "exp12_no_inhibition": dataclasses.replace(
            base,
            name="exp12_no_inhibition",
            inhibition=False,
            wrong_mode_inhibition=0.0,
            wrong_world_inhibition=0.0,
        ),
        "exp12_no_world_context": dataclasses.replace(
            base,
            name="exp12_no_world_context",
            world_context=False,
            shared_update_fraction=1.0,
            consolidation_strength=0.0,
            consolidation_pull=0.0,
        ),
        "exp12_shared_edges_only": dataclasses.replace(
            base,
            name="exp12_shared_edges_only",
            shared_edges_only=True,
            shared_update_fraction=1.0,
            consolidation_strength=0.0,
            consolidation_pull=0.0,
        ),
        "exp12_no_context_binding": dataclasses.replace(
            base,
            name="exp12_no_context_binding",
            context_binding=False,
            shared_update_fraction=0.04,
            consolidation_strength=0.05,
        ),
        "exp12_no_recurrence": dataclasses.replace(
            base,
            name="exp12_no_recurrence",
            recurrence=False,
        ),
        "exp12_no_structural_plasticity": dataclasses.replace(
            base,
            name="exp12_no_structural_plasticity",
            structural_plasticity=False,
            consolidation_strength=0.0,
            consolidation_pull=0.0,
        ),
        "exp12_strong_consolidation": dataclasses.replace(
            base,
            name="exp12_strong_consolidation",
            consolidation_strength=0.8,
            consolidation_pull=0.12,
            shared_update_fraction=0.12,
            clip_max=8.0,
        ),
    }


CORE_VARIANTS = (
    "exp12_full_context_separated_memory",
    "exp12_world_gated_plasticity",
    "exp12_no_consolidation",
    "exp12_no_world_context",
    "exp12_no_context_binding",
    "exp12_no_recurrence",
    "exp12_no_structural_plasticity",
    "exp12_strong_consolidation",
)

ALL_VARIANTS = tuple(build_variants().keys())


# -----------------------------
# Synthetic route-world substrate
# -----------------------------


def generate_world_routes(seed: int, world_count: int, modes: int, nodes: int) -> np.ndarray:
    """Create incompatible per-world, per-mode permutations.

    routes[world, mode, source] -> target.
    Every mode in every world is a permutation over nodes.  Independent
    permutations create high cross-world incompatibility while preserving a
    clean local transition rule.
    """
    rng = np.random.default_rng(seed)
    routes = np.empty((world_count, modes, nodes), dtype=np.int64)
    for w in range(world_count):
        for m in range(modes):
            perm = rng.permutation(nodes)
            # Avoid trivial identity-heavy routes.  A few fixed points are fine,
            # but too many would make the no-recurrence ablation look better than
            # it should.  Rotate until fewer than ~10% are fixed.
            attempts = 0
            while np.mean(perm == np.arange(nodes)) > 0.10 and attempts < 8:
                perm = rng.permutation(nodes)
                attempts += 1
            if np.mean(perm == np.arange(nodes)) > 0.10:
                perm = np.roll(perm, 1)
            routes[w, m] = perm
    return routes


# -----------------------------
# Mechanistic plastic route memory model
# -----------------------------


class PlasticRouteMemory:
    def __init__(self, variant: Variant, routes: np.ndarray, seed: int):
        self.variant = variant
        self.routes = routes
        self.world_count, self.modes, self.nodes = routes.shape
        self.rng = np.random.default_rng(seed + 100_003)
        noise = self.rng.normal(0.0, 1e-4, size=(self.world_count, self.modes, self.nodes, self.nodes))
        self.world_weights = noise.astype(np.float64)
        self.shared_weights = self.rng.normal(0.0, 1e-4, size=(self.modes, self.nodes, self.nodes)).astype(np.float64)
        # For the no-context-binding ablation, simulate a stable but wrong/blurred
        # binding map: training updates exist, but evaluation does not address the
        # correct context-specific route field.
        if self.world_count > 1:
            self.binding_map = np.roll(np.arange(self.world_count), 1)
        else:
            self.binding_map = np.arange(self.world_count)

    def train_world(self, world_id: int) -> None:
        v = self.variant
        if not v.structural_plasticity:
            self._clip()
            return

        lr = v.learning_rate
        source_idx = np.arange(self.nodes)

        # Shared-edges and no-world-context variants intentionally collapse all
        # worlds into a single global route table.  Later worlds overwrite earlier
        # incompatible mappings, reproducing the destructive-rebinding control.
        update_shared_as_primary = (not v.world_context) or v.shared_edges_only

        for mode in range(self.modes):
            targets = self.routes[world_id, mode]

            if update_shared_as_primary:
                self.shared_weights[mode, source_idx, :] *= 0.0
                self.shared_weights[mode, source_idx, targets] += lr
            else:
                # Normal context-separated route learning updates the addressed
                # world.  If binding is disabled, distribute the update across a
                # wrong/blurred address, creating local transition traces without
                # reliable world retrieval.
                if v.context_binding:
                    addressed_worlds = [world_id]
                    fractions = [v.world_update_fraction]
                else:
                    wrong_world = int(self.binding_map[world_id])
                    addressed_worlds = [wrong_world, world_id]
                    fractions = [0.70 * v.world_update_fraction, 0.30 * v.world_update_fraction]

                for addressed_world, frac in zip(addressed_worlds, fractions):
                    self.world_weights[addressed_world, mode, source_idx, targets] += lr * frac

                if v.shared_update_fraction > 0.0 and not v.world_gated_plasticity:
                    self.shared_weights[mode, source_idx, targets] += lr * v.shared_update_fraction

                if v.inhibition:
                    self._apply_inhibition(world_id, mode, targets)

        self._consolidate_world(world_id)
        self._clip()

    def _apply_inhibition(self, world_id: int, mode: int, targets: np.ndarray) -> None:
        v = self.variant
        source_idx = np.arange(self.nodes)
        if not v.world_context or v.shared_edges_only:
            return
        # Suppress the same source->target association in wrong modes and wrong
        # worlds.  This is intentionally mild; Experiment 11 already showed that
        # inhibition should not be necessary in the easy regime.
        if v.wrong_mode_inhibition > 0.0 and self.modes > 1:
            for other_mode in range(self.modes):
                if other_mode != mode:
                    self.world_weights[world_id, other_mode, source_idx, targets] -= v.wrong_mode_inhibition
        if v.wrong_world_inhibition > 0.0 and self.world_count > 1:
            for other_world in range(self.world_count):
                if other_world != world_id:
                    self.world_weights[other_world, mode, source_idx, targets] -= v.wrong_world_inhibition

    def _consolidate_world(self, world_id: int) -> None:
        v = self.variant
        if v.consolidation_strength <= 0.0:
            return
        if not v.structural_plasticity:
            return

        source_idx = np.arange(self.nodes)
        if v.world_context and not v.shared_edges_only:
            # Pull non-selected target alternatives toward zero, then reinforce
            # learned edges.  With excessive consolidation plus shared updates,
            # older worlds can become too rigid/noisy under high capacity.
            if v.consolidation_pull > 0.0:
                self.world_weights[world_id] *= (1.0 - v.consolidation_pull)
            for mode in range(self.modes):
                targets = self.routes[world_id, mode]
                self.world_weights[world_id, mode, source_idx, targets] += v.consolidation_strength
                if v.shared_update_fraction > 0.0 and not v.world_gated_plasticity:
                    self.shared_weights[mode, source_idx, targets] += v.consolidation_strength * v.shared_update_fraction
        else:
            if v.consolidation_pull > 0.0:
                self.shared_weights *= (1.0 - v.consolidation_pull)
            for mode in range(self.modes):
                targets = self.routes[world_id, mode]
                self.shared_weights[mode, source_idx, targets] += v.consolidation_strength

    def _clip(self) -> None:
        v = self.variant
        if not v.homeostasis:
            return
        np.clip(self.world_weights, v.clip_min, v.clip_max, out=self.world_weights)
        np.clip(self.shared_weights, v.clip_min, v.clip_max, out=self.shared_weights)

    def score_matrix(self, world_id: int, context_bleed: float = 0.0, context_dropout: float = 0.0) -> np.ndarray:
        """Return scores[mode, source, target] for the requested world context."""
        v = self.variant
        if (not v.world_context) or v.shared_edges_only:
            return self.shared_weights.copy()

        if not v.context_binding:
            # Context exists but cannot bind to the correct world-specific route
            # field.  Retrieval uses a blurred/wrong address plus shared traces.
            wrong_world = int(self.binding_map[world_id])
            blurred = 0.65 * self.world_weights[wrong_world] + 0.35 * self.world_weights.mean(axis=0)
            return blurred + self.shared_weights

        correct = self.world_weights[world_id]
        if self.world_count > 1:
            other_mean = (self.world_weights.sum(axis=0) - correct) / (self.world_count - 1)
        else:
            other_mean = np.zeros_like(correct)
        global_mean = self.world_weights.mean(axis=0)
        bleed = (1.0 - context_bleed) * correct + context_bleed * other_mean
        dropped = (1.0 - context_dropout) * bleed + context_dropout * global_mean
        return dropped + self.shared_weights

    def evaluate_world(
        self,
        world_id: int,
        route_length: int,
        context_bleed: float = 0.0,
        context_dropout: float = 0.0,
    ) -> Dict[str, float]:
        scores = self.score_matrix(world_id, context_bleed, context_dropout)
        pred_next = scores.argmax(axis=-1)  # [mode, source]
        true_next = self.routes[world_id]

        route_table_accuracy = float(np.mean(pred_next == true_next))
        transition_accuracy = route_table_accuracy

        source_idx = np.arange(self.nodes)[None, :]
        mode_idx = np.arange(self.modes)[:, None]
        correct_scores = scores[mode_idx, source_idx, true_next]
        masked = scores.copy()
        masked[mode_idx, source_idx, true_next] = -np.inf
        best_wrong_scores = masked.max(axis=-1)
        route_mean_correct_margin = float(np.mean(correct_scores - best_wrong_scores))
        route_min_correct_margin = float(np.min(correct_scores - best_wrong_scores))

        # Composition from trained one-step transitions.  The model has never been
        # given explicit multi-step labels; all route_length > 1 tests are held-out
        # compositions.  No recurrence leaves the transition table intact but blocks
        # iterative rollout.
        current_pred = np.tile(np.arange(self.nodes, dtype=np.int64), (self.modes, 1))
        if self.variant.recurrence:
            for _ in range(route_length):
                current_pred = pred_next[mode_idx, current_pred]
        else:
            # Single-step-only execution: it can answer local transitions but cannot
            # recursively feed its own output back into the route field.
            current_pred = pred_next

        current_true = np.tile(np.arange(self.nodes, dtype=np.int64), (self.modes, 1))
        for _ in range(route_length):
            current_true = true_next[mode_idx, current_true]
        composition_accuracy = float(np.mean(current_pred == current_true))

        # Composition margin: score at first local transition is still a useful
        # proxy for confidence, while composition accuracy is the behavioral test.
        composition_mean_correct_margin = route_mean_correct_margin
        composition_min_correct_margin = route_min_correct_margin

        world_margin, wrong_world_activation = self._world_separation_metrics(world_id, true_next)

        return {
            "composition_accuracy": composition_accuracy,
            "route_route_table_accuracy": route_table_accuracy,
            "transition_accuracy": transition_accuracy,
            "composition_mean_correct_margin": composition_mean_correct_margin,
            "composition_min_correct_margin": composition_min_correct_margin,
            "route_mean_correct_margin": route_mean_correct_margin,
            "route_min_correct_margin": route_min_correct_margin,
            "composition_mean_world_margin": world_margin,
            "route_mean_world_margin": world_margin,
            "composition_mean_wrong_world_activation": wrong_world_activation,
            "route_mean_wrong_world_activation": wrong_world_activation,
            "composition_route_gap": route_table_accuracy - composition_accuracy,
        }

    def _world_separation_metrics(self, world_id: int, true_next: np.ndarray) -> Tuple[float, float]:
        v = self.variant
        if (not v.world_context) or v.shared_edges_only:
            return (float("nan"), 0.50)

        source_idx = np.arange(self.nodes)[None, :]
        mode_idx = np.arange(self.modes)[:, None]
        # edge_scores_by_world[w, mode, source]
        edge_scores = self.world_weights[:, mode_idx, source_idx, true_next]
        correct = edge_scores[world_id]
        if self.world_count > 1:
            others = np.delete(edge_scores, world_id, axis=0)
            wrong_max = others.max(axis=0)
        else:
            wrong_max = np.zeros_like(correct)
        world_margin = float(np.mean(correct - wrong_max))

        # Probability mass assigned to the strongest wrong world for the correct
        # edge.  Lower is cleaner separation; higher means wrong-world activation.
        shifted = edge_scores - edge_scores.max(axis=0, keepdims=True)
        probs = np.exp(shifted)
        probs = probs / probs.sum(axis=0, keepdims=True)
        if self.world_count > 1:
            wrong_probs = np.delete(probs, world_id, axis=0)
            wrong_activation = float(np.mean(wrong_probs.max(axis=0)))
        else:
            wrong_activation = 0.0
        return world_margin, wrong_activation


# -----------------------------
# Runner
# -----------------------------


class Experiment12Runner:
    def __init__(self, cfg: RunConfig):
        self.cfg = cfg
        self.variants = build_variants()
        unknown = [v for v in cfg.variants if v not in self.variants]
        if unknown:
            raise ValueError(f"Unknown variants: {unknown}. Available: {sorted(self.variants)}")
        self.metrics: List[Dict[str, object]] = []
        self.run_rows: List[Dict[str, object]] = []
        self.progress_path = cfg.out_dir / "progress.jsonl"
        cfg.out_dir.mkdir(parents=True, exist_ok=True)
        (cfg.out_dir / "plots").mkdir(parents=True, exist_ok=True)

    def run(self) -> None:
        start = time.time()
        total_jobs = len(self.cfg.variants) * self.cfg.seeds * len(self.cfg.world_counts)
        completed = 0
        for variant_name in self.cfg.variants:
            variant = self.variants[variant_name]
            for seed in range(self.cfg.seeds):
                for world_count in self.cfg.world_counts:
                    job_start = time.time()
                    self._run_core_model(variant, seed, world_count)
                    completed += 1
                    self._progress(
                        event="core_job_completed",
                        completed=completed,
                        total=total_jobs,
                        variant=variant.name,
                        seed=seed,
                        world_count=world_count,
                        seconds=time.time() - job_start,
                        elapsed_seconds=time.time() - start,
                    )

        self._run_consolidation_pressure(start)
        self._write_outputs(start)

    def _run_core_model(self, variant: Variant, seed: int, world_count: int) -> None:
        routes = generate_world_routes(seed=seed, world_count=world_count, modes=self.cfg.modes, nodes=self.cfg.nodes)
        model = PlasticRouteMemory(variant=variant, routes=routes, seed=seed)

        # Continual learning: A -> B -> C -> ...; after each newly learned world,
        # re-test every world learned so far.  This produces the retention matrix.
        for train_world in range(world_count):
            model.train_world(train_world)
            for eval_world in range(train_world + 1):
                m = model.evaluate_world(eval_world, route_length=self.cfg.default_eval_steps)
                self._append_metric(
                    m,
                    phase="continual_retention",
                    variant=variant,
                    seed=seed,
                    world_count=world_count,
                    route_length=self.cfg.default_eval_steps,
                    train_checkpoint=train_world,
                    eval_world=eval_world,
                    context_bleed=0.0,
                    context_dropout=0.0,
                    consolidation_strength=variant.consolidation_strength,
                )

        # Final capacity and route length sweep.
        for route_length in self.cfg.route_lengths:
            for eval_world in range(world_count):
                m = model.evaluate_world(eval_world, route_length=route_length)
                self._append_metric(
                    m,
                    phase="capacity_final",
                    variant=variant,
                    seed=seed,
                    world_count=world_count,
                    route_length=route_length,
                    train_checkpoint=world_count - 1,
                    eval_world=eval_world,
                    context_bleed=0.0,
                    context_dropout=0.0,
                    consolidation_strength=variant.consolidation_strength,
                )

                gen_phase = "seen_one_step" if route_length == 1 else "heldout_multistep"
                self._append_metric(
                    m,
                    phase="heldout_generalization",
                    variant=variant,
                    seed=seed,
                    world_count=world_count,
                    route_length=route_length,
                    train_checkpoint=world_count - 1,
                    eval_world=eval_world,
                    context_bleed=0.0,
                    context_dropout=0.0,
                    consolidation_strength=variant.consolidation_strength,
                    generalization_condition=gen_phase,
                )

        # Context bleed sweep, holding dropout at zero.
        for bleed in self.cfg.context_bleeds:
            for eval_world in range(world_count):
                m = model.evaluate_world(eval_world, route_length=self.cfg.default_eval_steps, context_bleed=bleed)
                self._append_metric(
                    m,
                    phase="context_bleed",
                    variant=variant,
                    seed=seed,
                    world_count=world_count,
                    route_length=self.cfg.default_eval_steps,
                    train_checkpoint=world_count - 1,
                    eval_world=eval_world,
                    context_bleed=bleed,
                    context_dropout=0.0,
                    consolidation_strength=variant.consolidation_strength,
                )

        # Context dropout sweep, holding bleed at zero.
        for dropout in self.cfg.context_dropouts:
            for eval_world in range(world_count):
                m = model.evaluate_world(eval_world, route_length=self.cfg.default_eval_steps, context_dropout=dropout)
                self._append_metric(
                    m,
                    phase="context_dropout",
                    variant=variant,
                    seed=seed,
                    world_count=world_count,
                    route_length=self.cfg.default_eval_steps,
                    train_checkpoint=world_count - 1,
                    eval_world=eval_world,
                    context_bleed=0.0,
                    context_dropout=dropout,
                    consolidation_strength=variant.consolidation_strength,
                )

        self.run_rows.append(
            {
                "variant": variant.name,
                "seed": seed,
                "world_count": world_count,
                "nodes": self.cfg.nodes,
                "modes": self.cfg.modes,
                "variant_json": variant.to_json(),
            }
        )

    def _run_consolidation_pressure(self, experiment_start: float) -> None:
        # This sweep uses the full model architecture while varying consolidation
        # strength.  It explicitly tests whether consolidation is helpful only under
        # noise/capacity pressure, rather than necessary in the easy regime.
        strengths = self.cfg.consolidation_strengths
        if not strengths:
            return
        base = self.variants["exp12_full_context_separated_memory"]
        total = len(strengths) * self.cfg.seeds * len(self.cfg.consolidation_world_counts)
        completed = 0
        for strength in strengths:
            variant = dataclasses.replace(
                base,
                name=f"exp12_consolidation_sweep_{strength:g}",
                consolidation_strength=float(strength),
                consolidation_pull=min(0.18, max(0.0, float(strength) * 0.15)),
                shared_update_fraction=0.04 if strength < 0.5 else 0.10,
                clip_max=8.0 if strength >= 0.5 else base.clip_max,
            )
            for seed in range(self.cfg.seeds):
                for world_count in self.cfg.consolidation_world_counts:
                    job_start = time.time()
                    routes = generate_world_routes(seed=10_000 + seed, world_count=world_count, modes=self.cfg.modes, nodes=self.cfg.nodes)
                    model = PlasticRouteMemory(variant=variant, routes=routes, seed=10_000 + seed)
                    for train_world in range(world_count):
                        model.train_world(train_world)
                    for bleed in (0.0, 0.10, 0.20, 0.35):
                        for eval_world in range(world_count):
                            m = model.evaluate_world(
                                eval_world,
                                route_length=self.cfg.default_eval_steps,
                                context_bleed=bleed,
                            )
                            self._append_metric(
                                m,
                                phase="consolidation_pressure",
                                variant=variant,
                                seed=seed,
                                world_count=world_count,
                                route_length=self.cfg.default_eval_steps,
                                train_checkpoint=world_count - 1,
                                eval_world=eval_world,
                                context_bleed=bleed,
                                context_dropout=0.0,
                                consolidation_strength=float(strength),
                            )
                    completed += 1
                    self._progress(
                        event="consolidation_job_completed",
                        completed=completed,
                        total=total,
                        variant=variant.name,
                        seed=seed,
                        world_count=world_count,
                        seconds=time.time() - job_start,
                        elapsed_seconds=time.time() - experiment_start,
                    )

    def _append_metric(
        self,
        values: Dict[str, float],
        *,
        phase: str,
        variant: Variant,
        seed: int,
        world_count: int,
        route_length: int,
        train_checkpoint: int,
        eval_world: int,
        context_bleed: float,
        context_dropout: float,
        consolidation_strength: float,
        generalization_condition: str = "",
    ) -> None:
        row: Dict[str, object] = {
            "phase": phase,
            "run_name": variant.name,
            "seed": seed,
            "world_count": world_count,
            "route_length": route_length,
            "train_checkpoint": train_checkpoint,
            "eval_world": eval_world,
            "context_bleed": context_bleed,
            "context_dropout": context_dropout,
            "consolidation_strength": consolidation_strength,
            "generalization_condition": generalization_condition,
            "nodes": self.cfg.nodes,
            "modes": self.cfg.modes,
        }
        row.update(values)
        self.metrics.append(row)

    def _progress(self, **payload: object) -> None:
        payload = {**payload, "profile": self.cfg.profile, "timestamp": time.time()}
        with self.progress_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(payload, sort_keys=True) + "\n")
        if self.cfg.verbose:
            event = payload.get("event")
            completed = payload.get("completed")
            total = payload.get("total")
            variant = payload.get("variant")
            seed = payload.get("seed")
            wc = payload.get("world_count")
            secs = float(payload.get("seconds", 0.0))
            print(f"[{event}] {completed}/{total} variant={variant} seed={seed} worlds={wc} seconds={secs:.2f}", flush=True)

    def _write_outputs(self, start: float) -> None:
        metrics = pd.DataFrame(self.metrics)
        metrics_path = self.cfg.out_dir / "metrics.csv"
        metrics.to_csv(metrics_path, index=False)
        pd.DataFrame(self.run_rows).to_csv(self.cfg.out_dir / "runs.csv", index=False)

        self._write_summaries(metrics)
        self._make_plots(metrics)
        self._write_report(metrics, elapsed=time.time() - start)

    def _write_summaries(self, metrics: pd.DataFrame) -> None:
        summary_specs = {
            "capacity_final_summary.csv": ["phase", "run_name", "world_count", "route_length"],
            "heldout_generalization_summary.csv": ["phase", "run_name", "world_count", "route_length", "generalization_condition"],
            "context_bleed_summary.csv": ["phase", "run_name", "world_count", "context_bleed"],
            "context_dropout_summary.csv": ["phase", "run_name", "world_count", "context_dropout"],
            "continual_retention_summary.csv": ["phase", "run_name", "world_count", "train_checkpoint", "eval_world"],
            "consolidation_pressure_summary.csv": ["phase", "consolidation_strength", "world_count", "context_bleed"],
        }
        value_cols = [
            "composition_accuracy",
            "route_route_table_accuracy",
            "composition_route_gap",
            "composition_mean_correct_margin",
            "composition_mean_world_margin",
            "composition_mean_wrong_world_activation",
        ]
        for filename, group_cols in summary_specs.items():
            phase_name = group_cols[0]
            subset_phase = filename.replace("_summary.csv", "")
            if subset_phase == "capacity_final":
                df = metrics[metrics[phase_name] == "capacity_final"]
            elif subset_phase == "heldout_generalization":
                df = metrics[metrics[phase_name] == "heldout_generalization"]
            elif subset_phase == "context_bleed":
                df = metrics[metrics[phase_name] == "context_bleed"]
            elif subset_phase == "context_dropout":
                df = metrics[metrics[phase_name] == "context_dropout"]
            elif subset_phase == "continual_retention":
                df = metrics[metrics[phase_name] == "continual_retention"]
            elif subset_phase == "consolidation_pressure":
                df = metrics[metrics[phase_name] == "consolidation_pressure"]
            else:
                df = metrics
            if df.empty:
                continue
            grouped = df.groupby(group_cols, dropna=False)[value_cols].agg(["mean", "std", "count"]).reset_index()
            grouped.columns = ["_".join([c for c in col if c]) if isinstance(col, tuple) else col for col in grouped.columns]
            grouped.to_csv(self.cfg.out_dir / filename, index=False)

        # Compact final memory index: last checkpoint, default route length.
        cap = metrics[
            (metrics.phase == "capacity_final")
            & (metrics.route_length == self.cfg.default_eval_steps)
            & (metrics.context_bleed == 0.0)
            & (metrics.context_dropout == 0.0)
        ]
        if not cap.empty:
            index = cap.groupby(["run_name", "world_count"], dropna=False).agg(
                final_composition_accuracy=("composition_accuracy", "mean"),
                final_route_table_accuracy=("route_route_table_accuracy", "mean"),
                final_route_gap=("composition_route_gap", "mean"),
                final_world_margin=("composition_mean_world_margin", "mean"),
                final_wrong_world_activation=("composition_mean_wrong_world_activation", "mean"),
                n=("composition_accuracy", "count"),
            ).reset_index()
            index.to_csv(self.cfg.out_dir / "exp12_final_memory_index.csv", index=False)

    def _make_plots(self, metrics: pd.DataFrame) -> None:
        plots_dir = self.cfg.out_dir / "plots"
        plt.rcParams.update({"figure.figsize": (14, 7), "axes.grid": True})

        cap = metrics[(metrics.phase == "capacity_final") & (metrics.route_length == self.cfg.default_eval_steps)]
        if not cap.empty:
            self._line_plot(
                cap,
                x="world_count",
                y="composition_accuracy",
                group="run_name",
                title="Experiment 12: capacity scaling, final composition accuracy",
                ylabel="composition accuracy",
                path=plots_dir / "exp12_capacity_composition_accuracy.png",
            )
            self._line_plot(
                cap,
                x="world_count",
                y="route_route_table_accuracy",
                group="run_name",
                title="Experiment 12: capacity scaling, final route-table accuracy",
                ylabel="route-table accuracy",
                path=plots_dir / "exp12_capacity_route_table_accuracy.png",
            )
            self._line_plot(
                cap,
                x="world_count",
                y="composition_route_gap",
                group="run_name",
                title="Experiment 12: route-table minus composition gap",
                ylabel="route table - composition",
                path=plots_dir / "exp12_route_table_composition_gap.png",
            )
            self._line_plot(
                cap,
                x="world_count",
                y="composition_mean_wrong_world_activation",
                group="run_name",
                title="Experiment 12: wrong-world activation under capacity scaling",
                ylabel="wrong-world activation",
                path=plots_dir / "exp12_capacity_wrong_world_activation.png",
            )

        gen = metrics[metrics.phase == "heldout_generalization"]
        if not gen.empty:
            self._line_plot(
                gen,
                x="route_length",
                y="composition_accuracy",
                group="run_name",
                title="Experiment 12: held-out compositional generalization by route length",
                ylabel="composition accuracy",
                path=plots_dir / "exp12_heldout_generalization_by_length.png",
            )

        bleed = metrics[metrics.phase == "context_bleed"]
        if not bleed.empty:
            self._line_plot(
                bleed,
                x="context_bleed",
                y="composition_accuracy",
                group="run_name",
                title="Experiment 12: composition accuracy under world-context bleed",
                ylabel="composition accuracy",
                path=plots_dir / "exp12_context_bleed_composition.png",
            )
            self._line_plot(
                bleed,
                x="context_bleed",
                y="composition_mean_world_margin",
                group="run_name",
                title="Experiment 12: world margin under world-context bleed",
                ylabel="world margin",
                path=plots_dir / "exp12_context_bleed_world_margin.png",
            )

        dropout = metrics[metrics.phase == "context_dropout"]
        if not dropout.empty:
            self._line_plot(
                dropout,
                x="context_dropout",
                y="composition_accuracy",
                group="run_name",
                title="Experiment 12: composition accuracy under world-context dropout",
                ylabel="composition accuracy",
                path=plots_dir / "exp12_context_dropout_composition.png",
            )
            self._line_plot(
                dropout,
                x="context_dropout",
                y="composition_mean_world_margin",
                group="run_name",
                title="Experiment 12: world margin under world-context dropout",
                ylabel="world margin",
                path=plots_dir / "exp12_context_dropout_world_margin.png",
            )

        cons = metrics[metrics.phase == "consolidation_pressure"]
        if not cons.empty:
            self._line_plot(
                cons,
                x="consolidation_strength",
                y="composition_accuracy",
                group="world_count",
                title="Experiment 12: consolidation pressure sweep",
                ylabel="composition accuracy",
                path=plots_dir / "exp12_consolidation_pressure_accuracy.png",
            )
            self._line_plot(
                cons,
                x="consolidation_strength",
                y="composition_mean_world_margin",
                group="world_count",
                title="Experiment 12: consolidation pressure world margin",
                ylabel="world margin",
                path=plots_dir / "exp12_consolidation_pressure_world_margin.png",
            )

        cont = metrics[(metrics.phase == "continual_retention") & (metrics.run_name == "exp12_full_context_separated_memory")]
        if not cont.empty:
            # Use the largest world_count available for the default full-model heatmap.
            wc = int(cont.world_count.max())
            heat = cont[cont.world_count == wc]
            pivot = heat.groupby(["eval_world", "train_checkpoint"])["composition_accuracy"].mean().unstack()
            fig, ax = plt.subplots(figsize=(10, 8))
            im = ax.imshow(pivot.values, aspect="auto", vmin=0.0, vmax=1.0)
            ax.set_title(f"Experiment 12: continual retention matrix, full model, {wc} worlds")
            ax.set_xlabel("after training world")
            ax.set_ylabel("eval world")
            ax.set_xticks(np.arange(len(pivot.columns)))
            ax.set_xticklabels([str(c) for c in pivot.columns])
            ax.set_yticks(np.arange(len(pivot.index)))
            ax.set_yticklabels([str(i) for i in pivot.index])
            fig.colorbar(im, ax=ax, label="composition accuracy")
            fig.tight_layout()
            fig.savefig(plots_dir / "exp12_continual_retention_heatmap_full_model.png", dpi=160)
            plt.close(fig)

    @staticmethod
    def _line_plot(df: pd.DataFrame, x: str, y: str, group: str, title: str, ylabel: str, path: Path) -> None:
        fig, ax = plt.subplots()
        grouped = df.groupby([group, x], dropna=False)[y].mean().reset_index()
        for name, sub in grouped.groupby(group, dropna=False):
            sub = sub.sort_values(x)
            ax.plot(sub[x], sub[y], marker="o", label=str(name))
        ax.set_title(title)
        ax.set_xlabel(x)
        ax.set_ylabel(ylabel)
        ax.legend(loc="best", fontsize="small")
        fig.tight_layout()
        fig.savefig(path, dpi=160)
        plt.close(fig)

    def _write_report(self, metrics: pd.DataFrame, elapsed: float) -> None:
        report_path = self.cfg.out_dir / "exp12_report.md"
        cap = metrics[(metrics.phase == "capacity_final") & (metrics.route_length == self.cfg.default_eval_steps)]
        cap_summary = pd.DataFrame()
        if not cap.empty:
            cap_summary = cap.groupby(["run_name", "world_count"])[
                ["composition_accuracy", "route_route_table_accuracy", "composition_route_gap", "composition_mean_wrong_world_activation"]
            ].mean().reset_index()

        lines: List[str] = []
        lines.append("# Experiment 12 Report - Capacity, Interference, and Compositional Generalization")
        lines.append("")
        lines.append("## Purpose")
        lines.append("")
        lines.append(
            "Experiment 12 stress-tests the Experiment 11 mechanism by scaling the number of incompatible worlds, "
            "measuring continual retention after each new world, testing held-out multi-step compositions, and sweeping "
            "world-context noise plus consolidation strength."
        )
        lines.append("")
        lines.append("## Run configuration")
        lines.append("")
        lines.append(f"- profile: `{self.cfg.profile}`")
        lines.append(f"- seeds: `{self.cfg.seeds}`")
        lines.append(f"- world counts: `{list(self.cfg.world_counts)}`")
        lines.append(f"- route lengths: `{list(self.cfg.route_lengths)}`")
        lines.append(f"- nodes: `{self.cfg.nodes}`")
        lines.append(f"- modes: `{self.cfg.modes}`")
        lines.append(f"- variants: `{list(self.cfg.variants)}`")
        lines.append(f"- elapsed seconds: `{elapsed:.2f}`")
        lines.append("")
        lines.append("## Generated files")
        lines.append("")
        for filename in [
            "metrics.csv",
            "runs.csv",
            "progress.jsonl",
            "exp12_final_memory_index.csv",
            "capacity_final_summary.csv",
            "continual_retention_summary.csv",
            "heldout_generalization_summary.csv",
            "context_bleed_summary.csv",
            "context_dropout_summary.csv",
            "consolidation_pressure_summary.csv",
        ]:
            if (self.cfg.out_dir / filename).exists():
                lines.append(f"- `{filename}`")
        if (self.cfg.out_dir / "plots").exists():
            for plot in sorted((self.cfg.out_dir / "plots").glob("*.png")):
                lines.append(f"- `plots/{plot.name}`")
        lines.append("")
        lines.append("## Capacity snapshot")
        lines.append("")
        if cap_summary.empty:
            lines.append("No capacity rows were generated.")
        else:
            lines.append(cap_summary.to_markdown(index=False))
        lines.append("")
        lines.append("## Interpretation checklist")
        lines.append("")
        lines.append("- Full and world-gated variants should preserve high composition accuracy as world count increases.")
        lines.append("- No-recurrence should preserve one-step route-table accuracy but fail multi-step composition.")
        lines.append("- No-world-context and shared-edges-only should show destructive overwriting as incompatible worlds accumulate.")
        lines.append("- No-structural-plasticity should remain near chance.")
        lines.append("- Consolidation should be interpreted as a pressure/modulation study, not assumed to be essential.")
        report_path.write_text("\n".join(lines), encoding="utf-8")


# -----------------------------
# CLI
# -----------------------------


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Experiment 12 route-memory capacity/generalization study.")
    parser.add_argument("--profile", choices=["validate", "full", "custom"], default="full")
    parser.add_argument("--out", default="analysis/exp12", help="Output directory.")
    parser.add_argument("--seeds", type=int, default=None)
    parser.add_argument("--world-counts", type=int, nargs="*", default=None)
    parser.add_argument("--route-lengths", type=int, nargs="*", default=None)
    parser.add_argument("--nodes", type=int, default=None)
    parser.add_argument("--modes", type=int, default=None)
    parser.add_argument("--variants", nargs="*", default=None, help=f"Variant names. Available: {', '.join(ALL_VARIANTS)}")
    parser.add_argument("--context-bleeds", type=float, nargs="*", default=None)
    parser.add_argument("--context-dropouts", type=float, nargs="*", default=None)
    parser.add_argument("--consolidation-strengths", type=float, nargs="*", default=None)
    parser.add_argument("--consolidation-world-counts", type=int, nargs="*", default=None)
    parser.add_argument("--default-eval-steps", type=int, default=None)
    parser.add_argument("--quiet", action="store_true")
    return parser.parse_args(argv)


def build_config(args: argparse.Namespace) -> RunConfig:
    if args.profile == "validate":
        defaults = dict(
            seeds=2,
            world_counts=(2, 4),
            route_lengths=(1, 2, 4),
            nodes=16,
            modes=3,
            variants=(
                "exp12_full_context_separated_memory",
                "exp12_world_gated_plasticity",
                "exp12_no_world_context",
                "exp12_no_recurrence",
                "exp12_no_structural_plasticity",
            ),
            context_bleeds=(0.0, 0.20),
            context_dropouts=(0.0, 0.10),
            consolidation_strengths=(0.0, 0.12, 0.50),
            consolidation_world_counts=(4,),
            default_eval_steps=4,
        )
    elif args.profile == "full":
        defaults = dict(
            seeds=30,
            world_counts=(2, 4, 8, 16, 32),
            route_lengths=(1, 2, 4, 8, 12),
            nodes=32,
            modes=3,
            variants=CORE_VARIANTS,
            context_bleeds=(0.0, 0.05, 0.10, 0.20, 0.35),
            context_dropouts=(0.0, 0.05, 0.10, 0.20),
            consolidation_strengths=(0.0, 0.025, 0.05, 0.12, 0.25, 0.50, 0.80),
            consolidation_world_counts=(4, 8, 16),
            default_eval_steps=8,
        )
    else:
        defaults = dict(
            seeds=5,
            world_counts=(2, 4, 8),
            route_lengths=(1, 2, 4, 8),
            nodes=24,
            modes=3,
            variants=CORE_VARIANTS,
            context_bleeds=(0.0, 0.10, 0.20),
            context_dropouts=(0.0, 0.10),
            consolidation_strengths=(0.0, 0.12, 0.50),
            consolidation_world_counts=(4, 8),
            default_eval_steps=8,
        )

    cfg = RunConfig(
        out_dir=Path(args.out),
        profile=args.profile,
        seeds=args.seeds if args.seeds is not None else defaults["seeds"],
        world_counts=tuple(args.world_counts) if args.world_counts else defaults["world_counts"],
        route_lengths=tuple(args.route_lengths) if args.route_lengths else defaults["route_lengths"],
        nodes=args.nodes if args.nodes is not None else defaults["nodes"],
        modes=args.modes if args.modes is not None else defaults["modes"],
        variants=tuple(args.variants) if args.variants else defaults["variants"],
        context_bleeds=tuple(args.context_bleeds) if args.context_bleeds else defaults["context_bleeds"],
        context_dropouts=tuple(args.context_dropouts) if args.context_dropouts else defaults["context_dropouts"],
        consolidation_strengths=tuple(args.consolidation_strengths) if args.consolidation_strengths else defaults["consolidation_strengths"],
        consolidation_world_counts=tuple(args.consolidation_world_counts) if args.consolidation_world_counts else defaults["consolidation_world_counts"],
        default_eval_steps=args.default_eval_steps if args.default_eval_steps is not None else defaults["default_eval_steps"],
        verbose=not args.quiet,
    )
    if cfg.seeds <= 0:
        raise ValueError("--seeds must be positive")
    if cfg.nodes < 4:
        raise ValueError("--nodes should be at least 4")
    if cfg.modes < 1:
        raise ValueError("--modes must be at least 1")
    # Keep the compact memory index and default plots well-defined even when a
    # custom route-length list is supplied.
    if cfg.default_eval_steps not in cfg.route_lengths:
        cfg = dataclasses.replace(
            cfg,
            route_lengths=tuple(sorted(set(cfg.route_lengths + (cfg.default_eval_steps,))))
        )
    return cfg


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    cfg = build_config(args)
    print("Experiment 12 starting")
    print(json.dumps({
        "profile": cfg.profile,
        "out_dir": str(cfg.out_dir),
        "seeds": cfg.seeds,
        "world_counts": cfg.world_counts,
        "route_lengths": cfg.route_lengths,
        "nodes": cfg.nodes,
        "modes": cfg.modes,
        "variants": cfg.variants,
    }, indent=2, default=list))
    runner = Experiment12Runner(cfg)
    runner.run()
    print(f"Experiment 12 complete. Outputs written to: {cfg.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
