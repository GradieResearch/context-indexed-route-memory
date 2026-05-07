# Project Status

## Current State

This repository contains self-contained experiment directories under `experiments/` plus manuscript, synthesis, source-data, and repo-audit documentation under `docs/`. Use the docs index and source-of-truth note for navigation before editing evidence-heavy files.

This status document reflects the current repository state after importing Exp14. Exp13.2 baseline alignment remains a separate unresolved pass, while Exp14 is now documented as completed symbolic latent-context evidence.

Source path: `docs/README.md`; `docs/manuscript/SOURCE_OF_TRUTH.md`; `docs/experiments/EXPERIMENT_REGISTRY.md`.

## Experiments Completed Or Used In Current Spine

- Exp1-Exp6: historical/exploratory and methodological precursor material.
- Exp7-Exp10: supporting mechanism-building experiments.
- Exp11: context-separated incompatible-world memory.
- Exp12: clean capacity, continual retention, and held-out composition scaling.
- Exp13: finite-capacity breaking point, context corruption, holdout boundary, and continuous bridge.
- Exp13.1: publication-hardening full run for recurrence, structural plasticity, context binding, budget/consolidation, freeze-plasticity, and lesion diagnostics.
- Exp14: latent symbolic context inference from partial transition cues, with smoke, validation, and full runs passing validation.

Source path: `docs/experiments/HISTORICAL_EXPERIMENTS.md`; `docs/experiments/EXPERIMENT_REGISTRY.md`.

## Main Scientific Findings So Far

Claim: Structural plasticity, world/context indexing, and recurrence form the current core mechanism inside the route-memory benchmark.
Evidence: Exp8, Exp11, Exp12, Exp13, and Exp13.1 ablations align with current summaries and local artifacts.
Caveat: This is internal evidence only; external baseline and prior-art integration remain pending in this pass.
Source path: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/threads/experiment12to13_export.md`; `docs/threads/experiment13_1_analysis_digest.md`.

Claim: Route-table storage and multi-step execution are separable.
Evidence: No-recurrence variants preserve route-table accuracy while composition fails in Exp11-Exp13.1.
Caveat: This is a route-memory benchmark claim, not a broad recurrence novelty claim.
Source path: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`.

Claim: Exp13 and Exp13.1 turn the story from ceiling performance into boundary mapping and publication hardening.
Evidence: Global/local budget pressure, adversarial or wrong-world context corruption, true primitive holdout, continuous-noise bridge artifacts, and Exp13.1 validation artifacts are present locally.
Caveat: Exp13.1 resolves some planned hardening but leaves lesion failure, uncertainty reporting, stochastic corruption, baseline integration, and final figure scripts open.
Source path: `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/validation_report.md`; `docs/manuscript/LIMITATIONS_AND_THREATS.md`.

Claim: Exp14 partially addresses the oracle context-label limitation by selecting symbolic worlds from transition cues.
Evidence: The full run passed validation and the hard clean slice reaches 1.0000 CIRM world selection and composition; the highest-corruption hard slice remains around 0.9416 while the oracle context-gated table remains an upper bound.
Caveat: This is symbolic cue inference, not raw sensory latent-world discovery or generic stochastic robustness.
Source path: `docs/threads/experiment14_analysis_digest.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_report.md`.

## Current Manuscript Readiness

Status: promising but not submission-ready.

The strongest internal story is coherent through Exp14, but Exp14 should be treated as a symbolic latent-context bridge until final figure/source-data work and manuscript placement are decided. The manuscript still needs a separate Exp13.2 import/alignment pass, prior-art positioning, uncertainty/effect-size reporting, final figure scripts, command verification, license/citation metadata, and a decision about whether lesion/holdout/stochastic corruption follow-ups are necessary.

Source path: `docs/synthesis/PUBLICATION_READINESS.md`; `docs/manuscript/MANUSCRIPT_TODO.md`.

## Largest Blockers

- Exp13.2 baseline integration is deferred to a separate pass.
- Exp14 main-vs-supplement placement and final figure/source-data work are unresolved.
- Seed-level confidence intervals and effect sizes are missing for core claims.
- Final figures need reproducible scripts and source-data manifests.
- Prior-art/novelty source import is incomplete.
- Exp13 holdout metrics require seen/unseen cleanup if retained centrally.
- Exp13.1 targeted lesion diagnostic failed the expected pattern.
- Context corruption evidence is wrong-world/context-identity sensitivity, not generic stochastic robustness.
- License and citation metadata are missing.

## Recommended Next Action

Decide whether Exp14 belongs in the main manuscript or supplement, proceed with the separate Exp13.2 analysis/import/alignment pass, then generate manuscript-grade CI/effect-size tables and final figure scripts.

Source path: `docs/synthesis/NEXT_EXPERIMENTS.md`; `docs/manuscript/MANUSCRIPT_TODO.md`; `docs/repo_audit/P0_P1_PUBLICATION_CLEANUP_REPORT.md`.
