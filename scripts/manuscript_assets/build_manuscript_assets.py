from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from manuscript_data import (
    REPO_ROOT,
    RequiredInput,
    choose_existing,
    count_csv_rows,
    count_files,
    format_num,
    normal_ci,
    read_csv,
    rel_path,
    repo_path,
    summarize_validation,
    table_to_markdown,
    validate_inputs,
    write_csv_and_md,
)


FIG_DIR = repo_path("docs/manuscript/figures")
SOURCE_DIR = repo_path("docs/manuscript/source_data")
TABLE_DIR = repo_path("docs/manuscript/tables")
MANIFEST_PATH = repo_path("docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md")
REPORT_PATH = repo_path("docs/repo_audit/MANUSCRIPT_ASSET_GENERATION_REPORT.md")


FREEZE = "docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md"
EXP13_1_RUN = "exp13_1_full_20260506_214756"
EXP13_2_RUN = "exp13_2_full_20260507_165813"
EXP14_RUN = "exp14_full_20260507_210712"


EXPECTED_INPUTS = [
    RequiredInput(FREEZE, "required", "frozen first-manuscript claim set", "C1-C7,C13"),
    RequiredInput("docs/manuscript/CLAIMS_AND_EVIDENCE.md", "required", "claim evidence cross-check", "C1-C13"),
    RequiredInput("docs/manuscript/FIGURE_PLAN.md", "required", "pre-existing figure-plan conflict check", "C1-C13"),
    RequiredInput("docs/manuscript/MANUSCRIPT_TODO.md", "required", "pre-existing TODO cross-check", "C1-C13"),
    RequiredInput("docs/manuscript/LIMITATIONS_AND_THREATS.md", "required", "caveat source", "C1-C13"),
    RequiredInput("docs/synthesis/PUBLICATION_READINESS.md", "required", "readiness caveat cross-check", "C1-C13"),
    RequiredInput("docs/synthesis/NEXT_EXPERIMENTS.md", "required", "future-work boundary cross-check", "C8-C13"),
    RequiredInput("docs/experiments/EXPERIMENT_REGISTRY.md", "required", "experiment provenance registry", "C1-C13"),
    RequiredInput("docs/threads/THREAD_INDEX.md", "required", "thread digest index", "C1-C13"),
    RequiredInput("docs/repo_audit/THREAD_IMPORT_CONFLICTS.md", "required", "conflict/caveat source", "C1-C13"),
    RequiredInput("docs/repo_audit", "required", "repo audit directory", "C1-C13"),
    RequiredInput("experiments/experiment11_context_memory/README.md", "required", "conceptual/task source", "C1-C4"),
    RequiredInput("experiments/experiment12_capacity_generalization/README.md", "required", "conceptual/capacity source", "C5"),
    RequiredInput("experiments/experiment13_breaking_point/README.md", "required", "finite-budget protocol source", "C6,C7"),
    RequiredInput("experiments/experiment13_1_publication_hardening/README.md", "required", "ablation protocol source", "C1-C4"),
    RequiredInput(f"experiments/experiment13_1_publication_hardening/analysis/{EXP13_1_RUN}/exp13_1_ablation_metrics.csv", "required", "core ablation source", "C1-C4"),
    RequiredInput(f"experiments/experiment13_1_publication_hardening/analysis/{EXP13_1_RUN}/validation_results.json", "required", "run integrity", "C1-C4,C7"),
    RequiredInput("experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv", "required", "clean capacity scaling source", "C5"),
    RequiredInput("experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv", "required", "global finite-budget source", "C6"),
    RequiredInput("experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv", "required", "local finite-budget source", "C7"),
    RequiredInput(f"experiments/experiment13_2_baseline_suite/analysis/{EXP13_2_RUN}/exp13_2_summary.csv", "required", "symbolic baseline source table", "C2-C4,C12"),
    RequiredInput(f"experiments/experiment13_2_baseline_suite/analysis/{EXP13_2_RUN}/exp13_2_effect_sizes.csv", "required", "symbolic baseline effect sizes", "C2-C4,C12"),
    RequiredInput(f"experiments/experiment13_2_baseline_suite/analysis/{EXP13_2_RUN}/validation_results.json", "required", "baseline run integrity", "C12"),
    RequiredInput(f"experiments/experiment14_latent_context_inference/analysis/{EXP14_RUN}/exp14_summary.csv", "required", "symbolic cue-selection source", "C13"),
    RequiredInput(f"experiments/experiment14_latent_context_inference/analysis/{EXP14_RUN}/exp14_effect_sizes.csv", "required", "symbolic cue-selection effect sizes", "C13"),
    RequiredInput(f"experiments/experiment14_latent_context_inference/analysis/{EXP14_RUN}/validation_results.json", "required", "Exp14 run integrity", "C13"),
    RequiredInput("docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md", "required", "Exp14 import caveat", "C13"),
    RequiredInput("docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md", "required", "Exp13.2 import caveat", "C12"),
]


def metric_row(
    *,
    experiment_id: str,
    experiment_name: str,
    run_id: str,
    source_artifact: str,
    metric: str,
    mean: Any,
    std: Any = np.nan,
    count: Any = np.nan,
    ci_low: Any = np.nan,
    ci_high: Any = np.nan,
    manuscript_claim_id: str,
    caveat: str,
    condition: str = "",
    variant: str = "",
    baseline: str = "",
    comparison: str = "",
    profile: str = "",
    world_count: Any = np.nan,
    route_length: Any = np.nan,
    cue_count: Any = np.nan,
    corruption_rate: Any = np.nan,
    budget_ratio: Any = np.nan,
    panel: str = "",
    effect_size: Any = np.nan,
) -> dict[str, Any]:
    if pd.isna(ci_low) or pd.isna(ci_high):
        sem, lo, hi = normal_ci(float(mean), float(std) if not pd.isna(std) else np.nan, float(count) if not pd.isna(count) else np.nan)
    else:
        sem = None
        lo, hi = ci_low, ci_high
    if sem is None and not pd.isna(std) and not pd.isna(count) and count:
        sem = float(std) / np.sqrt(float(count))
    return {
        "experiment_id": experiment_id,
        "experiment_name": experiment_name,
        "run_id": run_id,
        "profile": profile,
        "source_artifact": source_artifact,
        "variant": variant,
        "baseline": baseline,
        "condition": condition,
        "world_count": world_count,
        "route_length": route_length,
        "cue_count": cue_count,
        "corruption_rate": corruption_rate,
        "budget_ratio": budget_ratio,
        "metric": metric,
        "mean": mean,
        "std": std,
        "sem": sem,
        "ci_low": lo,
        "ci_high": hi,
        "effect_size": effect_size,
        "comparison": comparison,
        "panel": panel,
        "caveat": caveat,
        "manuscript_claim_id": manuscript_claim_id,
    }


def build_figure_01() -> tuple[pd.DataFrame, list[str]]:
    source = "docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md"
    rows = [
        {
            "panel": "worlds_contexts",
            "element": "World/context cues select among incompatible transition systems.",
            "source_artifact": source,
            "manuscript_claim_id": "C2",
            "caveat": "Conceptual schematic only; not empirical evidence.",
        },
        {
            "panel": "structural_table",
            "element": "Context-indexed structural route table stores one-step transitions.",
            "source_artifact": source,
            "manuscript_claim_id": "C1,C4",
            "caveat": "Does not claim biological proof or novelty of context gating alone.",
        },
        {
            "panel": "recurrence",
            "element": "Recurrent execution composes stored one-step transitions into multi-step routes.",
            "source_artifact": source,
            "manuscript_claim_id": "C3,C4",
            "caveat": "Composition is over stored transitions, not unseen primitive inference.",
        },
        {
            "panel": "cue_selection",
            "element": "Symbolic transition cues can select the active context before execution.",
            "source_artifact": source,
            "manuscript_claim_id": "C13",
            "caveat": "Symbolic transition-cue selection, not raw sensory latent-world discovery.",
        },
    ]
    df = pd.DataFrame(rows)
    source_path = SOURCE_DIR / "figure_01_conceptual_route_memory.csv"
    df.to_csv(source_path, index=False)
    files = plot_conceptual_route_memory(df, FIG_DIR / "figure_01_conceptual_route_memory")
    return df, [rel_path(p) for p in files]


def build_figure_02() -> tuple[pd.DataFrame, list[str]]:
    source = f"experiments/experiment13_1_publication_hardening/analysis/{EXP13_1_RUN}/exp13_1_ablation_metrics.csv"
    df = read_csv(source)
    rows: list[dict[str, Any]] = []
    picks = {
        "exp13_1_full_model": "Full model",
        "exp13_1_no_structural_plasticity": "No structural\nplasticity",
        "exp13_1_no_context_binding": "No context\nbinding",
        "exp13_1_no_recurrence_at_eval": "No recurrence\nat eval",
    }
    sub = df[(df["phase"] == "structure_audit") & (df["route_length"] == 12) & (df["variant_name"].isin(picks))]
    caveat = "Internal symbolic ablation; normal-approximate CI from aggregate std/count; lesion diagnostics are not used."
    for _, r in sub.sort_values("variant_name").iterrows():
        for metric, prefix in [
            ("composition_accuracy", "composition_accuracy"),
            ("route_table_accuracy", "route_table_accuracy"),
        ]:
            rows.append(
                metric_row(
                    experiment_id="Exp13.1",
                    experiment_name="publication_hardening",
                    run_id=EXP13_1_RUN,
                    profile="full",
                    source_artifact=source,
                    variant=r["variant_name"],
                    condition=picks[r["variant_name"]],
                    route_length=r["route_length"],
                    metric=metric,
                    mean=r[f"{prefix}_mean"],
                    std=r[f"{prefix}_std"],
                    count=r[f"{prefix}_count"],
                    manuscript_claim_id="C1,C2,C3,C4",
                    caveat=caveat,
                )
            )
    out = pd.DataFrame(rows)
    out.to_csv(SOURCE_DIR / "figure_02_structural_plasticity_recurrence_ablation.csv", index=False)
    files = plot_ablation(out, FIG_DIR / "figure_02_structural_plasticity_recurrence_ablation")
    return out, [rel_path(p) for p in files]


def build_figure_03() -> tuple[pd.DataFrame, list[str]]:
    source = "experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv"
    df = read_csv(source)
    rows: list[dict[str, Any]] = []
    sub = df[df["run_name"] == "exp12_full_context_separated_memory"]
    caveat = "Ceiling-limited clean supplied-context scaling; no fitted capacity law is claimed."
    for _, r in sub.sort_values(["world_count", "route_length"]).iterrows():
        for metric, prefix in [
            ("composition_accuracy", "composition_accuracy"),
            ("route_table_accuracy", "route_route_table_accuracy"),
        ]:
            rows.append(
                metric_row(
                    experiment_id="Exp12",
                    experiment_name="capacity_generalization",
                    run_id="exp12",
                    profile="full",
                    source_artifact=source,
                    variant=r["run_name"],
                    condition="clean supplied context",
                    world_count=r["world_count"],
                    route_length=r["route_length"],
                    metric=metric,
                    mean=r[f"{prefix}_mean"],
                    std=r[f"{prefix}_std"],
                    count=r[f"{prefix}_count"],
                    manuscript_claim_id="C5",
                    caveat=caveat,
                )
            )
    out = pd.DataFrame(rows)
    out.to_csv(SOURCE_DIR / "figure_03_capacity_scaling.csv", index=False)
    files = plot_capacity_scaling(out, FIG_DIR / "figure_03_capacity_scaling")
    return out, [rel_path(p) for p in files]


def build_figure_04() -> tuple[pd.DataFrame, list[str]]:
    global_source = "experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv"
    local_source = "experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv"
    global_df = read_csv(global_source)
    local_df = read_csv(local_source)
    rows: list[dict[str, Any]] = []
    caveat = "Observed finite-budget degradation only; capacity-law fitting and paired seed-level local/global inference are not claimed."
    selections = [
        (global_df, global_source, "budget_ratio", "Global budget"),
        (local_df, local_source, "local_budget_ratio", "Local per-world budget"),
    ]
    for data, source, budget_col, condition in selections:
        sub = data[
            (data["run_name"] == "exp13_full_context_separated_memory")
            & (data["world_count"] == 32)
            & (data["route_length"] == 12)
        ]
        for _, r in sub.sort_values(budget_col).iterrows():
            for metric, prefix in [
                ("composition_accuracy", "composition_accuracy"),
                ("route_table_accuracy", "route_route_table_accuracy"),
            ]:
                rows.append(
                    metric_row(
                        experiment_id="Exp13",
                        experiment_name="breaking_point",
                        run_id="analysis",
                        profile="full",
                        source_artifact=source,
                        variant=r["run_name"],
                        condition=condition,
                        world_count=r["world_count"],
                        route_length=r["route_length"],
                        budget_ratio=r[budget_col],
                        metric=metric,
                        mean=r[f"{prefix}_mean"],
                        std=r[f"{prefix}_std"],
                        count=r[f"{prefix}_count"],
                        manuscript_claim_id="C6,C7",
                        caveat=caveat,
                    )
                )
    out = pd.DataFrame(rows)
    out.to_csv(SOURCE_DIR / "figure_04_finite_structural_budget_local_global.csv", index=False)
    files = plot_finite_budget(out, FIG_DIR / "figure_04_finite_structural_budget_local_global")
    return out, [rel_path(p) for p in files]


def build_figure_05() -> tuple[pd.DataFrame, list[str]]:
    source = f"experiments/experiment14_latent_context_inference/analysis/{EXP14_RUN}/exp14_summary.csv"
    df = read_csv(source)
    caveat = (
        "Symbolic transition-cue context selection only; oracle context-gated lookup remains an upper bound; "
        "shared no-context suffix metrics can be misleading when suffix probes bypass first-step context conflict."
    )
    rows: list[dict[str, Any]] = []
    metric_names = [
        "world_selection_accuracy_seen_route",
        "composition_accuracy_seen_route",
        "composition_accuracy_suffix_route",
        "first_step_context_accuracy",
    ]
    corruption_variants = [
        "exp14_cirm_latent_selector",
        "baseline_oracle_context_gated_table",
        "baseline_random_context_selector",
        "baseline_shared_no_context_table",
    ]
    corr = df[
        (df["world_count"] == 32)
        & (df["route_length"] == 16)
        & (df["cue_count"] == 8)
        & (df["variant"].isin(corruption_variants))
    ]
    cue = df[
        (df["world_count"] == 32)
        & (df["route_length"] == 16)
        & (df["corruption_rate"] == 0.25)
        & (df["variant"].isin(["exp14_cirm_latent_selector", "baseline_oracle_context_gated_table", "baseline_random_context_selector"]))
    ]
    for panel, data in [("corruption_sweep", corr), ("cue_count_sweep", cue)]:
        for _, r in data.sort_values(["variant", "cue_count", "corruption_rate"]).iterrows():
            for metric in metric_names:
                rows.append(
                    metric_row(
                        experiment_id="Exp14",
                        experiment_name="latent_context_inference",
                        run_id=EXP14_RUN,
                        profile="full",
                        source_artifact=source,
                        variant=r["variant"],
                        condition="symbolic transition-cue selection",
                        world_count=r["world_count"],
                        route_length=r["route_length"],
                        cue_count=r["cue_count"],
                        corruption_rate=r["corruption_rate"],
                        metric=metric,
                        mean=r[f"{metric}_mean"],
                        std=r[f"{metric}_std"],
                        count=r[f"{metric}_n"],
                        ci_low=r[f"{metric}_ci95_low"],
                        ci_high=r[f"{metric}_ci95_high"],
                        manuscript_claim_id="C13",
                        caveat=caveat,
                        panel=panel,
                    )
                )
    out = pd.DataFrame(rows)
    out.to_csv(SOURCE_DIR / "figure_05_symbolic_context_selection.csv", index=False)
    files = plot_latent_context(out, FIG_DIR / "figure_05_symbolic_context_selection")
    return out, [rel_path(p) for p in files]


def build_exp13_2_source_data() -> pd.DataFrame:
    source = f"experiments/experiment13_2_baseline_suite/analysis/{EXP13_2_RUN}/exp13_2_summary.csv"
    df = read_csv(source)
    variants = [
        "exp13_2_cirm_full",
        "baseline_context_gated_transition_table",
        "baseline_shared_transition_table",
        "baseline_route_endpoint_memorizer",
        "exp13_2_cirm_no_recurrence_at_eval",
        "exp13_2_cirm_no_structural_plasticity",
    ]
    sub = df[
        (df["phase"] == "baseline_comparison")
        & (df["world_count"] == 32)
        & (df["route_length"] == 16)
        & (df["variant"].isin(variants))
    ]
    caveat = (
        "Exp13.2 is a symbolic/algorithmic baseline suite. Oracle context-gated lookup matches CIRM under clean supplied context; "
        "do not claim broad neural superiority."
    )
    rows: list[dict[str, Any]] = []
    for _, r in sub.sort_values("variant").iterrows():
        for metric in [
            "route_table_accuracy_all",
            "composition_accuracy_seen_routes",
            "composition_accuracy_suffix_routes",
            "first_step_context_accuracy",
        ]:
            rows.append(
                metric_row(
                    experiment_id="Exp13.2",
                    experiment_name="baseline_suite",
                    run_id=EXP13_2_RUN,
                    profile="full",
                    source_artifact=source,
                    variant=r["variant"],
                    condition="hard clean supplied-context baseline slice",
                    world_count=r["world_count"],
                    route_length=r["route_length"],
                    metric=metric,
                    mean=r[f"{metric}_mean"],
                    std=r[f"{metric}_std"],
                    count=r[f"{metric}_n"],
                    ci_low=r[f"{metric}_ci95_low"],
                    ci_high=r[f"{metric}_ci95_high"],
                    manuscript_claim_id="C2,C3,C4,C12",
                    caveat=caveat,
                )
            )
    out = pd.DataFrame(rows)
    out.to_csv(SOURCE_DIR / "table_exp13_2_symbolic_baseline_suite.csv", index=False)
    return out


def build_claim_evidence_table(source_frames: dict[str, pd.DataFrame]) -> pd.DataFrame:
    fig2 = source_frames["figure_02"]
    fig3 = source_frames["figure_03"]
    fig4 = source_frames["figure_04"]
    fig5 = source_frames["figure_05"]
    exp13_2 = source_frames["exp13_2"]

    def val(df: pd.DataFrame, **query: Any) -> float:
        sub = df.copy()
        for k, v in query.items():
            sub = sub[sub[k] == v]
        return float(sub.iloc[0]["mean"]) if not sub.empty else float("nan")

    rows = [
        {
            "claim_id": "C1",
            "frozen_claim_wording": "Within this symbolic route-memory benchmark, removing structural plasticity collapses route-table formation and route execution.",
            "manuscript_role": "Main but benchmark-specific",
            "supporting_experiments": "Exp13.1, Exp13.2; earlier Exp8/Exp11/Exp12/Exp13 in claim inventory",
            "key_metric": "route_table_accuracy; composition_accuracy",
            "headline_result": f"Exp13.1 no-structural-plasticity route-table {val(fig2, variant='exp13_1_no_structural_plasticity', metric='route_table_accuracy'):.4f}, composition {val(fig2, variant='exp13_1_no_structural_plasticity', metric='composition_accuracy'):.4f}.",
            "baseline_or_control": "Full model; no-structural-plasticity ablation",
            "caveat": "Internal symbolic ablation; not broad neural or biological proof.",
            "figure_or_table": "Figure 2; Table 3",
            "source_paths": f"experiments/experiment13_1_publication_hardening/analysis/{EXP13_1_RUN}/exp13_1_ablation_metrics.csv",
        },
        {
            "claim_id": "C2",
            "frozen_claim_wording": "Context/world indexing separates incompatible transition systems; Exp14 shows the active symbolic context can also be selected from transition cues.",
            "manuscript_role": "Main but narrow",
            "supporting_experiments": "Exp13.1, Exp13.2, Exp14",
            "key_metric": "first_step_context_accuracy; world_selection_accuracy_seen_route",
            "headline_result": f"Exp14 CIRM hard clean cue-selected world selection {val(fig5, variant='exp14_cirm_latent_selector', metric='world_selection_accuracy_seen_route', panel='corruption_sweep', corruption_rate=0.0):.4f}; shared no-context Exp13.2 first-step {val(exp13_2, variant='baseline_shared_transition_table', metric='first_step_context_accuracy'):.4f}.",
            "baseline_or_control": "Shared no-context table; oracle context-gated upper bound",
            "caveat": "Split supplied-context indexing from symbolic cue-selected context; no raw sensory discovery claim.",
            "figure_or_table": "Figure 5; Tables 1 and 3",
            "source_paths": f"experiments/experiment14_latent_context_inference/analysis/{EXP14_RUN}/exp14_summary.csv; experiments/experiment13_2_baseline_suite/analysis/{EXP13_2_RUN}/exp13_2_summary.csv",
        },
        {
            "claim_id": "C3",
            "frozen_claim_wording": "Recurrent execution is required to compose stored one-step route memories into multi-step routes.",
            "manuscript_role": "Main",
            "supporting_experiments": "Exp13.1, Exp13.2",
            "key_metric": "route_table_accuracy vs composition_accuracy",
            "headline_result": f"Exp13.1 no-recurrence-at-eval route-table {val(fig2, variant='exp13_1_no_recurrence_at_eval', metric='route_table_accuracy'):.4f}, composition {val(fig2, variant='exp13_1_no_recurrence_at_eval', metric='composition_accuracy'):.4f}.",
            "baseline_or_control": "No-recurrence-at-eval control",
            "caveat": "Claim is storage/execution dissociation in this benchmark; recurrence itself is not novel.",
            "figure_or_table": "Figure 2; Tables 1 and 3",
            "source_paths": f"experiments/experiment13_1_publication_hardening/analysis/{EXP13_1_RUN}/exp13_1_ablation_metrics.csv; experiments/experiment13_2_baseline_suite/analysis/{EXP13_2_RUN}/exp13_2_summary.csv",
        },
        {
            "claim_id": "C4",
            "frozen_claim_wording": "Route-table storage and multi-step compositional execution are separable in this benchmark.",
            "manuscript_role": "Main",
            "supporting_experiments": "Exp13.1, Exp13.2, Exp14",
            "key_metric": "route-table/composition gap; suffix composition controls",
            "headline_result": "No-recurrence preserves one-step storage while composition collapses; endpoint memorization controls fail suffix composition.",
            "baseline_or_control": "No-recurrence and endpoint memorization controls",
            "caveat": "Does not imply unseen primitive-transition inference.",
            "figure_or_table": "Figure 2; Tables 1 and 3",
            "source_paths": f"experiments/experiment13_2_baseline_suite/analysis/{EXP13_2_RUN}/exp13_2_summary.csv; experiments/experiment14_latent_context_inference/analysis/{EXP14_RUN}/exp14_summary.csv",
        },
        {
            "claim_id": "C5",
            "frozen_claim_wording": "Under clean supplied context, the full model maintains ceiling route-table and composition accuracy through the tested world counts.",
            "manuscript_role": "Main but ceiling-limited",
            "supporting_experiments": "Exp12",
            "key_metric": "composition_accuracy; route_table_accuracy at world_count=32, route_length=12",
            "headline_result": f"Exp12 full model route-length 12 at 32 worlds: composition {val(fig3, world_count=32, route_length=12, metric='composition_accuracy'):.4f}, route-table {val(fig3, world_count=32, route_length=12, metric='route_table_accuracy'):.4f}.",
            "baseline_or_control": "Clean supplied-context full model scaling grid",
            "caveat": "Ceiling regime; avoid fitted-law wording.",
            "figure_or_table": "Figure 3; Tables 1 and 3",
            "source_paths": "experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv",
        },
        {
            "claim_id": "C6",
            "frozen_claim_wording": "Finite structural budget produces an observed route-execution degradation curve.",
            "manuscript_role": "Main but narrow",
            "supporting_experiments": "Exp13",
            "key_metric": "composition_accuracy across global budget_ratio",
            "headline_result": f"Exp13 32-world route-length 12 global budget curve rises from {val(fig4, condition='Global budget', metric='composition_accuracy', budget_ratio=0.25):.4f} at 0.25 budget to {val(fig4, condition='Global budget', metric='composition_accuracy', budget_ratio=1.0):.4f} at exact budget.",
            "baseline_or_control": "Budget-ratio sweep",
            "caveat": "Observed curve only; no fitted capacity law.",
            "figure_or_table": "Figure 4; Tables 1 and 3",
            "source_paths": "experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv",
        },
        {
            "claim_id": "C7",
            "frozen_claim_wording": "Local-vs-global budget behavior is supplement or narrow main unless paired seed-level comparison is added.",
            "manuscript_role": "Supplement or narrow main panel",
            "supporting_experiments": "Exp13, Exp13.1",
            "key_metric": "local vs global budget composition_accuracy",
            "headline_result": f"At 0.50 budget, Exp13 global composition {val(fig4, condition='Global budget', metric='composition_accuracy', budget_ratio=0.5):.4f} vs local per-world composition {val(fig4, condition='Local per-world budget', metric='composition_accuracy', budget_ratio=0.5):.4f}.",
            "baseline_or_control": "Global vs local budget sweeps",
            "caveat": "Paired seed-level comparison remains deferred; treat as narrow/supplementary.",
            "figure_or_table": "Figure 4; Tables 1 and 3",
            "source_paths": "experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv; docs/experiments/exp13_local_vs_global_budget_comparison.md",
        },
        {
            "claim_id": "C13",
            "frozen_claim_wording": "The active symbolic world/context can be selected from partial transition-cue evidence before route execution.",
            "manuscript_role": "Main but narrow, or high-priority supplement",
            "supporting_experiments": "Exp14",
            "key_metric": "world_selection_accuracy_seen_route; composition_accuracy_seen_route",
            "headline_result": f"Exp14 CIRM hard slice: clean world selection {val(fig5, variant='exp14_cirm_latent_selector', metric='world_selection_accuracy_seen_route', panel='corruption_sweep', corruption_rate=0.0):.4f}; at corruption 0.50, world selection {val(fig5, variant='exp14_cirm_latent_selector', metric='world_selection_accuracy_seen_route', panel='corruption_sweep', corruption_rate=0.5):.4f}.",
            "baseline_or_control": "Oracle context-gated upper bound; random/shared no-context selectors",
            "caveat": "Symbolic transition-cue evidence only; not autonomous perceptual context discovery.",
            "figure_or_table": "Figure 5; Tables 1 and 3",
            "source_paths": f"experiments/experiment14_latent_context_inference/analysis/{EXP14_RUN}/exp14_summary.csv",
        },
        {
            "claim_id": "C12",
            "frozen_claim_wording": "Baseline/prior-art comparison remains a discussion/readiness issue; Exp13.2 supplies symbolic/algorithmic baselines only.",
            "manuscript_role": "Discussion/readiness table",
            "supporting_experiments": "Exp13.2",
            "key_metric": "oracle context-gated table vs CIRM; shared no-context and endpoint controls",
            "headline_result": f"Exp13.2 hard clean slice: CIRM and oracle context-gated lookup both at {val(exp13_2, variant='baseline_context_gated_transition_table', metric='composition_accuracy_seen_routes'):.4f} seen-route composition.",
            "baseline_or_control": "Oracle context-gated lookup, shared no-context, endpoint memorizer, no-recurrence",
            "caveat": "No neural baselines and no prior-art novelty import; do not claim broad ML superiority.",
            "figure_or_table": "Table 1; Table 3; source-data table",
            "source_paths": f"experiments/experiment13_2_baseline_suite/analysis/{EXP13_2_RUN}/exp13_2_summary.csv; docs/manuscript/BASELINE_REQUIREMENTS.md",
        },
    ]
    out = pd.DataFrame(rows)
    write_csv_and_md(out, TABLE_DIR / "table_01_claim_evidence.csv", TABLE_DIR / "table_01_claim_evidence.md")
    return out


def build_run_integrity_table() -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    runs = [
        {
            "experiment_id": "Exp11",
            "experiment_name": "context_memory",
            "run_id": "exp11",
            "profile": "full",
            "analysis_dir": "experiments/experiment11_context_memory/analysis/exp11",
            "validation_json": None,
            "metrics": "experiments/experiment11_context_memory/analysis/exp11/metrics.csv",
            "summary": "experiments/experiment11_context_memory/analysis/exp11/exp11_summary.csv",
            "effects": None,
            "db": None,
            "manifest": None,
            "notes": "No validation JSON in this historical run; included as supporting artifact inspection.",
        },
        {
            "experiment_id": "Exp12",
            "experiment_name": "capacity_generalization",
            "run_id": "exp12",
            "profile": "full",
            "analysis_dir": "experiments/experiment12_capacity_generalization/analysis/exp12",
            "validation_json": None,
            "metrics": "experiments/experiment12_capacity_generalization/analysis/exp12/metrics.csv",
            "summary": "experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv",
            "effects": None,
            "db": None,
            "manifest": None,
            "notes": "No validation JSON in this historical run; used for C5 clean scaling.",
        },
        {
            "experiment_id": "Exp13",
            "experiment_name": "breaking_point",
            "run_id": "analysis",
            "profile": "full",
            "analysis_dir": "experiments/experiment13_breaking_point/analysis",
            "validation_json": "experiments/experiment13_breaking_point/analysis/validation_results.json",
            "metrics": "experiments/experiment13_breaking_point/analysis/metrics.csv",
            "summary": "experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv",
            "effects": None,
            "db": None,
            "manifest": None,
            "notes": "Aggregate finite-budget source; no per-run SQLite manifest for this older layout.",
        },
        {
            "experiment_id": "Exp13.1",
            "experiment_name": "publication_hardening",
            "run_id": EXP13_1_RUN,
            "profile": "full",
            "analysis_dir": f"experiments/experiment13_1_publication_hardening/analysis/{EXP13_1_RUN}",
            "validation_json": f"experiments/experiment13_1_publication_hardening/analysis/{EXP13_1_RUN}/validation_results.json",
            "metrics": f"experiments/experiment13_1_publication_hardening/analysis/{EXP13_1_RUN}/metrics.csv",
            "summary": f"experiments/experiment13_1_publication_hardening/analysis/{EXP13_1_RUN}/exp13_1_summary.csv",
            "effects": None,
            "db": f"experiments/experiment13_1_publication_hardening/runs/{EXP13_1_RUN}.sqlite3",
            "manifest": f"experiments/experiment13_1_publication_hardening/analysis/{EXP13_1_RUN}/run_manifest.json",
            "notes": "Validated publication-hardening ablation run; lesion result retained only as caveat.",
        },
        {
            "experiment_id": "Exp13.2",
            "experiment_name": "baseline_suite",
            "run_id": EXP13_2_RUN,
            "profile": "full",
            "analysis_dir": f"experiments/experiment13_2_baseline_suite/analysis/{EXP13_2_RUN}",
            "validation_json": f"experiments/experiment13_2_baseline_suite/analysis/{EXP13_2_RUN}/validation_results.json",
            "metrics": f"experiments/experiment13_2_baseline_suite/analysis/{EXP13_2_RUN}/exp13_2_metrics.csv",
            "summary": f"experiments/experiment13_2_baseline_suite/analysis/{EXP13_2_RUN}/exp13_2_summary.csv",
            "effects": f"experiments/experiment13_2_baseline_suite/analysis/{EXP13_2_RUN}/exp13_2_effect_sizes.csv",
            "db": f"experiments/experiment13_2_baseline_suite/runs/{EXP13_2_RUN}.sqlite3",
            "manifest": f"experiments/experiment13_2_baseline_suite/analysis/{EXP13_2_RUN}/run_manifest.json",
            "notes": "Symbolic/algorithmic baselines only; oracle context-gated table is an upper-bound clean supplied-context control.",
        },
        {
            "experiment_id": "Exp14",
            "experiment_name": "latent_context_inference",
            "run_id": EXP14_RUN,
            "profile": "full",
            "analysis_dir": f"experiments/experiment14_latent_context_inference/analysis/{EXP14_RUN}",
            "validation_json": f"experiments/experiment14_latent_context_inference/analysis/{EXP14_RUN}/validation_results.json",
            "metrics": f"experiments/experiment14_latent_context_inference/analysis/{EXP14_RUN}/exp14_metrics.csv",
            "summary": f"experiments/experiment14_latent_context_inference/analysis/{EXP14_RUN}/exp14_summary.csv",
            "effects": f"experiments/experiment14_latent_context_inference/analysis/{EXP14_RUN}/exp14_effect_sizes.csv",
            "db": f"experiments/experiment14_latent_context_inference/runs/{EXP14_RUN}.sqlite3",
            "manifest": f"experiments/experiment14_latent_context_inference/analysis/{EXP14_RUN}/run_manifest.json",
            "notes": "Symbolic transition-cue context-selection evidence; not raw sensory latent-world discovery.",
        },
    ]
    for run in runs:
        status, pass_count, warn_count, fail_count = summarize_validation(run["validation_json"])
        rows.append(
            {
                "experiment_id": run["experiment_id"],
                "experiment_name": run["experiment_name"],
                "run_id": run["run_id"],
                "profile": run["profile"],
                "validation_status": status,
                "pass_count": pass_count,
                "warn_count": warn_count,
                "fail_count": fail_count,
                "seed_count": seed_count_for_run(run),
                "metrics_rows": count_csv_rows(run["metrics"]) if run["metrics"] else 0,
                "summary_rows": count_csv_rows(run["summary"]) if run["summary"] else 0,
                "effect_size_rows": count_csv_rows(run["effects"]) if run["effects"] else 0,
                "plots_present": count_files(f"{run['analysis_dir']}/plots", "*.png") or count_files(run["analysis_dir"], "*.png"),
                "database_present": bool(run["db"] and repo_path(run["db"]).exists()),
                "manifest_present": bool(run["manifest"] and repo_path(run["manifest"]).exists()),
                "source_paths": "; ".join(choose_existing([p for p in [run["metrics"], run["summary"], run["effects"], run["validation_json"], run["db"], run["manifest"]] if p])),
                "notes": run["notes"],
            }
        )
    out = pd.DataFrame(rows)
    write_csv_and_md(out, TABLE_DIR / "table_02_run_integrity.csv", TABLE_DIR / "table_02_run_integrity.md")
    return out


def seed_count_for_run(run: dict[str, Any]) -> Any:
    if run["manifest"] and repo_path(run["manifest"]).exists():
        obj = json.loads(repo_path(run["manifest"]).read_text(encoding="utf-8"))
        seeds = obj.get("config", {}).get("seeds")
        if isinstance(seeds, list):
            return len(seeds)
    if run["summary"] and repo_path(run["summary"]).exists():
        df = pd.read_csv(repo_path(run["summary"]))
        if "seed_count" in df.columns and df["seed_count"].notna().any():
            return int(df["seed_count"].dropna().max())
    return ""


def build_statistical_summary_table(source_frames: dict[str, pd.DataFrame]) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []

    def add_from_source(df: pd.DataFrame, claim_id: str, experiment_id: str, filters: dict[str, Any], interpretation: str) -> None:
        sub = df.copy()
        for key, value in filters.items():
            if isinstance(value, (list, tuple, set)):
                sub = sub[sub[key].isin(value)]
            else:
                sub = sub[sub[key] == value]
        for _, r in sub.iterrows():
            rows.append(
                {
                    "claim_id": claim_id,
                    "experiment_id": experiment_id,
                    "run_id": r.get("run_id", ""),
                    "metric": r.get("metric", ""),
                    "condition": str(r.get("condition", "")).replace("\n", " "),
                    "variant": r.get("variant", ""),
                    "comparator": r.get("comparison", "") or r.get("baseline", ""),
                    "mean": r.get("mean", ""),
                    "ci_low": r.get("ci_low", ""),
                    "ci_high": r.get("ci_high", ""),
                    "effect_size": r.get("effect_size", ""),
                    "seed_count": r.get("seed_count", "") or r.get("sample_count", "") or r.get("composition_accuracy_count", ""),
                    "interpretation": interpretation,
                    "caveat": r.get("caveat", ""),
                    "source_paths": r.get("source_artifact", ""),
                }
            )

    add_from_source(
        source_frames["figure_02"],
        "C1-C4",
        "Exp13.1",
        {"metric": ["composition_accuracy", "route_table_accuracy"]},
        "Core ablation summary used for Figure 2.",
    )
    add_from_source(
        source_frames["figure_03"],
        "C5",
        "Exp12",
        {"route_length": 12, "metric": ["composition_accuracy", "route_table_accuracy"]},
        "Clean supplied-context route-length-12 capacity slice used for Figure 3.",
    )
    add_from_source(
        source_frames["figure_04"],
        "C6-C7",
        "Exp13",
        {"metric": "composition_accuracy"},
        "Finite structural budget and local/global pressure slice used for Figure 4.",
    )
    add_from_source(
        source_frames["figure_05"],
        "C13",
        "Exp14",
        {"metric": ["world_selection_accuracy_seen_route", "composition_accuracy_seen_route"], "panel": ["corruption_sweep", "cue_count_sweep"]},
        "Symbolic transition-cue context-selection slice used for Figure 5.",
    )
    add_from_source(
        source_frames["exp13_2"],
        "C2-C4,C12",
        "Exp13.2",
        {"metric": ["route_table_accuracy_all", "composition_accuracy_seen_routes", "composition_accuracy_suffix_routes", "first_step_context_accuracy"]},
        "Symbolic baseline hard-slice table source; not plotted as a freeze-required main figure.",
    )

    # Add available effect sizes for the human reviewer without fabricating missing values.
    effect_rows = []
    exp13_2_effects = read_csv(f"experiments/experiment13_2_baseline_suite/analysis/{EXP13_2_RUN}/exp13_2_effect_sizes.csv")
    e13 = exp13_2_effects[
        (exp13_2_effects["phase"] == "baseline_comparison")
        & (exp13_2_effects["world_count"] == 32)
        & (exp13_2_effects["route_length"] == 16)
        & (exp13_2_effects["comparison_variant"].isin(["baseline_context_gated_transition_table", "baseline_shared_transition_table", "baseline_route_endpoint_memorizer"]))
        & (exp13_2_effects["metric"].isin(["composition_accuracy_seen_routes", "composition_accuracy_suffix_routes", "first_step_context_accuracy"]))
    ]
    for _, r in e13.iterrows():
        effect_rows.append(
            {
                "claim_id": "C2-C4,C12",
                "experiment_id": "Exp13.2",
                "run_id": EXP13_2_RUN,
                "metric": r["metric"],
                "condition": "hard clean supplied-context effect-size artifact",
                "variant": r["baseline_variant"],
                "comparator": r["comparison_variant"],
                "mean": r["mean_difference_cirm_minus_comparison"],
                "ci_low": "",
                "ci_high": "",
                "effect_size": r["cohen_d_cirm_minus_comparison"],
                "seed_count": r["n_cirm"],
                "interpretation": "CIRM-minus-comparison effect-size artifact; grouping still needs human review before citation.",
                "caveat": "Oracle context-gated lookup may match CIRM; effect sizes can be zero or undefined under ceiling.",
                "source_paths": f"experiments/experiment13_2_baseline_suite/analysis/{EXP13_2_RUN}/exp13_2_effect_sizes.csv",
            }
        )
    exp14_effects = read_csv(f"experiments/experiment14_latent_context_inference/analysis/{EXP14_RUN}/exp14_effect_sizes.csv")
    e14 = exp14_effects[
        (exp14_effects["world_count"] == 32)
        & (exp14_effects["route_length"] == 16)
        & (exp14_effects["cue_count"] == 8)
        & (exp14_effects["corruption_rate"].isin([0.0, 0.5]))
        & (exp14_effects["comparison_variant"].isin(["baseline_oracle_context_gated_table", "baseline_random_context_selector", "baseline_shared_no_context_table"]))
        & (exp14_effects["metric"].isin(["world_selection_accuracy_seen_route", "composition_accuracy_seen_route"]))
    ]
    for _, r in e14.iterrows():
        effect_rows.append(
            {
                "claim_id": "C13",
                "experiment_id": "Exp14",
                "run_id": EXP14_RUN,
                "metric": r["metric"],
                "condition": f"hard slice cue_count=8 corruption={r['corruption_rate']}",
                "variant": r["baseline_variant"],
                "comparator": r["comparison_variant"],
                "mean": r["mean_difference_cirm_minus_comparison"],
                "ci_low": "",
                "ci_high": "",
                "effect_size": r["cohen_d_cirm_minus_comparison"],
                "seed_count": r["n_cirm"],
                "interpretation": "CIRM-minus-comparison effect-size artifact for symbolic cue-selection controls.",
                "caveat": "Oracle remains an upper bound; positive differences against selector controls do not imply raw sensory discovery.",
                "source_paths": f"experiments/experiment14_latent_context_inference/analysis/{EXP14_RUN}/exp14_effect_sizes.csv",
            }
        )

    out = pd.concat([pd.DataFrame(rows), pd.DataFrame(effect_rows)], ignore_index=True)
    write_csv_and_md(out, TABLE_DIR / "table_03_statistical_summary.csv", TABLE_DIR / "table_03_statistical_summary.md")
    return out


def write_manifest(
    figure_records: list[dict[str, Any]],
    table_records: list[dict[str, Any]],
    missing_deferred: list[dict[str, str]],
) -> None:
    lines = [
        "# Manuscript Asset Manifest",
        "",
        "## Generated command",
        "",
        "`python scripts/manuscript_assets/build_manuscript_assets.py`",
        "",
        f"Generated at: `{datetime.now(timezone.utc).isoformat()}`.",
        "",
        "## Generated figures",
        "",
        "| Figure | File(s) | Source data | Supports claim(s) | Source artifacts | Status | Caveat |",
        "|---|---|---|---|---|---|---|",
    ]
    for rec in figure_records:
        lines.append(
            f"| {rec['figure']} | {rec['files']} | `{rec['source_data']}` | {rec['claims']} | {rec['source_artifacts']} | {rec['status']} | {rec['caveat']} |"
        )
    lines.extend(
        [
            "",
            "## Generated tables",
            "",
            "| Table | File(s) | Source artifacts | Supports claim(s) | Status | Caveat |",
            "|---|---|---|---|---|---|",
        ]
    )
    for rec in table_records:
        lines.append(
            f"| {rec['table']} | {rec['files']} | {rec['source_artifacts']} | {rec['claims']} | {rec['status']} | {rec['caveat']} |"
        )
    lines.extend(
        [
            "",
            "## Missing or deferred assets",
            "",
            "| Asset | Reason | Required action |",
            "|---|---|---|",
        ]
    )
    for rec in missing_deferred:
        lines.append(f"| {rec['asset']} | {rec['reason']} | {rec['required_action']} |")
    MANIFEST_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_generation_report(
    *,
    warnings: list[str],
    figure_records: list[dict[str, Any]],
    table_records: list[dict[str, Any]],
    missing_required: list[str],
    missing_deferred: list[dict[str, str]],
    path_verification_result: str,
) -> None:
    inputs = [item.path for item in EXPECTED_INPUTS if repo_path(item.path).exists()]
    conflicts = [
        "Freeze document names Figure 4 as finite structural budget/local-vs-global pressure, while older prompt/figure-plan variants can describe a baseline-comparison Figure 4. This build follows the freeze document and writes Exp13.2 baseline evidence as source data and tables.",
        "Historical Figure Plan listed Exp14 as Figure 9 and Exp13.2 as deferred; this build follows the post-freeze main/candidate set and regenerates Exp14 as Figure 5 candidate evidence.",
    ]
    lines = [
        "# Manuscript Asset Generation Report",
        "",
        "## Summary",
        "",
        "Generated reproducible first-manuscript candidate figures, source-data CSVs, and manuscript tables from local repository artifacts without rerunning experiments or modifying completed experimental outputs.",
        "",
        "## Inputs inspected",
        "",
    ]
    lines.extend(f"- `{p}`" for p in inputs)
    lines.extend(
        [
            "",
            "## Generated source data",
            "",
        ]
    )
    for rec in figure_records:
        lines.append(f"- `{rec['source_data']}` supports {rec['claims']} from {rec['source_artifacts']}.")
    lines.append("- `docs/manuscript/source_data/table_exp13_2_symbolic_baseline_suite.csv` supports C2-C4/C12 from Exp13.2.")
    lines.extend(["", "## Generated figures", ""])
    for rec in figure_records:
        lines.append(f"- {rec['figure']}: {rec['files']} ({rec['status']}). Caveat: {rec['caveat']}")
    lines.extend(["", "## Generated tables", ""])
    for rec in table_records:
        lines.append(f"- {rec['table']}: {rec['files']} ({rec['status']}).")
    lines.extend(
        [
            "",
            "## Claims covered",
            "",
            "- C1, C2, C3, C4, C5, C6, C7, C13, and C12 discussion/readiness evidence are covered by generated source data and/or tables.",
            "",
            "## Claims not covered",
            "",
            "- C8 consolidation remains supplementary/preliminary and was not promoted into the generated main figure set.",
            "- C9 seen-vs-unseen primitive boundary remains deferred pending metric cleanup.",
            "- C10 context/cue corruption is represented only through Exp14 symbolic cue corruption; generic robustness is not claimed.",
            "- C11 continuous/noisy bridge remains supplementary/future and was not generated as a main figure.",
            "",
            "## Missing required artifacts",
            "",
        ]
    )
    if missing_required:
        lines.extend(f"- `{m}`" for m in missing_required)
    else:
        lines.append("- None.")
    lines.extend(["", "## Warnings and caveats", ""])
    for warning in warnings:
        lines.append(f"- {warning}")
    for conflict in conflicts:
        lines.append(f"- Conflict recorded: {conflict}")
    lines.extend(
        [
            "- Exp13.2 baseline outputs are symbolic/algorithmic only; neural baselines and prior-art/novelty import remain open.",
            "- Exp14 wording is limited to symbolic context selection from partial transition evidence.",
            "- Normal-approximate intervals are computed only where source artifacts provide aggregate std/count and do not already provide CI95 columns.",
            "",
            "## Figure readiness status",
            "",
            "| Figure | Status | Review need |",
            "|---|---|---|",
        ]
    )
    for rec in figure_records:
        lines.append(f"| {rec['figure']} | {rec['status']} | Human caption/layout review before manuscript submission. |")
    lines.extend(
        [
            "",
            "## Verification result",
            "",
            path_verification_result,
            "",
            "## Recommended next action",
            "",
            "Human-review figure captions, decide Exp14 main-vs-supplement placement, decide controlled symbolic/mechanistic venue posture, and keep neural/prior-art/novelty gaps explicit before submission.",
        ]
    )
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def ensure_runtime_dependencies() -> None:
    try:
        import matplotlib  # noqa: F401

        return
    except ModuleNotFoundError:
        venv_python = REPO_ROOT / ".venv" / "Scripts" / "python.exe"
        if venv_python.exists() and Path(sys.executable).resolve() != venv_python.resolve():
            print(f"matplotlib not available in {sys.executable}; re-running with {venv_python}")
            os.execv(str(venv_python), [str(venv_python), *sys.argv])
        raise


def main() -> int:
    ensure_runtime_dependencies()
    from manuscript_plotting import (
        plot_ablation,
        plot_capacity_scaling,
        plot_conceptual_route_memory,
        plot_finite_budget,
        plot_latent_context,
    )

    globals()["plot_ablation"] = plot_ablation
    globals()["plot_capacity_scaling"] = plot_capacity_scaling
    globals()["plot_conceptual_route_memory"] = plot_conceptual_route_memory
    globals()["plot_finite_budget"] = plot_finite_budget
    globals()["plot_latent_context"] = plot_latent_context

    for directory in [FIG_DIR, SOURCE_DIR, TABLE_DIR, REPORT_PATH.parent]:
        directory.mkdir(parents=True, exist_ok=True)

    missing_required, warnings = validate_inputs(EXPECTED_INPUTS)
    if missing_required:
        REPORT_PATH.write_text(
            "# Manuscript Asset Generation Report\n\n## Missing required artifacts\n\n"
            + "\n".join(f"- {m}" for m in missing_required)
            + "\n",
            encoding="utf-8",
        )
        print("Missing required manuscript inputs:")
        for item in missing_required:
            print(f"  - {item}")
        return 2

    source_frames: dict[str, pd.DataFrame] = {}
    source_frames["figure_01"], fig1_files = build_figure_01()
    source_frames["figure_02"], fig2_files = build_figure_02()
    source_frames["figure_03"], fig3_files = build_figure_03()
    source_frames["figure_04"], fig4_files = build_figure_04()
    source_frames["figure_05"], fig5_files = build_figure_05()
    source_frames["exp13_2"] = build_exp13_2_source_data()

    claim_table = build_claim_evidence_table(source_frames)
    integrity_table = build_run_integrity_table()
    stats_table = build_statistical_summary_table(source_frames)

    figure_records = [
        {
            "figure": "Figure 1 - Conceptual route-memory schematic",
            "files": "`docs/manuscript/figures/figure_01_conceptual_route_memory.png`; `docs/manuscript/figures/figure_01_conceptual_route_memory.svg`",
            "source_data": "docs/manuscript/source_data/figure_01_conceptual_route_memory.csv",
            "claims": "C1-C4 framing; C13 wording boundary",
            "source_artifacts": "`docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`; experiment READMEs",
            "status": "generated candidate schematic",
            "caveat": "Conceptual, not empirical evidence.",
        },
        {
            "figure": "Figure 2 - Structural plasticity and recurrence ablation",
            "files": "`docs/manuscript/figures/figure_02_structural_plasticity_recurrence_ablation.png`; `docs/manuscript/figures/figure_02_structural_plasticity_recurrence_ablation.svg`",
            "source_data": "docs/manuscript/source_data/figure_02_structural_plasticity_recurrence_ablation.csv",
            "claims": "C1,C2,C3,C4",
            "source_artifacts": f"`experiments/experiment13_1_publication_hardening/analysis/{EXP13_1_RUN}/exp13_1_ablation_metrics.csv`",
            "status": "generated candidate main figure",
            "caveat": "Internal symbolic ablation; uncertainty uses aggregate normal approximation.",
        },
        {
            "figure": "Figure 3 - Clean capacity scaling",
            "files": "`docs/manuscript/figures/figure_03_capacity_scaling.png`; `docs/manuscript/figures/figure_03_capacity_scaling.svg`",
            "source_data": "docs/manuscript/source_data/figure_03_capacity_scaling.csv",
            "claims": "C5",
            "source_artifacts": "`experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`",
            "status": "generated candidate main figure",
            "caveat": "Ceiling-limited clean supplied-context result; no fitted law.",
        },
        {
            "figure": "Figure 4 - Finite structural budget/local-global pressure",
            "files": "`docs/manuscript/figures/figure_04_finite_structural_budget_local_global.png`; `docs/manuscript/figures/figure_04_finite_structural_budget_local_global.svg`",
            "source_data": "docs/manuscript/source_data/figure_04_finite_structural_budget_local_global.csv",
            "claims": "C6,C7",
            "source_artifacts": "`experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv`",
            "status": "generated candidate narrow-main/supplement figure",
            "caveat": "Observed degradation curve only; paired seed-level local/global inference remains deferred.",
        },
        {
            "figure": "Figure 5 - Symbolic context selection from transition cues",
            "files": "`docs/manuscript/figures/figure_05_symbolic_context_selection.png`; `docs/manuscript/figures/figure_05_symbolic_context_selection.svg`",
            "source_data": "docs/manuscript/source_data/figure_05_symbolic_context_selection.csv",
            "claims": "C13",
            "source_artifacts": f"`experiments/experiment14_latent_context_inference/analysis/{EXP14_RUN}/exp14_summary.csv`",
            "status": "generated candidate main-or-supplement figure",
            "caveat": "Symbolic transition-cue selection only; oracle remains an upper bound.",
        },
    ]
    table_records = [
        {
            "table": "Table 1 - Claim evidence",
            "files": "`docs/manuscript/tables/table_01_claim_evidence.csv`; `docs/manuscript/tables/table_01_claim_evidence.md`",
            "source_artifacts": "Frozen claim set plus generated source data.",
            "claims": "C1-C7,C13,C12",
            "status": "generated manuscript source table",
            "caveat": "Headline results are conservative summaries tied to source paths.",
        },
        {
            "table": "Table 2 - Run integrity",
            "files": "`docs/manuscript/tables/table_02_run_integrity.csv`; `docs/manuscript/tables/table_02_run_integrity.md`",
            "source_artifacts": "Validation JSONs, manifests, metrics, summaries, plots, and run DB paths where present.",
            "claims": "run provenance for C1-C7,C13",
            "status": "generated manuscript source table",
            "caveat": "Older Exp11/Exp12 layouts lack validation JSON/SQLite manifests.",
        },
        {
            "table": "Table 3 - Statistical summary",
            "files": "`docs/manuscript/tables/table_03_statistical_summary.csv`; `docs/manuscript/tables/table_03_statistical_summary.md`",
            "source_artifacts": "Generated figure source data and Exp13.2/Exp14 effect-size CSVs.",
            "claims": "C1-C7,C13,C12",
            "status": "generated manuscript source table",
            "caveat": "Effect-size grouping still needs human review before exact manuscript citation.",
        },
    ]
    missing_deferred = [
        {
            "asset": "Neural/prior-art baseline comparison figure",
            "reason": "Freeze document keeps neural baselines and prior-art novelty import outside the current completed evidence.",
            "required_action": "Decide target venue and import prior-art/novelty sources before submission-readiness claims.",
        },
        {
            "asset": "C8 consolidation figure",
            "reason": "Freeze document recommends supplement-only/preliminary handling.",
            "required_action": "Generate only if supplement scope is approved and caption keeps the stability-plasticity caveat.",
        },
        {
            "asset": "C9 seen/unseen primitive-boundary figure",
            "reason": "Metric cleanup remains required.",
            "required_action": "Add seen/unseen/all route-table and composition split metrics before central use.",
        },
        {
            "asset": "Positive lesion mechanism figure",
            "reason": "Freeze document drops positive lesion evidence; Exp13.1 diagnostic failed expected pattern.",
            "required_action": "Do not cite positively unless audited and rerun in a successor/approved analysis.",
        },
    ]
    write_manifest(figure_records, table_records, missing_deferred)
    write_generation_report(
        warnings=warnings,
        figure_records=figure_records,
        table_records=table_records,
        missing_required=[],
        missing_deferred=missing_deferred,
        path_verification_result="Path verifier not yet run in this build invocation. Run `python scripts/verify_doc_source_paths.py` after build and update this section if needed.",
    )

    print("Manuscript asset build complete.")
    print(f"Generated figures: {len(figure_records)}")
    print(f"Generated source-data files: {len(figure_records) + 1}")
    print(f"Generated manuscript tables: {len(table_records)}")
    print(f"Claim evidence rows: {len(claim_table)}")
    print(f"Run integrity rows: {len(integrity_table)}")
    print(f"Statistical summary rows: {len(stats_table)}")
    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"  - {warning}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
