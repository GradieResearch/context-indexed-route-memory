#!/usr/bin/env python
"""Manuscript reproducibility driver.

This script provides a conservative, claim-scoped reproducibility command surface
for the current manuscript package. It is intentionally stdlib-only for the
artifact-validation path so reviewers can run it before installing heavier
experiment dependencies.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import platform
import shlex
import subprocess
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[1]
CLAIM_MAP_PATH = Path("docs/manuscript/source_data/manuscript_claim_artifact_map.csv")
DEFAULT_REPORT_MD = Path("docs/repo_audit/MANUSCRIPT_REPRODUCIBILITY_REPORT.md")
DEFAULT_REPORT_JSON = Path("docs/repo_audit/manuscript_reproducibility_report.json")
ASSET_BUILD_SCRIPT = Path("scripts/manuscript_assets/build_manuscript_assets.py")

KEY_SOURCE_DATA_CHECKS: dict[str, set[str]] = {
    "docs/manuscript/source_data/table_04_exp15_neural_comparator.csv": {
        "variant",
        "first_step_context_conflict_accuracy",
        "retention_after_sequential_worlds",
        "seen_route_composition_accuracy",
        "suffix_route_composition_accuracy",
        "transition_accuracy",
        "interpretation",
    },
    "docs/manuscript/source_data/table_03_compact_final_safe.csv": {
        "claim_id",
        "experiment_id",
        "table_slice",
        "main_metric_summary",
        "manuscript_use",
        "final_status",
        "caveat",
        "source_paths",
    },
    "docs/manuscript/source_data/figure_05_symbolic_context_selection.csv": {
        "experiment_id",
        "variant",
        "metric",
        "mean",
        "manuscript_claim_id",
    },
    "docs/manuscript/source_data/figure_03_capacity_scaling.csv": {
        "experiment_id",
        "world_count",
        "route_length",
        "metric",
        "mean",
        "manuscript_claim_id",
    },
}

SMOKE_COMMANDS: list[dict[str, str]] = [
    {
        "experiment": "Exp11",
        "command": "pwsh -NoProfile -ExecutionPolicy Bypass -File experiments/experiment11_context_memory/start_exp11.ps1 -ValidationOnly",
        "reason": "Validation-only launcher documented in reproducibility audit.",
    },
    {
        "experiment": "Exp12",
        "command": "pwsh -NoProfile -ExecutionPolicy Bypass -File experiments/experiment12_capacity_generalization/start_exp12.ps1 -Profile validate -OutDir analysis/exp12_validation",
        "reason": "Validate profile documented in reproducibility audit.",
    },
    {
        "experiment": "Exp13",
        "command": "pwsh -NoProfile -ExecutionPolicy Bypass -File experiments/experiment13_breaking_point/start_exp13.ps1 -Profile smoke -Clean",
        "reason": "Smoke profile documented in reproducibility audit.",
    },
    {
        "experiment": "Exp13.1",
        "command": "pwsh -NoProfile -ExecutionPolicy Bypass -File experiments/experiment13_1_publication_hardening/start_exp13_1_validate.ps1 -RunId latest",
        "reason": "Validation wrapper documented in reproducibility audit.",
    },
    {
        "experiment": "Exp14",
        "command": "pwsh -NoProfile -ExecutionPolicy Bypass -File experiments/experiment14_latent_context_inference/start_exp14_validation.ps1",
        "reason": "Validation wrapper documented in reproducibility audit.",
    },
    {
        "experiment": "Exp15",
        "command": "pwsh -NoProfile -ExecutionPolicy Bypass -File experiments/experiment15_neural_baseline_comparator/start_exp15_validation.ps1",
        "reason": "Validation wrapper documented in reproducibility audit.",
    },
]

FULL_CRITICAL_COMMANDS: list[dict[str, str]] = [
    {
        "experiment": "Exp12",
        "command": "pwsh -NoProfile -ExecutionPolicy Bypass -File experiments/experiment12_capacity_generalization/start_exp12.ps1 -Profile full -OutDir analysis/exp12",
        "reason": "Clean supplied-context capacity claim C5.",
    },
    {
        "experiment": "Exp13",
        "command": "pwsh -NoProfile -ExecutionPolicy Bypass -File experiments/experiment13_breaking_point/start_exp13.ps1 -Profile standard -Clean",
        "reason": "Finite-budget degradation claim C6 and boundary C7.",
    },
    {
        "experiment": "Exp13.1",
        "command": "pwsh -NoProfile -ExecutionPolicy Bypass -File experiments/experiment13_1_publication_hardening/start_exp13_1_full.ps1",
        "reason": "Ablation claims C1-C4.",
    },
    {
        "experiment": "Exp14",
        "command": "pwsh -NoProfile -ExecutionPolicy Bypass -File experiments/experiment14_latent_context_inference/start_exp14_full.ps1",
        "reason": "Symbolic transition-cue context-selection claim C13.",
    },
    {
        "experiment": "Exp15",
        "command": "pwsh -NoProfile -ExecutionPolicy Bypass -File experiments/experiment15_neural_baseline_comparator/start_exp15_full.ps1",
        "reason": "Minimal fixed-profile neural comparator C12/Table 4.",
    },
]


@dataclass
class CheckResult:
    name: str
    status: str
    message: str
    path: str = ""
    claim_id: str = ""
    details: dict[str, object] = field(default_factory=dict)


@dataclass
class ProfileResult:
    profile: str
    status: str
    started_at: str
    finished_at: str
    elapsed_seconds: float
    checks: list[CheckResult]
    caveats: list[str] = field(default_factory=list)


def rel(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def repo_path(path: str | Path) -> Path:
    return REPO_ROOT / Path(path)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def split_semicolon(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def command_path(command: str) -> str | None:
    """Best-effort extraction of a path-like token from a documented command."""
    if not command.strip():
        return None
    try:
        tokens = shlex.split(command, posix=os.name != "nt")
    except ValueError:
        tokens = command.split()
    path_suffixes = (".ps1", ".py", ".sh", ".bat", ".cmd", ".md", ".csv", ".json")
    for token in tokens:
        normalized = token.replace("\\", "/")
        if normalized.startswith("experiments/") or normalized.startswith("scripts/") or normalized.startswith("docs/"):
            return normalized
        if normalized.endswith(path_suffixes):
            return normalized
    return None


def read_csv_rows(path: Path) -> tuple[list[str], list[dict[str, str]], str | None]:
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            headers = list(reader.fieldnames or [])
            rows = list(reader)
        return headers, rows, None
    except Exception as exc:  # pragma: no cover - defensive reporting path
        return [], [], f"{type(exc).__name__}: {exc}"


def load_claim_map() -> tuple[list[dict[str, str]], list[CheckResult]]:
    path = repo_path(CLAIM_MAP_PATH)
    checks: list[CheckResult] = []
    if not path.exists():
        checks.append(CheckResult("claim_map_exists", "FAIL", "Claim artifact map is missing.", CLAIM_MAP_PATH.as_posix()))
        return [], checks
    headers, rows, error = read_csv_rows(path)
    if error:
        checks.append(CheckResult("claim_map_parse", "FAIL", f"Could not parse claim artifact map: {error}", CLAIM_MAP_PATH.as_posix()))
        return [], checks
    required = {
        "claim_id",
        "claim_role",
        "primary_source_artifacts",
        "validation_artifacts",
        "analysis_scripts_or_commands",
        "statistical_status",
        "fresh_rerun_priority",
    }
    missing = sorted(required.difference(headers))
    if missing:
        checks.append(CheckResult("claim_map_schema", "FAIL", f"Missing required columns: {', '.join(missing)}", CLAIM_MAP_PATH.as_posix()))
    else:
        checks.append(CheckResult("claim_map_schema", "PASS", f"Claim map has {len(rows)} rows and required columns.", CLAIM_MAP_PATH.as_posix()))
    return rows, checks


def check_csv_artifact(path: str, claim_id: str, *, required_columns: set[str] | None = None) -> list[CheckResult]:
    checks: list[CheckResult] = []
    absolute = repo_path(path)
    if not absolute.exists():
        return [CheckResult("csv_exists", "FAIL", "CSV artifact is missing.", path, claim_id)]
    headers, rows, error = read_csv_rows(absolute)
    if error:
        return [CheckResult("csv_parse", "FAIL", f"CSV could not be parsed: {error}", path, claim_id)]
    if not headers:
        checks.append(CheckResult("csv_schema", "FAIL", "CSV has no header row.", path, claim_id))
    elif len(rows) == 0:
        checks.append(CheckResult("csv_rows", "FAIL", "CSV has no data rows.", path, claim_id, {"headers": headers}))
    else:
        checks.append(CheckResult("csv_parse", "PASS", f"CSV parsed with {len(rows)} rows and {len(headers)} columns.", path, claim_id))
    if required_columns:
        missing = sorted(required_columns.difference(headers))
        if missing:
            checks.append(CheckResult("csv_required_columns", "FAIL", f"Missing required columns: {', '.join(missing)}", path, claim_id))
        else:
            checks.append(CheckResult("csv_required_columns", "PASS", "Required columns are present.", path, claim_id))
    return checks


def validate_artifacts() -> ProfileResult:
    started = time.perf_counter()
    started_at = utc_now()
    checks: list[CheckResult] = []
    caveats: list[str] = []
    rows, map_checks = load_claim_map()
    checks.extend(map_checks)

    for row in rows:
        claim_id = row.get("claim_id", "")
        role = row.get("claim_role", "")
        status = row.get("statistical_status", "")
        strict = status not in {"non_claim", "not_final"} and "boundary" not in role.lower()
        for field_name in ("primary_source_artifacts", "validation_artifacts"):
            for artifact in split_semicolon(row.get(field_name, "")):
                absolute = repo_path(artifact)
                if absolute.exists():
                    checks.append(CheckResult(f"{field_name}_exists", "PASS", "Artifact exists.", artifact, claim_id))
                    if artifact.endswith(".csv"):
                        checks.extend(check_csv_artifact(artifact, claim_id, required_columns=KEY_SOURCE_DATA_CHECKS.get(artifact)))
                else:
                    checks.append(
                        CheckResult(
                            f"{field_name}_exists",
                            "FAIL" if strict else "WARN",
                            "Artifact is missing." if strict else "Boundary/non-claim artifact is missing or intentionally not central.",
                            artifact,
                            claim_id,
                        )
                    )
        for command in split_semicolon(row.get("analysis_scripts_or_commands", "")):
            path = command_path(command)
            if path is None:
                checks.append(CheckResult("command_path_parse", "WARN", "Could not infer a path from documented command.", command, claim_id))
                continue
            if repo_path(path).exists():
                checks.append(CheckResult("command_path_exists", "PASS", "Documented command path exists.", path, claim_id, {"command": command}))
            else:
                checks.append(CheckResult("command_path_exists", "WARN", "Documented command path does not exist or is environment-specific.", path, claim_id, {"command": command}))

    for artifact, columns in KEY_SOURCE_DATA_CHECKS.items():
        checks.extend(check_csv_artifact(artifact, "source-data", required_columns=columns))

    caveats.append("This profile validates committed artifacts and schemas; it does not rerun expensive experiments.")
    caveats.append("Boundary and non-claim rows are checked but not promoted to manuscript evidence.")
    return finish_profile("validate-artifacts", started_at, started, checks, caveats)


def rebuild_manuscript_assets() -> ProfileResult:
    started = time.perf_counter()
    started_at = utc_now()
    checks: list[CheckResult] = []
    caveats = [
        "This profile runs the manuscript asset build script from committed artifacts.",
        "Generated file differences should be reviewed before committing regenerated assets.",
    ]
    if not repo_path(ASSET_BUILD_SCRIPT).exists():
        checks.append(CheckResult("asset_script_exists", "FAIL", "Manuscript asset build script is missing.", ASSET_BUILD_SCRIPT.as_posix()))
        return finish_profile("rebuild-manuscript-assets", started_at, started, checks, caveats)

    command = [sys.executable, ASSET_BUILD_SCRIPT.as_posix()]
    proc = subprocess.run(command, cwd=REPO_ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output_tail = "\n".join((proc.stdout or "").splitlines()[-40:])
    if proc.returncode == 0:
        checks.append(CheckResult("asset_build", "PASS", "Manuscript asset build completed.", ASSET_BUILD_SCRIPT.as_posix(), details={"output_tail": output_tail}))
    else:
        checks.append(
            CheckResult(
                "asset_build",
                "WARN",
                "Manuscript asset build did not complete in this environment; install experiment/asset dependencies and rerun locally.",
                ASSET_BUILD_SCRIPT.as_posix(),
                details={"returncode": proc.returncode, "output_tail": output_tail},
            )
        )
    for required in [
        "docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md",
        "docs/repo_audit/MANUSCRIPT_ASSET_GENERATION_REPORT.md",
        "docs/manuscript/tables/table_04_exp15_neural_comparator.md",
        "docs/manuscript/tables/table_03_compact_final_safe.md",
        "docs/manuscript/source_data/table_04_exp15_neural_comparator.csv",
        "docs/manuscript/source_data/table_03_compact_final_safe.csv",
    ]:
        checks.append(
            CheckResult(
                "asset_output_exists",
                "PASS" if repo_path(required).exists() else "FAIL",
                "Expected manuscript asset output exists." if repo_path(required).exists() else "Expected manuscript asset output is missing.",
                required,
            )
        )
    return finish_profile("rebuild-manuscript-assets", started_at, started, checks, caveats)


def plan_profile(profile: str, commands: Iterable[dict[str, str]]) -> ProfileResult:
    started = time.perf_counter()
    started_at = utc_now()
    checks: list[CheckResult] = []
    for item in commands:
        path = command_path(item["command"])
        exists = bool(path and repo_path(path).exists())
        checks.append(
            CheckResult(
                "planned_command",
                "PASS" if exists else "WARN",
                "Command path exists; execution is opt-in." if exists else "Command path was not found; review launcher path before execution.",
                path or item["command"],
                details=item,
            )
        )
    caveats = [
        f"The {profile} profile currently records the execution plan only.",
        "Full execution is intentionally opt-in so preserved historical outputs are not overwritten.",
    ]
    return finish_profile(profile, started_at, started, checks, caveats)


def finish_profile(profile: str, started_at: str, started: float, checks: list[CheckResult], caveats: list[str]) -> ProfileResult:
    if any(check.status == "FAIL" for check in checks):
        status = "FAIL"
    elif any(check.status == "WARN" for check in checks):
        status = "WARN"
    else:
        status = "PASS"
    return ProfileResult(profile, status, started_at, utc_now(), time.perf_counter() - started, checks, caveats)


def git_value(args: list[str], default: str = "unknown") -> str:
    try:
        proc = subprocess.run(["git", *args], cwd=REPO_ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=False)
        value = proc.stdout.strip()
        return value or default
    except Exception:
        return default


def environment_metadata(command: str) -> dict[str, object]:
    return {
        "generated_at": utc_now(),
        "repository_root": rel(REPO_ROOT),
        "commit_sha": git_value(["rev-parse", "HEAD"]),
        "branch": git_value(["rev-parse", "--abbrev-ref", "HEAD"]),
        "python": sys.version.replace("\n", " "),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "command": command,
    }


def result_to_dict(result: ProfileResult) -> dict[str, object]:
    return {
        "profile": result.profile,
        "status": result.status,
        "started_at": result.started_at,
        "finished_at": result.finished_at,
        "elapsed_seconds": result.elapsed_seconds,
        "caveats": result.caveats,
        "checks": [
            {
                "name": check.name,
                "status": check.status,
                "message": check.message,
                "path": check.path,
                "claim_id": check.claim_id,
                "details": check.details,
            }
            for check in result.checks
        ],
    }


def write_json_report(path: Path, metadata: dict[str, object], results: list[ProfileResult]) -> None:
    payload = {
        "metadata": metadata,
        "overall_status": overall_status(results),
        "profiles": [result_to_dict(result) for result in results],
    }
    target = repo_path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def overall_status(results: list[ProfileResult]) -> str:
    if any(result.status == "FAIL" for result in results):
        return "FAIL"
    if any(result.status == "WARN" for result in results):
        return "WARN"
    return "PASS"


def summarize_counts(checks: Iterable[CheckResult]) -> dict[str, int]:
    counts = {"PASS": 0, "WARN": 0, "FAIL": 0}
    for check in checks:
        counts[check.status] = counts.get(check.status, 0) + 1
    return counts


def write_markdown_report(path: Path, metadata: dict[str, object], results: list[ProfileResult]) -> None:
    lines: list[str] = []
    lines.append("# Manuscript Reproducibility Report")
    lines.append("")
    lines.append(f"Generated at: {metadata['generated_at']}")
    lines.append("")
    lines.append(f"Overall status: **{overall_status(results)}**")
    lines.append("")
    lines.append("## Environment")
    lines.append("")
    for key in ["commit_sha", "branch", "python", "platform", "machine", "processor", "command"]:
        lines.append(f"- {key}: `{metadata.get(key, 'unknown')}`")
    lines.append("")
    lines.append("## Profile Summary")
    lines.append("")
    lines.append("| Profile | Status | PASS | WARN | FAIL | Elapsed seconds |")
    lines.append("|---|---:|---:|---:|---:|---:|")
    for result in results:
        counts = summarize_counts(result.checks)
        lines.append(
            f"| {result.profile} | {result.status} | {counts.get('PASS', 0)} | {counts.get('WARN', 0)} | {counts.get('FAIL', 0)} | {result.elapsed_seconds:.2f} |"
        )
    lines.append("")
    for result in results:
        lines.append(f"## Profile: {result.profile}")
        lines.append("")
        lines.append(f"Status: **{result.status}**")
        lines.append("")
        if result.caveats:
            lines.append("Caveats:")
            lines.append("")
            for caveat in result.caveats:
                lines.append(f"- {caveat}")
            lines.append("")
        notable = [check for check in result.checks if check.status in {"FAIL", "WARN"}]
        if notable:
            lines.append("### Warnings and failures")
            lines.append("")
            lines.append("| Status | Check | Claim | Path | Message |")
            lines.append("|---|---|---|---|---|")
            for check in notable[:100]:
                lines.append(
                    f"| {check.status} | {check.name} | {check.claim_id or '-'} | `{check.path}` | {check.message} |"
                )
            if len(notable) > 100:
                lines.append(f"\nAdditional warnings/failures omitted from Markdown: {len(notable) - 100}. See JSON report.")
            lines.append("")
        lines.append("### Check counts")
        lines.append("")
        counts = summarize_counts(result.checks)
        lines.append(f"- PASS: {counts.get('PASS', 0)}")
        lines.append(f"- WARN: {counts.get('WARN', 0)}")
        lines.append(f"- FAIL: {counts.get('FAIL', 0)}")
        lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append("This report is claim-scoped. It validates the committed evidence package and/or records planned execution paths; it does not by itself promote boundary or non-claim evidence into the retained manuscript claim set.")
    lines.append("")
    lines.append("Full manuscript submission readiness still requires human venue/citation decisions, final statistical comparison-family choices, and any target-venue reviewer-strategy baseline decision.")
    lines.append("")
    target = repo_path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(lines), encoding="utf-8")


def run_profiles(profile: str) -> list[ProfileResult]:
    if profile == "validate-artifacts":
        return [validate_artifacts()]
    if profile == "rebuild-manuscript-assets":
        return [rebuild_manuscript_assets()]
    if profile == "smoke":
        return [plan_profile("smoke", SMOKE_COMMANDS)]
    if profile == "rerun-critical":
        return [plan_profile("rerun-critical", FULL_CRITICAL_COMMANDS)]
    if profile == "full-critical":
        return [plan_profile("full-critical", FULL_CRITICAL_COMMANDS)]
    if profile == "foundation":
        return [validate_artifacts(), rebuild_manuscript_assets(), plan_profile("smoke", SMOKE_COMMANDS)]
    raise ValueError(f"Unsupported profile: {profile}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run manuscript reproducibility checks.")
    parser.add_argument(
        "--profile",
        required=True,
        choices=["validate-artifacts", "rebuild-manuscript-assets", "smoke", "rerun-critical", "full-critical", "foundation"],
        help="Reproducibility profile to run. 'foundation' runs validate-artifacts, rebuild-manuscript-assets, and smoke planning.",
    )
    parser.add_argument("--report-md", default=DEFAULT_REPORT_MD.as_posix(), help="Markdown report output path.")
    parser.add_argument("--report-json", default=DEFAULT_REPORT_JSON.as_posix(), help="JSON report output path.")
    parser.add_argument("--strict", action="store_true", help="Return non-zero on WARN as well as FAIL.")
    parser.add_argument("--jobs", type=int, default=1, help="Reserved for future rerun/full-critical execution planning.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    command = "python " + " ".join(shlex.quote(part) for part in [rel(Path(__file__)), *sys.argv[1:]])
    results = run_profiles(args.profile)
    metadata = environment_metadata(command)
    metadata["jobs"] = args.jobs
    write_json_report(Path(args.report_json), metadata, results)
    write_markdown_report(Path(args.report_md), metadata, results)
    status = overall_status(results)
    print(f"Manuscript reproducibility profile '{args.profile}' completed with status {status}.")
    print(f"Markdown report: {args.report_md}")
    print(f"JSON report: {args.report_json}")
    if status == "FAIL":
        return 1
    if args.strict and status == "WARN":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
