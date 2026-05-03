from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine, text


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze Experiment 4 successor traversal suite.")
    parser.add_argument("--db", type=Path, default=Path("runs/exp4_successor_suite.sqlite3"))
    parser.add_argument("--output-dir", type=Path, default=Path("analysis/exp4"))
    return parser.parse_args()


def load_tables(db: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    engine = create_engine(f"sqlite:///{db}", future=True)
    runs = pd.read_sql("select * from experiment_runs", engine)
    metrics = pd.read_sql("select * from metric_records", engine)
    return runs, metrics


def pivot_latest(metrics: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for (run_id, split, name), group in metrics.groupby(["run_id", "split", "name"]):
        latest = group.sort_values("step").iloc[-1]
        rows.append({"run_id": run_id, "metric": f"{split}/{name}", "value": latest["value"]})
    if not rows:
        return pd.DataFrame()
    return pd.DataFrame(rows).pivot(index="run_id", columns="metric", values="value").reset_index()


def best_metric(metrics: pd.DataFrame, split: str, name: str) -> pd.DataFrame:
    filtered = metrics[(metrics["split"] == split) & (metrics["name"] == name)]
    if filtered.empty:
        return pd.DataFrame(columns=["run_id", f"best_{split}_{name}"])
    return filtered.groupby("run_id")["value"].max().reset_index().rename(columns={"value": f"best_{split}_{name}"})


def plot_bar(df: pd.DataFrame, x: str, y: str, title: str, output: Path) -> None:
    plt.figure(figsize=(14, 6))
    plt.bar(df[x], df[y])
    plt.title(title)
    plt.ylabel(y)
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(output, dpi=150)
    plt.close()


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    runs, metrics = load_tables(args.db)
    latest = pivot_latest(metrics)
    best_addition = best_metric(metrics, "addition", "accuracy")
    best_transition = best_metric(metrics, "transition", "accuracy")
    summary = runs[["id", "run_name", "status", "best_accuracy"]].rename(columns={"id": "run_id"})
    summary = summary.merge(best_addition, on="run_id", how="left").merge(best_transition, on="run_id", how="left").merge(latest, on="run_id", how="left")
    summary = summary.sort_values("best_addition_accuracy", ascending=False)
    summary.to_csv(args.output_dir / "exp4_comparison.csv", index=False)

    if not summary.empty:
        plot_bar(summary, "run_name", "best_addition_accuracy", "Experiment 4: best compositional addition accuracy", args.output_dir / "exp4_best_addition_accuracy.png")
        if "addition/average_recurrent_drive" in summary.columns:
            plot_bar(summary, "run_name", "addition/average_recurrent_drive", "Experiment 4: latest recurrent drive", args.output_dir / "exp4_recurrent_drive.png")
        if "addition/average_unique_active" in summary.columns:
            plot_bar(summary, "run_name", "addition/average_unique_active", "Experiment 4: latest unique active units", args.output_dir / "exp4_unique_active.png")

    report = [
        "# Experiment 4 Analysis — Successor Traversal",
        "",
        "This experiment asks a sharper question than MNIST: can a recurrent plastic graph learn a local successor transition and compose it repeatedly to solve addition-like tasks it was not directly trained on?",
        "",
        "## Summary table",
        "",
        summary.to_markdown(index=False),
        "",
        "## Interpretation framework",
        "",
        "A strong result would show `exp4_full_traversal` beating `exp4_no_recurrence` on multi-step addition, not merely matching it on one-step transitions.",
        "",
        "Key things to inspect:",
        "",
        "- `best_addition_accuracy`: whether traversal composes beyond single-step memory.",
        "- `addition/accuracy_steps_2+`: whether performance degrades gracefully with path length.",
        "- `addition/average_recurrent_drive`: whether recurrent edges are functionally active.",
        "- `addition/average_unique_active`: whether recurrence recruits additional assemblies rather than collapsing.",
        "- `exp4_no_structural_plasticity`: tests whether edge rewiring/growth is load-bearing.",
        "- `exp4_no_homeostasis`: tests whether activity regulation prevents runaway spread.",
        "",
    ]
    (args.output_dir / "exp4_report.md").write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote analysis to {args.output_dir}")


if __name__ == "__main__":
    main()
