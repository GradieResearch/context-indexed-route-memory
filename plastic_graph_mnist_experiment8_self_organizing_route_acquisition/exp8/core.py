"""Experiment 8 core: self-organizing contextual route acquisition.

Experiment 7 showed that a clean route field can be composed recurrently. Experiment 8
asks whether a local, assembly-based, plastic graph can *acquire* that route field
from one-step transition experiences, then compose unseen multi-step queries.

This implementation is intentionally small and inspectable. It uses distributed
number and mode assemblies over a latent hidden population and a recurrent route
matrix learned with local Hebbian-style updates. The route matrix is not filled by
an oracle table at evaluation time; it is formed only by exposure to transition
examples.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, Iterable, List, Optional, Sequence, Tuple
import math
import random

import numpy as np

MODES: Dict[str, int] = {
    "minus_one": -1,
    "plus_one": 1,
    "plus_two": 2,
}
MODE_NAMES: Tuple[str, ...] = tuple(MODES.keys())


@dataclass(frozen=True)
class Task:
    mode: str
    start: int
    steps: int
    target: int

    @property
    def delta(self) -> int:
        return MODES[self.mode]


@dataclass
class VariantConfig:
    name: str
    recurrence: bool = True
    structural_plasticity: bool = True
    context_binding: bool = True
    inhibition: bool = True
    reward_gate: bool = True
    homeostasis: bool = True
    context_bleed: float = 0.0
    feedback_noise: float = 0.0
    delayed_reward: bool = False
    learning_rate: float = 1.0
    inhibition_strength: float = 0.08
    wrong_context_inhibition: float = 0.05
    decay: float = 0.0
    noise_std: float = 0.0
    clip_min: float = -1.5
    clip_max: float = 3.0


@dataclass
class GraphConfig:
    max_number: int = 31
    hidden_units: int = 4096
    number_assembly_size: int = 72
    mode_assembly_size: int = 24
    pair_assembly_size: int = 48
    mode_overlap: float = 0.0
    init_scale: float = 1e-4


@dataclass
class PredictionTrace:
    task: Task
    predicted: int
    correct: bool
    step_predictions: List[int]
    step_expected: List[int]
    step_target_ranks: List[int]
    step_correct_margins: List[float]
    step_context_margins: List[float]
    wrong_route_activations: List[float]
    failure_type: str

    def to_row(self, run_name: str, seed: int, split: str, exposure_repeats: int, phase: str) -> dict:
        return {
            "run_name": run_name,
            "seed": seed,
            "split": split,
            "phase": phase,
            "exposure_repeats": exposure_repeats,
            "mode": self.task.mode,
            "start": self.task.start,
            "steps": self.task.steps,
            "target": self.task.target,
            "predicted": self.predicted,
            "correct": int(self.correct),
            "failure_type": self.failure_type,
            "mean_step_target_rank": float(np.mean(self.step_target_ranks)) if self.step_target_ranks else math.nan,
            "max_step_target_rank": float(np.max(self.step_target_ranks)) if self.step_target_ranks else math.nan,
            "mean_correct_margin": float(np.mean(self.step_correct_margins)) if self.step_correct_margins else math.nan,
            "min_correct_margin": float(np.min(self.step_correct_margins)) if self.step_correct_margins else math.nan,
            "mean_context_margin": _nanmean_or_nan(self.step_context_margins) if self.step_context_margins else math.nan,
            "min_context_margin": _nanmin_or_nan(self.step_context_margins) if self.step_context_margins else math.nan,
            "mean_wrong_route_activation": _nanmean_or_nan(self.wrong_route_activations) if self.wrong_route_activations else math.nan,
            "expected_path": "->".join(map(str, [self.task.start] + self.step_expected)),
            "actual_path": "->".join(map(str, [self.task.start] + self.step_predictions)),
        }


def true_target(start: int, mode: str, steps: int) -> int:
    return start + MODES[mode] * steps


def generate_bounded_tasks(max_number: int, max_steps: int, min_steps: int = 1) -> List[Task]:
    tasks: List[Task] = []
    for mode in MODE_NAMES:
        for start in range(max_number + 1):
            for steps in range(min_steps, max_steps + 1):
                target = true_target(start, mode, steps)
                if 0 <= target <= max_number:
                    tasks.append(Task(mode=mode, start=start, steps=steps, target=target))
    return tasks


def generate_transition_tasks(max_number: int) -> List[Task]:
    return generate_bounded_tasks(max_number, max_steps=1, min_steps=1)


def shuffled_repeated(items: Sequence[Task], repeats: int, rng: random.Random) -> List[Task]:
    out: List[Task] = []
    for _ in range(repeats):
        batch = list(items)
        rng.shuffle(batch)
        out.extend(batch)
    return out




def _nanmean_or_nan(values) -> float:
    arr = np.asarray(values, dtype=float)
    arr = arr[~np.isnan(arr)]
    return float(np.mean(arr)) if arr.size else math.nan

def _nanmin_or_nan(values) -> float:
    arr = np.asarray(values, dtype=float)
    arr = arr[~np.isnan(arr)]
    return float(np.min(arr)) if arr.size else math.nan

def _safe_sigmoid(x: float) -> float:
    if x >= 35:
        return 1.0
    if x <= -35:
        return 0.0
    return 1.0 / (1.0 + math.exp(-x))


class AssemblyWorld:
    """Sparse distributed number/mode assemblies over a latent population."""

    def __init__(self, cfg: GraphConfig, seed: int):
        self.cfg = cfg
        self.rng = np.random.default_rng(seed)
        if cfg.number_assembly_size + cfg.mode_assembly_size >= cfg.hidden_units:
            raise ValueError("Assembly sizes are too large for hidden_units.")

        # Number assemblies are random sparse subsets. We allow mild overlap because
        # real distributed representations are not perfectly orthogonal.
        self.number_assemblies: List[np.ndarray] = []
        for _ in range(cfg.max_number + 1):
            idx = self.rng.choice(cfg.hidden_units, size=cfg.number_assembly_size, replace=False)
            self.number_assemblies.append(np.array(sorted(idx), dtype=np.int32))

        shared_count = int(round(cfg.mode_assembly_size * max(0.0, min(1.0, cfg.mode_overlap))))
        shared = self.rng.choice(cfg.hidden_units, size=shared_count, replace=False) if shared_count else np.array([], dtype=np.int32)
        used_shared = set(int(x) for x in shared)
        self.mode_assemblies: Dict[str, np.ndarray] = {}
        for mode in MODE_NAMES:
            unique_count = cfg.mode_assembly_size - shared_count
            if unique_count > 0:
                # Avoid reusing the shared units within the same mode assembly.
                candidates = np.array([i for i in range(cfg.hidden_units) if i not in used_shared], dtype=np.int32)
                unique = self.rng.choice(candidates, size=unique_count, replace=False)
                idx = np.concatenate([shared, unique])
            else:
                idx = shared.copy()
            self.mode_assemblies[mode] = np.array(sorted(idx), dtype=np.int32)

        # Pair assemblies are the explicit context-binding substrate: they represent
        # the coactivation of a source number and a mode. They are still randomly
        # assigned latent units; the target route itself is acquired by local plasticity.
        self.pair_assemblies: Dict[Tuple[int, str], np.ndarray] = {}
        for n in range(cfg.max_number + 1):
            for mode in MODE_NAMES:
                idx = self.rng.choice(cfg.hidden_units, size=cfg.pair_assembly_size, replace=False)
                self.pair_assemblies[(n, mode)] = np.array(sorted(idx), dtype=np.int32)

    def number(self, n: int) -> np.ndarray:
        return self.number_assemblies[n]

    def mode(self, mode: str) -> np.ndarray:
        return self.mode_assemblies[mode]

    def pair(self, source: int, mode: str) -> np.ndarray:
        return self.pair_assemblies[(source, mode)]

    def combined_pre(self, source: int, mode: str, variant: VariantConfig, rng: np.random.Generator, include_context: bool = True) -> np.ndarray:
        parts = [self.number(source)]
        if include_context and variant.context_binding:
            parts.append(self.mode(mode))
            parts.append(self.pair(source, mode))
            if variant.context_bleed > 0.0:
                for other_mode in MODE_NAMES:
                    if other_mode == mode:
                        continue
                    other_mode_asm = self.mode(other_mode)
                    take_mode = int(round(len(other_mode_asm) * variant.context_bleed))
                    if take_mode > 0:
                        parts.append(rng.choice(other_mode_asm, size=take_mode, replace=False))
                    other_pair = self.pair(source, other_mode)
                    take_pair = int(round(len(other_pair) * variant.context_bleed))
                    if take_pair > 0:
                        parts.append(rng.choice(other_pair, size=take_pair, replace=False))
        return np.unique(np.concatenate(parts)).astype(np.int32)


class SelfOrganizingRouteGraph:
    """Local-plastic recurrent route graph.

    W[pre_unit, post_unit] is strengthened when a source+mode assembly precedes a
    target number assembly. Recurrent prediction repeatedly applies the same learned
    W to the current number assembly under the active context.
    """

    def __init__(self, graph_cfg: GraphConfig, variant: VariantConfig, seed: int):
        self.graph_cfg = graph_cfg
        self.variant = variant
        self.seed = seed
        self.rng = np.random.default_rng(seed)
        self.py_rng = random.Random(seed)
        self.world = AssemblyWorld(graph_cfg, seed)
        self.W = self.rng.normal(0.0, graph_cfg.init_scale, size=(graph_cfg.hidden_units, graph_cfg.hidden_units)).astype(np.float32)
        self._score_cache: Optional[Dict[Tuple[int, str], np.ndarray]] = None

    @property
    def max_number(self) -> int:
        return self.graph_cfg.max_number

    def _valid_next(self, source: int, mode: str) -> Optional[int]:
        target = true_target(source, mode, 1)
        if 0 <= target <= self.max_number:
            return target
        return None

    def _scores_for_pre(self, pre: np.ndarray) -> np.ndarray:
        # Aggregate drive into latent units, then decode by average drive into each
        # number assembly. Mean rather than sum keeps scores comparable across assembly sizes.
        drive = self.W[pre, :].sum(axis=0)
        scores = np.empty(self.max_number + 1, dtype=np.float32)
        for n in range(self.max_number + 1):
            scores[n] = float(np.mean(drive[self.world.number(n)]))
        return scores

    def finalize(self) -> None:
        """Freeze learned weights into a source/mode score cache for fast evaluation."""
        cache: Dict[Tuple[int, str], np.ndarray] = {}
        for source in range(self.max_number + 1):
            for mode in MODE_NAMES:
                pre = self.world.combined_pre(source, mode, self.variant, self.rng, include_context=True)
                cache[(source, mode)] = self._scores_for_pre(pre)
        self._score_cache = cache

    def scores(self, source: int, mode: str) -> np.ndarray:
        if self._score_cache is not None:
            return self._score_cache[(source, mode)]
        pre = self.world.combined_pre(source, mode, self.variant, self.rng, include_context=True)
        return self._scores_for_pre(pre)

    def train_transition(self, source: int, mode: str, true_target_n: int) -> None:
        v = self.variant
        self._score_cache = None
        if not v.structural_plasticity:
            return

        observed_target = true_target_n
        reward = 1.0
        if v.feedback_noise > 0.0 and self.rng.random() < v.feedback_noise:
            wrong = [n for n in range(self.max_number + 1) if n != true_target_n]
            observed_target = int(self.rng.choice(wrong))
            # Reward-gated variant treats noisy feedback as uncertain and skips the update.
            # No-reward-gate variant incorporates the misleading update.
            if v.reward_gate:
                reward = 0.0

        if v.reward_gate and reward <= 0.0:
            return

        if v.decay > 0:
            self.W *= np.float32(1.0 - v.decay)

        pre = self.world.combined_pre(source, mode, v, self.rng, include_context=v.context_binding)
        target = self.world.number(observed_target)
        delta = np.float32(v.learning_rate / max(1, len(pre)))
        self.W[np.ix_(pre, target)] += delta

        if v.inhibition:
            # Suppress other number assemblies from the same active source/context.
            wrong_units: List[np.ndarray] = [self.world.number(n) for n in range(self.max_number + 1) if n != observed_target]
            wrong_union = np.unique(np.concatenate(wrong_units)).astype(np.int32)
            self.W[np.ix_(pre, wrong_union)] -= np.float32(v.inhibition_strength * v.learning_rate / max(1, len(pre)))

            # Suppress the same target when driven by competing mode assemblies at this source.
            if v.context_binding:
                for other_mode in MODE_NAMES:
                    if other_mode == mode:
                        continue
                    other_pre = self.world.combined_pre(source, other_mode, v, self.rng, include_context=True)
                    self.W[np.ix_(other_pre, target)] -= np.float32(v.wrong_context_inhibition * v.learning_rate / max(1, len(other_pre)))

        if v.noise_std > 0.0:
            self.W[np.ix_(pre, target)] += self.rng.normal(0.0, v.noise_std, size=(len(pre), len(target))).astype(np.float32)

        if v.homeostasis:
            np.clip(self.W, v.clip_min, v.clip_max, out=self.W)

    def train_path_delayed(self, task: Task) -> None:
        """Optional delayed reward update: traverse true path, then update all local edges.

        This is still local at consolidation time, but it withholds updates until the
        path endpoint is known. It is useful for later stress testing delayed credit.
        """
        current = task.start
        transitions: List[Tuple[int, str, int]] = []
        for _ in range(task.steps):
            nxt = self._valid_next(current, task.mode)
            if nxt is None:
                return
            transitions.append((current, task.mode, nxt))
            current = nxt
        for source, mode, target in transitions:
            self.train_transition(source, mode, target)

    def train_curriculum(self, transition_tasks: Sequence[Task], repeats: int, composition_tasks: Sequence[Task], path_repeats: int) -> None:
        if self.variant.delayed_reward and path_repeats > 0:
            for task in shuffled_repeated(composition_tasks, path_repeats, self.py_rng):
                self.train_path_delayed(task)
            return
        for task in shuffled_repeated(transition_tasks, repeats, self.py_rng):
            self.train_transition(task.start, task.mode, task.target)
        # Optional consolidation is off for the main experiment. It exists as a control.
        for task in shuffled_repeated(composition_tasks, path_repeats, self.py_rng):
            self.train_path_delayed(task)

    def target_rank_and_margin(self, source: int, mode: str, target: int) -> Tuple[int, float, float, float]:
        scores = self.scores(source, mode)
        order = np.argsort(scores)[::-1]
        rank = int(np.where(order == target)[0][0]) + 1
        target_score = float(scores[target])
        wrong_scores = np.delete(scores, target)
        best_wrong = float(np.max(wrong_scores)) if wrong_scores.size else -math.inf
        return rank, target_score - best_wrong, target_score, float(np.max(scores))

    def context_margin(self, source: int, mode: str, target: int) -> float:
        if not self.variant.context_binding:
            return math.nan
        correct = float(self.scores(source, mode)[target])
        wrong = [float(self.scores(source, other)[target]) for other in MODE_NAMES if other != mode]
        return correct - max(wrong) if wrong else math.nan

    def wrong_route_activation(self, source: int, mode: str, target: int) -> float:
        if not self.variant.context_binding:
            return math.nan
        correct_score = float(self.scores(source, mode)[target])
        wrong_scores = [float(self.scores(source, other)[target]) for other in MODE_NAMES if other != mode]
        if not wrong_scores:
            return math.nan
        # High when wrong modes also strongly support the same target.
        return float(np.mean([_safe_sigmoid(w - correct_score) for w in wrong_scores]))

    def predict(self, task: Task) -> PredictionTrace:
        current = task.start
        step_predictions: List[int] = []
        step_expected: List[int] = []
        ranks: List[int] = []
        margins: List[float] = []
        context_margins: List[float] = []
        wrong_acts: List[float] = []
        failure_type = "none"

        steps_to_run = task.steps if self.variant.recurrence else 1
        expected_current = task.start
        for step_i in range(steps_to_run):
            expected_next = self._valid_next(expected_current, task.mode)
            if expected_next is None:
                break
            step_expected.append(expected_next)

            scores = self.scores(current, task.mode)
            predicted_next = int(np.argmax(scores))
            step_predictions.append(predicted_next)

            rank, margin, _, _ = self.target_rank_and_margin(current, task.mode, expected_next if current == expected_current else true_target(current, task.mode, 1) if 0 <= true_target(current, task.mode, 1) <= self.max_number else predicted_next)
            ranks.append(rank)
            margins.append(margin)
            context_margins.append(self.context_margin(current, task.mode, expected_next if current == expected_current else predicted_next))
            wrong_acts.append(self.wrong_route_activation(current, task.mode, expected_next if current == expected_current else predicted_next))

            if predicted_next != expected_next and failure_type == "none":
                if step_i == 0:
                    failure_type = "first_step_failure"
                else:
                    failure_type = "mid_route_drift"
            current = predicted_next
            expected_current = expected_next

        predicted = current if self.variant.recurrence else (step_predictions[-1] if step_predictions else task.start)
        correct = predicted == task.target
        if not correct and not self.variant.recurrence:
            failure_type = "no_recurrence_single_step_only"
        elif not correct and failure_type == "none":
            failure_type = "decoder_or_endpoint_failure"
        return PredictionTrace(
            task=task,
            predicted=predicted,
            correct=correct,
            step_predictions=step_predictions,
            step_expected=step_expected,
            step_target_ranks=ranks,
            step_correct_margins=margins,
            step_context_margins=context_margins,
            wrong_route_activations=wrong_acts,
            failure_type=failure_type,
        )

    def route_diagnostics(self) -> List[dict]:
        rows: List[dict] = []
        for mode in MODE_NAMES:
            for source in range(self.max_number + 1):
                target = self._valid_next(source, mode)
                if target is None:
                    continue
                scores = self.scores(source, mode)
                predicted = int(np.argmax(scores))
                rank, margin, target_score, best_score = self.target_rank_and_margin(source, mode, target)
                order = np.argsort(scores)[::-1][:5]
                rows.append({
                    "mode": mode,
                    "source": source,
                    "true_target": target,
                    "predicted_target": predicted,
                    "correct": int(predicted == target),
                    "target_rank": rank,
                    "correct_margin": margin,
                    "context_margin": self.context_margin(source, mode, target),
                    "wrong_route_activation": self.wrong_route_activation(source, mode, target),
                    "target_score": target_score,
                    "best_score": best_score,
                    "top_targets": ";".join(f"{int(i)}:{float(scores[i]):.5f}" for i in order),
                })
        return rows


def make_variants(base_context_bleed: float = 0.0, feedback_noise: float = 0.0) -> List[VariantConfig]:
    return [
        VariantConfig(name="exp8_full_self_organizing_route_field", context_bleed=base_context_bleed, feedback_noise=feedback_noise),
        VariantConfig(name="exp8_no_recurrence", recurrence=False, context_bleed=base_context_bleed, feedback_noise=feedback_noise),
        VariantConfig(name="exp8_no_structural_plasticity", structural_plasticity=False, context_bleed=base_context_bleed, feedback_noise=feedback_noise),
        VariantConfig(name="exp8_no_context_binding", context_binding=False, context_bleed=base_context_bleed, feedback_noise=feedback_noise),
        VariantConfig(name="exp8_no_inhibition", inhibition=False, context_bleed=base_context_bleed, feedback_noise=feedback_noise),
        VariantConfig(name="exp8_no_reward_gate", reward_gate=False, context_bleed=base_context_bleed, feedback_noise=feedback_noise),
        VariantConfig(name="exp8_no_homeostasis", homeostasis=False, clip_min=-1e9, clip_max=1e9, context_bleed=base_context_bleed, feedback_noise=feedback_noise),
        VariantConfig(name="exp8_context_bleed", context_bleed=max(base_context_bleed, 0.20), feedback_noise=feedback_noise),
    ]


def summarize_traces(traces: Sequence[PredictionTrace], prefix: str) -> dict:
    if not traces:
        return {}
    return {
        f"{prefix}/accuracy": float(np.mean([t.correct for t in traces])),
        f"{prefix}/mean_target_rank": float(np.nanmean([np.mean(t.step_target_ranks) if t.step_target_ranks else math.nan for t in traces])),
        f"{prefix}/mean_correct_margin": float(np.nanmean([np.mean(t.step_correct_margins) if t.step_correct_margins else math.nan for t in traces])),
        f"{prefix}/min_correct_margin": float(np.nanmean([np.min(t.step_correct_margins) if t.step_correct_margins else math.nan for t in traces])),
        f"{prefix}/mean_context_margin": _nanmean_or_nan([_nanmean_or_nan(t.step_context_margins) if t.step_context_margins else math.nan for t in traces]),
        f"{prefix}/mean_wrong_route_activation": _nanmean_or_nan([_nanmean_or_nan(t.wrong_route_activations) if t.wrong_route_activations else math.nan for t in traces]),
    }


def summarize_by_mode_and_steps(traces: Sequence[PredictionTrace], prefix: str) -> dict:
    metrics: Dict[str, float] = {}
    for mode in MODE_NAMES:
        subset = [t for t in traces if t.task.mode == mode]
        if subset:
            metrics[f"{prefix}/accuracy_mode_{mode}"] = float(np.mean([t.correct for t in subset]))
    for steps in sorted(set(t.task.steps for t in traces)):
        subset = [t for t in traces if t.task.steps == steps]
        if subset:
            metrics[f"{prefix}/accuracy_steps_{steps}"] = float(np.mean([t.correct for t in subset]))
    return metrics


def evaluate_baselines(tasks: Sequence[Task], max_number: int, seed: int) -> List[dict]:
    rng = random.Random(seed)
    rows: List[dict] = []
    if not tasks:
        return rows
    targets = [t.target for t in tasks]
    most_common = max(set(targets), key=targets.count)
    strategies = {
        "identity_start": lambda t: t.start,
        "most_frequent_target": lambda t: most_common,
        "always_minus_one": lambda t: true_target(t.start, "minus_one", t.steps),
        "always_plus_one": lambda t: true_target(t.start, "plus_one", t.steps),
        "always_plus_two": lambda t: true_target(t.start, "plus_two", t.steps),
        "lookup_oracle": lambda t: t.target,
        "transition_table_composition_oracle": lambda t: t.target,
        "random_uniform": lambda t: rng.randint(0, max_number),
    }
    for name, fn in strategies.items():
        correct = 0
        for t in tasks:
            pred = fn(t)
            correct += int(pred == t.target)
        rows.append({"baseline": name, "accuracy": correct / len(tasks), "n": len(tasks)})
    return rows


def route_summary(route_rows: Sequence[dict]) -> dict:
    if not route_rows:
        return {}
    return {
        "route_table/accuracy": float(np.mean([r["correct"] for r in route_rows])),
        "route_table/mean_target_rank": float(np.mean([r["target_rank"] for r in route_rows])),
        "route_table/mean_correct_margin": float(np.mean([r["correct_margin"] for r in route_rows])),
        "route_table/mean_context_margin": _nanmean_or_nan([r["context_margin"] for r in route_rows]),
        "route_table/mean_wrong_route_activation": _nanmean_or_nan([r["wrong_route_activation"] for r in route_rows]),
    }
