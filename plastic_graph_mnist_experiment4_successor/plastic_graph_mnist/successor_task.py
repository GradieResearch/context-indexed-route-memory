from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Tuple

import numpy as np


@dataclass(frozen=True)
class SuccessorTaskConfig:
    """Configuration for the Experiment 4 symbolic traversal task.

    The task is intentionally tiny and inspectable. The model is not trained on
    addition examples directly. It learns the local transition n -> n + 1 and is
    then evaluated on whether it can compose that transition b times to solve
    a + b.
    """

    max_number: int = 24
    max_addend: int = 5
    train_transition_repeats: int = 120
    seed: int = 42


@dataclass(frozen=True)
class TransitionExample:
    source: int
    target: int


@dataclass(frozen=True)
class AdditionExample:
    start: int
    steps: int
    target: int


class SuccessorTask:
    """Produces local successor and compositional addition examples."""

    def __init__(self, config: SuccessorTaskConfig):
        if config.max_addend < 1:
            raise ValueError("max_addend must be >= 1")
        if config.max_number <= config.max_addend + 1:
            raise ValueError("max_number must be larger than max_addend + 1")
        self.config = config
        self.rng = np.random.default_rng(config.seed)

    def transition_examples(self) -> List[TransitionExample]:
        base = [TransitionExample(n, n + 1) for n in range(self.config.max_number)]
        repeated = base * self.config.train_transition_repeats
        self.rng.shuffle(repeated)
        return repeated

    def addition_examples(self) -> List[AdditionExample]:
        examples: list[AdditionExample] = []
        for start in range(self.config.max_number + 1):
            for steps in range(self.config.max_addend + 1):
                target = start + steps
                if target <= self.config.max_number:
                    examples.append(AdditionExample(start, steps, target))
        return examples

    def heldout_long_addition_examples(self) -> List[AdditionExample]:
        """Compositional tests requiring at least 2 transitions."""
        return [ex for ex in self.addition_examples() if ex.steps >= 2]
