#!/usr/bin/env python3
"""Validation checks for Experiment 13 outputs.

The goal is not to force a predetermined result. The goal is to detect whether the run
actually exercised the planned scientific contrasts: capacity breaking, context corruption,
recurrence/composition separation, no-world-context interference, primitive holdout failure,
and continuous front-end degradation.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

import numpy as np
import pandas as pd


PASS = "PASS"
WARN = "WARN"
FAIL = "FAIL"


def mean_at(df: pd.DataFrame, **filters) -> float:
    sub = df.copy()
    for k, v in filters.items():
        if isinstance(v, (list, tuple, set)):
            sub = sub[sub[k].isin(v)]
        else:
            sub = sub[sub[k] == v]
    if sub.empty:
        return float("nan")
    return float(sub["composition_accuracy"].mean())


def check(condition: bool, name: str, detail: str, severity: str = FAIL) -> Dict[str, Any]:
    return {
        "status": PASS if condition else severity,
        "name": name,
        "detail": detail,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Experiment 13 analysis outputs.")
    parser.add_argument("--analysis-dir", default="analysis")
    parser.add_argument("--fail-on-warn", action="store_true")
    args = parser.parse_args()

    analysis_dir = Path(args.analysis_dir)
    metrics_path = analysis_dir / "metrics.csv"
    if not metrics_path.exists():
        raise FileNotFoundError(f"Could not find {metrics_path}")

    df = pd.read_csv(metrics_path)
    results: List[Dict[str, Any]] = []

    required_phases = {
        "capacity_pressure",
        "local_capacity_pressure",
        "context_corruption",
        "continual_retention_pressure",
        "true_holdout_generalization",
        "continuous_frontend_bridge",
    }
    phases = set(df["phase"].dropna().unique())
    results.append(check(required_phases.issubset(phases), "all phases executed", f"Found phases: {sorted(phases)}"))

    # 1. Full model should be excellent at exact/surplus capacity under clean symbolic conditions.
    cap = df[df["phase"] == "capacity_pressure"]
    full_exact = cap[
        (cap["run_name"] == "exp13_full_context_separated_memory")
        & (cap["budget_ratio"] >= 1.0)
        & (cap["route_length"] >= 4)
    ]["composition_accuracy"].mean()
    results.append(check(full_exact > 0.90, "full model succeeds at exact/surplus capacity", f"mean={full_exact:.4f}"))

    # 2. Full model should degrade under below-capacity budgets.
    full_low = cap[
        (cap["run_name"] == "exp13_full_context_separated_memory")
        & (cap["budget_ratio"] <= 0.5)
        & (cap["route_length"] >= 4)
    ]["composition_accuracy"].mean()
    results.append(check(full_low < full_exact - 0.10, "finite memory pressure creates a breaking curve", f"low={full_low:.4f}, exact={full_exact:.4f}"))

    # 3. No recurrence should preserve more one-step/table behavior than multi-step composition.
    norec = cap[(cap["run_name"] == "exp13_no_recurrence") & (cap["budget_ratio"] >= 1.0)]
    if not norec.empty:
        route_table = norec["route_route_table_accuracy"].mean()
        multi_comp = norec[norec["route_length"] >= 4]["composition_accuracy"].mean()
        results.append(check(route_table - multi_comp > 0.50, "no-recurrence separates one-step storage from composition", f"route_table={route_table:.4f}, multi_comp={multi_comp:.4f}"))
    else:
        results.append(check(False, "no-recurrence data present", "No no-recurrence rows found"))

    # 4. No-world-context should be worse than full under exact capacity.
    nwc_exact = cap[
        (cap["run_name"] == "exp13_no_world_context")
        & (cap["budget_ratio"] >= 1.0)
        & (cap["route_length"] >= 4)
    ]["composition_accuracy"].mean()
    results.append(check(nwc_exact < full_exact - 0.30, "no-world-context shows interference", f"no_world_context={nwc_exact:.4f}, full={full_exact:.4f}"))

    # 5. Adversarial context corruption should collapse world selection around/after 0.5 for context-using variants.
    ctx = df[(df["phase"] == "context_corruption") & (df["context_corruption_type"] == "adversarial_mixture")]
    full_ctx_low = ctx[(ctx["run_name"] == "exp13_full_context_separated_memory") & (ctx["context_corruption_level"] <= 0.25)]["top1_world_accuracy"].mean()
    full_ctx_high = ctx[(ctx["run_name"] == "exp13_full_context_separated_memory") & (ctx["context_corruption_level"] >= 0.60)]["top1_world_accuracy"].mean()
    results.append(check(full_ctx_low - full_ctx_high > 0.50, "adversarial context corruption creates world-selection failure", f"low={full_ctx_low:.4f}, high={full_ctx_high:.4f}"))

    # 6. Primitive holdout should distinguish seen primitives from unseen primitives.
    hold = df[df["phase"] == "true_holdout_generalization"]
    seen = hold[
        (hold["run_name"] == "exp13_full_context_separated_memory")
        & (hold["generalization_condition"] == "compositions_from_seen_primitives")
        & (hold["primitive_holdout_rate"] >= 0.2)
    ]["composition_accuracy"].mean()
    unseen = hold[
        (hold["run_name"] == "exp13_full_context_separated_memory")
        & (hold["generalization_condition"] == "routes_requiring_unseen_primitives")
        & (hold["primitive_holdout_rate"] >= 0.2)
    ]["composition_accuracy"].mean()
    results.append(check(seen - unseen > 0.20, "primitive holdout separates composition from unseen-transition inference", f"seen={seen:.4f}, unseen={unseen:.4f}"))

    # 7. Continuous bridge should degrade with high perceptual noise.
    cont = df[df["phase"] == "continuous_frontend_bridge"]
    cont_full = cont[cont["run_name"] == "exp13_full_context_separated_memory"]
    low_noise = cont_full[cont_full["continuous_noise"] <= 0.10]["composition_accuracy"].mean()
    high_noise = cont_full[cont_full["continuous_noise"] >= 0.75]["composition_accuracy"].mean()
    results.append(check(low_noise - high_noise > 0.20, "continuous front-end degrades under perceptual noise", f"low={low_noise:.4f}, high={high_noise:.4f}"))

    # 8. Consolidation should alter behavior or retention under finite memory pressure. This is a warning if not observed.
    ret = df[(df["phase"] == "continual_retention_pressure") & (df["budget_ratio"] <= 0.75)]
    no_cons = ret[ret["run_name"] == "exp13_no_consolidation"]["composition_accuracy"].mean()
    strong_cons = ret[ret["run_name"] == "exp13_strong_consolidation"]["composition_accuracy"].mean()
    delta = abs(strong_cons - no_cons)
    results.append(check(delta > 0.02, "consolidation changes finite-pressure behavior", f"no_consolidation={no_cons:.4f}, strong={strong_cons:.4f}, delta={delta:.4f}", severity=WARN))

    failed = [r for r in results if r["status"] == FAIL]
    warned = [r for r in results if r["status"] == WARN]

    report_lines = ["# Experiment 13 Validation Report", ""]
    for r in results:
        report_lines.append(f"## {r['status']}: {r['name']}")
        report_lines.append("")
        report_lines.append(str(r["detail"]))
        report_lines.append("")
    report_lines.append("## Summary")
    report_lines.append("")
    report_lines.append(f"- pass: {sum(1 for r in results if r['status'] == PASS)}")
    report_lines.append(f"- warn: {len(warned)}")
    report_lines.append(f"- fail: {len(failed)}")

    (analysis_dir / "validation_results.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    (analysis_dir / "validation_report.md").write_text("\n".join(report_lines), encoding="utf-8")

    print("Experiment 13 validation summary:")
    for r in results:
        print(f"[{r['status']}] {r['name']}: {r['detail']}")

    if failed:
        return 1
    if warned and args.fail_on_warn:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
