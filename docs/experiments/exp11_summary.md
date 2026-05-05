# Experiment 11: Context-Separated Memory and Non-Destructive Rebinding

## Evidence status

- Local artifacts indexed: yes
- Local artifacts checked for key claims: partial
- Thread digest imported: yes; Exp11 result thread imported
- Human/manuscript validation pending: yes
- Claims fully validated for publication: no

## Status

- Code present: yes
- Analysis artifacts present: yes
- Validation present: yes
- Thread digest present: `docs/threads/experiment5to10_export.md`; `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`
- Manuscript relevance: Candidate main context-separated memory result after review.

## Purpose

Experiments 7-9 established a route-field mechanism: Experiment 10 showed adaptive rule reversal. A learned route field can be rebound when mode meanings change, and consolidation controls the stability-plasticity tradeoff. But the strongest ordinary reversal behavior was still mostly overwrite: new rule B replaced old rule A under the same context labels. Experiment 11 tests whether a higher-level world context allows multiple rule systems to coexist without destructive overwrite. A higher-order context signal can bind route fields into separable memory worlds, allowing the same mode labels to have different transition semantics in different task contexts. Train A, consolidate, then train B

Source path: `experiments/experiment11_context_memory/EXPERIMENT_11_CONTEXT_MEMORY.md`

## Hypothesis

TODO: Import the pre-run hypothesis from the relevant ChatGPT thread digest or local design document section. This first pass only consolidates local post-run artifacts.

## Experimental design

- Local source used for design: `experiments/experiment11_context_memory/EXPERIMENT_11_CONTEXT_MEMORY.md`
- Task/design clue: Experiments 7-9 established a route-field mechanism: Experiment 10 showed adaptive rule reversal. A learned route field can be rebound when mode meanings change, and consolidation controls the stability-plasticity tradeoff. But the strongest ordinary reversal behavior was still mostly overwrite: new rule B replaced old rule A under the same context labels. Experiment 11 tests whether a higher-level world context allows multiple rule systems to coexist without destructive overwrite. A higher-order context signal can bind route fields into separable memory worlds, allowing the same mode labels to have different transition semantics in different task contexts. Train A, consolidate, then train B
- Run scripts detected: `experiments/experiment11_context_memory/run_exp11_context_memory.py`, `experiments/experiment11_context_memory/run_exp11_suite.py`, `experiments/experiment11_context_memory/start.ps1`, `experiments/experiment11_context_memory/start.sh`, `experiments/experiment11_context_memory/start_exp11.ps1`
- Analysis CSVs detected: 22; plot files detected: 38; generated/design reports detected: 4.
- TODO: import thread digest for pre-run hypothesis, design rationale, and intended interpretation.

## Local report summary

- `experiments/experiment11_context_memory/EXPERIMENT_11_CONTEXT_MEMORY.md`: Experiments 7-9 established a route-field mechanism: Experiment 10 showed adaptive rule reversal. A learned route field can be rebound when mode meanings change, and consolidation controls the stability-plasticity tradeoff. But the strongest ordinary reversal behavior was still mostly overwrite: new rule B replaced old rule A under the same context labels. Experiment 11 tests whether a higher-level world context allo
- `experiments/experiment11_context_memory/TRACKER_UPDATE_EXP11.md`: Experiment 11 - Context-Separated Memory and Non-Destructive Rebinding Can higher-order world context separate multiple route systems over the same symbolic substrate so that new rule worlds can be learned without destroying old ones? Experiment 10 demonstrated adaptive route reversal and a clear stability-plasticity tradeoff. However, ordinary same-context reversal mostly overwrote old rules. The dual-context result
- `experiments/experiment11_context_memory/analysis/exp11/exp11_report.md`: Experiment 11 tests whether higher-order world context can separate multiple route systems over the same source/mode substrate. It measures old-world retention while a new world is learned, alternating-world stability, multi-world scaling, and retrieval robustness under world-context bleed/dropout. - `exp11_alternating_composition.png` - `exp11_alternating_route_table.png` - `exp11_alternating_world_margin.png` - `ex
- `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_report.md`: Experiment 11 tests whether higher-order world context can separate multiple route systems over the same source/mode substrate. It measures old-world retention while a new world is learned, alternating-world stability, multi-world scaling, and retrieval robustness under world-context bleed/dropout. - `exp11_alternating_composition.png` - `exp11_alternating_route_table.png` - `exp11_alternating_world_margin.png` - `ex

## Variants / ablations

| Variant | Intended mechanism tested | Expected behavior | Observed behavior | Source artifact |
| --- | --- | --- | --- | --- |
| exp11_full_context_separated_memory | Reference/full mechanism | TODO: import intended expectation from thread digest | A retention=1.0; B acquisition=1.0 | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv` |
| exp11_no_consolidation | Removes consolidation | TODO: import intended expectation from thread digest | A retention=1.0; B acquisition=1.0 | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv` |
| exp11_no_context_binding | Removes context or world indexing | TODO: import intended expectation from thread digest | A retention=0.0492; B acquisition=0.0545 | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv` |
| exp11_no_inhibition | Removes inhibitory route suppression | TODO: import intended expectation from thread digest | A retention=1.0; B acquisition=1.0 | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv` |
| exp11_no_recurrence | Removes recurrent multi-step execution | TODO: import intended expectation from thread digest | A retention=0.0; B acquisition=0.0 | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv` |
| exp11_no_structural_plasticity | Removes structural plasticity / route formation | TODO: import intended expectation from thread digest | A retention=0.0306; B acquisition=0.0283 | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv` |
| exp11_no_world_context | Removes context or world indexing | TODO: import intended expectation from thread digest | A retention=0.2895; B acquisition=1.0 | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv` |
| exp11_shared_edges_only | Forces shared edge substrate | TODO: import intended expectation from thread digest | A retention=0.2895; B acquisition=1.0 | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv` |
| exp11_strong_consolidation | Raises consolidation strength | TODO: import intended expectation from thread digest | A retention=1.0; B acquisition=1.0 | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv` |
| exp11_world_gated_plasticity | Restricts plastic updates by world | TODO: import intended expectation from thread digest | A retention=1.0; B acquisition=1.0 | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv` |

## Metrics

| Metric | Meaning | Where computed | Source artifact | Caveats |
| --- | --- | --- | --- | --- |
| composition_accuracy | Multi-step recurrent route execution accuracy. | Generated analysis CSV/report | `experiments/experiment11_context_memory/analysis/exp11/exp11_final_sequential_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| transition_accuracy | One-step route learning accuracy. | Generated analysis CSV/report | `experiments/experiment11_context_memory/analysis/exp11/exp11_final_sequential_summary.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| retention_A_after_B | Old-world/rule A retention after learning B. | Generated analysis CSV/report | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| acquisition_B_after_A | New-world/rule B acquisition after A. | Generated analysis CSV/report | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| world_margin_A_after_B | World margin for A after B learning. | Generated analysis CSV/report | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv` | Check aggregation, seeds, profile, and split before manuscript use. |
| world_margin_B_after_A | World margin for B after A learning. | Generated analysis CSV/report | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv` | Check aggregation, seeds, profile, and split before manuscript use. |

## Key results

### Result 1: Context-separated full model retains and acquires route systems locally

Claim: Exp11 memory indices report 1.0 retention of A after B and 1.0 acquisition of B after A for the full context-separated-memory variant.
Evidence: `exp11_full_context_separated_memory`: retention_A_after_B=1.0, acquisition_B_after_A=1.0, route_retention_A_after_B=1.0, route_acquisition_B_after_A=1.0.
Caveat: Synthetic world-context task; not a complete continual-learning solution.
Source path: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment11_context_memory/analysis/exp11/exp11_report.md`

### Result 2: No recurrence preserves route tables but loses sequential composition

Claim: The no-recurrence memory-index row has route retention/acquisition at 1.0 but composition retention/acquisition at 0.0.
Evidence: `exp11_no_recurrence`: retention_A_after_B=0.0, acquisition_B_after_A=0.0, route_retention_A_after_B=1.0, route_acquisition_B_after_A=1.0.
Caveat: Interpretation should remain benchmark-specific.
Source path: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`

### Result 3: No structural plasticity and no world context degrade memory indices

Claim: No-structural-plasticity is near zero and no-world-context is partial on A retention in the local memory-index table.
Evidence: `exp11_no_structural_plasticity`: retention_A_after_B=0.0306, acquisition_B_after_A=0.0283; `exp11_no_world_context`: retention_A_after_B=0.2895, acquisition_B_after_A=1.0.
Caveat: No-world-context still acquires B in this table; claims should be about interference/retention, not total failure.
Source path: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`

## What this experiment supports

- Local evidence summarized above; final supported-claim language must be imported into `docs/manuscript/CLAIMS_AND_EVIDENCE.md` after human/thread review.

## What this experiment does not prove

- Does not establish novelty by itself.
- Does not remove the need for baseline and reproducibility review.

## Known implementation or interpretation caveats

- Thread digest imported. Local artifacts have been partially checked for key claims. Manuscript-level validation and external baseline comparison remain pending.
- Check run profile, seeds, and aggregation before manuscript use.

## Artifacts

| Path | Type | Description | Manuscript relevance | Notes |
| --- | --- | --- | --- | --- |
| `experiments/experiment11_context_memory/README.md` | readme | Experiment README | medium | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/run_exp11_context_memory.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/run_exp11_suite.py` | script | Experiment runner | low | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/start.ps1` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/start.sh` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/start_exp11.ps1` | script | Launcher | low | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/EXPERIMENT_11_CONTEXT_MEMORY.md` | report | Supporting artifact | medium | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/TRACKER_UPDATE_EXP11.md` | report | Supporting artifact | medium | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11/exp11_report.md` | report | Generated report | medium | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_report.md` | report | Generated report | medium | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11/exp11_baseline_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11/exp11_failure_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11/exp11_final_sequential_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv` | summary_csv | Supporting artifact | high | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11/exp11_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11/metrics.csv` | metrics_csv | Primary metrics table | high | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11/metrics_wide.csv` | metrics_csv | Wide metrics table | high | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11/runs.csv` | summary_csv | Run manifest | high | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_baseline_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_failure_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_final_sequential_summary.csv` | summary_csv | Summary table | high | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_memory_indices.csv` | summary_csv | Supporting artifact | high | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11/exp11_alternating_composition.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11/exp11_alternating_route_table.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11/exp11_alternating_world_margin.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11/exp11_context_bleed_composition.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11/exp11_context_bleed_world_margin.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11/exp11_context_bleed_wrong_world_activation.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11/exp11_context_dropout_composition.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11/exp11_context_dropout_world_margin.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11/exp11_context_dropout_wrong_world_activation.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `experiments/experiment11_context_memory/analysis/exp11/exp11_failure_taxonomy_final_sequential.png` | plot | Plot image | high | Indexed locally; review before citing. |
| `docs/repo_audit/ARTIFACT_INDEX.csv` | index | 38 plot files total for this experiment | high | Use full index for exhaustive plot list. |

## Candidate manuscript figures

| Figure idea | Source image/data | Claim supported | Caveat |
| --- | --- | --- | --- |
| exp11 alternating composition | `experiments/experiment11_context_memory/analysis/exp11/exp11_alternating_composition.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp11 alternating route table | `experiments/experiment11_context_memory/analysis/exp11/exp11_alternating_route_table.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp11 alternating world margin | `experiments/experiment11_context_memory/analysis/exp11/exp11_alternating_world_margin.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp11 context bleed composition | `experiments/experiment11_context_memory/analysis/exp11/exp11_context_bleed_composition.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp11 context bleed world margin | `experiments/experiment11_context_memory/analysis/exp11/exp11_context_bleed_world_margin.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp11 context bleed wrong world activation | `experiments/experiment11_context_memory/analysis/exp11/exp11_context_bleed_wrong_world_activation.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp11 context dropout composition | `experiments/experiment11_context_memory/analysis/exp11/exp11_context_dropout_composition.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp11 context dropout world margin | `experiments/experiment11_context_memory/analysis/exp11/exp11_context_dropout_world_margin.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp11 context dropout wrong world activation | `experiments/experiment11_context_memory/analysis/exp11/exp11_context_dropout_wrong_world_activation.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp11 failure taxonomy final sequential | `experiments/experiment11_context_memory/analysis/exp11/exp11_failure_taxonomy_final_sequential.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp11 scaling final composition | `experiments/experiment11_context_memory/analysis/exp11/exp11_scaling_final_composition.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| exp11 scaling final route table | `experiments/experiment11_context_memory/analysis/exp11/exp11_scaling_final_route_table.png` | TODO: connect to reviewed claim. | Plot filename indicates relevance; inspect source data and plotting code. |
| Additional plots (26) | `docs/repo_audit/ARTIFACT_INDEX.csv` | TODO | See full artifact index. |

## Follow-up actions

- Import the relevant ChatGPT thread digest.
- Confirm which local run profile should be treated as canonical.
- Review source CSVs before upgrading any claim above local-only evidence.
- Update central claims/evidence rows if this experiment remains manuscript-relevant.

## Thread-derived analysis

### Analysis source: `docs/threads/experiment5to10_export.md`

Completed result / design / caveat / decision: Design decision.
Evidence: The thread designed Exp11 to test true context-separated memory after Exp10's ambiguous dual-context result.
Caveat: This earlier thread did not analyze full Exp11 local results.
Source thread: `docs/threads/experiment5to10_export.md`
Related local artifact path: `experiments/experiment11_context_memory/EXPERIMENT_11_CONTEXT_MEMORY.md`
Status: Design only

### Analysis source: `docs/threads/experiment11_export`

Completed result / design / caveat / decision: Completed result with caveat.
Evidence: The thread analyzes Exp11 full and world-gated variants retaining A while acquiring B; no-recurrence separates route-table memory from composition; no-structural-plasticity and no-world-context variants fail in interpretable ways.
Caveat: Synthetic task; no external baselines, no formal confidence intervals, and no capacity-limit proof in Exp11 alone.
Source thread: `docs/threads/experiment11_export`
Related local artifact path: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment11_context_memory/analysis/exp11/exp11_report.md`
Status: Strong

### Analysis source: `docs/threads/experiment12to13_export.md`

Completed result / design / caveat / decision: Manuscript framing decision.
Evidence: The thread treats Exp11 as the backbone of the narrowed claim: structural storage, contextual retrieval, and recurrent execution.
Caveat: Exp11 was not reanalyzed directly in that thread; rely on `docs/threads/experiment11_export` for Exp11 result details.
Source thread: `docs/threads/experiment12to13_export.md`
Related local artifact path: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`
Status: Strong

## Key results (thread-integrated)

### Result 1: Full model retains A and acquires B

Claim: Exp11 supports non-destructive retention across two incompatible route worlds in the tested symbolic regime.
Evidence: `exp11_full_context_separated_memory` has retention_A_after_B 1.0, acquisition_B_after_A 1.0, and route retention/acquisition 1.0.
Caveat: Oracle world context is supplied; broader continual-learning baselines are absent.
Source thread: `docs/threads/experiment11_export`
Source artifact: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`
Manuscript status: Strong

### Result 2: Recurrence separates storage from execution

Claim: Exp11 no-recurrence preserves route tables but fails composed behavior.
Evidence: `exp11_no_recurrence` has route_retention_A_after_B and route_acquisition_B_after_A at 1.0, while retention_A_after_B and acquisition_B_after_A are 0.0.
Caveat: Benchmark-specific; not a universal recurrence claim.
Source thread: `docs/threads/experiment11_export`
Source artifact: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment11_context_memory/analysis/exp11/exp11_sequential_route_table.png`
Manuscript status: Strong

### Result 3: No world context shows destructive interference

Claim: Without world context, Exp11 acquires B but loses much of A, consistent with collision/overwrite.
Evidence: `exp11_no_world_context` has acquisition_B_after_A 1.0 but retention_A_after_B about 0.2895; shared-edges-only has the same pattern in the thread.
Caveat: Phrase as retention/interference, not total failure.
Source thread: `docs/threads/experiment11_export`
Source artifact: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment11_context_memory/analysis/exp11/exp11_failure_taxonomy_final_sequential.png`
Manuscript status: Strong

### Result 4: Consolidation and inhibition are not essential in this clean regime

Claim: Exp11 does not support a claim that consolidation or inhibition is essential for clean context-separated memory.
Evidence: The thread and local memory indices show no-consolidation and no-inhibition variants at 1.0 retention/acquisition.
Caveat: They may matter under pressure, noise, or capacity limits.
Source thread: `docs/threads/experiment11_export`
Source artifact: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`
Manuscript status: Strong

## What this experiment supports (thread-integrated)

- Context-indexed incompatible-world memory in a synthetic route task.
- Structural storage, contextual selection, and recurrent execution decomposition.

## What this experiment does not prove (thread-integrated)

- It does not establish capacity limits.
- It does not prove consolidation or inhibition are generally necessary.
- It does not include external baselines or latent world inference.

## Follow-up actions (thread-integrated)

- Add seed-level intervals/effect sizes.
- Use Exp12/Exp13 for scaling and boundary claims.
