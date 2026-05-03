from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def _pivot_metrics(metrics: pd.DataFrame) -> pd.DataFrame:
    if metrics.empty:
        return pd.DataFrame()
    return metrics.pivot_table(
        index=["run_name", "seed", "phase", "exposure_repeats"],
        columns="metric",
        values="value",
        aggfunc="first",
    ).reset_index()


def _safe_metric(df: pd.DataFrame, name: str) -> pd.Series:
    if name in df.columns:
        return df[name]
    return pd.Series([np.nan] * len(df), index=df.index)


def _summarize(metrics_wide: pd.DataFrame) -> pd.DataFrame:
    if metrics_wide.empty:
        return pd.DataFrame()
    group_cols = ["run_name", "phase", "exposure_repeats"]
    wanted = [
        "transition/accuracy",
        "composition/accuracy",
        "composition/mean_target_rank",
        "composition/mean_correct_margin",
        "composition/mean_context_margin",
        "composition/mean_wrong_route_activation",
        "route_table/accuracy",
        "route_table/mean_target_rank",
        "route_table/mean_correct_margin",
        "route_table/mean_context_margin",
        "route_table/mean_wrong_route_activation",
    ]
    rows = []
    for key, g in metrics_wide.groupby(group_cols):
        base = dict(zip(group_cols, key))
        for metric in wanted:
            if metric in g.columns:
                vals = g[metric].dropna()
                base[metric.replace("/", "_") + "_mean"] = float(vals.mean()) if len(vals) else np.nan
                base[metric.replace("/", "_") + "_std"] = float(vals.std(ddof=0)) if len(vals) else np.nan
        base["n_seeds"] = int(g["seed"].nunique())
        rows.append(base)
    return pd.DataFrame(rows).sort_values(["exposure_repeats", "run_name"])


def _baseline_summary(baselines: pd.DataFrame) -> pd.DataFrame:
    if baselines.empty:
        return pd.DataFrame()
    return (
        baselines.groupby(["split", "baseline"], as_index=False)
        .agg(accuracy_mean=("accuracy", "mean"), accuracy_std=("accuracy", "std"), n=("n", "first"))
        .sort_values(["split", "accuracy_mean"], ascending=[True, False])
    )


def _route_summary(route: pd.DataFrame) -> pd.DataFrame:
    if route.empty:
        return pd.DataFrame()
    return (
        route.groupby(["run_name", "phase", "exposure_repeats"], as_index=False)
        .agg(
            route_table_accuracy=("correct", "mean"),
            mean_target_rank=("target_rank", "mean"),
            mean_correct_margin=("correct_margin", "mean"),
            mean_context_margin=("context_margin", "mean"),
            mean_wrong_route_activation=("wrong_route_activation", "mean"),
        )
        .sort_values(["exposure_repeats", "route_table_accuracy"], ascending=[True, False])
    )


def _plot_bar(summary: pd.DataFrame, metric: str, title: str, ylabel: str, path: Path, exposure: int | None = None) -> None:
    if summary.empty or metric not in summary.columns:
        return
    df = summary if exposure is None else summary[summary["exposure_repeats"] == exposure]
    if df.empty:
        return
    df = df.sort_values(metric, ascending=False)
    plt.figure(figsize=(14, 5))
    plt.bar(df["run_name"].astype(str), df[metric])
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel("run_name")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def _plot_exposure(summary: pd.DataFrame, metric: str, title: str, ylabel: str, path: Path) -> None:
    if summary.empty or metric not in summary.columns:
        return
    plt.figure(figsize=(14, 5))
    for run_name, g in summary.groupby("run_name"):
        g = g.sort_values("exposure_repeats")
        plt.plot(g["exposure_repeats"], g[metric], marker="o", label=run_name)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel("transition exposure repeats")
    plt.legend(loc="best")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def _plot_accuracy_by_steps(predictions: pd.DataFrame, path: Path, exposure: int | None = None) -> None:
    if predictions.empty:
        return
    df = predictions[predictions["split"] == "composition"].copy()
    if exposure is not None:
        df = df[df["exposure_repeats"] == exposure]
    if df.empty:
        return
    acc = df.groupby(["run_name", "steps"], as_index=False)["correct"].mean()
    plt.figure(figsize=(14, 5))
    for run_name, g in acc.groupby("run_name"):
        g = g.sort_values("steps")
        plt.plot(g["steps"], g["correct"], marker="o", label=run_name)
    plt.title("Experiment 8: composition accuracy by path length")
    plt.ylabel("accuracy")
    plt.xlabel("composition steps")
    plt.legend(loc="best")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def _plot_accuracy_by_mode(predictions: pd.DataFrame, path: Path, exposure: int | None = None) -> None:
    if predictions.empty:
        return
    df = predictions[predictions["split"] == "composition"].copy()
    if exposure is not None:
        df = df[df["exposure_repeats"] == exposure]
    if df.empty:
        return
    acc = df.groupby(["run_name", "mode"], as_index=False)["correct"].mean()
    pivot = acc.pivot(index="run_name", columns="mode", values="correct").fillna(0)
    pivot = pivot.sort_index()
    ax = pivot.plot(kind="bar", figsize=(14, 5))
    ax.set_title("Experiment 8: composition accuracy by mode")
    ax.set_ylabel("accuracy")
    ax.set_xlabel("run_name")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def _plot_failure_types(predictions: pd.DataFrame, path: Path, exposure: int | None = None) -> None:
    if predictions.empty:
        return
    df = predictions[(predictions["split"] == "composition") & (predictions["correct"] == 0)].copy()
    if exposure is not None:
        df = df[df["exposure_repeats"] == exposure]
    if df.empty:
        return
    counts = df.groupby(["run_name", "failure_type"]).size().reset_index(name="count")
    pivot = counts.pivot(index="run_name", columns="failure_type", values="count").fillna(0)
    ax = pivot.plot(kind="bar", stacked=True, figsize=(14, 5))
    ax.set_title("Experiment 8: composition failure taxonomy")
    ax.set_ylabel("count")
    ax.set_xlabel("run_name")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def _plot_route_heatmaps(route: pd.DataFrame, output_dir: Path) -> None:
    if route.empty:
        return
    # Create a few diagnostic heatmaps for the full model, first exposure, first seed.
    candidates = route[route["run_name"] == "exp8_full_self_organizing_route_field"]
    if candidates.empty:
        candidates = route
    exposure = int(candidates["exposure_repeats"].min())
    seed = int(candidates[candidates["exposure_repeats"] == exposure]["seed"].min())
    subset = candidates[(candidates["exposure_repeats"] == exposure) & (candidates["seed"] == seed)]
    run_name = subset["run_name"].iloc[0] if not subset.empty else "unknown"
    for mode, g in subset.groupby("mode"):
        if g.empty:
            continue
        sources = sorted(g["source"].unique())
        targets = sorted(g["true_target"].unique())
        mat = np.zeros((len(sources), len(targets)))
        sidx = {s: i for i, s in enumerate(sources)}
        tidx = {t: i for i, t in enumerate(targets)}
        for _, row in g.iterrows():
            mat[sidx[row["source"]], tidx[row["true_target"]]] = row["correct_margin"]
        plt.figure(figsize=(9, 7))
        plt.imshow(mat, aspect="auto")
        plt.colorbar(label="correct target margin")
        plt.title(f"Route-field margin: {run_name}, seed={seed}, mode={mode}, exposure={exposure}")
        plt.xlabel("true target")
        plt.ylabel("source")
        plt.xticks(range(len(targets)), targets, rotation=90)
        plt.yticks(range(len(sources)), sources)
        plt.tight_layout()
        plt.savefig(output_dir / f"route_margin_heatmap_{run_name}_seed{seed}_{mode}_exp{exposure}.png")
        plt.close()


def _write_report(output_dir: Path, summary: pd.DataFrame, baseline_summary: pd.DataFrame, route_summary_df: pd.DataFrame) -> None:
    lines = []
    lines.append("# Experiment 8 Analysis - Self-Organizing Contextual Route Acquisition\n")
    lines.append("Experiment 8 tests whether a local plastic graph can acquire a context-conditioned route field from one-step transition experience, then compose unseen multi-step traversals recurrently.\n")
    if not summary.empty:
        lines.append("## Variant summary\n")
        display_cols = [c for c in [
            "run_name", "exposure_repeats", "transition_accuracy_mean", "transition_accuracy_std",
            "composition_accuracy_mean", "composition_accuracy_std", "composition_mean_target_rank_mean",
            "composition_mean_correct_margin_mean", "composition_mean_context_margin_mean",
            "composition_mean_wrong_route_activation_mean", "route_table_accuracy_mean", "n_seeds",
        ] if c in summary.columns]
        lines.append(summary[display_cols].to_markdown(index=False))
        lines.append("\n")
    if not baseline_summary.empty:
        lines.append("## Deterministic baselines\n")
        lines.append(baseline_summary.to_markdown(index=False))
        lines.append("\n")
    if not route_summary_df.empty:
        lines.append("## Route-field diagnostics\n")
        lines.append(route_summary_df.to_markdown(index=False))
        lines.append("\n")
    lines.append("## Interpretation guide\n")
    lines.append("- `transition_accuracy`: one-step transition learning.\n")
    lines.append("- `composition_accuracy`: unseen multi-step recurrent traversal.\n")
    lines.append("- `route_table_accuracy`: direct inspection of the learned local route field.\n")
    lines.append("- `mean_target_rank`: whether the target is near the top even when argmax is wrong.\n")
    lines.append("- `mean_correct_margin`: target score minus strongest wrong target.\n")
    lines.append("- `mean_context_margin`: correct mode support minus strongest wrong-mode support for the same target.\n")
    lines.append("- `mean_wrong_route_activation`: bounded proxy for competing route activation.\n")
    lines.append("- failure taxonomy distinguishes first-step failures from mid-route drift and no-recurrence single-step failures.\n")
    (output_dir / "exp8_report.md").write_text("\n".join(lines), encoding="utf-8")


def analyze(db_path: Path | str, output_dir: Path | str) -> None:
    db_path = Path(db_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    runs = pd.read_sql_query("SELECT * FROM runs", conn)
    metrics = pd.read_sql_query("SELECT * FROM metrics", conn)
    predictions = pd.read_sql_query("SELECT * FROM predictions", conn)
    route = pd.read_sql_query("SELECT * FROM route_diagnostics", conn)
    baselines = pd.read_sql_query("SELECT * FROM baselines", conn)
    conn.close()

    runs.to_csv(output_dir / "runs.csv", index=False)
    metrics.to_csv(output_dir / "metrics.csv", index=False)
    predictions.to_csv(output_dir / "predictions.csv", index=False)
    route.to_csv(output_dir / "route_diagnostics.csv", index=False)
    baselines.to_csv(output_dir / "baselines.csv", index=False)

    wide = _pivot_metrics(metrics)
    wide.to_csv(output_dir / "metrics_wide.csv", index=False)
    summary = _summarize(wide)
    summary.to_csv(output_dir / "exp8_summary.csv", index=False)
    baseline_summary = _baseline_summary(baselines)
    baseline_summary.to_csv(output_dir / "exp8_baseline_summary.csv", index=False)
    route_summary_df = _route_summary(route)
    route_summary_df.to_csv(output_dir / "exp8_route_summary.csv", index=False)

    exposure = int(summary["exposure_repeats"].min()) if not summary.empty else None
    _plot_bar(summary, "composition_accuracy_mean", "Experiment 8: mean composition accuracy", "accuracy", output_dir / "exp8_composition_accuracy.png", exposure)
    _plot_bar(summary, "transition_accuracy_mean", "Experiment 8: mean transition accuracy", "accuracy", output_dir / "exp8_transition_accuracy.png", exposure)
    _plot_bar(summary, "composition_mean_target_rank_mean", "Experiment 8: mean target rank during composition", "rank; lower is better", output_dir / "exp8_target_rank.png", exposure)
    _plot_bar(summary, "composition_mean_correct_margin_mean", "Experiment 8: correct-route margin", "margin", output_dir / "exp8_correct_margin.png", exposure)
    _plot_bar(summary, "composition_mean_context_margin_mean", "Experiment 8: context margin", "margin", output_dir / "exp8_context_margin.png", exposure)
    _plot_exposure(summary, "composition_accuracy_mean", "Experiment 8: exposure curve - composition accuracy", "accuracy", output_dir / "exp8_exposure_curve_composition.png")
    _plot_exposure(summary, "route_table_accuracy_mean", "Experiment 8: exposure curve - route table accuracy", "accuracy", output_dir / "exp8_exposure_curve_route_table.png")
    _plot_exposure(summary, "composition_mean_correct_margin_mean", "Experiment 8: exposure curve - correct margin", "margin", output_dir / "exp8_exposure_curve_margin.png")
    _plot_accuracy_by_steps(predictions, output_dir / "exp8_accuracy_by_steps.png", exposure)
    _plot_accuracy_by_mode(predictions, output_dir / "exp8_accuracy_by_mode.png", exposure)
    _plot_failure_types(predictions, output_dir / "exp8_failure_taxonomy.png", exposure)
    _plot_route_heatmaps(route, output_dir)
    _write_report(output_dir, summary, baseline_summary, route_summary_df)


def main() -> None:
    p = argparse.ArgumentParser(description="Analyze Experiment 8 SQLite results.")
    p.add_argument("--db", default="runs/exp8_self_organizing_route_acquisition.sqlite3")
    p.add_argument("--output-dir", default="analysis/exp8")
    args = p.parse_args()
    analyze(args.db, args.output_dir)


if __name__ == "__main__":
    main()
