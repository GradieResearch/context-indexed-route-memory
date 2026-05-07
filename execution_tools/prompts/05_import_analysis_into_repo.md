# Prompt: Import Analysis Into Repository

```text
You are working inside the local repository:

GradieResearch/context-indexed-route-memory

We have completed analysis of Experiment <ID> in a ChatGPT thread and saved the thread digest package under:

docs/imports/<THREAD_DIGEST_FILENAME>.zip

The import package should contain:

`<THREAD_DIGEST_FILENAME>.md`

After validating and extracting the package, the digest must be placed at:

docs/threads/<THREAD_DIGEST_FILENAME>.md

Your task is to import that analysis into the repository’s canonical documentation system.

Do not modify experiment code.
Do not rerun experiments.
Do not delete generated artifacts.
Do not delete the original zip from `docs/imports/` unless explicitly asked.
Do not invent conclusions.
Do not strengthen claims beyond the thread digest and local artifacts.
Do not treat design proposals as completed results.
If the thread digest and local artifacts conflict, record the conflict.

Evidence discipline:
Claim -> Evidence -> Caveat -> Source path

Every claim must cite:
1. the thread digest path, and
2. the local artifact path if available.

If local artifact support is absent, mark:
`local verification pending`.

Source path discipline:
- Active manuscript/evidence/source paths must use current `experiments/...` prefixes.
- Do not cite stale root-level experiment paths such as `experiment12_capacity_generalization/...`.
- If a referenced artifact does not exist locally, mark it planned, missing, future, or local verification pending instead of treating it as evidence.
- Rerun and run-output paths must remain inside the owning experiment directory.


Naming convention:
- Do not assume a literal file named `expNN_summary.md` exists.
- Inspect `docs/experiments/EXPERIMENT_REGISTRY.md` and existing summaries.
- Use the repository's convention, for example `docs/experiments/exp13_summary.md`, `docs/experiments/exp13_1_summary.md`, or `docs/experiments/<experiment_id>_summary.md`.
- If no summary exists, create one from `docs/experiments/EXPERIMENT_SUMMARY_TEMPLATE.md`.

Inputs:
- Import zip: `docs/imports/<THREAD_DIGEST_FILENAME>.zip`
- Thread digest after extraction: `docs/threads/<THREAD_DIGEST_FILENAME>.md`
- Experiment directory: `experiments/<EXPERIMENT_DIR>/`
- Current canonical docs:
  - `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
  - `docs/manuscript/FIGURE_PLAN.md`
  - `docs/manuscript/LIMITATIONS_AND_THREATS.md`
  - `docs/manuscript/MANUSCRIPT_TODO.md`
  - `docs/experiments/EXPERIMENT_REGISTRY.md`
  - `docs/synthesis/PROJECT_STATUS.md`
  - `docs/synthesis/PUBLICATION_READINESS.md`
  - `docs/synthesis/NEXT_EXPERIMENTS.md`
  - `docs/threads/THREAD_INDEX.md`

Tasks:

################################################################################
# Phase 0 - Stage thread digest from import zip
################################################################################

Validate the import package before changing canonical docs.

Steps:
- Confirm `docs/imports/<THREAD_DIGEST_FILENAME>.zip` exists.
- Inspect the zip contents.
- Confirm it contains exactly one required markdown digest named `<THREAD_DIGEST_FILENAME>.md`.
- Confirm the markdown digest is at the zip root, not nested inside a directory.
- If the zip contains extra files, ignore them unless they are explicitly documented as supporting context; do not import generated repo edits from the zip.
- Extract only `<THREAD_DIGEST_FILENAME>.md` to a temporary location or directly to `docs/threads/<THREAD_DIGEST_FILENAME>.md`.
- If `docs/threads/<THREAD_DIGEST_FILENAME>.md` already exists, do not overwrite it silently. Compare contents and either preserve the existing file or create a clearly named conflict note in `docs/repo_audit/THREAD_IMPORT_CONFLICTS.md`.
- Confirm the extracted digest begins with `# Thread Digest:` and includes the import package checklist.
- Use `docs/threads/<THREAD_DIGEST_FILENAME>.md` as the source thread path for all later updates.

################################################################################
# Phase 1 — Inspect local artifacts
################################################################################

Inspect the experiment directory and analysis outputs.

Identify:
- run ID(s);
- per-run SQLite database or raw run record if applicable;
- generated report;
- validation report;
- metrics CSVs;
- summary CSVs;
- plots;
- run manifest;
- README;
- run scripts.

Confirm that artifact paths mentioned in the thread digest exist.

Record missing or renamed artifacts.
Record any artifact path that does not use the current `experiments/...` prefix.

################################################################################
# Phase 2 — Update thread index
################################################################################

Update `docs/threads/THREAD_INDEX.md`.

Add the new thread digest row with:
- thread file;
- experiments covered;
- main purpose;
- contains completed results;
- contains designs only;
- imported into summaries;
- imported into claims;
- notes.

################################################################################
# Phase 3 — Update experiment summary
################################################################################

Create or update:

`docs/experiments/<experiment_id>_summary.md`

If a summary already exists, add an "Analysis import" or "Thread-derived analysis" section.

Include:

## Evidence status

- Local artifacts indexed:
- Local artifacts checked for key claims:
- Owning experiment README completed-runs/results updated:
- Thread digest imported:
- Human/manuscript validation pending:
- Claims fully validated for publication:

## Key results

Use:

### Result <N>: <title>

Claim:
Evidence:
Caveat:
Source thread:
Source artifact:
Manuscript status:

## What this experiment supports

## What this experiment does not prove

## Known caveats

## Candidate manuscript figures

## Required follow-up

Do not overwrite existing useful summary content unless it is stale or contradicted by the new analysis.

Also update `experiments/<EXPERIMENT_DIR>/README.md` if completed run results, run database paths, configuration notes, GPU limitations, or analysis output paths are missing from its completed-runs/results section.

################################################################################
# Phase 4 — Update experiment registry
################################################################################

Update `docs/experiments/EXPERIMENT_REGISTRY.md`.

For the experiment:
- update thread digest;
- update local artifact status;
- update manuscript role;
- update evidence status;
- update required follow-up.

If this is a new experiment, add a new row.

################################################################################
# Phase 5 — Update claims and evidence
################################################################################

Update `docs/manuscript/CLAIMS_AND_EVIDENCE.md`.

For each claim affected by this experiment:
- strengthen, weaken, refine, or leave unchanged;
- update status only if justified;
- add source thread path;
- add local artifact paths;
- add caveat;
- add required follow-up.

Do not add new claims unless necessary.
If adding a new claim, assign a new claim ID and make it conservative.

If the experiment invalidates or weakens a claim, mark that explicitly.

################################################################################
# Phase 6 — Update figure plan
################################################################################

Update `docs/manuscript/FIGURE_PLAN.md`.

Add or revise figure entries:
- source data;
- source plot;
- claim supported;
- caveat;
- main/supplement status.

Do not treat generated plots as final paper figures unless final figure scripts exist.

################################################################################
# Phase 7 — Update limitations and threats
################################################################################

Update `docs/manuscript/LIMITATIONS_AND_THREATS.md`.

Add new limitations from the thread digest.

Examples:
- metric cleanup;
- insufficient seeds;
- baseline gap;
- context-label/oracle limitation;
- stochastic corruption limitation;
- applied bridge limitation;
- biological overclaiming risk.

################################################################################
# Phase 8 — Update manuscript TODO and synthesis docs
################################################################################

Update:
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/synthesis/PROJECT_STATUS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/synthesis/NEXT_EXPERIMENTS.md`

Reflect:
- experiment completed;
- analysis imported;
- new blockers;
- resolved blockers;
- next recommended action.

Do not mark something complete unless the artifact exists.
Do not mark a run complete unless its owning experiment README records the run and the artifacts are present.

################################################################################
# Phase 9 — Source data and artifact index
################################################################################

If the experiment produced small, evidence-critical aggregate summary CSVs, consider copying them into:

`docs/source_data/`

Only if this is already a repo convention.

If copied:
- preserve source artifact path;
- update `docs/source_data/README.md`;
- do not hide original experiment path.

Update artifact indices if they are maintained:
- `docs/repo_audit/ARTIFACT_INDEX.csv`
- `docs/experiments/EXPERIMENT_ARTIFACTS_INDEX.csv`

If indexes are generated by scripts, do not manually edit unless instructed; instead note that regeneration is required.

################################################################################
# Phase 10 — Conflict log
################################################################################

Create or update:

`docs/repo_audit/THREAD_IMPORT_CONFLICTS.md`

Record:
- claims in thread digest without local artifact support;
- missing artifacts;
- thread/artifact contradictions;
- claims that may be too strong;
- implementation caveats;
- required reruns.

################################################################################
# Phase 11 — Import report
################################################################################

Create:

`docs/repo_audit/EXP<ID>_ANALYSIS_IMPORT_REPORT.md`

Include:

# Experiment <ID> Analysis Import Report

## Summary

## Import package reviewed

## Thread digest imported

## Local artifacts reviewed

## Docs updated

## Claims changed

| Claim ID | Change | Reason | Source |
|---|---|---|---|

## Figures changed

## Limitations added

## TODOs added or resolved

## Conflicts or caveats

## Path verification result

################################################################################
# Phase 12 — Verification
################################################################################

Run:

python scripts/verify_doc_source_paths.py

Fix active broken paths.
Fix stale source paths that omit the `experiments/...` prefix, unless they are deliberately marked historical, future, planned, missing, or local verification pending.

Do not commit.
Do not push.

Final response:
1. Files modified.
2. Owning experiment README/run log changed.
3. Claims changed.
4. Figures changed.
5. Limitations added.
6. TODOs changed.
7. Conflicts recorded.
8. Path verifier result.
9. Recommended QA prompt or next action.
```
