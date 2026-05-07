# Prompt: Import Staged Analysis Digest Into Repository

```text
You are working inside the local repository:

GradieResearch/context-indexed-route-memory

A ChatGPT experiment-analysis thread produced a staged digest package for repository import.

This prompt is for LOCAL REPOSITORY MAINTENANCE ONLY.

You must:
- validate and import the staged thread digest;
- inspect the local experiment artifacts;
- update repository documentation conservatively;
- record conflicts and verification gaps;
- create an import report;
- run path verification.

You must not:
- modify experiment code;
- rerun experiments;
- delete generated artifacts;
- delete the import zip unless explicitly instructed;
- invent conclusions;
- strengthen claims beyond the staged digest and verified local artifacts;
- treat planned designs, hypotheses, or future-work notes as completed results;
- commit or push.

################################################################################
# Inputs
################################################################################

Repository:

GradieResearch/context-indexed-route-memory

Import zip:

docs/imports/<THREAD_DIGEST_FILENAME>.zip

Expected digest inside zip:

<THREAD_DIGEST_FILENAME>.md

Expected final digest path:

docs/threads/<THREAD_DIGEST_FILENAME>.md

Experiment metadata:

- Experiment ID: <ID>
- Experiment name: <EXPERIMENT_NAME>
- Experiment directory: experiments/<EXPERIMENT_DIR>/
- Run ID(s): <RUN_ID_OR_IDS>
- Run profile(s): <PROFILE_OR_PROFILES>
- Main analysis directory/directories:
  - experiments/<EXPERIMENT_DIR>/analysis/<RUN_ID>/
- Database/raw record path(s), if applicable:
  - experiments/<EXPERIMENT_DIR>/runs/<RUN_ID>.sqlite3

Known key artifact paths, if provided:

<KEY_ARTIFACT_PATHS_OR_WRITE_NONE_PROVIDED>

Required docs to inspect/update:

- experiments/<EXPERIMENT_DIR>/README.md
- docs/threads/THREAD_INDEX.md
- docs/experiments/EXPERIMENT_REGISTRY.md
- docs/experiments/<experiment_id>_summary.md
- docs/manuscript/CLAIMS_AND_EVIDENCE.md
- docs/manuscript/FIGURE_PLAN.md
- docs/manuscript/LIMITATIONS_AND_THREATS.md
- docs/manuscript/MANUSCRIPT_TODO.md
- docs/manuscript/BASELINE_REQUIREMENTS.md if relevant
- docs/synthesis/PROJECT_STATUS.md
- docs/synthesis/PUBLICATION_READINESS.md
- docs/synthesis/NEXT_EXPERIMENTS.md
- docs/source_data/ if repo convention requires source-data mirrors
- docs/repo_audit/ARTIFACT_INDEX.csv if maintained manually
- docs/experiments/EXPERIMENT_ARTIFACTS_INDEX.csv if maintained manually
- docs/repo_audit/THREAD_IMPORT_CONFLICTS.md
- docs/repo_audit/EXP<ID>_ANALYSIS_IMPORT_REPORT.md

################################################################################
# Core interpretation rules
################################################################################

The staged thread digest is the analysis import source.

Local artifacts are the verification source.

Use this hierarchy:

1. Local artifact evidence can support the digest.
2. Local artifact evidence can narrow or weaken the digest.
3. Local artifact evidence can reveal conflicts with the digest.
4. If the digest makes a claim but no local artifact path supports it, keep the claim only if clearly marked:
   `local verification pending`.
5. If the local artifacts contradict the digest, do not silently choose one. Record the conflict in:
   docs/repo_audit/THREAD_IMPORT_CONFLICTS.md
6. If existing repository docs contradict the digest or artifacts, record the conflict before updating.
7. If registry/status docs say an experiment is planned/design-only but local completed artifacts exist, reconcile conservatively and record the status transition in the import report.
8. If artifacts exist only in the import bundle or are referenced by upload-only names, do not invent repo-relative paths.

Do not convert a promising result into a central manuscript claim unless the digest and local artifacts both support that status.

################################################################################
# Evidence discipline
################################################################################

Use the pattern:

Claim -> Evidence -> Caveat -> Source path

Every completed-result claim must cite:

1. the imported thread digest:
   docs/threads/<THREAD_DIGEST_FILENAME>.md

2. at least one local artifact path, when available:
   experiments/<EXPERIMENT_DIR>/...

If local artifact support is absent, stale, renamed, missing, LFS-only, or not directly inspectable, write:

`local verification pending`

Evidence path rules:

- Active experiment evidence paths must use `experiments/...`.
- Do not cite stale root-level experiment paths as active evidence.
- Do not cite screenshots, pasted snippets, or upload-only paths as if they are repo artifacts.
- Missing artifacts must be marked:
  `missing`, `planned`, `future work`, or `local verification pending`.
- Run outputs must remain inside the owning experiment directory.
- Do not copy large generated artifacts into documentation directories.
- Only create small source-data mirrors if this is already a repository convention, and preserve the original artifact path.

################################################################################
# Claim status discipline
################################################################################

When updating claims, use conservative manuscript status labels such as:

- Strong
- Promising
- Preliminary
- Needs rerun
- Needs metric cleanup
- Needs implementation audit
- Needs baseline
- Needs final figure
- Supplement only
- Historical only
- Do not use
- Local verification pending

Do not remove caveats when promoting a result.

Do not upgrade a claim from preliminary/promising to strong unless:
- validation passed;
- local artifact paths are verified;
- metrics are clear;
- seed count/uncertainty are adequate for the claim;
- relevant baselines or controls exist;
- the digest explicitly supports the stronger interpretation.

################################################################################
# Figure discipline
################################################################################

Generated analysis plots are not automatically paper-ready figures.

When updating FIGURE_PLAN.md, distinguish:

- diagnostic plot;
- generated analysis plot;
- candidate manuscript panel;
- supplement candidate;
- final manuscript figure;
- do not use.

A generated plot can become a candidate manuscript panel only if:
- the artifact path exists;
- the plotted metric is valid;
- the caption-worthy claim is explicitly supported;
- the caveat is recorded;
- no final figure regeneration script is missing, or the missing final script is listed as a TODO.

If a plot is useful but not final, mark it as:
`candidate figure; final rendering pending`.

################################################################################
# Phase 0 — Preflight
################################################################################

Before changing files:

1. Confirm the import zip exists:
   docs/imports/<THREAD_DIGEST_FILENAME>.zip

2. Inspect zip contents.

3. Confirm the zip contains exactly one markdown digest at the zip root:
   <THREAD_DIGEST_FILENAME>.md

4. Confirm the digest filename matches the expected final path:
   docs/threads/<THREAD_DIGEST_FILENAME>.md

5. Confirm the digest begins with:
   `# Thread Digest:`

6. Confirm the digest contains an import checklist or equivalent repository-update section.

7. If the digest already exists in docs/threads/:
   - compare the existing file with the staged digest;
   - do not silently overwrite;
   - if identical, record that no extraction change was needed;
   - if different, preserve the current file by reviewing the diff and record the replacement in the import report.

################################################################################
# Phase 1 — Stage digest
################################################################################

Extract only the markdown digest to:

docs/threads/<THREAD_DIGEST_FILENAME>.md

Do not extract unrelated files.

Do not extract generated repo updates.

Do not extract Codex prompts as thread digests.

After extraction, inspect the digest and identify:

- experiment ID;
- experiment name;
- experiment directory;
- run profile(s);
- run ID(s);
- uploaded artifact bundle;
- claimed local artifact paths;
- per-run database path(s);
- key results;
- claim/evidence/caveat rows;
- required repository updates;
- open questions;
- paths needing verification;
- recommended next action.

################################################################################
# Phase 2 — Inspect local artifacts
################################################################################

Inspect the owning experiment directory:

experiments/<EXPERIMENT_DIR>/

Inspect, where present:

- README;
- experiment summary docs;
- run scripts;
- validation/start scripts;
- analysis directories;
- run directories;
- generated reports;
- validation reports;
- validation JSON;
- metrics CSVs;
- summary CSVs;
- effect-size/statistics CSVs;
- plots;
- manifest/config files;
- progress logs;
- SQLite/raw run records;
- device/runtime metadata;
- warnings;
- failed validation checks.

For each expected run ID, determine:

- run exists / missing;
- analysis directory exists / missing;
- database/raw record exists / missing / not applicable;
- validation status PASS/WARN/FAIL/unknown;
- metrics present / missing;
- plots present / missing;
- manifest/config present / missing;
- progress log present / missing;
- README run log updated / stale / absent.

Create an artifact audit summary for the import report.

Use a table like:

| Artifact class | Expected path | Status | Notes |
|---|---|---|---|
| Thread digest | docs/threads/<THREAD_DIGEST_FILENAME>.md | verified/missing/conflict | ... |
| Report | experiments/<EXPERIMENT_DIR>/analysis/<RUN_ID>/<REPORT> | verified/missing | ... |
| Validation report | ... | PASS/WARN/FAIL/missing | ... |
| Metrics CSV | ... | verified/missing | ... |
| Plot | ... | verified/missing | ... |
| SQLite/raw record | ... | verified/missing/not applicable | ... |

################################################################################
# Phase 3 — Decide import posture
################################################################################

Before updating claims, decide the import posture.

Choose one:

1. Completed validated result
2. Completed result with warnings
3. Partial result
4. Failed/invalid run
5. Design-only import
6. Analysis-only import with local verification pending
7. Conflict import requiring human review

Record this posture in:

docs/repo_audit/EXP<ID>_ANALYSIS_IMPORT_REPORT.md

Use the posture to control documentation updates:

- Completed validated result:
  update registry, README, claims, figures, limitations, TODOs, synthesis docs.

- Completed result with warnings:
  update docs, but mark caveats and warning status clearly.

- Partial result:
  update thread index and experiment summary; do not promote claims.

- Failed/invalid run:
  record as failed/diagnostic; do not use as manuscript evidence unless failure itself is relevant.

- Design-only import:
  update design/planning sections only; do not update completed-results claims.

- Analysis-only import with local verification pending:
  import digest and record pending paths; avoid claims promotion.

- Conflict import requiring human review:
  import digest, record conflicts, minimize claims changes.

################################################################################
# Phase 4 — Update repository docs
################################################################################

Update docs conservatively and only where supported.

Required updates:

1. Thread index

Update:

docs/threads/THREAD_INDEX.md

Add a row for:

docs/threads/<THREAD_DIGEST_FILENAME>.md

Include:
- experiment ID;
- short title;
- date if available;
- run ID(s);
- import posture;
- key contribution;
- caveat.

2. Owning experiment README

Update:

experiments/<EXPERIMENT_DIR>/README.md

Add or update:
- completed run(s);
- run profile(s);
- validation status;
- main artifact paths;
- key result summary;
- known caveats;
- manuscript status;
- next action.

Do not rewrite the entire README unless necessary.

3. Experiment registry

Update:

docs/experiments/EXPERIMENT_REGISTRY.md

Record:
- experiment status;
- run ID(s);
- validation status;
- artifact location;
- manuscript relevance;
- caveat;
- whether results are imported from a thread digest.

If the registry previously listed the experiment as planned/design-only but artifacts now exist, record that transition clearly.

4. Experiment summary

Create or update:

docs/experiments/<experiment_id>_summary.md

Include:
- purpose;
- design;
- run IDs;
- artifact paths;
- key results;
- caveats;
- manuscript status;
- relationship to claims;
- next action.

5. Claims and evidence

Update:

docs/manuscript/CLAIMS_AND_EVIDENCE.md

For each changed claim:
- do not strengthen beyond evidence;
- include digest path;
- include local artifact path;
- include caveat;
- include manuscript status.

Use claim IDs already present when possible.

If a result requires a new claim, add it only if the digest explicitly recommends it and local artifacts support it.

Otherwise record it as:
`possible future claim / not yet promoted`.

6. Figure plan

Update:

docs/manuscript/FIGURE_PLAN.md

For each referenced plot:
- path;
- what it shows;
- supported claim;
- caveat;
- status:
  diagnostic / candidate panel / supplement / final pending / do not use.

7. Limitations and threats

Update:

docs/manuscript/LIMITATIONS_AND_THREATS.md

Add or refine:
- metric limitations;
- baseline limitations;
- implementation limitations;
- symbolic-vs-neural limitations;
- oracle/context assumptions;
- seed/uncertainty limitations;
- generalization boundaries;
- artifact/local verification issues.

8. Manuscript TODO

Update:

docs/manuscript/MANUSCRIPT_TODO.md

Add, resolve, or refine TODOs for:
- reruns;
- metric cleanup;
- implementation audits;
- baseline work;
- final figure generation;
- source-data mirrors;
- claim narrowing;
- prior-art positioning;
- manuscript drafting.

9. Baseline requirements

If relevant, update:

docs/manuscript/BASELINE_REQUIREMENTS.md

Only update this file if the experiment affects baseline interpretation.

10. Synthesis docs

Update as appropriate:

- docs/synthesis/PROJECT_STATUS.md
- docs/synthesis/PUBLICATION_READINESS.md
- docs/synthesis/NEXT_EXPERIMENTS.md

Keep synthesis updates concise and traceable.

Do not rewrite the project narrative unless the imported result materially changes it.

11. Artifact indexes

Update only if these are manually maintained:

- docs/repo_audit/ARTIFACT_INDEX.csv
- docs/experiments/EXPERIMENT_ARTIFACTS_INDEX.csv

If they appear generated or stale, do not manually edit them. Instead, note regeneration needed in the import report.

################################################################################
# Phase 5 — Conflict log
################################################################################

Update or create:

docs/repo_audit/THREAD_IMPORT_CONFLICTS.md

Record any conflict involving:

- digest vs local artifacts;
- digest vs existing docs;
- artifact path missing or renamed;
- registry status mismatch;
- README status mismatch;
- validation report mismatch;
- metrics/report mismatch;
- upload-only artifact path;
- stale root-level path;
- generated plot treated as final figure without final script;
- claim strengthened beyond artifact support;
- missing source data;
- missing baseline support;
- missing reproducibility metadata.

Use this format:

## Experiment <ID>: <short conflict title>

- Date:
- Digest:
  docs/threads/<THREAD_DIGEST_FILENAME>.md
- Local artifact(s):
  <paths>
- Conflict:
  <what disagrees>
- Resolution:
  <what was done>
- Remaining action:
  <what still needs human or local verification>

If no conflicts are found, state that in the import report. Do not add noise to THREAD_IMPORT_CONFLICTS.md unnecessarily.

################################################################################
# Phase 6 — Import report
################################################################################

Create or update:

docs/repo_audit/EXP<ID>_ANALYSIS_IMPORT_REPORT.md

Use this structure:

# Experiment <ID> Analysis Import Report

## Summary

State:
- imported digest;
- experiment directory;
- run ID(s);
- import posture;
- validation status;
- high-level result;
- high-level caveat;
- whether claims were changed.

## Import package reviewed

- Zip path:
- Digest filename:
- Digest final path:
- Zip contents valid: yes/no
- Notes:

## Thread digest imported

- Final path:
- Existing digest overwritten: yes/no/not applicable
- Diff reviewed: yes/no/not applicable
- Notes:

## Local artifacts reviewed

| Artifact class | Path | Status | Notes |
|---|---|---|---|

## Run integrity summary

| Run ID | Profile | Analysis dir | Raw DB | Validation | Metrics | Plots | Notes |
|---|---|---|---|---|---|---|---|

## Docs updated

| File | Change summary |
|---|---|

## Claims changed

| Claim ID | Change | Evidence | Caveat | Status |
|---|---|---|---|---|

If no claims were changed, say so explicitly.

## Figures changed

| Figure/plot | Path | Change | Status | Caveat |
|---|---|---|---|---|

If no figures were changed, say so explicitly.

## Limitations added or refined

| Limitation | Reason | Source |
|---|---|---|

## TODOs added or resolved

| TODO | Change | Reason |
|---|---|---|

## Conflicts or caveats

State whether conflicts were recorded in:

docs/repo_audit/THREAD_IMPORT_CONFLICTS.md

Summarize unresolved issues.

## Path verification result

Include:
- command run;
- pass/fail status;
- broken paths found;
- fixes made;
- remaining broken paths, if any.

## Recommended next action

Choose one:
- repository QA review;
- rerun;
- metric cleanup;
- implementation audit;
- final figure generation;
- baseline implementation;
- manuscript drafting;
- next experiment;
- human review required.

################################################################################
# Phase 7 — Verification
################################################################################

Run:

python scripts/verify_doc_source_paths.py

Then:

1. Fix active broken paths introduced by this import.
2. Do not “fix” broken historical/planned paths by inventing files.
3. If a path is intentionally future/planned/missing, mark it clearly in the relevant doc.
4. Rerun the verifier after fixes if practical.
5. Record the final verifier result in:
   docs/repo_audit/EXP<ID>_ANALYSIS_IMPORT_REPORT.md

Also run lightweight repository checks if they exist and are safe documentation checks, for example:

- markdown link/path checks;
- docs lint scripts;
- artifact index validation scripts.

Do not run experiments.

Do not run long compute jobs.

Do not modify experiment code.

################################################################################
# Final response
################################################################################

When finished, respond with:

1. Import posture.
2. Files modified.
3. Digest imported.
4. README/run log changes.
5. Registry changes.
6. Claims changed.
7. Figures changed.
8. Limitations added or refined.
9. TODOs changed.
10. Conflicts recorded.
11. Path verifier result.
12. Remaining paths needing local verification.
13. Recommended next action.

Keep the final response factual and concise.

Do not claim success if verification failed.

Do not commit.

Do not push.