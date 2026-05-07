# Prompt: Extract Thread Analysis Digest

```text
I am consolidating this experiment analysis thread into the GitHub repository for manuscript preparation.

Please create a structured, forensic digest of this conversation and package it for repository import.

Repository import contract:
- Produce a downloadable zip archive.
- The zip archive must contain exactly one required markdown digest file:
  `<THREAD_DIGEST_FILENAME>.md`
- Replace `<THREAD_DIGEST_FILENAME>` with the actual digest filename, without angle brackets.
- Use a stable, repo-safe, lower_snake_case filename that identifies the thread scope.
- Prefer filenames like:
  - `experiment13_1_analysis_digest.md`
  - `experiment14_baseline_design_digest.md`
  - `experiment13_publication_hardening_analysis_digest.md`
- Do not name the file literally `<THREAD_DIGEST_FILENAME>.md`.
- Do not put the digest inside a nested directory in the zip.
- Do not include generated repo updates in the zip. This package is only the thread digest for later import.
- The expected local staging path after download is:
  `docs/imports/<THREAD_DIGEST_FILENAME>.zip`
- The expected final repository path after import is:
  `docs/threads/<THREAD_DIGEST_FILENAME>.md`

Do not add new speculation unless clearly labeled.
Extract only what was actually discussed, designed, concluded, corrected, or analyzed in this thread.
Distinguish completed results from design proposals.
Use exact experiment numbers and artifact filenames when available.
Use current repo-relative paths with the `experiments/...` prefix when local paths are known.
If local paths are unknown, stale, or only represented by uploaded files, mark them `local verification pending`.

The markdown digest inside the zip must use the following structure:

# Thread Digest: Experiment <ID> <short title>

Digest filename: `<THREAD_DIGEST_FILENAME>.md`
Intended repository path: `docs/threads/<THREAD_DIGEST_FILENAME>.md`
Import package expected at: `docs/imports/<THREAD_DIGEST_FILENAME>.zip`

## 1. Thread scope

What was this thread mainly about?

## 2. Experiment analyzed or designed

- Experiment ID:
- Experiment name:
- Experiment directory:
- Run profile:
- Run ID:
- Uploaded artifact bundle:
- Main local artifact paths, if known:
- Per-run database path, if applicable:

## 3. Experimental design discussed

Include:
- purpose;
- hypotheses;
- variants/baselines;
- metrics;
- run profiles;
- expected outcomes;
- implementation notes;
- known risks.

If the thread analyzed completed results, distinguish original design from post-hoc interpretation.

## 4. Results analyzed

For each result:

### Result <N>: <title>

Claim:
Evidence:
Caveat:
Source artifact:
Thread status:

Status options:
- Strong
- Promising
- Preliminary
- Needs rerun
- Needs metric cleanup
- Needs baseline
- Historical only
- Do not use

## 5. Key scientific conclusions supported by this thread

Use:

Claim:
Evidence:
Caveat:
Experiment:
Artifact(s):
Manuscript relevance:

## 6. Important flaws, mistakes, or implementation concerns identified

Include:
- metric problems;
- artifact problems;
- validation warnings;
- suspicious results;
- seed/statistical limitations;
- naming or ablation-definition problems;
- anything requiring rerun.

## 7. Figures or artifacts referenced

List:
- filenames;
- CSVs;
- reports;
- plots;
- validation artifacts;
- run manifests.

## 8. Decisions made

List concrete decisions:
- interpretation decisions;
- manuscript framing decisions;
- whether claim statuses changed;
- whether result belongs in main/supplement;
- follow-up experiments.

## 9. Open questions

List unresolved scientific or implementation questions.

## 10. Relationship to first manuscript

Explain how this thread contributes to:
- central claim;
- supporting claim;
- limitation;
- future work;
- supplementary material.

## 11. Claims-and-evidence rows contributed by this thread

Create a markdown table:

| Claim | Evidence | Caveat | Experiment(s) | Artifact(s) | Manuscript status |
|---|---|---|---|---|---|

## 12. Required repository updates

List exact files to update:

- `experiments/<experiment_dir>/README.md`
- `docs/threads/...`
- `docs/experiments/...`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/synthesis/PROJECT_STATUS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/synthesis/NEXT_EXPERIMENTS.md`
- `docs/repo_audit/...`

## 13. Recommended next action

State what should happen next.

## 14. Import package checklist

Confirm:

- Zip filename:
- Digest filename inside zip:
- Digest is at zip root, not nested:
- Digest final path after repo import:
- Digest contains only thread-derived analysis, not direct repo edits:
- Any local artifact paths needing verification:

Important:
This digest will be imported into the repository under `docs/threads/`.
The zip should be downloaded to `docs/imports/` before running the repository import prompt.
It must be conservative, source-oriented, and useful to a future agent.
```
