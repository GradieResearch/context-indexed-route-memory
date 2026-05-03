"""Core utilities for Experiment 7: route-field diagnostics.

This experiment is intentionally diagnostic rather than benchmark-oriented. It uses a
small symbolic successor world so we can inspect whether a recurrent plastic route
field has actually learned the transition table it claims to traverse.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
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
    context_mixing: float = 0.0
    noise_std: float = 0.0
    init_scale: float = 1e-4
    learning_rate: float = 1.0
    decay: float = 0.0
    wrong_target_decay: float = 0.15
    wrong_context_decay: float = 0.10
    clip_min: float = -3.0
    clip_max: float = 10.0


@dataclass
class PredictionTrace:
    task: Task
    predicted: int
    correct: bool
    step_predictions: List[int]
    step_target_ranks: List[int]
    step_correct_margins: List[float]
    step_context_margins: List[float]
    wrong_route_activations: List[float]

    def to_metric_row(self, run_name: str, seed: int, split: str) -> dict:
        return {
            "run_name": run_name,
            "seed": seed,
            "split": split,
            "mode": self.task.mode,
            "start": self.task.start,
            "steps": self.task.steps,
            "target": self.task.target,
            "predicted": self.predicted,
            "correct": int(self.correct),
            "mean_step_target_rank": float(np.mean(self.step_target_ranks)) if self.step_target_ranks else math.nan,
            "max_step_target_rank": float(np.max(self.step_target_ranks)) if self.step_target_ranks else math.nan,
            "mean_correct_margin": float(np.mean(self.step_correct_margins)) if self.step_correct_margins else math.nan,
            "min_correct_margin": float(np.min(self.step_correct_margins)) if self.step_correct_margins else math.nan,
            "mean_context_margin": float(np.mean(self.step_context_margins)) if self.step_context_margins else math.nan,
            "min_context_margin": float(np.min(self.step_context_margins)) if self.step_context_margins else math.nan,
            "mean_wrong_route_activation": float(np.mean(self.wrong_route_activations)) if self.wrong_route_activations else math.nan,
            "path": "->".join(map(str, [self.task.start] + self.step_predictions)),
        }


def true_target(start: int, mode: str, steps: int) -> int:
    return start + MODES[mode] * steps


def generate_bounded_tasks(max_number: int, max_steps: int, min_steps: int = 1) -> List[Task]:
    """Generate all tasks whose final target stays within the number world.

    We deliberately use bounded tasks so failures cannot be blamed on out-of-range
    boundary effects. This was one of the main diagnostic risks identified after
    Experiment 5.
    """
    tasks: List[Task] = []
    for mode in MODE_NAMES:
        for start in range(max_number + 1):
            for steps in range(min_steps, max_steps + 1):
                target = true_target(start, mode, steps)
                if 0 <= target <= max_number:
                    tasks.append(Task(mode=mode, start=start, steps=steps, target=target))
    return tasks


def generate_transition_tasks(max_number: int) -> List[Task]:
    return generate_bounded_tasks(max_number=max_number, max_steps=1, min_steps=1)


def shuffled_repeated(items: Sequence[Task], repeats: int, rng: random.Random) -> List[Task]:
    out: List[Task] = []
    for _ in range(repeats):
        batch = list(items)
        rng.shuffle(batch)
        out.extend(batch)
    return out


class ContextualRouteFieldGraph:
    """A minimal recurrent plastic graph over discrete number assemblies.

    The route field is represented as mode-conditioned transition scores:

        route[mode, source, destination]

    When context binding is disabled, all modes write into one shared route table.
    This intentionally creates a collision diagnostic: the same source state has
    competing targets under different modes.
    """

    def __init__(self, max_number: int, config: VariantConfig, seed: int):
        self.max_number = max_number
        self.num_numbers = max_number + 1
        self.config = config
        self.rng = np.random.default_rng(seed)
        self.py_rng = random.Random(seed)
        mode_dim = len(MODE_NAMES) if config.context_binding else 1
        self.route = self.rng.normal(0.0, config.init_scale, size=(mode_dim, self.num_numbers, self.num_numbers))
        # Strongly discourage invalid self-loop default dominance without making
        # impossible transitions unreachable.
        self.route[:, :, :] -= 1e-6

    def _mode_index(self, mode: str) -> int:
        if not self.config.context_binding:
            return 0
        return MODE_NAMES.index(mode)

    def _valid_next_target(self, source: int, mode: str) -> Optional[int]:
        target = true_target(source, mode, 1)
        if 0 <= target <= self.max_number:
            return target
        return None

    def train_transition(self, source: int, mode: str, target: int, reward: float = 1.0) -> None:
        if not self.config.structural_plasticity:
            return
        if self.config.reward_gate:
            gated_reward = max(0.0, reward)
        else:
            gated_reward = 1.0
        if gated_reward == 0.0:
            return

        c = self.config
        mi = self._mode_index(mode)
        if c.decay:
            self.route *= (1.0 - c.decay)

        self.route[mi, source, target] += c.learning_rate * gated_reward

        if c.inhibition:
            wrong_targets = np.ones(self.num_numbers, dtype=bool)
            wrong_targets[target] = False
            self.route[mi, source, wrong_targets] -= c.wrong_target_decay * c.learning_rate * gated_reward
            if c.context_binding:
                for omi, other_mode in enumerate(MODE_NAMES):
                    if omi != mi:
                        self.route[omi, source, target] -= c.wrong_context_decay * c.learning_rate * gated_reward

        if c.noise_std > 0:
            self.route[:, source, :] += self.rng.normal(0.0, c.noise_std, size=self.route[:, source, :].shape)

        np.clip(self.route, c.clip_min, c.clip_max, out=self.route)

    def train_task_path(self, task: Task) -> None:
        current = task.start
        for _ in range(task.steps):
            target = self._valid_next_target(current, task.mode)
            if target is None:
                return
            self.train_transition(current, task.mode, target, reward=1.0)
            current = target

    def transition_scores(self, source: int, mode: str) -> np.ndarray:
        c = self.config
        if c.context_binding:
            mi = self._mode_index(mode)
            scores = np.array(self.route[mi, source, :], copy=True)
            if c.context_mixing > 0 and len(MODE_NAMES) > 1:
                other_indices = [i for i, m in enumerate(MODE_NAMES) if m != mode]
                other_mean = np.mean(self.route[other_indices, source, :], axis=0)
                scores = (1.0 - c.context_mixing) * scores + c.context_mixing * other_mean
        else:
            scores = np.array(self.route[0, source, :], copy=True)
        return scores

    def target_rank_and_margin(self, source: int, mode: str, target: int) -> Tuple[int, float]:
        scores = self.transition_scores(source, mode)
        target_score = float(scores[target])
        # Rank is 1-based. Ties are pessimistically handled by sorting descending.
        order = np.argsort(scores)[::-1]
        rank = int(np.where(order == target)[0][0]) + 1
        wrong_scores = np.delete(scores, target)
        best_wrong = float(np.max(wrong_scores)) if wrong_scores.size else -math.inf
        return rank, target_score - best_wrong

    def context_margin(self, source: int, mode: str, target: int) -> float:
        if not self.config.context_binding:
            return math.nan
        mi = self._mode_index(mode)
        correct = float(self.route[mi, source, target])
        wrong = [float(self.route[i, source, target]) for i in range(len(MODE_NAMES)) if i != mi]
        return correct - max(wrong) if wrong else math.nan

    def wrong_route_activation(self, source: int, mode: str, target: int) -> float:
        if not self.config.context_binding:
            return math.nan
        mi = self._mode_index(mode)
        wrong_values = [float(self.route[i, source, target]) for i in range(len(MODE_NAMES)) if i != mi]
        if not wrong_values:
            return math.nan
        # Sigmoid maps raw drive into a bounded diagnostic. This makes the metric
        # comparable when variants have different total recurrent drive scales.
        return float(np.mean([1.0 / (1.0 + math.exp(-v)) for v in wrong_values]))

    def predict(self, task: Task) -> PredictionTrace:
        current = task.start
        step_predictions: List[int] = []
        ranks: List[int] = []
        correct_margins: List[float] = []
        context_margins: List[float] = []
        wrong_activations: List[float] = []

        steps_to_run = task.steps if self.config.recurrence else 1
        for _ in range(steps_to_run):
            step_target = self._valid_next_target(current, task.mode)
            scores = self.transition_scores(current, task.mode)
            predicted_next = int(np.argmax(scores))
            step_predictions.append(predicted_next)

            if step_target is not None:
                rank, margin = self.target_rank_and_margin(current, task.mode, step_target)
                ranks.append(rank)
                correct_margins.append(margin)
                context_margins.append(self.context_margin(current, task.mode, step_target))
                wrong_activations.append(self.wrong_route_activation(current, task.mode, step_target))

            current = predicted_next

        predicted = current
        correct = predicted == task.target
        return PredictionTrace(
            task=task,
            predicted=predicted,
            correct=correct,
            step_predictions=step_predictions,
            step_target_ranks=ranks,
            step_correct_margins=correct_margins,
            step_context_margins=context_margins,
            wrong_route_activations=wrong_activations,
        )

    def route_diagnostics(self) -> List[dict]:
        rows: List[dict] = []
        for mode in MODE_NAMES:
            for source in range(self.num_numbers):
                target = self._valid_next_target(source, mode)
                if target is None:
                    continue
                scores = self.transition_scores(source, mode)
                pred = int(np.argmax(scores))
                rank, margin = self.target_rank_and_margin(source, mode, target)
                top_indices = list(np.argsort(scores)[::-1][:5])
                top_targets = ";".join(f"{i}:{scores[i]:.4f}" for i in top_indices)
                rows.append({
                    "mode": mode,
                    "source": source,
                    "true_target": target,
                    "predicted_target": pred,
                    "correct": int(pred == target),
                    "target_rank": rank,
                    "correct_margin": margin,
                    "context_margin": self.context_margin(source, mode, target),
                    "wrong_route_activation": self.wrong_route_activation(source, mode, target),
                    "target_score": float(scores[target]),
                    "best_score": float(np.max(scores)),
                    "top_targets": top_targets,
                })
        return rows

    def route_matrix_for_mode(self, mode: str) -> np.ndarray:
        mat = np.zeros((self.num_numbers, self.num_numbers), dtype=float)
        for source in range(self.num_numbers):
            mat[source, :] = self.transition_scores(source, mode)
        return mat


def make_variants() -> List[VariantConfig]:
    return [
        VariantConfig(name="exp7_full_route_field"),
        VariantConfig(name="exp7_no_recurrence", recurrence=False),
        VariantConfig(name="exp7_no_context_binding", context_binding=False),
        VariantConfig(name="exp7_no_structural_plasticity", structural_plasticity=False, init_scale=0.05),
        VariantConfig(name="exp7_no_inhibition", inhibition=False),
        VariantConfig(name="exp7_context_bleed", context_mixing=0.35),
        VariantConfig(name="exp7_noisy_plasticity", noise_std=0.025),
    ]


def task_accuracy(traces: Sequence[PredictionTrace]) -> float:
    if not traces:
        return math.nan
    return float(np.mean([t.correct for t in traces]))


def summarize_traces(traces: Sequence[PredictionTrace], prefix: str = "") -> Dict[str, float]:
    if not traces:
        return {}
    rows = [t.to_metric_row(run_name="", seed=0, split="") for t in traces]
    result: Dict[str, float] = {}
    result[f"{prefix}accuracy"] = float(np.mean([r["correct"] for r in rows]))
    result[f"{prefix}average_target_rank"] = float(np.nanmean([r["mean_step_target_rank"] for r in rows]))
    result[f"{prefix}average_correct_margin"] = float(np.nanmean([r["mean_correct_margin"] for r in rows]))
    result[f"{prefix}minimum_correct_margin"] = float(np.nanmean([r["min_correct_margin"] for r in rows]))
    result[f"{prefix}average_context_margin"] = float(np.nanmean([r["mean_context_margin"] for r in rows]))
    result[f"{prefix}average_wrong_route_activation"] = float(np.nanmean([r["mean_wrong_route_activation"] for r in rows]))
    return result


def evaluate_baselines(tasks: Sequence[Task], max_number: int, seed: int) -> List[dict]:
    rng = random.Random(seed)
    targets = [t.target for t in tasks]
    most_frequent = max(set(targets), key=targets.count) if targets else 0

    def clamp(n: int) -> int:
        return max(0, min(max_number, n))

    rows: List[dict] = []
    baseline_fns = {
        "random_uniform": lambda t: rng.randint(0, max_number),
        "most_frequent_target": lambda t: most_frequent,
        "identity_start": lambda t: t.start,
        "always_plus_one": lambda t: clamp(t.start + t.steps),
        "always_plus_two": lambda t: clamp(t.start + 2 * t.steps),
        "always_minus_one": lambda t: clamp(t.start - t.steps),
        "lookup_oracle": lambda t: t.target,
    }
    for name, fn in baseline_fns.items():
        correct = [int(fn(t) == t.target) for t in tasks]
        rows.append({
            "baseline": name,
            "accuracy": float(np.mean(correct)) if correct else math.nan,
            "n": len(correct),
        })
    return rows


def evaluate_transition_table_oracle(tasks: Sequence[Task], max_number: int) -> dict:
    """A symbolic ceiling: exact one-step table + exact repeated composition."""
    correct = []
    for task in tasks:
        current = task.start
        for _ in range(task.steps):
            current = true_target(current, task.mode, 1)
        correct.append(int(current == task.target))
    return {"baseline": "transition_table_composition_oracle", "accuracy": float(np.mean(correct)), "n": len(correct)}
