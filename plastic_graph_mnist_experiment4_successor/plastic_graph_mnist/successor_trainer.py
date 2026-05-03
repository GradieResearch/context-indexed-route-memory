from __future__ import annotations

import logging
from dataclasses import asdict
from pathlib import Path
from typing import Dict, Iterable, List

import numpy as np

from .storage import ExperimentStore
from .successor_graph import SparseRecurrentAssemblyGraph, SuccessorGraphConfig
from .successor_task import AdditionExample, SuccessorTask, SuccessorTaskConfig

logger = logging.getLogger(__name__)


class SuccessorExperimentTrainer:
    """Trains and evaluates Experiment 4's compositional traversal task."""

    def __init__(
        self,
        graph_config: SuccessorGraphConfig,
        task_config: SuccessorTaskConfig,
        store: ExperimentStore,
        run_name: str,
    ):
        self.graph_config = graph_config
        self.task_config = task_config
        self.store = store
        self.run_name = run_name
        self.graph = SparseRecurrentAssemblyGraph(graph_config)
        self.task = SuccessorTask(task_config)
        self.run_id: int | None = None
        self.global_step = 0

    def start(self) -> int:
        config = {
            "experiment_phase": "exp4_successor_traversal",
            "graph": self.graph.config_dict(),
            "task": asdict(self.task_config),
        }
        self.run_id = self.store.create_run(self.run_name, config)
        return self.run_id

    def train(self, eval_every: int = 250) -> None:
        if self.run_id is None:
            self.start()
        assert self.run_id is not None
        examples = self.task.transition_examples()
        best_addition_accuracy = 0.0
        running_after_correct: list[float] = []

        for ex in examples:
            self.global_step += 1
            stats = self.graph.train_transition(ex.source, ex.target)
            running_after_correct.append(stats["after_correct"])
            if len(running_after_correct) > 250:
                running_after_correct.pop(0)

            if self.global_step % eval_every == 0:
                transition = self.evaluate_transitions()
                addition = self.evaluate_addition(self.task.heldout_long_addition_examples())
                best_addition_accuracy = max(best_addition_accuracy, addition["accuracy"])
                logger.info(
                    "step=%s transition_acc=%.4f addition_acc=%.4f avg_steps=%.2f",
                    self.global_step,
                    transition["accuracy"],
                    addition["accuracy"],
                    addition["average_steps"],
                )
                for split, metrics in (("transition", transition), ("addition", addition)):
                    for name, value in metrics.items():
                        self.store.record_metric(self.run_id, 0, self.global_step, split, name, float(value))
                self.store.record_metric(
                    self.run_id,
                    0,
                    self.global_step,
                    "train",
                    "recent_after_transition_accuracy",
                    float(np.mean(running_after_correct)) if running_after_correct else 0.0,
                )

        self.store.save_checkpoint(self.run_id, 0, self.global_step, "final", self.graph.arrays())
        self.store.complete_run(self.run_id, "completed", best_addition_accuracy)

    def evaluate_transitions(self) -> Dict[str, float]:
        correct = 0
        confidences = []
        drives = []
        unique = []
        for n in range(self.task_config.max_number):
            result = self.graph.traverse(n, 1, n + 1)
            correct += int(result.predicted == n + 1)
            confidences.append(result.confidence)
            drives.append(result.recurrent_drive_norm)
            unique.append(result.unique_active_units)
        total = self.task_config.max_number
        return {
            "accuracy": correct / total,
            "average_confidence": float(np.mean(confidences)),
            "average_recurrent_drive": float(np.mean(drives)),
            "average_unique_active": float(np.mean(unique)),
        }

    def evaluate_addition(self, examples: Iterable[AdditionExample]) -> Dict[str, float]:
        examples = list(examples)
        correct = 0
        confidences = []
        drives = []
        unique = []
        steps = []
        exact_by_steps: dict[int, list[int]] = {}
        for ex in examples:
            result = self.graph.traverse(ex.start, ex.steps, ex.target)
            hit = int(result.predicted == ex.target)
            correct += hit
            confidences.append(result.confidence)
            drives.append(result.recurrent_drive_norm)
            unique.append(result.unique_active_units)
            steps.append(ex.steps)
            exact_by_steps.setdefault(ex.steps, []).append(hit)
        metrics: Dict[str, float] = {
            "accuracy": correct / max(1, len(examples)),
            "average_confidence": float(np.mean(confidences)) if confidences else 0.0,
            "average_recurrent_drive": float(np.mean(drives)) if drives else 0.0,
            "average_unique_active": float(np.mean(unique)) if unique else 0.0,
            "average_steps": float(np.mean(steps)) if steps else 0.0,
        }
        for step_count, hits in exact_by_steps.items():
            metrics[f"accuracy_steps_{step_count}"] = float(np.mean(hits))
        return metrics
