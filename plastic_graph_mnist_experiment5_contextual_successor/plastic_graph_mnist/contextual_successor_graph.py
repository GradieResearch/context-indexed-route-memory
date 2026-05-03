from __future__ import annotations

import math
from dataclasses import asdict, dataclass
from typing import Dict, Tuple

import numpy as np

from .context_router import ContextRouterConfig, PersistentContextRouter
from .inhibition import ContextualInhibitionController, InhibitionConfig
from .successor_graph import ConceptAssemblyBook


@dataclass(frozen=True)
class ContextualSuccessorGraphConfig:
    """Sparse recurrent graph for Experiment 5's contextual traversal world."""

    num_concepts: int = 25
    mode_names: Tuple[str, ...] = ("plus_one", "plus_two", "minus_one")
    hidden_units: int = 4096
    assembly_size: int = 72
    mode_assembly_size: int = 24
    active_units: int = 96
    recurrent_edges_per_unit: int = 48
    learning_rate: float = 0.08
    negative_learning_rate: float = 0.02
    structural_replacements_per_update: int = 8
    weight_decay: float = 0.0001
    homeostasis_strength: float = 0.02
    context_routing_bonus: float = 0.5
    reserved_context_units: int = 16
    context_source_gain: float = 4.0
    competing_context_penalty: float = 0.35
    lingering_activity_penalty: float = 0.08
    use_recurrence: bool = True
    use_structural_plasticity: bool = True
    use_homeostasis: bool = True
    use_reward_gate: bool = True
    use_context_routing: bool = True
    use_inhibition: bool = True
    seed: int = 42


@dataclass(frozen=True)
class ContextualTraversalResult:
    predicted: int
    predicted_mode: str
    confidence: float
    context_confidence: float
    active_units: int
    unique_active_units: int
    recurrent_drive_norm: float
    path_entropy: float
    concept_overlaps: np.ndarray
    mode_overlaps: np.ndarray


class ModeAssemblyBook:
    """Maps context/mode labels to persistent sparse assemblies."""

    def __init__(self, mode_names: Tuple[str, ...], hidden_units: int, assembly_size: int, rng: np.random.Generator):
        if assembly_size > hidden_units:
            raise ValueError("mode assembly_size cannot exceed hidden_units")
        self.mode_names = mode_names
        self.name_to_index = {name: idx for idx, name in enumerate(mode_names)}
        self._assemblies = np.zeros((len(mode_names), assembly_size), dtype=np.int32)
        for index in range(len(mode_names)):
            self._assemblies[index] = np.sort(rng.choice(hidden_units, size=assembly_size, replace=False))

    def assembly(self, mode: str) -> np.ndarray:
        return self._assemblies[self.name_to_index[mode]]

    def competing_assemblies(self, mode: str) -> np.ndarray:
        current = self.name_to_index[mode]
        indices = [idx for idx in range(len(self.mode_names)) if idx != current]
        if not indices:
            return np.zeros(0, dtype=np.int32)
        return np.unique(self._assemblies[indices].reshape(-1)).astype(np.int32)

    def decode(self, active: np.ndarray) -> tuple[str, float, np.ndarray]:
        active_set = set(int(x) for x in active)
        overlaps = np.zeros(len(self.mode_names), dtype=np.float32)
        for index, _name in enumerate(self.mode_names):
            overlaps[index] = sum(1 for unit in self._assemblies[index] if int(unit) in active_set) / len(self._assemblies[index])
        predicted_index = int(np.argmax(overlaps))
        return self.mode_names[predicted_index], float(overlaps[predicted_index]), overlaps

    def arrays(self) -> Dict[str, np.ndarray]:
        return {"mode_assemblies": self._assemblies.copy()}


class ContextualSparseRecurrentGraph:
    """Context-conditioned recurrent plastic graph with sparse local updates."""

    def __init__(self, config: ContextualSuccessorGraphConfig):
        if config.assembly_size > config.active_units:
            raise ValueError("assembly_size should not exceed active_units")
        if config.reserved_context_units >= config.active_units:
            raise ValueError("reserved_context_units must be smaller than active_units")
        self.config = config
        self.rng = np.random.default_rng(config.seed)
        self.book = ConceptAssemblyBook(
            num_concepts=config.num_concepts,
            hidden_units=config.hidden_units,
            assembly_size=config.assembly_size,
            rng=self.rng,
        )
        self.mode_book = ModeAssemblyBook(
            mode_names=config.mode_names,
            hidden_units=config.hidden_units,
            assembly_size=config.mode_assembly_size,
            rng=self.rng,
        )
        self.router = PersistentContextRouter(
            ContextRouterConfig(
                routing_bonus=config.context_routing_bonus,
                reserved_context_units=config.reserved_context_units,
            )
        )
        self.inhibition = ContextualInhibitionController(
            InhibitionConfig(
                competing_context_penalty=config.competing_context_penalty,
                lingering_activity_penalty=config.lingering_activity_penalty,
            )
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

    def activate_state(self, concept: int, mode: str) -> np.ndarray:
        concept_units = self.book.assembly(concept)
        context_units = self.mode_book.assembly(mode)
        return np.unique(np.concatenate([concept_units, context_units])).astype(np.int32)

    def decode_state(self, active: np.ndarray) -> tuple[int, float, np.ndarray, str, float, np.ndarray]:
        predicted, confidence, concept_overlaps = self.book.decode(active)
        predicted_mode, context_confidence, mode_overlaps = self.mode_book.decode(active)
        return predicted, confidence, concept_overlaps, predicted_mode, context_confidence, mode_overlaps

    def decode_concept_from_drive(self, drive: np.ndarray) -> int:
        scores = np.zeros(self.config.num_concepts, dtype=np.float32)
        for concept in range(self.config.num_concepts):
            scores[concept] = float(np.mean(drive[self.book.assembly(concept)]))
        return int(np.argmax(scores))

    def _select_next_active(self, drive: np.ndarray, mode: str) -> np.ndarray:
        if self.config.use_context_routing:
            return self.router.select_active(drive, self.mode_book.assembly(mode), self.config.active_units)

        if self.config.active_units >= self.config.hidden_units:
            return np.argsort(drive)[::-1].astype(np.int32)
        top = np.argpartition(drive, -self.config.active_units)[-self.config.active_units:]
        return top[np.argsort(drive[top])[::-1]].astype(np.int32)

    def step(self, active: np.ndarray, mode: str) -> tuple[np.ndarray, float, np.ndarray]:
        if not self.config.use_recurrence:
            drive = np.zeros(self.config.hidden_units, dtype=np.float32)
            drive[active] = 1.0
            return active.copy(), 0.0, drive

        drive = np.zeros(self.config.hidden_units, dtype=np.float32)
        context_set = set(int(x) for x in self.mode_book.assembly(mode))
        for source in active:
            gain = self.config.context_source_gain if int(source) in context_set else 1.0
            np.add.at(drive, self.edge_targets[source], self.edge_weights[source] * gain)

        if self.config.use_homeostasis:
            drive = drive - self.thresholds
        if self.config.use_context_routing:
            drive = self.router.boost(drive, self.mode_book.assembly(mode))
        if self.config.use_inhibition:
            drive = self.inhibition.apply(
                drive,
                current_context_units=self.mode_book.assembly(mode),
                competing_context_units=self.mode_book.competing_assemblies(mode),
                previous_active=active,
            )

        recurrent_drive_norm = float(np.linalg.norm(drive))
        next_active = self._select_next_active(drive, mode)
        return next_active, recurrent_drive_norm, drive

    def traverse(self, start_concept: int, mode: str, steps: int) -> ContextualTraversalResult:
        active = self.activate_state(start_concept, mode)
        seen = set(int(x) for x in active)
        total_drive = 0.0
        for _ in range(steps):
            raw_next, drive_norm, drive = self.step(active, mode)
            total_drive += drive_norm
            seen.update(int(x) for x in raw_next)
            predicted = self.decode_concept_from_drive(drive)
            if self.config.use_context_routing:
                active = self.activate_state(predicted, mode)
            else:
                active = self.book.assembly(predicted).copy()
            seen.update(int(x) for x in active)

        predicted, confidence, concept_overlaps, predicted_mode, context_confidence, mode_overlaps = self.decode_state(active)
        probs = concept_overlaps / max(float(concept_overlaps.sum()), 1e-6)
        path_entropy = float(-np.sum(probs * np.log(np.clip(probs, 1e-8, 1.0))) / math.log(len(probs)))
        return ContextualTraversalResult(
            predicted=predicted,
            predicted_mode=predicted_mode,
            confidence=confidence,
            context_confidence=context_confidence,
            active_units=int(len(active)),
            unique_active_units=int(len(seen)),
            recurrent_drive_norm=total_drive / max(1, steps),
            path_entropy=path_entropy,
            concept_overlaps=concept_overlaps,
            mode_overlaps=mode_overlaps,
        )

    def _apply_update(self, source_concept: int, mode: str, target_concept: int, reward: float) -> tuple[int, int, int]:
        source_active = self.activate_state(source_concept, mode)
        target_active = self.book.assembly(target_concept)
        predicted = self.traverse(source_concept, mode, 1)
        target_set = set(int(x) for x in target_active)
        predicted_set = set(int(x) for x in self.book.assembly(predicted.predicted))

        replacements = 0
        potentiated = 0
        depressed = 0

        for source in source_active:
            targets = self.edge_targets[source]
            weights = self.edge_weights[source]
            hit_mask = np.array([int(t) in target_set for t in targets], dtype=bool)
            if hit_mask.any() and reward > 0.0:
                weights[hit_mask] += self.config.learning_rate * reward
                potentiated += int(hit_mask.sum())

            if reward < 0.0:
                bad_mask = np.array([int(t) in predicted_set for t in targets], dtype=bool)
                if bad_mask.any():
                    weights[bad_mask] -= self.config.negative_learning_rate * abs(reward)
                    depressed += int(bad_mask.sum())

            if self.config.use_structural_plasticity:
                replace_count = min(self.config.structural_replacements_per_update, len(weights))
                weakest = np.argpartition(weights, replace_count - 1)[:replace_count]
                new_targets = self.rng.choice(target_active, size=replace_count, replace=True)
                targets[weakest] = new_targets.astype(np.int32)
                weights[weakest] = np.maximum(weights[weakest], 0.0) + self.config.learning_rate * max(reward, 0.25)
                replacements += int(replace_count)

        self.edge_weights *= (1.0 - self.config.weight_decay)
        np.clip(self.edge_weights, -1.0, 2.0, out=self.edge_weights)

        if self.config.use_homeostasis:
            self.usage *= 0.995
            self.usage[source_active] += 1.0
            centered = (self.usage - self.usage.mean()) / (self.usage.std() + 1e-6)
            self.thresholds += self.config.homeostasis_strength * centered
            np.clip(self.thresholds, -2.0, 2.0, out=self.thresholds)

        return potentiated, depressed, replacements

    def train_sequence(self, example, feedback_noise: float = 0.0, delayed_reward: bool = False) -> Dict[str, float]:
        before = self.traverse(example.start, example.mode, example.steps)
        raw_reward = 1.0 if before.predicted == example.target else -1.0
        if feedback_noise > 0.0 and self.rng.random() < feedback_noise:
            raw_reward *= -1.0
        reward = raw_reward if self.config.use_reward_gate else 1.0

        potentiated = 0
        depressed = 0
        replacements = 0

        if delayed_reward and example.steps > 1:
            for source, target in zip(example.path[:-1], example.path[1:]):
                p, d, r = self._apply_update(source, example.mode, target, reward)
                potentiated += p
                depressed += d
                replacements += r
        else:
            for source, target in zip(example.path[:-1], example.path[1:]):
                local_before = self.traverse(source, example.mode, 1)
                local_reward = 1.0 if local_before.predicted == target else -1.0
                if feedback_noise > 0.0 and self.rng.random() < feedback_noise:
                    local_reward *= -1.0
                if not self.config.use_reward_gate:
                    local_reward = 1.0
                p, d, r = self._apply_update(source, example.mode, target, local_reward)
                potentiated += p
                depressed += d
                replacements += r

        after = self.traverse(example.start, example.mode, example.steps)
        return {
            "before_correct": float(before.predicted == example.target),
            "after_correct": float(after.predicted == example.target),
            "before_context_match": float(before.predicted_mode == example.mode),
            "after_context_match": float(after.predicted_mode == example.mode),
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
        arrays.update(self.mode_book.arrays())
        return arrays

    def config_dict(self) -> Dict[str, object]:
        return asdict(self.config)
