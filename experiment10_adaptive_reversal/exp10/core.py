"""Experiment 10 core: rule reversal, retention, and adaptive rebinding.

Experiment 10 builds on Experiment 8/9. A local plastic route field first learns
rule set A from one-step transitions, then the transition meanings are changed to
rule set B. The experiment measures whether the graph can adapt to the new rule,
how much old-rule structure remains, whether consolidation slows/helps retention,
and whether a higher-level task context can preserve both worlds without overwrite.

The implementation intentionally remains inspectable. It uses sparse distributed
assemblies over a latent hidden population and a local Hebbian-style route matrix.
Multi-step composition is never directly trained; it is evaluated by recurrently
traversing the learned one-step route field.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Sequence, Tuple
import math
import random

import numpy as np

# Mode labels are stable. The rule set chooses their delta.
MODE_NAMES: Tuple[str, ...] = ("minus_one", "plus_one", "plus_two")
RULE_DELTAS: Dict[str, Dict[str, int]] = {
    "A": {"minus_one": -1, "plus_one": 1, "plus_two": 2},
    # plus_two is deliberately unchanged as an anchor. plus_one/minus_one reverse.
    "B": {"minus_one": 1, "plus_one": -1, "plus_two": 2},
}
RULE_NAMES: Tuple[str, ...] = ("A", "B")


@dataclass(frozen=True)
class Task:
    rule: str
    mode: str
    start: int
    steps: int
    target: int

    @property
    def delta(self) -> int:
        return RULE_DELTAS[self.rule][self.mode]


@dataclass
class VariantConfig:
    name: str
    recurrence: bool = True
    structural_plasticity: bool = True
    context_binding: bool = True
    inhibition: bool = True
    reward_gate: bool = True
    eligibility_trace: bool = True
    homeostasis: bool = True
    dual_context_worlds: bool = False
    consolidation_strength: float = 0.0
    consolidation_on_reversal: bool = False
    learning_rate: float = 1.0
    reversal_learning_rate_multiplier: float = 1.0
    switchback_learning_rate_multiplier: float = 1.0
    inhibition_strength: float = 0.08
    wrong_context_inhibition: float = 0.05
    feedback_noise: float = 0.0
    reward_delay_steps: int = 0
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
    world_assembly_size: int = 24
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


def true_target(start: int, mode: str, steps: int, rule: str) -> int:
    return start + RULE_DELTAS[rule][mode] * steps


def generate_bounded_tasks(max_number: int, max_steps: int, rule: str, min_steps: int = 1) -> List[Task]:
    tasks: List[Task] = []
    for mode in MODE_NAMES:
        for start in range(max_number + 1):
            for steps in range(min_steps, max_steps + 1):
                target = true_target(start, mode, steps, rule)
                if 0 <= target <= max_number:
                    tasks.append(Task(rule=rule, mode=mode, start=start, steps=steps, target=target))
    return tasks


def generate_transition_tasks(max_number: int, rule: str) -> List[Task]:
    return generate_bounded_tasks(max_number, max_steps=1, min_steps=1, rule=rule)


def shuffled_repeated(items: Sequence[Task], repeats: int, rng: random.Random) -> List[Task]:
    out: List[Task] = []
    for _ in range(max(0, repeats)):
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
    """Sparse distributed assemblies for numbers, modes, worlds, and source-mode pairs."""

    def __init__(self, cfg: GraphConfig, seed: int):
        self.cfg = cfg
        self.rng = np.random.default_rng(seed)
        max_asm = cfg.number_assembly_size + cfg.mode_assembly_size + cfg.pair_assembly_size + cfg.world_assembly_size
        if max_asm >= cfg.hidden_units:
            raise ValueError("Assembly sizes are too large for hidden_units.")

        self.number_assemblies: List[np.ndarray] = []
        for _ in range(cfg.max_number + 1):
            idx = self.rng.choice(cfg.hidden_units, size=cfg.number_assembly_size, replace=False)
            self.number_assemblies.append(np.array(sorted(idx), dtype=np.int32))

        self.mode_assemblies: Dict[str, np.ndarray] = {}
        for mode in MODE_NAMES:
            idx = self.rng.choice(cfg.hidden_units, size=cfg.mode_assembly_size, replace=False)
            self.mode_assemblies[mode] = np.array(sorted(idx), dtype=np.int32)

        self.world_assemblies: Dict[str, np.ndarray] = {}
        for rule in RULE_NAMES:
            idx = self.rng.choice(cfg.hidden_units, size=cfg.world_assembly_size, replace=False)
            self.world_assemblies[rule] = np.array(sorted(idx), dtype=np.int32)

        # Shared pair assemblies implement overwrite/reversal pressure.
        self.shared_pair_assemblies: Dict[Tuple[int, str], np.ndarray] = {}
        for n in range(cfg.max_number + 1):
            for mode in MODE_NAMES:
                idx = self.rng.choice(cfg.hidden_units, size=cfg.pair_assembly_size, replace=False)
                self.shared_pair_assemblies[(n, mode)] = np.array(sorted(idx), dtype=np.int32)

        # World-specific pair assemblies allow hierarchical context retention.
        self.world_pair_assemblies: Dict[Tuple[str, int, str], np.ndarray] = {}
        for rule in RULE_NAMES:
            for n in range(cfg.max_number + 1):
                for mode in MODE_NAMES:
                    idx = self.rng.choice(cfg.hidden_units, size=cfg.pair_assembly_size, replace=False)
                    self.world_pair_assemblies[(rule, n, mode)] = np.array(sorted(idx), dtype=np.int32)

    def number(self, n: int) -> np.ndarray:
        return self.number_assemblies[n]

    def mode(self, mode: str) -> np.ndarray:
        return self.mode_assemblies[mode]

    def world(self, rule: str) -> np.ndarray:
        return self.world_assemblies[rule]

    def pair(self, source: int, mode: str, rule_context: str, dual_context: bool) -> np.ndarray:
        if dual_context:
            return self.world_pair_assemblies[(rule_context, source, mode)]
        return self.shared_pair_assemblies[(source, mode)]

    def combined_pre(self, source: int, mode: str, rule_context: str, variant: VariantConfig) -> np.ndarray:
        if variant.dual_context_worlds and variant.context_binding:
            # In the dual-world condition, the higher-level context owns the route.
            # Avoid shared source/mode pre-units so B updates do not erase A through
            # common assemblies. The world-specific pair still encodes source+mode.
            parts = [self.world(rule_context), self.pair(source, mode, rule_context, True)]
            return np.unique(np.concatenate(parts)).astype(np.int32)
        parts = [self.number(source)]
        if variant.context_binding:
            parts.append(self.mode(mode))
            parts.append(self.pair(source, mode, rule_context, False))
        return np.unique(np.concatenate(parts)).astype(np.int32)


class AdaptiveRouteGraph:
    """Local-plastic route graph with reversal, consolidation, and dual-context support."""

    def __init__(self, graph_cfg: GraphConfig, variant: VariantConfig, seed: int):
        self.graph_cfg = graph_cfg
        self.variant = variant
        self.seed = seed
        self.rng = np.random.default_rng(seed)
        self.py_rng = random.Random(seed)
        self.world = AssemblyWorld(graph_cfg, seed)
        self.W = self.rng.normal(0.0, graph_cfg.init_scale, size=(graph_cfg.hidden_units, graph_cfg.hidden_units)).astype(np.float32)
        self.consolidated_W: Optional[np.ndarray] = None
        self._score_cache: Optional[Dict[Tuple[int, str, str], np.ndarray]] = None

    @property
    def max_number(self) -> int:
        return self.graph_cfg.max_number

    def _valid_next(self, source: int, mode: str, rule: str) -> Optional[int]:
        target = true_target(source, mode, 1, rule)
        if 0 <= target <= self.max_number:
            return target
        return None

    def _scores_for_pre(self, pre: np.ndarray) -> np.ndarray:
        drive = self.W[pre, :].sum(axis=0)
        scores = np.empty(self.max_number + 1, dtype=np.float32)
        for n in range(self.max_number + 1):
            scores[n] = float(np.mean(drive[self.world.number(n)]))
        return scores

    def finalize(self) -> None:
        cache: Dict[Tuple[int, str, str], np.ndarray] = {}
        for source in range(self.max_number + 1):
            for mode in MODE_NAMES:
                for rule_context in RULE_NAMES:
                    pre = self.world.combined_pre(source, mode, rule_context, self.variant)
                    cache[(source, mode, rule_context)] = self._scores_for_pre(pre)
        self._score_cache = cache

    def scores(self, source: int, mode: str, rule_context: str) -> np.ndarray:
        if self._score_cache is not None:
            return self._score_cache[(source, mode, rule_context)]
        pre = self.world.combined_pre(source, mode, rule_context, self.variant)
        return self._scores_for_pre(pre)

    def consolidate(self) -> None:
        if self.variant.consolidation_strength > 0.0 and self.variant.consolidation_on_reversal:
            self.consolidated_W = self.W.copy()

    def _pull_toward_consolidated(self) -> None:
        if self.consolidated_W is None:
            return
        s = max(0.0, min(1.0, self.variant.consolidation_strength))
        if s <= 0.0:
            return
        # A small pull after every update makes old routes harder to overwrite.
        pull = np.float32(0.035 * s)
        self.W *= np.float32(1.0 - pull)
        self.W += self.consolidated_W * pull

    def _apply_update(self, source: int, mode: str, rule_context: str, observed_target: int, phase: str) -> None:
        v = self.variant
        self._score_cache = None
        if not v.structural_plasticity:
            return
        if v.reward_gate and observed_target < 0:
            return
        if not (0 <= observed_target <= self.max_number):
            return

        if v.decay > 0:
            self.W *= np.float32(1.0 - v.decay)

        lr_mult = 1.0
        if phase == "reversal":
            lr_mult = v.reversal_learning_rate_multiplier
        elif phase == "switchback":
            lr_mult = v.switchback_learning_rate_multiplier
        if self.consolidated_W is not None and phase in {"reversal", "switchback"}:
            # Consolidation trades plasticity for retention.
            lr_mult *= max(0.08, 1.0 - 0.70 * max(0.0, min(1.0, v.consolidation_strength)))

        pre = self.world.combined_pre(source, mode, rule_context, v)
        target = self.world.number(observed_target)
        delta = np.float32(v.learning_rate * lr_mult / max(1, len(pre)))
        self.W[np.ix_(pre, target)] += delta

        if v.inhibition:
            wrong_units = [self.world.number(n) for n in range(self.max_number + 1) if n != observed_target]
            wrong_union = np.unique(np.concatenate(wrong_units)).astype(np.int32)
            self.W[np.ix_(pre, wrong_union)] -= np.float32(v.inhibition_strength * v.learning_rate * lr_mult / max(1, len(pre)))

            if v.context_binding:
                # Suppress the same target under competing modes and, for dual-context worlds,
                # competing rule contexts.
                # For dual-context worlds, do not punish the inactive world; this is the
                # mechanism that allows A and B to coexist rather than overwrite.
                contexts = (rule_context,)
                for other_rule in contexts:
                    for other_mode in MODE_NAMES:
                        if other_mode == mode and other_rule == rule_context:
                            continue
                        other_pre = self.world.combined_pre(source, other_mode, other_rule, v)
                        self.W[np.ix_(other_pre, target)] -= np.float32(v.wrong_context_inhibition * v.learning_rate * lr_mult / max(1, len(other_pre)))

        if v.noise_std > 0.0:
            self.W[np.ix_(pre, target)] += self.rng.normal(0.0, v.noise_std, size=(len(pre), len(target))).astype(np.float32)

        if v.homeostasis:
            np.clip(self.W, v.clip_min, v.clip_max, out=self.W)

        if phase in {"reversal", "switchback"}:
            self._pull_toward_consolidated()

    def _feedback_target(self, true_target_n: int) -> int:
        v = self.variant
        if v.feedback_noise > 0.0 and self.rng.random() < v.feedback_noise:
            wrong = [n for n in range(self.max_number + 1) if n != true_target_n]
            wrong_target = int(self.rng.choice(wrong))
            return -1 if v.reward_gate else wrong_target
        return true_target_n

    def train_curriculum(self, transition_tasks: Sequence[Task], repeats: int, phase: str) -> None:
        stream = shuffled_repeated(transition_tasks, repeats, self.py_rng)
        delay = max(0, self.variant.reward_delay_steps)
        if delay <= 0:
            for task in stream:
                self._apply_update(task.start, task.mode, task.rule, self._feedback_target(task.target), phase)
            return

        pending: List[Task] = []
        for task in stream:
            pending.append(task)
            if len(pending) > delay:
                original = pending.pop(0)
                observed = self._feedback_target(original.target)
                if self.variant.eligibility_trace:
                    self._apply_update(original.start, original.mode, original.rule, observed, phase)
                else:
                    self._apply_update(task.start, task.mode, task.rule, observed, phase)
        last = stream[-1] if stream else None
        while pending:
            original = pending.pop(0)
            observed = self._feedback_target(original.target)
            if self.variant.eligibility_trace:
                self._apply_update(original.start, original.mode, original.rule, observed, phase)
            elif last is not None:
                self._apply_update(last.start, last.mode, last.rule, observed, phase)

    def target_rank_and_margin(self, source: int, mode: str, rule_context: str, target: int) -> Tuple[int, float, float, float]:
        scores = self.scores(source, mode, rule_context)
        order = np.argsort(scores)[::-1]
        rank = int(np.where(order == target)[0][0]) + 1
        target_score = float(scores[target])
        wrong_scores = np.delete(scores, target)
        best_wrong = float(np.max(wrong_scores)) if wrong_scores.size else -math.inf
        return rank, target_score - best_wrong, target_score, float(np.max(scores))

    def context_margin(self, source: int, mode: str, rule_context: str, target: int) -> float:
        if not self.variant.context_binding:
            return math.nan
        correct = float(self.scores(source, mode, rule_context)[target])
        wrong = []
        contexts = RULE_NAMES if self.variant.dual_context_worlds else (rule_context,)
        for other_rule in contexts:
            for other_mode in MODE_NAMES:
                if other_rule == rule_context and other_mode == mode:
                    continue
                wrong.append(float(self.scores(source, other_mode, other_rule)[target]))
        return correct - max(wrong) if wrong else math.nan

    def wrong_route_activation(self, source: int, mode: str, rule_context: str, target: int) -> float:
        if not self.variant.context_binding:
            return math.nan
        correct = float(self.scores(source, mode, rule_context)[target])
        wrong = []
        contexts = RULE_NAMES if self.variant.dual_context_worlds else (rule_context,)
        for other_rule in contexts:
            for other_mode in MODE_NAMES:
                if other_rule == rule_context and other_mode == mode:
                    continue
                wrong.append(float(self.scores(source, other_mode, other_rule)[target]))
        return float(np.mean([_safe_sigmoid(w - correct) for w in wrong])) if wrong else math.nan

    def predict(self, task: Task) -> PredictionTrace:
        current = task.start
        expected_current = task.start
        step_predictions: List[int] = []
        step_expected: List[int] = []
        ranks: List[int] = []
        margins: List[float] = []
        context_margins: List[float] = []
        wrong_acts: List[float] = []
        failure_type = "none"

        steps_to_run = task.steps if self.variant.recurrence else 1
        for step_i in range(steps_to_run):
            expected_next = self._valid_next(expected_current, task.mode, task.rule)
            if expected_next is None:
                break
            step_expected.append(expected_next)
            scores = self.scores(current, task.mode, task.rule)
            predicted_next = int(np.argmax(scores))
            step_predictions.append(predicted_next)

            local_expected = expected_next if current == expected_current else true_target(current, task.mode, 1, task.rule)
            if not (0 <= local_expected <= self.max_number):
                local_expected = predicted_next
            rank, margin, _, _ = self.target_rank_and_margin(current, task.mode, task.rule, local_expected)
            ranks.append(rank)
            margins.append(margin)
            context_margins.append(self.context_margin(current, task.mode, task.rule, local_expected))
            wrong_acts.append(self.wrong_route_activation(current, task.mode, task.rule, local_expected))

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
        return PredictionTrace(task, predicted, correct, step_predictions, step_expected, ranks, margins, context_margins, wrong_acts, failure_type)

    def route_diagnostics(self, rule: str) -> List[dict]:
        rows: List[dict] = []
        for mode in MODE_NAMES:
            for source in range(self.max_number + 1):
                target = self._valid_next(source, mode, rule)
                if target is None:
                    continue
                scores = self.scores(source, mode, rule)
                predicted = int(np.argmax(scores))
                rank, margin, target_score, best_score = self.target_rank_and_margin(source, mode, rule, target)
                order = np.argsort(scores)[::-1][:5]
                rows.append({
                    "eval_rule": rule,
                    "mode": mode,
                    "source": source,
                    "true_target": target,
                    "predicted_target": predicted,
                    "correct": int(predicted == target),
                    "target_rank": rank,
                    "correct_margin": margin,
                    "context_margin": self.context_margin(source, mode, rule, target),
                    "wrong_route_activation": self.wrong_route_activation(source, mode, rule, target),
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


def route_summary(route_rows: Sequence[dict], prefix: str) -> dict:
    if not route_rows:
        return {}
    return {
        f"{prefix}/route_table_accuracy": float(np.mean([r["correct"] for r in route_rows])),
        f"{prefix}/mean_target_rank": float(np.mean([r["target_rank"] for r in route_rows])),
        f"{prefix}/mean_correct_margin": float(np.mean([r["correct_margin"] for r in route_rows])),
        f"{prefix}/mean_context_margin": _nanmean_or_nan([r["context_margin"] for r in route_rows]),
        f"{prefix}/mean_wrong_route_activation": _nanmean_or_nan([r["wrong_route_activation"] for r in route_rows]),
    }


def failure_counts(traces: Sequence[PredictionTrace], run_name: str, seed: int, phase: str, checkpoint: int, eval_rule: str) -> List[dict]:
    counts: Dict[str, int] = {}
    for t in traces:
        if not t.correct:
            counts[t.failure_type] = counts.get(t.failure_type, 0) + 1
    return [
        {"run_name": run_name, "seed": seed, "phase": phase, "checkpoint": checkpoint, "eval_rule": eval_rule, "failure_type": k, "count": v}
        for k, v in sorted(counts.items())
    ]


def make_reversal_variants(feedback_noise: float = 0.0, reward_delay_steps: int = 0) -> List[VariantConfig]:
    return [
        VariantConfig(name="exp10_full_adaptive_reversal", feedback_noise=feedback_noise, reward_delay_steps=reward_delay_steps, consolidation_strength=0.10, consolidation_on_reversal=True),
        VariantConfig(name="exp10_no_consolidation", feedback_noise=feedback_noise, reward_delay_steps=reward_delay_steps, consolidation_strength=0.0),
        VariantConfig(name="exp10_strong_consolidation", feedback_noise=feedback_noise, reward_delay_steps=reward_delay_steps, consolidation_strength=0.80, consolidation_on_reversal=True),
        VariantConfig(name="exp10_dual_context_worlds", feedback_noise=feedback_noise, reward_delay_steps=reward_delay_steps, dual_context_worlds=True, consolidation_strength=0.0, learning_rate=2.0, inhibition_strength=0.06),
        VariantConfig(name="exp10_no_inhibition", feedback_noise=feedback_noise, reward_delay_steps=reward_delay_steps, inhibition=False, consolidation_strength=0.10, consolidation_on_reversal=True),
        VariantConfig(name="exp10_no_reward_gate", feedback_noise=feedback_noise, reward_delay_steps=reward_delay_steps, reward_gate=False, consolidation_strength=0.10, consolidation_on_reversal=True),
        VariantConfig(name="exp10_no_eligibility_trace", feedback_noise=feedback_noise, reward_delay_steps=reward_delay_steps, eligibility_trace=False, consolidation_strength=0.10, consolidation_on_reversal=True),
        VariantConfig(name="exp10_no_homeostasis", feedback_noise=feedback_noise, reward_delay_steps=reward_delay_steps, homeostasis=False, consolidation_strength=0.10, consolidation_on_reversal=True),
        VariantConfig(name="exp10_no_structural_plasticity", feedback_noise=feedback_noise, reward_delay_steps=reward_delay_steps, structural_plasticity=False),
    ]


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
        "always_rule_A": lambda t: true_target(t.start, t.mode, t.steps, "A"),
        "always_rule_B": lambda t: true_target(t.start, t.mode, t.steps, "B"),
        "lookup_oracle": lambda t: t.target,
        "random_uniform": lambda t: rng.randint(0, max_number),
    }
    for name, fn in strategies.items():
        correct = 0
        for t in tasks:
            pred = fn(t)
            correct += int(pred == t.target)
        rows.append({"baseline": name, "accuracy": correct / len(tasks), "n": len(tasks)})
    return rows
