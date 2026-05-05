# Publication Readiness

## Summary Judgment

Status: promising, but not manuscript-ready.

The internal evidence now supports a narrow manuscript spine: context-indexed structural plasticity stores incompatible local route systems, and recurrence is required to execute those stored routes compositionally. Submission readiness is blocked by external baselines, Exp13.1 hardening, statistical reporting, and final reproducible figures.

Source path: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/threads/experiment12to13_export.md`.

## Strongest Evidence

- Exp11 A/B context-separated retention and ablations. Source path: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `docs/threads/experiment11_export`.
- Exp12 clean scaling to 32 worlds with no-recurrence/no-world-context/no-structural-plasticity contrasts. Source path: `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `docs/threads/experiment12to13_export.md`.
- Exp13 finite-capacity breaking and no-recurrence route-table/composition dissociation. Source path: `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `docs/threads/experiment12to13_export.md`.

## Weakest Evidence

- Consolidation as a stability-plasticity bias is preliminary because Exp13 validation shows only a small finite-pressure delta. Source path: `experiments/experiment13_breaking_point/analysis/validation_report.md`.
- Primitive holdout needs metric cleanup. Source path: `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv`.
- Continuous/noisy input is only a front-end bridge, not end-to-end perception. Source path: `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv`.
- External baseline evidence is absent. Source path: `docs/manuscript/BASELINE_REQUIREMENTS.md`.

## Required Before Submission

- Complete Exp13.1 publication-hardening audit.
- Add external baseline suite.
- Add seed-level confidence intervals and effect sizes.
- Fix holdout metrics and no-context-binding ablation naming/design.
- Create final paper figures from reproducible scripts.
- Keep biological and novelty claims narrow.

## Reviewer-Risk Matrix

| Reviewer criticism | Why they might say it | Current answer | Required fix |
|---|---|---|---|
| This is just context gating/task masks. | Context labels are supplied and baselines are missing. | Current claim is narrower: structural-plastic recurrent route memory plus route-table/execution dissociation. | Add context-gated, task-mask, replay, and parameter-isolation baselines. |
| Internal ablations are not enough. | Most claims compare only model variants. | Exp8-Exp13 show coherent mechanism necessity within the benchmark. | Run external baseline suite and report effect sizes. |
| Generalization is overstated. | Exp13 unseen primitive transitions fail. | The manuscript should claim composition over stored primitives, not unseen transition inference. | Fix seen/unseen/all holdout metrics and wording. |
| Consolidation claim is weak. | Easy regimes do not need consolidation; Exp13 delta is small. | Current claim is bias/tradeoff, not necessity. | Run consolidation dose-response under finite capacity. |
| Context noise result is artificial. | Exp13 adversarial corruption is threshold-like. | It is useful as a selection-boundary test. | Add stochastic graded context corruption. |
| Biological framing overreaches. | The task is symbolic and synthetic. | Frame as computational inspiration only. | Tighten related work and limitations language. |
| Applied bridge is not applied learning. | Continuous front-end is decoded/noisy, not learned perception. | Keep it preliminary or supplementary. | Build a real visual-state route-memory bridge later. |
