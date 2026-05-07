# Experiment 14 Analysis Import Report

## Summary

- Imported digest: `docs/threads/experiment14_analysis_digest.md`
- Experiment directory: `experiments/experiment14_latent_context_inference/`
- Run IDs: `exp14_full_20260507_210712`; `exp14_validation_20260507_210649`; `exp14_smoke_20260507_210610`
- Import posture: completed validated result
- Validation status: all three profiles PASS, 27 pass, 0 warn, 0 fail
- High-level result: Exp14 supports symbolic latent context/world selection from partial transition cues before route execution.
- High-level caveat: symbolic transition-cue inference only; oracle context-gated lookup remains an upper bound; generated plots are not final figures.
- Claims changed: yes, C13 added as a promising claim.

## Import package reviewed

- Zip path: `docs/imports/experiment14_analysis_digest.zip`
- Digest filename: `experiment14_analysis_digest.md`
- Digest final path: `docs/threads/experiment14_analysis_digest.md`
- Zip contents valid: yes
- Notes: zip contained exactly one root markdown digest, and the digest began with `# Thread Digest:`.

## Thread digest imported

- Final path: `docs/threads/experiment14_analysis_digest.md`
- Existing digest overwritten: not applicable
- Diff reviewed: not applicable
- Notes: digest did not previously exist under `docs/threads/`.

## Local artifacts reviewed

| Artifact class | Path | Status | Notes |
|---|---|---|---|
| Thread digest | `docs/threads/experiment14_analysis_digest.md` | verified | Extracted from staged zip only. |
| Experiment README | `experiments/experiment14_latent_context_inference/README.md` | verified/updated | Completed runs section added. |
| Full report | `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_report.md` | verified | Reports run identity and hard-slice summary. |
| Full validation report | `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_report.md` | PASS | 27 pass, 0 warn, 0 fail. |
| Full validation JSON | `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_results.json` | PASS | Machine-readable validation status. |
| Full manifest | `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/run_manifest.json` | verified | Includes config, row counts, runtime/device metadata, and CPU-only GPU rationale. |
| Full metrics CSV | `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_metrics.csv` | verified | 46,080 data rows. |
| Full summary CSV | `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv` | verified | 2,304 data rows. |
| Full effect sizes CSV | `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_effect_sizes.csv` | verified | 12,288 data rows. |
| Full progress log | `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/progress.jsonl` | verified | 46,083 events, includes `run_complete`. |
| Full plots | `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/plots/exp14_world_selection_vs_corruption.png` | verified | One of six generated analysis plots; candidate only. |
| Full SQLite DB | `experiments/experiment14_latent_context_inference/runs/exp14_full_20260507_210712.sqlite3` | verified | Tables: `effect_sizes`, `manifest`, `metrics`, `summary`. |
| Validation profile report | `experiments/experiment14_latent_context_inference/analysis/exp14_validation_20260507_210649/validation_report.md` | PASS | 27 pass, 0 warn, 0 fail. |
| Validation SQLite DB | `experiments/experiment14_latent_context_inference/runs/exp14_validation_20260507_210649.sqlite3` | verified | Tables: `effect_sizes`, `manifest`, `metrics`, `summary`. |
| Smoke profile report | `experiments/experiment14_latent_context_inference/analysis/exp14_smoke_20260507_210610/validation_report.md` | PASS | 27 pass, 0 warn, 0 fail. |
| Smoke SQLite DB | `experiments/experiment14_latent_context_inference/runs/exp14_smoke_20260507_210610.sqlite3` | verified | Tables: `effect_sizes`, `manifest`, `metrics`, `summary`. |

## Run integrity summary

| Run ID | Profile | Analysis dir | Raw DB | Validation | Metrics | Plots | Notes |
|---|---|---|---|---|---|---|---|
| `exp14_full_20260507_210712` | full | verified | verified | PASS | 46,080 metrics rows; 2,304 summary rows; 12,288 effect-size rows | 6 png files | Manuscript-facing analyzed run. |
| `exp14_validation_20260507_210649` | validation | verified | verified | PASS | 1,440 metrics rows; 288 summary rows; 1,512 effect-size rows | 6 png files | Medium sanity run. |
| `exp14_smoke_20260507_210610` | smoke | verified | verified | PASS | 112 metrics rows; 56 summary rows; 288 effect-size rows | 6 png files | Fast command/artifact sanity run. |

## Docs updated

| File | Change summary |
|---|---|
| `docs/threads/experiment14_analysis_digest.md` | Imported staged digest. |
| `docs/threads/THREAD_INDEX.md` | Added Exp14 digest row and import note. |
| `experiments/experiment14_latent_context_inference/README.md` | Added completed runs/results section with evidence/caveats. |
| `docs/experiments/EXPERIMENT_REGISTRY.md` | Added Exp14 row and recorded transition from prior design-only mentions to completed artifacts. |
| `docs/experiments/exp14_summary.md` | Created dedicated experiment summary. |
| `docs/manuscript/CLAIMS_AND_EVIDENCE.md` | Added C13 as promising symbolic latent-context evidence. |
| `docs/manuscript/FIGURE_PLAN.md` | Added Figure 9 candidate/supplement entry and readiness row. |
| `docs/manuscript/LIMITATIONS_AND_THREATS.md` | Refined oracle-context limitation and added Exp14 symbolic-context caveat. |
| `docs/manuscript/MANUSCRIPT_TODO.md` | Added Exp14 placement/final-figure TODO and moved richer latent-world inference to future work. |
| `docs/synthesis/PROJECT_STATUS.md` | Added Exp14 status and readiness caveat. |
| `docs/synthesis/PUBLICATION_READINESS.md` | Added Exp14 strongest/weakest evidence and reviewer-risk note. |
| `docs/synthesis/NEXT_EXPERIMENTS.md` | Added Exp14 placement as the next decision and follow-up guidance. |
| `docs/experiments/EXPERIMENT_CLAIMS_MATRIX.csv` | Added C13 mapping for Exp14. |
| `docs/repo_audit/P0_P1_PUBLICATION_CLEANUP_REPORT.md` | Marked an old upload-bundle zip reference as missing/local verification pending so it is not treated as an active artifact. |
| `docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md` | Created this import report. |

## Claims changed

| Claim ID | Change | Evidence | Caveat | Status |
|---|---|---|---|---|
| C13 | Added new latent symbolic context-inference claim. | `docs/threads/experiment14_analysis_digest.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_report.md` | Symbolic transition cues only; oracle remains upper bound; corruption is synthetic. | Promising |

## Figures changed

| Figure/plot | Path | Change | Status | Caveat |
|---|---|---|---|---|
| Figure 9 - Latent Symbolic Context Inference | `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/plots/exp14_world_selection_vs_corruption.png`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/plots/exp14_seen_composition_vs_corruption.png`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/plots/exp14_cue_count_selection_sensitivity.png`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/plots/exp14_cue_count_composition_sensitivity.png` | Added candidate figure/supplement entry. | Candidate panel; final rendering pending. | Generated analysis plots only; symbolic cues; oracle upper bound remains. |

## Limitations added or refined

| Limitation | Reason | Source |
|---|---|---|
| Latent context inference remains symbolic. | Exp14 uses symbolic transition cues, not raw sensory streams. | `docs/threads/experiment14_analysis_digest.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv` |
| Oracle context-gated lookup remains an upper bound. | Oracle stays at 1.0000 in hard corrupted slice and is not a fair latent-selector baseline. | `docs/threads/experiment14_analysis_digest.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv` |
| Generated Exp14 plots are not final figures. | Manuscript figure scripts/source-data mirrors are still needed if retained. | `docs/manuscript/FIGURE_PLAN.md` |

## TODOs added or resolved

| TODO | Change | Reason |
|---|---|---|
| Decide Exp14 manuscript placement and add final artifacts if retained. | Added. | C13 is promising but main/supplement placement is unresolved. |
| Richer latent-world inference. | Refined from generic future latent-world inference. | Exp14 now covers symbolic transition-cue selection but not raw sensory or learned perceptual context discovery. |

## Conflicts or caveats

No digest-vs-local-artifact conflicts were found. Earlier docs and thread digests described Exp14 as proposed/design-only; local artifacts now show completed validated runs. This was treated as a status transition, updated in active docs, and recorded in this report rather than added as a conflict entry.

Artifact indexes under `docs/repo_audit/ARTIFACT_INDEX.csv` and `docs/experiments/EXPERIMENT_ARTIFACTS_INDEX.csv` appear to be generated or broad audit outputs from a prior cleanup pass, so they were not manually edited during this import. Regenerate them in a later index-maintenance pass if Exp14 artifacts should be included there.

## Path verification result

- Command run: `python scripts/verify_doc_source_paths.py`
- Pass/fail status: pass after one fix
- Broken paths found: first run found one pre-existing active broken path in `docs/repo_audit/P0_P1_PUBLICATION_CLEANUP_REPORT.md` for missing/local verification pending upload bundle `experiments/experiment14_latent_context_inference/e14_analysis.zip`.
- Fixes made: marked the old upload-bundle path as missing/local verification pending and not an active repository artifact.
- Remaining broken paths, if any: none. Final result: 89 files scanned, 4,631 OK paths, 0 missing active paths, 11 planned/future skips, 43 local-verification-pending skips.

## Recommended next action

Manuscript placement decision: decide whether Exp14 C13 belongs in the main results, supplement, or follow-up framing. If retained, generate final figure scripts and source-data mirrors.
