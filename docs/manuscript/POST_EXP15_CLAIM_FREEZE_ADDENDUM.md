# Post-Exp15 Claim Freeze Addendum

Status: active post-Exp15 claim-freeze addendum for Manuscript V2 hardening.

Purpose: narrow the first-manuscript claim posture after importing Experiment 15. This addendum supplements `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`; it does not replace the first freeze document. Use the narrower statement when the two documents differ.

## Addendum summary

Experiment 15 closes the "neural baselines are absent" limitation only in a minimal fixed-profile sense. It also narrows several claims because a context-conditioned neural transition MLP and a world-head transition MLP solve the clean hard slice at ceiling. The manuscript should therefore present CIRM as an interpretable mechanism and benchmark decomposition, not as broad evidence of CIRM superiority over neural models.

Recommended Exp15 placement for V2: compact main-text Table 4, with the option to move it to supplement during journal formatting or venue targeting.

Source table:

- `docs/manuscript/tables/table_04_exp15_neural_comparator.md`
- `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`

---

## C1 - Structural route storage

Claim -> Within this symbolic route-memory benchmark and tested CIRM-family ablations, structural route storage is required for reliable route-table formation and route execution.

Evidence -> CIRM ablations and symbolic baselines show collapse when structural route storage is removed.

Caveat -> Exp15 shows that `neural_transition_mlp_context` and `neural_transition_mlp_world_heads_context` solve the clean hard slice at 1.0000 across reported hard-slice metrics. Therefore C1 must not be worded as a universal requirement for all route-memory systems or all neural implementations.

Source path -> `docs/threads/experiment15_analysis_digest.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`; `docs/manuscript/tables/table_04_exp15_neural_comparator.md`.

## C2 - Context/world indexing

Claim -> Context/world indexing is required for deliberately incompatible local transitions and first-step/full-route disambiguation in this benchmark.

Evidence -> No-context variants fail conflict-sensitive first-step probes. At the hard slice, `neural_transition_mlp_no_context` has first-step context conflict accuracy 0.0312, while context-conditioned transition MLP and world-head transition MLP variants reach 1.0000.

Caveat -> `neural_transition_mlp_no_context` reaches 1.0000 suffix-route composition and 0.9193 transition accuracy at the same hard slice. Context necessity must therefore be framed around incompatible first-step/full-route disambiguation, not every suffix transition.

Source path -> `docs/threads/experiment15_analysis_digest.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`; `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`.

## C4 - Storage, endpoint memorization, and composition dissociation

Claim -> Endpoint memorization and reusable transition composition are separable.

Evidence -> At the hard slice, `neural_gru_endpoint_context` reaches 0.9990 seen-route composition but only 0.4040 suffix-route composition and 0.0232 transition accuracy. `neural_transformer_sequence_context` reaches 0.5435 seen-route composition, 0.1184 suffix-route composition, and 0.0070 transition accuracy.

Caveat -> Endpoint models and transition models optimize different objectives. This supports a decomposition claim, not a universal architecture ranking.

Source path -> `docs/threads/experiment15_analysis_digest.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`; `docs/manuscript/tables/table_04_exp15_neural_comparator.md`.

## C12 - Baseline coverage

Claim -> Minimal neural comparator coverage is now present.

Evidence -> Exp15 completed a fixed-profile neural comparator suite with 10 seeds, 9 variants, 5 metrics, and validation PASS for `exp15_full_20260508_092811`.

Caveat -> Exp15 is not exhaustive neural benchmarking. It uses fixed small models/hyperparameters, omits memory-augmented/key-value neural baselines, omits route length 16 from the default full profile, and includes a reconstructed-manifest/empty-SQLite-`run_manifest` provenance caveat.

Source path -> `docs/experiments/exp15_summary.md`; `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`; `docs/threads/experiment15_analysis_digest.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/validation_report.md`.

## C13 / Exp14 - Symbolic transition-cue context selection

Claim -> Exp14 supports selection of the active symbolic world/context from partial transition-cue evidence before route execution.

Evidence -> The hard clean Exp14 slice reaches ceiling world selection and composition, while corruption sweeps expose degradation boundaries.

Caveat -> Exp14 is symbolic transition-cue context selection. It is not raw sensory latent-world discovery, not end-to-end perception, and not a general latent-cause inference model. The oracle context-gated table remains an upper-bound control.

Source path -> `docs/threads/experiment14_analysis_digest.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `docs/manuscript/figures/figure_05_symbolic_context_selection.png`.

## Non-claim: Exp15 replay collapse

Claim -> None retained pending audit.

Evidence -> The replay variant shows near-zero hard-slice performance.

Caveat -> Treat this as an implementation/training-regime audit item. It may reflect a bug, insufficient replay buffer, undertraining, or a meaningful sequential-interference failure. Do not use it as general evidence that replay fails.

Source path -> `docs/threads/experiment15_analysis_digest.md`; `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`.

---

## Manuscript-language guardrails

Allowed:

- "minimal fixed-profile neural comparator"
- "context-conditioned transition learning solves the clean symbolic transition task"
- "endpoint memorization and reusable transition composition dissociate"
- "context is required for incompatible local transitions"
- "Exp14 selects symbolic context from transition cues"
- "CIRM is an interpretable route-memory mechanism and benchmark decomposition"

Avoid:

- "CIRM beats neural networks"
- "ordinary neural networks cannot solve route memory"
- "context is required for every suffix route"
- "Exp14 discovers latent worlds from raw data"
- "replay fails as a general method"
- "the benchmark proves a biological memory mechanism"
