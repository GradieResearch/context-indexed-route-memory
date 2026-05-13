# Manuscript V3 Drafting Report

Date: 2026-05-13

Branch: `draft-manuscript-v3`

Primary output: `docs/manuscript/draft/MANUSCRIPT_V3.md`

## 1. Source Files Used

The V3 draft was written from V2 and the current claim-hardening/reproducibility package:

- `docs/manuscript/draft/MANUSCRIPT_V2.md`
- `docs/manuscript/MANUSCRIPT_REPRODUCIBILITY_MAP.md`
- `docs/manuscript/source_data/manuscript_claim_artifact_map.csv`
- `docs/manuscript/source_data/reproducibility_claim_summary.csv`
- `docs/manuscript/source_data/seed_level_core_claim_metrics.csv`
- `docs/manuscript/tables/table_reproducibility_claim_summary.md`
- `docs/repo_audit/CLAIM_SCOPED_REPRODUCIBILITY_SUMMARY_REPORT.md`
- `docs/repo_audit/MANUSCRIPT_REPRODUCIBILITY_PROTOCOL.md`
- `docs/repo_audit/MANUSCRIPT_REPRODUCIBILITY_REPORT.md`
- `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`
- `docs/manuscript/tables/table_03_compact_final_safe.md`
- `docs/manuscript/source_data/table_03_compact_final_safe.csv`
- `docs/manuscript/tables/table_04_exp15_neural_comparator.md`
- `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`
- `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`
- `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/MANUSCRIPT_SPINE.md`
- `docs/manuscript/SOURCE_OF_TRUTH.md`

## 2. What V3 Changed Relative To V2

V3 removes V2's internal draft-status and repository-audit voice and rewrites the manuscript as a conventional, review-facing paper draft. The structure is now title, abstract, introduction, background, benchmark setup, model/method, experiments, results, reproducibility/evidence traceability, limitations, discussion, and conclusion.

V3 keeps V2's title, citation-placeholder style, compact Table 3 descriptive posture, and Table 4 neural-comparator caveats. It compresses submission-readiness material into a short reproducibility section instead of presenting the manuscript as a repo audit.

No source data, experiment outputs, historical runs, figures, or manuscript assets were regenerated or edited.

## 3. Retained Claims Included

Claim -> C1 structural route storage remains benchmark/model-family-specific.
Evidence -> V3 cites the compact Table 3 descriptive slice in which the full model reaches route-table/composition accuracy 1.000 and no-structural-plasticity falls to route_table_accuracy 0.0286 and composition_accuracy 0.0317.
Caveat -> Not universalized to all neural route-memory systems; Exp15 transition MLP variants solve the clean hard slice.
Source path -> `docs/manuscript/tables/table_03_compact_final_safe.md`; `docs/manuscript/source_data/table_03_compact_final_safe.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_ablation_metrics.csv`

Claim -> C2 context/world indexing remains conflict-specific.
Evidence -> V3 discusses first-step/full-route disambiguation and the no-context suffix caveat, including Table 4's no-context transition MLP pattern.
Caveat -> Does not claim context is required for every suffix transition.
Source path -> `docs/manuscript/source_data/reproducibility_claim_summary.csv`; `docs/manuscript/tables/table_04_exp15_neural_comparator.md`; `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`

Claim -> C3 recurrent execution is required for multi-step composition in the tested contracts.
Evidence -> V3 uses the compact Table 3 no-recurrence result: route_table_accuracy 1.000 with composition_accuracy 0.0401.
Caveat -> Recurrence itself is not presented as novel.
Source path -> `docs/manuscript/tables/table_03_compact_final_safe.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_ablation_metrics.csv`

Claim -> C4 route-table storage, endpoint memorization, and composition are separable.
Evidence -> V3 combines the no-recurrence separation with Table 4 endpoint-vs-suffix/transition results.
Caveat -> This is a decomposition claim, not an architecture ranking.
Source path -> `docs/manuscript/source_data/reproducibility_claim_summary.csv`; `docs/manuscript/tables/table_04_exp15_neural_comparator.md`

Claim -> C5 clean supplied-context ceiling behavior through tested world counts.
Evidence -> V3 reports route-table and composition accuracy 1.000 across the mirrored clean supplied-context grid.
Caveat -> Ceiling-limited and supplied-context only; no capacity law.
Source path -> `docs/manuscript/tables/table_03_compact_final_safe.md`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`

Claim -> C6 finite structural budget produces observed degradation.
Evidence -> V3 reports the descriptive budget-ratio curve from 0.276 at 0.25 to 1.000 at exact/surplus budget.
Caveat -> Descriptive observed degradation only; no fitted law; C7 not promoted.
Source path -> `docs/manuscript/tables/table_03_compact_final_safe.md`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`

Claim -> C13 symbolic transition-cue context selection.
Evidence -> V3 reports CIRM latent selector world-selection/seen-composition values of 1.000 at corruption 0.00/0.10, 0.999 at 0.25, and 0.942 at 0.50.
Caveat -> Symbolic transition-cue selection only; not raw sensory latent-world discovery.
Source path -> `docs/manuscript/tables/table_03_compact_final_safe.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`

Claim -> C12 baseline/comparator coverage is present but non-exhaustive.
Evidence -> V3 includes symbolic/algorithmic baselines and the fixed-profile Table 4 neural comparator, including the fact that context-conditioned and world-head transition MLP variants solve the clean hard slice.
Caveat -> No broad neural superiority claim; Exp15 replay collapse remains non-claim pending audit.
Source path -> `docs/manuscript/tables/table_04_exp15_neural_comparator.md`; `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`

## 4. Boundary, Supplement, And Non-Claims Kept Excluded

Boundary/supplement only:

- C7 local-versus-global pressure.
- C8 consolidation/stability-plasticity discussion.
- C10 context/cue corruption sensitivity.
- C11 continuous/noisy bridge.

Non-claims or excluded central claims:

- C9 seen/unseen primitive boundary until metric cleanup exists.
- Exp13.1 positive lesion evidence.
- Exp15 replay collapse.
- Broad CIRM-over-neural claims.
- Raw sensory latent-world discovery.
- Biological validation.
- Solved continual learning.
- Broad architecture superiority.

## 5. Unresolved Submission Blockers

- Citation metadata and bibliography convention remain citation-finalization pending.
- Final venue choice remains open.
- Final figure/table placement and caption review remain open.
- Compact Table 3 is descriptive; final effect-size and comparison-family choices remain conservative unless separately approved.
- Optional broader neural or memory-augmented/key-value baselines remain venue-dependent.
- License and `CITATION.cff` remain human decisions before public release/submission.
- Exp15 replay and Exp13.1 lesion diagnostics remain audit items if anyone wants to interpret them scientifically.

## 6. Validation Commands Run

Command -> `python scripts/verify_doc_source_paths.py`
Result -> PASS. The final run scanned 153 files, reported 0 missing active paths, and skipped only planned/future or explicitly local-verification-pending paths.
Caveat -> Existing planned/local-pending references elsewhere in the repository remain skipped by design.

Command -> `python scripts/reproduce_manuscript.py --profile validate-artifacts`
Result -> PASS. The validate-artifacts profile completed successfully.
Caveat -> This validates committed artifacts and schemas; it does not rerun expensive experiments.

Command -> `rg --files scripts | rg "(lint|check|verify|validate|markdown|md|doc)"`
Result -> Only the existing source-path verifier and manuscript-assets README were discovered as lightweight markdown/source-check candidates.
Caveat -> No separate markdown lint command was found.

## 7. Claim Posture

V3 does not widen any claim. It narrows the presentation relative to V2 by removing repo-audit/status-note framing, keeping Table 3 descriptive, keeping Table 4 fixed-profile and non-exhaustive, and explicitly excluding boundary/supplement/non-claim evidence from the central manuscript claims.

No expensive experiments were rerun. No historical outputs were overwritten intentionally. The `validate-artifacts` command refreshed its own generated reproducibility report files during execution; those generated report changes were restored so the working tree remains scoped to the requested V3 manuscript and V3 drafting report.
