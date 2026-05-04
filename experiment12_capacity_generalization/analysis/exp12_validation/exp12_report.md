# Experiment 12 Report - Capacity, Interference, and Compositional Generalization

## Purpose

Experiment 12 stress-tests the Experiment 11 mechanism by scaling the number of incompatible worlds, measuring continual retention after each new world, testing held-out multi-step compositions, and sweeping world-context noise plus consolidation strength.

## Run configuration

- profile: `validate`
- seeds: `2`
- world counts: `[2, 4]`
- route lengths: `[1, 2, 4]`
- nodes: `16`
- modes: `3`
- variants: `['exp12_full_context_separated_memory', 'exp12_world_gated_plasticity', 'exp12_no_world_context', 'exp12_no_recurrence', 'exp12_no_structural_plasticity']`
- elapsed seconds: `16.92`

## Generated files

- `metrics.csv`
- `runs.csv`
- `progress.jsonl`
- `exp12_final_memory_index.csv`
- `capacity_final_summary.csv`
- `continual_retention_summary.csv`
- `heldout_generalization_summary.csv`
- `context_bleed_summary.csv`
- `context_dropout_summary.csv`
- `consolidation_pressure_summary.csv`
- `plots/exp12_capacity_composition_accuracy.png`
- `plots/exp12_capacity_route_table_accuracy.png`
- `plots/exp12_capacity_wrong_world_activation.png`
- `plots/exp12_consolidation_pressure_accuracy.png`
- `plots/exp12_consolidation_pressure_world_margin.png`
- `plots/exp12_context_bleed_composition.png`
- `plots/exp12_context_bleed_world_margin.png`
- `plots/exp12_context_dropout_composition.png`
- `plots/exp12_context_dropout_world_margin.png`
- `plots/exp12_continual_retention_heatmap_full_model.png`
- `plots/exp12_heldout_generalization_by_length.png`
- `plots/exp12_route_table_composition_gap.png`

## Capacity snapshot

| run_name                            |   world_count |   composition_accuracy |   route_route_table_accuracy |   composition_route_gap |   composition_mean_wrong_world_activation |
|:------------------------------------|--------------:|-----------------------:|-----------------------------:|------------------------:|------------------------------------------:|
| exp12_full_context_separated_memory |             2 |              1         |                    1         |              0          |                                  0.251946 |
| exp12_full_context_separated_memory |             4 |              1         |                    1         |              0          |                                  0.20201  |
| exp12_no_recurrence                 |             2 |              0.0520833 |                    1         |              0.947917   |                                  0.251946 |
| exp12_no_recurrence                 |             4 |              0.0729167 |                    1         |              0.927083   |                                  0.20201  |
| exp12_no_structural_plasticity      |             2 |              0.0625    |                    0.0677083 |              0.00520833 |                                  0.499998 |
| exp12_no_structural_plasticity      |             4 |              0.0442708 |                    0.0572917 |              0.0130208  |                                  0.250021 |
| exp12_no_world_context              |             2 |              0.53125   |                    0.520833  |             -0.0104167  |                                  0.5      |
| exp12_no_world_context              |             4 |              0.307292  |                    0.299479  |             -0.0078125  |                                  0.5      |
| exp12_world_gated_plasticity        |             2 |              1         |                    1         |              0          |                                  0.230741 |
| exp12_world_gated_plasticity        |             4 |              1         |                    1         |              0          |                                  0.195375 |

## Interpretation checklist

- Full and world-gated variants should preserve high composition accuracy as world count increases.
- No-recurrence should preserve one-step route-table accuracy but fail multi-step composition.
- No-world-context and shared-edges-only should show destructive overwriting as incompatible worlds accumulate.
- No-structural-plasticity should remain near chance.
- Consolidation should be interpreted as a pressure/modulation study, not assumed to be essential.