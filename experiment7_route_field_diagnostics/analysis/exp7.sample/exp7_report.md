# Experiment 7 Analysis - Route Field Diagnostics

Experiment 7 is a diagnostic follow-up to the contextual successor problem. It does not try to make the task harder. It tries to expose exactly where contextual traversal succeeds or breaks: one-step transition learning, recurrent composition, context-conditioned route binding, final-state prediction, or route-field purity.

## Variant summary

| run_name                      |   transition_accuracy |   transition_accuracy_std |   composition_accuracy |   composition_accuracy_std |   mean_target_rank |   mean_correct_margin |   mean_context_margin |   mean_wrong_route_activation |
|:------------------------------|----------------------:|--------------------------:|-----------------------:|---------------------------:|-------------------:|----------------------:|----------------------:|------------------------------:|
| exp7_context_bleed            |                1.0000 |                    0.0000 |                 1.0000 |                     0.0000 |             1.0000 |                6.1946 |               13.0000 |                        0.0474 |
| exp7_full_route_field         |                1.0000 |                    0.0000 |                 1.0000 |                     0.0000 |             1.0000 |               13.0000 |               13.0000 |                        0.0474 |
| exp7_no_inhibition            |                1.0000 |                    0.0000 |                 1.0000 |                     0.0000 |             1.0000 |                9.9998 |                9.9999 |                        0.5000 |
| exp7_noisy_plasticity         |                1.0000 |                    0.0000 |                 1.0000 |                     0.0000 |             1.0000 |               12.9531 |               12.9794 |                        0.0476 |
| exp7_no_context_binding       |                0.3750 |                    0.0000 |                 0.1962 |                     0.0534 |             1.8955 |                0.1625 |              nan      |                      nan      |
| exp7_no_structural_plasticity |                0.0563 |                    0.0140 |                 0.0846 |                     0.0322 |             7.3673 |               -0.0940 |               -0.0417 |                        0.5001 |
| exp7_no_recurrence            |                1.0000 |                    0.0000 |                 0.0000 |                     0.0000 |             1.0000 |               13.0000 |               13.0000 |                        0.0474 |

## Deterministic baselines

| split       | baseline                            |   accuracy |   accuracy_std |   n |
|:------------|:------------------------------------|-----------:|---------------:|----:|
| composition | lookup_oracle                       |     1.0000 |         0.0000 |  52 |
| composition | transition_table_composition_oracle |     1.0000 |         0.0000 |  52 |
| composition | always_minus_one                    |     0.3654 |         0.0000 |  52 |
| composition | always_plus_one                     |     0.3654 |         0.0000 |  52 |
| composition | always_plus_two                     |     0.3077 |         0.0000 |  52 |
| composition | most_frequent_target                |     0.1154 |         0.0000 |  52 |
| composition | random_uniform                      |     0.1000 |         0.0498 |  52 |
| composition | identity_start                      |     0.0000 |         0.0000 |  52 |
| transition  | lookup_oracle                       |     1.0000 |         0.0000 |  32 |
| transition  | transition_table_composition_oracle |     1.0000 |         0.0000 |  32 |
| transition  | always_minus_one                    |     0.3438 |         0.0000 |  32 |
| transition  | always_plus_one                     |     0.3438 |         0.0000 |  32 |
| transition  | always_plus_two                     |     0.3438 |         0.0000 |  32 |
| transition  | most_frequent_target                |     0.0938 |         0.0000 |  32 |
| transition  | random_uniform                      |     0.0750 |         0.0568 |  32 |
| transition  | identity_start                      |     0.0000 |         0.0000 |  32 |

## Route-field diagnostics

| run_name                      |   route_table_accuracy |   mean_target_rank |   mean_correct_margin |   mean_context_margin |   mean_wrong_route_activation |
|:------------------------------|-----------------------:|-------------------:|----------------------:|----------------------:|------------------------------:|
| exp7_context_bleed            |                 1.0000 |             1.0000 |                6.2133 |               13.0000 |                        0.0474 |
| exp7_full_route_field         |                 1.0000 |             1.0000 |               13.0000 |               13.0000 |                        0.0474 |
| exp7_no_inhibition            |                 1.0000 |             1.0000 |                9.9998 |                9.9999 |                        0.5000 |
| exp7_noisy_plasticity         |                 1.0000 |             1.0000 |               12.9538 |               12.9793 |                        0.0476 |
| exp7_no_recurrence            |                 1.0000 |             1.0000 |               13.0000 |               13.0000 |                        0.0474 |
| exp7_no_context_binding       |                 0.3750 |             1.9062 |                0.2728 |              nan      |                      nan      |
| exp7_no_structural_plasticity |                 0.0563 |             7.1312 |               -0.0914 |               -0.0379 |                        0.5000 |

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
