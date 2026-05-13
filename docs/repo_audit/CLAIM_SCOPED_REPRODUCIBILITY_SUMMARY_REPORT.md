# Claim-Scoped Reproducibility Summary Report

Generated at: 2026-05-13T02:23:37+00:00

Generation command:

```bash
python scripts/build_claim_scoped_reproducibility_summary.py
```

## What Was Generated

- `docs/manuscript/source_data/reproducibility_claim_summary.csv`
- `docs/manuscript/source_data/seed_level_core_claim_metrics.csv`
- `docs/manuscript/tables/table_reproducibility_claim_summary.md`
- `docs/repo_audit/CLAIM_SCOPED_REPRODUCIBILITY_SUMMARY_REPORT.md`

The script only read committed artifacts. It did not rerun experiments and did not write inside any `experiments/` directory.

## Source Artifacts Parsed

| Path | Status | Rows/lines | Seed exposure |
|---|---:|---:|---|
| `docs/manuscript/source_data/manuscript_claim_artifact_map.csv` | parsed | 10 | no |
| `docs/manuscript/MANUSCRIPT_REPRODUCIBILITY_MAP.md` | parsed | 186 | no |
| `docs/repo_audit/MANUSCRIPT_REPRODUCIBILITY_PROTOCOL.md` | parsed | 237 | no |
| `docs/repo_audit/MANUSCRIPT_REPRODUCIBILITY_REPORT.md` | parsed | 80 | no |
| `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md` | parsed | 81 | no |
| `docs/source_data/STATISTICAL_REPORTING_READINESS.csv` | parsed | 14 | no |
| `docs/manuscript/tables/table_03_compact_final_safe.md` | parsed | 16 | no |
| `docs/manuscript/source_data/table_03_compact_final_safe.csv` | parsed | 4 | no |
| `docs/manuscript/tables/table_04_exp15_neural_comparator.md` | parsed | 30 | no |
| `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv` | parsed | 9 | no |
| `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv` | parsed | 200 | no |
| `experiments/experiment12_capacity_generalization/analysis/exp12/metrics.csv` | parsed | 477360 | yes (30 seeds) |
| `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | parsed | 640 | no |
| `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv` | parsed | 64 | no |
| `experiments/experiment13_breaking_point/analysis/metrics.csv` | parsed | 47015 | yes (5 seeds) |
| `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv` | parsed | 36 | no |
| `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_ablation_metrics.csv` | parsed | 43 | no |
| `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv` | parsed | 748 | no |
| `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_effect_sizes.csv` | parsed | 624 | no |
| `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv` | parsed | 2304 | no |
| `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_effect_sizes.csv` | parsed | 12288 | no |
| `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_metrics.csv` | parsed | 46080 | yes (20 seeds) |
| `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv` | parsed | 540 | no |
| `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_seed_metrics.csv` | parsed | 5400 | yes (10 seeds) |
| `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_effect_sizes.csv` | parsed | 1440 | no |

## Retained Claim Coverage

| Claim | Seed-level support | Aggregate-only or review limitation | Source path |
|---|---|---|---|
| C1 | Exp13.1 aggregate rows report n=20 per selected structure-audit variant; Exp13.2 aggregate n=20; Exp15 seed rows available for boundary context | descriptive_support_available; seed-level comparison grouping pending | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv` |
| C2 | 20 seeds from exp14_metrics.csv; 10 seeds from exp15_seed_metrics.csv; Exp13.2 is aggregate summary | partial_seed_level_support; comparison-family review pending | `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv` |
| C3 | Exp13.1 aggregate rows report n=20 per selected structure-audit variant; Exp13.2 aggregate n=20 | descriptive_support_available; seed-level comparison grouping pending | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv` |
| C4 | 20 seeds from exp14_metrics.csv; 10 seeds from exp15_seed_metrics.csv; Exp13.2 is aggregate summary | partial_seed_level_support; comparison-family review pending | `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv` |
| C5 | 30 seeds from metrics.csv | seed_level_descriptive_support_available | `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv` |
| C6 | 5 seeds from metrics.csv | seed_level_descriptive_support_available | `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` |
| C13 | 20 seeds from exp14_metrics.csv | seed_level_descriptive_support_available; effect-size artifact not promoted | `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv` |
| C12 | 10 seeds from exp15_seed_metrics.csv; Exp13.2 is aggregate summary | baseline_coverage_documented; non-exhaustive | `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv` |

## Claim Interpretations

### C1

Claim -> main mechanism claim.

Evidence -> Exp13.1 full model route_table_accuracy=1.000 and composition_accuracy=1.000; no structural plasticity route_table_accuracy=0.0286 and composition_accuracy=0.0317.

Caveat -> benchmark/model-family-specific; do not universalize to all neural route-memory systems

Source path -> `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`

### C2

Claim -> main context/indexing claim.

Evidence -> Context-sensitive first-step/full-route disambiguation is supported in selected symbolic and neural comparator slices; no-context suffix success is preserved as a caveat.

Caveat -> context necessity is conflict-specific; no-context suffix success prevents blanket context-required wording

Source path -> `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`

### C3

Claim -> main recurrence/execution claim.

Evidence -> Exp13.1 full model route_table_accuracy=1.000 and composition_accuracy=1.000; no recurrence at eval route_table_accuracy=1.000 but composition_accuracy=0.0401 at route_length=12.

Caveat -> recurrence itself is not novel; claim is storage/execution dissociation inside the benchmark

Source path -> `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`

### C4

Claim -> main decomposition claim.

Evidence -> Endpoint, transition, route-table, and composition metrics separate in Exp14/Exp15 slices; Table 4 remains fixed-profile and non-ranking.

Caveat -> decomposition claim only; not an architecture ranking

Source path -> `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`

### C5

Claim -> main clean-capacity claim.

Evidence -> Route-table and composition accuracy are 1.000 across the mirrored clean supplied-context grid used for Figure 3.

Caveat -> ceiling-limited through tested world counts only; no capacity law

Source path -> `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`

### C6

Claim -> main finite-budget boundary claim.

Evidence -> Composition accuracy rises from 0.276 at budget_ratio=0.25 to 0.517 at 0.50, 0.758 at 0.75, and 1.000 at exact/surplus budget levels.

Caveat -> observed degradation only; no fitted capacity law

Source path -> `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`

### C13

Claim -> main-narrow symbolic context-selection claim.

Evidence -> CIRM latent selector reaches 1.000 world-selection/seen-composition accuracy at corruption 0.00 and 0.10, 0.999 at 0.25, and 0.942 at 0.50. Oracle context-gated lookup remains 1.000. Shared no-context lookup fails first-step/seen-route metrics near chance while suffix probes can remain misleadingly high.

Caveat -> symbolic transition-cue selection only; not raw sensory latent-world discovery

Source path -> `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`

### C12

Claim -> discussion/table baseline claim.

Evidence -> Symbolic/algorithmic baselines and a minimal fixed-profile neural comparator are present; Table 4 shows transition MLP context/world-head variants solve the clean hard slice.

Caveat -> Exp15 is fixed-profile and non-exhaustive; replay collapse remains non-claim pending audit

Source path -> `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`

## Adequate Seed-Level Support

- C5 has seed-level Exp12 rows for clean supplied-context route-table and composition accuracy.
- C6 has seed-level Exp13 rows for finite structural-budget route-table and composition accuracy.
- C13 has seed-level Exp14 rows for symbolic cue-selected context metrics at the compact Table 3 slice.
- C12 has seed-level Exp15 fixed-profile neural comparator rows.
- C2 and C4 have partial seed-level support from Exp14 and Exp15, but their cross-experiment comparison families still need human review before inferential wording.

## Aggregate-Only Or Comparison-Family Pending Claims

- C1 and C3 rely heavily on Exp13.1 and Exp13.2 aggregate summaries for the current manuscript source set; no seed rows were fabricated from those aggregate files.
- C2 and C4 should remain descriptive until the exact cross-artifact comparison families are approved.
- C13 has an effect-size artifact, but this summary keeps effect-size language as `not_claimed` pending manuscript comparison-family approval.
- Compact Table 3 remains descriptive only.

## Boundary, Supplement, And Non-Claim Evidence

- Boundary/supplement only: C7 local-versus-global pressure, C8 consolidation/stability-plasticity discussion, C10 context/cue corruption sensitivity, C11 continuous/noisy bridge.
- Non-claims: C9 seen/unseen primitive boundary, Exp13.1 positive lesion evidence, Exp15 replay collapse, broad CIRM-over-neural claims, raw sensory latent-world discovery, biological validation.
- Exp15 replay collapse remains a non-claim pending implementation/training/buffer audit.

## Fresh Rerun Recommendation

No fresh expensive experiment rerun was performed or required for this PR. The next V3 drafting step can use the committed artifact package plus this summary. Before final submission, the author-facing `rerun-critical` pathway from `docs/repo_audit/MANUSCRIPT_REPRODUCIBILITY_PROTOCOL.md` remains recommended if time and hardware allow, especially if human statistical review changes comparison families.

## Manuscript Claim Posture

This generated summary does not widen the manuscript claim posture. It keeps C1 benchmark/model-family-specific, C2 conflict-specific, C5 ceiling-limited and supplied-context only, C6 descriptive with no capacity law, C13 symbolic-cue-only, and C12 fixed-profile/non-exhaustive. It does not promote boundary, supplement, or non-claim evidence into the retained main claim set.

Seed-level rows emitted: 11780.
