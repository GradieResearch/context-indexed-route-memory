# Publication Readiness

## Summary Judgment

Status: ready for claim hardening and final figure/table planning, but not submission-ready.

The current internal spine is defensible but narrow: in a controlled symbolic route-memory benchmark, context-indexed structural plasticity stores incompatible local transition systems, recurrent execution composes stored one-step transitions into multi-step routes, Exp13.2 supplies symbolic/algorithmic baseline coverage, and Exp14 shows that the active symbolic world can be selected from partial transition cues. Exp11, Exp12, Exp13, Exp13.1, Exp13.2, and Exp14 support this story with important caveats.

Exp13.2 should now be treated as imported symbolic/algorithmic baseline evidence. It partially satisfies C12 for a controlled symbolic/mechanistic manuscript, but it does not provide neural baselines and does not replace prior-art/novelty import.

Source path: `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/manuscript/LIMITATIONS_AND_THREATS.md`; `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`; `docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md`.

## Strongest Evidence

- Exp11 A/B context-separated retention and ablations. Source path: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `docs/threads/experiment11_export`.
- Exp12 clean scaling to 32 worlds with no-recurrence/no-world-context/no-structural-plasticity contrasts. Source path: `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `docs/threads/experiment12to13_export.md`.
- Exp13 finite-capacity breaking and no-recurrence route-table/composition dissociation. Source path: `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`.
- Exp13.1 publication-hardening ablations: no-recurrence-at-eval preserves route-table accuracy while composition collapses, no-structural-plasticity fails, no-context-binding fails, and local budget pressure is much more damaging than global budget pressure. Source path: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv`.
- Exp13.2 symbolic/algorithmic baseline suite: oracle context-gated lookup matches CIRM on the clean supplied-context benchmark, no-context lookup fails conflict-sensitive probes, no-recurrence separates route-table storage from composition, endpoint memorization fails suffix composition, and hash/superposition-style controls expose context compression/collision behavior. Source path: `docs/experiments/exp13_2_summary.md`; `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`.
- Exp14 latent symbolic context selection: full run validation passed, clean hard-slice CIRM selection/composition reaches 1.0000, and cue corruption/cue-count sweeps quantify the symbolic selection boundary. Source path: `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_report.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `docs/threads/experiment14_analysis_digest.md`.

## Weakest Evidence

- Neural baselines are absent. Source path: `docs/manuscript/BASELINE_REQUIREMENTS.md`.
- Prior-art/novelty evidence remains incomplete. Source path: `docs/manuscript/BASELINE_REQUIREMENTS.md`; local verification pending for `Pasted text.txt`.
- Consolidation as a stability-plasticity bias is preliminary because Exp13 validation shows only a small finite-pressure delta and Exp13.1 did not show constrained-budget accuracy rescue. Source path: `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv`.
- Exp13.1 targeted lesion evidence failed the expected pattern and should not be used as positive mechanism evidence. Source path: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_lesion_metrics.csv`.
- Primitive holdout needs metric cleanup if retained centrally. Source path: `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv`.
- Continuous/noisy input is only a front-end bridge, not end-to-end perception. Source path: `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv`.
- Exp14 is symbolic transition-cue inference, not raw sensory latent-world discovery; the oracle context-gated table remains an upper bound. Source path: `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `docs/threads/experiment14_analysis_digest.md`.

## Required Before Manuscript Draft

- Use `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md` as the handoff for final figure/table generation and manuscript drafting.
- Decide whether Exp14/C13 is a main-text result or supplementary result.
- Decide whether the first submission target permits a controlled symbolic/mechanistic benchmark without neural baselines.
- Refresh `docs/manuscript/MANUSCRIPT_SPINE.md` from the claim-freeze document.

## Required Before Submission

- Add seed-level confidence intervals and effect sizes for retained core claims.
- Create final paper figures from reproducible scripts with source-data manifests.
- Add source-data/final figures for Exp14 if retained.
- Import prior-art/novelty evidence as local source artifacts.
- Verify manuscript-critical smoke/validation/full commands and document runtimes/hardware.
- Add human-chosen `LICENSE` and `CITATION.cff`.
- Fix holdout metrics if C9 remains central.
- Audit/rerun Exp13.1 lesion diagnostic only if positive lesion evidence will be cited.
- Keep biological, novelty, continual-learning, perception, and generalization claims narrow.
- Run `python scripts/verify_doc_source_paths.py` before readiness handoff.

## Operational Readiness

Claim: The repository is more navigable after this cleanup, but remains scientifically not submission-ready.

Evidence: The README/docs index, source-of-truth note, claim-freeze document, manuscript TODO, figure plan, reproducibility audit, source-data manifest, and statistical-readiness table now describe the post-Exp13.2/post-Exp14 state.

Caveat: This is documentation readiness, not new scientific evidence.

Source path: `README.md`; `docs/README.md`; `docs/manuscript/SOURCE_OF_TRUTH.md`; `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`; `docs/manuscript/MANUSCRIPT_TODO.md`; `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`; `docs/source_data/SOURCE_DATA_MANIFEST.csv`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`.

## Reviewer-Risk Matrix

| Reviewer criticism | Why they might say it | Current answer | Required fix |
|---|---|---|---|
| Internal ablations are not enough. | Most core claims compare model variants and symbolic controls. | Exp13.2 adds symbolic/algorithmic baselines, but not neural baselines. | Decide target venue and add neural baselines if needed. |
| Oracle context-gated lookup solves clean supplied-context benchmark. | Exp13.2 shows oracle context-gated lookup matches CIRM in the clean supplied-context setting. | Agreed; raw clean supplied-context accuracy is not the novelty claim. | Frame contribution around mechanism decomposition, capacity/boundary mapping, and Exp14 symbolic cue-selected context. |
| Generalization is overstated. | Exp13 unseen primitive transitions fail. | The manuscript should claim composition over stored primitives, not unseen transition inference. | Fix seen/unseen/all holdout metrics and wording if C9 is retained centrally. |
| Consolidation claim is weak. | Easy regimes do not need consolidation; Exp13 delta is small. | Current claim is bias/tradeoff, not necessity. | Keep supplementary or add dose-response/robustness evidence. |
| Context noise result is artificial. | Exp13 adversarial corruption, Exp13.1 wrong-world injection, and Exp14 cue corruption are synthetic selection tests. | It is useful as a selection-boundary test. | Add stochastic graded context corruption only if generic robustness is claimed. |
| Targeted lesion claim fails. | Exp13.1 targeted lesion is less damaging than random count-matched lesion. | Do not use the lesion diagnostic as positive mechanism evidence. | Audit critical-edge selection and rerun if lesion evidence is needed. |
| Biological framing overreaches. | The task is symbolic and synthetic. | Frame as computational inspiration only. | Tighten related work and limitations language. |
| Applied bridge is not applied learning. | Continuous front-end is decoded/noisy, not learned perception. | Keep it preliminary or supplementary. | Build a real visual-state route-memory bridge later. |
| Latent-context claim overreaches. | Exp14 uses symbolic transition cues and synthetic corruption. | C13 is limited to symbolic cue selection; oracle context gating remains an upper bound. | Keep wording narrow and add final source-data-backed figures only if retained. |
