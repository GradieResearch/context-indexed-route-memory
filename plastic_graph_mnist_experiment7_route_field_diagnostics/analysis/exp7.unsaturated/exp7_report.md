# Experiment 7 Analysis - Route Field Diagnostics

Experiment 7 is a diagnostic follow-up to the contextual successor problem. It does not try to make the task harder. It tries to expose exactly where contextual traversal succeeds or breaks: one-step transition learning, recurrent composition, context-conditioned route binding, final-state prediction, or route-field purity.

## Variant summary

| run_name                      |   transition_accuracy |   transition_accuracy_std |   composition_accuracy |   composition_accuracy_std |   mean_target_rank |   mean_correct_margin |   mean_context_margin |   mean_wrong_route_activation |
|:------------------------------|----------------------:|--------------------------:|-----------------------:|---------------------------:|-------------------:|----------------------:|----------------------:|------------------------------:|
| exp7_context_bleed            |                1.0000 |                    0.0000 |                 1.0000 |                     0.0000 |             1.0000 |                0.5941 |                1.2470 |                        0.4382 |
| exp7_full_route_field         |                1.0000 |                    0.0000 |                 1.0000 |                     0.0000 |             1.0000 |                1.1498 |                1.2470 |                        0.4382 |
| exp7_no_inhibition            |                1.0000 |                    0.0000 |                 1.0000 |                     0.0000 |             1.0000 |                0.9998 |                0.9999 |                        0.5000 |
| exp7_noisy_plasticity         |                1.0000 |                    0.0000 |                 1.0000 |                     0.0000 |             1.0000 |                1.0602 |                1.2203 |                        0.4385 |
| exp7_no_context_binding       |                0.3478 |                    0.0000 |                 0.0536 |                     0.0191 |             1.9612 |                0.0182 |              nan      |                      nan      |
| exp7_no_structural_plasticity |                0.0322 |                    0.0190 |                 0.0288 |                     0.0084 |            16.1047 |               -0.0998 |               -0.0296 |                        0.5005 |
| exp7_no_recurrence            |                1.0000 |                    0.0000 |                 0.0000 |                     0.0000 |             1.0000 |                1.1498 |                1.2421 |                        0.4390 |

## Deterministic baselines

| split       | baseline                            |   accuracy |   accuracy_std |   n |
|:------------|:------------------------------------|-----------:|---------------:|----:|
| composition | lookup_oracle                       |     1.0000 |         0.0000 | 532 |
| composition | transition_table_composition_oracle |     1.0000 |         0.0000 | 532 |
| composition | always_minus_one                    |     0.3553 |         0.0000 | 532 |
| composition | always_plus_one                     |     0.3553 |         0.0000 | 532 |
| composition | always_plus_two                     |     0.3026 |         0.0000 | 532 |
| composition | most_frequent_target                |     0.0395 |         0.0000 | 532 |
| composition | random_uniform                      |     0.0296 |         0.0079 | 532 |
| composition | identity_start                      |     0.0000 |         0.0000 | 532 |
| transition  | lookup_oracle                       |     1.0000 |         0.0000 |  92 |
| transition  | transition_table_composition_oracle |     1.0000 |         0.0000 |  92 |
| transition  | always_minus_one                    |     0.3370 |         0.0000 |  92 |
| transition  | always_plus_one                     |     0.3370 |         0.0000 |  92 |
| transition  | always_plus_two                     |     0.3370 |         0.0000 |  92 |
| transition  | most_frequent_target                |     0.0326 |         0.0000 |  92 |
| transition  | random_uniform                      |     0.0297 |         0.0159 |  92 |
| transition  | identity_start                      |     0.0000 |         0.0000 |  92 |

## Route-field diagnostics

| run_name                      |   route_table_accuracy |   mean_target_rank |   mean_correct_margin |   mean_context_margin |   mean_wrong_route_activation |
|:------------------------------|-----------------------:|-------------------:|----------------------:|----------------------:|------------------------------:|
| exp7_context_bleed            |                 1.0000 |             1.0000 |                0.5950 |                1.2418 |                        0.4390 |
| exp7_full_route_field         |                 1.0000 |             1.0000 |                1.1498 |                1.2418 |                        0.4390 |
| exp7_no_inhibition            |                 1.0000 |             1.0000 |                0.9998 |                0.9999 |                        0.5000 |
| exp7_noisy_plasticity         |                 1.0000 |             1.0000 |                1.0610 |                1.2159 |                        0.4392 |
| exp7_no_recurrence            |                 1.0000 |             1.0000 |                1.1498 |                1.2418 |                        0.4390 |
| exp7_no_context_binding       |                 0.3478 |             1.9674 |                0.0124 |              nan      |                      nan      |
| exp7_no_structural_plasticity |                 0.0322 |            16.1812 |               -0.1009 |               -0.0277 |                        0.5002 |

## Interpretation guide

- `transition_accuracy` shows whether the local one-step route table was learned.
- `composition_accuracy` shows whether repeated recurrent traversal works after local route learning.
- `mean_target_rank` tells whether the true next state is near the top even when argmax is wrong.
- `mean_correct_margin` is the true next state's score minus the strongest wrong target score.
- `mean_context_margin` is the correct mode's support for the true target minus the strongest wrong mode's support for that same target.
- `mean_wrong_route_activation` is a bounded proxy for whether competing mode routes remain active.

## Generated figures

- `exp7_accuracy_by_mode.png`
- `exp7_accuracy_by_steps.png`
- `exp7_composition_accuracy.png`
- `exp7_context_margin.png`
- `exp7_correct_margin.png`
- `exp7_target_rank.png`
- `exp7_transition_accuracy.png`
- `route_margin_heatmap_exp7_context_bleed_seed0_minus_one.png`
- `route_margin_heatmap_exp7_context_bleed_seed0_plus_one.png`
- `route_margin_heatmap_exp7_context_bleed_seed0_plus_two.png`
