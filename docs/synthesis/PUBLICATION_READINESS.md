# Publication Readiness

## Summary Judgment

Status: post-Analysis-Pass-15A, post-citation-ledger/status pass, post-human-decision capture, post-direct Section 2.7 manuscript patch, and Table 3 grouping-review start. The manuscript is not submission-ready; the next blocker is finalizing or regenerating Table 3 grouping.

The current internal spine is defensible but narrow: in a controlled symbolic route-memory benchmark, context-indexed structural plasticity stores incompatible local transition systems, recurrent execution composes stored one-step transitions into multi-step routes, Exp13.2 supplies symbolic/algorithmic baseline coverage, Exp14 shows that the active symbolic world can be selected from partial transition cues, Exp15 supplies a minimal neural comparator, and Analysis Pass 15A records the retained claim set and source-CSV mapping. Exp11, Exp12, Exp13, Exp13.1, Exp13.2, Exp14, and Exp15 support this story with important caveats.

The repository has now moved beyond the raw citation/prior-art audit, human-decision, and direct Section 2.7 patch stages. `docs/manuscript/REFERENCES.md` is the checked venue-neutral citation ledger, `docs/manuscript/closest_prior_art_table.md` is the checked closest-prior-art companion artifact, and `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md` records the human decisions for citation/export convention, closest-prior-art placement, and figure/table placement. `docs/manuscript/finalization/SECTION_2_7_PROSE_PATCH.md` has been applied to manuscript Section 2.7. `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md` starts the Table 3 grouping/effect-size review and confirms that Table 3 remains candidate-only until grouping/slice columns and final effect-size comparisons are reviewed.

Current retained V2 posture:

- Main scientific spine: C1, C2, C3, C4, C5, C6, and C13.
- Discussion/table baseline claim: C12.
- Boundary or supplement only: C7, C8, C10, and C11.
- Out of the main claim set or non-claims: C9, Exp13.1 positive lesion evidence, Exp15 replay collapse, broad CIRM-over-neural claims, raw sensory latent-world discovery, and biological validation.

Current placement posture:

- Figures 1-3: main.
- Figure 4: supplement by default unless the finite-budget story is intentionally emphasized.
- Figure 5: main-narrow because Exp14 reduces the oracle-context criticism.
- Table 3: candidate until grouping/effect-size review is complete.
- Table 4: compact main-text Exp15 neural comparator table.

Exp13.2 should be treated as imported symbolic/algorithmic baseline evidence, and Exp15 should be treated as imported minimal neural comparator evidence. Together they partially satisfy C12 for a controlled symbolic/mechanistic manuscript, but Exp15 remains fixed-profile and non-exhaustive. The checked citation ledger improves prior-art hygiene, but it does not choose a final target-venue bibliography format.

Source path: `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`; `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`; `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/manuscript/LIMITATIONS_AND_THREATS.md`; `docs/manuscript/REFERENCES.md`; `docs/manuscript/closest_prior_art_table.md`; `docs/manuscript/finalization/CITATION_LEDGER_INTEGRATION_STATUS.md`; `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md`; `docs/manuscript/finalization/SECTION_2_7_PROSE_PATCH.md`; `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md`; `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`; `docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md`; `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`.

## Manuscript Asset Pipeline Status

Status: reproducible candidate assets generated, with human placement decisions recorded, but not final submission-ready figures.

Claim -> The first-manuscript claim freeze has a local reproducible asset pipeline for candidate figures, source data, and source tables. Analysis Pass 15A keeps these as candidate/human-review assets rather than automatically final figures.

Evidence -> `python scripts/manuscript_assets/build_manuscript_assets.py` generates candidate Figures 1-5, source-data CSVs under `docs/manuscript/source_data/`, manuscript tables under `docs/manuscript/tables/`, `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`, and `docs/repo_audit/MANUSCRIPT_ASSET_GENERATION_REPORT.md`. Exp15 Table 4 is present as a compact source-data-backed V2 comparator table. Human placement decisions are now recorded in `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md` and summarized in `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`.

Caveat -> Human review is still required for caption wording and journal formatting. Table 3 remains candidate until grouping/effect-size review is completed. The generated assets do not remove the non-exhaustive neural-baseline caveat.

Source path: `scripts/manuscript_assets/build_manuscript_assets.py`; `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`; `docs/repo_audit/MANUSCRIPT_ASSET_GENERATION_REPORT.md`; `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`; `docs/manuscript/tables/table_04_exp15_neural_comparator.md`; `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md`; `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md`.

## Strongest Evidence

- Exp11 A/B context-separated retention and ablations. Source path: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `docs/threads/experiment11_export`.
- Exp12 clean scaling to 32 worlds with no-recurrence/no-world-context/no-structural-plasticity contrasts. Source path: `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `docs/threads/experiment12to13_export.md`.
- Exp13 finite-capacity breaking and no-recurrence route-table/composition dissociation. Source path: `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`.
- Exp13.1 publication-hardening ablations: no-recurrence-at-eval preserves route-table accuracy while composition collapses, no-structural-plasticity fails, no-context-binding fails, and local budget pressure is much more damaging than global budget pressure. Source path: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv`.
- Exp13.2 symbolic/algorithmic baseline suite: oracle context-gated lookup matches CIRM on the clean supplied-context benchmark, no-context lookup fails conflict-sensitive probes, no-recurrence separates route-table storage from composition, endpoint memorization fails suffix composition, and hash/superposition-style controls expose context compression/collision behavior. Source path: `docs/experiments/exp13_2_summary.md`; `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`.
- Exp14 latent symbolic context selection: full run validation passed, clean hard-slice CIRM selection/composition reaches 1.0000, and cue corruption/cue-count sweeps quantify the symbolic selection boundary. Source path: `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_report.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `docs/threads/experiment14_analysis_digest.md`.
- Exp15 minimal neural comparator: full run validation passed; context-conditioned transition MLP and world-head transition MLP variants solve all hard-slice metrics at 1.0000, endpoint GRU/Transformer variants expose endpoint-vs-composition dissociations, and no-context transition MLP fails first-step/full-route disambiguation while solving suffix composition. Source path: `docs/threads/experiment15_analysis_digest.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/validation_report.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`.
- Checked citation ledger, closest-prior-art table, and Section 2.7 prose patch: major placeholder-key metadata is recorded without inventing fake bibliography output, prior-art families are separated into inherited mechanisms/non-novel claims/narrow contribution, and the prose replacement has been applied directly to the manuscript draft. Source path: `docs/manuscript/REFERENCES.md`; `docs/manuscript/closest_prior_art_table.md`; `docs/manuscript/draft/MANUSCRIPT_V2.md`; `docs/manuscript/finalization/CITATION_PRIOR_ART_INSERTION_REPORT.md`; `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md`; `docs/manuscript/finalization/SECTION_2_7_PROSE_PATCH.md`.

## Weakest Evidence

- Neural baseline coverage is minimal and non-exhaustive. Exp15 used fixed small models/hyperparameters, omitted memory-augmented/key-value neural baselines, omitted route length 16 from the default full profile, and includes manifest/SQLite provenance caveats. Source path: `docs/threads/experiment15_analysis_digest.md`; `experiments/experiment15_neural_baseline_comparator/README.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/run_manifest.json`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_config.json`.
- Final target-venue bibliography format remains undecided. `docs/manuscript/REFERENCES.md` is a checked venue-neutral ledger, not a final journal-formatted bibliography. Source path: `docs/manuscript/REFERENCES.md`; `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md`.
- Table 3 remains candidate-only. The started review identifies ambiguous grouping/slice metadata, repeated-looking Exp14 rows, `nan` effect sizes, and missing paired seed-level local/global comparison for C7. Source path: `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md`; `docs/manuscript/tables/table_03_statistical_summary.md`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`.
- Consolidation as a stability-plasticity bias is preliminary because Exp13 validation shows only a small finite-pressure delta and Exp13.1 did not show constrained-budget accuracy rescue. Source path: `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv`.
- Exp13.1 targeted lesion evidence failed the expected pattern and should not be used as positive mechanism evidence. Source path: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_lesion_metrics.csv`.
- Primitive holdout needs metric cleanup if retained centrally. Source path: `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv`.
- Continuous/noisy input is only a front-end bridge, not end-to-end perception. Source path: `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv`.
- Exp14 is symbolic transition-cue inference, not raw sensory latent-world discovery; the oracle context-gated table remains an upper bound. Source path: `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `docs/threads/experiment14_analysis_digest.md`.

## Required Before Manuscript Draft Finalization

- Regenerate or revise Table 3 with explicit grouping/slice columns, or create a compact final-safe main-text Table 3 and move the full statistical map to supplement.
- Human-review generated Figures 1-5 and Tables 1-4 for caption wording, caveats, and venue-specific formatting.
- Keep Figure 4 supplement-default unless the finite-budget story is intentionally emphasized.
- Keep Figure 5 main-narrow unless a later venue decision requires supplement relocation.
- Keep Table 4 as compact main-text unless a later venue decision requires supplement relocation.
- Refresh `docs/manuscript/MANUSCRIPT_SPINE.md` from the post-human-decision/post-Table-3-review state if the manuscript structure changes.

## Required Before Submission

- Apply final target-venue citation/export convention to the manuscript without inventing metadata.
- Finalize seed-level confidence intervals and effect sizes for retained core claims.
- Human-review and finalize the generated candidate paper figures from the reproducible manuscript asset script.
- Add source-data/final figures for Exp14 if retained.
- Keep Exp15 as compact Table 4 unless a human/venue decision moves it to supplement.
- Verify manuscript-critical smoke/validation/full commands and document runtimes/hardware.
- Add human-chosen `LICENSE` and `CITATION.cff`.
- Fix holdout metrics if C9 becomes central.
- Audit/rerun Exp13.1 lesion diagnostic only if positive lesion evidence will be cited.
- Keep biological, novelty, continual-learning, perception, and generalization claims narrow.
- Run `python scripts/verify_doc_source_paths.py` before readiness handoff.

## Operational Readiness

Claim: The repository is more navigable after the post-citation-ledger and human-decision cleanup, but remains scientifically not submission-ready.

Evidence: The README/docs index, source-of-truth note, post-Exp15 addendum, retained-claims hardening document, manuscript TODO, figure plan, reproducibility audit, source-data manifest, statistical-readiness table, checked references ledger, closest-prior-art table, human decision status, Section 2.7 prose patch, and Table 3 grouping review describe the post-Exp13.2/post-Exp14/post-Exp15/post-15A/post-citation-ledger/post-human-decision state.

Caveat: This is documentation readiness, not new scientific evidence.

Source path: `README.md`; `docs/README.md`; `docs/manuscript/SOURCE_OF_TRUTH.md`; `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`; `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`; `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`; `docs/manuscript/MANUSCRIPT_TODO.md`; `docs/manuscript/REFERENCES.md`; `docs/manuscript/closest_prior_art_table.md`; `docs/manuscript/finalization/CITATION_PRIOR_ART_INSERTION_REPORT.md`; `docs/manuscript/finalization/CITATION_LEDGER_INTEGRATION_STATUS.md`; `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md`; `docs/manuscript/finalization/SECTION_2_7_PROSE_PATCH.md`; `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md`; `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`; `docs/source_data/SOURCE_DATA_MANIFEST.csv`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`.

## Reviewer-Risk Matrix

| Reviewer criticism | Why they might say it | Current answer | Required fix |
|---|---|---|---|
| Internal ablations are not enough. | Most core claims compare model variants and symbolic controls. | Exp13.2 adds symbolic/algorithmic baselines, and Exp15 adds a minimal neural comparator. | Decide target venue and add memory-augmented or broader neural baselines if needed. |
| Neural comparator is too small. | Exp15 is fixed-profile, with small models and no architecture search. | Agreed; Exp15 is a minimal comparator, not a neural benchmark suite. | Keep claims narrow, or create a successor neural-baseline experiment if the venue requires it. |
| Oracle context-gated lookup solves clean supplied-context benchmark. | Exp13.2 shows oracle context-gated lookup matches CIRM in the clean supplied-context setting. | Agreed; raw clean supplied-context accuracy is not the novelty claim. | Frame contribution around mechanism decomposition, capacity/boundary mapping, and Exp14 symbolic cue-selected context. |
| Related work / citation format is not final. | The repo has a checked ledger but not a target-venue bibliography style. | Agreed; `REFERENCES.md` is a venue-neutral metadata ledger. | Choose target venue/convention later and convert without inventing metadata. |
| Closest-prior-art comparison is narrow and must remain traceable. | The source-backed table exists separately and Section 2.7 now contains the prose positioning. | Agreed; human chose prose placement, the direct manuscript patch is complete, and the companion table remains the source artifact. | Preserve narrow wording and keep `docs/manuscript/closest_prior_art_table.md` available for reviewer traceability. |
| Table 3 statistics are not final. | Candidate table lacks enough explicit grouping/slice metadata for every final claim comparison. | Agreed; Table 3 review has started and marks it candidate-only. | Regenerate or revise Table 3 with explicit grouping columns and final-status flags. |
| Generalization is overstated. | Exp13 unseen primitive transitions fail. | The manuscript should claim composition over stored primitives, not unseen transition inference. | Fix seen/unseen/all holdout metrics and wording if C9 is retained centrally. |
| Consolidation claim is weak. | Easy regimes do not need consolidation; Exp13 delta is small. | Current claim is bias/tradeoff, not necessity. | Keep supplementary or add dose-response/robustness evidence. |
| Context noise result is artificial. | Exp13 adversarial corruption, Exp13.1 wrong-world injection, and Exp14 cue corruption are synthetic selection tests. | It is useful as a selection-boundary test. | Add stochastic graded context corruption only if generic robustness is claimed. |
| Targeted lesion claim fails. | Exp13.1 targeted lesion is less damaging than random count-matched lesion. | Do not use the lesion diagnostic as positive mechanism evidence. | Audit critical-edge selection and rerun if lesion evidence is needed. |
| Biological framing overreaches. | The task is symbolic and synthetic. | Frame as computational inspiration only. | Tighten related work and limitations language. |
| Applied bridge is not applied learning. | Continuous front-end is decoded/noisy, not learned perception. | Keep it preliminary or supplementary. | Build a real visual-state route-memory bridge later. |
| Latent-context claim overreaches. | Exp14 uses symbolic transition cues and synthetic corruption. | C13 is limited to symbolic cue selection; oracle context gating remains an upper bound. | Keep wording narrow and add final source-data-backed figures only if retained. |
