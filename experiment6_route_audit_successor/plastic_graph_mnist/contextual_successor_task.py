from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Tuple

import numpy as np


MODE_DELTAS_PHASE_0 = {
    "plus_one": 1,
    "plus_two": 2,
    "minus_one": -1,
}

MODE_DELTAS_PHASE_1 = {
    "plus_one": 2,
    "plus_two": 1,
    "minus_one": -2,
}


@dataclass(frozen=True)
class ContextualSuccessorTaskConfig:
    """Configuration for Experiment 6's route-audited contextual traversal world."""

    max_number: int = 24
    max_steps: int = 5
    train_sequence_repeats: int = 120
    training_max_steps: int = 2
    modes: Tuple[str, ...] = ("plus_one", "plus_two", "minus_one")
    feedback_noise: float = 0.0
    delayed_reward: bool = False
    rule_reversal: bool = False
    reversal_fraction: float = 0.5
    seed: int = 42


@dataclass(frozen=True)
class ContextualSequenceExample:
    mode: str
    start: int
    steps: int
    target: int
    phase: int
    path: Tuple[int, ...]


class ContextualSuccessorTask:
    """Produces context-sensitive traversal examples and optional rule changes."""

    def __init__(self, config: ContextualSuccessorTaskConfig):
        if config.max_steps < 1:
            raise ValueError("max_steps must be >= 1")
        if config.training_max_steps < 1:
            raise ValueError("training_max_steps must be >= 1")
        if not 0.0 <= config.feedback_noise <= 0.5:
            raise ValueError("feedback_noise must be between 0.0 and 0.5")
        if config.rule_reversal and not 0.0 < config.reversal_fraction < 1.0:
            raise ValueError("reversal_fraction must be between 0 and 1 when rule_reversal is enabled")
        unknown = [mode for mode in config.modes if mode not in MODE_DELTAS_PHASE_0]
        if unknown:
            raise ValueError(f"Unsupported modes: {unknown}")
        self.config = config
        self.rng = np.random.default_rng(config.seed)

    @property
    def mode_names(self) -> Tuple[str, ...]:
        return self.config.modes

    def phase_delta(self, mode: str, phase: int) -> int:
        if phase <= 0:
            return MODE_DELTAS_PHASE_0[mode]
        return MODE_DELTAS_PHASE_1[mode]

    def transition(self, mode: str, value: int, phase: int) -> int | None:
        target = value + self.phase_delta(mode, phase)
        if 0 <= target <= self.config.max_number:
            return target
        return None

    def rollout(self, mode: str, start: int, steps: int, phase: int) -> Tuple[int, ...] | None:
        path = [start]
        current = start
        for _ in range(steps):
            nxt = self.transition(mode, current, phase)
            if nxt is None:
                return None
            path.append(nxt)
            current = nxt
        return tuple(path)

    def make_example(self, mode: str, start: int, steps: int, phase: int) -> ContextualSequenceExample | None:
        path = self.rollout(mode, start, steps, phase)
        if path is None:
            return None
        return ContextualSequenceExample(
            mode=mode,
            start=start,
            steps=steps,
            target=path[-1],
            phase=phase,
            path=path,
        )

    def training_examples(self) -> List[ContextualSequenceExample]:
        base: list[ContextualSequenceExample] = []
        for mode in self.config.modes:
            for start in range(self.config.max_number + 1):
                for steps in range(1, self.config.training_max_steps + 1):
                    example = self.make_example(mode, start, steps, phase=0)
                    if example is not None:
                        base.append(example)
        examples: list[ContextualSequenceExample] = []
        if not self.config.rule_reversal:
            examples = base * self.config.train_sequence_repeats
            self.rng.shuffle(examples)
            return examples

        before_repeats = max(1, int(round(self.config.train_sequence_repeats * self.config.reversal_fraction)))
        after_repeats = max(1, self.config.train_sequence_repeats - before_repeats)
        before = list(base) * before_repeats
        after: list[ContextualSequenceExample] = []
        for mode in self.config.modes:
            for start in range(self.config.max_number + 1):
                for steps in range(1, self.config.training_max_steps + 1):
                    example = self.make_example(mode, start, steps, phase=1)
                    if example is not None:
                        after.append(example)
        after = after * after_repeats
        self.rng.shuffle(before)
        self.rng.shuffle(after)
        return before + after

    def evaluation_examples(self, phase: int, min_steps: int = 1) -> List[ContextualSequenceExample]:
        examples: list[ContextualSequenceExample] = []
        for mode in self.config.modes:
            for start in range(self.config.max_number + 1):
                for steps in range(min_steps, self.config.max_steps + 1):
                    example = self.make_example(mode, start, steps, phase=phase)
                    if example is not None:
                        examples.append(example)
        return examples

    def best_competing_target(self, mode: str, start: int, steps: int, phase: int) -> tuple[str, int] | None:
        candidates: list[tuple[str, int]] = []
        for other_mode in self.config.modes:
            if other_mode == mode:
                continue
            path = self.rollout(other_mode, start, steps, phase)
            if path is not None:
                candidates.append((other_mode, path[-1]))
        if not candidates:
            return None
        return candidates[0]
