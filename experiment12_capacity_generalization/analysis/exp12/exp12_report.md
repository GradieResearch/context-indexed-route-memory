# Experiment 12 Report - Capacity, Interference, and Compositional Generalization

## Purpose

Experiment 12 stress-tests the Experiment 11 mechanism by scaling the number of incompatible worlds, measuring continual retention after each new world, testing held-out multi-step compositions, and sweeping world-context noise plus consolidation strength.

## Run configuration

- profile: `full`
- seeds: `30`
- world counts: `[2, 4, 8, 16, 32]`
- route lengths: `[1, 2, 4, 8, 12]`
- nodes: `32`
- modes: `3`
- variants: `['exp12_full_context_separated_memory', 'exp12_world_gated_plasticity', 'exp12_no_consolidation', 'exp12_no_world_context', 'exp12_no_context_binding', 'exp12_no_recurrence', 'exp12_no_structural_plasticity', 'exp12_strong_consolidation']`
- elapsed seconds: `185.49`

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
| exp12_full_context_separated_memory |             2 |              1         |                    1         |              0          |                                 0.248408  |
| exp12_full_context_separated_memory |             4 |              1         |                    1         |              0          |                                 0.182343  |
| exp12_full_context_separated_memory |             8 |              1         |                    1         |              0          |                                 0.129625  |
| exp12_full_context_separated_memory |            16 |              1         |                    1         |              0          |                                 0.0920284 |
| exp12_full_context_separated_memory |            32 |              1         |                    1         |              0          |                                 0.0637515 |
| exp12_no_consolidation              |             2 |              1         |                    1         |              0          |                                 0.26564   |
| exp12_no_consolidation              |             4 |              1         |                    1         |              0          |                                 0.188731  |
| exp12_no_consolidation              |             8 |              1         |                    1         |              0          |                                 0.129592  |
| exp12_no_consolidation              |            16 |              1         |                    1         |              0          |                                 0.0889679 |
| exp12_no_consolidation              |            32 |              1         |                    1         |              0          |                                 0.0599892 |
| exp12_no_context_binding            |             2 |              1         |                    1         |              0          |                                 0.572252  |
| exp12_no_context_binding            |             4 |              1         |                    1         |              0          |                                 0.361284  |
| exp12_no_context_binding            |             8 |              1         |                    1         |              0          |                                 0.207946  |
| exp12_no_context_binding            |            16 |              1         |                    1         |              0          |                                 0.112774  |
| exp12_no_context_binding            |            32 |              1         |                    1         |              0          |                                 0.0591802 |
| exp12_no_recurrence                 |             2 |              0.0534722 |                    1         |              0.946528   |                                 0.248408  |
| exp12_no_recurrence                 |             4 |              0.0592882 |                    1         |              0.940712   |                                 0.182343  |
| exp12_no_recurrence                 |             8 |              0.0575087 |                    1         |              0.942491   |                                 0.129625  |
| exp12_no_recurrence                 |            16 |              0.0590495 |                    1         |              0.940951   |                                 0.0920284 |
| exp12_no_recurrence                 |            32 |              0.0565755 |                    1         |              0.943424   |                                 0.0637515 |
| exp12_no_structural_plasticity      |             2 |              0.0362847 |                    0.0322917 |             -0.00399306 |                                 0.5       |
| exp12_no_structural_plasticity      |             4 |              0.0356771 |                    0.0325521 |             -0.003125   |                                 0.250021  |
| exp12_no_structural_plasticity      |             8 |              0.0389323 |                    0.0304687 |             -0.00846354 |                                 0.125017  |
| exp12_no_structural_plasticity      |            16 |              0.0378906 |                    0.0310764 |             -0.00681424 |                                 0.0625108 |
| exp12_no_structural_plasticity      |            32 |              0.0375868 |                    0.0311089 |             -0.00647786 |                                 0.0312564 |
| exp12_no_world_context              |             2 |              0.519444  |                    0.513368  |             -0.00607639 |                                 0.5       |
| exp12_no_world_context              |             4 |              0.278646  |                    0.273872  |             -0.00477431 |                                 0.5       |
| exp12_no_world_context              |             8 |              0.161762  |                    0.153212  |             -0.00855035 |                                 0.5       |
| exp12_no_world_context              |            16 |              0.0976345 |                    0.0921224 |             -0.00551215 |                                 0.5       |
| exp12_no_world_context              |            32 |              0.0706055 |                    0.0609158 |             -0.00968967 |                                 0.5       |
| exp12_strong_consolidation          |             2 |              1         |                    1         |              0          |                                 0.160293  |
| exp12_strong_consolidation          |             4 |              1         |                    1         |              0          |                                 0.143493  |
| exp12_strong_consolidation          |             8 |              1         |                    1         |              0          |                                 0.127653  |
| exp12_strong_consolidation          |            16 |              1         |                    1         |              0          |                                 0.112235  |
| exp12_strong_consolidation          |            32 |              1         |                    1         |              0          |                                 0.0915713 |
| exp12_world_gated_plasticity        |             2 |              1         |                    1         |              0          |                                 0.226849  |
| exp12_world_gated_plasticity        |             4 |              1         |                    1         |              0          |                                 0.173813  |
| exp12_world_gated_plasticity        |             8 |              1         |                    1         |              0          |                                 0.129488  |
| exp12_world_gated_plasticity        |            16 |              1         |                    1         |              0          |                                 0.0961791 |
| exp12_world_gated_plasticity        |            32 |              1         |                    1         |              0          |                                 0.0690327 |

## Interpretation checklist

- Full and world-gated variants should preserve high composition accuracy as world count increases.
- No-recurrence should preserve one-step route-table accuracy but fail multi-step composition.
- No-world-context and shared-edges-only should show destructive overwriting as incompatible worlds accumulate.
- No-structural-plasticity should remain near chance.
- Consolidation should be interpreted as a pressure/modulation study, not assumed to be essential.