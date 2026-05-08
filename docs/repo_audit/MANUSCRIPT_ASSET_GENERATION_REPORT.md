# Manuscript Asset Generation Report

## Summary

Generated reproducible first-manuscript candidate figures, source-data CSVs, and manuscript tables from local repository artifacts without rerunning experiments or modifying completed experimental outputs.

## Inputs inspected

- `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/synthesis/NEXT_EXPERIMENTS.md`
- `docs/experiments/EXPERIMENT_REGISTRY.md`
- `docs/threads/THREAD_INDEX.md`
- `docs/repo_audit/THREAD_IMPORT_CONFLICTS.md`
- `docs/repo_audit`
- `experiments/experiment11_context_memory/README.md`
- `experiments/experiment12_capacity_generalization/README.md`
- `experiments/experiment13_breaking_point/README.md`
- `experiments/experiment13_1_publication_hardening/README.md`
- `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_ablation_metrics.csv`
- `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/validation_results.json`
- `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`
- `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`
- `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv`
- `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`
- `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_effect_sizes.csv`
- `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/validation_results.json`
- `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`
- `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_effect_sizes.csv`
- `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_results.json`
- `docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md`
- `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`

## Generated source data

- `docs/manuscript/source_data/figure_01_conceptual_route_memory.csv` supports C1-C4 framing; C13 wording boundary from `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`; experiment READMEs.
- `docs/manuscript/source_data/figure_02_structural_plasticity_recurrence_ablation.csv` supports C1,C2,C3,C4 from `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_ablation_metrics.csv`.
- `docs/manuscript/source_data/figure_03_capacity_scaling.csv` supports C5 from `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`.
- `docs/manuscript/source_data/figure_04_finite_structural_budget_local_global.csv` supports C6,C7 from `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv`.
- `docs/manuscript/source_data/figure_05_symbolic_context_selection.csv` supports C13 from `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`.
- `docs/manuscript/source_data/table_exp13_2_symbolic_baseline_suite.csv` supports C2-C4/C12 from Exp13.2.

## Generated figures

- Figure 1 - Conceptual route-memory schematic: `docs/manuscript/figures/figure_01_conceptual_route_memory.png`; `docs/manuscript/figures/figure_01_conceptual_route_memory.svg` (generated candidate schematic). Caveat: Conceptual, not empirical evidence.
- Figure 2 - Structural plasticity and recurrence ablation: `docs/manuscript/figures/figure_02_structural_plasticity_recurrence_ablation.png`; `docs/manuscript/figures/figure_02_structural_plasticity_recurrence_ablation.svg` (generated candidate main figure). Caveat: Internal symbolic ablation; uncertainty uses aggregate normal approximation.
- Figure 3 - Clean capacity scaling: `docs/manuscript/figures/figure_03_capacity_scaling.png`; `docs/manuscript/figures/figure_03_capacity_scaling.svg` (generated candidate main figure). Caveat: Ceiling-limited clean supplied-context result; no fitted law.
- Figure 4 - Finite structural budget/local-global pressure: `docs/manuscript/figures/figure_04_finite_structural_budget_local_global.png`; `docs/manuscript/figures/figure_04_finite_structural_budget_local_global.svg` (generated candidate narrow-main/supplement figure). Caveat: Observed degradation curve only; paired seed-level local/global inference remains deferred.
- Figure 5 - Symbolic context selection from transition cues: `docs/manuscript/figures/figure_05_symbolic_context_selection.png`; `docs/manuscript/figures/figure_05_symbolic_context_selection.svg` (generated candidate main-or-supplement figure). Caveat: Symbolic transition-cue selection only; oracle remains an upper bound.

## Generated tables

- Table 1 - Claim evidence: `docs/manuscript/tables/table_01_claim_evidence.csv`; `docs/manuscript/tables/table_01_claim_evidence.md` (generated manuscript source table).
- Table 2 - Run integrity: `docs/manuscript/tables/table_02_run_integrity.csv`; `docs/manuscript/tables/table_02_run_integrity.md` (generated manuscript source table).
- Table 3 - Statistical summary: `docs/manuscript/tables/table_03_statistical_summary.csv`; `docs/manuscript/tables/table_03_statistical_summary.md` (generated manuscript source table).

## Claims covered

- C1, C2, C3, C4, C5, C6, C7, C13, and C12 discussion/readiness evidence are covered by generated source data and/or tables.

## Claims not covered

- C8 consolidation remains supplementary/preliminary and was not promoted into the generated main figure set.
- C9 seen-vs-unseen primitive boundary remains deferred pending metric cleanup.
- C10 context/cue corruption is represented only through Exp14 symbolic cue corruption; generic robustness is not claimed.
- C11 continuous/noisy bridge remains supplementary/future and was not generated as a main figure.

## Missing required artifacts

- None.

## Warnings and caveats

- Conflict recorded: Freeze document names Figure 4 as finite structural budget/local-vs-global pressure, while older prompt/figure-plan variants can describe a baseline-comparison Figure 4. This build follows the freeze document and writes Exp13.2 baseline evidence as source data and tables.
- Conflict recorded: Historical Figure Plan listed Exp14 as Figure 9 and Exp13.2 as deferred; this build follows the post-freeze main/candidate set and regenerates Exp14 as Figure 5 candidate evidence.
- Exp13.2 baseline outputs are symbolic/algorithmic only; neural baselines and prior-art/novelty import remain open.
- Exp14 wording is limited to symbolic context selection from partial transition evidence.
- Normal-approximate intervals are computed only where source artifacts provide aggregate std/count and do not already provide CI95 columns.

## Figure readiness status

| Figure | Status | Review need |
|---|---|---|
| Figure 1 - Conceptual route-memory schematic | generated candidate schematic | Human caption/layout review before manuscript submission. |
| Figure 2 - Structural plasticity and recurrence ablation | generated candidate main figure | Human caption/layout review before manuscript submission. |
| Figure 3 - Clean capacity scaling | generated candidate main figure | Human caption/layout review before manuscript submission. |
| Figure 4 - Finite structural budget/local-global pressure | generated candidate narrow-main/supplement figure | Human caption/layout review before manuscript submission. |
| Figure 5 - Symbolic context selection from transition cues | generated candidate main-or-supplement figure | Human caption/layout review before manuscript submission. |

## Verification result

Command run: `python scripts/verify_doc_source_paths.py`

Result: PASS. Files scanned: 105. OK paths: 5220. Missing active paths: 0. Skipped planned/future paths: 11. Skipped local-verification-pending paths: 43.

## Recommended next action

Human-review figure captions, decide Exp14 main-vs-supplement placement, decide controlled symbolic/mechanistic venue posture, and keep neural/prior-art/novelty gaps explicit before submission.
