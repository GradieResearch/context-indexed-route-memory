from __future__ import annotations

from pathlib import Path
import math

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def _metric_wide(metrics: pd.DataFrame) -> pd.DataFrame:
    if metrics.empty:
        return pd.DataFrame()
    keys = ["run_name", "seed", "phase", "checkpoint", "eval_rule", "feedback_noise", "reward_delay_steps"]
    return metrics.pivot_table(index=keys, columns="metric", values="value", aggfunc="mean").reset_index()


def _save_plot(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()


def _plot_line(summary: pd.DataFrame, metric: str, title: str, path: Path, phase_contains: str, eval_rule: str | None = None) -> None:
    df = summary[summary["phase"].str.contains(phase_contains, regex=False)].copy()
    if eval_rule is not None:
        df = df[df["eval_rule"] == eval_rule]
    if df.empty or metric not in df.columns:
        return
    plt.figure(figsize=(14, 6))
    for run_name, sub in df.groupby("run_name"):
        sub = sub.sort_values("checkpoint")
        plt.plot(sub["checkpoint"], sub[metric], marker="o", label=run_name)
    plt.xlabel("exposures after phase start")
    plt.ylabel(metric)
    plt.title(title)
    plt.ylim(-0.05, 1.05 if "accuracy" in metric else None)
    plt.legend(fontsize=8)
    _save_plot(path)


def _plot_dual_rule(summary: pd.DataFrame, metric: str, title: str, path: Path, phase_contains: str) -> None:
    df = summary[summary["phase"].str.contains(phase_contains, regex=False)].copy()
    if df.empty or metric not in df.columns:
        return
    plt.figure(figsize=(14, 6))
    for (run_name, eval_rule), sub in df.groupby(["run_name", "eval_rule"]):
        sub = sub.sort_values("checkpoint")
        linestyle = "-" if eval_rule == "B" else "--"
        plt.plot(sub["checkpoint"], sub[metric], marker="o", linestyle=linestyle, label=f"{run_name} / rule {eval_rule}")
    plt.xlabel("exposures after phase start")
    plt.ylabel(metric)
    plt.title(title)
    plt.ylim(-0.05, 1.05 if "accuracy" in metric else None)
    plt.legend(fontsize=7, ncol=2)
    _save_plot(path)


def _plot_bar(clean: pd.DataFrame, metric: str, title: str, path: Path) -> None:
    if clean.empty or metric not in clean.columns:
        return
    df = clean.copy().sort_values(metric, ascending=False)
    plt.figure(figsize=(13, 5))
    plt.bar(df["run_name"], df[metric])
    plt.xticks(rotation=35, ha="right")
    plt.ylabel(metric)
    plt.title(title)
    _save_plot(path)


def _heatmap(route: pd.DataFrame, out_dir: Path, run_name: str, phase: str, checkpoint: int, eval_rule: str, mode: str) -> None:
    df = route[(route["run_name"] == run_name) & (route["seed"] == route["seed"].min()) & (route["phase"] == phase) & (route["checkpoint"] == checkpoint) & (route["eval_rule"] == eval_rule) & (route["mode"] == mode)].copy()
    if df.empty:
        return
    pivot = df.pivot_table(index="source", columns="true_target", values="correct_margin", aggfunc="mean")
    plt.figure(figsize=(9, 7))
    plt.imshow(pivot.values, aspect="auto", origin="upper")
    plt.colorbar(label="correct target margin")
    plt.xticks(range(len(pivot.columns)), [str(c) for c in pivot.columns], rotation=90)
    plt.yticks(range(len(pivot.index)), [str(i) for i in pivot.index])
    plt.xlabel("true target")
    plt.ylabel("source")
    plt.title(f"Route-field margin: {run_name}, {phase}, rule={eval_rule}, mode={mode}, ckpt={checkpoint}")
    name = f"route_margin_heatmap_{phase}_{run_name}_{eval_rule}_{mode}_ckpt{checkpoint}.png".replace("/", "_")
    _save_plot(out_dir / name)


def _thresholds(summary: pd.DataFrame) -> pd.DataFrame:
    rows = []
    rev = summary[summary["phase"].str.contains("reversal", regex=False)].copy()
    if rev.empty:
        return pd.DataFrame()
    for (run_name, seed, eval_rule), sub in rev.groupby(["run_name", "seed", "eval_rule"]):
        sub = sub.sort_values("checkpoint")
        comp = "composition/accuracy"
        if comp not in sub.columns:
            continue
        final = float(sub[comp].iloc[-1])
        threshold_50 = 0.5 * final
        threshold_80 = 0.8
        c50 = next((int(r.checkpoint) for r in sub.itertuples() if getattr(r, comp.replace('/', '_'), None) is not None), math.nan)
        # Pandas namedtuple mangles column names, easier iterate rows.
        c50 = math.nan
        c80 = math.nan
        for _, r in sub.iterrows():
            val = r[comp]
            if eval_rule == "B" and math.isnan(c50) and val >= threshold_50:
                c50 = int(r["checkpoint"])
            if eval_rule == "B" and math.isnan(c80) and val >= threshold_80:
                c80 = int(r["checkpoint"])
        rows.append({"run_name": run_name, "seed": seed, "eval_rule": eval_rule, "final_accuracy": final, "adaptation_half_life": c50, "adaptation_threshold_80": c80})
    return pd.DataFrame(rows)


def analyze(output_dir: str | Path) -> None:
    output_dir = Path(output_dir)
    metrics_path = output_dir / "metrics.csv"
    if not metrics_path.exists():
        raise FileNotFoundError(metrics_path)
    metrics = pd.read_csv(metrics_path)
    route = pd.read_csv(output_dir / "route_diagnostics.csv") if (output_dir / "route_diagnostics.csv").exists() else pd.DataFrame()
    failures = pd.read_csv(output_dir / "failure_taxonomy.csv") if (output_dir / "failure_taxonomy.csv").exists() else pd.DataFrame()
    baselines = pd.read_csv(output_dir / "baselines.csv") if (output_dir / "baselines.csv").exists() else pd.DataFrame()

    wide = _metric_wide(metrics)
    wide.to_csv(output_dir / "metrics_wide.csv", index=False)

    group_cols = ["run_name", "phase", "checkpoint", "eval_rule", "feedback_noise", "reward_delay_steps"]
    summary = wide.groupby(group_cols, dropna=False).mean(numeric_only=True).reset_index()
    summary.to_csv(output_dir / "exp10_summary.csv", index=False)

    route_summary = pd.DataFrame()
    if not route.empty:
        route_group_cols = ["run_name", "phase", "checkpoint", "eval_rule", "mode", "feedback_noise", "reward_delay_steps"]
        route_summary = route.groupby(route_group_cols, dropna=False).agg(
            route_table_accuracy=("correct", "mean"),
            mean_target_rank=("target_rank", "mean"),
            mean_correct_margin=("correct_margin", "mean"),
            mean_context_margin=("context_margin", "mean"),
            mean_wrong_route_activation=("wrong_route_activation", "mean"),
        ).reset_index()
        route_summary.to_csv(output_dir / "exp10_route_summary.csv", index=False)

    if not baselines.empty:
        base_summary = baselines.groupby(["split", "eval_rule", "baseline"], dropna=False).agg(accuracy_mean=("accuracy", "mean"), accuracy_std=("accuracy", "std"), n=("n", "mean")).reset_index()
        base_summary.to_csv(output_dir / "exp10_baseline_summary.csv", index=False)

    # Curves.
    _plot_dual_rule(summary, "composition/accuracy", "Experiment 10: reversal composition accuracy (old A vs new B)", output_dir / "exp10_reversal_composition_dual_rule.png", "reversal")
    _plot_dual_rule(summary, "route/route_table_accuracy", "Experiment 10: reversal route-table accuracy (old A vs new B)", output_dir / "exp10_reversal_route_table_dual_rule.png", "reversal")
    _plot_dual_rule(summary, "composition/mean_correct_margin", "Experiment 10: reversal correct margin (old A vs new B)", output_dir / "exp10_reversal_correct_margin_dual_rule.png", "reversal")
    _plot_line(summary, "composition/accuracy", "Experiment 10: new-rule B composition adaptation", output_dir / "exp10_reversal_new_rule_composition.png", "reversal", eval_rule="B")
    _plot_line(summary, "composition/accuracy", "Experiment 10: old-rule A retention during reversal", output_dir / "exp10_reversal_old_rule_retention.png", "reversal", eval_rule="A")
    _plot_line(summary, "route/route_table_accuracy", "Experiment 10: new-rule B route-table adaptation", output_dir / "exp10_reversal_new_rule_route_table.png", "reversal", eval_rule="B")

    # Switchback data is retained in CSVs and report; plots are omitted by default to keep analysis fast.

    # Final clean reversal bars.
    rev = summary[summary["phase"].str.contains("reversal", regex=False)].copy()
    if not rev.empty:
        max_ckpt = rev["checkpoint"].max()
        final_new = rev[(rev["checkpoint"] == max_ckpt) & (rev["eval_rule"] == "B")]
        final_old = rev[(rev["checkpoint"] == max_ckpt) & (rev["eval_rule"] == "A")]
        _plot_bar(final_new, "composition/accuracy", f"Experiment 10: final new-rule B composition at ckpt={max_ckpt}", output_dir / "exp10_final_new_rule_composition.png")
        _plot_bar(final_old, "composition/accuracy", f"Experiment 10: final old-rule A retention at ckpt={max_ckpt}", output_dir / "exp10_final_old_rule_retention.png")

    # Failure taxonomy final reversal.
    if not failures.empty:
        f = failures[failures["phase"].str.contains("reversal", regex=False)].copy()
        if not f.empty:
            max_ckpt = f["checkpoint"].max()
            f = f[(f["checkpoint"] == max_ckpt) & (f["eval_rule"] == "B")]
            if not f.empty:
                pivot = f.groupby(["run_name", "failure_type"])["count"].sum().unstack(fill_value=0)
                pivot.plot(kind="bar", stacked=True, figsize=(14, 6))
                plt.ylabel("count")
                plt.title("Experiment 10: new-rule B failure taxonomy at final reversal checkpoint")
                plt.xticks(rotation=35, ha="right")
                _save_plot(output_dir / "exp10_failure_taxonomy_final_new_rule.png")

    # Per-mode route heatmaps can be regenerated from route_diagnostics.csv if needed.
    # They are omitted by default to keep Experiment 10 runs fast and avoid huge image sets.

    thresh = _thresholds(summary)
    if not thresh.empty:
        thresh.to_csv(output_dir / "exp10_adaptation_thresholds.csv", index=False)

    # Markdown report.
    report = []
    report.append("# Experiment 10 Analysis - Rule Reversal, Retention, and Adaptive Rebinding\n")
    report.append("Experiment 10 tests whether a route field learned under rule A can adapt when the meaning of mode labels is changed to rule B. It also tests whether consolidation, inhibition, reward gating, eligibility traces, and dual world context affect the stability-plasticity tradeoff.\n")
    report.append("## Variant summary\n")
    display_cols = [c for c in ["run_name", "phase", "checkpoint", "eval_rule", "composition/accuracy", "route/route_table_accuracy", "composition/mean_correct_margin", "route/mean_wrong_route_activation", "feedback_noise", "reward_delay_steps"] if c in summary.columns]
    if display_cols:
        # Keep the report compact: first/last checkpoint for reversal plus final switchback if present.
        compact = summary.copy()
        keep = []
        for phase, sub in compact.groupby("phase"):
            keep.extend(sub[sub["checkpoint"].isin([sub["checkpoint"].min(), sub["checkpoint"].max()])].index.tolist())
        report.append(compact.loc[sorted(set(keep)), display_cols].to_markdown(index=False))
        report.append("\n")
    if not baselines.empty:
        report.append("## Deterministic baselines\n")
        base_summary = pd.read_csv(output_dir / "exp10_baseline_summary.csv") if (output_dir / "exp10_baseline_summary.csv").exists() else pd.DataFrame()
        if not base_summary.empty:
            report.append(base_summary.to_markdown(index=False))
            report.append("\n")
    report.append("## Interpretation guide\n")
    report.append("- `eval_rule=A` measures old-rule retention. `eval_rule=B` measures new-rule adaptation.\n")
    report.append("- `checkpoint=0` in the reversal phase is immediately after the rule change, before any B training.\n")
    report.append("- New-rule adaptation should increase with reversal exposures; old-rule retention should decrease if the same context labels are overwritten.\n")
    report.append("- `exp10_dual_context_worlds` tests whether adding higher-level world context can retain both rule sets.\n")
    report.append("- `exp10_strong_consolidation` should preserve old routes but slow new-rule acquisition.\n")
    report.append("- `exp10_no_consolidation` should adapt quickly but forget more aggressively.\n")
    report.append("- `exp10_no_inhibition` should show more old-route interference.\n")
    report.append("- `exp10_no_reward_gate` and `exp10_no_eligibility_trace` are most meaningful in the optional noisy/delayed stress phase.\n")
    (output_dir / "exp10_report.md").write_text("\n".join(report), encoding="utf-8")


if __name__ == "__main__":
    analyze(Path("analysis/exp10"))
