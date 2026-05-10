# Manuscript TODO

Purpose: Maintain a conservative work queue for turning this repository into a manuscript-grade research artifact.

## Current Next Operational Priority

Move from **human-decision capture and direct Section 2.7 manuscript patching** into **Table 3 statistical grouping cleanup**.

The repository is no longer waiting for the initial post-15A citation/prior-art audit, checked citation ledger, or human placement decisions. Those steps now exist as durable artifacts:

- `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md`
- `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`
- `docs/manuscript/REFERENCES.md`
- `docs/manuscript/closest_prior_art_table.md`
- `docs/manuscript/finalization/CITATION_PRIOR_ART_INSERTION_REPORT.md`
- `docs/manuscript/finalization/CITATION_LEDGER_INTEGRATION_STATUS.md`
- `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md`
- `docs/manuscript/finalization/SECTION_2_7_PROSE_PATCH.md`
- `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md`

Human decisions now recorded:

1. Citation/export convention: keep `docs/manuscript/REFERENCES.md` as the venue-neutral ledger until a target venue/convention is chosen.
2. Closest-prior-art placement: convert `docs/manuscript/closest_prior_art_table.md` into prose in Section 2.7 and retain the table as a companion artifact.
3. Figure/table placement: Figures 1-3 main; Figure 4 supplement-default unless the finite-budget story is emphasized; Figure 5 main-narrow; Table 3 candidate until grouping/effect-size review is complete; Table 4 compact main-text.

The current active work is therefore:

1. Regenerate or revise Table 3 with explicit grouping/slice columns, or create a compact final-safe main-text Table 3 and move the full statistical map to supplement.
2. Run `python scripts/verify_doc_source_paths.py` after table/statistical-doc updates and before readiness handoff.

Current retained V2 posture:

- Main scientific spine: C1, C2, C3, C4, C5, C6, and C13.
- Discussion/table baseline claim: C12.
- Boundary or supplement only: C7, C8, C10, and C11.
- Out of the main claim set or non-claims: C9, Exp13.1 positive lesion evidence, Exp15 replay collapse, broad CIRM-over-neural claims, raw sensory latent-world discovery, and biological validation.

Claim: The repository has a conservative V2 manuscript draft with Section 2.7 closest-prior-art prose applied directly, a post-Exp15 claim-narrowing layer, a retained-claim decision, candidate manuscript figures/tables, an updated statistical-readiness map, a checked citation ledger, a closest-prior-art companion table, recorded human integration decisions, and a started Table 3 grouping review, but it is not submission-ready.

Evidence: Exp11, Exp12, Exp13, Exp13.1, Exp13.2, Exp14, and Exp15 have local artifacts and imported summaries. Exp13.2 partially satisfies symbolic/algorithmic baseline coverage, Exp14 supports symbolic transition-cue context selection, Exp15 adds minimal fixed-profile neural comparator evidence, V2 Table 4 captures the Exp15 hard-slice comparator, `docs/manuscript/REFERENCES.md` verifies major placeholder-key metadata, `docs/manuscript/closest_prior_art_table.md` supplies the closest-prior-art structure, Section 2.7 of `docs/manuscript/draft/MANUSCRIPT_V2.md` now contains the closest-prior-art positioning prose, and `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md` records the initial Table 3 review.

Caveat: The manuscript still needs final related-work citation formatting after target venue selection, human-reviewed captions, final seed-level statistical grouping, fresh command verification, and license/citation metadata. Table 3 remains candidate-only until grouping/effect-size review is completed. Exp15 neural coverage is fixed-profile and non-exhaustive; optional memory-augmented neural baselines remain a venue/reviewer decision.

Source path: `docs/manuscript/draft/MANUSCRIPT_V2.md`; `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`; `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`; `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`; `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md`; `docs/manuscript/REFERENCES.md`; `docs/manuscript/closest_prior_art_table.md`; `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`; `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md`; `docs/manuscript/finalization/SECTION_2_7_PROSE_PATCH.md`; `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`; `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`; `docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md`; `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`.

## Step 4 Manuscript Asset Pipeline Status

Claim -> A reproducible candidate manuscript asset pipeline exists for the frozen first-manuscript claim set.

Evidence -> `python scripts/manuscript_assets/build_manuscript_assets.py` generates candidate Figures 1-5, source-data CSVs, claim/run-integrity/statistical tables, `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`, and `docs/repo_audit/MANUSCRIPT_ASSET_GENERATION_REPORT.md`. Exp15 Table 4 has also been generated as a source-data-backed V2 comparator table. `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md` records the required review for these assets and the human placement decision is now recorded.

Caveat -> These are generated candidate manuscript assets, not final journal figures or final captions. Table 3 remains candidate until grouping/effect-size review is completed. Exp15 is a minimal fixed-profile neural comparator, and optional neural-baseline decisions remain open.

Source path: `scripts/manuscript_assets/build_manuscript_assets.py`; `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`; `docs/repo_audit/MANUSCRIPT_ASSET_GENERATION_REPORT.md`; `docs/manuscript/tables/table_04_exp15_neural_comparator.md`; `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`; `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md`; `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md`.

## Completed Repository-Readiness Work

| Completed item | Result | Source path |
|---|---|---|
| Path verifier and CI workflow. | Active documentation paths can be checked locally and in GitHub Actions. | `scripts/verify_doc_source_paths.py`; `.github/workflows/verify-doc-paths.yml` |
| Exp13.1 publication-hardening import. | Exp13.1 artifacts are documented with caveats; lesion diagnostic remains non-positive. | `docs/experiments/exp13_1_summary.md`; `docs/repo_audit/EXP13_1_ANALYSIS_IMPORT_REPORT.md` |
| Exp13.2 symbolic/algorithmic baseline import. | Exp13.2 artifacts are documented as partial baseline coverage; oracle context-gated lookup matches CIRM on clean supplied-context route memory. | `docs/experiments/exp13_2_summary.md`; `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`; `docs/threads/experiment13_2_analysis_digest.md` |
| Exp14 latent-context digest import. | Exp14 full, validation, and smoke runs are documented; C13 is added as symbolic transition-cue context-selection evidence. | `docs/experiments/exp14_summary.md`; `docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md`; `docs/threads/experiment14_analysis_digest.md` |
| Exp15 neural baseline comparator import. | Exp15 full run digest and local artifacts are imported; neural baseline comparator is completed as minimal fixed-profile evidence, with manifest/SQLite and replay caveats. | `docs/threads/experiment15_analysis_digest.md`; `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/validation_report.md` |
| Manuscript V2 capture. | V2 manuscript draft exists with conservative post-Exp15 posture. | `docs/manuscript/draft/MANUSCRIPT_V2.md` |
| Exp15 Table 4 capture. | Compact source-data-backed V2 neural comparator table exists. | `docs/manuscript/tables/table_04_exp15_neural_comparator.md`; `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv` |
| Analysis Pass 15A retained-claim hardening. | Retained main claims and source CSVs are explicitly mapped; statistical-readiness tracker separates retained, boundary, supplement, blocked, and non-claim evidence. | `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv` |
| Post-15A citation/prior-art audit. | Citation placeholders were mapped to prior-art families; the missing novelty/prior-art artifact was not invented and was retired as the only path forward. | `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md`; `docs/manuscript/NOVELTY_POSITIONING.md` |
| Checked citation ledger. | Major placeholder-key metadata is checked in a venue-neutral reference ledger; no fake `.bib`/CSL export has been invented. | `docs/manuscript/REFERENCES.md`; `docs/manuscript/finalization/CITATION_PRIOR_ART_INSERTION_REPORT.md` |
| Closest-prior-art companion table. | Prior-art families are separated into inherited ideas, non-novel claims, and the manuscript's narrow contribution. | `docs/manuscript/closest_prior_art_table.md` |
| Section 2.7 closest-prior-art prose applied. | The manuscript draft now contains prose-level closest-prior-art positioning and no longer contains the old closest-prior-art TODO. | `docs/manuscript/draft/MANUSCRIPT_V2.md`; `docs/manuscript/finalization/SECTION_2_7_PROSE_PATCH.md`; `docs/manuscript/closest_prior_art_table.md` |
| Human decision integration status. | Citation/export convention, closest-prior-art placement, and figure/table placement are recorded. | `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md` |
| Table 3 grouping review started. | Table 3 is confirmed candidate-only until grouping/slice columns and final effect-size comparisons are reviewed. | `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md`; `docs/manuscript/tables/table_03_statistical_summary.md`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv` |

## P0 - Current Next Pass

| TODO | Reason | Source path | Target output |
|---|---|---|---|
| Regenerate or revise Table 3 with explicit grouping/slice columns. | Candidate Table 3 mixes descriptive rows, ceiling rows, aggregate intervals, and repeated-looking slices without enough final grouping metadata. | `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md`; `docs/manuscript/tables/table_03_statistical_summary.md`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv` | Final-safe Table 3 or a compact main-text table plus supplementary statistical map. |
| Run documentation source-path verifier before readiness handoff. | New finalization docs and any manuscript updates should not introduce broken active paths. | `scripts/verify_doc_source_paths.py` | Passing verifier output or exact failure report. |
| Decide whether target venue strategy requires a memory-augmented/key-value neural comparator. | Exp15 is intentionally minimal and fixed-profile; broader neural coverage is venue-dependent. | `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md`; `experiments/experiment15_neural_baseline_comparator/README.md` | Explicit venue/reviewer decision; do not start a new experiment by default. |

## P0 - Required Before Manuscript Submission

| TODO | Reason | Source path | Target output |
|---|---|---|---|
| Apply final citation/export convention after target venue selection. | Placeholder keys should be converted only after a convention is chosen. | `docs/manuscript/REFERENCES.md`; `docs/manuscript/draft/MANUSCRIPT_V2.md` | Chosen bibliography/citation format without invented metadata. |
| Finalize seed-level confidence intervals and effect sizes for retained claims. | Pass 15A mapped sources but did not certify every statistical comparison as final. | `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`; `docs/manuscript/tables/table_03_statistical_summary.md`; `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md`; `scripts/compute_seed_metric_summary.py` | Human-reviewed CI/effect-size tables tied to explicit claim groupings. |
| Human-review generated candidate figures and captions. | Generated assets are reproducible candidates, not final journal figures. | `scripts/manuscript_assets/build_manuscript_assets.py`; `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`; `docs/manuscript/FIGURE_PLAN.md`; `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md` | Final captions, approved placement, and journal-specific formatting changes. |
| Verify manuscript-critical run commands on a fresh checkout. | Commands were inspected/documented, not freshly rerun in this pass. | `docs/repo_audit/REPRODUCIBILITY_AUDIT.md` | Command log with pass/fail, runtime, hardware, and expected outputs. |
| Fix holdout metrics if retaining Exp13 holdout claims centrally. | C9 remains out of the main claim set until seen/unseen/all metric cleanup is done. | `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv` | Split metrics such as `route_table_accuracy_seen`, `route_table_accuracy_unseen`, and matching composition splits. |
| Audit/rerun Exp13.1 lesion diagnostic before citing positive lesion evidence. | Targeted critical-edge lesions were less damaging than random count-matched lesions. | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_lesion_metrics.csv`; `docs/threads/experiment13_1_analysis_digest.md` | Corrected lesion diagnostic or explicit decision not to cite lesion evidence. |
| Audit Exp15 replay variant before citing it. | Replay collapse is a non-claim pending implementation/training-regime audit. | `docs/threads/experiment15_analysis_digest.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv` | Implementation/training-regime audit or explicit decision not to cite replay scientifically. |
| Add license and citation metadata. | Reuse and citation terms are unclear. | `README.md`; `docs/synthesis/PUBLICATION_READINESS.md` | Human-chosen `LICENSE` and `CITATION.cff`. |

## P1 - Strongly Recommended

| TODO | Reason | Source path | Target output |
|---|---|---|---|
| Add stochastic context corruption only if generic robustness is claimed. | Current evidence supports identity/selection sensitivity, not generic stochastic robustness. | `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_context_corruption.csv` | Stochastic corruption table with top-1 world selection, margins, and composition. |
| Refine consolidation analysis only if consolidation becomes central. | Current evidence supports bias/tradeoff, not necessity. | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv` | Margin/robustness summaries or a caveated decision to keep consolidation supplementary. |
| Fit capacity laws only if C6/C7 become stronger quantitative claims. | Current evidence supports observed degradation, not a fitted capacity law. | `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | Capacity-law summaries and final figure panel if retained. |
| Upgrade local-vs-global comparison if C7 is elevated. | C7 is boundary/supplement only after Pass 15A and the Table 3 review. | `docs/experiments/exp13_local_vs_global_budget_comparison.md`; `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv` | Paired seed-level local-vs-global table with confidence intervals. |
| Maintain artifact and evidence indexes as outputs change. | Manuscript claims must remain traceable to source paths. | `docs/repo_audit/ARTIFACT_INDEX.csv`; `docs/experiments/EXPERIMENT_ARTIFACTS_INDEX.csv` | Updated indexes after any new run or source-data import. |

## P2 - Future Work

| TODO | Reason | Source path | Target output |
|---|---|---|---|
| Richer latent-world inference. | Exp14 covers symbolic transition-cue selection but not raw sensory or learned perceptual context discovery. | `docs/manuscript/LIMITATIONS_AND_THREATS.md`; `docs/threads/experiment14_analysis_digest.md` | New experiment directory only if the manuscript needs a stronger non-symbolic bridge. |
| Richer non-symbolic tasks. | Move beyond synthetic symbolic route memory. | `docs/threads/experiment12to13_export.md` | Applied bridge experiment, not claimed by current C11. |
| Biological mapping expansion. | Keep biological claims disciplined while exploring inspiration. | `docs/theory/BIOLOGICAL_FRAMING.md` | Theory note or discussion section with citations. |
