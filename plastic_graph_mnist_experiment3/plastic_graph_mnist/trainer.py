from __future__ import annotations

import logging
from dataclasses import dataclass
from time import perf_counter

import numpy as np

from .config import ExperimentConfig
from .data import MnistProvider, Sample
from .modulators import RewardModulator
from .plastic_graph import PlasticGraphNetwork
from .storage import ExperimentStore

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class EvaluationResult:
    accuracy: float
    average_confidence: float
    count: int


class ExperimentTrainer:
    """Coordinates data, graph dynamics, reward modulation, and persistence."""

    def __init__(
        self,
        config: ExperimentConfig,
        data_provider: MnistProvider,
        graph: PlasticGraphNetwork,
        modulator: RewardModulator,
        store: ExperimentStore,
        run_id: int,
    ):
        self.config = config
        self.data_provider = data_provider
        self.graph = graph
        self.modulator = modulator
        self.store = store
        self.run_id = run_id
        self.global_step = 0
        self.best_accuracy = 0.0

    def train(self) -> None:
        train_samples, test_samples = self.data_provider.load(self.config.max_train, self.config.max_test)
        started = perf_counter()
        try:
            for epoch in range(1, self.config.epochs + 1):
                self._train_epoch(epoch, train_samples, test_samples)

            final_eval = self.evaluate(test_samples)
            self.best_accuracy = max(self.best_accuracy, final_eval.accuracy)
            self._record_eval(epoch=self.config.epochs, result=final_eval)
            self._checkpoint(epoch=self.config.epochs, artifact_name="final")
            self.store.complete_run(self.run_id, status="completed", best_accuracy=self.best_accuracy)
            logger.info("Training completed in %.2fs best_accuracy=%.4f", perf_counter() - started, self.best_accuracy)
        except Exception:
            logger.exception("Training failed")
            self.store.complete_run(self.run_id, status="failed", best_accuracy=self.best_accuracy)
            raise

    def _train_epoch(self, epoch: int, train_samples: list[Sample], test_samples: list[Sample]) -> None:
        correct_window = 0
        confidence_window = 0.0
        unique_active_window = 0.0
        recurrent_drive_window = 0.0
        window_count = 0
        epoch_started = perf_counter()

        for sample in self.data_provider.shuffled(train_samples, epoch):
            self.global_step += 1
            result = self.graph.forward(sample.x)
            modulation = self.modulator.evaluate(result.probabilities, sample.y)
            self.graph.learn(sample.x, sample.y, result, modulation)

            correct_window += int(modulation.correct)
            confidence_window += modulation.confidence
            unique_active_window += result.unique_active_count
            recurrent_drive_window += result.recurrent_drive_norm
            window_count += 1

            if self.global_step % self.config.log_every == 0:
                train_acc = correct_window / max(window_count, 1)
                avg_conf = confidence_window / max(window_count, 1)
                avg_unique_active = unique_active_window / max(window_count, 1)
                avg_recurrent_drive = recurrent_drive_window / max(window_count, 1)
                logger.info(
                    "epoch=%s step=%s window_train_acc=%.4f avg_conf=%.4f unique_active=%.1f recurrent_drive=%.3f gate=%.3f novelty=%.3f",
                    epoch,
                    self.global_step,
                    train_acc,
                    avg_conf,
                    avg_unique_active,
                    avg_recurrent_drive,
                    modulation.plasticity_gate,
                    modulation.novelty,
                )
                self.store.record_metric(self.run_id, epoch, self.global_step, "train", "window_accuracy", train_acc)
                self.store.record_metric(self.run_id, epoch, self.global_step, "train", "average_confidence", avg_conf)
                self.store.record_metric(self.run_id, epoch, self.global_step, "train", "average_unique_active", avg_unique_active)
                self.store.record_metric(self.run_id, epoch, self.global_step, "train", "average_recurrent_drive_norm", avg_recurrent_drive)
                correct_window = 0
                confidence_window = 0.0
                unique_active_window = 0.0
                recurrent_drive_window = 0.0
                window_count = 0

            if self.global_step % self.config.eval_every == 0:
                eval_result = self.evaluate(test_samples)
                self.best_accuracy = max(self.best_accuracy, eval_result.accuracy)
                self._record_eval(epoch, eval_result)
                logger.info(
                    "EVAL epoch=%s step=%s accuracy=%.4f avg_conf=%.4f best=%.4f",
                    epoch,
                    self.global_step,
                    eval_result.accuracy,
                    eval_result.average_confidence,
                    self.best_accuracy,
                )

            if self.global_step % self.config.checkpoint_every == 0:
                self._checkpoint(epoch, artifact_name=f"step_{self.global_step}")

        logger.info("Finished epoch=%s in %.2fs", epoch, perf_counter() - epoch_started)

    def evaluate(self, samples: list[Sample]) -> EvaluationResult:
        correct = 0
        confidence = 0.0
        for sample in samples:
            result = self.graph.forward(sample.x)
            correct += int(result.prediction == sample.y)
            confidence += float(np.max(result.probabilities))
        count = len(samples)
        return EvaluationResult(
            accuracy=correct / max(count, 1),
            average_confidence=confidence / max(count, 1),
            count=count,
        )

    def _record_eval(self, epoch: int, result: EvaluationResult) -> None:
        self.store.record_metric(self.run_id, epoch, self.global_step, "test", "accuracy", result.accuracy)
        self.store.record_metric(self.run_id, epoch, self.global_step, "test", "average_confidence", result.average_confidence)

    def _checkpoint(self, epoch: int, artifact_name: str) -> None:
        self.store.save_checkpoint(
            run_id=self.run_id,
            epoch=epoch,
            step=self.global_step,
            artifact_name=artifact_name,
            arrays=self.graph.checkpoint_arrays(),
        )
