# Experiment 13 Report - Breaking Point, Context Corruption, and Continuous Front-End Bridge

## Purpose

Experiment 13 deliberately pushes the Experiment 12 mechanism out of the ceiling regime. It asks where context-indexed structural route memory breaks when memory capacity, context integrity, primitive transition coverage, and perceptual input quality are degraded.

## Run configuration

- profile: `standard`
- seeds: `5`
- nodes: `32`
- modes: `3`
- capacity world counts: `[4, 8, 16, 32]`
- capacity route lengths: `[1, 4, 8, 12]`
- global budget ratios: `[0.25, 0.5, 0.75, 1.0, 1.25]`
- context corruption world count: `32`
- retention world count: `32`
- variants: `['exp13_full_context_separated_memory', 'exp13_world_gated_plasticity', 'exp13_no_consolidation', 'exp13_strong_consolidation', 'exp13_no_world_context', 'exp13_no_context_binding', 'exp13_no_recurrence', 'exp13_no_structural_plasticity']`
- elapsed seconds: `2112.24`

## Generated files

- `capacity_pressure_summary.csv`
- `context_corruption_summary.csv`
- `continual_retention_pressure_summary.csv`
- `continuous_frontend_bridge_summary.csv`
- `local_capacity_pressure_summary.csv`
- `metrics.csv`
- `runs.csv`
- `true_holdout_generalization_summary.csv`
- `plots/*.png`

## Capacity pressure snapshot

| run_name                            |   world_count |   route_length |   budget_ratio |   composition_accuracy_mean |   route_route_table_accuracy_mean |   composition_route_gap_mean |   top1_world_accuracy_mean |   used_edge_fraction_mean |
|:------------------------------------|--------------:|---------------:|---------------:|----------------------------:|----------------------------------:|-----------------------------:|---------------------------:|--------------------------:|
| exp13_full_context_separated_memory |             4 |             12 |           0.25 |                    0.267708 |                          0.281771 |                  0.0140625   |                          1 |                      0.25 |
| exp13_full_context_separated_memory |             4 |             12 |           0.5  |                    0.5125   |                          0.520312 |                  0.0078125   |                          1 |                      0.5  |
| exp13_full_context_separated_memory |             4 |             12 |           0.75 |                    0.754167 |                          0.759896 |                  0.00572917  |                          1 |                      0.75 |
| exp13_full_context_separated_memory |             4 |             12 |           1    |                    1        |                          1        |                  0           |                          1 |                      1    |
| exp13_full_context_separated_memory |             8 |             12 |           0.25 |                    0.26875  |                          0.277344 |                  0.00859375  |                          1 |                      0.25 |
| exp13_full_context_separated_memory |             8 |             12 |           0.5  |                    0.5125   |                          0.517969 |                  0.00546875  |                          1 |                      0.5  |
| exp13_full_context_separated_memory |             8 |             12 |           0.75 |                    0.754687 |                          0.761198 |                  0.00651042  |                          1 |                      0.75 |
| exp13_full_context_separated_memory |             8 |             12 |           1    |                    1        |                          1        |                  0           |                          1 |                      1    |
| exp13_full_context_separated_memory |            16 |             12 |           0.25 |                    0.269792 |                          0.272526 |                  0.00273437  |                          1 |                      0.25 |
| exp13_full_context_separated_memory |            16 |             12 |           0.5  |                    0.51224  |                          0.514844 |                  0.00260417  |                          1 |                      0.5  |
| exp13_full_context_separated_memory |            16 |             12 |           0.75 |                    0.75625  |                          0.757812 |                  0.0015625   |                          1 |                      0.75 |
| exp13_full_context_separated_memory |            16 |             12 |           1    |                    1        |                          1        |                  0           |                          1 |                      1    |
| exp13_full_context_separated_memory |            32 |             12 |           0.25 |                    0.275521 |                          0.272331 |                 -0.0031901   |                          1 |                      0.25 |
| exp13_full_context_separated_memory |            32 |             12 |           0.5  |                    0.517318 |                          0.514388 |                 -0.00292969  |                          1 |                      0.5  |
| exp13_full_context_separated_memory |            32 |             12 |           0.75 |                    0.757943 |                          0.757096 |                 -0.000846354 |                          1 |                      0.75 |
| exp13_full_context_separated_memory |            32 |             12 |           1    |                    1        |                          1        |                  0           |                          1 |                      1    |
| exp13_no_consolidation              |             4 |             12 |           0.25 |                    0.275    |                          0.278646 |                  0.00364583  |                          1 |                      0.25 |
| exp13_no_consolidation              |             4 |             12 |           0.5  |                    0.516667 |                          0.518229 |                  0.0015625   |                          1 |                      0.5  |
| exp13_no_consolidation              |             4 |             12 |           0.75 |                    0.761458 |                          0.756771 |                 -0.0046875   |                          1 |                      0.75 |
| exp13_no_consolidation              |             4 |             12 |           1    |                    1        |                          1        |                  0           |                          1 |                      1    |
| exp13_no_consolidation              |             8 |             12 |           0.25 |                    0.275    |                          0.273698 |                 -0.00130208  |                          1 |                      0.25 |
| exp13_no_consolidation              |             8 |             12 |           0.5  |                    0.517188 |                          0.516927 |                 -0.000260417 |                          1 |                      0.5  |
| exp13_no_consolidation              |             8 |             12 |           0.75 |                    0.760938 |                          0.757552 |                 -0.00338542  |                          1 |                      0.75 |
| exp13_no_consolidation              |             8 |             12 |           1    |                    1        |                          1        |                  0           |                          1 |                      1    |
| exp13_no_consolidation              |            16 |             12 |           0.25 |                    0.272656 |                          0.271745 |                 -0.000911458 |                          1 |                      0.25 |
| exp13_no_consolidation              |            16 |             12 |           0.5  |                    0.516667 |                          0.514714 |                 -0.00195312  |                          1 |                      0.5  |
| exp13_no_consolidation              |            16 |             12 |           0.75 |                    0.759115 |                          0.757031 |                 -0.00208333  |                          1 |                      0.75 |
| exp13_no_consolidation              |            16 |             12 |           1    |                    1        |                          1        |                  0           |                          1 |                      1    |
| exp13_no_consolidation              |            32 |             12 |           0.25 |                    0.276562 |                          0.272917 |                 -0.00364583  |                          1 |                      0.25 |
| exp13_no_consolidation              |            32 |             12 |           0.5  |                    0.517188 |                          0.515625 |                 -0.0015625   |                          1 |                      0.5  |
| exp13_no_consolidation              |            32 |             12 |           0.75 |                    0.758984 |                          0.757682 |                 -0.00130208  |                          1 |                      0.75 |
| exp13_no_consolidation              |            32 |             12 |           1    |                    1        |                          1        |                  0           |                          1 |                      1    |
| exp13_no_context_binding            |             4 |             12 |           0.25 |                    0.267708 |                          0.281771 |                  0.0140625   |                          1 |                      0.25 |
| exp13_no_context_binding            |             4 |             12 |           0.5  |                    0.5125   |                          0.520312 |                  0.0078125   |                          1 |                      0.5  |
| exp13_no_context_binding            |             4 |             12 |           0.75 |                    0.754167 |                          0.759896 |                  0.00572917  |                          1 |                      0.75 |
| exp13_no_context_binding            |             4 |             12 |           1    |                    1        |                          1        |                  0           |                          1 |                      1    |
| exp13_no_context_binding            |             8 |             12 |           0.25 |                    0.26875  |                          0.277344 |                  0.00859375  |                          1 |                      0.25 |
| exp13_no_context_binding            |             8 |             12 |           0.5  |                    0.5125   |                          0.517969 |                  0.00546875  |                          1 |                      0.5  |
| exp13_no_context_binding            |             8 |             12 |           0.75 |                    0.754687 |                          0.761198 |                  0.00651042  |                          1 |                      0.75 |
| exp13_no_context_binding            |             8 |             12 |           1    |                    1        |                          1        |                  0           |                          1 |                      1    |

## Adversarial context corruption snapshot

| run_name                            |   context_corruption_level |   composition_accuracy_mean |   top1_world_accuracy_mean |   composition_mean_world_margin_mean |   composition_mean_wrong_world_activation_mean |
|:------------------------------------|---------------------------:|----------------------------:|---------------------------:|-------------------------------------:|-----------------------------------------------:|
| exp13_full_context_separated_memory |                       0    |                   1         |                          1 |                                1     |                                         0      |
| exp13_full_context_separated_memory |                       0.1  |                   1         |                          1 |                                0.8   |                                         0.1    |
| exp13_full_context_separated_memory |                       0.25 |                   1         |                          1 |                                0.5   |                                         0.25   |
| exp13_full_context_separated_memory |                       0.4  |                   1         |                          1 |                                0.2   |                                         0.4    |
| exp13_full_context_separated_memory |                       0.49 |                   1         |                          1 |                                0.02  |                                         0.49   |
| exp13_full_context_separated_memory |                       0.51 |                   0.0317708 |                          0 |                               -0.02  |                                         0.51   |
| exp13_full_context_separated_memory |                       0.6  |                   0.0317708 |                          0 |                               -0.2   |                                         0.6    |
| exp13_full_context_separated_memory |                       0.75 |                   0.0317708 |                          0 |                               -0.5   |                                         0.75   |
| exp13_full_context_separated_memory |                       0.9  |                   0.0317708 |                          0 |                               -0.8   |                                         0.9    |
| exp13_full_context_separated_memory |                       0.99 |                   0.0317708 |                          0 |                               -0.98  |                                         0.99   |
| exp13_no_consolidation              |                       0    |                   1         |                          1 |                                0.95  |                                         0      |
| exp13_no_consolidation              |                       0.1  |                   1         |                          1 |                                0.76  |                                         0.095  |
| exp13_no_consolidation              |                       0.25 |                   1         |                          1 |                                0.475 |                                         0.2375 |
| exp13_no_consolidation              |                       0.4  |                   1         |                          1 |                                0.19  |                                         0.38   |
| exp13_no_consolidation              |                       0.49 |                   1         |                          1 |                                0.019 |                                         0.4655 |
| exp13_no_consolidation              |                       0.51 |                   0.0317708 |                          0 |                               -0.019 |                                         0.4845 |
| exp13_no_consolidation              |                       0.6  |                   0.0317708 |                          0 |                               -0.19  |                                         0.57   |
| exp13_no_consolidation              |                       0.75 |                   0.0317708 |                          0 |                               -0.475 |                                         0.7125 |
| exp13_no_consolidation              |                       0.9  |                   0.0317708 |                          0 |                               -0.76  |                                         0.855  |
| exp13_no_consolidation              |                       0.99 |                   0.0317708 |                          0 |                               -0.931 |                                         0.9405 |
| exp13_no_context_binding            |                       0    |                   1         |                          1 |                                0.15  |                                         0      |
| exp13_no_context_binding            |                       0.1  |                   1         |                          1 |                                0.12  |                                         0.015  |
| exp13_no_context_binding            |                       0.25 |                   1         |                          1 |                                0.075 |                                         0.0375 |
| exp13_no_context_binding            |                       0.4  |                   1         |                          1 |                                0.03  |                                         0.06   |
| exp13_no_context_binding            |                       0.49 |                   1         |                          1 |                                0.003 |                                         0.0735 |
| exp13_no_context_binding            |                       0.51 |                   0.0317708 |                          0 |                               -0.003 |                                         0.0765 |
| exp13_no_context_binding            |                       0.6  |                   0.0317708 |                          0 |                               -0.03  |                                         0.09   |
| exp13_no_context_binding            |                       0.75 |                   0.0317708 |                          0 |                               -0.075 |                                         0.1125 |
| exp13_no_context_binding            |                       0.9  |                   0.0317708 |                          0 |                               -0.12  |                                         0.135  |
| exp13_no_context_binding            |                       0.99 |                   0.0317708 |                          0 |                               -0.147 |                                         0.1485 |
| exp13_no_recurrence                 |                       0    |                   0.0395833 |                          1 |                                1     |                                         0      |
| exp13_no_recurrence                 |                       0.1  |                   0.0395833 |                          1 |                                0.8   |                                         0.1    |
| exp13_no_recurrence                 |                       0.25 |                   0.0395833 |                          1 |                                0.5   |                                         0.25   |
| exp13_no_recurrence                 |                       0.4  |                   0.0395833 |                          1 |                                0.2   |                                         0.4    |
| exp13_no_recurrence                 |                       0.49 |                   0.0395833 |                          1 |                                0.02  |                                         0.49   |
| exp13_no_recurrence                 |                       0.51 |                   0.0291667 |                          0 |                               -0.02  |                                         0.51   |
| exp13_no_recurrence                 |                       0.6  |                   0.0291667 |                          0 |                               -0.2   |                                         0.6    |
| exp13_no_recurrence                 |                       0.75 |                   0.0291667 |                          0 |                               -0.5   |                                         0.75   |
| exp13_no_recurrence                 |                       0.9  |                   0.0291667 |                          0 |                               -0.8   |                                         0.9    |
| exp13_no_recurrence                 |                       0.99 |                   0.0291667 |                          0 |                               -0.98  |                                         0.99   |

## True holdout snapshot

| run_name                            | generalization_condition           |   primitive_holdout_rate |   route_length |   composition_accuracy_mean |   route_route_table_accuracy_mean |   composition_route_gap_mean |
|:------------------------------------|:-----------------------------------|-------------------------:|---------------:|----------------------------:|----------------------------------:|-----------------------------:|
| exp13_full_context_separated_memory | one_step_unseen_primitives         |                      0.1 |              1 |                   0.0270833 |                          0.902214 |                    0.87513   |
| exp13_full_context_separated_memory | one_step_unseen_primitives         |                      0.2 |              1 |                   0.0354167 |                          0.806771 |                    0.771354  |
| exp13_full_context_separated_memory | one_step_unseen_primitives         |                      0.4 |              1 |                   0.0346354 |                          0.612109 |                    0.577474  |
| exp13_full_context_separated_memory | one_step_unseen_primitives         |                      0.6 |              1 |                   0.0273438 |                          0.419271 |                    0.391927  |
| exp13_full_context_separated_memory | compositions_from_seen_primitives  |                      0   |              8 |                   1         |                          1        |                    0         |
| exp13_full_context_separated_memory | compositions_from_seen_primitives  |                      0.1 |              8 |                   1         |                          0.902214 |                   -0.0977865 |
| exp13_full_context_separated_memory | compositions_from_seen_primitives  |                      0.2 |              8 |                   1         |                          0.806771 |                   -0.193229  |
| exp13_full_context_separated_memory | compositions_from_seen_primitives  |                      0.4 |              8 |                   1         |                          0.612109 |                   -0.387891  |
| exp13_full_context_separated_memory | compositions_from_seen_primitives  |                      0.6 |              8 |                   0.677344  |                          0.419271 |                   -0.258073  |
| exp13_full_context_separated_memory | routes_requiring_unseen_primitives |                      0.1 |              8 |                   0.114323  |                          0.902214 |                    0.787891  |
| exp13_full_context_separated_memory | routes_requiring_unseen_primitives |                      0.2 |              8 |                   0.103125  |                          0.806771 |                    0.703646  |
| exp13_full_context_separated_memory | routes_requiring_unseen_primitives |                      0.4 |              8 |                   0.0757812 |                          0.612109 |                    0.536328  |
| exp13_full_context_separated_memory | routes_requiring_unseen_primitives |                      0.6 |              8 |                   0.0450521 |                          0.419271 |                    0.374219  |
| exp13_no_consolidation              | one_step_unseen_primitives         |                      0.1 |              1 |                   0.0270833 |                          0.902214 |                    0.87513   |
| exp13_no_consolidation              | one_step_unseen_primitives         |                      0.2 |              1 |                   0.0354167 |                          0.806771 |                    0.771354  |
| exp13_no_consolidation              | one_step_unseen_primitives         |                      0.4 |              1 |                   0.0346354 |                          0.612109 |                    0.577474  |
| exp13_no_consolidation              | one_step_unseen_primitives         |                      0.6 |              1 |                   0.0273438 |                          0.419271 |                    0.391927  |
| exp13_no_consolidation              | compositions_from_seen_primitives  |                      0   |              8 |                   1         |                          1        |                    0         |
| exp13_no_consolidation              | compositions_from_seen_primitives  |                      0.1 |              8 |                   1         |                          0.902214 |                   -0.0977865 |
| exp13_no_consolidation              | compositions_from_seen_primitives  |                      0.2 |              8 |                   1         |                          0.806771 |                   -0.193229  |
| exp13_no_consolidation              | compositions_from_seen_primitives  |                      0.4 |              8 |                   1         |                          0.612109 |                   -0.387891  |
| exp13_no_consolidation              | compositions_from_seen_primitives  |                      0.6 |              8 |                   0.677344  |                          0.419271 |                   -0.258073  |
| exp13_no_consolidation              | routes_requiring_unseen_primitives |                      0.1 |              8 |                   0.114323  |                          0.902214 |                    0.787891  |
| exp13_no_consolidation              | routes_requiring_unseen_primitives |                      0.2 |              8 |                   0.103125  |                          0.806771 |                    0.703646  |
| exp13_no_consolidation              | routes_requiring_unseen_primitives |                      0.4 |              8 |                   0.0757812 |                          0.612109 |                    0.536328  |
| exp13_no_consolidation              | routes_requiring_unseen_primitives |                      0.6 |              8 |                   0.0450521 |                          0.419271 |                    0.374219  |
| exp13_no_recurrence                 | one_step_unseen_primitives         |                      0.1 |              1 |                   0.0270833 |                          0.902214 |                    0.87513   |
| exp13_no_recurrence                 | one_step_unseen_primitives         |                      0.2 |              1 |                   0.0354167 |                          0.806771 |                    0.771354  |
| exp13_no_recurrence                 | one_step_unseen_primitives         |                      0.4 |              1 |                   0.0346354 |                          0.612109 |                    0.577474  |
| exp13_no_recurrence                 | one_step_unseen_primitives         |                      0.6 |              1 |                   0.0273438 |                          0.419271 |                    0.391927  |
| exp13_no_recurrence                 | compositions_from_seen_primitives  |                      0   |              8 |                   0.0377604 |                          1        |                    0.96224   |
| exp13_no_recurrence                 | compositions_from_seen_primitives  |                      0.1 |              8 |                   0.0484375 |                          0.902214 |                    0.853776  |
| exp13_no_recurrence                 | compositions_from_seen_primitives  |                      0.2 |              8 |                   0.0455729 |                          0.806771 |                    0.761198  |
| exp13_no_recurrence                 | compositions_from_seen_primitives  |                      0.4 |              8 |                   0.0375    |                          0.612109 |                    0.574609  |
| exp13_no_recurrence                 | compositions_from_seen_primitives  |                      0.6 |              8 |                   0.0208333 |                          0.419271 |                    0.398438  |
| exp13_no_recurrence                 | routes_requiring_unseen_primitives |                      0.1 |              8 |                   0.0335937 |                          0.902214 |                    0.86862   |
| exp13_no_recurrence                 | routes_requiring_unseen_primitives |                      0.2 |              8 |                   0.0395833 |                          0.806771 |                    0.767188  |
| exp13_no_recurrence                 | routes_requiring_unseen_primitives |                      0.4 |              8 |                   0.0369792 |                          0.612109 |                    0.57513   |
| exp13_no_recurrence                 | routes_requiring_unseen_primitives |                      0.6 |              8 |                   0.0341146 |                          0.419271 |                    0.385156  |
| exp13_no_world_context              | one_step_unseen_primitives         |                      0.1 |              1 |                   0.0294271 |                          0.147526 |                    0.118099  |

## Continuous front-end bridge snapshot

| run_name                            |   continuous_noise |   composition_accuracy_mean |   decoded_start_accuracy_observed_mean |   top1_world_accuracy_mean |
|:------------------------------------|-------------------:|----------------------------:|---------------------------------------:|---------------------------:|
| exp13_full_context_separated_memory |               0    |                   1         |                               1        |                          1 |
| exp13_full_context_separated_memory |               0.05 |                   1         |                               1        |                          1 |
| exp13_full_context_separated_memory |               0.1  |                   1         |                               1        |                          1 |
| exp13_full_context_separated_memory |               0.2  |                   0.991146  |                               0.988542 |                          1 |
| exp13_full_context_separated_memory |               0.35 |                   0.792448  |                               0.740104 |                          1 |
| exp13_full_context_separated_memory |               0.5  |                   0.579948  |                               0.467708 |                          1 |
| exp13_full_context_separated_memory |               0.75 |                   0.421094  |                               0.26276  |                          1 |
| exp13_full_context_separated_memory |               1    |                   0.347135  |                               0.169792 |                          1 |
| exp13_no_recurrence                 |               0    |                   0.0354167 |                               1        |                          1 |
| exp13_no_recurrence                 |               0.05 |                   0.0354167 |                               1        |                          1 |
| exp13_no_recurrence                 |               0.1  |                   0.0385417 |                               1        |                          1 |
| exp13_no_recurrence                 |               0.2  |                   0.0411458 |                               0.989844 |                          1 |
| exp13_no_recurrence                 |               0.35 |                   0.0421875 |                               0.754167 |                          1 |
| exp13_no_recurrence                 |               0.5  |                   0.0458333 |                               0.47526  |                          1 |
| exp13_no_recurrence                 |               0.75 |                   0.0408854 |                               0.246875 |                          1 |
| exp13_no_recurrence                 |               1    |                   0.0416667 |                               0.159115 |                          1 |
| exp13_no_structural_plasticity      |               0    |                   0.0302083 |                               1        |                          1 |
| exp13_no_structural_plasticity      |               0.05 |                   0.034375  |                               1        |                          1 |
| exp13_no_structural_plasticity      |               0.1  |                   0.0307292 |                               1        |                          1 |
| exp13_no_structural_plasticity      |               0.2  |                   0.034375  |                               0.99349  |                          1 |
| exp13_no_structural_plasticity      |               0.35 |                   0.0333333 |                               0.753385 |                          1 |
| exp13_no_structural_plasticity      |               0.5  |                   0.0325521 |                               0.469531 |                          1 |
| exp13_no_structural_plasticity      |               0.75 |                   0.0260417 |                               0.264062 |                          1 |
| exp13_no_structural_plasticity      |               1    |                   0.0307292 |                               0.172396 |                          1 |
| exp13_no_world_context              |               0    |                   0.0348958 |                               1        |                          0 |
| exp13_no_world_context              |               0.05 |                   0.0333333 |                               1        |                          0 |
| exp13_no_world_context              |               0.1  |                   0.0361979 |                               1        |                          0 |
| exp13_no_world_context              |               0.2  |                   0.0333333 |                               0.991146 |                          0 |
| exp13_no_world_context              |               0.35 |                   0.0330729 |                               0.744792 |                          0 |
| exp13_no_world_context              |               0.5  |                   0.0348958 |                               0.478125 |                          0 |
| exp13_no_world_context              |               0.75 |                   0.0388021 |                               0.264323 |                          0 |
| exp13_no_world_context              |               1    |                   0.0346354 |                               0.161979 |                          0 |

## Interpretation guide

Expected successful-breaking-point patterns:

1. At or above exact structural capacity (`budget_ratio >= 1.0`), the full model should resemble Experiment 12.
2. Below exact structural capacity, the full model should degrade smoothly rather than remain saturated.
3. No-recurrence should preserve one-step route-table accuracy where edges exist, but show a large composition-route gap for multi-step routes.
4. No-world-context should degrade as incompatible worlds accumulate because shared edges collide.
5. Context corruption should now show a measurable world-selection failure curve, especially under adversarial mixture.
6. Consolidation should shift the retention/acquisition tradeoff under finite memory pressure rather than merely increasing margins.
7. True primitive holdout should separate composition from memorized primitives from inference over genuinely unseen primitive transitions.
8. The continuous front-end bridge should show that route memory survives modest input noise but fails when perceptual decoding fails.

## Manuscript positioning

Experiment 13 is intended to convert the Experiment 12 all-ones result into a boundary-mapping result. For the first manuscript, this should support a more defensible claim: context-indexed structural plasticity and recurrence permit non-destructive storage and execution of incompatible route systems, and the model fails predictably when context, structure, recurrence, or primitive coverage are selectively degraded.
