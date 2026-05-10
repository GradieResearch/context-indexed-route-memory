# Publication Readiness

## Summary Judgment

Status: post-Analysis-Pass-15A, post-citation-ledger/status pass, post-human-decision capture, post-direct Section 2.7 manuscript patch, and post-compact Table 3 split. The manuscript is not submission-ready; the next blocker is documentation/path verification plus caption/manuscript alignment for the compact Table 3 path.

The current internal spine remains defensible but narrow: in a controlled symbolic route-memory benchmark, context-indexed structural plasticity stores incompatible local transition systems, recurrent execution composes stored one-step transitions into multi-step routes, Exp13.2 supplies symbolic/algorithmic baseline coverage, Exp14 shows that the active symbolic world can be selected from partial symbolic transition cues, Exp15 supplies a minimal neural comparator, and Analysis Pass 15A records the retained claim set and source-CSV mapping.

The repository has moved beyond the raw citation/prior-art audit, human-decision, direct Section 2.7 patch, and current-pass Table 3 cleanup stages. `docs/manuscript/REFERENCES.md` remains the checked venue-neutral citation ledger. `docs/manuscript/closest_prior_art_table.md` remains the closest-prior-art companion artifact. `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md` records the human decisions for citation/export convention, closest-prior-art placement, and figure/table placement. `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md` now records the Table 3 outcome: use a compact final-safe descriptive main-text Table 3 and retain the full generated statistical map as candidate/supplementary support.

Current retained V2 posture:

- Main scientific spine: C1, C2, C3, C4, C5, C6, and C13.
- Discussion/table baseline claim: C12.
- Boundary or supplement only: C7, C8, C10, and C11.
- Out of the main claim set or non-claims: C9, Exp13.1 positive lesion evidence, Exp15 replay collapse, broad CIRM-over-neural claims, raw sensory latent-world discovery, and biological validation.

Current placement posture:

- Figures 1-3: main.
- Figure 4: supplement by default unless the finite-budget story is intentionally emphasized.
- Figure 5: main-narrow because Exp14 reduces the oracle-context criticism.
- Table 3: compact final-safe descriptive main-text table at `docs/manuscript/tables/table_03_compact_final_safe.md`, with source data at `docs/manuscript/source_data/table_03_compact_final_safe.csv`.
- Detailed generated statistical map: retained as candidate/supplementary support at `docs/manuscript/tables/table_03_statistical_summary.md` and `.csv`.
- Table 4: compact main-text Exp15 neural comparator table.

## Manuscript Asset Pipeline Status

Status: reproducible candidate assets generated, with human placement decisions and the compact Table 3 split recorded, but not final submission-ready figures/captions.

Claim -> The first-manuscript claim freeze has a local reproducible asset pipeline for candidate figures, source data, and source tables. The compact Table 3 split prevents the generated detailed statistical map from being treated as final inferential statistics.

Evidence -> `python scripts/manuscript_assets/build_manuscript_assets.py` generates candidate Figures 1-5, source-data CSVs, manuscript tables, `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`, and `docs/repo_audit/MANUSCRIPT_ASSET_GENERATION_REPORT.md`. Exp15 Table 4 is present as a compact source-data-backed V2 comparator table. Compact Table 3 is now present as a descriptive source-data-backed main-text table.

Caveat -> Human review is still required for caption wording and journal formatting. Compact Table 3 is descriptive and final-safe for the current manuscript pass; it does not claim final inferential effect sizes or approved comparison-family statistics.

## Strongest Evidence

- Exp12 clean scaling reaches ceiling across the mirrored supplied-context grid used for Figure 3. Source path: `docs/manuscript/source_data/figure_03_capacity_scaling.csv`.
- Exp13 finite structural budget shows observed degradation and recovery across explicit budget ratios. Source path: `docs/manuscript/source_data/figure_04_finite_structural_budget_local_global.csv`.
- Exp13.1 publication-hardening ablations separate full-model, no-context-binding, no-recurrence-at-eval, and no-structural-plasticity behavior. Source path: `docs/manuscript/tables/table_03_statistical_summary.csv`.
- Exp14 symbolic transition-cue selection reaches ceiling or near-ceiling in the selected hard cue slices and degrades under high cue corruption while the oracle context-gated table remains an upper bound. Source path: `docs/manuscript/source_data/figure_05_symbolic_context_selection.csv`; `docs/threads/experiment14_analysis_digest.md`.
- Exp15 minimal neural comparator narrows broad claims and supports Table 4 caveats. Source path: `docs/manuscript/tables/table_04_exp15_neural_comparator.md`; `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`.
- Checked citation ledger, closest-prior-art table, and Section 2.7 prose patch preserve prior-art hygiene without inventing final venue formatting. Source path: `docs/manuscript/REFERENCES.md`; `docs/manuscript/closest_prior_art_table.md`; `docs/manuscript/draft/MANUSCRIPT_V2.md`.

## Weakest Evidence / Remaining Reviewer Risks

- Neural baseline coverage remains minimal and non-exhaustive. Exp15 is fixed-profile and omits broader memory-augmented/key-value neural baselines.
- Final target-venue bibliography format remains undecided. `docs/manuscript/REFERENCES.md` is a venue-neutral ledger, not final journal formatting.
- Inferential effect-size claims are still not finalized. Compact Table 3 is descriptive; the generated detailed statistical map remains candidate/supplementary because it still includes ambiguous/repeated-looking rows, aggregate-normal intervals, and `nan` effect-size cells.
- C7 local-vs-global pressure remains boundary/supplement only until paired seed-level local/global grouping exists.
- Exp13.1 targeted lesion evidence should not be used as positive mechanism evidence.
- Primitive holdout needs metric cleanup if retained centrally.
- Exp14 is symbolic transition-cue inference, not raw sensory latent-world discovery.

## Required Before Manuscript Draft Finalization

- Run `python scripts/verify_doc_source_paths.py` after the compact Table 3 split.
- Polish manuscript and caption references so compact Table 3 is cited as descriptive and the generated detailed map remains candidate/supplementary.
- Human-review generated Figures 1-5 and Tables 1-4 for caption wording, caveats, and venue-specific formatting.
- Keep Figure 4 supplement-default unless the finite-budget story is intentionally emphasized.
- Keep Figure 5 main-narrow unless a later venue decision requires supplement relocation.
- Keep Table 4 as compact main-text unless a later venue decision requires supplement relocation.

## Required Before Submission

- Apply final target-venue citation/export convention to the manuscript without inventing metadata.
- Add inferential seed-level confidence intervals/effect sizes only if the manuscript needs approved comparison-family claims beyond compact descriptive Table 3.
- Verify manuscript-critical smoke/validation/full commands and document runtimes/hardware.
- Add human-chosen `LICENSE` and `CITATION.cff`.
- Fix holdout metrics if C9 becomes central.
- Audit/rerun Exp13.1 lesion diagnostic only if positive lesion evidence will be cited.
- Keep biological, novelty, continual-learning, perception, and generalization claims narrow.

## Operational Readiness

Claim: The repository is more navigable after the post-citation-ledger, human-decision, Section 2.7, and compact Table 3 cleanup passes, but remains scientifically not submission-ready.

Evidence: The manuscript TODO, finalization checklist, statistical-readiness table, checked references ledger, closest-prior-art table, human decision status, Section 2.7 prose patch, Table 3 grouping review, compact Table 3, and compact Table 3 source data describe the current state.

Caveat: This is documentation readiness, not new scientific evidence.

Source path: `docs/manuscript/MANUSCRIPT_TODO.md`; `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`; `docs/manuscript/REFERENCES.md`; `docs/manuscript/closest_prior_art_table.md`; `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md`; `docs/manuscript/finalization/SECTION_2_7_PROSE_PATCH.md`; `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md`; `docs/manuscript/tables/table_03_compact_final_safe.md`; `docs/manuscript/source_data/table_03_compact_final_safe.csv`.
