# Limitations and Threats

Purpose: Track limitations, reviewer attack surfaces, and non-claims so the manuscript stays disciplined.

## Missing External Baselines

Claim: External baselines are required before submission-readiness can be claimed.
Evidence: The imported Exp11 and Exp12-13 thread digests flag baselines as required, and the Exp12-13 digest reports a novelty assessment that warned against treating context gating, task masks, recurrence, structural plasticity, or continual learning as individually novel.
Caveat: The novelty assessment artifact named `Pasted text.txt` is not present locally; local verification pending. `docs/manuscript/BASELINE_REQUIREMENTS.md` is a planning document, not evidence for novelty.
Source path: `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md`
Proposed fix: Implement a baseline suite covering locally source-backed families: context-dependent gating / XdG-style comparators, SI or stabilization-plus-gating, replay, task masks / HAT, parameter isolation / PackNet / PathNet, hypernetworks, superposition, and cognitive-map / CSCG / TEM-style comparators.

## Symbolic Benchmark Limitation

Why it matters: Most evidence comes from synthetic route-memory tasks with symbolic nodes, modes, and supplied contexts.
Where identified: Exp6, Exp11, and Exp12-13 digests repeatedly warn against biological or broad applied overclaims.
Source thread path: `docs/threads/experiment6_export.md`; `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`.
Proposed fix: Keep claims benchmark-specific; use the continuous/noisy bridge only as preliminary until richer non-symbolic tasks exist.

## Oracle Context / World-Label Limitation

Why it matters: Many experiments provide world/context labels directly. This supports context-indexed storage, but not latent world inference.
Where identified: Exp11 and Exp12-13 framing; Exp14 was proposed as a future latent-world inference bridge.
Source thread path: `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`.
Proposed fix: Add a future experiment where world/context is inferred from prediction error or partial evidence, not supplied as an oracle label.

## Metric Cleanup Requirements

Why it matters: Reviewers can reject claims if metric definitions hide failure modes or combine incompatible cases.
Where identified: Exp13 holdout and no-context-binding caveats.
Source thread path: `docs/threads/experiment12to13_export.md`.
Proposed fix: Add holdout seen-vs-unseen metric splits; report route-table all/seen/unseen; add context corruption sensitivity; add seed-level confidence intervals; run consolidation dose-response.

## No Overclaiming Biological Theory

Why it matters: The model is biologically inspired, but the experiments do not validate a complete hippocampal or neural theory.
Where identified: Novelty/framing discussion in the Exp12-13 digest and earlier manuscript framing.
Source thread path: `docs/threads/experiment12to13_export.md`; `docs/threads/experiment11_export`.
Proposed fix: Use language such as "computationally inspired by indexing, remapping, recurrence, and structural plasticity"; avoid claims of biological explanation.

## Applied Bridge Remains Preliminary

Why it matters: Exp13 continuous/noisy input tests whether a decoded noisy start state can feed the route-memory mechanism, not whether the model learns perception end to end.
Where identified: Exp12-13 digest and Exp13 validation.
Source thread path: `docs/threads/experiment12to13_export.md`.
Proposed fix: Keep Figure 7 as supplementary or preliminary unless a new applied visual-state route-memory experiment is run.

## Context Corruption Is Not Fully Realistic Yet

Claim: Exp13 adversarial context corruption is useful failure evidence but not a graded stochastic robustness test.
Evidence: `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv` shows the full model collapses under adversarial mixture once wrong-world evidence dominates.
Caveat: Exp11/Exp12 context-noise artifacts are diagnostics only; stochastic/graded corruption remains required.
Source path: `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`; `docs/threads/experiment12to13_export.md`
Proposed fix: Add stochastic context corruption and report top-1 world selection, margins, and behavior across corruption probability.

## Consolidation Claim Is Fragile

Why it matters: Easy regimes do not require consolidation, and Exp13 validation reports only a small finite-pressure consolidation delta.
Where identified: Exp10, Exp11, Exp12, and Exp13 thread analyses.
Source thread path: `docs/threads/experiment5to10_export.md`; `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`.
Proposed fix: Frame consolidation as a stability-plasticity bias; run dose-response under finite capacity before central use.

## Non-Claims

- Do not claim solved continual learning.
- Do not claim context gating is novel by itself.
- Do not claim broad abstract rule induction.
- Do not claim end-to-end perception.
- Do not claim consolidation is universally necessary.
