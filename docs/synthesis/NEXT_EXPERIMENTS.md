# Next Experiments

## Repository-Readiness Context

P0/P1 repository-readiness work is sufficient for a conservative manuscript handoff, but not for submission. Exp14 has now been imported as a completed symbolic latent-context follow-up; Exp13.2 baseline alignment remains separate.

Claim: The next operational step is to decide Exp14 manuscript placement, complete the separate Exp13.2 analysis/import/alignment pass, and then perform statistical and figure hardening.
Evidence: C13 is now `Promising`, C12 remains `Needs baseline`, and the current audits identify missing CI/effect-size tables, final figure scripts, prior-art import, and command verification.
Caveat: This does not make the repository submission-ready.
Source path: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/manuscript/MANUSCRIPT_TODO.md`; `docs/synthesis/PUBLICATION_READINESS.md`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`; `docs/threads/experiment14_analysis_digest.md`

## Immediate Order Of Operations

1. Decide whether Exp14 C13 is main-text, supplement, or follow-up-only.
2. Complete the separate Exp13.2 import/alignment pass without relying on this cleanup report as baseline analysis.
3. Generate manuscript-grade seed-level CI/effect-size tables for C1-C13 where retained.
4. Build final reproducible figure scripts and source-data manifests.
5. Import prior-art/novelty sources and update C12.
6. Verify Exp11, Exp12, Exp13, Exp13.1, and retained Exp14 run commands on a fresh checkout.
7. Decide whether Exp13.1 lesion rerun, Exp13 holdout cleanup, or richer latent/noise follow-up is necessary based on final manuscript claims.

## Exp13.1 Follow-Up

Purpose: Resolve caveats exposed by the completed Exp13.1 full run if the manuscript needs those claims.

Follow-up goals:
- Audit targeted critical-edge lesion selection and rerun only if lesion evidence is needed.
- Add seed-level confidence intervals, effect sizes, and final figure scripts.
- Add explicit device/runtime metadata to future manifests, with CPU-only rationale if applicable.
- Preserve the main boundary questions: finite capacity, local capacity, recurrence dissociation, wrong-world context corruption, and consolidation pressure.

Source path: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/validation_report.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_lesion_metrics.csv`; `docs/threads/experiment13_1_analysis_digest.md`.

## Baseline Integration

Exp13.2 is intentionally deferred. Do not update claims, figures, or source-data manifests as if baseline work has been completed until the separate pass reviews the local artifacts and caveats.

Claim: Baseline integration remains a manuscript P0 blocker in this pass.
Evidence: `docs/manuscript/BASELINE_REQUIREMENTS.md` lists required baseline families, and C12 remains `Needs baseline`.
Caveat: This is a scope boundary for the current pass, not an analysis of Exp13.2 results.
Source path: `docs/manuscript/BASELINE_REQUIREMENTS.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md`

## Applied Bridge

Visual-state route memory should remain future work unless the first manuscript explicitly needs it.

Limitations:
- Current Exp13 bridge is not end-to-end perception.
- Applied bridge should wait until baseline integration, uncertainty reporting, and final figure workflows are hardened.

Source path: `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv`; `docs/manuscript/LIMITATIONS_AND_THREATS.md`

## Exp14 Follow-Up

Exp14 is complete and validated as symbolic transition-cue context selection. The immediate decision is manuscript placement rather than rerun.

Potential follow-up goals:
- Add final figure scripts and source-data mirrors if C13 becomes main or supplement evidence.
- Add a short implementation/theory note for cue-count and synthetic corruption behavior if exact curves are interpreted.
- Build a successor only if the manuscript needs raw sensory, learned perceptual, or non-symbolic latent context discovery.

Source path: `docs/threads/experiment14_analysis_digest.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_report.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`
