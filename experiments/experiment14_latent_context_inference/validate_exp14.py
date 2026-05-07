#!/usr/bin/env python3
"""Validation checks for Experiment 14 latent context inference artifacts."""

from __future__ import annotations

import argparse
import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

import pandas as pd


EXPERIMENT_NAME = "exp14_latent_context_inference"
ANALYSIS_ID = "exp14"
REQUIRED_FILES = [
    "exp14_metrics.csv",
    "metrics.csv",
    "exp14_summary.csv",
    "exp14_effect_sizes.csv",
    "run_manifest.json",
    "progress.jsonl",
    "experiment_report.md",
]
REQUIRED_COLUMNS = [
    "experiment_name",
    "analysis_id",
    "schema_version",
    "phase",
    "seed",
    "world_count",
    "route_length",
    "variant",
    "cue_count",
    "corruption_rate",
    "composition_accuracy_seen_route",
    "composition_accuracy_suffix_route",
    "world_selection_accuracy_seen_route",
    "world_selection_accuracy_suffix_route",
    "first_step_context_accuracy",
    "mean_world_margin_seen_route",
]
REQUIRED_VARIANTS = [
    "exp14_cirm_latent_selector",
    "baseline_oracle_context_gated_table",
    "baseline_shared_no_context_table",
    "baseline_route_endpoint_memorizer_with_latent_selector",
    "baseline_random_context_selector",
    "baseline_recency_context_selector",
]
REQUIRED_PHASES = ["latent_context_inference"]


@dataclass
class Check:
    status: str
    name: str
    detail: str


def newest_run_dir(analysis_root: Path) -> Path:
    candidates = [p for p in analysis_root.glob(f"{ANALYSIS_ID}_*") if p.is_dir()]
    if not candidates:
        raise FileNotFoundError(f"No {ANALYSIS_ID}_* directories found under {analysis_root}")
    return max(candidates, key=lambda p: p.stat().st_mtime)


def add_check(checks: List[Check], status: str, name: str, detail: str) -> None:
    checks.append(Check(status=status, name=name, detail=detail))


def metric_mean(summary: pd.DataFrame, *, variant: str, metric: str, clean: bool = True, hardest: bool = True) -> float:
    df = summary[summary["variant"] == variant].copy()
    if clean:
        df = df[df["corruption_rate"] == 0.0]
    if hardest and not df.empty:
        max_world = df["world_count"].max()
        max_route = df["route_length"].max()
        max_cue = df["cue_count"].max()
        df = df[(df["world_count"] == max_world) & (df["route_length"] == max_route) & (df["cue_count"] == max_cue)]
    if df.empty:
        return float("nan")
    return float(df[f"{metric}_mean"].mean())


def run_validation(analysis_dir: Path) -> Dict[str, Any]:
    checks: List[Check] = []
    for filename in REQUIRED_FILES:
        path = analysis_dir / filename
        add_check(checks, "PASS" if path.exists() else "FAIL", f"file exists: {filename}", str(path))

    metrics_path = analysis_dir / "exp14_metrics.csv"
    summary_path = analysis_dir / "exp14_summary.csv"
    effects_path = analysis_dir / "exp14_effect_sizes.csv"
    manifest_path = analysis_dir / "run_manifest.json"

    metrics = pd.read_csv(metrics_path) if metrics_path.exists() else pd.DataFrame()
    summary = pd.read_csv(summary_path) if summary_path.exists() else pd.DataFrame()
    effects = pd.read_csv(effects_path) if effects_path.exists() else pd.DataFrame()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}

    add_check(checks, "PASS" if len(metrics) > 0 else "FAIL", "metrics row count", f"{len(metrics)} rows")
    add_check(checks, "PASS" if len(summary) > 0 else "FAIL", "summary row count", f"{len(summary)} rows")
    add_check(checks, "PASS" if len(effects) > 0 else "WARN", "effect sizes row count", f"{len(effects)} rows")

    missing_cols = [c for c in REQUIRED_COLUMNS if c not in metrics.columns]
    add_check(checks, "PASS" if not missing_cols else "FAIL", "required metric columns", f"missing={missing_cols}")

    phases = set(metrics["phase"].dropna().unique()) if "phase" in metrics else set()
    missing_phases = [p for p in REQUIRED_PHASES if p not in phases]
    add_check(checks, "PASS" if not missing_phases else "FAIL", "required phases present", f"missing={missing_phases}")

    variants = set(metrics["variant"].dropna().unique()) if "variant" in metrics else set()
    missing_variants = [v for v in REQUIRED_VARIANTS if v not in variants]
    hash_variants = [v for v in variants if str(v).startswith("baseline_hash_slot_selector")]
    variant_status = "PASS" if not missing_variants and hash_variants else "FAIL"
    add_check(checks, variant_status, "required variants present", f"missing={missing_variants}; hash_variants={sorted(hash_variants)}")

    seed_count = int(metrics["seed"].nunique()) if "seed" in metrics else 0
    add_check(checks, "PASS" if seed_count > 0 else "FAIL", "seed count nonzero", f"seed_count={seed_count}")

    add_check(
        checks,
        "PASS" if manifest.get("experiment_name") == EXPERIMENT_NAME else "FAIL",
        "manifest experiment name",
        str(manifest.get("experiment_name")),
    )
    device = manifest.get("device", {})
    add_check(
        checks,
        "PASS" if device.get("gpu_used") is False and device.get("cpu_count") else "FAIL",
        "device metadata present",
        json.dumps(device)[:400],
    )

    sqlite_rel = manifest.get("artifact_paths", {}).get("sqlite_db")
    if sqlite_rel:
        # SQLite path is repo-relative from the experiment directory. Resolve relative to analysis_dir parent.
        experiment_dir = analysis_dir.parent.parent if analysis_dir.parent.name == "analysis" else analysis_dir.parent
        sqlite_path = experiment_dir / sqlite_rel
        if not sqlite_path.exists():
            sqlite_path = Path(sqlite_rel)
        add_check(checks, "PASS" if sqlite_path.exists() else "FAIL", "sqlite db exists", str(sqlite_path))
        if sqlite_path.exists():
            with sqlite3.connect(sqlite_path) as conn:
                tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name", conn)["name"].tolist()
            expected_tables = {"metrics", "summary", "effect_sizes", "manifest"}
            add_check(checks, "PASS" if expected_tables.issubset(set(tables)) else "FAIL", "sqlite tables", json.dumps(tables))
    else:
        add_check(checks, "WARN", "sqlite db exists", "SQLite was not requested for this run")

    # Scientific sanity checks. They are deliberately conservative and tied to the hardest clean condition.
    if not summary.empty:
        oracle_comp = metric_mean(summary, variant="baseline_oracle_context_gated_table", metric="composition_accuracy_seen_route")
        cirm_world = metric_mean(summary, variant="exp14_cirm_latent_selector", metric="world_selection_accuracy_seen_route")
        cirm_comp = metric_mean(summary, variant="exp14_cirm_latent_selector", metric="composition_accuracy_seen_route")
        shared_comp = metric_mean(summary, variant="baseline_shared_no_context_table", metric="composition_accuracy_seen_route")
        endpoint_suffix = metric_mean(summary, variant="baseline_route_endpoint_memorizer_with_latent_selector", metric="composition_accuracy_suffix_route")
        random_world = metric_mean(summary, variant="baseline_random_context_selector", metric="world_selection_accuracy_seen_route")

        add_check(checks, "PASS" if oracle_comp >= 0.99 else "FAIL", "oracle context upper bound solves clean seen routes", f"mean={oracle_comp:.4f}")
        add_check(checks, "PASS" if cirm_world >= 0.99 else "FAIL", "CIRM latent selector identifies clean context", f"mean={cirm_world:.4f}")
        add_check(checks, "PASS" if cirm_comp >= 0.99 else "FAIL", "CIRM latent selector composes clean seen routes", f"mean={cirm_comp:.4f}")
        add_check(checks, "PASS" if shared_comp < 0.50 else "FAIL", "shared no-context table underperforms clean seen routes", f"mean={shared_comp:.4f}")
        add_check(checks, "PASS" if endpoint_suffix < 0.10 else "FAIL", "endpoint memorizer fails suffix routes", f"mean={endpoint_suffix:.4f}")
        add_check(checks, "PASS" if random_world < 0.50 else "WARN", "random selector below useful context selection", f"mean={random_world:.4f}")

        max_corruption = float(summary["corruption_rate"].max())
        max_world = int(summary["world_count"].max())
        max_route = int(summary["route_length"].max())
        max_cue = int(summary["cue_count"].max())
        clean_row = summary[
            (summary["variant"] == "exp14_cirm_latent_selector")
            & (summary["world_count"] == max_world)
            & (summary["route_length"] == max_route)
            & (summary["cue_count"] == max_cue)
            & (summary["corruption_rate"] == 0.0)
        ]
        corrupt_row = summary[
            (summary["variant"] == "exp14_cirm_latent_selector")
            & (summary["world_count"] == max_world)
            & (summary["route_length"] == max_route)
            & (summary["cue_count"] == max_cue)
            & (summary["corruption_rate"] == max_corruption)
        ]
        if not clean_row.empty and not corrupt_row.empty:
            clean_world = float(clean_row.iloc[0]["world_selection_accuracy_seen_route_mean"])
            corrupt_world = float(corrupt_row.iloc[0]["world_selection_accuracy_seen_route_mean"])
            add_check(
                checks,
                "PASS" if corrupt_world < clean_world else "WARN",
                "corruption reduces or challenges CIRM context selection",
                f"clean={clean_world:.4f}; max_corruption={max_corruption}; corrupted={corrupt_world:.4f}",
            )

    plot_dir = analysis_dir / "plots"
    png_count = len(list(plot_dir.glob("*.png"))) if plot_dir.exists() else 0
    add_check(checks, "PASS" if png_count >= 6 else "FAIL", "plots generated", f"{png_count} png files")

    progress_path = analysis_dir / "progress.jsonl"
    if progress_path.exists():
        text = progress_path.read_text(encoding="utf-8")
        add_check(checks, "PASS" if '"event": "run_complete"' in text else "FAIL", "progress has run_complete", f"events={len(text.splitlines())}")
    else:
        add_check(checks, "FAIL", "progress has run_complete", "progress.jsonl missing")

    pass_count = sum(1 for c in checks if c.status == "PASS")
    warn_count = sum(1 for c in checks if c.status == "WARN")
    fail_count = sum(1 for c in checks if c.status == "FAIL")
    status = "FAIL" if fail_count else "PASS"
    return {
        "experiment_name": EXPERIMENT_NAME,
        "analysis_id": ANALYSIS_ID,
        "analysis_dir": str(analysis_dir),
        "status": status,
        "pass_count": pass_count,
        "warn_count": warn_count,
        "fail_count": fail_count,
        "checks": [c.__dict__ for c in checks],
    }


def write_report(result: Dict[str, Any], analysis_dir: Path) -> None:
    lines = [
        "# Experiment 14 Validation Report",
        "",
        f"- Analysis directory: `{analysis_dir}`",
        f"- Status: **{result['status']}**",
        f"- PASS: {result['pass_count']}",
        f"- WARN: {result['warn_count']}",
        f"- FAIL: {result['fail_count']}",
        "",
        "## Checks",
        "",
        "| Status | Check | Detail |",
        "|---|---|---|",
    ]
    for check in result["checks"]:
        detail = str(check["detail"]).replace("|", "\\|")
        lines.append(f"| {check['status']} | {check['name']} | {detail} |")
    (analysis_dir / "validation_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (analysis_dir / "validation_results.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Experiment 14 artifacts.")
    parser.add_argument("--analysis-root", default="analysis", help="Root analysis directory containing exp14_* run directories.")
    parser.add_argument("--analysis-dir", default=None, help="Specific analysis run directory to validate.")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    analysis_dir = Path(args.analysis_dir) if args.analysis_dir else newest_run_dir(Path(args.analysis_root))
    result = run_validation(analysis_dir)
    write_report(result, analysis_dir)
    print(f"[{EXPERIMENT_NAME}] Validation {result['status']}: PASS={result['pass_count']} WARN={result['warn_count']} FAIL={result['fail_count']}")
    print(f"[{EXPERIMENT_NAME}] Report: {analysis_dir / 'validation_report.md'}")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
