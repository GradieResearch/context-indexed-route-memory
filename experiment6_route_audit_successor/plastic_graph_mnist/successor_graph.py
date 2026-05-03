from __future__ import annotations

import logging
from dataclasses import asdict, dataclass
from typing import Dict, Iterable, Tuple

import numpy as np

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class SuccessorGraphConfig:
    """Sparse assembly graph used for Experiment 4.

    The model represents each number as a sparse distributed assembly of hidden
    units. It learns directed recurrent edges between assemblies using a local
    reward-gated Hebbian rule. Addition is evaluated by repeatedly traversing
    the learned successor graph.
    """

    num_concepts: int = 25
    hidden_units: int = 4096
    assembly_size: int = 96
    active_units: int = 96
    recurrent_edges_per_unit: int = 48
    learning_rate: float = 0.08
    negative_learning_rate: float = 0.02
    structural_replacements_per_update: int = 8
    weight_decay: float = 0.0001
    homeostasis_strength: float = 0.02
    use_recurrence: bool = True
    use_structural_plasticity: bool = True
    use_homeostasis: bool = True
    use_reward_gate: bool = True
    seed: int = 42


@dataclass(frozen=True)
class TraversalResult:
    predicted: int
    confidence: float
    active_units: int
    unique_active_units: int
    recurrent_drive_norm: float
    overlap_with_target: float | None = None


class ConceptAssemblyBook:
    """Maps symbolic concepts to sparse hidden-unit assemblies."""

    def __init__(self, num_concepts: int, hidden_units: int, assembly_size: int, rng: np.random.Generator):
        if assembly_size > hidden_units:
            raise ValueError("assembly_size cannot exceed hidden_units")
        self.num_concepts = num_concepts
        self.hidden_units = hidden_units
        self.assembly_size = assembly_size
        self._assemblies = np.zeros((num_concepts, assembly_size), dtype=np.int32)
        for concept in range(num_concepts):
            self._assemblies[concept] = np.sort(rng.choice(hidden_units, size=assembly_size, replace=False))

    def assembly(self, concept: int) -> np.ndarray:
        return self._assemblies[concept]

    def decode(self, active: np.ndarray) -> Tuple[int, float, np.ndarray]:
        active_set = set(int(x) for x in active)
        overlaps = np.zeros(self.num_concepts, dtype=np.float32)
        for concept in range(self.num_concepts):
            overlaps[concept] = sum(1 for unit in self._assemblies[concept] if int(unit) in active_set) / self.assembly_size
        predicted = int(np.argmax(overlaps))
        confidence = float(overlaps[predicted])
        return predicted, confidence, overlaps

    def arrays(self) -> Dict[str, np.ndarray]:
        return {"concept_assemblies": self._assemblies.copy()}


class SparseRecurrentAssemblyGraph:
    """Persistent sparse graph with local recurrent structural plasticity.

    This is intentionally not a backprop-trained neural network. It is a small
    experimental substrate for testing whether repeated local successor feedback
    can create a traversable recurrent graph.
    """

    def __init__(self, config: SuccessorGraphConfig):
        self.config = config
        self.rng = np.random.default_rng(config.seed)
        self.book = ConceptAssemblyBook(
            num_concepts=config.num_concepts,
            hidden_units=config.hidden_units,
            assembly_size=config.assembly_size,
            rng=self.rng,
        )
        self.edge_targets = self.rng.integers(
            0,
            config.hidden_units,
            size=(config.hidden_units, config.recurrent_edges_per_unit),
            dtype=np.int32,
        )
        self.edge_weights = self.rng.normal(
            loc=0.0,
            scale=0.02,
            size=(config.hidden_units, config.recurrent_edges_per_unit),
        ).astype(np.float32)
        self.thresholds = np.zeros(config.hidden_units, dtype=np.float32)
        self.usage = np.zeros(config.hidden_units, dtype=np.float32)

    def activate_concept(self, concept: int) -> np.ndarray:
        return self.book.assembly(concept).copy()

    def step(self, active: np.ndarray) -> Tuple[np.ndarray, float]:
        if not self.config.use_recurrence:
            return active.copy(), 0.0

        drive = np.zeros(self.config.hidden_units, dtype=np.float32)
        for source in active:
            targets = self.edge_targets[source]
            weights = self.edge_weights[source]
            np.add.at(drive, targets, weights)

        if self.config.use_homeostasis:
            drive = drive - self.thresholds

        recurrent_drive_norm = float(np.linalg.norm(drive))
        if self.config.active_units >= self.config.hidden_units:
            next_active = np.argsort(drive)[::-1].astype(np.int32)
        else:
            top = np.argpartition(drive, -self.config.active_units)[-self.config.active_units:]
            next_active = top[np.argsort(drive[top])[::-1]].astype(np.int32)
        return next_active, recurrent_drive_norm

    def traverse(self, start_concept: int, steps: int, target: int | None = None) -> TraversalResult:
        active = self.activate_concept(start_concept)
        seen = set(int(x) for x in active)
        total_drive = 0.0
        for _ in range(steps):
            active, drive = self.step(active)
            total_drive += drive
            seen.update(int(x) for x in active)

        predicted, confidence, overlaps = self.book.decode(active)
        target_overlap = None if target is None else float(overlaps[target])
        return TraversalResult(
            predicted=predicted,
            confidence=confidence,
            active_units=int(len(active)),
            unique_active_units=int(len(seen)),
            recurrent_drive_norm=total_drive / max(1, steps),
            overlap_with_target=target_overlap,
        )

    def train_transition(self, source_concept: int, target_concept: int) -> Dict[str, float]:
        source_active = self.activate_concept(source_concept)
        target_active = self.book.assembly(target_concept)
        before = self.traverse(source_concept, 1, target_concept)
        reward = 1.0 if before.predicted == target_concept else -1.0
        if not self.config.use_reward_gate:
            reward = 1.0

        # Local Hebbian update: active source units strengthen edges that land in
        # the next concept assembly. Incorrect traversals also weaken the most
        # active predicted assembly, giving the graph a way to unlearn detours.
        target_set = set(int(x) for x in target_active)
        predicted_set = set(int(x) for x in self.book.assembly(before.predicted))
        replacements = 0
        potentiated = 0
        depressed = 0

        for source in source_active:
            targets = self.edge_targets[source]
            weights = self.edge_weights[source]
            hit_mask = np.array([int(t) in target_set for t in targets], dtype=bool)
            if hit_mask.any():
                weights[hit_mask] += self.config.learning_rate * max(reward, 0.0)
                potentiated += int(hit_mask.sum())

            if reward < 0.0:
                bad_mask = np.array([int(t) in predicted_set for t in targets], dtype=bool)
                if bad_mask.any():
                    weights[bad_mask] -= self.config.negative_learning_rate
                    depressed += int(bad_mask.sum())

            if self.config.use_structural_plasticity:
                missing_slots = min(self.config.structural_replacements_per_update, len(weights))
                weakest = np.argpartition(weights, missing_slots - 1)[:missing_slots]
                new_targets = self.rng.choice(target_active, size=missing_slots, replace=True)
                targets[weakest] = new_targets.astype(np.int32)
                weights[weakest] = np.maximum(weights[weakest], 0.0) + self.config.learning_rate * 0.5
                replacements += int(missing_slots)

        self.edge_weights *= (1.0 - self.config.weight_decay)
        np.clip(self.edge_weights, -1.0, 2.0, out=self.edge_weights)

        if self.config.use_homeostasis:
            self.usage *= 0.995
            self.usage[source_active] += 1.0
            self.thresholds += self.config.homeostasis_strength * (self.usage - self.usage.mean()) / (self.usage.std() + 1e-6)
            np.clip(self.thresholds, -2.0, 2.0, out=self.thresholds)

        after = self.traverse(source_concept, 1, target_concept)
        return {
            "before_correct": float(before.predicted == target_concept),
            "after_correct": float(after.predicted == target_concept),
            "before_confidence": before.confidence,
            "after_confidence": after.confidence,
            "reward": float(reward),
            "potentiated_edges": float(potentiated),
            "depressed_edges": float(depressed),
            "structural_replacements": float(replacements),
        }

    def arrays(self) -> Dict[str, np.ndarray]:
        arrays = {
            "edge_targets": self.edge_targets.copy(),
            "edge_weights": self.edge_weights.copy(),
            "thresholds": self.thresholds.copy(),
            "usage": self.usage.copy(),
        }
        arrays.update(self.book.arrays())
        return arrays

    def config_dict(self) -> Dict[str, object]:
        return asdict(self.config)
