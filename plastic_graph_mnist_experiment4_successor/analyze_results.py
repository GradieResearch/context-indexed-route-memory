from __future__ import annotations

import argparse
import csv
import io
import json
import logging
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np

try:
    import matplotlib.pyplot as plt
except ImportError:  # pragma: no cover - handled at runtime
    plt = None


LOGGER = logging.getLogger("plastic_graph_analysis")


@dataclass(frozen=True)
class RunSummary:
    run_id: int
    run_name: str
    status: str
    started_at: str
    completed_at: str | None
    best_accuracy: float | None
    config: dict


@dataclass(frozen=True)
class MetricPoint:
    run_id: int
    epoch: int
    step: int
    split: str
    name: str
    value: float
    created_at: str


@dataclass(frozen=True)
class CheckpointSummary:
    checkpoint_id: int
    run_id: int
    epoch: int
    step: int
    artifact_name: str
    created_at: str
    arrays: dict[str, tuple[int, ...]]
    stats: dict[str, dict[str, float]]


class ExperimentDatabase:
    """Read-only access over the SQLite experiment database."""

    def __init__(self, database_path: Path):
        self.database_path = database_path

    def connect(self) -> sqlite3.Connection:
        if not self.database_path.exists():
            raise FileNotFoundError(f"Database not found: {self.database_path}")
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        return connection

    def list_runs(self) -> list[RunSummary]:
        with self.connect() as connection:
            rows = connection.execute(
                """
                SELECT id, run_name, status, started_at, completed_at, best_accuracy, config_json
                FROM experiment_runs
                ORDER BY id ASC
                """
            ).fetchall()
        return [self._row_to_run(row) for row in rows]

    def get_run(self, run_id: int | None) -> RunSummary:
        with self.connect() as connection:
            if run_id is None:
                row = connection.execute(
                    """
                    SELECT id, run_name, status, started_at, completed_at, best_accuracy, config_json
                    FROM experiment_runs
                    ORDER BY id DESC
                    LIMIT 1
                    """
                ).fetchone()
            else:
                row = connection.execute(
                    """
                    SELECT id, run_name, status, started_at, completed_at, best_accuracy, config_json
                    FROM experiment_runs
                    WHERE id = ?
                    """,
                    (run_id,),
                ).fetchone()
        if row is None:
            raise ValueError(f"No experiment run found for run_id={run_id!r}")
        return self._row_to_run(row)

    def get_metrics(self, run_id: int) -> list[MetricPoint]:
        with self.connect() as connection:
            rows = connection.execute(
                """
                SELECT run_id, epoch, step, split, name, value, created_at
                FROM metric_records
                WHERE run_id = ?
                ORDER BY step ASC, split ASC, name ASC
                """,
                (run_id,),
            ).fetchall()
        return [
            MetricPoint(
                run_id=row["run_id"],
                epoch=row["epoch"],
                step=row["step"],
                split=row["split"],
                name=row["name"],
                value=float(row["value"]),
                created_at=row["created_at"],
            )
            for row in rows
        ]

    def get_latest_checkpoint(self, run_id: int) -> tuple[sqlite3.Row, dict[str, np.ndarray]] | None:
        with self.connect() as connection:
            row = connection.execute(
                """
                SELECT id, run_id, epoch, step, artifact_name, payload, created_at
                FROM checkpoint_records
                WHERE run_id = ?
                ORDER BY step DESC, id DESC
                LIMIT 1
                """,
                (run_id,),
            ).fetchone()
        if row is None:
            return None
        arrays = self._load_npz(row["payload"])
        return row, arrays

    @staticmethod
    def _load_npz(payload: bytes) -> dict[str, np.ndarray]:
        with np.load(io.BytesIO(payload)) as loaded:
            return {name: loaded[name] for name in loaded.files}

    @staticmethod
    def _row_to_run(row: sqlite3.Row) -> RunSummary:
        return RunSummary(
            run_id=int(row["id"]),
            run_name=str(row["run_name"]),
            status=str(row["status"]),
            started_at=str(row["started_at"]),
            completed_at=str(row["completed_at"]) if row["completed_at"] else None,
            best_accuracy=float(row["best_accuracy"]) if row["best_accuracy"] is not None else None,
            config=json.loads(row["config_json"]),
        )


class MetricAnalyzer:
    """Transforms raw metric records into human-readable summaries."""

    def __init__(self, metrics: Sequence[MetricPoint]):
        self.metrics = list(metrics)

    def latest_by_metric(self) -> dict[tuple[str, str], MetricPoint]:
        latest: dict[tuple[str, str], MetricPoint] = {}
        for metric in self.metrics:
            key = (metric.split, metric.name)
            if key not in latest or metric.step >= latest[key].step:
                latest[key] = metric
        return latest

    def best_test_accuracy(self) -> MetricPoint | None:
        candidates = [m for m in self.metrics if m.split == "test" and m.name == "accuracy"]
        if not candidates:
            return None
        return max(candidates, key=lambda m: m.value)

    def first_last_delta(self, split: str, name: str) -> tuple[MetricPoint, MetricPoint, float] | None:
        series = [m for m in self.metrics if m.split == split and m.name == name]
        if len(series) < 2:
            return None
        first = min(series, key=lambda m: m.step)
        last = max(series, key=lambda m: m.step)
        return first, last, last.value - first.value

    def series(self, split: str, name: str) -> list[MetricPoint]:
        return [m for m in self.metrics if m.split == split and m.name == name]


class CheckpointAnalyzer:
    """Inspects model arrays saved in the latest checkpoint."""

    def summarize(self, row: sqlite3.Row, arrays: dict[str, np.ndarray]) -> CheckpointSummary:
        shapes = {name: tuple(array.shape) for name, array in arrays.items()}
        stats = {name: self._array_stats(array) for name, array in arrays.items()}
        return CheckpointSummary(
            checkpoint_id=int(row["id"]),
            run_id=int(row["run_id"]),
            epoch=int(row["epoch"]),
            step=int(row["step"]),
            artifact_name=str(row["artifact_name"]),
            created_at=str(row["created_at"]),
            arrays=shapes,
            stats=stats,
        )

    @staticmethod
    def _array_stats(array: np.ndarray) -> dict[str, float]:
        values = array.astype(np.float64, copy=False).ravel()
        if values.size == 0:
            return {"count": 0.0}
        return {
            "count": float(values.size),
            "mean": float(np.mean(values)),
            "std": float(np.std(values)),
            "min": float(np.min(values)),
            "p05": float(np.quantile(values, 0.05)),
            "p50": float(np.quantile(values, 0.50)),
            "p95": float(np.quantile(values, 0.95)),
            "max": float(np.max(values)),
            "nonzero_fraction": float(np.count_nonzero(values) / values.size),
        }


class AnalysisReportWriter:
    """Writes markdown, CSV, and optional PNG plots for one run."""

    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def write_metrics_csv(self, metrics: Iterable[MetricPoint]) -> Path:
        path = self.output_dir / "metrics.csv"
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(["run_id", "epoch", "step", "split", "name", "value", "created_at"])
            for metric in metrics:
                writer.writerow([
                    metric.run_id,
                    metric.epoch,
                    metric.step,
                    metric.split,
                    metric.name,
                    metric.value,
                    metric.created_at,
                ])
        return path

    def write_checkpoint_json(self, checkpoint: CheckpointSummary | None) -> Path | None:
        if checkpoint is None:
            return None
        path = self.output_dir / "latest_checkpoint_summary.json"
        payload = {
            "checkpoint_id": checkpoint.checkpoint_id,
            "run_id": checkpoint.run_id,
            "epoch": checkpoint.epoch,
            "step": checkpoint.step,
            "artifact_name": checkpoint.artifact_name,
            "created_at": checkpoint.created_at,
            "arrays": {k: list(v) for k, v in checkpoint.arrays.items()},
            "stats": checkpoint.stats,
        }
        path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
        return path

    def write_markdown(
        self,
        run: RunSummary,
        metrics: MetricAnalyzer,
        checkpoint: CheckpointSummary | None,
        generated_files: Sequence[Path],
    ) -> Path:
        path = self.output_dir / "analysis_report.md"
        latest = metrics.latest_by_metric()
        best = metrics.best_test_accuracy()
        train_delta = metrics.first_last_delta("train", "window_accuracy")
        test_delta = metrics.first_last_delta("test", "accuracy")

        lines: list[str] = []
        lines.append(f"# Plastic Graph MNIST Analysis — Run {run.run_id}\n")
        lines.append("## Run summary\n")
        lines.append(f"- Name: `{run.run_name}`")
        lines.append(f"- Status: `{run.status}`")
        lines.append(f"- Started: `{run.started_at}`")
        lines.append(f"- Completed: `{run.completed_at}`")
        lines.append(f"- Recorded best accuracy: `{self._fmt(run.best_accuracy)}`")
        lines.append("")

        lines.append("## Key metrics\n")
        if best is not None:
            lines.append(f"- Best test accuracy: **{best.value:.4f}** at step `{best.step}` / epoch `{best.epoch}`")
        for key in sorted(latest):
            metric = latest[key]
            lines.append(f"- Latest {metric.split}/{metric.name}: `{metric.value:.4f}` at step `{metric.step}`")
        if train_delta is not None:
            first, last, delta = train_delta
            lines.append(f"- Train window accuracy delta: `{first.value:.4f}` → `{last.value:.4f}` = `{delta:+.4f}`")
        if test_delta is not None:
            first, last, delta = test_delta
            lines.append(f"- Test accuracy delta: `{first.value:.4f}` → `{last.value:.4f}` = `{delta:+.4f}`")
        lines.append("")

        lines.append("## Configuration highlights\n")
        for key in [
            "hidden_units",
            "input_edges_per_hidden",
            "active_hidden",
            "learning_rate_hidden_output",
            "learning_rate_input_hidden",
            "trace_decay",
            "threshold_lr",
            "epochs",
            "max_train",
            "max_test",
        ]:
            if key in run.config:
                lines.append(f"- {key}: `{run.config[key]}`")
        lines.append("")

        if checkpoint is not None:
            lines.append("## Latest checkpoint\n")
            lines.append(f"- Artifact: `{checkpoint.artifact_name}`")
            lines.append(f"- Epoch/step: `{checkpoint.epoch}` / `{checkpoint.step}`")
            lines.append("- Arrays:")
            for name, shape in sorted(checkpoint.arrays.items()):
                stat = checkpoint.stats[name]
                lines.append(
                    f"  - `{name}` shape={shape}, mean={stat.get('mean', 0):.6f}, "
                    f"std={stat.get('std', 0):.6f}, p95={stat.get('p95', 0):.6f}, "
                    f"nonzero={stat.get('nonzero_fraction', 0):.4f}"
                )
            lines.append("")

        lines.append("## Interpretation guide\n")
        lines.append("- Rising `test/accuracy` means the plastic graph is learning pathways that generalize beyond the online training stream.")
        lines.append("- Rising `train/window_accuracy` with flat test accuracy suggests memorization or unstable routing rather than generalizable reasoning.")
        lines.append("- Very high confidence with poor accuracy suggests runaway reinforcement or an overly aggressive plasticity gate.")
        lines.append("- Very low confidence and poor accuracy suggests the readout is not consolidating useful hidden pathways.")
        lines.append("- Large threshold drift or very high trace concentration suggests the active population may be collapsing onto too few units.")
        lines.append("")

        if generated_files:
            lines.append("## Generated files\n")
            for generated in generated_files:
                lines.append(f"- `{generated.name}`")
            lines.append("")

        path.write_text("\n".join(lines), encoding="utf-8")
        return path

    def write_plots(self, analyzer: MetricAnalyzer) -> list[Path]:
        if plt is None:
            LOGGER.warning("matplotlib is not installed; skipping plots")
            return []

        paths: list[Path] = []
        paths.extend(self._plot_series(analyzer, "test", "accuracy", "test_accuracy.png"))
        paths.extend(self._plot_series(analyzer, "train", "window_accuracy", "train_window_accuracy.png"))
        paths.extend(self._plot_series(analyzer, "test", "average_confidence", "test_average_confidence.png"))
        paths.extend(self._plot_series(analyzer, "train", "average_confidence", "train_average_confidence.png"))
        return paths

    def _plot_series(self, analyzer: MetricAnalyzer, split: str, name: str, filename: str) -> list[Path]:
        series = analyzer.series(split, name)
        if not series:
            return []
        steps = [point.step for point in series]
        values = [point.value for point in series]
        fig = plt.figure(figsize=(9, 5))
        plt.plot(steps, values, marker="o")
        plt.xlabel("Global step")
        plt.ylabel(f"{split}/{name}")
        plt.title(f"{split}/{name} over time")
        plt.grid(True, alpha=0.25)
        path = self.output_dir / filename
        fig.tight_layout()
        fig.savefig(path, dpi=150)
        plt.close(fig)
        return [path]

    @staticmethod
    def _fmt(value: float | None) -> str:
        return "None" if value is None else f"{value:.4f}"


class AnalysisApplication:
    def __init__(self, database: ExperimentDatabase, writer: AnalysisReportWriter):
        self.database = database
        self.writer = writer

    def list_runs(self) -> None:
        runs = self.database.list_runs()
        if not runs:
            print("No experiment runs found.")
            return
        for run in runs:
            print(
                f"run_id={run.run_id} name={run.run_name!r} status={run.status} "
                f"best_accuracy={run.best_accuracy} started_at={run.started_at}"
            )

    def analyze(self, run_id: int | None) -> Path:
        run = self.database.get_run(run_id)
        metrics = self.database.get_metrics(run.run_id)
        metric_analyzer = MetricAnalyzer(metrics)

        checkpoint_summary = None
        latest_checkpoint = self.database.get_latest_checkpoint(run.run_id)
        if latest_checkpoint is not None:
            row, arrays = latest_checkpoint
            checkpoint_summary = CheckpointAnalyzer().summarize(row, arrays)

        generated: list[Path] = []
        generated.append(self.writer.write_metrics_csv(metrics))
        checkpoint_json = self.writer.write_checkpoint_json(checkpoint_summary)
        if checkpoint_json is not None:
            generated.append(checkpoint_json)
        generated.extend(self.writer.write_plots(metric_analyzer))
        report = self.writer.write_markdown(run, metric_analyzer, checkpoint_summary, generated)
        LOGGER.info("Analysis report written to %s", report)
        return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze plastic graph MNIST experiment results.")
    parser.add_argument("--db", type=Path, default=Path("runs/plastic_graph_mnist.sqlite3"), help="Path to experiment SQLite database.")
    parser.add_argument("--run-id", type=int, default=None, help="Run id to analyze. Defaults to the most recent run.")
    parser.add_argument("--output-dir", type=Path, default=Path("analysis"), help="Directory for report, CSV, and plots.")
    parser.add_argument("--list-runs", action="store_true", help="List available runs and exit.")
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"], help="Logging level.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.basicConfig(level=getattr(logging, args.log_level), format="%(asctime)s %(levelname)s %(name)s - %(message)s")

    database = ExperimentDatabase(args.db)
    writer = AnalysisReportWriter(args.output_dir)
    app = AnalysisApplication(database, writer)

    if args.list_runs:
        app.list_runs()
        return

    report = app.analyze(args.run_id)
    print(f"Analysis report written to: {report}")


if __name__ == "__main__":
    main()
