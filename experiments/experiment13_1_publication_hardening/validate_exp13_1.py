#!/usr/bin/env python3
"""Validate Experiment 13.1 analysis artifacts.

The validator checks artifact hygiene, schema consistency, and that the core
publication-hardening controls were actually emitted. It intentionally avoids
requiring a predetermined scientific effect size.
"""

from __future__ import annotations

import argparse
import json
import math
import sqlite3
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

import numpy as np
import pandas as pd


ANALYSIS_ID = "exp13_1"
PASS = "PASS"
WARN = "WARN"
FAIL = "FAIL"

REQUIRED_FILES = (
    "metrics.csv",
    f"{ANALYSIS_ID}_metrics.csv",
    f"{ANALYSIS_ID}_summary.csv",
    f"{ANALYSIS_ID}_variant_metrics.csv",
    f"{ANALYSIS_ID}_ablation_metrics.csv",
    f"{ANALYSIS_ID}_context_corruption.csv",
    f"{ANALYSIS_ID}_lesion_metrics.csv",
    f"{ANALYSIS_ID}_budget_consolidation.csv",
    f"{ANALYSIS_ID}_freeze_plasticity.csv",
    "experiment_report.md",
    f"{ANALYSIS_ID}_report.md",
    "run_manifest.json",
    "progress.jsonl",
)

REQUIRED_PLOTS = (
    f"{ANALYSIS_ID}_composition_accuracy.png",
    f"{ANALYSIS_ID}_route_table_accuracy.png",
    f"{ANALYSIS_ID}_context_confusion.png",
    f"{ANALYSIS_ID}_lesion_sensitivity.png",
    f"{ANALYSIS_ID}_recurrence_ablation.png",
    f"{ANALYSIS_ID}_budget_consolidation.png",
)

REQUIRED_VARIANTS = (
    "exp13_1_full_model",
    "exp13_1_no_recurrence_at_eval",
    "exp13_1_no_recurrence_throughout",
    "exp13_1_no_structural_plasticity",
    "exp13_1_no_context_binding",
    "exp13_1_no_world_gated_plasticity",
    "exp13_1_no_consolidation",
    "exp13_1_weak_consolidation",
    "exp13_1_aggressive_consolidation",
)

EXPECTED_COLUMNS = (
    "run_id",
    "experiment_name",
    "schema_version",
    "phase",
    "phase_detail",
    "variant_name",
    "seed",
    "world",
    "mode",
    "world_count",
    "nodes",
    "modes",
    "mode_slot_count",
    "route_length",
    "recurrence_training",
    "recurrence_evaluation",
    "recurrence_setting",
    "structural_plasticity",
    "world_context",
    "context_binding",
    "world_gated_plasticity",
    "plasticity_setting",
    "context_condition",
    "context_corruption_level",
    "lesion_condition",
    "freeze_condition",
    "budget_setting",
    "budget_ratio",
    "local_budget_ratio",
    "consolidation_setting",
    "consolidation_strength",
    "composition_accuracy",
    "route_table_accuracy",
    "transition_accuracy",
    "structure_transition_accuracy",
    "composition_route_gap",
    "route_margin",
    "world_margin",
    "mode_margin",
    "wrong_route_activation",
    "wrong_world_activation",
    "wrong_mode_activation",
    "structural_wrong_world_activation",
    "context_confusion",
    "top1_world_accuracy",
    "used_edge_fraction",
    "stored_edge_count",
    "lesion_sensitivity",
    "route_table_lesion_sensitivity",
)

METRIC_COLUMNS = (
    "composition_accuracy",
    "route_table_accuracy",
    "transition_accuracy",
    "structure_transition_accuracy",
    "composition_route_gap",
    "route_margin",
    "world_margin",
    "mode_margin",
    "wrong_route_activation",
    "wrong_world_activation",
    "wrong_mode_activation",
    "structural_wrong_world_activation",
    "context_confusion",
    "top1_world_accuracy",
    "used_edge_fraction",
    "stored_edge_count",
    "lesion_sensitivity",
    "route_table_lesion_sensitivity",
)

REQUIRED_PHASES = (
    "variant_comparison",
    "structure_audit",
    "freeze_plasticity",
    "context_corruption",
    "lesion_test",
    "budget_consolidation",
)

FORBIDDEN_REPORT_PHRASES = (
    "proves that",
    "demonstrates conclusively",
    "settles the question",
    "definitively proves",
)


def check(condition: bool, name: str, detail: str, severity: str = FAIL) -> Dict[str, Any]:
    return {"status": PASS if condition else severity, "name": name, "detail": detail}


def missing_items(expected: Sequence[str], actual: Sequence[str]) -> List[str]:
    actual_set = set(actual)
    return [item for item in expected if item not in actual_set]


def latest_analysis_dir(experiment_dir: Path) -> Optional[Path]:
    analysis_root = experiment_dir / "analysis"
    if not analysis_root.exists():
        return None
    candidates = [p for p in analysis_root.iterdir() if p.is_dir() and (p / "run_manifest.json").exists()]
    if not candidates:
        candidates = [p for p in analysis_root.iterdir() if p.is_dir()]
    if not candidates:
        return None
    return max(candidates, key=lambda p: p.stat().st_mtime)


def resolve_analysis_dir(args: argparse.Namespace) -> Path:
    if args.analysis_dir:
        return Path(args.analysis_dir).resolve()
    experiment_dir = Path(args.experiment_dir).resolve()
    if args.run_id == "latest":
        latest = latest_analysis_dir(experiment_dir)
        if latest is None:
            return experiment_dir / "analysis" / "latest_missing"
        return latest
    return experiment_dir / "analysis" / args.run_id


def load_manifest(analysis_dir: Path) -> Dict[str, Any]:
    path = analysis_dir / "run_manifest.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def check_required_files(analysis_dir: Path) -> List[Dict[str, Any]]:
    missing = [name for name in REQUIRED_FILES if not (analysis_dir / name).exists()]
    plot_missing = [name for name in REQUIRED_PLOTS if not (analysis_dir / "plots" / name).exists()]
    return [
        check(
            not missing,
            "required output files exist",
            "Missing files: " + ", ".join(missing) if missing else "All required files are present.",
        ),
        check(
            not plot_missing,
            "required plots exist under plots/",
            "Missing plots: " + ", ".join(plot_missing) if plot_missing else "All required plots are present under plots/.",
        ),
    ]


def check_manifest(analysis_dir: Path, manifest: Dict[str, Any]) -> List[Dict[str, Any]]:
    if not manifest:
        return [check(False, "run manifest can be loaded", "run_manifest.json missing or unreadable.")]
    required = ["run_id", "profile", "config", "variants", "total_progress_units"]
    missing = [key for key in required if key not in manifest]
    results = [
        check(
            not missing,
            "run manifest has required metadata",
            "Missing manifest keys: " + ", ".join(missing) if missing else f"run_id={manifest.get('run_id')}",
        )
    ]
    sqlite_path = manifest.get("sqlite_path")
    if sqlite_path:
        path = Path(sqlite_path)
        if not path.is_absolute():
            path = (analysis_dir / sqlite_path).resolve()
        results.append(check(path.exists(), "SQLite run database exists", str(path)))
        if path.exists():
            try:
                with sqlite3.connect(path) as conn:
                    tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)["name"].tolist()
                needed = {"metrics", "metadata", "variants"}
                results.append(
                    check(needed.issubset(set(tables)), "SQLite contains expected tables", f"tables={sorted(tables)}")
                )
            except Exception as exc:  # pragma: no cover - diagnostic path
                results.append(check(False, "SQLite can be inspected", repr(exc)))
    else:
        results.append(check(False, "SQLite path is recorded", "No sqlite_path in manifest.", severity=WARN))
    return results


def check_columns(df: pd.DataFrame) -> List[Dict[str, Any]]:
    missing = missing_items(EXPECTED_COLUMNS, list(df.columns))
    return [
        check(
            not missing,
            "expected metric and metadata columns present",
            "Missing columns: " + ", ".join(missing) if missing else "All expected columns are present.",
        )
    ]


def check_metric_values(df: pd.DataFrame) -> List[Dict[str, Any]]:
    missing_metrics = [col for col in METRIC_COLUMNS if col not in df.columns]
    results = [
        check(
            not missing_metrics,
            "all expected metric columns exist",
            "Missing metric columns: " + ", ".join(missing_metrics) if missing_metrics else "All expected metric columns exist.",
        )
    ]
    if missing_metrics:
        return results
    entirely_null = [col for col in METRIC_COLUMNS if df[col].isna().all()]
    results.append(
        check(
            not entirely_null,
            "no metric column is entirely null",
            "Entirely null metric columns: " + ", ".join(entirely_null) if entirely_null else "No metric column is entirely null.",
        )
    )
    non_finite = []
    for col in METRIC_COLUMNS:
        vals = pd.to_numeric(df[col], errors="coerce")
        if vals.isna().any() or not np.isfinite(vals.to_numpy(dtype=float)).all():
            non_finite.append(col)
    results.append(
        check(
            not non_finite,
            "metric columns are numeric and finite",
            "Non-finite metric columns: " + ", ".join(non_finite) if non_finite else "All metric columns are finite.",
        )
    )
    bounded = [
        "composition_accuracy",
        "route_table_accuracy",
        "transition_accuracy",
        "structure_transition_accuracy",
        "context_confusion",
        "top1_world_accuracy",
        "used_edge_fraction",
    ]
    out_of_range = [col for col in bounded if ((df[col] < -1e-9) | (df[col] > 1 + 1e-9)).any()]
    results.append(
        check(
            not out_of_range,
            "bounded metrics lie within [0, 1]",
            "Out-of-range bounded metrics: " + ", ".join(out_of_range) if out_of_range else "All bounded metrics are in range.",
        )
    )
    return results


def check_required_variants_and_phases(df: pd.DataFrame) -> List[Dict[str, Any]]:
    variants = sorted(df["variant_name"].dropna().unique()) if "variant_name" in df.columns else []
    phases = sorted(df["phase"].dropna().unique()) if "phase" in df.columns else []
    missing_variants = missing_items(REQUIRED_VARIANTS, variants)
    missing_phases = missing_items(REQUIRED_PHASES, phases)
    return [
        check(
            not missing_variants,
            "required variants are present",
            "Missing variants: " + ", ".join(missing_variants) if missing_variants else f"Variants: {variants}",
        ),
        check(
            not missing_phases,
            "required phases are present",
            "Missing phases: " + ", ".join(missing_phases) if missing_phases else f"Phases: {phases}",
        ),
    ]


def check_context_corruption(analysis_dir: Path, df: pd.DataFrame) -> List[Dict[str, Any]]:
    context_path = analysis_dir / f"{ANALYSIS_ID}_context_corruption.csv"
    if not context_path.exists():
        return [check(False, "context corruption summary exists", f"Missing {context_path.name}")]
    context = pd.read_csv(context_path)
    conditions = set(context.get("context_condition", pd.Series(dtype=str)).dropna().unique())
    required_conditions = {"clean", "context_dropout", "context_bleed", "wrong_world_injection"}
    missing_conditions = sorted(required_conditions - conditions)
    results = [
        check(
            not missing_conditions,
            "clean and corrupted context conditions are present",
            "Missing context conditions: " + ", ".join(missing_conditions)
            if missing_conditions
            else f"Context conditions: {sorted(conditions)}",
        )
    ]
    raw = df[df["phase"] == "context_corruption"].copy()
    clean = raw[raw["context_condition"] == "clean"]
    corrupted = raw[raw["context_condition"] != "clean"]
    if clean.empty or corrupted.empty:
        results.append(check(False, "clean vs corrupted context rows can be compared", "Clean or corrupted rows are absent."))
        return results
    compare_metrics = [
        "composition_accuracy",
        "route_table_accuracy",
        "world_margin",
        "wrong_world_activation",
        "context_confusion",
        "top1_world_accuracy",
    ]
    clean_group = clean.groupby(["variant_name", "seed"], dropna=False)[compare_metrics].mean().reset_index()
    corrupted_group = (
        corrupted.groupby(["variant_name", "seed", "context_condition", "context_corruption_level"], dropna=False)[compare_metrics]
        .mean()
        .reset_index()
    )
    merged = corrupted_group.merge(clean_group, on=["variant_name", "seed"], suffixes=("_corrupt", "_clean"))
    if merged.empty:
        results.append(check(False, "clean vs corrupted context metrics can be merged", "No comparable clean/corrupted rows."))
        return results
    any_difference = any(
        not np.allclose(
            merged[f"{metric}_corrupt"].to_numpy(dtype=float),
            merged[f"{metric}_clean"].to_numpy(dtype=float),
            equal_nan=True,
        )
        for metric in compare_metrics
    )
    results.append(
        check(
            any_difference,
            "corrupted context metrics are not identical to clean metrics across all rows",
            "At least one corruption metric differs from clean." if any_difference else "All compared corruption metrics match clean exactly.",
        )
    )
    return results


def check_recurrence_variants(df: pd.DataFrame) -> List[Dict[str, Any]]:
    eval_only = df[df["variant_name"] == "exp13_1_no_recurrence_at_eval"]
    throughout = df[df["variant_name"] == "exp13_1_no_recurrence_throughout"]
    results = [
        check(not eval_only.empty, "no-recurrence-at-eval rows exist", "Rows found." if not eval_only.empty else "No rows found."),
        check(not throughout.empty, "no-recurrence-throughout rows exist", "Rows found." if not throughout.empty else "No rows found."),
    ]
    if not eval_only.empty:
        results.append(
            check(
                bool(eval_only["recurrence_training"].eq(True).all() and eval_only["recurrence_evaluation"].eq(False).all()),
                "no-recurrence-at-eval keeps training recurrence metadata separate",
                "Expected recurrence_training=True and recurrence_evaluation=False.",
            )
        )
    if not throughout.empty:
        results.append(
            check(
                bool(throughout["recurrence_training"].eq(False).all() and throughout["recurrence_evaluation"].eq(False).all()),
                "no-recurrence-throughout is represented separately",
                "Expected recurrence_training=False and recurrence_evaluation=False.",
            )
        )
    return results


def check_lesions(analysis_dir: Path, df: pd.DataFrame) -> List[Dict[str, Any]]:
    lesion_path = analysis_dir / f"{ANALYSIS_ID}_lesion_metrics.csv"
    if not lesion_path.exists():
        return [check(False, "lesion metrics summary exists", f"Missing {lesion_path.name}")]
    lesion = pd.read_csv(lesion_path)
    conditions = set(lesion.get("lesion_condition", pd.Series(dtype=str)).dropna().unique())
    targeted = "targeted_critical_edges" in conditions
    random_baseline = bool({"random_count_matched_edges", "random_weight_distribution_matched_edges"}.intersection(conditions))
    raw_conditions = set(df[df["phase"] == "lesion_test"]["lesion_condition"].dropna().unique())
    return [
        check(targeted, "targeted route-field lesion is present", f"Lesion conditions: {sorted(conditions)}"),
        check(random_baseline, "matched/random lesion baseline is present", f"Lesion conditions: {sorted(conditions)}"),
        check(targeted and random_baseline and conditions.issubset(raw_conditions), "lesion summary conditions match raw lesion rows", f"Raw lesion conditions: {sorted(raw_conditions)}"),
    ]


def check_progress_log(analysis_dir: Path, manifest: Dict[str, Any]) -> List[Dict[str, Any]]:
    path = analysis_dir / "progress.jsonl"
    if not path.exists():
        return [check(False, "progress log exists", "Missing progress.jsonl")]
    rows: List[Dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    if not rows:
        return [check(False, "progress log has events", "progress.jsonl is empty")]
    keys = set().union(*(row.keys() for row in rows))
    required = {"completed_units", "total_units", "eta_seconds", "elapsed_seconds", "phase", "phase_completed", "phase_total"}
    missing = required - keys
    total_units = manifest.get("total_progress_units")
    completed = max(int(row.get("completed_units", 0)) for row in rows)
    return [
        check(not missing, "progress log includes ETA/rate fields", "Missing keys: " + ", ".join(sorted(missing)) if missing else "ETA/rate fields present."),
        check(total_units is None or completed >= int(total_units), "progress log reached planned total units", f"completed={completed}; manifest_total={total_units}"),
    ]


def check_report(analysis_dir: Path) -> List[Dict[str, Any]]:
    report_path = analysis_dir / "experiment_report.md"
    if not report_path.exists():
        return [check(False, "final report exists", f"Missing {report_path.name}")]
    text = report_path.read_text(encoding="utf-8").lower()
    missing_required = [phrase for phrase in ("caveats", "expected patterns only") if phrase not in text]
    forbidden_present = [phrase for phrase in FORBIDDEN_REPORT_PHRASES if phrase in text]
    return [
        check(
            not missing_required,
            "report includes caveats and expected-pattern framing",
            "Missing phrases: " + ", ".join(missing_required) if missing_required else "Report includes caveats and expected-pattern framing.",
        ),
        check(
            not forbidden_present,
            "report does not overclaim with forbidden phrases",
            "Forbidden phrases present: " + ", ".join(forbidden_present) if forbidden_present else "No forbidden overclaim phrases found.",
        ),
    ]


def write_validation_outputs(analysis_dir: Path, results: List[Dict[str, Any]]) -> None:
    analysis_dir.mkdir(parents=True, exist_ok=True)
    failed = [item for item in results if item["status"] == FAIL]
    warned = [item for item in results if item["status"] == WARN]
    lines = ["# Experiment 13.1 Validation Report", ""]
    for result in results:
        lines.append(f"## {result['status']}: {result['name']}")
        lines.append("")
        lines.append(str(result["detail"]))
        lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- pass: {sum(1 for r in results if r['status'] == PASS)}")
    lines.append(f"- warn: {len(warned)}")
    lines.append(f"- fail: {len(failed)}")
    (analysis_dir / "validation_results.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    (analysis_dir / "validation_report.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Experiment 13.1 outputs.")
    parser.add_argument("--experiment-dir", default=str(Path(__file__).resolve().parent))
    parser.add_argument("--run-id", default="latest", help="Run ID under analysis/. Use 'latest' to validate the newest run.")
    parser.add_argument("--analysis-dir", default=None, help="Exact analysis directory to validate.")
    parser.add_argument("--fail-on-warn", action="store_true")
    args = parser.parse_args()

    analysis_dir = resolve_analysis_dir(args)
    results: List[Dict[str, Any]] = []
    results.append(check(analysis_dir.exists(), "analysis directory exists", str(analysis_dir)))
    if not analysis_dir.exists():
        write_validation_outputs(analysis_dir, results)
        return 1

    manifest = load_manifest(analysis_dir)
    results.extend(check_required_files(analysis_dir))
    results.extend(check_manifest(analysis_dir, manifest))

    metrics_path = analysis_dir / "metrics.csv"
    if not metrics_path.exists():
        results.append(check(False, "raw metrics file can be loaded", f"Missing {metrics_path.name}"))
        write_validation_outputs(analysis_dir, results)
        return 1

    df = pd.read_csv(metrics_path)
    results.append(check(not df.empty, "raw metrics are non-empty", f"rows={len(df)}"))
    results.extend(check_columns(df))
    results.extend(check_metric_values(df))
    results.extend(check_required_variants_and_phases(df))
    results.extend(check_context_corruption(analysis_dir, df))
    results.extend(check_recurrence_variants(df))
    results.extend(check_lesions(analysis_dir, df))
    results.extend(check_progress_log(analysis_dir, manifest))
    results.extend(check_report(analysis_dir))

    write_validation_outputs(analysis_dir, results)
    print("Experiment 13.1 validation summary:")
    print(f"Analysis directory: {analysis_dir}")
    for result in results:
        print(f"[{result['status']}] {result['name']}: {result['detail']}")

    failed = [item for item in results if item["status"] == FAIL]
    warned = [item for item in results if item["status"] == WARN]
    if failed:
        return 1
    if warned and args.fail_on_warn:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
