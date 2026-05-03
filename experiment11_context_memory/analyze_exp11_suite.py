from __future__ import annotations

from pathlib import Path
import math
import pandas as pd
import matplotlib.pyplot as plt


def _metric_name(metric: str) -> str:
    return metric.replace("/", "_").replace(" ", "_")


def _read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path) if path.exists() and path.stat().st_size > 0 else pd.DataFrame()


def pivot_metrics(metrics: pd.DataFrame) -> pd.DataFrame:
    if metrics.empty:
        return metrics
    idx = ["run_name", "seed", "phase", "checkpoint", "eval_world", "world_context_bleed", "world_context_dropout"]
    wide = metrics.pivot_table(index=idx, columns="metric", values="value", aggfunc="mean").reset_index()
    wide.columns = [_metric_name(str(c)) for c in wide.columns]
    return wide


def save_plot(path: Path) -> None:
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()


def plot_sequential(wide: pd.DataFrame, output_dir: Path) -> None:
    seq = wide[wide["phase"].isin(["sequential_after_initial", "sequential_learn_B"])].copy()
    if seq.empty:
        return
    seq = seq.groupby(["run_name", "checkpoint", "eval_world"], as_index=False).agg({
        "composition_accuracy": "mean",
        "route_route_table_accuracy": "mean",
        "composition_mean_correct_margin": "mean",
        "composition_mean_world_margin": "mean",
        "composition_mean_wrong_world_activation": "mean",
    })
    for metric, title, ylabel, fname in [
        ("composition_accuracy", "Experiment 11: sequential A retention / B acquisition", "composition accuracy", "exp11_sequential_composition.png"),
        ("route_route_table_accuracy", "Experiment 11: sequential route-table accuracy", "route-table accuracy", "exp11_sequential_route_table.png"),
        ("composition_mean_correct_margin", "Experiment 11: sequential correct-route margin", "margin", "exp11_sequential_correct_margin.png"),
        ("composition_mean_world_margin", "Experiment 11: sequential world-separation margin", "world margin", "exp11_sequential_world_margin.png"),
        ("composition_mean_wrong_world_activation", "Experiment 11: sequential wrong-world activation", "wrong-world activation", "exp11_sequential_wrong_world_activation.png"),
    ]:
        if metric not in seq:
            continue
        plt.figure(figsize=(14, 7))
        for (run, world), sub in seq.groupby(["run_name", "eval_world"]):
            style = "--" if world == "A" else "-"
            plt.plot(sub["checkpoint"], sub[metric], marker="o", linestyle=style, label=f"{run} / world {world}")
        plt.title(title)
        plt.xlabel("B exposures after A learning")
        plt.ylabel(ylabel)
        plt.legend(fontsize=8, ncol=2)
        save_plot(output_dir / fname)


def plot_alternating(wide: pd.DataFrame, output_dir: Path) -> None:
    alt = wide[wide["phase"] == "alternating"].copy()
    if alt.empty:
        return
    alt = alt.groupby(["run_name", "checkpoint", "eval_world"], as_index=False).agg({
        "composition_accuracy": "mean",
        "route_route_table_accuracy": "mean",
        "composition_mean_world_margin": "mean",
    })
    for metric, title, fname in [
        ("composition_accuracy", "Experiment 11: alternating worlds composition", "exp11_alternating_composition.png"),
        ("route_route_table_accuracy", "Experiment 11: alternating worlds route-table", "exp11_alternating_route_table.png"),
        ("composition_mean_world_margin", "Experiment 11: alternating worlds margin", "exp11_alternating_world_margin.png"),
    ]:
        if metric not in alt:
            continue
        plt.figure(figsize=(14, 7))
        for (run, world), sub in alt.groupby(["run_name", "eval_world"]):
            plt.plot(sub["checkpoint"], sub[metric], marker="o", label=f"{run} / {world}")
        plt.title(title)
        plt.xlabel("alternation cycle")
        plt.ylabel(metric)
        plt.legend(fontsize=8, ncol=2)
        save_plot(output_dir / fname)


def plot_scaling(wide: pd.DataFrame, output_dir: Path) -> None:
    sc = wide[wide["phase"] == "scaling"].copy()
    if sc.empty:
        return
    max_ckpt = sc["checkpoint"].max()
    final = sc[sc["checkpoint"] == max_ckpt].groupby(["run_name", "eval_world"], as_index=False).agg({
        "composition_accuracy": "mean",
        "route_route_table_accuracy": "mean",
        "composition_mean_world_margin": "mean",
        "composition_mean_wrong_world_activation": "mean",
    })
    for metric, title, fname in [
        ("composition_accuracy", "Experiment 11: final multi-world composition", "exp11_scaling_final_composition.png"),
        ("route_route_table_accuracy", "Experiment 11: final multi-world route-table", "exp11_scaling_final_route_table.png"),
        ("composition_mean_world_margin", "Experiment 11: final multi-world separation margin", "exp11_scaling_final_world_margin.png"),
        ("composition_mean_wrong_world_activation", "Experiment 11: final multi-world wrong-world activation", "exp11_scaling_final_wrong_world_activation.png"),
    ]:
        if metric not in final:
            continue
        plt.figure(figsize=(14, 7))
        pivot = final.pivot(index="run_name", columns="eval_world", values=metric).fillna(0.0)
        pivot.plot(kind="bar", ax=plt.gca())
        plt.title(title)
        plt.xlabel("run name")
        plt.ylabel(metric)
        plt.xticks(rotation=35, ha="right")
        save_plot(output_dir / fname)


def plot_context_noise(wide: pd.DataFrame, output_dir: Path) -> None:
    for phase, xcol, title_fragment, fname_prefix in [
        ("context_bleed", "world_context_bleed", "world-context bleed", "exp11_context_bleed"),
        ("context_dropout", "world_context_dropout", "world-context dropout", "exp11_context_dropout"),
    ]:
        df = wide[wide["phase"] == phase].copy()
        if df.empty:
            continue
        df = df.groupby(["run_name", xcol, "eval_world"], as_index=False).agg({
            "composition_accuracy": "mean",
            "composition_mean_world_margin": "mean",
            "composition_mean_wrong_world_activation": "mean",
        })
        for metric, ylabel, suffix in [
            ("composition_accuracy", "composition accuracy", "composition"),
            ("composition_mean_world_margin", "world margin", "world_margin"),
            ("composition_mean_wrong_world_activation", "wrong-world activation", "wrong_world_activation"),
        ]:
            if metric not in df:
                continue
            plt.figure(figsize=(14, 7))
            for (run, world), sub in df.groupby(["run_name", "eval_world"]):
                plt.plot(sub[xcol], sub[metric], marker="o", label=f"{run} / {world}")
            plt.title(f"Experiment 11: {ylabel} under {title_fragment}")
            plt.xlabel(title_fragment)
            plt.ylabel(ylabel)
            plt.legend(fontsize=8, ncol=2)
            save_plot(output_dir / f"{fname_prefix}_{suffix}.png")


def summarize_outputs(wide: pd.DataFrame, baselines: pd.DataFrame, failure: pd.DataFrame, output_dir: Path) -> None:
    if wide.empty:
        return
    # Summary by run/phase/world/checkpoint.
    metric_cols = [c for c in wide.columns if c not in {"run_name", "seed", "phase", "checkpoint", "eval_world", "world_context_bleed", "world_context_dropout"}]
    summary = wide.groupby(["run_name", "phase", "checkpoint", "eval_world", "world_context_bleed", "world_context_dropout"], as_index=False)[metric_cols].mean()
    summary.to_csv(output_dir / "exp11_summary.csv", index=False)

    # Final sequential retention/acquisition.
    seq = summary[summary["phase"] == "sequential_learn_B"].copy()
    if not seq.empty:
        max_ckpt = seq["checkpoint"].max()
        final = seq[seq["checkpoint"] == max_ckpt]
        final.to_csv(output_dir / "exp11_final_sequential_summary.csv", index=False)
        # Retention/acquisition indices.
        rows = []
        for run, sub in final.groupby("run_name"):
            vals = {r.eval_world: r for r in sub.itertuples(index=False)}
            if "A" in vals and "B" in vals:
                rows.append({
                    "run_name": run,
                    "retention_A_after_B": getattr(vals["A"], "composition_accuracy", math.nan),
                    "acquisition_B_after_A": getattr(vals["B"], "composition_accuracy", math.nan),
                    "route_retention_A_after_B": getattr(vals["A"], "route_route_table_accuracy", math.nan),
                    "route_acquisition_B_after_A": getattr(vals["B"], "route_route_table_accuracy", math.nan),
                    "world_margin_A_after_B": getattr(vals["A"], "composition_mean_world_margin", math.nan),
                    "world_margin_B_after_A": getattr(vals["B"], "composition_mean_world_margin", math.nan),
                })
        pd.DataFrame(rows).to_csv(output_dir / "exp11_memory_indices.csv", index=False)

    if not baselines.empty:
        baseline_summary = baselines.groupby(["split", "eval_world", "baseline"], as_index=False).agg(accuracy_mean=("accuracy", "mean"), accuracy_std=("accuracy", "std"), n=("n", "first"))
        baseline_summary.to_csv(output_dir / "exp11_baseline_summary.csv", index=False)

    if not failure.empty:
        fsum = failure.groupby(["run_name", "phase", "checkpoint", "eval_world", "failure_type"], as_index=False)["count"].sum()
        fsum.to_csv(output_dir / "exp11_failure_summary.csv", index=False)
        final_seq = fsum[fsum["phase"] == "sequential_learn_B"].copy()
        if not final_seq.empty:
            max_ckpt = final_seq["checkpoint"].max()
            final_seq = final_seq[final_seq["checkpoint"] == max_ckpt]
            plt.figure(figsize=(14, 7))
            pivot = final_seq.pivot_table(index=["run_name", "eval_world"], columns="failure_type", values="count", aggfunc="sum", fill_value=0)
            pivot.plot(kind="bar", stacked=True, ax=plt.gca())
            plt.title("Experiment 11: final sequential failure taxonomy")
            plt.xlabel("run / eval world")
            plt.ylabel("count")
            plt.xticks(rotation=35, ha="right")
            save_plot(output_dir / "exp11_failure_taxonomy_final_sequential.png")


def write_report(output_dir: Path, wide: pd.DataFrame) -> None:
    lines = []
    lines.append("# Experiment 11 Analysis - Context-Separated Memory and Non-Destructive Rebinding\n")
    lines.append("Experiment 11 tests whether higher-order world context can separate multiple route systems over the same source/mode substrate. It measures old-world retention while a new world is learned, alternating-world stability, multi-world scaling, and retrieval robustness under world-context bleed/dropout.\n")
    if not wide.empty:
        summary_path = output_dir / "exp11_memory_indices.csv"
        if summary_path.exists():
            mem = pd.read_csv(summary_path)
            lines.append("## Final sequential memory indices\n")
            lines.append(mem.to_markdown(index=False))
            lines.append("\n")
        lines.append("## Generated outputs\n")
        for p in sorted(output_dir.glob("*.png")):
            lines.append(f"- `{p.name}`")
        lines.append("\n")
        lines.append("## Interpretation guide\n")
        lines.append("- `retention_A_after_B` measures whether world A remains accessible after world B training without A rehearsal.\n")
        lines.append("- `acquisition_B_after_A` measures whether the new world is acquired after A.\n")
        lines.append("- `composition_mean_world_margin` and `composition_mean_wrong_world_activation` indicate whether the correct world context suppresses other route worlds.\n")
        lines.append("- `exp11_no_world_context` and `exp11_shared_edges_only` should overwrite/collide.\n")
        lines.append("- `exp11_world_gated_plasticity` is the strongest test of non-destructive world-specific updates.\n")
    (output_dir / "exp11_report.md").write_text("\n".join(lines), encoding="utf-8")


def analyze(output_dir: Path | str) -> None:
    output_dir = Path(output_dir)
    metrics = _read_csv(output_dir / "metrics.csv")
    baselines = _read_csv(output_dir / "baselines.csv")
    failure = _read_csv(output_dir / "failure_taxonomy.csv")
    wide = pivot_metrics(metrics)
    if not wide.empty:
        wide.to_csv(output_dir / "metrics_wide.csv", index=False)
        plot_sequential(wide, output_dir)
        plot_alternating(wide, output_dir)
        plot_scaling(wide, output_dir)
        plot_context_noise(wide, output_dir)
        summarize_outputs(wide, baselines, failure, output_dir)
    write_report(output_dir, wide)


if __name__ == "__main__":
    analyze(Path("analysis/exp11"))
