# Manuscript Finalization Checklist

Purpose: working checklist for moving the Context-Indexed Route Memory manuscript from V2 draft capture to a submission-ready package after Exp15 import.

Use this as the operational tracker. Check items only when the repository contains the corresponding artifact or the manuscript has been explicitly updated.

Legend:

- `[ ]` not started
- `[~]` in progress / partial
- `[x]` complete
- `[!]` blocked or requires human decision

---

## Phase 0 - Finalization Control Docs

- [x] Create `docs/manuscript/finalization/`.
- [x] Add finalization plan.
- [x] Add finalization checklist.
- [x] Replace the old Exp15 implementation prompt with post-Exp15 finalization prompts.
- [x] Update next-step prompt through Analysis Pass 15A.
- [x] Link finalization folder from `docs/README.md`.
- [x] Update `docs/manuscript/SOURCE_OF_TRUTH.md` for post-Exp15/post-V2 document authority.
- [x] Update `docs/manuscript/finalization/README.md` for current finalization posture.
- [x] Add `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md` for Analysis Pass 15A.
- [x] Add `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md` for post-15A citation/prior-art hardening.
- [x] Add `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md` for generated Figure 1-5 / Table 1-4 human review.
- [~] Update next-step prompt for the next post-15A pass after citation/prior-art and figure/table review artifacts are merged.

---

## Phase 1 - Experiment 15 Neural Comparator

- [x] Create and implement `experiments/experiment15_neural_baseline_comparator/`.
- [x] Implement required fixed-profile neural variants: GRU endpoint, GRU rollout, small Transformer, transition MLP, replay-trained transition MLP, and parameter/world-head-isolated variant.
- [x] Add deterministic seed handling, runtime/hardware metadata, validation/full profiles, start scripts, analysis script, and validation script.
- [~] Run smoke profile locally. Full/validation artifacts are present; no separate smoke artifact was verified in the Exp15 import pass.
- [x] Run validation/full profile locally for `exp15_full_20260508_092811`.
- [x] Confirm required variants, context/no-context configs, suffix-vs-seen probes, finite metrics, and validation report are present.
- [x] Preserve full run artifacts under `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/`.
- [x] Generate Exp15 summary, seed-metric, effect-size, runtime, validation, and analysis-plot artifacts.
- [x] Import Exp15 docs and caveats into experiment, manuscript, synthesis, and repo-audit docs.
- [x] Create post-Exp15 claim freeze addendum at `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`.

---

## Phase 2 - Manuscript V2 Capture And Post-Exp15 Claim Freeze

- [x] Capture the discussion-drafted/post-Exp15 manuscript as `docs/manuscript/draft/MANUSCRIPT_V2.md`.
- [x] Preserve the V2 posture: controlled symbolic/mechanistic benchmark and evidence map, not broad neural superiority.
- [x] Record Exp15 as narrowing C1, C2, C4, and C12.
- [x] Record Exp14 as symbolic transition-cue context selection, not raw latent-world discovery.
- [x] Record Exp15 replay collapse as non-claim pending audit.
- [x] Decide Exp15 placement for V2: compact main-text Table 4, movable to supplement by later human/venue decision.
- [~] Decide Exp14 placement: retained as main-narrow Figure 5 for V2 hardening, with supplement relocation left as a later venue/human decision.

---

## Phase 3 - Prior-Art And Novelty Positioning

- [~] Locate/import or recreate the missing novelty/prior-art source artifact if still relevant. `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md` records that the original artifact remains absent and should not be invented; the audit is now the source-backed replacement path unless the original artifact is later recovered.
- [~] Verify all V1/V2 citation placeholders against real BibTeX metadata. `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md` maps the major V2 placeholder families to candidate real metadata, but a final bibliography file has not been added.
- [ ] Add or update bibliography file if repository conventions include one.
- [~] Separate prior-art families clearly: continual learning, memory-augmented neural networks, fast weights/differentiable plasticity, mixture-of-experts/modular routing, latent-cause/context inference, neural algorithmic reasoning, and compositional generalization. The audit identifies these families; manuscript prose still needs final citation insertion.
- [~] Ensure the manuscript does not claim novelty for context gating, recurrence, replay, task isolation, or memory augmentation in isolation. Current V2 posture and audit both state this boundary; final prose review remains.
- [~] Ensure novelty is framed as the controlled route-memory decomposition and evidence map. Current V2 posture and audit both state this boundary; final prose review remains.

---

## Phase 4 - Statistical Hardening

- [x] Decide retained main claims after Exp15 and V2 capture.
- [x] For each retained main claim, identify exact source CSV(s).
- [x] Update `docs/source_data/STATISTICAL_REPORTING_READINESS.csv` for retained, boundary, supplement, blocked, and non-claim evidence.
- [x] Ensure C9 remains out of the main claim set unless seen/unseen metrics are cleaned.
- [x] Avoid fitted capacity-law language unless capacity-law fitting is added.
- [~] Generate manuscript-grade seed-level summaries. Retained-claim source paths are mapped, but exact seed-level grouping still needs human review before final citation.
- [~] Generate 95% confidence intervals. Candidate Table 3 exists, but final CI grouping remains pending.
- [~] Generate effect sizes for direct comparisons. Exp13.2, Exp14, and Exp15 effect-size artifacts exist, but retained comparison grouping still needs review.
- [~] Review effect-size grouping for Exp13.2.
- [~] Review effect-size grouping for Exp14.
- [~] Review effect-size grouping for Exp15.
- [~] Update `docs/manuscript/tables/table_03_statistical_summary.md`. Current Table 3 is a generated candidate table and should not be treated as final until grouping is reviewed.

---

## Phase 5 - Final Figure, Table, And Source-Data Pipeline

- [~] Decide final main figure/table set. Pass 15A retains Figures 1-3, Figure 4 as C6 main-narrow with C7 boundary handling, Figure 5 as main-narrow movable to supplement, and Table 4 as compact V2 neural comparator table.
- [~] Create final Figure 1 schematic or provide source instructions for human-drawn schematic. Candidate Figure 1 exists; final label/caption review remains.
- [~] Generate final Figure 2 core ablation script/source data. Candidate asset/source data exist; final row/caption review remains.
- [~] Generate final Figure 3 clean capacity/retention script/source data. Candidate asset/source data exist; final ceiling-limited caption review remains.
- [~] Generate final Figure 4 finite-budget/local-vs-global script/source data, if retained. Candidate asset/source data exist; C7 local/global remains boundary-only pending paired seed-level analysis.
- [~] Generate final Figure 5 Exp14 symbolic context-selection script/source data, if retained. Candidate asset/source data exist; final main-vs-supplement and oracle-upper-bound caption review remain.
- [x] Add `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md` with placement, claim role, caption caveat, source-data status, and unresolved human decision for Figures 1-5 and Tables 1-4.
- [x] Decide Exp15 placement for V2: compact main-text Table 4, with supplement relocation left as a later venue/human decision.
- [x] Generate source-data-backed Exp15 neural comparator table, if retained.
- [x] Add `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`, if Exp15 Table 4 is retained.
- [x] Add `docs/manuscript/tables/table_04_exp15_neural_comparator.md`, if Exp15 Table 4 is retained.
- [~] Add source-data files for every final panel/table. Candidate source data exists for generated Figures 1-5 and Table 4; final human-approved panel/table set still needs confirmation.
- [x] Update `docs/source_data/SOURCE_DATA_MANIFEST.csv` for Exp15 Table 4.
- [x] Ensure candidate analysis plots are not cited as final manuscript figures unless regenerated by final figure scripts. Pass 15A explicitly keeps Exp15 plots as analysis artifacts only.
- [~] Add figure/table captions with explicit caveats. Caveats are identified in `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`; final caption prose remains a human-review task.

---

## Phase 6 - Manuscript Update

- [x] Update abstract after Exp15 and statistical hardening status.
- [x] Update introduction to reflect final claim posture.
- [ ] Update related work with verified citations.
- [x] Update methods/problem setup with Exp15 neural baseline details if Exp15 is retained.
- [x] Update results with current candidate figures/tables.
- [x] Update discussion to reflect final limitations.
- [x] Update limitations section to distinguish closed risks from retained scope boundaries.
- [x] Update non-claims.
- [x] Ensure oracle context-gated table is described as an upper-bound comparator.
- [x] Ensure Exp14 is described as symbolic transition-cue context selection, not raw latent-world discovery.
- [x] Ensure Exp15 is not overinterpreted as exhaustive neural benchmarking.
- [x] Ensure Exp15 replay collapse is not interpreted scientifically unless audited.
- [x] Ensure broad CIRM-over-neural-model claims are absent.
- [ ] Remove or clearly mark all TODOs before submission.

---

## Phase 7 - Reproducibility And Repository Hygiene

- [ ] Fresh clone or clean-environment command verification.
- [x] Run documentation source-path verifier after Exp15 import.
- [x] Confirm all requested Exp15 artifacts exist locally.
- [ ] Confirm all manuscript-cited artifacts exist locally after final figure/table decisions.
- [ ] Add runtime/hardware metadata standard to future experiment template or docs.
- [x] Document Exp15 runtime/hardware metadata and reconstructed-manifest caveat.
- [ ] Add `LICENSE` after human license choice.
- [ ] Add `CITATION.cff`.
- [~] Update README/current-status indexes after Exp13.2/Exp14/Exp15/V2 state is final. `docs/README.md` and finalization/source-of-truth indexes are aligned; root README status still needs separate review if desired.
- [ ] Add final reproducibility instructions.
- [ ] Decide whether to tag a release.
- [ ] Decide whether to archive on Zenodo after preprint/manuscript stabilization.

---

## Phase 8 - Optional Follow-Up Experiments Only If Needed

Do not start these by default. Revisit them only after post-Exp15 claim and figure/table decisions.

- [!] Optional neural-baseline successor - memory-augmented/key-value neural comparator, only if target venue or reviewers require broader neural coverage.
- [ ] Experiment 16 - Lesion Diagnostic Audit, only if positive lesion evidence is desired.
- [ ] Experiment 17 - Perceptual / Continuous Applied Bridge, only if applied bridge becomes central.
- [ ] Experiment 18 - Stochastic Context Corruption and Selection Margins, only if generic robustness is claimed.
- [ ] Experiment 19 - Consolidation Dose-Response Under Interference Pressure, only if consolidation becomes central.
- [ ] Experiment 20 or analysis-only pass - Seen-vs-Unseen Primitive Metric Cleanup, only if C9 becomes central.

---

## Current Recommended Next Checkbox

- [ ] Convert `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md` into final manuscript citation work: add or update bibliography entries, replace/verify manuscript placeholders, and add a closest-prior-art table if retained.
- [ ] Perform human review of `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`, especially Figure 4 main-vs-supplement, Figure 5 main-vs-supplement, Table 3 grouping, and Table 4 main-vs-supplement placement.
