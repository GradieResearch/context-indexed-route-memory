# First Manuscript Claim Freeze

Purpose: Freeze a conservative, post-Exp14 first-manuscript claim set before final figure/table generation and manuscript drafting.

This document is a manuscript-planning control point, not a new analysis artifact. It aligns the active claim posture after Exp13.2 symbolic/algorithmic baseline import and Exp14 symbolic transition-cue context-selection import.

## 1. Scope

The first manuscript should be framed as a controlled symbolic/mechanistic benchmark paper about context-indexed route memory.

Safe high-level contribution:

> In a controlled symbolic route-memory benchmark, context-indexed structural plasticity stores incompatible local transition systems, recurrent execution composes stored one-step transitions into multi-step routes, and symbolic transition cues can select the active world/context before route execution.

Non-claims:

- Do not claim solved continual learning.
- Do not claim context gating is novel by itself.
- Do not claim broad neural-network superiority.
- Do not claim broad biological proof or a complete hippocampal theory.
- Do not claim raw sensory latent-world discovery.
- Do not claim end-to-end perceptual learning.
- Do not claim inference of unseen primitive transitions.
- Do not use Exp13.1 lesion diagnostics as positive mechanism evidence unless audited and rerun.

## 2. Canonical Exp13.2 decision

Claim: Exp13.2 is now part of the local evidence base as a completed symbolic/algorithmic baseline suite.

Evidence: `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md` reports a completed import with local artifacts, `PASS: 28`, `WARN: 0`, `FAIL: 0`, and updates to baseline-related docs. `docs/experiments/exp13_2_summary.md` records the local full run, including 20 seeds, summary/effect-size artifacts, and the key caveat that oracle context-gated lookup matches CIRM on the clean supplied-context benchmark.

Caveat: Exp13.2 does not supply neural baselines and does not complete prior-art/novelty positioning. It partially satisfies C12 for a controlled symbolic/mechanistic manuscript, but it does not make the repository submission-ready for a stronger ML venue.

Source path: `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`; `docs/experiments/exp13_2_summary.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/validation_report.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`.

## 3. Canonical Exp14 decision

Claim: Exp14 is now part of the local evidence base as completed symbolic transition-cue context-selection evidence.

Evidence: `docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md` reports that smoke, validation, and full profiles passed validation. The full profile has 20 seeds, 46,080 metrics rows, 2,304 summary rows, 12,288 effect-size rows, and six generated analysis plots. The hard clean slice reaches 1.0000 CIRM world selection and composition; the highest-corruption hard slice remains around 0.9416 while the oracle context-gated table remains an upper bound.

Caveat: Exp14 supports symbolic transition-cue selection, not raw sensory latent-world discovery. Its generated plots are candidate analysis outputs, not final manuscript figures.

Source path: `docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md`; `docs/threads/experiment14_analysis_digest.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_report.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`.

## 4. Frozen main claims

| Claim | First-manuscript role | Safe wording | Supporting experiments | Required before draft | Required before submission |
|---|---|---|---|---|---|
| C1 Structural plasticity | Main but benchmark-specific | Within this symbolic route-memory benchmark, removing structural plasticity collapses route-table formation and route execution. | Exp8, Exp11, Exp12, Exp13, Exp13.1, Exp13.2 | Final figure/table plan | CI/effect-size table; prior-art framing |
| C2 World/context indexing | Main but narrow | Context/world indexing separates incompatible transition systems; Exp14 shows the active symbolic context can also be selected from transition cues. | Exp11, Exp12, Exp13, Exp13.1, Exp13.2, Exp14 | Separate supplied-context and cue-selected wording | CI/effect-size table; oracle-context caveat |
| C3 Recurrence | Main | Recurrent execution is required to compose stored one-step route memories into multi-step routes. | Exp7, Exp8, Exp11, Exp12, Exp13, Exp13.1, Exp13.2 | Final core-ablation figure | CI/effect-size table |
| C4 Route-table/composition dissociation | Main | Route-table storage and multi-step compositional execution are separable in this benchmark. | Exp7, Exp8, Exp11, Exp12, Exp13, Exp13.1, Exp13.2, Exp14 | Final core-ablation figure | CI/effect-size table |
| C5 Clean capacity scaling | Main but ceiling-limited | Under clean supplied context, the full model maintains ceiling route-table and composition accuracy through the tested world counts. | Exp12 | Pair with boundary figure to avoid ceiling-only story | CI/effect-size table; avoid fitted-law wording |
| C6 Finite-budget degradation | Main but narrow | Finite structural budget produces an observed route-execution degradation curve. | Exp13 | Decide whether this is main or paired with C7 | CI/effect-size table; capacity-law fitting only if claiming a law |
| C13 Symbolic transition-cue context selection | Main but narrow, or high-priority supplement | The active symbolic world/context can be selected from partial transition-cue evidence before route execution. | Exp14 | Decide main vs supplement placement; add source-data/final-figure plan | Final figure script; caption caveat that oracle remains upper bound |

## 5. Supplement-only or narrow boundary claims

| Claim | Recommended handling | Reason | Required if elevated |
|---|---|---|---|
| C7 Local-vs-global budget | Supplement or narrow main panel | Evidence is promising but still needs paired seed-level comparison. | Paired seed-level local/global table and CI/effect sizes. |
| C8 Consolidation | Supplement only | Evidence supports stability/plasticity bias, not accuracy rescue or necessity. | Margin/robustness analysis or stronger dose-response. |
| C9 Seen-vs-unseen primitive boundary | Supplement unless cleaned | Metric split cleanup remains required. | Add seen/unseen/all route-table and composition split metrics. |
| C10 Context corruption / cue corruption | Supplement or narrow boundary panel | Evidence supports wrong-world or cue-evidence sensitivity, not generic stochastic robustness. | Add stochastic context corruption only if robustness is claimed. |
| C11 Continuous/noisy bridge | Supplement/future work | Current bridge is decoded/noisy symbolic input, not learned perception. | New applied or end-to-end perceptual bridge experiment if central. |
| C12 Baselines/prior art | Discussion/readiness claim | Symbolic baselines are partially complete; neural baselines and prior art remain open. | Prior-art import and target-venue neural-baseline decision. |

## 6. Dropped or explicit non-claims for the first manuscript

| Candidate claim | Handling | Reason |
|---|---|---|
| Positive targeted-lesion mechanism claim | Drop | Exp13.1 targeted lesion diagnostic failed the expected pattern. |
| Broad biological memory mechanism | Drop as claim; keep as inspiration | Evidence is symbolic and synthetic. |
| Neural-network superiority | Drop unless neural baselines are added | Exp13.2 baselines are symbolic/algorithmic. |
| Solved continual learning | Drop | The benchmark is controlled and narrow. |
| Raw latent-world discovery | Drop | Exp14 uses symbolic transition cues. |
| End-to-end perception | Drop | Exp13 bridge is not learned perception. |
| Broad abstract rule induction | Drop | C9 explicitly warns against unseen primitive inference. |

## 7. Figure/table implications

Candidate main figure set:

1. Figure 1: conceptual schematic / benchmark setup.
2. Figure 2: core structural-plasticity, context-indexing, and recurrence ablation.
3. Figure 3: clean capacity scaling and retention.
4. Figure 4: finite structural budget / local-vs-global pressure.
5. Figure 5: symbolic transition-cue context selection from Exp14.
6. Table 1 or Supplement: Exp13.2 symbolic/algorithmic baseline suite, explicitly noting that oracle context-gated lookup matches CIRM under clean supplied context.

Supplement candidates:

- consolidation stability/plasticity bias;
- held-out seen-vs-unseen primitive boundary if metrics are cleaned;
- context corruption and wrong-world injection;
- continuous/noisy bridge;
- failed lesion diagnostic as negative diagnostic only.

Generated analysis plots must not be treated as final manuscript figures. Every retained panel needs a reproducible final figure script and source-data manifest entry.

## 8. Statistical/source-data implications

Required before submission:

- Add manuscript-grade CI/effect-size tables for C1-C7 and C13 where retained.
- Treat Exp13.2 effect-size artifacts as available but still requiring human-reviewed grouping before citation.
- Treat Exp14 effect-size artifacts as available but still requiring human-reviewed grouping before citation.
- Keep C9 out of the main claim set unless seen/unseen metric cleanup is completed.
- Keep capacity-law language out unless capacity fitting is added.

Source path: `docs/source_data/SOURCE_DATA_MANIFEST.csv`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`; `scripts/compute_seed_metric_summary.py`.

## 9. Remaining blockers before manuscript draft

- Decide final main-vs-supplement placement for Exp14/C13.
- Decide whether the first manuscript targets a controlled symbolic/mechanistic venue or requires neural baselines first.
- Generate final figure/table plan from this freeze document.
- Update manuscript spine to include Exp13.2 and Exp14 as completed evidence rather than pending/future work.

## 10. Remaining blockers before submission

- Manuscript-grade CI/effect-size tables.
- Final reproducible figure scripts and source-data manifests.
- Prior-art/novelty import and citations.
- Fresh command verification with runtime/hardware logs.
- License and citation metadata.
- C9 metric cleanup if retained centrally.
- Lesion audit/rerun only if lesion evidence is cited positively.

## 11. Recommended next action

Proceed to final figure/table generation scripts using this frozen claim set. Do not design another experiment unless the target venue requires neural baselines or unless the first manuscript intentionally elevates C9, generic robustness, positive lesion evidence, or raw latent-world discovery.
