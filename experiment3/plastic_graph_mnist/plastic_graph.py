from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Dict, List

import numpy as np

from .config import ExperimentConfig
from .modulators import ModulationSignal

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GraphStepResult:
    """One sparse graph traversal result.

    `active_indices` and `active_values` are the final active population used by
    the readout. `path_indices` and `path_values` include each recurrent step and
    become the biological-style eligibility trace for recurrent plasticity.
    """

    active_indices: np.ndarray
    active_values: np.ndarray
    logits: np.ndarray
    probabilities: np.ndarray
    prediction: int
    path_indices: List[np.ndarray] = field(default_factory=list)
    path_values: List[np.ndarray] = field(default_factory=list)
    unique_active_count: int = 0
    recurrent_drive_norm: float = 0.0


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
        if active_indices.size == 0 or learning_rate <= 0 or gate <= 0:
            return
        local_inputs = x[self.input_indices[active_indices]]
        # Bounded Hebbian/Oja-ish update: move local synapse weights toward useful input pattern.
        delta = learning_rate * gate * credit[:, None] * active_values[:, None] * (local_inputs - self.weights[active_indices])
        self.weights[active_indices] += delta.astype(np.float32)
        np.clip(self.weights[active_indices], -2.5, 2.5, out=self.weights[active_indices])


class SparseRecurrentProjection:
    """Sparse hidden-to-hidden synapses for short recurrent graph traversals.

    This is the key next-step experiment. The model no longer performs a single
    random-feature activation. It can propagate activity through a sparse hidden
    graph for a small number of steps, then reward-modulated plasticity reinforces
    or weakens the active transitions.
    """

    def __init__(self, target_indices: np.ndarray, weights: np.ndarray):
        if target_indices.shape != weights.shape:
            raise ValueError("target_indices and weights must have the same shape")
        self.target_indices = target_indices.astype(np.int32, copy=False)
        self.weights = weights.astype(np.float32, copy=False)

    @classmethod
    def random(
        cls,
        rng: np.random.Generator,
        hidden_units: int,
        edges_per_hidden: int,
        weight_scale: float,
    ) -> "SparseRecurrentProjection":
        targets = np.empty((hidden_units, edges_per_hidden), dtype=np.int32)
        for h in range(hidden_units):
            # Avoid self-loops initially. They can emerge conceptually through repeated recruitment,
            # but explicit self-loops make early dynamics less interpretable.
            choices = rng.choice(hidden_units - 1, size=edges_per_hidden, replace=False)
            targets[h] = np.where(choices >= h, choices + 1, choices)
        weights = rng.normal(loc=0.0, scale=weight_scale, size=(hidden_units, edges_per_hidden)).astype(np.float32)
        return cls(targets, weights)

    def compute_recurrent_drive(self, hidden_units: int, source_indices: np.ndarray, source_values: np.ndarray) -> np.ndarray:
        drive = np.zeros(hidden_units, dtype=np.float32)
        if source_indices.size == 0:
            return drive
        targets = self.target_indices[source_indices]
        contributions = source_values[:, None] * self.weights[source_indices]
        np.add.at(drive, targets.ravel(), contributions.ravel())
        return drive

    def plastic_update(
        self,
        path_indices: List[np.ndarray],
        path_values: List[np.ndarray],
        reward: float,
        learning_rate: float,
        gate: float,
        decay: float,
    ) -> None:
        if learning_rate <= 0 or gate <= 0 or len(path_indices) < 2:
            return

        effective_reward = np.float32(reward * gate)
        if effective_reward == 0:
            return

        for step in range(len(path_indices) - 1):
            src = path_indices[step]
            src_values = path_values[step]
            dst = path_indices[step + 1]
            dst_values = path_values[step + 1]
            if src.size == 0 or dst.size == 0:
                continue

            dst_value_map = {int(i): float(v) for i, v in zip(dst, dst_values)}
            targets = self.target_indices[src]
            target_values = np.zeros_like(targets, dtype=np.float32)
            # The active destination population becomes an eligibility mask.
            # For now this loop is intentionally explicit and inspectable; optimize later.
            for row in range(targets.shape[0]):
                for col in range(targets.shape[1]):
                    target_values[row, col] = dst_value_map.get(int(targets[row, col]), 0.0)

            eligibility = src_values[:, None] * target_values
            delta = learning_rate * effective_reward * eligibility
            self.weights[src] += delta.astype(np.float32)
            if decay > 0:
                self.weights[src] *= np.float32(1.0 - decay)
            np.clip(self.weights[src], -1.5, 1.5, out=self.weights[src])


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
        threshold_term = self.thresholds if self.config.use_thresholds else 0.0
        adjusted = (drive * self.excitability - threshold_term) / self.config.activation_temperature
        k = min(self.config.active_hidden, adjusted.shape[0])
        active = np.argpartition(adjusted, -k)[-k:]
        active = active[np.argsort(adjusted[active])[::-1]]
        values = self._sigmoid(adjusted[active]).astype(np.float32)
        return active.astype(np.int32), values

    def update_traces_and_homeostasis(self, path_indices: List[np.ndarray], path_values: List[np.ndarray]) -> None:
        if self.config.use_traces:
            self.traces *= self.config.trace_decay
            for active_indices, active_values in zip(path_indices, path_values):
                self.traces[active_indices] += active_values / max(len(path_indices), 1)

        if not self.config.use_thresholds:
            return

        # Active neurons become slightly harder to trigger; inactive population drifts down a little.
        # This keeps a small winner-take-active-set from monopolizing all traversals.
        if not path_indices:
            return
        all_active = np.unique(np.concatenate(path_indices))
        observed_rate = all_active.size / self.thresholds.size
        self.thresholds[all_active] += self.config.threshold_lr * (observed_rate - self.config.target_activation_rate + 0.25)
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
        credit = self.weights[active_indices] @ error
        delta = learning_rate * gate * active_values[:, None] * error[None, :]
        self.weights[active_indices] += delta.astype(np.float32)
        if weight_decay > 0:
            self.weights[active_indices] *= np.float32(1.0 - weight_decay)
        np.clip(self.weights[active_indices], -4.0, 4.0, out=self.weights[active_indices])
        return (reward * credit).astype(np.float32)


class PlasticGraphNetwork:
    """A sparse, persistent, reward-modulated graph substrate.

    Compared with the previous prototype, this version adds recurrent hidden-to-hidden
    graph traversal and recurrent eligibility updates. It remains intentionally simple:
    this is an experiment framework, not a state-of-the-art MNIST classifier.
    """

    def __init__(
        self,
        input_projection: SparseInputProjection,
        hidden: HiddenPopulation,
        output: OutputReadout,
        config: ExperimentConfig,
        recurrent_projection: SparseRecurrentProjection | None = None,
    ):
        self.input_projection = input_projection
        self.hidden = hidden
        self.output = output
        self.config = config
        self.recurrent_projection = recurrent_projection

    @classmethod
    def create(cls, config: ExperimentConfig) -> "PlasticGraphNetwork":
        rng = np.random.default_rng(config.seed)
        input_projection = SparseInputProjection.random(
            rng=rng,
            hidden_units=config.hidden_units,
            input_dim=config.input_dim,
            edges_per_hidden=config.input_edges_per_hidden,
        )
        recurrent_projection = None
        if config.use_recurrence and config.hidden_recurrent_edges_per_hidden > 0 and config.recurrent_steps > 0:
            recurrent_projection = SparseRecurrentProjection.random(
                rng=rng,
                hidden_units=config.hidden_units,
                edges_per_hidden=config.hidden_recurrent_edges_per_hidden,
                weight_scale=config.recurrent_weight_scale,
            )
        hidden = HiddenPopulation.create(config.hidden_units, config)
        output = OutputReadout.random(rng, config.hidden_units, config.output_dim)
        logger.info(
            "Initialized plastic graph: hidden=%s input_edges/hidden=%s active_hidden=%s recurrence=%s recurrent_edges/hidden=%s recurrent_steps=%s",
            config.hidden_units,
            config.input_edges_per_hidden,
            config.active_hidden,
            bool(recurrent_projection),
            config.hidden_recurrent_edges_per_hidden,
            config.recurrent_steps,
        )
        return cls(input_projection, hidden, output, config, recurrent_projection)

    def forward(self, x: np.ndarray) -> GraphStepResult:
        input_drive = self.input_projection.compute_drive(x)
        path_indices: List[np.ndarray] = []
        path_values: List[np.ndarray] = []
        recurrent_drive_norm = 0.0

        active_indices, active_values = self.hidden.activate(input_drive)
        path_indices.append(active_indices)
        path_values.append(active_values)

        if self.recurrent_projection is not None:
            for _ in range(self.config.recurrent_steps):
                recurrent_drive = self.recurrent_projection.compute_recurrent_drive(
                    hidden_units=self.config.hidden_units,
                    source_indices=active_indices,
                    source_values=active_values,
                )
                recurrent_drive_norm += float(np.linalg.norm(recurrent_drive))
                total_drive = input_drive + self.config.recurrent_mix * recurrent_drive
                active_indices, active_values = self.hidden.activate(total_drive)
                path_indices.append(active_indices)
                path_values.append(active_values)

        logits = self.output.logits(active_indices, active_values)
        probabilities = self._softmax(logits)
        prediction = int(np.argmax(probabilities))
        unique_active_count = int(np.unique(np.concatenate(path_indices)).size)
        return GraphStepResult(
            active_indices=active_indices,
            active_values=active_values,
            logits=logits,
            probabilities=probabilities,
            prediction=prediction,
            path_indices=path_indices,
            path_values=path_values,
            unique_active_count=unique_active_count,
            recurrent_drive_norm=recurrent_drive_norm,
        )

    def learn(self, x: np.ndarray, target: int, result: GraphStepResult, modulation: ModulationSignal) -> None:
        target_vec = np.zeros(self.config.output_dim, dtype=np.float32)
        target_vec[target] = 1.0
        error = target_vec - result.probabilities

        gate = modulation.plasticity_gate if self.config.use_reward_modulation else 1.0
        reward = modulation.reward if self.config.use_reward_modulation else (1.0 if modulation.correct else -self.config.negative_reward_scale)

        hidden_credit = self.output.plastic_update(
            active_indices=result.active_indices,
            active_values=result.active_values,
            error=error,
            learning_rate=self.config.learning_rate_hidden_output,
            reward=reward,
            gate=gate,
            weight_decay=self.config.weight_decay,
        )

        if self.config.use_input_plasticity:
            self.input_projection.plastic_update(
                x=x,
                active_indices=result.active_indices,
                active_values=result.active_values,
                credit=hidden_credit,
                learning_rate=self.config.learning_rate_input_hidden,
                gate=gate,
            )

        if self.recurrent_projection is not None:
            self.recurrent_projection.plastic_update(
                path_indices=result.path_indices,
                path_values=result.path_values,
                reward=reward,
                learning_rate=self.config.recurrent_lr,
                gate=gate,
                decay=self.config.recurrent_decay,
            )

        self.hidden.update_traces_and_homeostasis(result.path_indices, result.path_values)

    def checkpoint_arrays(self) -> Dict[str, np.ndarray]:
        arrays: Dict[str, np.ndarray] = {
            "input_indices": self.input_projection.input_indices,
            "input_weights": self.input_projection.weights,
            "hidden_thresholds": self.hidden.thresholds,
            "hidden_traces": self.hidden.traces,
            "hidden_excitability": self.hidden.excitability,
            "output_weights": self.output.weights,
        }
        if self.recurrent_projection is not None:
            arrays["recurrent_targets"] = self.recurrent_projection.target_indices
            arrays["recurrent_weights"] = self.recurrent_projection.weights
        return arrays

    @staticmethod
    def _softmax(logits: np.ndarray) -> np.ndarray:
        shifted = logits - np.max(logits)
        exp = np.exp(shifted)
        return (exp / np.sum(exp)).astype(np.float32)
