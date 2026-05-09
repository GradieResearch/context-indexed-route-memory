# Next Experiments / Next Work

## Repository-Readiness Context

P0/P1 repository-readiness work is sufficient for a conservative manuscript handoff, but not for submission. Exp13.2 has been imported as completed symbolic/algorithmic baseline evidence, Exp14 has been imported as completed symbolic transition-cue context-selection evidence, Exp15 has been imported as completed minimal neural comparator evidence, and `docs/manuscript/draft/MANUSCRIPT_V2.md` has been captured.

Claim: The immediate Exp15 execution/import and V2-capture items are closed; the next operational step is retained-claim selection, manuscript-grade statistical hardening, and final source-data-backed figure/table planning.

Evidence: `docs/threads/experiment15_analysis_digest.md` is imported, local artifacts for `exp15_full_20260508_092811` exist with validation PASS, `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md` exists, and `docs/manuscript/tables/table_04_exp15_neural_comparator.md` / `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv` exist.

Caveat: Exp15 provides minimal fixed-profile neural evidence, not exhaustive architecture search. The replay variant requires audit before scientific interpretation, and optional memory-augmented neural baselines remain a venue/reviewer decision.

Source path: `docs/manuscript/draft/MANUSCRIPT_V2.md`; `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`; `docs/threads/experiment15_analysis_digest.md`; `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`; `experiments/experiment15_neural_baseline_comparator/README.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/validation_report.md`; `docs/manuscript/tables/table_04_exp15_neural_comparator.md`.

## Immediate Order Of Operations

1. Use `docs/manuscript/finalization/NEXT_STEP_PROMPT.md` for Analysis Pass 15A.
2. Decide the retained main-claim set after V2 and post-Exp15 narrowing.
3. For each retained main claim, identify exact source CSVs and whether seed-level raw metrics are available.
4. Generate or update manuscript-grade CI/effect-size/statistical summaries where supported by local artifacts.
5. Update `docs/manuscript/tables/table_03_statistical_summary.md` and `docs/source_data/STATISTICAL_REPORTING_READINESS.csv` as evidence permits.
6. Decide final figure/table set, including Exp14 main-vs-supplement placement and whether Exp15 Table 4 stays main-text or moves to supplement.
7. Keep C9 out of the main claim set unless seen/unseen primitive metrics are cleaned.
8. Keep Exp15 replay collapse out of the scientific claim set unless audited.
9. Import prior-art/novelty sources and update related-work posture.
10. Verify retained experiment commands on a fresh checkout and document runtime/hardware expectations.

## Exp15 Neural Comparator

Purpose: Address the neural-baseline vulnerability without turning the first manuscript into an open-ended architecture search.

Implemented baseline families:

- GRU endpoint with context;
- GRU endpoint without context;
- GRU rollout with context;
- GRU rollout without context;
- small attention/Transformer-style endpoint model with context;
- one-step transition MLP with context;
- one-step transition MLP without context;
- sequential-world replay-trained transition MLP;
- parameter-isolated transition MLP with world-specific heads.

Verified local output from `exp15_full_20260508_092811`:

- `exp15_seed_metrics.csv`;
- `exp15_summary.csv`;
- `exp15_effect_sizes.csv`;
- `exp15_model_runtime.csv`;
- `run_manifest.json`;
- validation report;
- five diagnostic plots;
- compact V2 Table 4 source data under `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`.

Interpretation guardrail: Exp15 clarifies that ordinary fixed-profile neural comparators solve, fail, or partially solve different parts of the route-memory probe decomposition. It should not be described as exhaustive neural benchmarking or proof of neural-network superiority/inferiority.

## Exp13.1 Follow-Up

Purpose: Resolve caveats exposed by the completed Exp13.1 full run only if the manuscript needs those claims.

Follow-up goals:

- Audit targeted critical-edge lesion selection and rerun only if lesion evidence is needed.
- Add seed-level confidence intervals, effect sizes, and final figure scripts.
- Add explicit device/runtime metadata to future manifests, with CPU-only rationale if applicable.
- Preserve the main boundary questions: finite capacity, local capacity, recurrence dissociation, wrong-world context corruption, and consolidation pressure.

Source path: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/validation_report.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_lesion_metrics.csv`; `docs/threads/experiment13_1_analysis_digest.md`.

## Baseline Integration

Exp13.2 is complete and imported as a symbolic/algorithmic baseline suite. Exp15 is complete and imported as a minimal neural comparator. Together they partially resolve the baseline blocker for a controlled symbolic/mechanistic manuscript, but they do not replace prior-art/novelty import.

Claim: Baseline integration remains a manuscript-readiness issue until retained-claim statistics, final figure/table decisions, and prior-art/novelty positioning are complete.

Evidence: Exp13.2 includes oracle context-gated lookup, shared no-context lookup, endpoint memorization, recurrent controls, replay/LRU-style controls, hash/superposition controls, and parameter-isolation controls. Exp15 now adds completed minimal neural comparator results for GRU, Transformer-style endpoint, transition MLP, replay, and world-head variants.

Caveat: Neural-baseline evidence remains minimal and non-exhaustive. Exp15 omits a memory-augmented/key-value neural baseline, uses fixed small hyperparameters, and includes a replay variant that requires audit before interpretation.

Source path: `docs/manuscript/BASELINE_REQUIREMENTS.md`; `docs/experiments/exp13_2_summary.md`; `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`; `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`; `experiments/experiment15_neural_baseline_comparator/README.md`.

## Applied Bridge

Visual-state route memory should remain future work unless the first manuscript explicitly needs it.

Limitations:

- Current Exp13 bridge is not end-to-end perception.
- Applied bridge should wait until claim freeze, uncertainty reporting, final figure workflows, and target-venue baseline decisions are hardened.

Source path: `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv`; `docs/manuscript/LIMITATIONS_AND_THREATS.md`.

## Exp14 Follow-Up

Exp14 is complete and validated as symbolic transition-cue context selection. The immediate decision is manuscript placement rather than rerun.

Potential follow-up goals:

- Decide whether Exp14 is main-narrow Figure 5 or a supplementary result.
- Add final figure scripts and source-data mirrors if C13 remains main or supplement evidence.
- Add a short implementation/theory note for cue-count and synthetic corruption behavior if exact curves are interpreted.
- Build a successor only if the manuscript needs raw sensory, learned perceptual, or non-symbolic latent context discovery.

Source path: `docs/threads/experiment14_analysis_digest.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_report.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`.

## Do Not Start By Default

Do not start a new experiment by default. Revisit these only if retained claims, target venue, or reviewer strategy requires them:

- optional memory-augmented/key-value neural comparator;
- Exp15 replay implementation/training-regime audit;
- Exp13.1 lesion diagnostic audit/rerun;
- C9 seen/unseen primitive metric cleanup;
- stochastic context corruption / selection margin experiment;
- consolidation dose-response experiment;
- non-symbolic applied/perceptual bridge.
