from __future__ import annotations

from pathlib import Path
import sqlite3
import math

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def _safe_filename(s: str) -> str:
    return str(s).replace("/", "_").replace(" ", "_").replace(".", "p")


def _metric_pivot(metrics: pd.DataFrame) -> pd.DataFrame:
    idx = ["run_id", "run_name", "seed", "phase", "exposure_repeats", "context_bleed", "feedback_noise", "reward_delay_steps"]
    return metrics.pivot_table(index=idx, columns="metric", values="value", aggfunc="first").reset_index()


def _summary(wide: pd.DataFrame) -> pd.DataFrame:
    group = ["phase", "run_name", "context_bleed", "feedback_noise", "reward_delay_steps", "exposure_repeats"]
    rows = []
    metric_cols = [
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
    for keys, sub in wide.groupby(group, dropna=False):
        row = dict(zip(group, keys))
        row["n_seeds"] = int(sub["seed"].nunique())
        for col in metric_cols:
            if col in sub.columns:
                clean = pd.to_numeric(sub[col], errors="coerce")
                row[col.replace("/", "_") + "_mean"] = float(clean.mean())
                row[col.replace("/", "_") + "_std"] = float(clean.std(ddof=0))
        rows.append(row)
    return pd.DataFrame(rows)


def _baseline_summary(baselines: pd.DataFrame) -> pd.DataFrame:
    if baselines.empty:
        return pd.DataFrame()
    return baselines.groupby(["split", "baseline"], as_index=False).agg(
        accuracy_mean=("accuracy", "mean"), accuracy_std=("accuracy", "std"), n=("n", "first")
    ).sort_values(["split", "accuracy_mean"], ascending=[True, False])


def _route_summary(route: pd.DataFrame) -> pd.DataFrame:
    if route.empty:
        return pd.DataFrame()
    return route.groupby(["phase", "run_name", "context_bleed", "feedback_noise", "reward_delay_steps", "exposure_repeats"], as_index=False).agg(
        route_table_accuracy=("correct", "mean"),
        mean_target_rank=("target_rank", "mean"),
        mean_correct_margin=("correct_margin", "mean"),
        mean_context_margin=("context_margin", "mean"),
        mean_wrong_route_activation=("wrong_route_activation", "mean"),
    )


def _plot_line(summary: pd.DataFrame, phase: str, x_col: str, y_col: str, title: str, ylabel: str, output: Path, filter_delay: int | None = None):
    df = summary[summary["phase"] == phase].copy()
    if filter_delay is not None:
        df = df[df["reward_delay_steps"] == filter_delay]
    if df.empty or y_col not in df.columns:
        return
    plt.figure(figsize=(14, 6))
    for name, sub in df.groupby("run_name"):
        sub = sub.sort_values(x_col)
        plt.plot(sub[x_col], sub[y_col], marker="o", label=name)
    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel(ylabel)
    plt.legend(loc="best")
    plt.tight_layout()
    plt.savefig(output)
    plt.close()


def _plot_bar(summary: pd.DataFrame, y_col: str, title: str, ylabel: str, output: Path, phase: str | None = None):
    df = summary.copy()
    if phase is not None:
        df = df[df["phase"] == phase]
    if df.empty or y_col not in df.columns:
        return
    # Select clean points for a compact bar chart: no bleed/no noise/no delay where available.
    if "context_bleed" in df.columns:
        clean = df[(df["context_bleed"] == 0) & (df["feedback_noise"] == 0) & (df["reward_delay_steps"] == 0)]
        if not clean.empty:
            df = clean
    df = df.sort_values(y_col, ascending=False)
    plt.figure(figsize=(14, 6))
    plt.bar(df["run_name"], df[y_col])
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.savefig(output)
    plt.close()


def _plot_failure_taxonomy(predictions: pd.DataFrame, output: Path):
    comp = predictions[(predictions["split"] == "composition") & (predictions["correct"] == 0)].copy()
    if comp.empty:
        return
    # Summarize the most stressful setting for each phase: highest bleed for interference, highest noise+delay for feedback.
    rows = []
    for (phase, run_name), sub in comp.groupby(["phase", "run_name"]):
        if phase == "interference":
            sub = sub[sub["context_bleed"] == sub["context_bleed"].max()]
        elif phase == "feedback":
            sub = sub[(sub["feedback_noise"] == sub["feedback_noise"].max()) & (sub["reward_delay_steps"] == sub["reward_delay_steps"].max())]
        counts = sub["failure_type"].value_counts()
        for ft, c in counts.items():
            rows.append({"phase": phase, "run_name": run_name, "failure_type": ft, "count": int(c)})
    df = pd.DataFrame(rows)
    if df.empty:
        return
    pivot = df.pivot_table(index=["phase", "run_name"], columns="failure_type", values="count", fill_value=0)
    pivot.plot(kind="bar", stacked=True, figsize=(14, 6))
    plt.title("Experiment 9: composition failure taxonomy at strongest stress")
    plt.ylabel("count")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.savefig(output)
    plt.close()


def _heatmaps(route: pd.DataFrame, output_dir: Path):
    # Generate a few heatmaps for seed 0 full variant at highest interference and feedback stress.
    if route.empty:
        return
    candidates = []
    full_interference = route[(route["phase"] == "interference") & (route["run_name"] == "exp9_full_interference_robust") & (route["seed"] == route["seed"].min())]
    if not full_interference.empty:
        max_bleed = full_interference["context_bleed"].max()
        candidates.append(full_interference[full_interference["context_bleed"] == max_bleed])
    full_feedback = route[(route["phase"] == "feedback") & (route["run_name"] == "exp9_full_reward_robust") & (route["seed"] == route["seed"].min())]
    if not full_feedback.empty:
        max_noise = full_feedback["feedback_noise"].max()
        max_delay = full_feedback["reward_delay_steps"].max()
        candidates.append(full_feedback[(full_feedback["feedback_noise"] == max_noise) & (full_feedback["reward_delay_steps"] == max_delay)])
    for cand in candidates:
        if cand.empty:
            continue
        meta = cand.iloc[0]
        for mode, sub in cand.groupby("mode"):
            pivot = sub.pivot_table(index="source", columns="true_target", values="correct_margin", aggfunc="mean", fill_value=0)
            plt.figure(figsize=(10, 8))
            plt.imshow(pivot.values, aspect="auto")
            plt.colorbar(label="correct target margin")
            plt.title(
                f"Route-field margin: {meta['run_name']}, phase={meta['phase']}, mode={mode}, "
                f"bleed={meta['context_bleed']}, noise={meta['feedback_noise']}, delay={meta['reward_delay_steps']}"
            )
            plt.xlabel("true_target")
            plt.ylabel("source")
            plt.xticks(range(len(pivot.columns)), pivot.columns, rotation=90)
            plt.yticks(range(len(pivot.index)), pivot.index)
            plt.tight_layout()
            name = f"route_margin_heatmap_{_safe_filename(meta['phase'])}_{_safe_filename(meta['run_name'])}_{mode}.png"
            plt.savefig(output_dir / name)
            plt.close()


def _write_report(summary: pd.DataFrame, baselines: pd.DataFrame, route_summary: pd.DataFrame, output_dir: Path):
    lines = []
    lines.append("# Experiment 9 Analysis - Robust Adaptive Route Plasticity\n")
    lines.append("Experiment 9 stresses the self-organizing route acquisition mechanism discovered in Experiment 8. It asks two questions: whether inhibition protects context-bound routes under interference, and whether reward gating / eligibility traces protect route acquisition under noisy or delayed feedback.\n")
    if not summary.empty:
        lines.append("## Variant summary\n")
        display_cols = [c for c in [
            "phase", "run_name", "context_bleed", "feedback_noise", "reward_delay_steps", "exposure_repeats",
            "transition_accuracy_mean", "transition_accuracy_std", "composition_accuracy_mean", "composition_accuracy_std",
            "composition_mean_target_rank_mean", "composition_mean_correct_margin_mean", "composition_mean_context_margin_mean",
            "composition_mean_wrong_route_activation_mean", "route_table_accuracy_mean", "n_seeds",
        ] if c in summary.columns]
        lines.append(summary[display_cols].sort_values(["phase", "context_bleed", "feedback_noise", "reward_delay_steps", "run_name"]).to_markdown(index=False))
        lines.append("\n")
    if not baselines.empty:
        lines.append("## Deterministic baselines\n")
        lines.append(baselines.to_markdown(index=False))
        lines.append("\n")
    if not route_summary.empty:
        lines.append("## Route-field diagnostics\n")
        lines.append(route_summary.sort_values(["phase", "context_bleed", "feedback_noise", "reward_delay_steps", "run_name"]).to_markdown(index=False))
        lines.append("\n")
    lines.append("## Interpretation guide\n")
    lines.append("- `transition_accuracy`: local one-step route acquisition.\n")
    lines.append("- `composition_accuracy`: unseen multi-step recurrent traversal from the learned route field.\n")
    lines.append("- `context_bleed`: competing mode assemblies injected into the active context; this should stress inhibition.\n")
    lines.append("- `feedback_noise`: probability that a transition target is corrupted during training; this should stress reward gating.\n")
    lines.append("- `reward_delay_steps`: feedback delay in the one-step stream; this should stress eligibility traces.\n")
    lines.append("- `mean_correct_margin`: target score minus strongest wrong target.\n")
    lines.append("- `mean_context_margin`: correct-mode support minus strongest wrong-mode support for the same target.\n")
    lines.append("- `mean_wrong_route_activation`: bounded proxy for competing route activation.\n")
    (output_dir / "exp9_report.md").write_text("\n".join(lines), encoding="utf-8")


def analyze(db_path: Path, output_dir: Path) -> None:
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

    wide = _metric_pivot(metrics)
    summary = _summary(wide)
    baseline_summary = _baseline_summary(baselines)
    rsummary = _route_summary(route)
    wide.to_csv(output_dir / "metrics_wide.csv", index=False)
    summary.to_csv(output_dir / "exp9_summary.csv", index=False)
    baseline_summary.to_csv(output_dir / "exp9_baseline_summary.csv", index=False)
    rsummary.to_csv(output_dir / "exp9_route_summary.csv", index=False)

    _plot_bar(summary, "composition_accuracy_mean", "Experiment 9: clean-point composition accuracy", "accuracy", output_dir / "exp9_clean_composition_accuracy.png")
    _plot_bar(summary, "transition_accuracy_mean", "Experiment 9: clean-point transition accuracy", "accuracy", output_dir / "exp9_clean_transition_accuracy.png")

    _plot_line(summary, "interference", "context_bleed", "composition_accuracy_mean", "Experiment 9A: composition accuracy under context bleed", "composition accuracy", output_dir / "exp9_interference_composition_by_bleed.png")
    _plot_line(summary, "interference", "context_bleed", "composition_mean_correct_margin_mean", "Experiment 9A: correct-route margin under context bleed", "correct margin", output_dir / "exp9_interference_margin_by_bleed.png")
    _plot_line(summary, "interference", "context_bleed", "composition_mean_wrong_route_activation_mean", "Experiment 9A: wrong-route activation under context bleed", "wrong-route activation", output_dir / "exp9_interference_wrong_route_by_bleed.png")
    _plot_line(summary, "interference", "context_bleed", "route_table_accuracy_mean", "Experiment 9A: route-table accuracy under context bleed", "route-table accuracy", output_dir / "exp9_interference_route_table_by_bleed.png")

    for delay in sorted(summary[summary["phase"] == "feedback"]["reward_delay_steps"].dropna().unique()):
        _plot_line(summary, "feedback", "feedback_noise", "composition_accuracy_mean", f"Experiment 9B: composition under feedback noise, delay={int(delay)}", "composition accuracy", output_dir / f"exp9_feedback_composition_noise_delay_{int(delay)}.png", filter_delay=int(delay))
        _plot_line(summary, "feedback", "feedback_noise", "route_table_accuracy_mean", f"Experiment 9B: route-table under feedback noise, delay={int(delay)}", "route-table accuracy", output_dir / f"exp9_feedback_route_table_noise_delay_{int(delay)}.png", filter_delay=int(delay))
        _plot_line(summary, "feedback", "feedback_noise", "composition_mean_correct_margin_mean", f"Experiment 9B: correct margin under feedback noise, delay={int(delay)}", "correct margin", output_dir / f"exp9_feedback_margin_noise_delay_{int(delay)}.png", filter_delay=int(delay))

    _plot_failure_taxonomy(predictions, output_dir / "exp9_failure_taxonomy.png")
    _heatmaps(route, output_dir)
    _write_report(summary, baseline_summary, rsummary, output_dir)


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--db", default="runs/exp9_robust_adaptive_route_plasticity.sqlite3")
    p.add_argument("--output-dir", default="analysis/exp9")
    args = p.parse_args()
    analyze(Path(args.db), Path(args.output_dir))
