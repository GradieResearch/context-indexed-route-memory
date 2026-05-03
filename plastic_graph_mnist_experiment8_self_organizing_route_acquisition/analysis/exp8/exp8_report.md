# Experiment 8 Analysis - Self-Organizing Contextual Route Acquisition

Experiment 8 tests whether a local plastic graph can acquire a context-conditioned route field from one-step transition experience, then compose unseen multi-step traversals recurrently.

## Variant summary

| run_name                              |   exposure_repeats |   transition_accuracy_mean |   transition_accuracy_std |   composition_accuracy_mean |   composition_accuracy_std |   composition_mean_target_rank_mean |   composition_mean_correct_margin_mean |   composition_mean_context_margin_mean |   composition_mean_wrong_route_activation_mean |   route_table_accuracy_mean |   n_seeds |
|:--------------------------------------|-------------------:|---------------------------:|--------------------------:|----------------------------:|---------------------------:|------------------------------------:|---------------------------------------:|---------------------------------------:|-----------------------------------------------:|----------------------------:|----------:|
| exp8_context_bleed                    |                  1 |                  0.944928  |               0.0277736   |                    0.833772 |                 0.109212   |                             1.05734 |                            0.140215    |                            0.156317    |                                       0.457691 |                   0.944928  |        30 |
| exp8_full_self_organizing_route_field |                  1 |                  1         |               0           |                    1        |                 0          |                             1       |                            0.310338    |                            0.322738    |                                       0.416839 |                   1         |        30 |
| exp8_no_context_binding               |                  1 |                  0.347826  |               5.55112e-17 |                    0.047995 |                 0.0142058  |                             1.94138 |                           -0.0122687   |                          nan           |                                     nan        |                   0.347826  |        30 |
| exp8_no_homeostasis                   |                  1 |                  1         |               0           |                    1        |                 0          |                             1       |                            0.310338    |                            0.322738    |                                       0.416839 |                   1         |        30 |
| exp8_no_inhibition                    |                  1 |                  1         |               0           |                    1        |                 0          |                             1       |                            0.282819    |                            0.294135    |                                       0.422459 |                   1         |        30 |
| exp8_no_recurrence                    |                  1 |                  1         |               0           |                    0        |                 0          |                             1       |                            0.318329    |                            0.322011    |                                       0.417026 |                   1         |        30 |
| exp8_no_reward_gate                   |                  1 |                  1         |               0           |                    1        |                 0          |                             1       |                            0.310338    |                            0.322738    |                                       0.416839 |                   1         |        30 |
| exp8_no_structural_plasticity         |                  1 |                  0.0257246 |               0.0195417   |                    0.031203 |                 0.00871716 |                            16.0963  |                           -0.000273499 |                            3.91964e-05 |                                       0.499977 |                   0.0257246 |        30 |


## Deterministic baselines

| split       | baseline                            |   accuracy_mean |   accuracy_std |   n |
|:------------|:------------------------------------|----------------:|---------------:|----:|
| composition | lookup_oracle                       |       1         |     0          | 532 |
| composition | transition_table_composition_oracle |       1         |     0          | 532 |
| composition | always_minus_one                    |       0.355263  |     0          | 532 |
| composition | always_plus_one                     |       0.355263  |     0          | 532 |
| composition | always_plus_two                     |       0.289474  |     0          | 532 |
| composition | most_frequent_target                |       0.0394737 |     0          | 532 |
| composition | random_uniform                      |       0.0296366 |     0.00786231 | 532 |
| composition | identity_start                      |       0         |     0          | 532 |
| transition  | lookup_oracle                       |       1         |     0          |  92 |
| transition  | transition_table_composition_oracle |       1         |     0          |  92 |
| transition  | always_minus_one                    |       0.336957  |     0          |  92 |
| transition  | always_plus_one                     |       0.336957  |     0          |  92 |
| transition  | always_plus_two                     |       0.326087  |     0          |  92 |
| transition  | most_frequent_target                |       0.0326087 |     0          |  92 |
| transition  | random_uniform                      |       0.0297101 |     0.015876   |  92 |
| transition  | identity_start                      |       0         |     0          |  92 |


## Route-field diagnostics

| run_name                              | phase             |   exposure_repeats |   route_table_accuracy |   mean_target_rank |   mean_correct_margin |   mean_context_margin |   mean_wrong_route_activation |
|:--------------------------------------|:------------------|-------------------:|-----------------------:|-------------------:|----------------------:|----------------------:|------------------------------:|
| exp8_full_self_organizing_route_field | route_acquisition |                  1 |              1         |            1       |           0.314353    |           0.324413    |                      0.415984 |
| exp8_no_homeostasis                   | route_acquisition |                  1 |              1         |            1       |           0.314353    |           0.324413    |                      0.415984 |
| exp8_no_inhibition                    | route_acquisition |                  1 |              1         |            1       |           0.286817    |           0.295953    |                      0.421706 |
| exp8_no_recurrence                    | route_acquisition |                  1 |              1         |            1       |           0.314353    |           0.324413    |                      0.415984 |
| exp8_no_reward_gate                   | route_acquisition |                  1 |              1         |            1       |           0.314353    |           0.324413    |                      0.415984 |
| exp8_context_bleed                    | route_acquisition |                  1 |              0.944928  |            1.06848 |           0.142974    |           0.161689    |                      0.456389 |
| exp8_no_context_binding               | route_acquisition |                  1 |              0.347826  |            1.96739 |          -0.011528    |         nan           |                    nan        |
| exp8_no_structural_plasticity         | route_acquisition |                  1 |              0.0257246 |           16.3406  |          -0.000280762 |          -5.16274e-05 |                      0.499999 |


## Interpretation guide

- `transition_accuracy`: one-step transition learning.

- `composition_accuracy`: unseen multi-step recurrent traversal.

- `route_table_accuracy`: direct inspection of the learned local route field.

- `mean_target_rank`: whether the target is near the top even when argmax is wrong.

- `mean_correct_margin`: target score minus strongest wrong target.

- `mean_context_margin`: correct mode support minus strongest wrong-mode support for the same target.

- `mean_wrong_route_activation`: bounded proxy for competing route activation.

- failure taxonomy distinguishes first-step failures from mid-route drift and no-recurrence single-step failures.
