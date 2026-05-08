# Manuscript Finalization Checklist

Purpose: working checklist for moving the Context-Indexed Route Memory manuscript from V1 draft to submission-ready package.

Use this as the operational tracker. Check items only when the repository contains the corresponding artifact or the manuscript has been explicitly updated.

Legend:

- `[ ]` not started
- `[~]` in progress / partial
- `[x]` complete
- `[!]` blocked or requires human decision

---

## Phase 0 — Finalization control docs

- [x] Create `docs/manuscript/finalization/`.
- [x] Add finalization plan.
- [x] Add finalization checklist.
- [x] Add next-step prompt for Experiment 15.
- [ ] Link finalization folder from `docs/README.md` or manuscript index if desired.

---

## Phase 1 — Experiment 15 neural comparator

### Design and implementation

- [ ] Create planned directory `experiments/experiment15_neural_baseline_comparator/`.
- [ ] Add experiment README with purpose, hypotheses, variants, metrics, and expected outputs.
- [ ] Implement shared dataset/probe generation aligned to Exp13.2/Exp14 route-memory metrics.
- [ ] Implement GRU/LSTM endpoint baseline.
- [ ] Implement GRU/LSTM rollout baseline.
- [ ] Implement small Transformer sequence baseline.
- [ ] Implement neural one-step transition model rolled out recurrently.
- [ ] Implement replay-trained neural baseline.
- [ ] Implement parameter-isolated neural baseline.
- [ ] Decide whether to include optional neural key-value / memory-augmented lookup baseline.
- [ ] Add runtime/hardware manifest capture.
- [ ] Add progress logging with seed, variant, slice, elapsed time, and estimated remaining work.
- [ ] Add deterministic seed handling.
- [ ] Add smoke, validation, and full profiles.
- [ ] Add `start_exp15_validation.ps1`.
- [ ] Add `start_exp15_full.ps1`.
- [ ] Add analysis script.
- [ ] Add validation script.

### Validation

- [ ] Run smoke profile locally.
- [ ] Run validation profile locally.
- [ ] Confirm all required variants execute.
- [ ] Confirm no data leakage in suffix-route probes.
- [ ] Confirm no-context/context variants differ only by context input.
- [ ] Confirm replay/parameter-isolation configs are explicitly recorded.
- [ ] Confirm all metrics are in valid ranges.
- [ ] Confirm validation report reports PASS/WARN/FAIL counts.
- [ ] Fix implementation issues found by validation.

### Full run and analysis

- [ ] Run full profile locally.
- [ ] Preserve full run artifacts under `analysis/exp15_full_<timestamp>/`.
- [ ] Generate `exp15_summary.csv`.
- [ ] Generate `exp15_seed_metrics.csv`.
- [ ] Generate `exp15_effect_sizes.csv`.
- [ ] Generate `exp15_model_runtime.csv`.
- [ ] Generate route-length scaling plot.
- [ ] Generate world-count scaling plot.
- [ ] Generate seen-vs-suffix composition plot.
- [ ] Generate context-conflict accuracy plot.
- [ ] Generate retention-after-sequential-worlds plot.
- [ ] Generate validation report.
- [ ] Review whether Exp15 changes the manuscript claim posture.

### Import

- [ ] Add planned post-run summary `docs/experiments/exp15_summary.md` after results exist.
- [ ] Add planned post-run digest `docs/threads/experiment15_analysis_digest.md` after results exist.
- [ ] Update `docs/experiments/EXPERIMENT_REGISTRY.md`.
- [ ] Update `docs/manuscript/BASELINE_REQUIREMENTS.md`.
- [ ] Update `docs/manuscript/CLAIMS_AND_EVIDENCE.md`.
- [ ] Update `docs/manuscript/LIMITATIONS_AND_THREATS.md`.
- [ ] Update `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md` or create a post-Exp15 claim freeze.
- [ ] Update `docs/synthesis/PUBLICATION_READINESS.md`.
- [ ] Update `docs/synthesis/NEXT_EXPERIMENTS.md`.

---

## Phase 2 — Prior-art and novelty positioning

- [ ] Locate/import the missing novelty/prior-art source artifact referenced in baseline docs, if still relevant.
- [ ] Verify all V1 citation placeholders against real BibTeX metadata.
- [ ] Add or update bibliography file if repository conventions include one.
- [ ] Separate prior-art families clearly:
  - [ ] continual learning;
  - [ ] memory-augmented neural networks;
  - [ ] fast weights / differentiable plasticity;
  - [ ] mixture-of-experts / modular routing;
  - [ ] latent-cause / context inference;
  - [ ] neural algorithmic reasoning;
  - [ ] compositional generalization.
- [ ] Ensure the manuscript does not claim novelty for context gating, recurrence, replay, task isolation, or memory augmentation in isolation.
- [ ] Ensure novelty is framed as the controlled route-memory decomposition and evidence map.

---

## Phase 3 — Statistical hardening

- [ ] Decide retained main claims after Exp15.
- [ ] For each retained main claim, identify exact source CSV(s).
- [ ] Generate manuscript-grade seed-level summaries.
- [ ] Generate 95% confidence intervals.
- [ ] Generate effect sizes for direct comparisons.
- [ ] Review effect-size grouping for Exp13.2.
- [ ] Review effect-size grouping for Exp14.
- [ ] Review effect-size grouping for Exp15.
- [ ] Update `docs/manuscript/tables/table_03_statistical_summary.md`.
- [ ] Update `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`.
- [ ] Ensure C9 remains out of the main claim set unless seen/unseen metrics are cleaned.
- [ ] Avoid fitted capacity-law language unless capacity-law fitting is added.

---

## Phase 4 — Final figure and source-data pipeline

- [ ] Decide final main figure set.
- [ ] Create final Figure 1 schematic or provide source instructions for human-drawn schematic.
- [ ] Generate final Figure 2 core ablation script/source data.
- [ ] Generate final Figure 3 clean capacity/retention script/source data.
- [ ] Generate final Figure 4 finite-budget/local-vs-global script/source data, if retained.
- [ ] Generate final Figure 5 Exp14 symbolic context-selection script/source data.
- [ ] Generate final Exp15 neural comparator figure/table, if retained.
- [ ] Add source-data files for every final panel.
- [ ] Update `docs/source_data/SOURCE_DATA_MANIFEST.csv`.
- [ ] Ensure candidate analysis plots are not cited as final manuscript figures unless regenerated by final figure scripts.
- [ ] Add figure captions with explicit caveats.

---

## Phase 5 — Manuscript update

- [ ] Update abstract after Exp15 and statistical hardening.
- [ ] Update introduction to reflect final claim posture.
- [ ] Update related work with verified citations.
- [ ] Update methods with Exp15 neural baseline details.
- [ ] Update results with final figures/tables.
- [ ] Update discussion to reflect final limitations.
- [ ] Update limitations section to distinguish closed risks from retained scope boundaries.
- [ ] Update non-claims.
- [ ] Ensure oracle context-gated table is described as an upper-bound comparator.
- [ ] Ensure Exp14 is described as symbolic transition-cue context selection, not raw latent-world discovery.
- [ ] Ensure Exp15 is not overinterpreted as exhaustive neural benchmarking.
- [ ] Remove or clearly mark all TODOs before submission.

---

## Phase 6 — Reproducibility and repository hygiene

- [ ] Fresh clone or clean-environment command verification.
- [ ] Run documentation source-path verifier.
- [ ] Confirm all manuscript-cited artifacts exist locally.
- [ ] Add runtime/hardware metadata standard to future experiment template or docs.
- [ ] Ensure Exp15 manifests include runtime/hardware metadata.
- [ ] Add `LICENSE` after human license choice.
- [ ] Add `CITATION.cff`.
- [ ] Update README current-status section after Exp13.2/Exp14/Exp15 state is final.
- [ ] Add final reproducibility instructions.
- [ ] Decide whether to tag a release.
- [ ] Decide whether to archive on Zenodo after preprint/manuscript stabilization.

---

## Phase 7 — Optional follow-up experiments only if needed

Do not start these until Exp15 has been analyzed and the manuscript claim posture has been updated.

- [ ] Experiment 16 — Lesion Diagnostic Audit, only if positive lesion evidence is desired.
- [ ] Experiment 17 — Perceptual / Continuous Applied Bridge, only if applied bridge becomes central.
- [ ] Experiment 18 — Stochastic Context Corruption and Selection Margins, only if generic robustness is claimed.
- [ ] Experiment 19 — Consolidation Dose-Response Under Interference Pressure, only if consolidation becomes central.
- [ ] Experiment 20 or analysis-only pass — Seen-vs-Unseen Primitive Metric Cleanup, only if C9 becomes central.

---

## Current recommended next checkbox

- [ ] Create and implement planned directory `experiments/experiment15_neural_baseline_comparator/` using `docs/manuscript/finalization/NEXT_STEP_PROMPT.md`.
