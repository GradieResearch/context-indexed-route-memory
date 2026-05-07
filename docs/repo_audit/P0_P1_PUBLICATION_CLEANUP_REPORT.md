# P0/P1 Publication Cleanup Report

## Scope

This cleanup pass covers repository-readiness, manuscript-readiness, reproducibility, artifact indexing, source-data manifesting, statistical-readiness auditing, and documentation alignment for the non-Exp13.2 manuscript spine.

Exp13.2 is intentionally excluded. This pass did not modify `experiments/experiment13_2_baseline_suite/`, did not analyze Exp13.2 results, did not create the planned/future `docs/manuscript/BASELINE_RESULTS.md`, and did not mark C12 complete.

## Files Changed

- `README.md`
- `docs/README.md`
- `docs/experiments/EXPERIMENT_ARTIFACTS_INDEX.csv`
- `docs/experiments/EXPERIMENT_CLAIMS_MATRIX.csv`
- `docs/experiments/EXPERIMENT_REGISTRY.md`
- `docs/experiments/HISTORICAL_EXPERIMENTS.md`
- `docs/manuscript/BASELINE_REQUIREMENTS.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/manuscript/SOURCE_OF_TRUTH.md`
- `docs/repo_audit/ARTIFACT_INDEX.csv`
- `docs/repo_audit/MISSING_ARTIFACTS.md`
- `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`
- `docs/repo_audit/PATH_VERIFICATION_REPORT.md`
- `docs/repo_audit/P0_P1_PUBLICATION_CLEANUP_REPORT.md`
- `docs/source_data/README.md`
- `docs/source_data/SOURCE_DATA_MANIFEST.csv`
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`
- `docs/synthesis/NEXT_EXPERIMENTS.md`
- `docs/synthesis/PROJECT_STATUS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/synthesis/ROADMAP.md`
- `scripts/compute_seed_metric_summary.py`

Pre-existing unrelated dirty worktree items under `execution_tools/prompts/` were not touched. The previously mentioned upload-bundle path `experiments/experiment14_latent_context_inference/e14_analysis.zip` is missing/local verification pending and is not cited as an active repository artifact.

## Checks Run

| Command | Status | Notes |
|---|---|---|
| `python scripts/verify_doc_source_paths.py` | Passed before edits | Initial result: 83 files scanned, 5304 OK paths, 0 missing active paths. |
| `python scripts/compute_seed_metric_summary.py --help` | Passed | Help output confirms explicit input/output/grouping interface. |
| `python scripts/verify_doc_source_paths.py` | Passed after edits | Final result: 86 files scanned, 4462 OK paths, 0 missing active paths, 11 planned/future skips, 41 local-verification-pending skips. |
| `git status --short` | Passed inspection | Confirmed no Exp13.2 experiment artifact modifications; unrelated pre-existing dirty files remain. |

## P0 Items Addressed

- Re-established active canonical docs around the non-Exp13.2 scope.
- Kept C12 as `Needs baseline` and deferred Exp13.2 to a separate import/alignment pass.
- Updated baseline requirements as planning/deferred rather than completed baseline evidence.
- Regenerated artifact indexes excluding Exp13.2 and junk files such as `.DS_Store`, `__pycache__`, and `.pyc`.
- Added source-data and statistical-readiness manifests for non-Exp13.2 claim support.
- Added a non-destructive generic seed-summary utility for future human-reviewed CI tables.
- Updated reproducibility and missing-artifact audits for Exp11, Exp12, Exp13, and Exp13.1.
- Added license/citation metadata as an explicit readiness blocker because `LICENSE` and `CITATION.cff` are missing.

## P1 Items Addressed

- Improved README/docs navigation to point at current readiness and audit files.
- Updated publication-readiness and project-status docs to say the repo is improved but not submission-ready.
- Added final-figure readiness notes to the figure plan for candidate main figures.
- Preserved historical/supporting experiment tiers and kept Exp1-Exp6 from being elevated.
- Documented that Exp13.1 lesion evidence failed the expected pattern and must not be used positively without audit/rerun.

## Remaining P0 Blockers

- Complete separate Exp13.2 analysis/import/alignment pass.
- Generate manuscript-grade seed-level confidence intervals and effect sizes.
- Build final reproducible figure scripts and reviewed source-data tables.
- Import prior-art/novelty source artifact; `Pasted text.txt` remains local verification pending.
- Verify manuscript-critical run commands on a fresh checkout with runtime/hardware logs.
- Add human-chosen `LICENSE` and `CITATION.cff`.
- Fix Exp13 holdout seen/unseen metrics if C9 remains central.

## Remaining P1 Blockers

- Audit/rerun Exp13.1 lesion diagnostic only if positive lesion evidence is needed.
- Add stochastic context corruption if generic robustness is claimed.
- Add consolidation dose-response or keep consolidation supplementary.
- Add capacity-law fitting if C6/C7 become central quantitative results.
- Add explicit device/runtime metadata to future Exp13.1 manifests.

## Scientific Claims Changed

No scientific claim was strengthened.

Claim -> Exp13.2 should not be used in this pass to complete C12 or refine C1-C4.
Evidence -> The user explicitly scoped Exp13.2 out of this cleanup pass, and active docs now mark Exp13.2 import/alignment as deferred.
Caveat -> This is a scope/readiness alignment change, not a negative analysis of Exp13.2 artifacts.
Source path -> `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md`; `docs/manuscript/MANUSCRIPT_TODO.md`

## Path Verification Result

Final result: pass. The verifier reported 86 files scanned, 4462 OK path observations, 0 missing active paths, 11 planned/future skips, and 41 local-verification-pending skips.

## Recommended Next Action

1. Complete separate Exp13.2 analysis/import/alignment pass.
2. Generate manuscript-grade CI/effect-size tables.
3. Build final reproducible figure scripts/source-data manifests.
4. Draft the manuscript from the current Exp11-Exp13.1 spine.
5. Decide whether Exp13.1 lesion rerun, Exp13 holdout metric cleanup, or stochastic context corruption are necessary based on final manuscript claims.
