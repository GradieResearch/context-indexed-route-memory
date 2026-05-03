from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sqlalchemy import create_engine


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze Experiment 6 route-audit successor suite.")
    parser.add_argument("--db", type=Path, default=Path("runs/exp6_route_audit_successor_suite.sqlite3"))
    parser.add_argument("--output-dir", type=Path, default=Path("analysis/exp6"))
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


def plot_accuracy_by_mode(summary: pd.DataFrame, output: Path) -> None:
    mode_columns = [column for column in summary.columns if column.startswith("composition/accuracy_mode_")]
    if not mode_columns:
        return
    mode_names = [column.replace("composition/accuracy_mode_", "") for column in mode_columns]
    x = np.arange(len(summary))
    width = 0.22
    plt.figure(figsize=(14, 6))
    for index, column in enumerate(mode_columns):
        plt.bar(x + index * width, summary[column], width=width, label=mode_names[index])
    plt.xticks(x + width, summary["run_name"], rotation=30, ha="right")
    plt.ylim(0.0, 1.05)
    plt.ylabel("accuracy")
    plt.title("Experiment 6: composition accuracy by mode")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output, dpi=150)
    plt.close()


def plot_accuracy_by_path_length(summary: pd.DataFrame, output: Path) -> None:
    step_columns = [column for column in summary.columns if column.startswith("composition/accuracy_steps_")]
    if not step_columns:
        return
    ordered = sorted(step_columns, key=lambda value: int(value.rsplit("_", 1)[-1]))
    plt.figure(figsize=(14, 6))
    for _, row in summary.iterrows():
        values = [row[column] for column in ordered]
        labels = [int(column.rsplit("_", 1)[-1]) for column in ordered]
        plt.plot(labels, values, marker="o", label=row["run_name"])
    plt.ylim(0.0, 1.05)
    plt.xlabel("steps")
    plt.ylabel("accuracy")
    plt.title("Experiment 6: composition accuracy by path length")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output, dpi=150)
    plt.close()


def plot_confusion(summary: pd.DataFrame, run_name: str, output: Path) -> None:
    row = summary[summary["run_name"] == run_name]
    if row.empty:
        row = summary.iloc[[0]]
    confusion_columns = [column for column in summary.columns if column.startswith("composition/confusion_")]
    if not confusion_columns:
        return
    pairs = [column.replace("composition/confusion_", "") for column in confusion_columns]
    actual_modes = sorted({pair.split("__")[0] for pair in pairs})
    predicted_modes = sorted({pair.split("__")[1] for pair in pairs})
    matrix = np.zeros((len(actual_modes), len(predicted_modes)), dtype=np.float32)
    for i, actual in enumerate(actual_modes):
        for j, predicted in enumerate(predicted_modes):
            column = f"composition/confusion_{actual}__{predicted}"
            if column in row.columns:
                matrix[i, j] = float(row.iloc[0][column])

    plt.figure(figsize=(7, 6))
    plt.imshow(matrix, cmap="Blues", vmin=0.0, vmax=1.0)
    plt.xticks(range(len(predicted_modes)), predicted_modes, rotation=30, ha="right")
    plt.yticks(range(len(actual_modes)), actual_modes)
    plt.xlabel("predicted mode")
    plt.ylabel("actual mode")
    plt.title(f"Experiment 6: context confusion ({row.iloc[0]['run_name']})")
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            plt.text(j, i, f"{matrix[i, j]:.2f}", ha="center", va="center", color="black")
    plt.colorbar()
    plt.tight_layout()
    plt.savefig(output, dpi=150)
    plt.close()


def plot_adaptation_curve(metrics: pd.DataFrame, runs: pd.DataFrame, output: Path) -> None:
    filtered = metrics[(metrics["split"] == "composition") & (metrics["name"] == "accuracy")]
    if filtered.empty:
        return
    merged = filtered.merge(runs[["id", "run_name"]], left_on="run_id", right_on="id", how="left")
    plt.figure(figsize=(14, 6))
    for run_name, group in merged.groupby("run_name"):
        ordered = group.sort_values("step")
        plt.plot(ordered["step"], ordered["value"], marker="o", label=run_name)
    plt.ylim(0.0, 1.05)
    plt.xlabel("training step")
    plt.ylabel("composition accuracy")
    plt.title("Experiment 6: composition accuracy over training")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output, dpi=150)
    plt.close()


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    runs, metrics = load_tables(args.db)
    latest = pivot_latest(metrics)
    best_composition = best_metric(metrics, "composition", "accuracy")
    best_transition = best_metric(metrics, "transition", "accuracy")
    summary = runs[["id", "run_name", "status", "best_accuracy"]].rename(columns={"id": "run_id"})
    summary = summary.merge(best_composition, on="run_id", how="left").merge(best_transition, on="run_id", how="left").merge(latest, on="run_id", how="left")
    if summary.empty:
        print(f"No runs found in {args.db}")
        return

    summary = summary.sort_values("best_composition_accuracy", ascending=False)
    summary.to_csv(args.output_dir / "exp6_comparison.csv", index=False)

    plot_bar(summary, "run_name", "best_composition_accuracy", "Experiment 6: best composition accuracy", args.output_dir / "exp6_best_composition_accuracy.png")
    if "composition/average_recurrent_drive" in summary.columns:
        plot_bar(summary, "run_name", "composition/average_recurrent_drive", "Experiment 6: latest recurrent drive", args.output_dir / "exp6_recurrent_drive.png")
    if "composition/average_wrong_route_activation" in summary.columns:
        plot_bar(summary, "run_name", "composition/average_wrong_route_activation", "Experiment 6: wrong-route activation", args.output_dir / "exp6_wrong_route_activation.png")
    if "composition/average_route_margin" in summary.columns:
        plot_bar(summary, "run_name", "composition/average_route_margin", "Experiment 6: route margin", args.output_dir / "exp6_route_margin.png")
    plot_accuracy_by_mode(summary, args.output_dir / "exp6_accuracy_by_mode.png")
    plot_accuracy_by_path_length(summary, args.output_dir / "exp6_accuracy_by_path_length.png")
    plot_confusion(summary, "exp6_full_route_audit", args.output_dir / "exp6_context_confusion.png")
    plot_adaptation_curve(metrics, runs, args.output_dir / "exp6_adaptation_curve.png")

    report = [
        "# Experiment 6 Analysis - Route-Audit Successor World",
        "",
        "This experiment tests whether the recurrent plastic graph can choose among multiple transition systems using context while being evaluated on the raw recurrent trajectory rather than a reconstructed symbolic state.",
        "",
        "## Summary table",
        "",
        summary.to_markdown(index=False),
        "",
        "## Interpretation framework",
        "",
        "- `best_composition_accuracy`: whether the graph can compose mode-conditioned transitions across multiple steps.",
        "- `composition/accuracy_mode_*`: whether some contexts are easier or more fragile than others.",
        "- `composition/accuracy_steps_*`: whether longer traversals degrade gracefully or collapse.",
        "- `composition/average_target_route_activation`: mean overlap with the correct route at each traversal step.",
        "- `composition/average_wrong_route_activation`: mean overlap with the strongest competing route at each traversal step.",
        "- `composition/average_route_margin`: how much the correct route beats the strongest competitor along the path.",
        "- `composition/confusion_*`: whether the final active state preserves the intended mode or drifts into another route family.",
        "- `exp6_no_context_routing`: tests whether persistent context bias is load-bearing when we stop resetting the symbolic state.",
        "- `exp6_no_inhibition`: tests whether suppressing competing contexts reduces route mixing.",
        "",
    ]
    (args.output_dir / "exp6_report.md").write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote analysis to {args.output_dir}")


if __name__ == "__main__":
    main()
