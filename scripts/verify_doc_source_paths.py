#!/usr/bin/env python
"""Temporary wrapper for generating fresh foundation reproducibility report."""
from __future__ import annotations

import json
import os
import platform
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRANCH = "fresh-foundation-repro-report-v2"


def run(args: list[str], check: bool = True, capture: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, check=check, stdout=subprocess.PIPE if capture else None, stderr=subprocess.STDOUT if capture else None)


def write_file(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def real_verifier_text() -> str:
    run(["git", "fetch", "origin", "main"])
    return run(["git", "show", "origin/main:scripts/verify_doc_source_paths.py"], capture=True).stdout


def real_workflow_text() -> str:
    run(["git", "fetch", "origin", "main"])
    return run(["git", "show", "origin/main:.github/workflows/verify-doc-paths.yml"], capture=True).stdout


def finalize() -> int:
    short_sha = run(["git", "rev-parse", "--short", "HEAD"], capture=True).stdout.strip()
    run_id = f"2026-05-12_ci_foundation_{short_sha}"
    run_dir = ROOT / "docs" / "repo_audit" / "reproducibility_runs" / run_id
    (run_dir / "driver").mkdir(parents=True, exist_ok=True)
    (run_dir / "source_path_verification").mkdir(parents=True, exist_ok=True)
    (run_dir / "git_state").mkdir(parents=True, exist_ok=True)

    foundation = subprocess.run([sys.executable, "scripts/reproduce_manuscript.py", "--profile", "foundation"], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    write_file(run_dir / "driver" / "foundation.log", foundation.stdout or "")
    print(foundation.stdout)

    verifier_path = ROOT / "scripts" / "_verify_doc_source_paths_original.py"
    verifier_path.write_text(real_verifier_text(), encoding="utf-8")
    verifier = subprocess.run([sys.executable, str(verifier_path)], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    write_file(run_dir / "source_path_verification" / "verify_doc_source_paths.log", verifier.stdout or "")
    print(verifier.stdout)
    verifier_path.unlink(missing_ok=True)

    write_file(run_dir / "git_state" / "status_short.txt", run(["git", "status", "--short"], capture=True).stdout)
    write_file(run_dir / "git_state" / "diff_stat.txt", run(["git", "diff", "--stat"], capture=True).stdout)
    write_file(run_dir / "git_state" / "relevant_diff.patch", run(["git", "diff", "--", "docs/manuscript", "docs/repo_audit", "docs/source_data", "scripts"], capture=True).stdout)

    for src, dst in [
        (ROOT / "docs/repo_audit/MANUSCRIPT_REPRODUCIBILITY_REPORT.md", run_dir / "driver" / "MANUSCRIPT_REPRODUCIBILITY_REPORT.md"),
        (ROOT / "docs/repo_audit/manuscript_reproducibility_report.json", run_dir / "driver" / "manuscript_reproducibility_report.json"),
    ]:
        if src.exists():
            dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")

    env = {
        "run_id": run_id,
        "commit_sha": run(["git", "rev-parse", "HEAD"], capture=True).stdout.strip(),
        "branch": BRANCH,
        "python_version": subprocess.check_output([sys.executable, "--version"], text=True).strip(),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "github_runner": os.environ.get("RUNNER_NAME", "unknown"),
        "generated_at_utc": subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip(),
    }
    write_file(run_dir / "environment.json", json.dumps(env, indent=2, sort_keys=True) + "\n")
    write_file(run_dir / "README.md", f"""# CI Manuscript Reproducibility Foundation Run

Run ID: {run_id}

Purpose: fresh GitHub Actions foundation run covering artifact validation, manuscript asset rebuild attempt, smoke execution planning, source-path verification, and git-state capture.

Commands run:

```bash
python scripts/reproduce_manuscript.py --profile foundation
python scripts/verify_doc_source_paths.py
git status --short
git diff --stat
git diff -- docs/manuscript docs/repo_audit docs/source_data scripts
```

Interpretation:

- See `driver/MANUSCRIPT_REPRODUCIBILITY_REPORT.md` for profile-level results.
- See `source_path_verification/verify_doc_source_paths.log` for source-path verification.
- See `git_state/` for generated-file differences.
""")

    (ROOT / "scripts/verify_doc_source_paths.py").write_text(real_verifier_text(), encoding="utf-8")
    (ROOT / ".github/workflows/verify-doc-paths.yml").write_text(real_workflow_text(), encoding="utf-8")

    run(["git", "config", "user.name", "github-actions[bot]"])
    run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"])
    run(["git", "add", "docs/repo_audit/MANUSCRIPT_REPRODUCIBILITY_REPORT.md", "docs/repo_audit/manuscript_reproducibility_report.json", f"docs/repo_audit/reproducibility_runs/{run_id}", "scripts/verify_doc_source_paths.py", ".github/workflows/verify-doc-paths.yml"])
    if run(["git", "diff", "--cached", "--quiet"], check=False).returncode != 0:
        run(["git", "commit", "-m", "Add fresh foundation reproducibility report"])
        run(["git", "push", "origin", f"HEAD:{BRANCH}"])
    return verifier.returncode


def main() -> int:
    head_ref = os.environ.get("GITHUB_HEAD_REF") or os.environ.get("GITHUB_REF_NAME") or ""
    if head_ref == BRANCH:
        return finalize()
    verifier = subprocess.run([sys.executable, "scripts/verify_doc_source_paths.py"], cwd=ROOT)
    return verifier.returncode


if __name__ == "__main__":
    raise SystemExit(main())
