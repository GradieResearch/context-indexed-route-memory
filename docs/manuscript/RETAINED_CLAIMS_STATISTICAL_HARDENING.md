# Retained Claims and Statistical Hardening Pass 15A

Status: completed Analysis Pass 15A control document.

Purpose: record the retained V2 main-claim set after Experiment 15, map each retained claim to exact source CSVs, and separate manuscript-ready evidence from candidate/aggregate-only summaries that still need human-reviewed statistical grouping.

Controlling inputs:

- `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`
- `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/source_data/SOURCE_DATA_MANIFEST.csv`
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`
- `docs/manuscript/draft/MANUSCRIPT_V2.md`

## Retained V2 main-claim set

The retained manuscript spine is now:

| Claim ID | Retained role | Safe V2 wording | Primary source CSVs | Current statistical status | Remaining caveat |
|---|---|---|---|---|---|
| C1 | Main mechanism claim; Figure 2; Table 3 | Within this symbolic route-memory benchmark and tested CIRM-family ablations, structural route storage is required for reliable route-table formation and route execution. | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv` | Partial. Candidate Table 3 exists, but final seed-level grouping and effect-size selection still need review. | Do not state this as a universal requirement for all neural route-memory systems; Exp15 transition MLP variants solve the clean hard slice. |
| C2 | Main context/indexing claim; Figures 2 and 5; Table 4 caveat | Context/world indexing is required for incompatible local transitions and first-step/full-route disambiguation in this benchmark. | `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_seed_metrics.csv`; `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv` | Partial. Source-data-backed Exp15 Table 4 exists; C2-wide seed-level grouping remains human-review pending. | No-context neural suffix success means context necessity must be framed around conflict-sensitive first-step/full-route disambiguation, not every suffix transition. |
| C3 | Main recurrence/execution claim; Figure 2; Table 3 | Recurrent execution is required to compose stored one-step route memories into multi-step routes in the tested route-memory contracts. | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv` | Partial. Candidate aggregate-normal intervals exist; final seed-level comparison grouping remains pending. | Recurrence is not novel by itself; the retained claim is the storage/execution dissociation inside this benchmark. |
| C4 | Main decomposition claim; Figure 2; Table 4 | Route-table storage, endpoint memorization, and multi-step compositional execution are separable in this benchmark. | `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`; `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv` | Partial. Exp15 Table 4 is source-data-backed; C4-wide effect-size grouping still needs review. | Supports decomposition, not a universal architecture ranking. |
| C5 | Main clean-capacity claim; Figure 3; Table 3 | Under clean supplied context, the full model maintains ceiling route-table and composition accuracy through tested world counts. | `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/metrics.csv` | Partial. Aggregate source-data mirror and candidate intervals exist; no fitted capacity law is claimed. | Ceiling-limited result; avoid capacity-law language unless fitted. |
| C6 | Main finite-budget boundary claim; Figure 4; Table 3 | Finite structural budget produces an observed route-execution degradation curve. | `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `experiments/experiment13_breaking_point/analysis/metrics.csv` | Partial. Aggregate summaries and candidate intervals exist; seed-level/effect-size grouping still needs review. | Observed degradation curve only; no fitted law. |
| C13 | Main-narrow symbolic context-selection claim; Figure 5; Table 3 | The active symbolic world/context can be selected from partial transition-cue evidence before route execution. | `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_effect_sizes.csv`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_metrics.csv`; `docs/manuscript/source_data/figure_05_symbolic_context_selection.csv` | Partial. Candidate Figure 5/source data exist, and Exp14 effect-size artifact exists; exact manuscript comparison grouping still needs review. | Symbolic transition-cue selection only; not raw sensory latent-world discovery; oracle context-gated table remains an upper bound. |
| C12 | Discussion/table claim; Table 4 | Symbolic/algorithmic baselines and a minimal fixed-profile neural comparator are present, but baseline coverage is not exhaustive. | `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_effect_sizes.csv`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_effect_sizes.csv`; `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv` | Partial. Table 4 is source-data-backed; prior-art/citation import and optional broader neural-baseline decision remain open. | Exp15 is fixed-profile and non-exhaustive; memory-augmented/key-value neural baselines are omitted unless a target venue requires them. |

## Claims not retained as central V2 claims

| Claim ID / topic | Current handling | Reason |
|---|---|---|
| C7 local-vs-global pressure | Boundary evidence inside Figure 4 or supplement, not standalone main claim. | Paired seed-level local-vs-global inference remains pending. |
| C8 consolidation | Supplementary/stability-plasticity discussion only. | Evidence does not support a necessity or accuracy-rescue claim. |
| C9 seen-vs-unseen primitive boundary | Out of main claim set. | Seen/unseen/all metric cleanup is still required. |
| C10 context/cue corruption | Supplementary boundary evidence only. | Current evidence supports wrong-world or symbolic cue-evidence sensitivity, not generic stochastic robustness. |
| C11 continuous/noisy bridge | Supplement/future work. | Preliminary decoded/noisy symbolic bridge, not end-to-end perception. |
| Exp13.1 lesion diagnostic | Non-positive diagnostic; do not cite as positive mechanism evidence. | Targeted lesion behavior needs audit/rerun before positive use. |
| Exp15 replay collapse | Non-claim pending audit. | Could reflect implementation, training-regime, buffer, or undertraining issues. |
| Broad CIRM-over-neural claim | Dropped. | Exp15 context-conditioned transition MLP and world-head transition MLP solve the clean hard slice. |
| Raw latent-world discovery | Dropped. | Exp14 uses symbolic transition cues. |
| Biological validation | Dropped as a claim; inspiration only. | Current evidence is synthetic and symbolic. |

## Figure and table readiness decision

| Asset | Retained V2 placement | Status after Pass 15A | Required next action |
|---|---|---|---|
| Figure 1 conceptual schematic | Main | Candidate generated/source-data-backed as a schematic artifact. | Human-review labels and ensure non-claims are visible. |
| Figure 2 structural plasticity/context/recurrence ablation | Main | Candidate generated/source-data-backed; statistical grouping still needs review. | Human-review selected rows, captions, and Table 3 uncertainty language. |
| Figure 3 clean capacity scaling | Main | Candidate generated/source-data-backed; ceiling-limited. | Caption as ceiling-limited; do not add capacity-law language. |
| Figure 4 finite budget/local-global pressure | Main-narrow or supplement | Retain finite-budget degradation as C6; keep C7 local/global as caveated boundary only. | Add paired seed-level local/global analysis before making C7 a standalone claim. |
| Figure 5 symbolic transition-cue context selection | Retain as main-narrow for V2 hardening; movable to supplement by venue decision. | Candidate generated/source-data-backed; Exp14 effect-size artifact exists. | Caption as symbolic cue selection; state oracle upper-bound caveat. |
| Table 1 claim evidence | Main/supporting | Generated candidate table. | Human review of headline wording. |
| Table 2 run integrity | Main/supporting | Generated candidate table. | Human review of older-run provenance caveats. |
| Table 3 statistical summary | Main/supporting candidate, not final. | Existing generated table contains candidate aggregate-normal intervals and some unresolved effect-size/grouping gaps. | Do not cite as final until seed-level grouping/effect-size choices are reviewed. |
| Table 4 Exp15 neural comparator | Retain as compact main-text table for V2; movable to supplement by venue decision. | Source-data-backed hard-slice table exists. | Keep fixed-profile, replay, and provenance caveats in caption/prose. |
| Exp15 analysis plots | Supplementary analysis artifacts only. | Not promoted to final manuscript figures. | Do not cite as final figures unless regenerated as source-data-backed final assets. |

## Statistical hardening conclusion

This pass completes the retained-claim decision and source-path mapping, but it does not certify the statistical package as final. The repository now distinguishes:

- retained main claims: C1-C6 and C13;
- retained discussion/table baseline claim: C12;
- caveated boundary/supplement claims: C7, C8, C10, C11;
- out-of-main or non-claims: C9, Exp13.1 lesion evidence, Exp15 replay collapse, broad neural superiority, raw latent-world discovery, biological validation.

`docs/manuscript/tables/table_03_statistical_summary.md` remains a generated candidate statistical table. It should not be treated as final until the exact seed-level groupings and effect-size comparisons are human-reviewed for each retained claim.

## Next recommended action

Proceed to prior-art/citation hardening and human review of generated candidate figures/tables:

1. Verify V2 citation placeholders against real BibTeX metadata.
2. Import or recreate the missing novelty/prior-art source artifact if it is still relevant.
3. Human-review Figure 1-5 and Table 1-4 captions.
4. Decide whether target venue strategy requires a memory-augmented/key-value neural comparator.
5. Run fresh source-path verification after any caption/citation changes.
