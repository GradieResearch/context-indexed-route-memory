# Next Experiments

## Repository-Readiness Context

P0/P1 repository-readiness work is sufficient for a conservative manuscript handoff, but not for submission. Exp13.2 has been imported as completed symbolic/algorithmic baseline evidence, and Exp14 has been imported as completed symbolic transition-cue context-selection evidence.

Claim: The next operational step is Experiment 15 local execution and result import, not design of a new experiment.

Evidence: `experiments/experiment15_neural_baseline_comparator/` now contains an implementation-only neural comparator suite with validation/full launch scripts, analysis, validation, runtime metadata capture, and no checked-in result claims.

Caveat: Exp15 does not yet provide neural-baseline evidence. Paul still needs to run validation/full locally, upload the generated `analysis/exp15_full_*` artifacts, and import the analyzed results before manuscript claims are updated.

Source path: `docs/manuscript/finalization/NEXT_STEP_PROMPT.md`; `experiments/experiment15_neural_baseline_comparator/README.md`; `experiments/experiment15_neural_baseline_comparator/run_experiment15.py`; `experiments/experiment15_neural_baseline_comparator/validate_experiment15.py`.

## Immediate Order Of Operations

1. Run `experiments/experiment15_neural_baseline_comparator/start_exp15_validation.ps1` locally.
2. If validation passes, run `experiments/experiment15_neural_baseline_comparator/start_exp15_full.ps1` locally.
3. Upload the latest `analysis/exp15_full_*` directory in a separate analysis thread.
4. Produce an Exp15 analysis digest and decide whether neural results change the manuscript claim posture.
5. Import Exp15 results into the registry, baseline requirements, limitations, claim-freeze, and publication-readiness docs.
6. Generate manuscript-grade seed-level CI/effect-size tables for retained C1-C7, C13, and Exp15 neural-comparator claims if retained.
7. Build final reproducible figure scripts and source-data manifests.
8. Import prior-art/novelty sources and update C12 discussion/related-work posture.
9. Verify retained experiment commands on a fresh checkout.
10. Decide whether Exp13.1 lesion rerun, Exp13 holdout cleanup, stochastic context corruption, or other optional experiments are necessary based on final manuscript claims and target venue.

## Exp15 Neural Comparator

Purpose: Address the remaining neural-baseline vulnerability without turning the first manuscript into an open-ended architecture search.

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

Required local output after the full run:

- `exp15_seed_metrics.csv`;
- `exp15_summary.csv`;
- `exp15_effect_sizes.csv`;
- `exp15_model_runtime.csv`;
- `run_manifest.json`;
- validation report;
- five diagnostic plots.

Interpretation guardrail: Exp15 should clarify whether ordinary neural comparators solve, fail, or partially solve the route-memory probe decomposition. It should not be described as exhaustive neural benchmarking or proof of neural-network superiority/inferiority.

## Exp13.1 Follow-Up

Purpose: Resolve caveats exposed by the completed Exp13.1 full run only if the manuscript needs those claims.

Follow-up goals:

- Audit targeted critical-edge lesion selection and rerun only if lesion evidence is needed.
- Add seed-level confidence intervals, effect sizes, and final figure scripts.
- Add explicit device/runtime metadata to future manifests, with CPU-only rationale if applicable.
- Preserve the main boundary questions: finite capacity, local capacity, recurrence dissociation, wrong-world context corruption, and consolidation pressure.

Source path: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/validation_report.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_lesion_metrics.csv`; `docs/threads/experiment13_1_analysis_digest.md`.

## Baseline Integration

Exp13.2 is complete and imported as a symbolic/algorithmic baseline suite. It partially resolves the baseline blocker for a controlled symbolic/mechanistic manuscript, but it does not provide neural baselines and does not replace prior-art/novelty import.

Claim: Baseline integration remains a manuscript-readiness issue until Exp15 results and prior-art/novelty positioning are imported.

Evidence: Exp13.2 includes oracle context-gated lookup, shared no-context lookup, endpoint memorization, recurrent controls, replay/LRU-style controls, hash/superposition controls, and parameter-isolation controls. Exp15 implementation now provides the planned neural comparator suite, but no Exp15 result artifacts have been imported yet.

Caveat: Neural-baseline evidence remains absent until Paul runs Exp15 locally and imports the generated analysis.

Source path: `docs/manuscript/BASELINE_REQUIREMENTS.md`; `docs/experiments/exp13_2_summary.md`; `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`; `experiments/experiment15_neural_baseline_comparator/README.md`.

## Applied Bridge

Visual-state route memory should remain future work unless the first manuscript explicitly needs it.

Limitations:

- Current Exp13 bridge is not end-to-end perception.
- Applied bridge should wait until claim freeze, uncertainty reporting, final figure workflows, and target-venue baseline decisions are hardened.

Source path: `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv`; `docs/manuscript/LIMITATIONS_AND_THREATS.md`.

## Exp14 Follow-Up

Exp14 is complete and validated as symbolic transition-cue context selection. The immediate decision is manuscript placement rather than rerun.

Potential follow-up goals:

- Add final figure scripts and source-data mirrors if C13 becomes main or supplement evidence.
- Add a short implementation/theory note for cue-count and synthetic corruption behavior if exact curves are interpreted.
- Build a successor only if the manuscript needs raw sensory, learned perceptual, or non-symbolic latent context discovery.

Source path: `docs/threads/experiment14_analysis_digest.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_report.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`.
