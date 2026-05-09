# First Manuscript Claim Freeze

Purpose: Freeze a conservative first-manuscript claim set before final figure/table generation and manuscript submission hardening.

Status note: this document began as the post-Exp14 claim freeze. It remains the first-manuscript inclusion/exclusion control document, but it is now supplemented by `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`. When the addendum is stricter than this document, use the addendum.

This document is a manuscript-planning control point, not a new analysis artifact. It aligns the active claim posture after Exp13.2 symbolic/algorithmic baseline import, Exp14 symbolic transition-cue context-selection import, Exp15 minimal neural-comparator import, and `docs/manuscript/draft/MANUSCRIPT_V2.md` capture.

## 1. Scope

The first manuscript should be framed as a controlled symbolic/mechanistic benchmark paper about context-indexed route memory.

Safe high-level contribution:

> In a controlled symbolic route-memory benchmark, context-indexed structural route memory stores incompatible local transition systems, recurrent execution composes stored one-step transitions into multi-step routes, symbolic transition cues can select the active world/context before route execution, and minimal neural comparator results expose important distinctions between endpoint memorization, context-conditioned transition learning, suffix composition, and first-step conflict disambiguation.

Non-claims:

- Do not claim solved continual learning.
- Do not claim context gating is novel by itself.
- Do not claim broad neural-network superiority.
- Do not claim broad biological proof or a complete hippocampal theory.
- Do not claim raw sensory latent-world discovery.
- Do not claim end-to-end perceptual learning.
- Do not claim inference of unseen primitive transitions.
- Do not use Exp13.1 lesion diagnostics as positive mechanism evidence unless audited and rerun.
- Do not use Exp15 replay collapse as scientific evidence unless audited.

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

## 4. Canonical Exp15 decision

Claim: Exp15 is now part of the local evidence base as a completed minimal fixed-profile neural comparator.

Evidence: `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md` and `docs/threads/experiment15_analysis_digest.md` record the imported full run `exp15_full_20260508_092811`. The run contains 10 seeds, 9 variants, 5,400 seed metric rows, 540 summary rows, 1,080 runtime rows, a validation report, and compact V2 Table 4 artifacts.

Caveat: Exp15 is not exhaustive neural benchmarking. It uses fixed small models and hyperparameters, omits memory-augmented/key-value neural baselines, and includes a reconstructed-manifest/empty-SQLite-`run_manifest` caveat. Its results narrow the claim posture because `neural_transition_mlp_context` and `neural_transition_mlp_world_heads_context` solve the clean hard slice at ceiling.

Source path: `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`; `docs/threads/experiment15_analysis_digest.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/validation_report.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`; `docs/manuscript/tables/table_04_exp15_neural_comparator.md`; `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`.

## 5. Frozen main claims

| Claim | First-manuscript role | Safe wording | Supporting experiments | Required before draft | Required before submission |
|---|---|---|---|---|---|
| C1 Structural route storage | Main but benchmark-specific | Within this symbolic route-memory benchmark and tested CIRM-family ablations, removing structural route storage collapses route-table formation and route execution. | Exp8, Exp11, Exp12, Exp13, Exp13.1, Exp13.2; Exp15 as narrowing evidence | Captured in V2 | CI/effect-size table; prior-art framing; avoid universal structural-plasticity wording |
| C2 World/context indexing | Main but conflict-specific | Context/world indexing is required for incompatible local transitions and first-step/full-route disambiguation; Exp14 shows the active symbolic context can also be selected from transition cues. | Exp11, Exp12, Exp13, Exp13.1, Exp13.2, Exp14, Exp15 | Separate supplied-context, cue-selected, and neural no-context wording | CI/effect-size table; oracle-context and suffix-route caveats |
| C3 Recurrence | Main | Recurrent execution is required to compose stored one-step route memories into multi-step routes in the tested route-memory contracts. | Exp7, Exp8, Exp11, Exp12, Exp13, Exp13.1, Exp13.2 | Final core-ablation figure | CI/effect-size table |
| C4 Route-table/composition dissociation | Main | Route-table storage, endpoint memorization, and multi-step compositional execution are separable in this benchmark. | Exp7, Exp8, Exp11, Exp12, Exp13, Exp13.1, Exp13.2, Exp14, Exp15 | Final core-ablation figure and V2 Table 4 | CI/effect-size table; Exp15 fixed-profile caveat |
| C5 Clean capacity scaling | Main but ceiling-limited | Under clean supplied context, the full model maintains ceiling route-table and composition accuracy through the tested world counts. | Exp12 | Pair with boundary figure to avoid ceiling-only story | CI/effect-size table; avoid fitted-law wording |
| C6 Finite-budget degradation | Main but narrow | Finite structural budget produces an observed route-execution degradation curve. | Exp13 | Decide whether this is main or paired with C7 | CI/effect-size table; capacity-law fitting only if claiming a law |
| C13 Symbolic transition-cue context selection | Main but narrow, or high-priority supplement | The active symbolic world/context can be selected from partial transition-cue evidence before route execution. | Exp14 | Decide main vs supplement placement; add source-data/final-figure plan | Final figure script; caption caveat that oracle remains upper bound |
| C12 Baseline coverage | Discussion/table claim | Symbolic/algorithmic baselines and a minimal neural comparator are now present, but prior-art import and broader neural-baseline decisions remain open. | Exp13.2, Exp15 | V2 Table 4 captured | Prior-art import; target-venue decision on memory-augmented/broader neural baseline |

## 6. Supplement-only or narrow boundary claims

| Claim | Recommended handling | Reason | Required if elevated |
|---|---|---|---|
| C7 Local-vs-global budget | Supplement or narrow main panel | Evidence is promising but still needs paired seed-level comparison. | Paired seed-level local/global table and CI/effect sizes. |
| C8 Consolidation | Supplement only | Evidence supports stability/plasticity bias, not accuracy rescue or necessity. | Margin/robustness analysis or stronger dose-response. |
| C9 Seen-vs-unseen primitive boundary | Supplement unless cleaned | Metric split cleanup remains required. | Add seen/unseen/all route-table and composition split metrics. |
| C10 Context corruption / cue corruption | Supplement or narrow boundary panel | Evidence supports wrong-world or cue-evidence sensitivity, not generic stochastic robustness. | Add stochastic context corruption only if robustness is claimed. |
| C11 Continuous/noisy bridge | Supplement/future work | Current bridge is decoded/noisy symbolic input, not learned perception. | New applied or end-to-end perceptual bridge experiment if central. |

## 7. Dropped or explicit non-claims for the first manuscript

| Candidate claim | Handling | Reason |
|---|---|---|
| Positive targeted-lesion mechanism claim | Drop | Exp13.1 targeted lesion diagnostic failed the expected pattern. |
| Broad biological memory mechanism | Drop as claim; keep as inspiration | Evidence is symbolic and synthetic. |
| Broad neural-network superiority | Drop | Exp15 shows context-conditioned neural transition learners solve the clean hard slice. |
| Solved continual learning | Drop | The benchmark is controlled and narrow. |
| Raw latent-world discovery | Drop | Exp14 uses symbolic transition cues. |
| End-to-end perception | Drop | Exp13 bridge is not learned perception. |
| Broad abstract rule induction | Drop | C9 explicitly warns against unseen primitive inference. |
| Replay-fails-general-method claim | Drop | Exp15 replay collapse requires implementation/training-regime audit before interpretation. |

## 8. Figure/table implications

Candidate main figure/table set:

1. Figure 1: conceptual schematic / benchmark setup.
2. Figure 2: core structural-storage, context-indexing, and recurrence ablation.
3. Figure 3: clean capacity scaling and retention.
4. Figure 4: finite structural budget / local-vs-global pressure.
5. Figure 5: symbolic transition-cue context selection from Exp14, pending main-vs-supplement decision.
6. Table 1: claim evidence summary.
7. Table 2: run integrity summary.
8. Table 3: statistical summary, pending retained-claim hardening.
9. Table 4: Exp15 minimal neural comparator hard-slice table, currently retained in V2 with supplement relocation left as a later venue/human decision.

Supplement candidates:

- Exp13.2 symbolic/algorithmic baseline suite details;
- Exp15 detailed neural comparator plots/runtimes;
- consolidation stability/plasticity bias;
- held-out seen-vs-unseen primitive boundary if metrics are cleaned;
- context corruption and wrong-world injection;
- continuous/noisy bridge;
- failed lesion diagnostic as negative diagnostic only.

Generated analysis plots must not be treated as final manuscript figures. Every retained panel needs a reproducible final figure script and source-data manifest entry.

## 9. Statistical/source-data implications

Required before submission:

- Decide retained main claims after V2 and post-Exp15 narrowing.
- Add manuscript-grade CI/effect-size tables for retained C1-C7, C13, and retained baseline claims.
- Treat Exp13.2 effect-size artifacts as available but still requiring human-reviewed grouping before citation.
- Treat Exp14 effect-size artifacts as available but still requiring human-reviewed grouping before citation.
- Treat Exp15 effect-size artifacts as available but still requiring human-reviewed grouping before citation.
- Keep C9 out of the main claim set unless seen/unseen metric cleanup is completed.
- Keep Exp15 replay collapse out of the scientific claim set unless audited.
- Keep capacity-law language out unless capacity fitting is added.

Source path: `docs/source_data/SOURCE_DATA_MANIFEST.csv`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`; `scripts/compute_seed_metric_summary.py`.

## 10. Remaining blockers before submission

- Retained main-claim decision after V2 and post-Exp15 narrowing.
- Manuscript-grade CI/effect-size tables.
- Final reproducible figure scripts and source-data manifests.
- Prior-art/novelty import and citations.
- Fresh command verification with runtime/hardware logs.
- License and citation metadata.
- C9 metric cleanup if retained centrally.
- Lesion audit/rerun only if lesion evidence is cited positively.
- Exp15 replay audit only if replay collapse is cited scientifically.
- Optional memory-augmented/broader neural baseline only if target venue or reviewer strategy requires it.

## 11. Recommended next action

Use `docs/manuscript/finalization/NEXT_STEP_PROMPT.md` for Analysis Pass 15A: decide retained main claims, map each retained claim to exact source CSVs, update statistical-readiness tables, and harden final source-data-backed figures/tables. Do not design another experiment unless the target venue or retained claim set requires it.
