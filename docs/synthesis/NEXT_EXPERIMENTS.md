# Next Experiments

## Repository-Readiness Context

P0/P1 repository-readiness work is sufficient for a conservative manuscript handoff, but not for submission. Exp13.2 has been imported as completed symbolic/algorithmic baseline evidence, and Exp14 has been imported as completed symbolic transition-cue context-selection evidence.

Claim: The next operational step is not another experiment by default. The next step is first-manuscript claim hardening, then final figure/table generation.

Evidence: `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md` freezes a conservative first-manuscript claim boundary; C13 is `Promising`; C12 is partially satisfied by symbolic/algorithmic baselines but still needs prior-art import and a target-venue neural-baseline decision.

Caveat: This does not make the repository submission-ready.

Source path: `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/manuscript/MANUSCRIPT_TODO.md`; `docs/synthesis/PUBLICATION_READINESS.md`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`; `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`; `docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md`.

## Immediate Order Of Operations

1. Use `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md` as the controlling input for first-manuscript scope.
2. Decide whether Exp14 C13 is main-text or supplement.
3. Decide whether the first submission target permits a controlled symbolic/mechanistic benchmark without neural baselines.
4. Generate manuscript-grade seed-level CI/effect-size tables for C1-C7 and C13 where retained.
5. Build final reproducible figure scripts and source-data manifests.
6. Import prior-art/novelty sources and update C12 discussion/related-work posture.
7. Verify Exp11, Exp12, Exp13, Exp13.1, Exp13.2, and retained Exp14 run commands on a fresh checkout.
8. Decide whether Exp13.1 lesion rerun, Exp13 holdout cleanup, stochastic context corruption, or neural baselines are necessary based on final manuscript claims and target venue.

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

Claim: Baseline integration remains a manuscript-readiness issue, but it is now a target-venue and prior-art issue rather than an unreviewed Exp13.2-artifact issue.

Evidence: Exp13.2 includes oracle context-gated lookup, shared no-context lookup, endpoint memorization, recurrent controls, replay/LRU-style controls, hash/superposition controls, and parameter-isolation controls. Oracle context-gated lookup matches CIRM on the clean supplied-context benchmark.

Caveat: Neural baselines are absent. If targeting a stronger ML venue, implement neural baselines before submission.

Source path: `docs/manuscript/BASELINE_REQUIREMENTS.md`; `docs/experiments/exp13_2_summary.md`; `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`.

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
