from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Dict

import numpy as np

from .config import ExperimentConfig
from .modulators import ModulationSignal

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GraphStepResult:
    active_indices: np.ndarray
    active_values: np.ndarray
    logits: np.ndarray
    probabilities: np.ndarray
    prediction: int


class SparseInputProjection:
    """Sparse input-to-hidden synapses.

    For hidden neuron h, `input_indices[h]` gives the input pixels it listens to,
    and `weights[h]` gives plastic weights for those local synapses.
    """

    def __init__(self, input_indices: np.ndarray, weights: np.ndarray):
        if input_indices.shape != weights.shape:
            raise ValueError("input_indices and weights must have the same shape")
        self.input_indices = input_indices.astype(np.int32, copy=False)
        self.weights = weights.astype(np.float32, copy=False)

    @classmethod
    def random(cls, rng: np.random.Generator, hidden_units: int, input_dim: int, edges_per_hidden: int) -> "SparseInputProjection":
        indices = np.empty((hidden_units, edges_per_hidden), dtype=np.int32)
        for h in range(hidden_units):
            indices[h] = rng.choice(input_dim, size=edges_per_hidden, replace=False)
        weights = rng.normal(loc=0.0, scale=0.15, size=(hidden_units, edges_per_hidden)).astype(np.float32)
        return cls(indices, weights)

    def compute_drive(self, x: np.ndarray) -> np.ndarray:
        gathered = x[self.input_indices]
        return np.sum(gathered * self.weights, axis=1, dtype=np.float32)

    def plastic_update(
        self,
        x: np.ndarray,
        active_indices: np.ndarray,
        active_values: np.ndarray,
        credit: np.ndarray,
        learning_rate: float,
        gate: float,
    ) -> None:
        if active_indices.size == 0:
            return
        local_inputs = x[self.input_indices[active_indices]]
        # Oja-ish bounded Hebbian update: move local synapse weights toward useful input pattern.
        delta = learning_rate * gate * credit[:, None] * active_values[:, None] * (local_inputs - self.weights[active_indices])
        self.weights[active_indices] += delta.astype(np.float32)
        np.clip(self.weights[active_indices], -2.5, 2.5, out=self.weights[active_indices])


class HiddenPopulation:
    """Stateful hidden units with thresholds, traces, and sparse activation."""

    def __init__(self, thresholds: np.ndarray, traces: np.ndarray, excitability: np.ndarray, config: ExperimentConfig):
        self.thresholds = thresholds.astype(np.float32, copy=False)
        self.traces = traces.astype(np.float32, copy=False)
        self.excitability = excitability.astype(np.float32, copy=False)
        self.config = config

    @classmethod
    def create(cls, hidden_units: int, config: ExperimentConfig) -> "HiddenPopulation":
        thresholds = np.zeros(hidden_units, dtype=np.float32)
        traces = np.zeros(hidden_units, dtype=np.float32)
        excitability = np.ones(hidden_units, dtype=np.float32)
        return cls(thresholds=thresholds, traces=traces, excitability=excitability, config=config)

    def activate(self, drive: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        adjusted = (drive * self.excitability - self.thresholds) / self.config.activation_temperature
        k = min(self.config.active_hidden, adjusted.shape[0])
        active = np.argpartition(adjusted, -k)[-k:]
        # Sort descending for deterministic-ish traces and easier inspection.
        active = active[np.argsort(adjusted[active])[::-1]]
        values = self._sigmoid(adjusted[active]).astype(np.float32)
        return active.astype(np.int32), values

    def update_traces_and_homeostasis(self, active_indices: np.ndarray, active_values: np.ndarray) -> None:
        self.traces *= self.config.trace_decay
        self.traces[active_indices] += active_values

        observed_rate = active_indices.size / self.thresholds.size
        # Active neurons become slightly harder to trigger; inactive population drifts down a little.
        self.thresholds[active_indices] += self.config.threshold_lr * (observed_rate - self.config.target_activation_rate + active_values)
        self.thresholds -= self.config.threshold_lr * self.config.target_activation_rate / 10.0
        np.clip(self.thresholds, -3.0, 3.0, out=self.thresholds)

    @staticmethod
    def _sigmoid(x: np.ndarray) -> np.ndarray:
        return 1.0 / (1.0 + np.exp(-np.clip(x, -30.0, 30.0)))


class OutputReadout:
    """Plastic hidden-to-output synapses."""

    def __init__(self, weights: np.ndarray):
        self.weights = weights.astype(np.float32, copy=False)

    @classmethod
    def random(cls, rng: np.random.Generator, hidden_units: int, output_dim: int) -> "OutputReadout":
        weights = rng.normal(loc=0.0, scale=0.03, size=(hidden_units, output_dim)).astype(np.float32)
        return cls(weights)

    def logits(self, active_indices: np.ndarray, active_values: np.ndarray) -> np.ndarray:
        logits = active_values @ self.weights[active_indices]
        return logits.astype(np.float32)

    def plastic_update(
        self,
        active_indices: np.ndarray,
        active_values: np.ndarray,
        error: np.ndarray,
        learning_rate: float,
        reward: float,
        gate: float,
        weight_decay: float,
    ) -> np.ndarray:
        # Credit per active hidden unit before update; used to update input synapses.
        credit = self.weights[active_indices] @ error
        delta = learning_rate * gate * active_values[:, None] * error[None, :]
        self.weights[active_indices] += delta.astype(np.float32)
        if weight_decay > 0:
            self.weights[active_indices] *= np.float32(1.0 - weight_decay)
        np.clip(self.weights[active_indices], -4.0, 4.0, out=self.weights[active_indices])
        # Reward sign modulates whether the upstream feature synapses should be encouraged or discouraged.
        return (reward * credit).astype(np.float32)


class PlasticGraphNetwork:
    """A sparse, persistent, reward-modulated graph substrate.

    This is not a standard backprop MLP. It uses:
      - sparse input-to-hidden synapses
      - top-k active hidden population
      - hidden-to-output plastic readout
      - reward-gated local updates
      - neuron traces and threshold homeostasis
    """

    def __init__(
        self,
        input_projection: SparseInputProjection,
        hidden: HiddenPopulation,
        output: OutputReadout,
        config: ExperimentConfig,
    ):
        self.input_projection = input_projection
        self.hidden = hidden
        self.output = output
        self.config = config

    @classmethod
    def create(cls, config: ExperimentConfig) -> "PlasticGraphNetwork":
        rng = np.random.default_rng(config.seed)
        input_projection = SparseInputProjection.random(
            rng=rng,
            hidden_units=config.hidden_units,
            input_dim=config.input_dim,
            edges_per_hidden=config.input_edges_per_hidden,
        )
        hidden = HiddenPopulation.create(config.hidden_units, config)
        output = OutputReadout.random(rng, config.hidden_units, config.output_dim)
        logger.info(
            "Initialized plastic graph: hidden=%s input_edges/hidden=%s active_hidden=%s",
            config.hidden_units,
            config.input_edges_per_hidden,
            config.active_hidden,
        )
        return cls(input_projection, hidden, output, config)

    def forward(self, x: np.ndarray) -> GraphStepResult:
        drive = self.input_projection.compute_drive(x)
        active_indices, active_values = self.hidden.activate(drive)
        logits = self.output.logits(active_indices, active_values)
        probabilities = self._softmax(logits)
        prediction = int(np.argmax(probabilities))
        return GraphStepResult(
            active_indices=active_indices,
            active_values=active_values,
            logits=logits,
            probabilities=probabilities,
            prediction=prediction,
        )

    def learn(self, x: np.ndarray, target: int, result: GraphStepResult, modulation: ModulationSignal) -> None:
        target_vec = np.zeros(self.config.output_dim, dtype=np.float32)
        target_vec[target] = 1.0
        error = target_vec - result.probabilities

        hidden_credit = self.output.plastic_update(
            active_indices=result.active_indices,
            active_values=result.active_values,
            error=error,
            learning_rate=self.config.learning_rate_hidden_output,
            reward=modulation.reward,
            gate=modulation.plasticity_gate,
            weight_decay=self.config.weight_decay,
        )

        self.input_projection.plastic_update(
            x=x,
            active_indices=result.active_indices,
            active_values=result.active_values,
            credit=hidden_credit,
            learning_rate=self.config.learning_rate_input_hidden,
            gate=modulation.plasticity_gate,
        )

        self.hidden.update_traces_and_homeostasis(result.active_indices, result.active_values)

    def checkpoint_arrays(self) -> Dict[str, np.ndarray]:
        return {
            "input_indices": self.input_projection.input_indices,
            "input_weights": self.input_projection.weights,
            "hidden_thresholds": self.hidden.thresholds,
            "hidden_traces": self.hidden.traces,
            "hidden_excitability": self.hidden.excitability,
            "output_weights": self.output.weights,
        }

    @staticmethod
    def _softmax(logits: np.ndarray) -> np.ndarray:
        shifted = logits - np.max(logits)
        exp = np.exp(shifted)
        return (exp / np.sum(exp)).astype(np.float32)
