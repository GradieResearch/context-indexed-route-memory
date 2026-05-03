from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze Experiment 7 route-field diagnostic suite.")
    parser.add_argument("--db", default="runs/exp7_route_field_diagnostics.sqlite3", help="SQLite DB from run_exp7_suite.py")
    parser.add_argument("--output-dir", default="analysis/exp7", help="Output directory for report and figures")
    return parser.parse_args()


def read_table(conn: sqlite3.Connection, table: str) -> pd.DataFrame:
    return pd.read_sql_query(f"SELECT * FROM {table}", conn)


def metric_wide(metrics: pd.DataFrame, runs: pd.DataFrame) -> pd.DataFrame:
    merged = metrics.merge(runs[["run_id", "run_name", "seed"]], on="run_id", how="left")
    return merged.pivot_table(index=["run_name", "seed"], columns="metric", values="value", aggfunc="first").reset_index()


def save_bar(df: pd.DataFrame, x: str, y: str, title: str, output: Path, ylabel: str | None = None) -> None:
    plt.figure(figsize=(14, 6))
    plt.bar(df[x].astype(str), df[y])
    plt.xticks(rotation=30, ha="right")
    plt.ylabel(ylabel or y)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(output, dpi=160)
    plt.close()


def save_line_by_steps(predictions: pd.DataFrame, output: Path) -> None:
    comp = predictions[predictions["split"] == "composition"].copy()
    grouped = comp.groupby(["run_name", "steps"], as_index=False)["correct"].mean()
    plt.figure(figsize=(14, 6))
    for run_name, g in grouped.groupby("run_name"):
        plt.plot(g["steps"], g["correct"], marker="o", label=run_name)
    plt.xlabel("composition steps")
    plt.ylabel("accuracy")
    plt.ylim(0, 1.05)
    plt.title("Experiment 7: composition accuracy by path length")
    plt.legend(loc="best")
    plt.tight_layout()
    plt.savefig(output, dpi=160)
    plt.close()


def save_mode_bars(predictions: pd.DataFrame, output: Path) -> None:
    comp = predictions[predictions["split"] == "composition"].copy()
    grouped = comp.groupby(["run_name", "mode"], as_index=False)["correct"].mean()
    pivot = grouped.pivot(index="run_name", columns="mode", values="correct").fillna(0)
    ax = pivot.plot(kind="bar", figsize=(14, 6))
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("accuracy")
    ax.set_title("Experiment 7: composition accuracy by mode")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(output, dpi=160)
    plt.close()


def save_route_heatmap(route_diag: pd.DataFrame, run_name: str, seed: int, output: Path) -> None:
    subset = route_diag[(route_diag["run_name"] == run_name) & (route_diag["seed"] == seed)].copy()
    if subset.empty:
        return
    for mode, g in subset.groupby("mode"):
        pivot = g.pivot(index="source", columns="true_target", values="correct_margin").fillna(0.0)
        plt.figure(figsize=(8, 6))
        plt.imshow(pivot.values, aspect="auto")
        plt.colorbar(label="correct target margin")
        plt.xticks(range(len(pivot.columns)), pivot.columns)
        plt.yticks(range(len(pivot.index)), pivot.index)
        plt.xlabel("true target")
        plt.ylabel("source")
        plt.title(f"Route-field margin: {run_name}, seed={seed}, mode={mode}")
        plt.tight_layout()
        plt.savefig(output / f"route_margin_heatmap_{run_name}_seed{seed}_{mode}.png", dpi=160)
        plt.close()


def write_report(
    output_dir: Path,
    summary: pd.DataFrame,
    baseline_summary: pd.DataFrame,
    route_summary: pd.DataFrame,
    predictions: pd.DataFrame,
) -> None:
    report_path = output_dir / "exp7_report.md"
    comp = predictions[predictions["split"] == "composition"].copy()
    transition = predictions[predictions["split"] == "transition"].copy()

    lines = []
    lines.append("# Experiment 7 Analysis - Route Field Diagnostics")
    lines.append("")
    lines.append("Experiment 7 is a diagnostic follow-up to the contextual successor problem. It does not try to make the task harder. It tries to expose exactly where contextual traversal succeeds or breaks: one-step transition learning, recurrent composition, context-conditioned route binding, final-state prediction, or route-field purity.")
    lines.append("")
    lines.append("## Variant summary")
    lines.append("")
    lines.append(summary.to_markdown(index=False, floatfmt=".4f"))
    lines.append("")
    lines.append("## Deterministic baselines")
    lines.append("")
    lines.append(baseline_summary.to_markdown(index=False, floatfmt=".4f"))
    lines.append("")
    lines.append("## Route-field diagnostics")
    lines.append("")
    lines.append(route_summary.to_markdown(index=False, floatfmt=".4f"))
    lines.append("")
    lines.append("## Interpretation guide")
    lines.append("")
    lines.append("- `transition_accuracy` shows whether the local one-step route table was learned.")
    lines.append("- `composition_accuracy` shows whether repeated recurrent traversal works after local route learning.")
    lines.append("- `mean_target_rank` tells whether the true next state is near the top even when argmax is wrong.")
    lines.append("- `mean_correct_margin` is the true next state's score minus the strongest wrong target score.")
    lines.append("- `mean_context_margin` is the correct mode's support for the true target minus the strongest wrong mode's support for that same target.")
    lines.append("- `mean_wrong_route_activation` is a bounded proxy for whether competing mode routes remain active.")
    lines.append("")
    lines.append("## Generated figures")
    lines.append("")
    for fig in sorted(output_dir.glob("*.png")):
        lines.append(f"- `{fig.name}`")
    lines.append("")
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(args.db)
    runs = read_table(conn, "runs")
    metrics = read_table(conn, "metrics")
    predictions = read_table(conn, "predictions")
    route_diag = read_table(conn, "route_diagnostics")
    baselines = read_table(conn, "baselines")
    conn.close()

    wide = metric_wide(metrics, runs)
    summary = wide.groupby("run_name", as_index=False).agg(
        transition_accuracy=("transition/accuracy", "mean"),
        transition_accuracy_std=("transition/accuracy", "std"),
        composition_accuracy=("composition/accuracy", "mean"),
        composition_accuracy_std=("composition/accuracy", "std"),
        mean_target_rank=("composition/average_target_rank", "mean"),
        mean_correct_margin=("composition/average_correct_margin", "mean"),
        mean_context_margin=("composition/average_context_margin", "mean"),
        mean_wrong_route_activation=("composition/average_wrong_route_activation", "mean"),
    ).sort_values("composition_accuracy", ascending=False)

    baseline_summary = baselines.groupby(["split", "baseline"], as_index=False).agg(
        accuracy=("accuracy", "mean"),
        accuracy_std=("accuracy", "std"),
        n=("n", "first"),
    ).sort_values(["split", "accuracy"], ascending=[True, False])

    route_summary = route_diag.groupby("run_name", as_index=False).agg(
        route_table_accuracy=("correct", "mean"),
        mean_target_rank=("target_rank", "mean"),
        mean_correct_margin=("correct_margin", "mean"),
        mean_context_margin=("context_margin", "mean"),
        mean_wrong_route_activation=("wrong_route_activation", "mean"),
    ).sort_values("route_table_accuracy", ascending=False)

    summary.to_csv(output_dir / "exp7_summary.csv", index=False)
    baseline_summary.to_csv(output_dir / "exp7_baseline_summary.csv", index=False)
    route_summary.to_csv(output_dir / "exp7_route_summary.csv", index=False)

    save_bar(summary, "run_name", "composition_accuracy", "Experiment 7: mean composition accuracy", output_dir / "exp7_composition_accuracy.png", "accuracy")
    save_bar(summary, "run_name", "transition_accuracy", "Experiment 7: mean transition accuracy", output_dir / "exp7_transition_accuracy.png", "accuracy")
    save_bar(summary, "run_name", "mean_target_rank", "Experiment 7: mean target rank during composition", output_dir / "exp7_target_rank.png", "rank; lower is better")
    save_bar(summary, "run_name", "mean_correct_margin", "Experiment 7: correct-route margin", output_dir / "exp7_correct_margin.png", "margin")
    save_bar(route_summary, "run_name", "mean_context_margin", "Experiment 7: route-field context margin", output_dir / "exp7_context_margin.png", "margin")
    save_line_by_steps(predictions, output_dir / "exp7_accuracy_by_steps.png")
    save_mode_bars(predictions, output_dir / "exp7_accuracy_by_mode.png")

    if not summary.empty:
        best = summary.iloc[0]["run_name"]
        first_seed = int(runs[runs["run_name"] == best]["seed"].min())
        save_route_heatmap(route_diag, best, first_seed, output_dir)

    write_report(output_dir, summary, baseline_summary, route_summary, predictions)
    print(f"Wrote analysis to {output_dir}")


if __name__ == "__main__":
    main()
