#!/usr/bin/env python
"""Build a claim-scoped reproducibility summary from committed artifacts.

The script is intentionally stdlib-only and reads preserved outputs without
rerunning experiments or modifying historical experiment directories.
"""

from __future__ import annotations

import csv
import math
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean


REPO_ROOT = Path(__file__).resolve().parents[1]

CLAIM_MAP = Path("docs/manuscript/source_data/manuscript_claim_artifact_map.csv")
READINESS = Path("docs/source_data/STATISTICAL_REPORTING_READINESS.csv")
TABLE3_SOURCE = Path("docs/manuscript/source_data/table_03_compact_final_safe.csv")
TABLE4_SOURCE = Path("docs/manuscript/source_data/table_04_exp15_neural_comparator.csv")

OUTPUT_SUMMARY = Path("docs/manuscript/source_data/reproducibility_claim_summary.csv")
OUTPUT_SEED = Path("docs/manuscript/source_data/seed_level_core_claim_metrics.csv")
OUTPUT_TABLE = Path("docs/manuscript/tables/table_reproducibility_claim_summary.md")
OUTPUT_REPORT = Path("docs/repo_audit/CLAIM_SCOPED_REPRODUCIBILITY_SUMMARY_REPORT.md")

EXP12_METRICS = Path("experiments/experiment12_capacity_generalization/analysis/exp12/metrics.csv")
EXP13_METRICS = Path("experiments/experiment13_breaking_point/analysis/metrics.csv")
EXP14_METRICS = Path(
    "experiments/experiment14_latent_context_inference/analysis/"
    "exp14_full_20260507_210712/exp14_metrics.csv"
)
EXP15_SEED_METRICS = Path(
    "experiments/experiment15_neural_baseline_comparator/analysis/"
    "exp15_full_20260508_092811/exp15_seed_metrics.csv"
)

PARSED_INPUTS = [
    CLAIM_MAP,
    Path("docs/manuscript/MANUSCRIPT_REPRODUCIBILITY_MAP.md"),
    Path("docs/repo_audit/MANUSCRIPT_REPRODUCIBILITY_PROTOCOL.md"),
    Path("docs/repo_audit/MANUSCRIPT_REPRODUCIBILITY_REPORT.md"),
    Path("docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md"),
    READINESS,
    Path("docs/manuscript/tables/table_03_compact_final_safe.md"),
    TABLE3_SOURCE,
    Path("docs/manuscript/tables/table_04_exp15_neural_comparator.md"),
    TABLE4_SOURCE,
    Path("experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv"),
    EXP12_METRICS,
    Path("experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv"),
    Path("experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv"),
    EXP13_METRICS,
    Path(
        "experiments/experiment13_1_publication_hardening/analysis/"
        "exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv"
    ),
    Path(
        "experiments/experiment13_1_publication_hardening/analysis/"
        "exp13_1_full_20260506_214756/exp13_1_ablation_metrics.csv"
    ),
    Path(
        "experiments/experiment13_2_baseline_suite/analysis/"
        "exp13_2_full_20260507_165813/exp13_2_summary.csv"
    ),
    Path(
        "experiments/experiment13_2_baseline_suite/analysis/"
        "exp13_2_full_20260507_165813/exp13_2_effect_sizes.csv"
    ),
    Path(
        "experiments/experiment14_latent_context_inference/analysis/"
        "exp14_full_20260507_210712/exp14_summary.csv"
    ),
    Path(
        "experiments/experiment14_latent_context_inference/analysis/"
        "exp14_full_20260507_210712/exp14_effect_sizes.csv"
    ),
    EXP14_METRICS,
    Path(
        "experiments/experiment15_neural_baseline_comparator/analysis/"
        "exp15_full_20260508_092811/exp15_summary.csv"
    ),
    EXP15_SEED_METRICS,
    Path(
        "experiments/experiment15_neural_baseline_comparator/analysis/"
        "exp15_full_20260508_092811/exp15_effect_sizes.csv"
    ),
]

RETAINED_CLAIMS = ["C1", "C2", "C3", "C4", "C5", "C6", "C13", "C12"]


def repo_path(path: Path) -> Path:
    return REPO_ROOT / path


def read_csv(path: Path) -> list[dict[str, str]]:
    with repo_path(path).open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def read_csv_stream(path: Path):
    with repo_path(path).open("r", encoding="utf-8-sig", newline="") as handle:
        yield from csv.DictReader(handle)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    full_path = repo_path(path)
    full_path.parent.mkdir(parents=True, exist_ok=True)
    with full_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def fnum(value: object, digits: int = 4) -> str:
    if value in ("", None):
        return ""
    try:
        number = float(value)
    except (TypeError, ValueError):
        return str(value)
    if math.isinf(number):
        return "inf" if number > 0 else "-inf"
    if math.isnan(number):
        return "nan"
    return f"{number:.{digits}f}"


def split_semicolon(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def load_control_rows() -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]], dict[str, dict[str, str]]]:
    claim_rows = {row["claim_id"]: row for row in read_csv(CLAIM_MAP)}
    table3_rows = {row["claim_id"]: row for row in read_csv(TABLE3_SOURCE)}
    readiness_rows = {row["claim_id"]: row for row in read_csv(READINESS)}
    return claim_rows, table3_rows, readiness_rows


def aggregate_seed_metric(
    target: list[dict[str, object]],
    claim_id: str,
    experiment_id: str,
    source: Path,
    groups: dict[tuple[str, ...], list[float]],
    key_fields: list[str],
    metric_name: str,
    variant: str,
    run_id: str,
    extra_by_key: dict[tuple[str, ...], dict[str, str]] | None = None,
) -> None:
    for key in sorted(groups):
        values = groups[key]
        if not values:
            continue
        key_map = dict(zip(key_fields, key))
        extra = (extra_by_key or {}).get(key, {})
        target.append(
            {
                "claim_id": claim_id,
                "experiment_id": experiment_id,
                "run_id": run_id,
                "seed": key_map.get("seed", ""),
                "variant": variant,
                "world_count": key_map.get("world_count", ""),
                "route_length": key_map.get("route_length", ""),
                "metric_name": metric_name,
                "metric_value": fnum(mean(values), 8),
                "source_artifact": source.as_posix(),
                "budget_ratio": extra.get("budget_ratio", ""),
                "cue_count": extra.get("cue_count", ""),
                "corruption_rate": extra.get("corruption_rate", ""),
                "probe_type": extra.get("probe_type", ""),
                "aggregation_note": "mean across repeated source rows for the same seed and condition",
            }
        )


def build_exp12_seed_rows() -> list[dict[str, object]]:
    groups: dict[str, dict[tuple[str, ...], list[float]]] = {
        "composition_accuracy": defaultdict(list),
        "route_route_table_accuracy": defaultdict(list),
    }
    for row in read_csv_stream(EXP12_METRICS):
        if row.get("phase") != "capacity_final":
            continue
        if row.get("run_name") != "exp12_full_context_separated_memory":
            continue
        key = (row["seed"], row["world_count"], row["route_length"])
        for metric in groups:
            groups[metric][key].append(float(row[metric]))

    rows: list[dict[str, object]] = []
    for metric, metric_groups in groups.items():
        aggregate_seed_metric(
            rows,
            "C5",
            "Exp12",
            EXP12_METRICS,
            metric_groups,
            ["seed", "world_count", "route_length"],
            metric,
            "exp12_full_context_separated_memory",
            "capacity_final",
        )
    return rows


def build_exp13_seed_rows() -> list[dict[str, object]]:
    groups: dict[str, dict[tuple[str, ...], list[float]]] = {
        "composition_accuracy": defaultdict(list),
        "route_route_table_accuracy": defaultdict(list),
    }
    extras: dict[tuple[str, ...], dict[str, str]] = {}
    for row in read_csv_stream(EXP13_METRICS):
        if row.get("phase") != "capacity_pressure":
            continue
        if row.get("run_name") != "exp13_full_context_separated_memory":
            continue
        key = (row["seed"], row["world_count"], row["route_length"], row["budget_ratio"])
        extras[key] = {"budget_ratio": row["budget_ratio"]}
        for metric in groups:
            groups[metric][key].append(float(row[metric]))

    rows: list[dict[str, object]] = []
    for metric, metric_groups in groups.items():
        aggregate_seed_metric(
            rows,
            "C6",
            "Exp13",
            EXP13_METRICS,
            metric_groups,
            ["seed", "world_count", "route_length", "budget_ratio"],
            metric,
            "exp13_full_context_separated_memory",
            "capacity_pressure",
            extras,
        )
    return rows


def add_exp14_metric_rows(target: list[dict[str, object]], claim_id: str, variants: set[str], metrics: set[str]) -> None:
    for row in read_csv_stream(EXP14_METRICS):
        if row.get("variant") not in variants:
            continue
        if row.get("world_count") != "32" or row.get("route_length") != "16" or row.get("cue_count") != "8":
            continue
        for metric in sorted(metrics):
            target.append(
                {
                    "claim_id": claim_id,
                    "experiment_id": "Exp14",
                    "run_id": row.get("analysis_id", "exp14"),
                    "seed": row["seed"],
                    "variant": row["variant"],
                    "world_count": row["world_count"],
                    "route_length": row["route_length"],
                    "metric_name": metric,
                    "metric_value": row[metric],
                    "source_artifact": EXP14_METRICS.as_posix(),
                    "budget_ratio": "",
                    "cue_count": row["cue_count"],
                    "corruption_rate": row["corruption_rate"],
                    "probe_type": "",
                    "aggregation_note": "direct seed-level row from Exp14 metrics",
                }
            )


def add_exp15_metric_rows(target: list[dict[str, object]], claim_id: str, variants: set[str] | None, metrics: set[str]) -> None:
    for row in read_csv_stream(EXP15_SEED_METRICS):
        if variants is not None and row.get("variant") not in variants:
            continue
        if row.get("metric_name") not in metrics:
            continue
        target.append(
            {
                "claim_id": claim_id,
                "experiment_id": "Exp15",
                "run_id": row.get("run_id", ""),
                "seed": row["seed"],
                "variant": row["variant"],
                "world_count": row["world_count"],
                "route_length": row["route_length"],
                "metric_name": row["metric_name"],
                "metric_value": row["metric_value"],
                "source_artifact": EXP15_SEED_METRICS.as_posix(),
                "budget_ratio": "",
                "cue_count": "",
                "corruption_rate": "",
                "probe_type": row.get("probe_type", ""),
                "aggregation_note": "direct seed-level row from Exp15 seed_metrics",
            }
        )


def build_seed_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    rows.extend(build_exp12_seed_rows())
    rows.extend(build_exp13_seed_rows())

    exp14_metrics = {
        "composition_accuracy_seen_route",
        "composition_accuracy_suffix_route",
        "world_selection_accuracy_seen_route",
        "first_step_context_accuracy",
    }
    add_exp14_metric_rows(
        rows,
        "C13",
        {"exp14_cirm_latent_selector", "baseline_oracle_context_gated_table", "baseline_shared_no_context_table"},
        exp14_metrics,
    )
    add_exp14_metric_rows(
        rows,
        "C2",
        {"exp14_cirm_latent_selector", "baseline_shared_no_context_table"},
        {"composition_accuracy_seen_route", "first_step_context_accuracy", "world_selection_accuracy_seen_route"},
    )
    add_exp14_metric_rows(
        rows,
        "C4",
        {"baseline_route_endpoint_memorizer_with_latent_selector", "exp14_cirm_latent_selector"},
        {"composition_accuracy_seen_route", "composition_accuracy_suffix_route", "first_step_context_accuracy"},
    )

    exp15_core_metrics = {
        "first_step_context_conflict_accuracy",
        "seen_route_composition_accuracy",
        "suffix_route_composition_accuracy",
        "transition_accuracy",
        "retention_after_sequential_worlds",
    }
    add_exp15_metric_rows(rows, "C12", None, exp15_core_metrics)
    add_exp15_metric_rows(
        rows,
        "C2",
        {"neural_transition_mlp_context", "neural_transition_mlp_no_context", "neural_transition_mlp_world_heads_context"},
        {"first_step_context_conflict_accuracy", "seen_route_composition_accuracy", "suffix_route_composition_accuracy"},
    )
    add_exp15_metric_rows(
        rows,
        "C4",
        {"neural_gru_endpoint_context", "neural_transition_mlp_context", "neural_transition_mlp_world_heads_context"},
        {"seen_route_composition_accuracy", "suffix_route_composition_accuracy", "transition_accuracy"},
    )
    return rows


def source_path_summary(rows: list[dict[str, object]]) -> dict[str, dict[str, int]]:
    summary: dict[str, dict[str, int]] = defaultdict(lambda: {"rows": 0, "seeds": set()})  # type: ignore[dict-item]
    for row in rows:
        source = str(row["source_artifact"])
        summary[source]["rows"] += 1
        if row.get("seed") != "":
            summary[source]["seeds"].add(str(row["seed"]))  # type: ignore[attr-defined]
    return summary


def build_summary_rows(seed_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    claim_rows, table3_rows, readiness_rows = load_control_rows()
    seed_summary = source_path_summary(seed_rows)

    def seed_note(*paths: Path) -> str:
        parts = []
        for path in paths:
            info = seed_summary.get(path.as_posix())
            if info:
                parts.append(f"{len(info['seeds'])} seeds from {path.name}")  # type: ignore[arg-type]
        return "; ".join(parts) if parts else "aggregate-only in parsed claim artifacts"

    rows: list[dict[str, object]] = []
    configs = {
        "C1": {
            "experiment_ids": "Exp13.1; Exp13.2; Exp15",
            "metric_family": "route-table formation; route execution; structural ablation",
            "n_units": "Exp13.1 aggregate rows report n=20 per selected structure-audit variant; Exp13.2 aggregate n=20; Exp15 seed rows available for boundary context",
            "summary_value": "Exp13.1 full model route_table_accuracy=1.000 and composition_accuracy=1.000; no structural plasticity route_table_accuracy=0.0286 and composition_accuracy=0.0317.",
            "interval_or_spread": "descriptive means and SDs available in aggregate artifacts; final comparison-family intervals not claimed",
            "effect_size": "not_claimed",
            "status": "descriptive_support_available; seed-level comparison grouping pending",
        },
        "C2": {
            "experiment_ids": "Exp13.2; Exp14; Exp15",
            "metric_family": "context/world indexing; first-step conflict; full-route disambiguation",
            "n_units": seed_note(EXP14_METRICS, EXP15_SEED_METRICS) + "; Exp13.2 is aggregate summary",
            "summary_value": "Context-sensitive first-step/full-route disambiguation is supported in selected symbolic and neural comparator slices; no-context suffix success is preserved as a caveat.",
            "interval_or_spread": "Exp14 and Exp15 expose seed-level rows; C2-wide comparison-family intervals remain pending",
            "effect_size": "not_claimed",
            "status": "partial_seed_level_support; comparison-family review pending",
        },
        "C3": {
            "experiment_ids": "Exp13.1; Exp13.2",
            "metric_family": "recurrent execution; route-table versus composition split",
            "n_units": "Exp13.1 aggregate rows report n=20 per selected structure-audit variant; Exp13.2 aggregate n=20",
            "summary_value": "Exp13.1 full model route_table_accuracy=1.000 and composition_accuracy=1.000; no recurrence at eval route_table_accuracy=1.000 but composition_accuracy=0.0401 at route_length=12.",
            "interval_or_spread": "descriptive means and SDs available in aggregate artifacts; final comparison-family intervals not claimed",
            "effect_size": "not_claimed",
            "status": "descriptive_support_available; seed-level comparison grouping pending",
        },
        "C4": {
            "experiment_ids": "Exp13.2; Exp14; Exp15",
            "metric_family": "route table; endpoint memorization; suffix composition; transition learning",
            "n_units": seed_note(EXP14_METRICS, EXP15_SEED_METRICS) + "; Exp13.2 is aggregate summary",
            "summary_value": "Endpoint, transition, route-table, and composition metrics separate in Exp14/Exp15 slices; Table 4 remains fixed-profile and non-ranking.",
            "interval_or_spread": "Exp14 and Exp15 expose seed-level rows; C4-wide effect-size grouping remains pending",
            "effect_size": "not_claimed",
            "status": "partial_seed_level_support; comparison-family review pending",
        },
        "C5": {
            "experiment_ids": "Exp12",
            "metric_family": "clean supplied-context capacity scaling",
            "n_units": seed_note(EXP12_METRICS),
            "summary_value": table3_rows.get("C5", {}).get(
                "main_metric_summary",
                "Route-table and composition accuracy are 1.000 across the tested clean supplied-context grid.",
            ),
            "interval_or_spread": "zero observed spread for accuracy in mirrored clean grid; aggregate cell counts range from 60 to 960",
            "effect_size": "not_applicable",
            "status": "seed_level_descriptive_support_available",
        },
        "C6": {
            "experiment_ids": "Exp13",
            "metric_family": "finite structural budget degradation",
            "n_units": seed_note(EXP13_METRICS),
            "summary_value": table3_rows.get("C6", {}).get(
                "main_metric_summary",
                "Composition accuracy rises with global budget ratio and reaches ceiling at exact/surplus budget.",
            ),
            "interval_or_spread": "seed-level rows and aggregate SDs available; no fitted capacity law",
            "effect_size": "not_applicable",
            "status": "seed_level_descriptive_support_available",
        },
        "C13": {
            "experiment_ids": "Exp14",
            "metric_family": "symbolic transition-cue context selection",
            "n_units": seed_note(EXP14_METRICS),
            "summary_value": table3_rows.get("C13", {}).get(
                "main_metric_summary",
                "Symbolic transition-cue selector remains near ceiling across selected corruption levels.",
            ),
            "interval_or_spread": "Exp14 summary includes CI95 fields; exact manuscript comparison family still pending",
            "effect_size": "not_claimed",
            "status": "seed_level_descriptive_support_available; effect-size artifact not promoted",
        },
        "C12": {
            "experiment_ids": "Exp13.2; Exp15",
            "metric_family": "symbolic baselines; fixed-profile neural comparator",
            "n_units": seed_note(EXP15_SEED_METRICS) + "; Exp13.2 is aggregate summary",
            "summary_value": "Symbolic/algorithmic baselines and a minimal fixed-profile neural comparator are present; Table 4 shows transition MLP context/world-head variants solve the clean hard slice.",
            "interval_or_spread": "Exp15 summary has SD/SEM/CI fields by metric; Table 4 remains descriptive",
            "effect_size": "not_claimed",
            "status": "baseline_coverage_documented; non-exhaustive",
        },
    }

    for claim_id in RETAINED_CLAIMS:
        claim = claim_rows[claim_id]
        readiness = readiness_rows.get(claim_id, {})
        config = configs[claim_id]
        rows.append(
            {
                "claim_id": claim_id,
                "role": claim["claim_role"],
                "experiment_ids": config["experiment_ids"],
                "metric_family": config["metric_family"],
                "source_artifacts": claim["primary_source_artifacts"],
                "n_units": config["n_units"],
                "summary_value": config["summary_value"],
                "interval_or_spread": config["interval_or_spread"],
                "effect_size": config["effect_size"],
                "status": config["status"],
                "caveat": claim["claim_boundary"],
                "fresh_rerun_status": "not_rerun_in_this_PR; committed artifacts validated only",
                "readiness_status": readiness.get("statistical_status", ""),
            }
        )
    return rows


def markdown_escape(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def write_markdown_table(summary_rows: list[dict[str, object]]) -> None:
    headers = [
        "Claim",
        "Role",
        "Evidence source",
        "Reproducibility support",
        "Statistical status",
        "Caveat",
        "Submission posture",
    ]
    lines = [
        "# Claim-Scoped Reproducibility Summary",
        "",
        "| " + " | ".join(headers) + " |",
        "|---|---|---|---|---|---|---|",
    ]
    for row in summary_rows:
        posture = "Ready for V3 descriptive drafting; inferential language still frozen."
        if row["claim_id"] == "C12":
            posture = "Ready as non-exhaustive baseline posture; no broad neural claim."
        cells = [
            row["claim_id"],
            row["role"],
            row["experiment_ids"],
            row["summary_value"],
            f"{row['status']}; effect_size={row['effect_size']}",
            row["caveat"],
            posture,
        ]
        lines.append("| " + " | ".join(markdown_escape(cell) for cell in cells) + " |")
    repo_path(OUTPUT_TABLE).parent.mkdir(parents=True, exist_ok=True)
    repo_path(OUTPUT_TABLE).write_text("\n".join(lines) + "\n", encoding="utf-8")


def parsed_artifact_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for path in PARSED_INPUTS:
        full_path = repo_path(path)
        entry: dict[str, object] = {"path": path.as_posix(), "status": "missing", "rows": "", "seed_column": "no"}
        if full_path.exists():
            entry["status"] = "parsed"
            if path.suffix.lower() == ".csv":
                with full_path.open("r", encoding="utf-8-sig", newline="") as handle:
                    reader = csv.DictReader(handle)
                    count = 0
                    seeds = set()
                    fieldnames = reader.fieldnames or []
                    for row in reader:
                        count += 1
                        if "seed" in row and row.get("seed", "") != "":
                            seeds.add(row["seed"])
                    entry["rows"] = count
                    entry["seed_column"] = f"yes ({len(seeds)} seeds)" if "seed" in fieldnames else "no"
            else:
                entry["rows"] = len(full_path.read_text(encoding="utf-8").splitlines())
        rows.append(entry)
    return rows


def write_report(summary_rows: list[dict[str, object]], seed_rows: list[dict[str, object]]) -> None:
    parsed = parsed_artifact_rows()
    lines = [
        "# Claim-Scoped Reproducibility Summary Report",
        "",
        f"Generated at: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        "",
        "Generation command:",
        "",
        "```bash",
        "python scripts/build_claim_scoped_reproducibility_summary.py",
        "```",
        "",
        "## What Was Generated",
        "",
        "- `docs/manuscript/source_data/reproducibility_claim_summary.csv`",
        "- `docs/manuscript/source_data/seed_level_core_claim_metrics.csv`",
        "- `docs/manuscript/tables/table_reproducibility_claim_summary.md`",
        "- `docs/repo_audit/CLAIM_SCOPED_REPRODUCIBILITY_SUMMARY_REPORT.md`",
        "",
        "The script only read committed artifacts. It did not rerun experiments and did not write inside any `experiments/` directory.",
        "",
        "## Source Artifacts Parsed",
        "",
        "| Path | Status | Rows/lines | Seed exposure |",
        "|---|---:|---:|---|",
    ]
    for row in parsed:
        lines.append(
            f"| `{row['path']}` | {row['status']} | {row['rows']} | {row['seed_column']} |"
        )

    lines.extend(
        [
            "",
            "## Retained Claim Coverage",
            "",
            "| Claim | Seed-level support | Aggregate-only or review limitation | Source path |",
            "|---|---|---|---|",
        ]
    )
    for row in summary_rows:
        seed_support = row["n_units"]
        limitation = row["status"]
        first_source = split_semicolon(str(row["source_artifacts"]))[0]
        lines.append(
            f"| {row['claim_id']} | {markdown_escape(seed_support)} | {markdown_escape(limitation)} | `{first_source}` |"
        )

    lines.extend(
        [
            "",
            "## Claim Interpretations",
            "",
        ]
    )
    for row in summary_rows:
        first_source = split_semicolon(str(row["source_artifacts"]))[0]
        lines.extend(
            [
                f"### {row['claim_id']}",
                "",
                f"Claim -> {row['role']}.",
                "",
                f"Evidence -> {row['summary_value']}",
                "",
                f"Caveat -> {row['caveat']}",
                "",
                f"Source path -> `{first_source}`",
                "",
            ]
        )

    lines.extend(
        [
            "## Adequate Seed-Level Support",
            "",
            "- C5 has seed-level Exp12 rows for clean supplied-context route-table and composition accuracy.",
            "- C6 has seed-level Exp13 rows for finite structural-budget route-table and composition accuracy.",
            "- C13 has seed-level Exp14 rows for symbolic cue-selected context metrics at the compact Table 3 slice.",
            "- C12 has seed-level Exp15 fixed-profile neural comparator rows.",
            "- C2 and C4 have partial seed-level support from Exp14 and Exp15, but their cross-experiment comparison families still need human review before inferential wording.",
            "",
            "## Aggregate-Only Or Comparison-Family Pending Claims",
            "",
            "- C1 and C3 rely heavily on Exp13.1 and Exp13.2 aggregate summaries for the current manuscript source set; no seed rows were fabricated from those aggregate files.",
            "- C2 and C4 should remain descriptive until the exact cross-artifact comparison families are approved.",
            "- C13 has an effect-size artifact, but this summary keeps effect-size language as `not_claimed` pending manuscript comparison-family approval.",
            "- Compact Table 3 remains descriptive only.",
            "",
            "## Boundary, Supplement, And Non-Claim Evidence",
            "",
            "- Boundary/supplement only: C7 local-versus-global pressure, C8 consolidation/stability-plasticity discussion, C10 context/cue corruption sensitivity, C11 continuous/noisy bridge.",
            "- Non-claims: C9 seen/unseen primitive boundary, Exp13.1 positive lesion evidence, Exp15 replay collapse, broad CIRM-over-neural claims, raw sensory latent-world discovery, biological validation.",
            "- Exp15 replay collapse remains a non-claim pending implementation/training/buffer audit.",
            "",
            "## Fresh Rerun Recommendation",
            "",
            "No fresh expensive experiment rerun was performed or required for this PR. The next V3 drafting step can use the committed artifact package plus this summary. Before final submission, the author-facing `rerun-critical` pathway from `docs/repo_audit/MANUSCRIPT_REPRODUCIBILITY_PROTOCOL.md` remains recommended if time and hardware allow, especially if human statistical review changes comparison families.",
            "",
            "## Manuscript Claim Posture",
            "",
            "This generated summary does not widen the manuscript claim posture. It keeps C1 benchmark/model-family-specific, C2 conflict-specific, C5 ceiling-limited and supplied-context only, C6 descriptive with no capacity law, C13 symbolic-cue-only, and C12 fixed-profile/non-exhaustive. It does not promote boundary, supplement, or non-claim evidence into the retained main claim set.",
            "",
            f"Seed-level rows emitted: {len(seed_rows)}.",
        ]
    )
    repo_path(OUTPUT_REPORT).parent.mkdir(parents=True, exist_ok=True)
    repo_path(OUTPUT_REPORT).write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    seed_rows = build_seed_rows()
    summary_rows = build_summary_rows(seed_rows)

    summary_fields = [
        "claim_id",
        "role",
        "experiment_ids",
        "metric_family",
        "source_artifacts",
        "n_units",
        "summary_value",
        "interval_or_spread",
        "effect_size",
        "status",
        "caveat",
        "fresh_rerun_status",
        "readiness_status",
    ]
    seed_fields = [
        "claim_id",
        "experiment_id",
        "run_id",
        "seed",
        "variant",
        "world_count",
        "route_length",
        "metric_name",
        "metric_value",
        "source_artifact",
        "budget_ratio",
        "cue_count",
        "corruption_rate",
        "probe_type",
        "aggregation_note",
    ]
    write_csv(OUTPUT_SUMMARY, summary_fields, summary_rows)
    write_csv(OUTPUT_SEED, seed_fields, seed_rows)
    write_markdown_table(summary_rows)
    write_report(summary_rows, seed_rows)
    print(f"Wrote {OUTPUT_SUMMARY.as_posix()} ({len(summary_rows)} rows)")
    print(f"Wrote {OUTPUT_SEED.as_posix()} ({len(seed_rows)} rows)")
    print(f"Wrote {OUTPUT_TABLE.as_posix()}")
    print(f"Wrote {OUTPUT_REPORT.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
