"""Experiment 11 core: context-separated memory and non-destructive rebinding.

The experiment asks whether a local plastic route field can learn multiple rule
worlds over the same symbolic substrate and retrieve the correct route system
from a higher-order world context. Multi-step composition is never directly
trained; composition is evaluated by recurrent traversal of learned one-step
routes.

This is intentionally compact and inspectable. Route strength is represented as
local source/mode/world-to-target scores, with optional shared-route leakage to
model substrate overlap and interference.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple
import math
import random

import numpy as np

MODE_NAMES: Tuple[str, ...] = ("minus_one", "plus_one", "plus_two")
WORLD_DELTAS: Dict[str, Dict[str, int]] = {
    "A": {"minus_one": -1, "plus_one": 1, "plus_two": 2},
    "B": {"minus_one": 1, "plus_one": -1, "plus_two": 2},
    "C": {"minus_one": 1, "plus_one": 2, "plus_two": -1},
    "D": {"minus_one": -1, "plus_one": -2, "plus_two": 1},
}
WORLD_NAMES: Tuple[str, ...] = tuple(WORLD_DELTAS.keys())


@dataclass(frozen=True)
class Task:
    world: str
    mode: str
    start: int
    steps: int
    target: int

    @property
    def delta(self) -> int:
        return WORLD_DELTAS[self.world][self.mode]


@dataclass
class VariantConfig:
    name: str
    recurrence: bool = True
    structural_plasticity: bool = True
    world_context: bool = True
    context_binding: bool = True
    inhibition: bool = True
    homeostasis: bool = True
    consolidation_strength: float = 0.12
    shared_route_weight: float = 0.08
    shared_update_fraction: float = 0.08
    world_update_fraction: float = 1.0
    world_gated_plasticity: bool = False
    shared_edges_only: bool = False
    learning_rate: float = 1.0
    inhibition_strength: float = 0.10
    wrong_world_inhibition: float = 0.05
    wrong_mode_inhibition: float = 0.05
    consolidation_pull: float = 0.025
    clip_min: float = -2.0
    clip_max: float = 4.0


@dataclass
class GraphConfig:
    max_number: int = 31
    max_steps: int = 8
    worlds: Tuple[str, ...] = ("A", "B")


@dataclass
class PredictionTrace:
    task: Task
    predicted: int
    correct: bool
    step_predictions: List[int]
    step_expected: List[int]
    step_target_ranks: List[int]
    step_correct_margins: List[float]
    step_world_margins: List[float]
    step_mode_margins: List[float]
    wrong_world_activations: List[float]
    wrong_mode_activations: List[float]
    failure_type: str


def true_target(start: int, mode: str, steps: int, world: str) -> int:
    return start + WORLD_DELTAS[world][mode] * steps


def generate_bounded_tasks(max_number: int, max_steps: int, world: str, min_steps: int = 1) -> List[Task]:
    tasks: List[Task] = []
    for mode in MODE_NAMES:
        for start in range(max_number + 1):
            for steps in range(min_steps, max_steps + 1):
                target = true_target(start, mode, steps, world)
                if 0 <= target <= max_number:
                    tasks.append(Task(world=world, mode=mode, start=start, steps=steps, target=target))
    return tasks


def generate_transition_tasks(max_number: int, world: str) -> List[Task]:
    return generate_bounded_tasks(max_number=max_number, max_steps=1, min_steps=1, world=world)


def shuffled_repeated(items: Sequence[Task], repeats: int, rng: random.Random) -> List[Task]:
    out: List[Task] = []
    for _ in range(max(0, repeats)):
        batch = list(items)
        rng.shuffle(batch)
        out.extend(batch)
    return out


def _safe_sigmoid(x: float) -> float:
    if x >= 35:
        return 1.0
    if x <= -35:
        return 0.0
    return 1.0 / (1.0 + math.exp(-x))


def _nanmean(values: Iterable[float]) -> float:
    arr = np.asarray(list(values), dtype=float)
    arr = arr[~np.isnan(arr)]
    return float(np.mean(arr)) if arr.size else math.nan


class ContextMemoryGraph:
    """A local route-field graph with explicit/separable world context.

    Scores are stored in two substrates:
    - world_scores[world, source, mode, target]
    - shared_scores[source, mode_or_shared, target]

    Full variants mostly update world-specific scores, with a small shared update
    fraction to model overlap. Shared/no-world variants force collisions through
    the shared substrate. Evaluation can inject world-context bleed/dropout to
    test retrieval robustness.
    """

    def __init__(self, cfg: GraphConfig, variant: VariantConfig, seed: int):
        self.cfg = cfg
        self.variant = variant
        self.seed = seed
        self.rng = np.random.default_rng(seed)
        self.py_rng = random.Random(seed)
        self.world_index = {w: i for i, w in enumerate(WORLD_NAMES)}
        self.mode_index = {m: i for i, m in enumerate(MODE_NAMES)}
        n_worlds = len(WORLD_NAMES)
        n_modes = len(MODE_NAMES)
        n = cfg.max_number + 1
        # Tiny initialization breaks ties deterministically by seed.
        # Last mode index is the "unbound mode" channel for no-context-binding.
        # Both substrates need this channel: no_context_binding should keep world
        # separation while deliberately collapsing mode separation within a world.
        self.world_scores = self.rng.normal(0.0, 1e-5, size=(n_worlds, n, n_modes + 1, n)).astype(np.float32)
        self.shared_scores = self.rng.normal(0.0, 1e-5, size=(n, n_modes + 1, n)).astype(np.float32)
        self.consolidated_world_scores: Optional[np.ndarray] = None
        self.consolidated_shared_scores: Optional[np.ndarray] = None

    @property
    def max_number(self) -> int:
        return self.cfg.max_number

    def _mode_slot(self, mode: str) -> int:
        if not self.variant.context_binding:
            return len(MODE_NAMES)
        return self.mode_index[mode]

    def _world_slot(self, world: str) -> Optional[int]:
        if not self.variant.world_context:
            return None
        return self.world_index[world]

    def _valid_next(self, source: int, mode: str, world: str) -> Optional[int]:
        target = true_target(source, mode, 1, world)
        if 0 <= target <= self.max_number:
            return target
        return None

    def _world_score_vector(self, source: int, mode: str, world: str) -> np.ndarray:
        widx = self._world_slot(world)
        midx = self._mode_slot(mode)
        if widx is None or self.variant.shared_edges_only:
            return np.zeros(self.max_number + 1, dtype=np.float32)
        return self.world_scores[widx, source, midx, :]

    def _shared_score_vector(self, source: int, mode: str) -> np.ndarray:
        midx = self._mode_slot(mode)
        return self.shared_scores[source, midx, :]

    def scores(
        self,
        source: int,
        mode: str,
        world: str,
        world_context_bleed: float = 0.0,
        world_context_dropout: float = 0.0,
    ) -> np.ndarray:
        # Correct-world route contribution.
        shared = self._shared_score_vector(source, mode)
        if self.variant.shared_edges_only or not self.variant.world_context:
            return shared.copy()

        correct_world = self._world_score_vector(source, mode, world)
        if world_context_dropout >= 1.0:
            world_part = np.zeros_like(correct_world)
        else:
            other_worlds = [w for w in self.cfg.worlds if w != world]
            if other_worlds:
                other = np.mean([self._world_score_vector(source, mode, w) for w in other_worlds], axis=0)
            else:
                other = np.zeros_like(correct_world)
            bleed = max(0.0, min(1.0, world_context_bleed))
            dropout = max(0.0, min(1.0, world_context_dropout))
            world_part = (1.0 - dropout) * ((1.0 - bleed) * correct_world + bleed * other)
        return world_part + self.variant.shared_route_weight * shared

    def consolidate(self) -> None:
        if self.variant.consolidation_strength > 0:
            self.consolidated_world_scores = self.world_scores.copy()
            self.consolidated_shared_scores = self.shared_scores.copy()

    def _pull_to_consolidated(self, phase: str) -> None:
        if self.consolidated_world_scores is None or self.consolidated_shared_scores is None:
            return
        # Pull only during later learning phases, not initial acquisition.
        if phase in {"initial", "alternating_initial"}:
            return
        s = max(0.0, min(1.0, self.variant.consolidation_strength))
        if s <= 0:
            return
        pull = np.float32(self.variant.consolidation_pull * s)
        self.world_scores *= np.float32(1.0 - pull)
        self.world_scores += self.consolidated_world_scores * pull
        self.shared_scores *= np.float32(1.0 - pull)
        self.shared_scores += self.consolidated_shared_scores * pull

    def _learning_rate_for_phase(self, phase: str) -> float:
        lr = self.variant.learning_rate
        if phase not in {"initial", "alternating_initial"}:
            # Consolidation slows acquisition of new worlds/rules.
            lr *= max(0.05, 1.0 - 0.70 * max(0.0, min(1.0, self.variant.consolidation_strength)))
        return lr

    def _apply_update(self, task: Task, phase: str) -> None:
        v = self.variant
        if not v.structural_plasticity:
            return
        target = task.target
        if not (0 <= target <= self.max_number):
            return
        lr = self._learning_rate_for_phase(phase)
        midx = self._mode_slot(task.mode)
        widx = self._world_slot(task.world)

        update_world = (widx is not None) and not v.shared_edges_only
        update_shared = (not v.world_gated_plasticity) or v.shared_edges_only or not v.world_context
        world_frac = 0.0 if not update_world else v.world_update_fraction
        shared_frac = v.shared_update_fraction if update_shared else 0.0
        if v.shared_edges_only or not v.world_context:
            shared_frac = 1.0
            world_frac = 0.0

        if world_frac > 0.0 and widx is not None:
            self.world_scores[widx, task.start, midx, target] += np.float32(lr * world_frac)
            if v.inhibition:
                self.world_scores[widx, task.start, midx, :] -= np.float32(lr * world_frac * v.inhibition_strength)
                self.world_scores[widx, task.start, midx, target] += np.float32(lr * world_frac * v.inhibition_strength)
                # Suppress wrong modes in the active world.
                if v.context_binding:
                    for other_mode in MODE_NAMES:
                        if other_mode == task.mode:
                            continue
                        om = self._mode_slot(other_mode)
                        self.world_scores[widx, task.start, om, target] -= np.float32(lr * v.wrong_mode_inhibition)
                    # Suppress same mode/target in inactive worlds only mildly; this
                    # improves retrieval separation while not destroying memories.
                    # In the world-gated variant, inactive worlds must not be modified;
                    # otherwise the "gated" control is not actually non-destructive.
                    if not v.world_gated_plasticity:
                        for other_world in self.cfg.worlds:
                            if other_world == task.world:
                                continue
                            ow = self.world_index[other_world]
                            self.world_scores[ow, task.start, midx, target] -= np.float32(lr * v.wrong_world_inhibition * 0.25)

        if shared_frac > 0.0:
            self.shared_scores[task.start, midx, target] += np.float32(lr * shared_frac)
            if v.inhibition:
                self.shared_scores[task.start, midx, :] -= np.float32(lr * shared_frac * v.inhibition_strength)
                self.shared_scores[task.start, midx, target] += np.float32(lr * shared_frac * v.inhibition_strength)

        if v.homeostasis:
            np.clip(self.world_scores, v.clip_min, v.clip_max, out=self.world_scores)
            np.clip(self.shared_scores, v.clip_min, v.clip_max, out=self.shared_scores)
        self._pull_to_consolidated(phase)

    def train_curriculum(self, transition_tasks: Sequence[Task], repeats: int, phase: str) -> None:
        for task in shuffled_repeated(transition_tasks, repeats, self.py_rng):
            self._apply_update(task, phase)

    def target_rank_and_margin(
        self,
        source: int,
        mode: str,
        world: str,
        target: int,
        world_context_bleed: float = 0.0,
        world_context_dropout: float = 0.0,
    ) -> Tuple[int, float, float, float]:
        s = self.scores(source, mode, world, world_context_bleed, world_context_dropout)
        order = np.argsort(s)[::-1]
        rank = int(np.where(order == target)[0][0]) + 1
        target_score = float(s[target])
        wrong = np.delete(s, target)
        best_wrong = float(np.max(wrong)) if wrong.size else -math.inf
        return rank, target_score - best_wrong, target_score, float(np.max(s))

    def world_margin(
        self,
        source: int,
        mode: str,
        world: str,
        target: int,
        world_context_bleed: float = 0.0,
        world_context_dropout: float = 0.0,
    ) -> float:
        if not self.variant.world_context or self.variant.shared_edges_only:
            return math.nan
        correct = float(self.scores(source, mode, world, world_context_bleed, world_context_dropout)[target])
        wrong = []
        for other_world in self.cfg.worlds:
            if other_world == world:
                continue
            wrong.append(float(self.scores(source, mode, other_world, world_context_bleed, world_context_dropout)[target]))
        return correct - max(wrong) if wrong else math.nan

    def mode_margin(
        self,
        source: int,
        mode: str,
        world: str,
        target: int,
        world_context_bleed: float = 0.0,
        world_context_dropout: float = 0.0,
    ) -> float:
        if not self.variant.context_binding:
            return math.nan
        correct = float(self.scores(source, mode, world, world_context_bleed, world_context_dropout)[target])
        wrong = []
        for other_mode in MODE_NAMES:
            if other_mode == mode:
                continue
            wrong.append(float(self.scores(source, other_mode, world, world_context_bleed, world_context_dropout)[target]))
        return correct - max(wrong) if wrong else math.nan

    def wrong_world_activation(
        self,
        source: int,
        mode: str,
        world: str,
        target: int,
        world_context_bleed: float = 0.0,
        world_context_dropout: float = 0.0,
    ) -> float:
        if not self.variant.world_context or self.variant.shared_edges_only:
            return math.nan
        correct = float(self.scores(source, mode, world, world_context_bleed, world_context_dropout)[target])
        wrong = []
        for other_world in self.cfg.worlds:
            if other_world == world:
                continue
            wrong.append(float(self.scores(source, mode, other_world, world_context_bleed, world_context_dropout)[target]))
        return float(np.mean([_safe_sigmoid(w - correct) for w in wrong])) if wrong else math.nan

    def wrong_mode_activation(
        self,
        source: int,
        mode: str,
        world: str,
        target: int,
        world_context_bleed: float = 0.0,
        world_context_dropout: float = 0.0,
    ) -> float:
        if not self.variant.context_binding:
            return math.nan
        correct = float(self.scores(source, mode, world, world_context_bleed, world_context_dropout)[target])
        wrong = []
        for other_mode in MODE_NAMES:
            if other_mode == mode:
                continue
            wrong.append(float(self.scores(source, other_mode, world, world_context_bleed, world_context_dropout)[target]))
        return float(np.mean([_safe_sigmoid(w - correct) for w in wrong])) if wrong else math.nan

    def predict(
        self,
        task: Task,
        world_context_bleed: float = 0.0,
        world_context_dropout: float = 0.0,
    ) -> PredictionTrace:
        current = task.start
        expected_current = task.start
        step_predictions: List[int] = []
        step_expected: List[int] = []
        ranks: List[int] = []
        correct_margins: List[float] = []
        world_margins: List[float] = []
        mode_margins: List[float] = []
        wrong_worlds: List[float] = []
        wrong_modes: List[float] = []
        failure_type = "none"
        steps_to_run = task.steps if self.variant.recurrence else 1
        for step_i in range(steps_to_run):
            expected_next = self._valid_next(expected_current, task.mode, task.world)
            if expected_next is None:
                break
            step_expected.append(expected_next)
            scores = self.scores(current, task.mode, task.world, world_context_bleed, world_context_dropout)
            predicted_next = int(np.argmax(scores))
            step_predictions.append(predicted_next)
            local_expected = expected_next if current == expected_current else true_target(current, task.mode, 1, task.world)
            if not (0 <= local_expected <= self.max_number):
                local_expected = predicted_next
            rank, margin, _, _ = self.target_rank_and_margin(current, task.mode, task.world, local_expected, world_context_bleed, world_context_dropout)
            ranks.append(rank)
            correct_margins.append(margin)
            world_margins.append(self.world_margin(current, task.mode, task.world, local_expected, world_context_bleed, world_context_dropout))
            mode_margins.append(self.mode_margin(current, task.mode, task.world, local_expected, world_context_bleed, world_context_dropout))
            wrong_worlds.append(self.wrong_world_activation(current, task.mode, task.world, local_expected, world_context_bleed, world_context_dropout))
            wrong_modes.append(self.wrong_mode_activation(current, task.mode, task.world, local_expected, world_context_bleed, world_context_dropout))
            if predicted_next != expected_next and failure_type == "none":
                failure_type = "first_step_failure" if step_i == 0 else "mid_route_drift"
            current = predicted_next
            expected_current = expected_next
        predicted = current if self.variant.recurrence else (step_predictions[-1] if step_predictions else task.start)
        correct = predicted == task.target
        if not correct and not self.variant.recurrence:
            failure_type = "no_recurrence_single_step_only"
        elif not correct and failure_type == "none":
            failure_type = "decoder_or_endpoint_failure"
        return PredictionTrace(task, predicted, correct, step_predictions, step_expected, ranks, correct_margins, world_margins, mode_margins, wrong_worlds, wrong_modes, failure_type)

    def route_diagnostics(
        self,
        eval_world: str,
        world_context_bleed: float = 0.0,
        world_context_dropout: float = 0.0,
    ) -> List[dict]:
        rows: List[dict] = []
        for mode in MODE_NAMES:
            for source in range(self.max_number + 1):
                target = self._valid_next(source, mode, eval_world)
                if target is None:
                    continue
                scores = self.scores(source, mode, eval_world, world_context_bleed, world_context_dropout)
                predicted = int(np.argmax(scores))
                rank, margin, target_score, best_score = self.target_rank_and_margin(source, mode, eval_world, target, world_context_bleed, world_context_dropout)
                order = np.argsort(scores)[::-1][:5]
                rows.append({
                    "eval_world": eval_world,
                    "mode": mode,
                    "source": source,
                    "true_target": target,
                    "predicted_target": predicted,
                    "correct": int(predicted == target),
                    "target_rank": rank,
                    "correct_margin": margin,
                    "world_margin": self.world_margin(source, mode, eval_world, target, world_context_bleed, world_context_dropout),
                    "mode_margin": self.mode_margin(source, mode, eval_world, target, world_context_bleed, world_context_dropout),
                    "wrong_world_activation": self.wrong_world_activation(source, mode, eval_world, target, world_context_bleed, world_context_dropout),
                    "wrong_mode_activation": self.wrong_mode_activation(source, mode, eval_world, target, world_context_bleed, world_context_dropout),
                    "target_score": target_score,
                    "best_score": best_score,
                    "top_targets": ";".join(f"{int(i)}:{float(scores[i]):.5f}" for i in order),
                })
        return rows


def summarize_traces(traces: Sequence[PredictionTrace], prefix: str) -> dict:
    if not traces:
        return {}
    return {
        f"{prefix}/accuracy": float(np.mean([t.correct for t in traces])),
        f"{prefix}/mean_target_rank": _nanmean([np.mean(t.step_target_ranks) if t.step_target_ranks else math.nan for t in traces]),
        f"{prefix}/mean_correct_margin": _nanmean([np.mean(t.step_correct_margins) if t.step_correct_margins else math.nan for t in traces]),
        f"{prefix}/min_correct_margin": _nanmean([np.min(t.step_correct_margins) if t.step_correct_margins else math.nan for t in traces]),
        f"{prefix}/mean_world_margin": _nanmean([_nanmean(t.step_world_margins) if t.step_world_margins else math.nan for t in traces]),
        f"{prefix}/mean_mode_margin": _nanmean([_nanmean(t.step_mode_margins) if t.step_mode_margins else math.nan for t in traces]),
        f"{prefix}/mean_wrong_world_activation": _nanmean([_nanmean(t.wrong_world_activations) if t.wrong_world_activations else math.nan for t in traces]),
        f"{prefix}/mean_wrong_mode_activation": _nanmean([_nanmean(t.wrong_mode_activations) if t.wrong_mode_activations else math.nan for t in traces]),
    }


def summarize_by_mode_and_steps(traces: Sequence[PredictionTrace], prefix: str) -> dict:
    out: Dict[str, float] = {}
    for mode in MODE_NAMES:
        subset = [t for t in traces if t.task.mode == mode]
        if subset:
            out[f"{prefix}/accuracy_mode_{mode}"] = float(np.mean([t.correct for t in subset]))
    for steps in sorted(set(t.task.steps for t in traces)):
        subset = [t for t in traces if t.task.steps == steps]
        if subset:
            out[f"{prefix}/accuracy_steps_{steps}"] = float(np.mean([t.correct for t in subset]))
    return out


def route_summary(route_rows: Sequence[dict], prefix: str) -> dict:
    if not route_rows:
        return {}
    return {
        f"{prefix}/route_table_accuracy": float(np.mean([r["correct"] for r in route_rows])),
        f"{prefix}/mean_target_rank": float(np.mean([r["target_rank"] for r in route_rows])),
        f"{prefix}/mean_correct_margin": float(np.mean([r["correct_margin"] for r in route_rows])),
        f"{prefix}/mean_world_margin": _nanmean([r["world_margin"] for r in route_rows]),
        f"{prefix}/mean_mode_margin": _nanmean([r["mode_margin"] for r in route_rows]),
        f"{prefix}/mean_wrong_world_activation": _nanmean([r["wrong_world_activation"] for r in route_rows]),
        f"{prefix}/mean_wrong_mode_activation": _nanmean([r["wrong_mode_activation"] for r in route_rows]),
    }


def failure_counts(traces: Sequence[PredictionTrace], run_name: str, seed: int, phase: str, checkpoint: int, eval_world: str) -> List[dict]:
    counts: Dict[str, int] = {}
    for t in traces:
        if not t.correct:
            counts[t.failure_type] = counts.get(t.failure_type, 0) + 1
    return [
        {"run_name": run_name, "seed": seed, "phase": phase, "checkpoint": checkpoint, "eval_world": eval_world, "failure_type": k, "count": v}
        for k, v in sorted(counts.items())
    ]


def make_variants() -> List[VariantConfig]:
    return [
        VariantConfig(name="exp11_full_context_separated_memory", consolidation_strength=0.12, shared_route_weight=0.06, shared_update_fraction=0.04),
        VariantConfig(name="exp11_world_gated_plasticity", consolidation_strength=0.05, shared_route_weight=0.0, shared_update_fraction=0.0, world_gated_plasticity=True, learning_rate=1.2),
        VariantConfig(name="exp11_no_world_context", world_context=False, consolidation_strength=0.0, shared_route_weight=1.0, shared_update_fraction=1.0),
        VariantConfig(name="exp11_no_recurrence", recurrence=False, consolidation_strength=0.12, shared_route_weight=0.06, shared_update_fraction=0.04),
        VariantConfig(name="exp11_no_context_binding", context_binding=False, consolidation_strength=0.0, shared_route_weight=0.06, shared_update_fraction=0.04),
        VariantConfig(name="exp11_no_inhibition", inhibition=False, consolidation_strength=0.12, shared_route_weight=0.08, shared_update_fraction=0.06),
        VariantConfig(name="exp11_no_structural_plasticity", structural_plasticity=False),
        VariantConfig(name="exp11_no_consolidation", consolidation_strength=0.0, shared_route_weight=0.06, shared_update_fraction=0.04, learning_rate=1.2),
        VariantConfig(name="exp11_strong_consolidation", consolidation_strength=0.80, shared_route_weight=0.06, shared_update_fraction=0.04),
        VariantConfig(name="exp11_shared_edges_only", shared_edges_only=True, world_context=True, consolidation_strength=0.0, shared_route_weight=1.0, shared_update_fraction=1.0),
    ]


def evaluate_baselines(tasks: Sequence[Task], max_number: int, seed: int, worlds: Sequence[str]) -> List[dict]:
    rng = random.Random(seed)
    if not tasks:
        return []
    targets = [t.target for t in tasks]
    most_common = max(set(targets), key=targets.count)
    strategies = {
        "identity_start": lambda t: t.start,
        "most_frequent_target": lambda t: most_common,
        "lookup_oracle": lambda t: t.target,
        "random_uniform": lambda t: rng.randint(0, max_number),
    }
    for w in worlds:
        strategies[f"always_world_{w}"] = lambda t, world=w: true_target(t.start, t.mode, t.steps, world)
    rows: List[dict] = []
    for name, fn in strategies.items():
        correct = 0
        for t in tasks:
            pred = fn(t)
            correct += int(pred == t.target)
        rows.append({"baseline": name, "accuracy": correct / len(tasks), "n": len(tasks)})
    return rows
