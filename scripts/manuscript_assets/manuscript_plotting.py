from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


FIGURE_SIZE = (7.0, 4.6)
DPI = 300


def configure_matplotlib() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 9,
            "axes.titlesize": 10,
            "axes.labelsize": 9,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "legend.fontsize": 8,
            "figure.titlesize": 11,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "grid.color": "0.86",
            "grid.linewidth": 0.6,
            "savefig.bbox": "tight",
        }
    )


def save_figure(fig: plt.Figure, stem: Path) -> list[str]:
    stem.parent.mkdir(parents=True, exist_ok=True)
    png = stem.with_suffix(".png")
    svg = stem.with_suffix(".svg")
    fig.savefig(png, dpi=DPI)
    fig.savefig(svg)
    plt.close(fig)
    return [png.as_posix(), svg.as_posix()]


def plot_conceptual_route_memory(source_data: pd.DataFrame, out_stem: Path) -> list[str]:
    configure_matplotlib()
    fig, ax = plt.subplots(figsize=(8.0, 4.5))
    ax.set_axis_off()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)

    boxes = [
        ("World/context cues", 0.5, 4.2, 2.0, 0.9),
        ("Context-indexed\nstructural table", 3.1, 4.2, 2.3, 0.9),
        ("One-step\nroute memories", 6.0, 4.2, 2.0, 0.9),
        ("Recurrent\nroute execution", 3.8, 2.1, 2.8, 0.9),
        ("Multi-step route\nprediction", 7.2, 2.1, 2.1, 0.9),
    ]
    for label, x, y, w, h in boxes:
        rect = plt.Rectangle((x, y), w, h, fill=False, linewidth=1.3, color="0.1")
        ax.add_patch(rect)
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center")

    arrows = [
        ((2.5, 4.65), (3.1, 4.65)),
        ((5.4, 4.65), (6.0, 4.65)),
        ((7.0, 4.2), (5.2, 3.0)),
        ((6.6, 2.55), (7.2, 2.55)),
        ((3.8, 2.55), (2.2, 4.2)),
    ]
    for (x0, y0), (x1, y1) in arrows:
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0), arrowprops={"arrowstyle": "->", "lw": 1.1, "color": "0.1"})

    ax.text(0.7, 0.75, "Conceptual schematic only; not empirical evidence.", ha="left", va="center", color="0.25")
    ax.text(0.7, 0.35, "World labels may be supplied or symbolically selected from transition cues.", ha="left", va="center", color="0.25")
    ax.set_title("Context-indexed route memory benchmark setup")
    return save_figure(fig, out_stem)


def plot_ablation(df: pd.DataFrame, out_stem: Path) -> list[str]:
    configure_matplotlib()
    fig, ax = plt.subplots(figsize=FIGURE_SIZE)
    order = ["Full model", "No structural\nplasticity", "No context\nbinding", "No recurrence\nat eval"]
    metrics = ["route_table_accuracy", "composition_accuracy"]
    width = 0.34
    x = np.arange(len(order))
    colors = ["0.2", "0.62"]
    hatches = ["", "///"]
    for i, metric in enumerate(metrics):
        sub = df[df["metric"] == metric].set_index("condition").reindex(order)
        y = sub["mean"].to_numpy(dtype=float)
        yerr = (sub["ci_high"] - sub["mean"]).fillna(0).to_numpy(dtype=float)
        ax.bar(x + (i - 0.5) * width, y, width, yerr=yerr, capsize=3, label=metric.replace("_", " "), color=colors[i], hatch=hatches[i])
    ax.set_ylim(0, 1.08)
    ax.set_ylabel("Accuracy")
    ax.set_xticks(x)
    ax.set_xticklabels(order)
    ax.legend(frameon=False, loc="upper right")
    ax.set_title("Core ablations separate storage from route execution")
    return save_figure(fig, out_stem)


def plot_capacity_scaling(df: pd.DataFrame, out_stem: Path) -> list[str]:
    configure_matplotlib()
    fig, ax = plt.subplots(figsize=FIGURE_SIZE)
    sub = df[(df["route_length"] == 12) & (df["variant"] == "exp12_full_context_separated_memory")]
    for metric, marker, color in [
        ("composition_accuracy", "o", "0.2"),
        ("route_table_accuracy", "s", "0.55"),
    ]:
        m = sub[sub["metric"] == metric].sort_values("world_count")
        yerr = (m["ci_high"] - m["mean"]).fillna(0).to_numpy(dtype=float)
        ax.errorbar(m["world_count"], m["mean"], yerr=yerr, marker=marker, color=color, linewidth=1.6, capsize=3, label=metric.replace("_", " "))
    ax.set_xscale("log", base=2)
    ax.set_xticks(sorted(sub["world_count"].dropna().unique()))
    ax.get_xaxis().set_major_formatter(plt.ScalarFormatter())
    ax.set_ylim(0, 1.08)
    ax.set_xlabel("World count")
    ax.set_ylabel("Accuracy at route length 12")
    ax.legend(frameon=False, loc="lower left")
    ax.set_title("Clean supplied-context scaling remains ceiling-limited")
    return save_figure(fig, out_stem)


def plot_finite_budget(df: pd.DataFrame, out_stem: Path) -> list[str]:
    configure_matplotlib()
    fig, ax = plt.subplots(figsize=FIGURE_SIZE)
    for condition, marker, color in [
        ("Global budget", "o", "0.2"),
        ("Local per-world budget", "s", "0.58"),
    ]:
        m = df[(df["condition"] == condition) & (df["metric"] == "composition_accuracy")].sort_values("budget_ratio")
        yerr = (m["ci_high"] - m["mean"]).fillna(0).to_numpy(dtype=float)
        ax.errorbar(m["budget_ratio"], m["mean"], yerr=yerr, marker=marker, linewidth=1.6, color=color, capsize=3, label=condition)
    ax.set_ylim(0, 1.08)
    ax.set_xlabel("Available structural budget ratio")
    ax.set_ylabel("Composition accuracy")
    ax.legend(frameon=False, loc="upper left")
    ax.set_title("Finite structural budget produces degradation")
    return save_figure(fig, out_stem)


def plot_latent_context(df: pd.DataFrame, out_stem: Path) -> list[str]:
    configure_matplotlib()
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.8), sharey=True)

    left = df[(df["panel"] == "corruption_sweep") & (df["metric"] == "world_selection_accuracy_seen_route")]
    labels = {
        "exp14_cirm_latent_selector": "CIRM cue-selected",
        "baseline_oracle_context_gated_table": "Oracle context-gated",
        "baseline_random_context_selector": "Random selector",
        "baseline_shared_no_context_table": "Shared no-context",
    }
    styles = {
        "exp14_cirm_latent_selector": ("o", "0.15"),
        "baseline_oracle_context_gated_table": ("s", "0.45"),
        "baseline_random_context_selector": ("^", "0.7"),
        "baseline_shared_no_context_table": ("x", "0.0"),
    }
    for variant, label in labels.items():
        m = left[left["variant"] == variant].sort_values("corruption_rate")
        if m.empty:
            continue
        marker, color = styles[variant]
        yerr = (m["ci_high"] - m["mean"]).fillna(0).to_numpy(dtype=float)
        axes[0].errorbar(m["corruption_rate"], m["mean"], yerr=yerr, marker=marker, linewidth=1.4, color=color, capsize=3, label=label)
    axes[0].set_title("Cue corruption sweep")
    axes[0].set_xlabel("Cue corruption rate")
    axes[0].set_ylabel("World-selection accuracy")

    right = df[(df["panel"] == "cue_count_sweep") & (df["variant"] == "exp14_cirm_latent_selector") & (df["metric"].isin(["world_selection_accuracy_seen_route", "composition_accuracy_seen_route"]))]
    for metric, marker, color in [
        ("world_selection_accuracy_seen_route", "o", "0.15"),
        ("composition_accuracy_seen_route", "s", "0.58"),
    ]:
        m = right[right["metric"] == metric].sort_values("cue_count")
        yerr = (m["ci_high"] - m["mean"]).fillna(0).to_numpy(dtype=float)
        axes[1].errorbar(m["cue_count"], m["mean"], yerr=yerr, marker=marker, linewidth=1.4, color=color, capsize=3, label=metric.replace("_", " "))
    axes[1].set_title("Cue-count sensitivity at corruption 0.25")
    axes[1].set_xlabel("Transition cues")

    for ax in axes:
        ax.set_ylim(0, 1.08)
        ax.legend(frameon=False, loc="lower right")
    fig.suptitle("Symbolic context selection from partial transition evidence")
    return save_figure(fig, out_stem)
