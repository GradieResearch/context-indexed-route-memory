# Manuscript TODO

Purpose: Maintain a conservative work queue for turning this repository into a manuscript-grade research artifact.

## Current Next Operational Priority

Move from post-Exp14 documentation alignment into first-manuscript claim hardening. Exp13.2 is now treated as an imported symbolic/algorithmic baseline suite, and Exp14 is treated as imported symbolic transition-cue context-selection evidence.

Claim: The repository is close to a conservative first-manuscript claim freeze, but it is not submission-ready.

Evidence: Exp11, Exp12, Exp13, Exp13.1, Exp13.2, and Exp14 now have local artifacts and imported summaries. Exp13.2 partially satisfies symbolic/algorithmic baseline coverage, while Exp14 partially reduces the oracle-context-label limitation.

Caveat: The manuscript still needs final claim freeze, manuscript-grade uncertainty/effect-size tables, reproducible figure scripts, prior-art/novelty import, fresh command verification, and license/citation metadata. Neural baselines remain absent and must either be added or explicitly scoped out depending on target venue.

Source path: `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`; `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`; `docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`.

## P0 - Required Before Manuscript Draft

| TODO | Reason | Related experiment | Source path | Target output |
|---|---|---|---|---|
| Freeze first-manuscript claims. | The repository needs a stable claim boundary before final figures and prose drafting. | Manuscript-level | `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md` | Human-reviewed claim set with main, narrow-main, supplement, drop, and future-work statuses. |
| Decide Exp14 manuscript placement. | Exp14 is validated symbolic cue-selection evidence, but main-vs-supplement placement changes figure scope. | Exp14 | `docs/threads/experiment14_analysis_digest.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `docs/manuscript/FIGURE_PLAN.md` | Main/supplement decision, final figure script, and source-data mirror for retained panels. |
| Resolve venue baseline posture. | Exp13.2 supplies symbolic/algorithmic baselines, but not neural baselines. | Exp13.2 and manuscript-level | `docs/manuscript/BASELINE_REQUIREMENTS.md`; `docs/experiments/exp13_2_summary.md`; `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md` | Explicit decision: controlled symbolic/mechanistic benchmark paper now, or neural-baseline expansion before stronger ML submission. |

## P0 - Required Before Manuscript Submission

| TODO | Reason | Related experiment | Source path | Target output |
|---|---|---|---|---|
| Add seed-level confidence intervals and effect sizes. | Many claims cite aggregate means without manuscript-grade uncertainty. | Exp11-Exp14 | `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`; `scripts/compute_seed_metric_summary.py` | Human-reviewed CI/effect-size tables tied to explicit claim groupings. |
| Create final reproducible paper figures. | Current figure plan cites generated analysis plots, not final panel scripts. | Exp11-Exp14, Exp13.2 if retained | `docs/manuscript/FIGURE_PLAN.md`; `docs/source_data/SOURCE_DATA_MANIFEST.csv` | Figure scripts plus source-data manifests for every retained panel. |
| Verify manuscript-critical run commands on a fresh checkout. | Commands were inspected or documented, not freshly rerun in this cleanup pass. | Exp11-Exp14, Exp13.2 if cited | `docs/repo_audit/REPRODUCIBILITY_AUDIT.md` | Command log with pass/fail, runtime, hardware, and expected outputs. |
| Import novelty/prior-art assessment as a local artifact. | C12 and related-work framing depend on prior-art positioning and a missing thread-referenced artifact. | Manuscript-level | local verification pending for `Pasted text.txt`; `docs/manuscript/BASELINE_REQUIREMENTS.md` | Future `docs/manuscript/NOVELTY_ASSESSMENT_IMPORTED.md` or equivalent cited artifact. |
| Fix holdout metrics if retaining Exp13 holdout claims centrally. | Exp13 route-table/generalization claims need seen/unseen/all metric cleanup. | Exp13 or successor analysis | `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv` | Split metrics such as `route_table_accuracy_seen`, `route_table_accuracy_unseen`, and matching composition splits. |
| Audit/rerun Exp13.1 lesion diagnostic before citing positive lesion evidence. | Targeted critical-edge lesions were less damaging than random count-matched lesions. | Exp13.1 | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_lesion_metrics.csv`; `docs/threads/experiment13_1_analysis_digest.md` | Corrected lesion diagnostic or explicit decision not to cite lesion evidence. |
| Add license and citation metadata. | The repo currently lacks `LICENSE` and `CITATION.cff`; reuse and citation terms are unclear. | Repository-level | `README.md`; `docs/synthesis/PUBLICATION_READINESS.md` | Human-chosen license and citation metadata. |

## P1 - Strongly Recommended

| TODO | Reason | Related experiment | Source path | Target output |
|---|---|---|---|---|
| Add stochastic context corruption beyond wrong-world injection if generic robustness is claimed. | Current context corruption evidence supports identity/selection sensitivity, not generic stochastic robustness. | Exp13.1 or successor | `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_context_corruption.csv` | Stochastic corruption table with top-1 world selection, margins, and composition. |
| Refine consolidation analysis beyond accuracy rescue. | Exp13.1 did not show constrained-budget accuracy rescue from consolidation strength. | Exp13.1 or successor | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv` | Margin/robustness summaries or a caveated decision to keep consolidation supplementary. |
| Fit capacity laws only if C6/C7 become central quantitative claims. | Exp13 shows observed degradation curves but no fitted capacity model. | Exp13/Exp13.1 | `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | Capacity-law summaries and final figure panel if retained. |
| Upgrade local-vs-global comparison. | The current Exp13 comparison is docs-only and aggregate-level. | Exp13/Exp13.1 | `docs/experiments/exp13_local_vs_global_budget_comparison.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv` | Paired seed-level local-vs-global table with confidence intervals. |
| Maintain artifact and evidence indexes as outputs change. | Manuscript claims must remain traceable to source paths. | All future runs | `docs/repo_audit/ARTIFACT_INDEX.csv`; `docs/experiments/EXPERIMENT_ARTIFACTS_INDEX.csv` | Updated indexes after any new run or source-data import. |

## P2 - Future Work

| TODO | Reason | Related experiment | Source path | Target output |
|---|---|---|---|---|
| Richer latent-world inference. | Exp14 covers symbolic transition-cue selection but not raw sensory or learned perceptual context discovery. | Future successor | `docs/manuscript/LIMITATIONS_AND_THREATS.md`; `docs/threads/experiment14_analysis_digest.md` | New experiment directory under `experiments/` only if the manuscript needs a stronger non-symbolic bridge. |
| Richer non-symbolic tasks. | Move beyond synthetic symbolic route memory. | Future | `docs/threads/experiment12to13_export.md` | Applied bridge experiment, not claimed by current C11. |
| Biological mapping expansion. | Keep biological claims disciplined while exploring inspiration. | Future | `docs/theory/BIOLOGICAL_FRAMING.md` | Theory note or discussion section with citations. |

## Completed Repository-Readiness Work

| Completed item | Result | Source path |
|---|---|---|
| Path verifier and CI workflow. | Active documentation paths can be checked locally and in GitHub Actions. | `scripts/verify_doc_source_paths.py`; `.github/workflows/verify-doc-paths.yml` |
| Exp13.1 publication-hardening import. | Exp13.1 artifacts are documented with caveats; lesion diagnostic remains non-positive. | `docs/experiments/exp13_1_summary.md`; `docs/repo_audit/EXP13_1_ANALYSIS_IMPORT_REPORT.md` |
| Exp13.2 symbolic/algorithmic baseline import. | Exp13.2 artifacts are documented as partial baseline coverage; oracle context-gated lookup matches CIRM on clean supplied-context route memory. | `docs/experiments/exp13_2_summary.md`; `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`; `docs/threads/experiment13_2_analysis_digest.md` |
| Exp14 latent-context digest import. | Exp14 full, validation, and smoke runs are documented; C13 is added as promising symbolic transition-cue context-selection evidence. | `docs/experiments/exp14_summary.md`; `docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md`; `docs/threads/experiment14_analysis_digest.md` |
