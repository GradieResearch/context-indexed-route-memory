# Limitations and Threats

Purpose: Track limitations, reviewer attack surfaces, and non-claims so the manuscript stays disciplined.

## Baseline Coverage Still Incomplete

Claim: Baseline and prior-art coverage remain incomplete in this cleanup pass.
Evidence: Current central evidence is internal to Exp11, Exp12, Exp13, and Exp13.1. `docs/manuscript/BASELINE_REQUIREMENTS.md` defines required baseline families but does not import Exp13.2 results in this pass.
Caveat: Exp13.2 is intentionally deferred to a separate analysis/import/alignment pass; do not mark C12 complete here.
Source path: `docs/manuscript/BASELINE_REQUIREMENTS.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
Proposed fix: Complete the separate Exp13.2 pass, import missing novelty/prior-art sources, and decide whether additional neural baselines are required.

## Symbolic Benchmark Limitation

Why it matters: Most evidence comes from synthetic route-memory tasks with symbolic nodes, modes, and supplied contexts.
Where identified: Exp6, Exp11, and Exp12-13 digests repeatedly warn against biological or broad applied overclaims.
Source thread path: `docs/threads/experiment6_export.md`; `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`.
Proposed fix: Keep claims benchmark-specific; use the continuous/noisy bridge only as preliminary until richer non-symbolic tasks exist.

## Oracle Context / World-Label Limitation

Why it matters: Many experiments provide world/context labels directly. This supports context-indexed storage, but not latent world inference.
Where identified: Exp11 and Exp12-13 framing; Exp14 completed the first symbolic cue-selection follow-up.
Source path: `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`; `docs/threads/experiment14_analysis_digest.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`.
Proposed fix: Use Exp14 only as symbolic transition-cue inference evidence. Keep the limitation that this is not raw sensory context discovery, and keep the oracle context-gated table as an upper bound rather than a defeated competitor.

## Latent Context Inference Remains Symbolic

Claim: Exp14 partially reduces the oracle-world-label limitation by selecting context from transition cues, but does not solve latent-world discovery.
Evidence: `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_report.md` reports PASS 27, WARN 0, FAIL 0, and `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv` supports clean hard-slice CIRM world selection and composition at 1.0000.
Caveat: The cues are symbolic transition evidence; the corruption process is synthetic; oracle context-gated lookup remains at 1.0000 under the hard corrupted slice.
Source path: `docs/threads/experiment14_analysis_digest.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_report.md`
Proposed fix: Decide whether Exp14 is main or supplement; if central, add final figure scripts/source-data mirrors and a short implementation note for cue-count/corruption behavior.

## Metric Cleanup Requirements

Why it matters: Reviewers can reject claims if metric definitions hide failure modes or combine incompatible cases.
Where identified: Exp13 holdout and no-context-binding caveats; Exp13.1 confidence-interval/effect-size and final-figure gaps.
Source thread path: `docs/threads/experiment12to13_export.md`; `docs/threads/experiment13_1_analysis_digest.md`.
Proposed fix: Add holdout seen-vs-unseen metric splits where relevant; report seed-level confidence intervals and effect sizes; generate final paper figures from reproducible scripts; keep Exp13.1 aggregate CSVs tied to authoritative experiment paths.

## Exp13.1 Lesion Diagnostic Failure

Claim: The current Exp13.1 targeted critical-edge lesion diagnostic should not be used as positive route-critical-structure evidence.
Evidence: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_lesion_metrics.csv` reports targeted lesion sensitivity about 0.0808 versus random count-matched lesion sensitivity about 0.5085.
Caveat: This may indicate a diagnostic implementation issue, a flawed critical-edge definition, or a task setting where the chosen targeted lesion does not isolate route-critical structure.
Source path: `docs/threads/experiment13_1_analysis_digest.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_lesion_metrics.csv`
Proposed fix: Audit critical-edge selection, verify matched lesion controls, and rerun before using lesion sensitivity as manuscript evidence.

## No Overclaiming Biological Theory

Why it matters: The model is biologically inspired, but the experiments do not validate a complete hippocampal or neural theory.
Where identified: Novelty/framing discussion in the Exp12-13 digest and earlier manuscript framing.
Source thread path: `docs/threads/experiment12to13_export.md`; `docs/threads/experiment11_export`.
Proposed fix: Use language such as "computationally inspired by indexing, remapping, recurrence, and structural plasticity"; avoid claims of biological explanation.

## Applied Bridge Remains Preliminary

Why it matters: Exp13 continuous/noisy input tests whether a decoded noisy start state can feed the route-memory mechanism, not whether the model learns perception end to end.
Where identified: Exp12-13 digest and Exp13 validation.
Source thread path: `docs/threads/experiment12to13_export.md`.
Proposed fix: Keep this as supplementary or preliminary unless a new applied visual-state route-memory experiment is run.

## Context Corruption Is Not Fully Realistic Yet

Claim: Exp13 adversarial context corruption and Exp13.1 wrong-world injection are useful failure evidence but not generic stochastic robustness tests.
Evidence: `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv` shows the full model collapses under adversarial mixture once wrong-world evidence dominates. `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_context_corruption.csv` shows wrong-world injection collapse at high corruption.
Caveat: Exp11/Exp12 context-noise artifacts are diagnostics only; Exp13.1 context dropout and bleed did not reduce composition accuracy.
Source path: `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`; `docs/threads/experiment12to13_export.md`; `docs/threads/experiment13_1_analysis_digest.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_context_corruption.csv`
Proposed fix: Add stochastic context corruption and report top-1 world selection, margins, and behavior across corruption probability.

## Consolidation Claim Is Fragile

Why it matters: Easy regimes do not require consolidation, Exp13 validation reports only a small finite-pressure consolidation delta, and Exp13.1 did not show an accuracy rescue from consolidation strength under constrained budgets.
Where identified: Exp10, Exp11, Exp12, Exp13, and Exp13.1 thread analyses.
Source thread path: `docs/threads/experiment5to10_export.md`; `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`; `docs/threads/experiment13_1_analysis_digest.md`.
Proposed fix: Frame consolidation as a stability-plasticity bias; use Exp13.1 freeze-plasticity only as a caveated internal diagnostic unless stronger dose-response or robustness evidence is added.

## Exp13.1 Reproducibility Metadata Gap

Why it matters: The run passed validation, but manuscript-grade reproducibility benefits from explicit device/runtime metadata.
Evidence: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/validation_report.md` reports PASS 27, WARN 0, FAIL 0, while `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/run_manifest.json` records configuration but not GPU/device/runtime metadata.
Caveat: The experiment is table-based and CPU-oriented, so missing GPU usage is not a computational failure; it is a documentation gap.
Source path: `docs/threads/experiment13_1_analysis_digest.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/validation_report.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/run_manifest.json`
Proposed fix: Add device/runtime metadata to future run manifests and explicitly document CPU-only rationale.

## License And Citation Metadata Missing

Why it matters: The repository currently lacks `LICENSE` and `CITATION.cff`.
Evidence: Local filesystem inspection in this cleanup pass found neither file at the repository root.
Caveat: Legal terms should be chosen by the human researcher; this pass does not invent a license.
Source path: `README.md`; `docs/repo_audit/P0_P1_PUBLICATION_CLEANUP_REPORT.md`
Proposed fix: Add a human-selected license and citation metadata before public release or manuscript submission.

## Non-Claims

- Do not claim solved continual learning.
- Do not claim context gating is novel by itself.
- Do not claim broad abstract rule induction.
- Do not claim end-to-end perception.
- Do not claim raw sensory latent-world discovery from Exp14.
- Do not claim consolidation is universally necessary.
- Do not use Exp13.1 lesion diagnostics as positive mechanism evidence unless audited and rerun.
- Do not use Exp13.2 to complete baseline claims until the separate Exp13.2 pass is done.
