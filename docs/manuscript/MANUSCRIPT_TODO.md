# Manuscript TODO

Purpose: Maintain a conservative work queue for turning this repository into a manuscript-grade research artifact.

## Current Next Operational Priority

Move from post-Exp15 / post-Manuscript-V2 documentation alignment into **Analysis Pass 15A: retained-claim and statistical hardening**.

Exp13.2 is now treated as an imported symbolic/algorithmic baseline suite, Exp14 is treated as imported symbolic transition-cue context-selection evidence, Exp15 is treated as imported minimal neural comparator evidence, and `docs/manuscript/draft/MANUSCRIPT_V2.md` has been captured.

Claim: The repository has a conservative V2 manuscript draft and a post-Exp15 claim-narrowing layer, but it is not submission-ready.

Evidence: Exp11, Exp12, Exp13, Exp13.1, Exp13.2, Exp14, and Exp15 now have local artifacts and imported summaries. Exp13.2 partially satisfies symbolic/algorithmic baseline coverage, Exp14 partially reduces the oracle-context-label limitation, Exp15 adds minimal neural comparator evidence, and V2 Table 4 captures the Exp15 hard-slice comparator.

Caveat: The manuscript still needs retained main-claim selection, manuscript-grade uncertainty/effect-size tables, human-reviewed final figures/tables, prior-art/novelty import, fresh command verification, and license/citation metadata. Exp15 neural coverage is fixed-profile and non-exhaustive; optional memory-augmented neural baselines remain a venue/reviewer decision.

Source path: `docs/manuscript/draft/MANUSCRIPT_V2.md`; `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`; `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`; `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`; `docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md`; `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`.

## Step 4 Manuscript Asset Pipeline Status

Claim -> A reproducible candidate manuscript asset pipeline now exists for the frozen first-manuscript claim set.

Evidence -> `python scripts/manuscript_assets/build_manuscript_assets.py` generates candidate Figures 1-5, source-data CSVs, claim/run-integrity/statistical tables, `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`, and `docs/repo_audit/MANUSCRIPT_ASSET_GENERATION_REPORT.md`. Exp15 Table 4 has also been generated as a source-data-backed V2 comparator table.

Caveat -> These are generated candidate manuscript assets, not human-approved final journal figures or final captions. Exp14 placement remains main-vs-supplement unresolved, Exp13.2 remains symbolic/algorithmic baseline evidence only, Exp15 is a minimal fixed-profile neural comparator, and prior-art/optional neural-baseline decisions remain open.

Source path: `scripts/manuscript_assets/build_manuscript_assets.py`; `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`; `docs/repo_audit/MANUSCRIPT_ASSET_GENERATION_REPORT.md`; `docs/manuscript/tables/table_04_exp15_neural_comparator.md`.

## P0 - Current Analysis Pass 15A

| TODO | Reason | Related experiment | Source path | Target output |
|---|---|---|---|---|
| Decide retained main claims after V2 and post-Exp15 narrowing. | V2 exists, but final statistical/source-data hardening needs a precise retained claim set. | Manuscript-level | `docs/manuscript/draft/MANUSCRIPT_V2.md`; `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/manuscript/finalization/NEXT_STEP_PROMPT.md` | Retained main-claim list with claim ID, manuscript role, source CSVs, and caveats. |
| Map retained claims to exact source CSVs. | Statistical hardening cannot proceed from prose alone. | Exp11-Exp15 | `docs/source_data/SOURCE_DATA_MANIFEST.csv`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv` | Claim-to-source table distinguishing seed-level raw metrics, aggregate summaries, and missing source-data mirrors. |
| Update manuscript-grade uncertainty/effect-size readiness. | Many claims cite aggregate means without final CI/effect-size review. | Exp11-Exp15 | `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`; `scripts/compute_seed_metric_summary.py`; `docs/manuscript/tables/table_03_statistical_summary.md` | Updated Table 3 and readiness CSV, or explicit gaps where statistics cannot be computed yet. |
| Decide final figure/table set. | Generated candidate assets exist, but final main-vs-supplement and caption decisions remain open. | Exp11-Exp15 | `docs/manuscript/FIGURE_PLAN.md`; `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`; `docs/manuscript/tables/table_04_exp15_neural_comparator.md` | Final figure/table decision list with remaining source-data/script gaps. |

## P0 - Required Before Manuscript Submission

| TODO | Reason | Related experiment | Source path | Target output |
|---|---|---|---|---|
| Add seed-level confidence intervals and effect sizes. | Many claims cite aggregate means without manuscript-grade uncertainty. | Exp11-Exp15 | `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`; `scripts/compute_seed_metric_summary.py` | Human-reviewed CI/effect-size tables tied to explicit claim groupings. |
| Human-review generated candidate figures and captions. | Step 4 generated reproducible candidate figures/source data, but final manuscript readiness still requires caption review, panel review, and journal formatting. | Exp11-Exp15 | `scripts/manuscript_assets/build_manuscript_assets.py`; `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`; `docs/manuscript/FIGURE_PLAN.md`; `docs/manuscript/tables/table_04_exp15_neural_comparator.md` | Final captions, approved main-vs-supplement placement, and any journal-specific formatting changes. |
| Verify manuscript-critical run commands on a fresh checkout. | Commands were inspected or documented, not freshly rerun in this cleanup pass. | Exp11-Exp15 | `docs/repo_audit/REPRODUCIBILITY_AUDIT.md` | Command log with pass/fail, runtime, hardware, and expected outputs. |
| Import novelty/prior-art assessment as a local artifact. | C12 and related-work framing depend on prior-art positioning and a missing thread-referenced artifact. | Manuscript-level | local verification pending for `Pasted text.txt`; `docs/manuscript/BASELINE_REQUIREMENTS.md` | Future `docs/manuscript/NOVELTY_ASSESSMENT_IMPORTED.md` or equivalent cited artifact. |
| Fix holdout metrics if retaining Exp13 holdout claims centrally. | Exp13 route-table/generalization claims need seen/unseen/all metric cleanup. | Exp13 or successor analysis | `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv` | Split metrics such as `route_table_accuracy_seen`, `route_table_accuracy_unseen`, and matching composition splits. |
| Audit/rerun Exp13.1 lesion diagnostic before citing positive lesion evidence. | Targeted critical-edge lesions were less damaging than random count-matched lesions. | Exp13.1 | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_lesion_metrics.csv`; `docs/threads/experiment13_1_analysis_digest.md` | Corrected lesion diagnostic or explicit decision not to cite lesion evidence. |
| Audit Exp15 replay variant before citing it. | The replay transition MLP collapsed in the hard slice, but the digest marks this surprising enough to require implementation/training-regime audit. | Exp15 | `docs/threads/experiment15_analysis_digest.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv` | Implementation/training-regime audit or explicit decision not to cite replay as scientific evidence. |
| Decide optional memory-augmented neural baseline. | Exp15 intentionally omitted neural key-value/memory-augmented lookup for scope control. | Exp15 or successor | `experiments/experiment15_neural_baseline_comparator/README.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_config.json` | Venue/reviewer decision on whether to create a successor experiment. |
| Add license and citation metadata. | The repo currently lacks `LICENSE` and `CITATION.cff`; reuse and citation terms are unclear. | Repository-level | `README.md`; `docs/synthesis/PUBLICATION_READINESS.md` | Human-chosen license and citation metadata. |

## P1 - Strongly Recommended

| TODO | Reason | Related experiment | Source path | Target output |
|---|---|---|---|---|
| Add stochastic context corruption beyond wrong-world injection if generic robustness is claimed. | Current context corruption evidence supports identity/selection sensitivity, not generic stochastic robustness. | Exp13.1 or successor | `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_context_corruption.csv` | Stochastic corruption table with top-1 world selection, margins, and composition. |
| Refine consolidation analysis beyond accuracy rescue. | Exp13.1 did not show constrained-budget accuracy rescue from consolidation strength. | Exp13.1 or successor | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv` | Margin/robustness summaries or a caveated decision to keep consolidation supplementary. |
| Fit capacity laws only if C6/C7 become central quantitative claims. | Exp13 shows observed degradation curves but no fitted capacity model. | Exp13/Exp13.1 | `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | Capacity-law summaries and final figure panel if retained. |
| Upgrade local-vs-global comparison. | The current Exp13 comparison is docs-only and aggregate-level. | Exp13/Exp13.1 | `docs/experiments/exp13_local_vs_global_budget_comparison.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv` | Paired seed-level local-vs-global table with confidence intervals. |
| Maintain artifact and evidence indexes as outputs change. | Manuscript claims must remain traceable to source paths. | All future runs | `docs/repo_audit/ARTIFACT_INDEX.csv`; `docs/experiments/EXPERIMENT_ARTIFACTS_INDEX.csv` | Updated indexes after any new run or source-data import. |
| Keep broad neural-superiority claims out of the manuscript. | Exp15 shows a conventional context-conditioned transition MLP solves the clean symbolic benchmark. | Exp15 and manuscript-level | `docs/threads/experiment15_analysis_digest.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv` | Mechanism/decomposition framing rather than broad ML superiority language. |

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
| Exp15 neural baseline comparator import. | Exp15 full run digest and local artifacts are imported; neural baseline comparator is completed as minimal fixed-profile evidence, with manifest/SQLite and replay caveats. | `docs/threads/experiment15_analysis_digest.md`; `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/validation_report.md` |
| Manuscript V2 capture. | V2 manuscript draft exists with conservative post-Exp15 posture. | `docs/manuscript/draft/MANUSCRIPT_V2.md` |
| Exp15 Table 4 capture. | Compact source-data-backed V2 neural comparator table exists. | `docs/manuscript/tables/table_04_exp15_neural_comparator.md`; `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv` |
