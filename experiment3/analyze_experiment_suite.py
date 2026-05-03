from __future__ import annotations

import argparse
import csv
import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import matplotlib.pyplot as plt
except ImportError:  # pragma: no cover
    plt = None


@dataclass(frozen=True)
class RunResult:
    run_id: int
    run_name: str
    status: str
    best_accuracy: float | None
    latest_test_accuracy: float | None
    latest_test_confidence: float | None
    latest_train_accuracy: float | None
    latest_train_confidence: float | None
    latest_unique_active: float | None
    latest_recurrent_drive: float | None
    config: dict[str, Any]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compare plastic graph experiment-suite variants")
    parser.add_argument("--db", type=Path, default=Path("runs/plastic_graph_suite.sqlite3"))
    parser.add_argument("--output-dir", type=Path, default=Path("analysis/suite"))
    return parser.parse_args()


def connect(db: Path) -> sqlite3.Connection:
    if not db.exists():
        raise FileNotFoundError(f"Database not found: {db}")
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    return con


def latest_metric(con: sqlite3.Connection, run_id: int, split: str, name: str) -> float | None:
    row = con.execute(
        """
        SELECT value
        FROM metric_records
        WHERE run_id = ? AND split = ? AND name = ?
        ORDER BY step DESC, id DESC
        LIMIT 1
        """,
        (run_id, split, name),
    ).fetchone()
    return None if row is None else float(row["value"])


def collect_results(db: Path) -> list[RunResult]:
    with connect(db) as con:
        rows = con.execute(
            """
            SELECT id, run_name, status, best_accuracy, config_json
            FROM experiment_runs
            ORDER BY id ASC
            """
        ).fetchall()
        results: list[RunResult] = []
        for row in rows:
            run_id = int(row["id"])
            config = json.loads(row["config_json"])
            results.append(
                RunResult(
                    run_id=run_id,
                    run_name=row["run_name"],
                    status=row["status"],
                    best_accuracy=None if row["best_accuracy"] is None else float(row["best_accuracy"]),
                    latest_test_accuracy=latest_metric(con, run_id, "test", "accuracy"),
                    latest_test_confidence=latest_metric(con, run_id, "test", "average_confidence"),
                    latest_train_accuracy=latest_metric(con, run_id, "train", "window_accuracy"),
                    latest_train_confidence=latest_metric(con, run_id, "train", "average_confidence"),
                    latest_unique_active=latest_metric(con, run_id, "train", "average_unique_active"),
                    latest_recurrent_drive=latest_metric(con, run_id, "train", "average_recurrent_drive_norm"),
                    config=config,
                )
            )
    return results


def write_csv(results: list[RunResult], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "run_id",
                "run_name",
                "status",
                "best_accuracy",
                "latest_test_accuracy",
                "latest_test_confidence",
                "latest_train_accuracy",
                "latest_train_confidence",
                "generalization_gap",
                "latest_unique_active",
                "latest_recurrent_drive",
                "use_recurrence",
                "use_thresholds",
                "use_traces",
                "use_input_plasticity",
                "use_reward_modulation",
            ],
        )
        writer.writeheader()
        for r in results:
            gap = None
            if r.latest_train_accuracy is not None and r.latest_test_accuracy is not None:
                gap = r.latest_train_accuracy - r.latest_test_accuracy
            writer.writerow(
                {
                    "run_id": r.run_id,
                    "run_name": r.run_name,
                    "status": r.status,
                    "best_accuracy": r.best_accuracy,
                    "latest_test_accuracy": r.latest_test_accuracy,
                    "latest_test_confidence": r.latest_test_confidence,
                    "latest_train_accuracy": r.latest_train_accuracy,
                    "latest_train_confidence": r.latest_train_confidence,
                    "generalization_gap": gap,
                    "latest_unique_active": r.latest_unique_active,
                    "latest_recurrent_drive": r.latest_recurrent_drive,
                    "use_recurrence": r.config.get("use_recurrence"),
                    "use_thresholds": r.config.get("use_thresholds"),
                    "use_traces": r.config.get("use_traces"),
                    "use_input_plasticity": r.config.get("use_input_plasticity"),
                    "use_reward_modulation": r.config.get("use_reward_modulation"),
                }
            )


def fmt(value: float | None) -> str:
    return "n/a" if value is None else f"{value:.4f}"


def write_markdown(results: list[RunResult], path: Path) -> None:
    ordered = sorted(results, key=lambda r: (r.best_accuracy or -1), reverse=True)
    lines = [
        "# Plastic Graph Experiment Suite Analysis",
        "",
        "This report compares controlled variants of the sparse plastic graph model. The goal is not merely to maximize MNIST accuracy; the goal is to identify which architectural mechanisms actually contribute to stable, generalizable online learning.",
        "",
        "## How to read this",
        "",
        "- **Best accuracy**: best recorded test accuracy. This is the headline performance metric.",
        "- **Generalization gap**: latest train window accuracy minus latest test accuracy. A large positive gap suggests memorization or over-specialization.",
        "- **Unique active**: average number of unique hidden units recruited across the recurrent traversal. If recurrence is active, this should usually exceed `active_hidden`.",
        "- **Recurrent drive**: magnitude of hidden-to-hidden contribution. If this is near zero, the recurrent graph is present but not functionally important yet.",
        "",
        "## Results",
        "",
        "| Rank | Run | Best test acc | Latest test acc | Train acc | Gap | Unique active | Recurrent drive |",
        "|---:|---|---:|---:|---:|---:|---:|---:|",
    ]
    for idx, r in enumerate(ordered, start=1):
        gap = None
        if r.latest_train_accuracy is not None and r.latest_test_accuracy is not None:
            gap = r.latest_train_accuracy - r.latest_test_accuracy
        lines.append(
            f"| {idx} | `{r.run_name}` | {fmt(r.best_accuracy)} | {fmt(r.latest_test_accuracy)} | {fmt(r.latest_train_accuracy)} | {fmt(gap)} | {fmt(r.latest_unique_active)} | {fmt(r.latest_recurrent_drive)} |"
        )

    lines += [
        "",
        "## Interpretation framework",
        "",
        "A variant is interesting if it improves test accuracy, improves learning speed, reduces the train/test gap, or demonstrates meaningful recurrent traversal without collapse. A higher training accuracy alone is not enough.",
        "",
        "### What would support the biological/plastic-graph thesis?",
        "",
        "1. The recurrent model beats the no-recurrence control or reaches the same accuracy with fewer active units.",
        "2. The recurrent model shows non-trivial recurrent drive and higher unique-active recruitment.",
        "3. The no-homeostasis variant has worse collapse, worse accuracy, or a larger generalization gap.",
        "4. The frozen-input variant underperforms the full model, suggesting that input-side plasticity is doing real work.",
        "5. The no-reward-modulation variant becomes less stable, less accurate, or overconfident.",
        "",
        "### What would weaken the thesis?",
        "",
        "If `no_recurrence_sparse_plastic_readout` performs essentially the same as the full recurrent model, then the current recurrent graph is not yet adding much. That would not kill the idea, but it would mean the next design needs stronger hidden-to-hidden dynamics, better recurrent credit assignment, or a task that requires multi-step traversal.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def plot_bar(results: list[RunResult], output_path: Path) -> None:
    if plt is None:
        return
    names = [r.run_name for r in results]
    values = [r.best_accuracy or 0.0 for r in results]
    plt.figure(figsize=(12, 6))
    plt.bar(range(len(names)), values)
    plt.xticks(range(len(names)), names, rotation=30, ha="right")
    plt.ylabel("Best test accuracy")
    plt.title("Best test accuracy by experiment variant")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    results = collect_results(args.db)
    if not results:
        raise SystemExit("No runs found")
    write_csv(results, args.output_dir / "suite_comparison.csv")
    write_markdown(results, args.output_dir / "suite_report.md")
    plot_bar(results, args.output_dir / "suite_best_accuracy.png")
    print(f"Wrote suite analysis to {args.output_dir}")


if __name__ == "__main__":
    main()
