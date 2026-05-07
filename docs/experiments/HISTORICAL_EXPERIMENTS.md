# Historical and Exploratory Experiments

## Purpose

Exp1-Exp10 are not all equally central to the first manuscript. This document separates historical exploration, mechanism-building support, and manuscript-critical evidence so future edits do not accidentally upgrade old exploratory results into central claims.

Claim: The current manuscript-critical spine is Exp11-Exp13 plus completed Exp13.1 hardening.
Evidence: The experiment registry, manuscript spine, and publication-readiness docs all make Exp13.1 lesion audit, separate Exp13.2 baseline alignment, uncertainty, and final figures the next blockers.
Caveat: Supporting and historical experiments may still be useful for background or supplementary context, but they should not be treated as external baselines or final manuscript evidence without renewed validation.
Source path: `docs/experiments/EXPERIMENT_REGISTRY.md`; `docs/manuscript/MANUSCRIPT_SPINE.md`; `docs/synthesis/PUBLICATION_READINESS.md`

Scope note: Exp13.2 is intentionally excluded from the current cleanup pass and is not part of the Tier A internal spine until a separate import/alignment pass updates the canonical docs.

## Experiment tiers

## Tier A - Manuscript-critical

Experiments: Exp11, Exp12, Exp13, Exp13.1.

Role:

- Provides the current first-manuscript spine: context-separated incompatible-world memory, clean-context scaling, boundary mapping, and publication hardening.

How it may be used:

- Use for central manuscript evidence only with the caveats in `docs/manuscript/CLAIMS_AND_EVIDENCE.md`.
- Use Exp13.1 with the caveats in `docs/experiments/exp13_1_summary.md`, especially the failed lesion diagnostic.

How it should not be used:

- Do not claim submission readiness before the separate Exp13.2 baseline pass, uncertainty reporting, Exp13.1 lesion audit if needed, and final figures.
- Do not modify Exp13 in place to implement successor hardening.

| Experiment | Directory | Summary doc | Manuscript role | Caveat |
|---|---|---|---|---|
| Exp11 | `experiments/experiment11_context_memory/` | `docs/experiments/exp11_summary.md` | Candidate main context-separated memory evidence. | Oracle world context; external baselines and intervals pending. |
| Exp12 | `experiments/experiment12_capacity_generalization/` | `docs/experiments/exp12_summary.md` | Candidate main capacity/scaling evidence. | Ceiling-limited; context-noise sweeps are diagnostic, not final robustness evidence. |
| Exp13 | `experiments/experiment13_breaking_point/` | `docs/experiments/exp13_summary.md` | Candidate main boundary-mapping evidence. | Metric cleanup, clean ablations, stochastic context corruption, and capacity-law summaries pending. |
| Exp13.1 | `experiments/experiment13_1_publication_hardening/` | `docs/experiments/exp13_1_summary.md` | Publication hardening successor. | Internal evidence only; targeted lesion diagnostic failed and baselines/uncertainty remain pending. |

## Tier B - Mechanism-building / supporting

Experiments: Exp7, Exp8, Exp9, Exp10.

Role:

- Builds mechanism intuition for route fields, self-organizing acquisition, robustness stressors, and stability-plasticity tradeoffs.

How it may be used:

- Use as background, mechanism support, or supplementary evidence when tied to current source paths and caveats.
- Use Exp7/Exp8 to explain route-table versus recurrent execution mechanics.

How it should not be used:

- Do not treat supporting internal ablations as external baselines.
- Do not make broad biological, continual-learning, or robustness claims from these experiments alone.

| Experiment | Directory | Summary doc | Manuscript role | Caveat |
|---|---|---|---|---|
| Exp7 | `experiments/experiment7_route_field_diagnostics/` | `docs/experiments/exp7_summary.md` | Diagnostic route-field support. | Clean diagnostic setting; not self-organized acquisition. |
| Exp8 | `experiments/experiment8_self_organizing_route_acquisition/` | `docs/experiments/exp8_summary.md` | Supporting mechanism evidence for route-field acquisition. | Synthetic symbolic task; external baselines pending. |
| Exp9 | `experiments/experiment9_robust_adaptive_route_plasticity/` | `docs/experiments/exp9_summary.md` | Supporting robustness and stressor evidence. | Effects are stress-dependent; not required in every clean regime. |
| Exp10 | `experiments/experiment10_adaptive_reversal/` | `docs/experiments/exp10_summary.md` | Supporting stability-plasticity and reversal evidence. | Adaptive rebinding, not non-destructive multi-world memory. |

## Tier C - Historical / exploratory

Experiments: Exp1, Exp2, Exp3, Exp4, Exp5, Exp6.

Role:

- Records the exploratory path from MNIST/plastic-graph prototypes to route traversal and corrected route audits.

How it may be used:

- Use for project history, motivation, and negative or caveated methodological lessons.
- Use only with local artifacts and explicit caveats if any exact number is cited.

How it should not be used:

- Do not use as central evidence for the first route-memory manuscript unless later docs explicitly elevate a specific result.
- Do not cite as external baselines or as proof of the final mechanism.

| Experiment | Directory | Summary doc | Manuscript role | Caveat |
|---|---|---|---|---|
| Exp1 | `experiments/experiment1/` | `docs/experiments/exp1_summary.md` | Historical implementation background. | No non-empty Exp1-specific result digest; no central route-memory claim. |
| Exp2 | `experiments/experiment2/` | `docs/experiments/exp2_summary.md` | Historical MNIST/plastic-graph evidence. | Classification prototype; not route-memory composition. |
| Exp3 | `experiments/experiment3/` | `docs/experiments/exp3_summary.md` | Historical motivation for moving beyond MNIST. | MNIST suite did not isolate recurrent traversal. |
| Exp4 | `experiments/experiment4_successor/` | `docs/experiments/exp4_summary.md` | Early traversal contrast. | Single successor task; no incompatible context-conditioned worlds. |
| Exp5 | `experiments/experiment5_contextual_successor/` | `docs/experiments/exp5_summary.md` | Caveated contextual-successor precursor. | Low composition and traversal-loop ambiguity. |
| Exp6 | `experiments/experiment6_route_audit_successor/` | `docs/experiments/exp6_summary.md` | Corrected route-audit failure/diagnostic precursor. | Negative but informative; not robust contextual route memory. |
