#!/usr/bin/env python
"""Temporary PR-branch finalizer for compact Table 3 alignment.

This file is intentionally temporary. On the target branch used by PR #22 it
patches the manuscript/docs from a real GitHub Actions checkout, runs the real
verifier copied from origin/main, commits the resulting docs, restores this file
from origin/main, removes the temporary workflow, and pushes the branch.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRANCH = "finalize-table3-placeholder-verification"
DATE = "2026-05-10"

STALE_TABLE3 = "[Table 3 here: statistical summary. Source: `docs/manuscript/tables/table_03_statistical_summary.md`. Caveat: effect-size grouping still needs human review.]"
COMPACT_TABLE3 = "[Table 3 here: compact final-safe descriptive statistical summary. Source: `docs/manuscript/tables/table_03_compact_final_safe.md`; source data: `docs/manuscript/source_data/table_03_compact_final_safe.csv`. Detailed generated statistical map retained as candidate/supplementary audit support at `docs/manuscript/tables/table_03_statistical_summary.md` and `docs/manuscript/tables/table_03_statistical_summary.csv`. Caveat: descriptive only; do not treat as final inferential effect-size evidence or approved comparison-family statistics.]"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def run(args: list[str], *, check: bool = True, capture: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, check=check, stdout=subprocess.PIPE if capture else None, stderr=subprocess.STDOUT if capture else None)


def restore_real_verifier_to_temp() -> Path:
    run(["git", "fetch", "origin", "main"])
    original = run(["git", "show", "origin/main:scripts/verify_doc_source_paths.py"], capture=True).stdout
    temp_path = ROOT / "scripts" / "_verify_doc_source_paths_original.py"
    temp_path.write_text(original, encoding="utf-8")
    return temp_path


def run_real_verifier(temp_path: Path) -> tuple[int, str]:
    proc = subprocess.run([sys.executable, str(temp_path)], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc.returncode, (proc.stdout or "").strip()


def patch_manuscript() -> None:
    manuscript_path = "docs/manuscript/draft/MANUSCRIPT_V2.md"
    manuscript = read(manuscript_path)
    if STALE_TABLE3 in manuscript:
        manuscript = manuscript.replace(STALE_TABLE3, COMPACT_TABLE3)
    elif COMPACT_TABLE3 not in manuscript:
        raise RuntimeError("Could not find stale or compact Table 3 placeholder in MANUSCRIPT_V2.md")
    write(manuscript_path, manuscript)


def update_status_docs(verifier_code: int, verifier_output: str) -> None:
    if len(verifier_output) > 6000:
        verifier_output = verifier_output[:6000] + "\n... [truncated]"
    safe_output = verifier_output.replace("```", "` ` `") or "(no output)"
    passed = verifier_code == 0
    verification_result = "**passed**" if passed else "**failed**"
    result_line = "Result: **complete for the compact Table 3 manuscript-placeholder and source-path verification blocker**." if passed else "Result: **not complete**. The manuscript placeholder was patched, but source-path verification failed and the failure output is recorded below."
    remaining = (
        "The Table 3 placeholder/source-path verification loop is closed. The next blocker is final figure/table caption polish and manuscript TODO cleanup, especially Figures 1-3, Figure 5, compact Table 3, and Table 4."
        if passed else
        "Fix only the broken active paths reported by the verifier, preserve the conservative claim posture, and rerun `python scripts/verify_doc_source_paths.py`."
    )

    write("docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md", f"""# Table 3 Verification And Alignment Status

Date: {DATE}

Purpose: record the status of the compact Table 3 manuscript-placeholder and source-path verification pass requested after the compact final-safe Table 3 split.

## Status

{result_line}

The compact Table 3 split itself is complete. `docs/manuscript/draft/MANUSCRIPT_V2.md` now distinguishes the compact descriptive main-text Table 3 from the detailed generated statistical map.

## Manuscript Table 3 alignment

`docs/manuscript/draft/MANUSCRIPT_V2.md` now uses this main-text placeholder:

```md
{COMPACT_TABLE3}
```

The main-text Table 3 path is:

- `docs/manuscript/tables/table_03_compact_final_safe.md`
- `docs/manuscript/source_data/table_03_compact_final_safe.csv`

The detailed generated statistical map remains candidate/supplementary audit support only:

- `docs/manuscript/tables/table_03_statistical_summary.md`
- `docs/manuscript/tables/table_03_statistical_summary.csv`

Do not add final effect-size language or approved comparison-family statistics unless those groupings are explicitly reviewed later.

## Verification result

Command:

```bash
python scripts/verify_doc_source_paths.py
```

Execution environment: GitHub Actions pull-request checkout for branch `{BRANCH}`.

Result: {verification_result}.

Output:

```text
{safe_output}
```

## Remaining blocker

{remaining}
""")

    checklist_path = "docs/manuscript/finalization/FINALIZATION_CHECKLIST.md"
    checklist = read(checklist_path)
    checklist = checklist.replace(
        "Purpose: working checklist for moving the Context-Indexed Route Memory manuscript from V2 draft capture to a submission-ready package after Exp15 import, human placement decisions, Section 2.7 closest-prior-art integration, the compact-safe Table 3 split, and the first verification/alignment status capture.",
        "Purpose: working checklist for moving the Context-Indexed Route Memory manuscript from V2 draft capture to a submission-ready package after Exp15 import, human placement decisions, Section 2.7 closest-prior-art integration, the compact-safe Table 3 split, and the Table 3 manuscript-placeholder/source-path verification pass.",
    )
    checklist = checklist.replace(
        "- [!] Patch stale `MANUSCRIPT_V2.md` Table 3 placeholder so main-text Table 3 cites `docs/manuscript/tables/table_03_compact_final_safe.md`, not `docs/manuscript/tables/table_03_statistical_summary.md`.",
        "- [x] Patch stale `MANUSCRIPT_V2.md` Table 3 placeholder so main-text Table 3 cites `docs/manuscript/tables/table_03_compact_final_safe.md`, not `docs/manuscript/tables/table_03_statistical_summary.md`.",
    )
    run_line = "- [x] Run `python scripts/verify_doc_source_paths.py` after the compact Table 3 split and manuscript placeholder patch. Result recorded in `docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md`." if passed else "- [!] Run `python scripts/verify_doc_source_paths.py` after the compact Table 3 split and manuscript placeholder patch. The verifier failed; see `docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md`."
    checklist = re.sub(r"- \[!\] Run `python scripts/verify_doc_source_paths\.py` after the compact Table 3 split\.[^\n]*", run_line, checklist)
    checklist = re.sub(r"## Current Recommended Next Checkbox\n\n.*\Z", f"""## Current Recommended Next Checkbox

- [x] Apply `docs/manuscript/finalization/SECTION_2_7_PROSE_PATCH.md` directly to `docs/manuscript/draft/MANUSCRIPT_V2.md` without overwriting unrelated manuscript content.
- [x] Create a compact final-safe main-text Table 3 and move the full generated statistical map to candidate/supplementary status.
- [x] Record the current verification/alignment status in `docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md`.
- [x] Patch the stale `docs/manuscript/draft/MANUSCRIPT_V2.md` Table 3 placeholder to cite compact Table 3 as the main-text path.
- [{'x' if passed else '!'}] Run `python scripts/verify_doc_source_paths.py` after the manuscript placeholder patch.
- [ ] Polish and human-review final captions/prose for Figures 1-3, Figure 5, compact Table 3, and Table 4 while preserving caveats.
- [ ] Remove or clearly mark all remaining manuscript TODOs before submission.
""", checklist, flags=re.S)
    write(checklist_path, checklist)

    todo_path = "docs/manuscript/MANUSCRIPT_TODO.md"
    todo = read(todo_path)
    todo_priority = f"""## Current Next Operational Priority

Complete final **figure/table caption polish and manuscript TODO cleanup** after compact Table 3 alignment.

The compact Table 3 decision has been made and the manuscript placeholder has been patched:

- Main-text Table 3: `docs/manuscript/tables/table_03_compact_final_safe.md`
- Main-text Table 3 source data: `docs/manuscript/source_data/table_03_compact_final_safe.csv`
- Detailed candidate/supplementary statistical map: `docs/manuscript/tables/table_03_statistical_summary.md` and `docs/manuscript/tables/table_03_statistical_summary.csv`

Status note: `docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md` records the Table 3 manuscript-placeholder patch and source-path verifier result. The verifier {'passed' if passed else 'failed'} in the recorded GitHub Actions environment.

The current active work is therefore:

1. Polish captions/prose for Figures 1-3, Figure 5, compact Table 3, and Table 4.
2. Keep compact Table 3 descriptive; do not turn it into final inferential effect-size evidence.
3. Keep the detailed generated statistical map candidate/supplementary unless comparison families are explicitly approved.
4. Remove or clearly mark remaining manuscript TODOs before submission.
5. Defer venue-specific citation/export, optional memory-augmented neural baselines, license, and `CITATION.cff` until explicit human decisions are made.

"""
    todo = re.sub(r"## Current Next Operational Priority\n\n.*?## Current retained V2 posture", todo_priority + "## Current retained V2 posture", todo, flags=re.S)
    todo = todo.replace(
        "| Table 3 verification/alignment status capture. | Current blocker is documented: patch stale manuscript placeholder and run verifier from clean local/CI environment. | `docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md`; `docs/manuscript/finalization/NEXT_STEP_PROMPT.md` |",
        "| Table 3 manuscript alignment and source-path verification. | Stale manuscript Table 3 placeholder patched; verifier result recorded. | `docs/manuscript/draft/MANUSCRIPT_V2.md`; `docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md`; `docs/manuscript/finalization/NEXT_STEP_PROMPT.md` |",
    )
    p0_current = """## P0 - Current Next Pass

| TODO | Reason | Source path | Target output |
|---|---|---|---|
| Polish figure/table captions and manuscript prose. | Candidate assets exist, but final journal-style caption wording still needs human review and caveat preservation. | `docs/manuscript/draft/MANUSCRIPT_V2.md`; `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`; `docs/manuscript/tables/table_03_compact_final_safe.md`; `docs/manuscript/tables/table_04_exp15_neural_comparator.md` | Final-safe captions/prose for Figures 1-3, Figure 5, compact Table 3, and Table 4. |
| Remove or clearly mark remaining manuscript TODOs. | The draft still contains TODO placeholders that cannot remain in a submission draft. | `docs/manuscript/draft/MANUSCRIPT_V2.md` | No unreviewed submission-blocking TODOs in the manuscript draft. |
| Decide whether target venue strategy requires a memory-augmented/key-value neural comparator. | Exp15 is intentionally minimal and fixed-profile; broader neural coverage is venue-dependent. | `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md`; `experiments/experiment15_neural_baseline_comparator/README.md` | Explicit venue/reviewer decision; do not start a new experiment by default. |

"""
    todo = re.sub(r"## P0 - Current Next Pass\n\n.*?## P0 - Required Before Manuscript Submission", p0_current + "## P0 - Required Before Manuscript Submission", todo, flags=re.S)
    write(todo_path, todo)

    readiness_path = "docs/synthesis/PUBLICATION_READINESS.md"
    readiness = read(readiness_path)
    readiness = readiness.replace(
        "Status: post-Analysis-Pass-15A, post-citation-ledger/status pass, post-human-decision capture, post-direct Section 2.7 manuscript patch, post-compact Table 3 split, and post-status capture for the remaining Table 3 verification/alignment blocker. The manuscript is not submission-ready; the next blocker is now specifically to patch the stale manuscript Table 3 placeholder and run documentation source-path verification from a clean local/CI environment.",
        f"Status: post-Analysis-Pass-15A, post-citation-ledger/status pass, post-human-decision capture, post-direct Section 2.7 manuscript patch, post-compact Table 3 split, and post-Table-3 manuscript-placeholder/source-path verification pass. The manuscript is not submission-ready; the next blocker is final figure/table caption polish and manuscript TODO cleanup. The source-path verifier {'passed' if passed else 'failed'} in the recorded verification environment.",
    )
    readiness = readiness.replace(
        "`docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md` records that the Table 3 verification/alignment pass remains open until the manuscript placeholder is patched and the source-path verifier is run.",
        "`docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md` records the manuscript placeholder patch and source-path verifier result for the compact Table 3 alignment pass.",
    )
    readiness = readiness.replace("The manuscript draft still needs its stale Table 3 placeholder patched before this alignment pass is complete.", "The manuscript draft now cites compact Table 3 as the main-text descriptive table; final caption/prose review remains.")
    readiness = re.sub(r"## Required Before Manuscript Draft Finalization\n\n.*?\n## Required Before Submission", "## Required Before Manuscript Draft Finalization\n\n- Human-review generated Figures 1-5 and Tables 1-4 for caption wording, caveats, and venue-specific formatting.\n- Polish manuscript prose around compact Table 3 and Table 4 without adding final inferential effect-size claims.\n- Remove or clearly mark all remaining manuscript TODOs before submission.\n- Keep Figure 4 supplement-default unless the finite-budget story is intentionally emphasized.\n- Keep Figure 5 main-narrow unless a later venue decision requires supplement relocation.\n- Keep Table 4 as compact main-text unless a later venue decision requires supplement relocation.\n\n## Required Before Submission", readiness, flags=re.S)
    readiness = readiness.replace("The documentation source-path verifier still needs to be run from a clean local/CI environment after the manuscript placeholder patch.", "The documentation source-path verifier result after the manuscript placeholder patch is recorded in `docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md`.")
    write(readiness_path, readiness)

    human_path = "docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md"
    human = read(human_path)
    human = human.replace("Status: post-human-decision placement tracker, post-compact Table 3 split, and post-status capture for the remaining Table 3 verification/alignment blocker; still not a final journal art/caption approval.", "Status: post-human-decision placement tracker, post-compact Table 3 split, and post-Table-3 manuscript-placeholder/source-path verification pass; still not a final journal art/caption approval.")
    human = human.replace("`docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md` records that the manuscript draft still needs its stale Table 3 placeholder patched before this alignment pass is complete.", "`docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md` records the Table 3 manuscript-placeholder patch and source-path verifier result.")
    human = human.replace("Patch manuscript placeholder so main-text Table 3 points here; then polish caption/prose to route readers to the detailed map only as candidate/supplementary support.", "Polish caption/prose to keep compact Table 3 descriptive and route readers to the detailed map only as candidate/supplementary support.")
    human = re.sub(r"## Recommended next review order\n\n.*\Z", "## Recommended next review order\n\n1. Polish captions for Figures 1-3, Figure 5, compact Table 3, and Table 4.\n2. Remove or clearly mark remaining manuscript TODOs before submission.\n3. Decide later, based on venue/reviewer strategy, whether Table 1/Table 2 remain main/supporting or move to supplement/repository appendix.\n4. Decide later, based on venue/reviewer strategy, whether optional memory-augmented/key-value neural baselines are needed.\n", human, flags=re.S)
    write(human_path, human)

    next_prompt = """# Next Step Prompt: Polish Figure/Table Captions And Clear Manuscript TODOs

Use this prompt after compact Table 3 manuscript-placeholder alignment and source-path verification have been recorded.

```text
You are working in the repository:

GradieResearch/context-indexed-route-memory

Task: complete the next manuscript-finalization pass: final-safe figure/table caption polish and manuscript TODO cleanup. Do not start new experiments.

Starting context:

The repository is post-Exp15, post-Manuscript-V2-capture, post-Analysis-Pass-15A, post-citation/prior-art audit, post-citation-ledger pass, post-human-decision capture, post-Section-2.7 closest-prior-art prose integration, post-compact Table 3 split, and post-Table-3 manuscript-placeholder/source-path verification status capture.

Already completed:

- `docs/manuscript/draft/MANUSCRIPT_V2.md` exists and carries the conservative post-Exp15 manuscript posture.
- Section 2.7 contains closest-prior-art positioning prose, with `docs/manuscript/closest_prior_art_table.md` retained as a companion artifact.
- `docs/manuscript/tables/table_03_compact_final_safe.md` is the compact descriptive main-text Table 3.
- `docs/manuscript/source_data/table_03_compact_final_safe.csv` is the compact Table 3 source-data mirror.
- `docs/manuscript/tables/table_03_statistical_summary.md` and `docs/manuscript/tables/table_03_statistical_summary.csv` remain detailed candidate/supplementary statistical-map artifacts, not final inferential statistics.
- `docs/manuscript/draft/MANUSCRIPT_V2.md` points main-text Table 3 at the compact final-safe descriptive table and keeps the detailed statistical map candidate/supplementary.
- `docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md` records the Table 3 manuscript-placeholder patch and source-path verifier result.
- `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`, `docs/manuscript/MANUSCRIPT_TODO.md`, `docs/synthesis/PUBLICATION_READINESS.md`, and `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md` identify caption/prose polish and TODO cleanup as the next active blocker.

Immediate work:

1. Review:
   - `docs/manuscript/draft/MANUSCRIPT_V2.md`
   - `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`
   - `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`
   - `docs/manuscript/MANUSCRIPT_TODO.md`
   - `docs/synthesis/PUBLICATION_READINESS.md`

2. Polish manuscript figure/table placeholder and caption prose for:
   - Figures 1-3 as main figures.
   - Figure 5 as main-narrow symbolic transition-cue context-selection evidence.
   - Figure 4 as supplement-default unless a human explicitly emphasizes the finite-budget story.
   - Compact Table 3 as descriptive main-text statistics only.
   - Table 4 as compact main-text Exp15 neural comparator evidence.

3. Remove or clearly mark remaining submission-blocking TODOs in `docs/manuscript/draft/MANUSCRIPT_V2.md`.

4. Sync operational docs after the caption/TODO pass:
   - `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`
   - `docs/manuscript/MANUSCRIPT_TODO.md`
   - `docs/synthesis/PUBLICATION_READINESS.md`
   - `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`
   - this `NEXT_STEP_PROMPT.md`

5. Run `python scripts/verify_doc_source_paths.py` if any active source paths are added or edited. Record the result exactly if run.

Preserve the current claim posture:

- Do not add final effect-size language unless explicit comparison families are approved.
- Keep compact Table 3 descriptive only.
- Keep C1 benchmark/model-family-specific.
- Keep C2 conflict-specific, not a blanket context-is-required-for-every-suffix claim.
- Keep C5 ceiling-limited and supplied-context only.
- Keep C6 as observed finite-budget degradation only; no fitted capacity law.
- Keep C7 boundary/supplement unless paired seed-level local-vs-global grouping exists.
- Keep C13 symbolic transition-cue context selection only.
- Keep Exp15 replay collapse as non-claim pending audit.
- Do not claim broad neural superiority, solved continual learning, raw sensory latent-world discovery, or biological validation.

Do not do these unless explicitly requested:

- Do not rerun experiments.
- Do not modify experiment code.
- Do not start Exp16 or optional successor experiments.
- Do not add memory-augmented/key-value neural baselines unless a venue/reviewer strategy requires them.
- Do not audit Exp15 replay unless specifically requested.
- Do not create final bibliography files until a venue/citation convention is chosen.

Definition of done:

- `docs/manuscript/draft/MANUSCRIPT_V2.md` has final-safe caption/placeholder prose for the current figure/table package and no unreviewed submission-blocking TODOs.
- Compact Table 3 remains descriptive and source-data-backed.
- Table 4 remains minimal fixed-profile neural-comparator evidence with caveats.
- Operational docs point to the next real blocker after caption/TODO cleanup.
- Final response summarizes changed files, verifier status if run, final caption/TODO status, and remaining blockers.
```
"""
    write("docs/manuscript/finalization/NEXT_STEP_PROMPT.md", next_prompt)


def finalize() -> int:
    patch_manuscript()
    temp = restore_real_verifier_to_temp()
    try:
        code, output = run_real_verifier(temp)
        update_status_docs(code, output)
        temp.unlink(missing_ok=True)

        # Restore the real verifier script and remove the branch-local workflow.
        run(["git", "checkout", "origin/main", "--", "scripts/verify_doc_source_paths.py"])
        (ROOT / ".github/workflows/temp-finalize-table3-placeholder.yml").unlink(missing_ok=True)

        run(["git", "config", "user.name", "github-actions[bot]"])
        run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"])
        run(["git", "add", "docs/manuscript/draft/MANUSCRIPT_V2.md", "docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md", "docs/manuscript/finalization/FINALIZATION_CHECKLIST.md", "docs/manuscript/MANUSCRIPT_TODO.md", "docs/synthesis/PUBLICATION_READINESS.md", "docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md", "docs/manuscript/finalization/NEXT_STEP_PROMPT.md", "scripts/verify_doc_source_paths.py", ".github/workflows/temp-finalize-table3-placeholder.yml"])
        diff = run(["git", "diff", "--cached", "--quiet"], check=False)
        if diff.returncode != 0:
            run(["git", "commit", "-m", "Finalize compact Table 3 manuscript alignment"])
            run(["git", "push", "origin", f"HEAD:{BRANCH}"])
        return code
    finally:
        temp.unlink(missing_ok=True)


def main() -> int:
    head_ref = os.environ.get("GITHUB_HEAD_REF") or os.environ.get("GITHUB_REF_NAME") or ""
    if head_ref == BRANCH:
        return finalize()
    temp = restore_real_verifier_to_temp()
    try:
        code, output = run_real_verifier(temp)
        print(output)
        return code
    finally:
        temp.unlink(missing_ok=True)


if __name__ == "__main__":
    sys.exit(main())
