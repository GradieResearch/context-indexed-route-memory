# Manuscript Asset Manifest

## Generated command

`python scripts/manuscript_assets/build_manuscript_assets.py`

Generated at: `2026-05-08T06:23:37.850719+00:00`.

## Generated figures

| Figure | File(s) | Source data | Supports claim(s) | Source artifacts | Status | Caveat |
|---|---|---|---|---|---|---|
| Figure 1 - Conceptual route-memory schematic | `docs/manuscript/figures/figure_01_conceptual_route_memory.png`; `docs/manuscript/figures/figure_01_conceptual_route_memory.svg` | `docs/manuscript/source_data/figure_01_conceptual_route_memory.csv` | C1-C4 framing; C13 wording boundary | `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`; experiment READMEs | generated candidate schematic | Conceptual, not empirical evidence. |
| Figure 2 - Structural plasticity and recurrence ablation | `docs/manuscript/figures/figure_02_structural_plasticity_recurrence_ablation.png`; `docs/manuscript/figures/figure_02_structural_plasticity_recurrence_ablation.svg` | `docs/manuscript/source_data/figure_02_structural_plasticity_recurrence_ablation.csv` | C1,C2,C3,C4 | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_ablation_metrics.csv` | generated candidate main figure | Internal symbolic ablation; uncertainty uses aggregate normal approximation. |
| Figure 3 - Clean capacity scaling | `docs/manuscript/figures/figure_03_capacity_scaling.png`; `docs/manuscript/figures/figure_03_capacity_scaling.svg` | `docs/manuscript/source_data/figure_03_capacity_scaling.csv` | C5 | `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv` | generated candidate main figure | Ceiling-limited clean supplied-context result; no fitted law. |
| Figure 4 - Finite structural budget/local-global pressure | `docs/manuscript/figures/figure_04_finite_structural_budget_local_global.png`; `docs/manuscript/figures/figure_04_finite_structural_budget_local_global.svg` | `docs/manuscript/source_data/figure_04_finite_structural_budget_local_global.csv` | C6,C7 | `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv` | generated candidate narrow-main/supplement figure | Observed degradation curve only; paired seed-level local/global inference remains deferred. |
| Figure 5 - Symbolic context selection from transition cues | `docs/manuscript/figures/figure_05_symbolic_context_selection.png`; `docs/manuscript/figures/figure_05_symbolic_context_selection.svg` | `docs/manuscript/source_data/figure_05_symbolic_context_selection.csv` | C13 | `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv` | generated candidate main-or-supplement figure | Symbolic transition-cue selection only; oracle remains an upper bound. |

## Generated tables

| Table | File(s) | Source artifacts | Supports claim(s) | Status | Caveat |
|---|---|---|---|---|---|
| Table 1 - Claim evidence | `docs/manuscript/tables/table_01_claim_evidence.csv`; `docs/manuscript/tables/table_01_claim_evidence.md` | Frozen claim set plus generated source data. | C1-C7,C13,C12 | generated manuscript source table | Headline results are conservative summaries tied to source paths. |
| Table 2 - Run integrity | `docs/manuscript/tables/table_02_run_integrity.csv`; `docs/manuscript/tables/table_02_run_integrity.md` | Validation JSONs, manifests, metrics, summaries, plots, and run DB paths where present. | run provenance for C1-C7,C13 | generated manuscript source table | Older Exp11/Exp12 layouts lack validation JSON/SQLite manifests. |
| Table 3 - Statistical summary | `docs/manuscript/tables/table_03_statistical_summary.csv`; `docs/manuscript/tables/table_03_statistical_summary.md` | Generated figure source data and Exp13.2/Exp14 effect-size CSVs. | C1-C7,C13,C12 | generated manuscript source table | Effect-size grouping still needs human review before exact manuscript citation. |

## Missing or deferred assets

| Asset | Reason | Required action |
|---|---|---|
| Neural/prior-art baseline comparison figure | Freeze document keeps neural baselines and prior-art novelty import outside the current completed evidence. | Decide target venue and import prior-art/novelty sources before submission-readiness claims. |
| C8 consolidation figure | Freeze document recommends supplement-only/preliminary handling. | Generate only if supplement scope is approved and caption keeps the stability-plasticity caveat. |
| C9 seen/unseen primitive-boundary figure | Metric cleanup remains required. | Add seen/unseen/all route-table and composition split metrics before central use. |
| Positive lesion mechanism figure | Freeze document drops positive lesion evidence; Exp13.1 diagnostic failed expected pattern. | Do not cite positively unless audited and rerun in a successor/approved analysis. |
