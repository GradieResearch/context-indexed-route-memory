# Manuscript Finalization Checklist

Purpose: working checklist for moving the Context-Indexed Route Memory manuscript from V2 draft capture to a submission-ready package after Exp15 import, human placement decisions, Section 2.7 closest-prior-art integration, the compact-safe Table 3 split, and the first verification/alignment status capture.

Use this as the operational tracker. Check items only when the repository contains the corresponding artifact or the manuscript has been explicitly updated.

Legend:

- `[ ]` not started
- `[~]` in progress / partial
- `[x]` complete
- `[!]` blocked or requires human decision

---

## Phase 0 - Finalization Control Docs

- [x] Create `docs/manuscript/finalization/`.
- [x] Add finalization plan and checklist.
- [x] Replace the old Exp15 implementation prompt with post-Exp15 finalization prompts.
- [x] Update `docs/manuscript/SOURCE_OF_TRUTH.md` and finalization indexes for post-Exp15/post-V2 document authority.
- [x] Add `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md` for Analysis Pass 15A.
- [x] Add `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md` for post-15A citation/prior-art hardening.
- [x] Add `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md` for generated Figure 1-5 / Table 1-4 human review.
- [x] Add `docs/manuscript/REFERENCES.md` as checked venue-neutral citation ledger.
- [x] Add `docs/manuscript/closest_prior_art_table.md` as closest-prior-art companion artifact.
- [x] Add citation-ledger, human-decision, and Section 2.7 finalization status artifacts.
- [x] Add `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md` and update it with the compact Table 3 split outcome.
- [x] Add `docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md` to capture the remaining compact Table 3 verification/alignment blocker.

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
- [x] Decide Exp15 placement for V2: compact main-text Table 4.
- [x] Decide Exp14 placement: Figure 5 remains main-narrow because it reduces the oracle-context criticism.

---

## Phase 3 - Prior-Art And Novelty Positioning

- [x] Retire the missing novelty/prior-art source artifact as an active blocker unless it is later recovered.
- [x] Verify major V1/V2 citation placeholder families against checked metadata in a venue-neutral ledger.
- [x] Decide citation/export convention for now: keep `docs/manuscript/REFERENCES.md` as the venue-neutral ledger until a target venue/convention is chosen.
- [x] Do not create BibTeX, CSL JSON, numbered references, or target-journal formatting yet.
- [x] Separate prior-art families clearly: continual learning, memory-augmented neural systems, fast weights/differentiable plasticity, mixture-of-experts/modular routing, latent-cause/context inference, neural algorithmic reasoning, compositional generalization, symbolic graph/path lookup, hippocampal/CLS inspiration, and minimal neural comparator posture.
- [x] Ensure novelty is framed at the control-doc level as the controlled route-memory decomposition and evidence map.
- [x] Decide closest-prior-art placement: convert `docs/manuscript/closest_prior_art_table.md` into prose in Section 2.7 and retain the table as a companion artifact.
- [x] Apply closest-prior-art prose directly to `docs/manuscript/draft/MANUSCRIPT_V2.md`.

---

## Phase 4 - Statistical Hardening

- [x] Decide retained main claims after Exp15 and V2 capture.
- [x] For each retained main claim, identify exact source CSV(s).
- [x] Update `docs/source_data/STATISTICAL_REPORTING_READINESS.csv` for retained, boundary, supplement, blocked, and non-claim evidence.
- [x] Ensure C9 remains out of the main claim set unless seen/unseen metrics are cleaned.
- [x] Avoid fitted capacity-law language unless capacity-law fitting is added.
- [x] Complete the current-pass Table 3 cleanup using Option B: compact final-safe descriptive main-text Table 3 plus retained detailed candidate/supplementary statistical map.
- [x] Add `docs/manuscript/tables/table_03_compact_final_safe.md`.
- [x] Add `docs/manuscript/source_data/table_03_compact_final_safe.csv`.
- [x] Preserve `docs/manuscript/tables/table_03_statistical_summary.md` and `.csv` as detailed candidate/supplementary statistical-map artifacts, not final main-text statistics.
- [~] Manuscript-grade seed-level summaries, 95% confidence intervals, and effect sizes remain available/partially mapped, but final inferential comparison families are still not claimed by compact Table 3.
- [~] Review effect-size grouping for Exp13.2, Exp14, and Exp15 only if the manuscript later needs inferential effect-size wording.

---

## Phase 5 - Final Figure, Table, And Source-Data Pipeline

- [x] Decide final figure/table placement posture for the current manuscript pass:
  - Figures 1-3: main.
  - Figure 4: supplement by default unless the finite-budget story is intentionally emphasized.
  - Figure 5: main-narrow.
  - Table 3: compact final-safe descriptive main-text table; detailed generated statistical map retained as candidate/supplementary support.
  - Table 4: compact main-text table.
- [~] Create final Figure 1 schematic or provide source instructions for human-drawn schematic. Candidate Figure 1 exists; final label/caption review remains.
- [~] Generate final Figure 2 core ablation script/source data. Candidate asset/source data exist; final row/caption review remains.
- [~] Generate final Figure 3 clean capacity/retention script/source data. Candidate asset/source data exist; final ceiling-limited caption review remains.
- [~] Keep Figure 4 as supplement-default unless the finite-budget story is intentionally emphasized.
- [~] Keep Figure 5 as main-narrow with symbolic transition-cue and oracle-upper-bound caveats.
- [x] Generate source-data-backed Exp15 neural comparator Table 4.
- [x] Add `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`.
- [x] Add `docs/manuscript/tables/table_04_exp15_neural_comparator.md`.
- [~] Add figure/table captions with explicit caveats. Caveats are identified in `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`; final caption prose remains a review task.

---

## Phase 6 - Manuscript Update

- [x] Update abstract after Exp15 and statistical hardening status.
- [x] Update introduction to reflect final claim posture.
- [~] Update related work with verified citations. `docs/manuscript/REFERENCES.md` verifies metadata, but final manuscript citation style/conversion remains pending until target venue selection.
- [x] Apply closest-prior-art Section 2.7 prose directly to the manuscript draft.
- [x] Update methods/problem setup with Exp15 neural baseline details if Exp15 is retained.
- [x] Update results with current candidate figures/tables.
- [x] Update discussion to reflect final limitations.
- [x] Ensure oracle context-gated table is described as an upper-bound comparator.
- [x] Ensure Exp14 is described as symbolic transition-cue context selection, not raw sensory latent-world discovery.
- [x] Ensure Exp15 is not overinterpreted as exhaustive neural benchmarking.
- [x] Ensure Exp15 replay collapse is not interpreted scientifically unless audited.
- [x] Ensure broad CIRM-over-neural-model claims are absent.
- [!] Patch stale `MANUSCRIPT_V2.md` Table 3 placeholder so main-text Table 3 cites `docs/manuscript/tables/table_03_compact_final_safe.md`, not `docs/manuscript/tables/table_03_statistical_summary.md`.
- [~] Keep caption/prose wording aligned so compact Table 3 is descriptive and the detailed statistical map remains candidate/supplementary.
- [ ] Remove or clearly mark all TODOs before submission.

---

## Phase 7 - Reproducibility And Repository Hygiene

- [ ] Fresh clone or clean-environment command verification.
- [x] Run documentation source-path verifier after Exp15 import.
- [x] Confirm all requested Exp15 artifacts exist locally.
- [ ] Confirm all manuscript-cited artifacts exist locally after final figure/table decisions.
- [!] Run `python scripts/verify_doc_source_paths.py` after the compact Table 3 split. Prior attempt could not run because the execution environment could not resolve `github.com` for a clean checkout; see `docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md`.
- [ ] Add runtime/hardware metadata standard to future experiment template or docs.
- [x] Document Exp15 runtime/hardware metadata and reconstructed-manifest caveat.
- [ ] Add `LICENSE` after human license choice.
- [ ] Add `CITATION.cff`.
- [~] Update README/current-status indexes after Exp13.2/Exp14/Exp15/V2/Table 3 compact split state is final.
- [ ] Add final reproducibility instructions.
- [ ] Decide whether to tag a release.
- [ ] Decide whether to archive on Zenodo after preprint/manuscript stabilization.

---

## Phase 8 - Optional Follow-Up Experiments Only If Needed

Do not start these by default. Revisit them only after human venue and reviewer-strategy decisions.

- [!] Optional neural-baseline successor - memory-augmented/key-value neural comparator, only if target venue or reviewers require broader neural coverage.
- [ ] Experiment 16 - Lesion Diagnostic Audit, only if positive lesion evidence is desired.
- [ ] Experiment 17 - Perceptual / Continuous Applied Bridge, only if applied bridge becomes central.
- [ ] Experiment 18 - Stochastic Context Corruption and Selection Margins, only if generic robustness is claimed.
- [ ] Experiment 19 - Consolidation Dose-Response Under Interference Pressure, only if consolidation becomes central.
- [ ] Experiment 20 or analysis-only pass - Seen-vs-Unseen Primitive Metric Cleanup, only if C9 becomes central.

---

## Current Recommended Next Checkbox

- [x] Apply `docs/manuscript/finalization/SECTION_2_7_PROSE_PATCH.md` directly to `docs/manuscript/draft/MANUSCRIPT_V2.md` without overwriting unrelated manuscript content.
- [x] Create a compact final-safe main-text Table 3 and move the full generated statistical map to candidate/supplementary status.
- [x] Record the current verification/alignment status in `docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md`.
- [ ] Patch the stale `docs/manuscript/draft/MANUSCRIPT_V2.md` Table 3 placeholder to cite compact Table 3 as the main-text path.
- [ ] Run `python scripts/verify_doc_source_paths.py` in a clean checkout or CI-capable environment after the manuscript placeholder patch.
- [ ] If the verifier passes, update this checklist, `docs/manuscript/MANUSCRIPT_TODO.md`, `docs/synthesis/PUBLICATION_READINESS.md`, and `docs/manuscript/finalization/NEXT_STEP_PROMPT.md` to the next blocker after Table 3 alignment.
