from __future__ import annotations

import logging
from dataclasses import asdict
from typing import Dict, Iterable

import numpy as np

from .contextual_successor_graph import ContextualSparseRecurrentGraph, ContextualSuccessorGraphConfig
from .contextual_successor_task import ContextualSequenceExample, ContextualSuccessorTask, ContextualSuccessorTaskConfig
from .storage import ExperimentStore

logger = logging.getLogger(__name__)


class ContextualSuccessorExperimentTrainer:
    """Trains and evaluates Experiment 6's route-audited contextual traversal world."""

    def __init__(
        self,
        graph_config: ContextualSuccessorGraphConfig,
        task_config: ContextualSuccessorTaskConfig,
        store: ExperimentStore,
        run_name: str,
    ):
        self.graph_config = graph_config
        self.task_config = task_config
        self.store = store
        self.run_name = run_name
        self.graph = ContextualSparseRecurrentGraph(graph_config)
        self.task = ContextualSuccessorTask(task_config)
        self.run_id: int | None = None
        self.global_step = 0

    def start(self) -> int:
        config = {
            "experiment_phase": "exp6_route_audit_successor_world",
            "graph": self.graph.config_dict(),
            "task": asdict(self.task_config),
        }
        self.run_id = self.store.create_run(self.run_name, config)
        return self.run_id

    def train(self, eval_every: int = 250) -> None:
        if self.run_id is None:
            self.start()
        assert self.run_id is not None
        examples = self.task.training_examples()
        best_composition_accuracy = 0.0
        running_after_correct: list[float] = []

        for example in examples:
            self.global_step += 1
            stats = self.graph.train_sequence(
                example,
                feedback_noise=self.task_config.feedback_noise,
                delayed_reward=self.task_config.delayed_reward,
            )
            running_after_correct.append(stats["after_correct"])
            if len(running_after_correct) > 250:
                running_after_correct.pop(0)

            if self.global_step % eval_every == 0:
                current_phase = example.phase
                transition = self.evaluate_examples(self.task.evaluation_examples(current_phase, min_steps=1))
                composition = self.evaluate_examples(self.task.evaluation_examples(current_phase, min_steps=2))
                best_composition_accuracy = max(best_composition_accuracy, composition["accuracy"])
                logger.info(
                    "step=%s phase=%s transition_acc=%.4f composition_acc=%.4f wrong_route=%.4f",
                    self.global_step,
                    current_phase,
                    transition["accuracy"],
                    composition["accuracy"],
                    composition["average_wrong_route_activation"],
                )
                for split, metrics in (("transition", transition), ("composition", composition)):
                    for name, value in metrics.items():
                        self.store.record_metric(self.run_id, 0, self.global_step, split, name, float(value))
                self.store.record_metric(
                    self.run_id,
                    0,
                    self.global_step,
                    "train",
                    "recent_after_sequence_accuracy",
                    float(np.mean(running_after_correct)) if running_after_correct else 0.0,
                )
                self.store.record_metric(self.run_id, 0, self.global_step, "train", "current_phase", float(current_phase))

        self.store.save_checkpoint(self.run_id, 0, self.global_step, "final", self.graph.arrays())
        self.store.complete_run(self.run_id, "completed", best_composition_accuracy)

    def evaluate_examples(self, examples: Iterable[ContextualSequenceExample]) -> Dict[str, float]:
        examples = list(examples)
        if not examples:
            return {"accuracy": 0.0}

        correct = 0
        drives = []
        unique = []
        path_entropy = []
        confidences = []
        context_confidences = []
        wrong_routes = []
        right_routes = []
        margins = []
        context_margins = []
        steps = []
        accuracy_by_steps: dict[int, list[int]] = {}
        accuracy_by_mode: dict[str, list[int]] = {}
        confusion: dict[tuple[str, str], int] = {}

        for example in examples:
            result = self.graph.traverse(example.start, example.mode, example.steps)
            hit = int(result.predicted == example.target)
            correct += hit
            drives.append(result.recurrent_drive_norm)
            unique.append(result.unique_active_units)
            path_entropy.append(result.path_entropy)
            confidences.append(result.confidence)
            context_confidences.append(result.context_confidence)
            steps.append(example.steps)

            per_step_wrong = []
            per_step_right = []
            for step_index in range(example.steps):
                concept_overlaps = result.step_concept_overlaps[step_index]
                target_overlap = float(concept_overlaps[example.path[step_index + 1]])
                competing_overlap = 0.0
                for other_mode in self.task.mode_names:
                    if other_mode == example.mode:
                        continue
                    other_path = self.task.rollout(other_mode, example.start, example.steps, example.phase)
                    if other_path is None:
                        continue
                    competing_overlap = max(competing_overlap, float(concept_overlaps[other_path[step_index + 1]]))
                per_step_right.append(target_overlap)
                per_step_wrong.append(competing_overlap)

            wrong_routes.append(float(np.mean(per_step_wrong)) if per_step_wrong else 0.0)
            right_routes.append(float(np.mean(per_step_right)) if per_step_right else 0.0)
            margins.append((float(np.mean(per_step_right)) if per_step_right else 0.0) - (float(np.mean(per_step_wrong)) if per_step_wrong else 0.0))
            mode_index = self.task.mode_names.index(example.mode)
            competing_mode = max(float(result.mode_overlaps[idx]) for idx, other_mode in enumerate(self.task.mode_names) if other_mode != example.mode)
            context_margins.append(float(result.mode_overlaps[mode_index]) - competing_mode)

            accuracy_by_steps.setdefault(example.steps, []).append(hit)
            accuracy_by_mode.setdefault(example.mode, []).append(hit)
            confusion[(example.mode, result.predicted_mode)] = confusion.get((example.mode, result.predicted_mode), 0) + 1

        metrics: Dict[str, float] = {
            "accuracy": correct / len(examples),
            "average_confidence": float(np.mean(confidences)),
            "average_context_confidence": float(np.mean(context_confidences)),
            "average_recurrent_drive": float(np.mean(drives)),
            "average_unique_active": float(np.mean(unique)),
            "average_path_entropy": float(np.mean(path_entropy)),
            "average_target_route_activation": float(np.mean(right_routes)),
            "average_wrong_route_activation": float(np.mean(wrong_routes)),
            "average_route_margin": float(np.mean(margins)),
            "average_context_margin": float(np.mean(context_margins)),
            "average_steps": float(np.mean(steps)),
        }
        for step_count, hits in sorted(accuracy_by_steps.items()):
            metrics[f"accuracy_steps_{step_count}"] = float(np.mean(hits))
        for mode_name, hits in sorted(accuracy_by_mode.items()):
            metrics[f"accuracy_mode_{mode_name}"] = float(np.mean(hits))
        for actual_mode in self.task.mode_names:
            row_total = sum(confusion.get((actual_mode, predicted_mode), 0) for predicted_mode in self.task.mode_names)
            for predicted_mode in self.task.mode_names:
                key = f"confusion_{actual_mode}__{predicted_mode}"
                value = confusion.get((actual_mode, predicted_mode), 0) / max(1, row_total)
                metrics[key] = float(value)
        return metrics
