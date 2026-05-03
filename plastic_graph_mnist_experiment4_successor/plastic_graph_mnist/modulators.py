from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ModulationSignal:
    reward: float
    plasticity_gate: float
    confidence: float
    novelty: float
    correct: bool


class RewardModulator:
    """Converts task feedback into a biological-ish plasticity gate.

    This is an artificial analogue of reward/salience/uncertainty systems. It does
    not make the graph 'feel' anything; it controls how much an event should update
    durable pathways.
    """

    def __init__(self, min_gate: float = 0.05, max_gate: float = 1.0, negative_reward_scale: float = 0.35):
        self.min_gate = min_gate
        self.max_gate = max_gate
        self.negative_reward_scale = negative_reward_scale

    def evaluate(self, probabilities: np.ndarray, target: int) -> ModulationSignal:
        prediction = int(np.argmax(probabilities))
        correct = prediction == target
        confidence = float(np.max(probabilities))
        entropy = float(-(probabilities * np.log(probabilities + 1e-8)).sum())
        max_entropy = float(np.log(len(probabilities)))
        novelty = entropy / max_entropy

        if correct:
            reward = 1.0
        else:
            reward = -self.negative_reward_scale

        # High novelty/uncertainty should keep plasticity open. Very confident wrong
        # answers still receive a non-trivial negative update via reward.
        raw_gate = 0.35 + 0.65 * novelty
        plasticity_gate = float(np.clip(raw_gate, self.min_gate, self.max_gate))

        return ModulationSignal(
            reward=reward,
            plasticity_gate=plasticity_gate,
            confidence=confidence,
            novelty=novelty,
            correct=correct,
        )
