# Publication Readiness

## Summary Judgment

Status: improved and navigable, but not submission-ready.

The current internal spine is defensible but narrow: in a controlled symbolic route-memory benchmark, context-indexed structural plasticity stores incompatible local transition systems, recurrent execution composes stored one-step transitions into multi-step routes, and Exp14 shows that the active symbolic world can be selected from partial transition cues. Exp11, Exp12, Exp13, Exp13.1, and Exp14 support this story with important caveats.

Exp13.2 is intentionally excluded from this cleanup pass. Baseline-suite analysis/import/alignment must happen separately before C12 or baseline figures are updated.

Source path: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/manuscript/LIMITATIONS_AND_THREATS.md`; `docs/repo_audit/P0_P1_PUBLICATION_CLEANUP_REPORT.md`.

## Strongest Evidence

- Exp11 A/B context-separated retention and ablations. Source path: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `docs/threads/experiment11_export`.
- Exp12 clean scaling to 32 worlds with no-recurrence/no-world-context/no-structural-plasticity contrasts. Source path: `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `docs/threads/experiment12to13_export.md`.
- Exp13 finite-capacity breaking and no-recurrence route-table/composition dissociation. Source path: `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`.
- Exp13.1 publication-hardening ablations: no-recurrence-at-eval preserves route-table accuracy while composition collapses, no-structural-plasticity fails, no-context-binding fails, and local budget pressure is much more damaging than global budget pressure. Source path: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv`.
- Exp14 latent symbolic context inference: full run validation passed, clean hard-slice CIRM selection/composition reaches 1.0000, and cue corruption/cue-count sweeps quantify the boundary. Source path: `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_report.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `docs/threads/experiment14_analysis_digest.md`.

## Weakest Evidence

- External/symbolic baseline integration is deferred to a separate Exp13.2 pass. Source path: `docs/manuscript/BASELINE_REQUIREMENTS.md`.
- Consolidation as a stability-plasticity bias is preliminary because Exp13 validation shows only a small finite-pressure delta and Exp13.1 did not show constrained-budget accuracy rescue. Source path: `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv`.
- Exp13.1 targeted lesion evidence failed the expected pattern and should not be used as positive mechanism evidence. Source path: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_lesion_metrics.csv`.
- Primitive holdout needs metric cleanup. Source path: `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv`.
- Continuous/noisy input is only a front-end bridge, not end-to-end perception. Source path: `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv`.
- Exp14 is symbolic transition-cue inference, not raw sensory latent-world discovery; the oracle context-gated table remains an upper bound. Source path: `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `docs/threads/experiment14_analysis_digest.md`.
- Prior-art/novelty evidence remains incomplete. Source path: `docs/manuscript/BASELINE_REQUIREMENTS.md`; local verification pending for `Pasted text.txt`.

## Required Before Submission

- Complete separate Exp13.2 analysis/import/alignment pass and decide whether additional neural baselines are required.
- Add seed-level confidence intervals and effect sizes for core claims.
- Create final paper figures from reproducible scripts with source-data manifests.
- Decide whether Exp14 C13 is main text or supplement, and add source-data/final figures if retained.
- Import prior-art/novelty evidence as local source artifacts.
- Verify manuscript-critical smoke/validation/full commands and document runtimes/hardware.
- Add human-chosen `LICENSE` and `CITATION.cff`.
- Fix holdout metrics if C9 remains central.
- Audit/rerun Exp13.1 lesion diagnostic only if positive lesion evidence will be cited.
- Keep biological, novelty, continual-learning, perception, and generalization claims narrow.
- Run `python scripts/verify_doc_source_paths.py` before readiness handoff.

## Operational Readiness

Claim: The repository is more navigable after this cleanup, but remains scientifically not submission-ready.
Evidence: The README, docs index, manuscript TODO, figure plan, reproducibility audit, artifact index, missing-artifacts report, source-data manifest, and statistical-readiness table now describe the non-Exp13.2 state.
Caveat: This is documentation readiness, not new scientific evidence.
Source path: `README.md`; `docs/README.md`; `docs/manuscript/MANUSCRIPT_TODO.md`; `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`; `docs/source_data/SOURCE_DATA_MANIFEST.csv`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`

## Reviewer-Risk Matrix

| Reviewer criticism | Why they might say it | Current answer | Required fix |
|---|---|---|---|
| Internal ablations are not enough. | Most claims compare only model variants. | Agreed; C12 remains `Needs baseline` in this pass. | Complete separate Exp13.2 import/alignment and decide on neural baselines. |
| Generalization is overstated. | Exp13 unseen primitive transitions fail. | The manuscript should claim composition over stored primitives, not unseen transition inference. | Fix seen/unseen/all holdout metrics and wording. |
| Consolidation claim is weak. | Easy regimes do not need consolidation; Exp13 delta is small. | Current claim is bias/tradeoff, not necessity. | Add dose-response or keep supplementary. |
| Context noise result is artificial. | Exp13 adversarial corruption and Exp13.1 wrong-world injection are identity tests. | It is useful as a selection-boundary test. | Add stochastic graded context corruption if robustness is claimed. |
| Targeted lesion claim fails. | Exp13.1 targeted lesion is less damaging than random count-matched lesion. | Do not use the lesion diagnostic as positive mechanism evidence. | Audit critical-edge selection and rerun if lesion evidence is needed. |
| Biological framing overreaches. | The task is symbolic and synthetic. | Frame as computational inspiration only. | Tighten related work and limitations language. |
| Applied bridge is not applied learning. | Continuous front-end is decoded/noisy, not learned perception. | Keep it preliminary or supplementary. | Build a real visual-state route-memory bridge later. |
| Latent-context claim overreaches. | Exp14 uses symbolic transition cues and synthetic corruption. | C13 is limited to symbolic cue selection; oracle context gating remains an upper bound. | Keep wording narrow and add final source-data-backed figures only if retained. |
