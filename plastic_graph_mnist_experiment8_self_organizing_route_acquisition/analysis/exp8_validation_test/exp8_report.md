# Experiment 8 Analysis - Self-Organizing Contextual Route Acquisition

Experiment 8 tests whether a local plastic graph can acquire a context-conditioned route field from one-step transition experience, then compose unseen multi-step traversals recurrently.

## Variant summary

| run_name                              |   exposure_repeats |   transition_accuracy_mean |   transition_accuracy_std |   composition_accuracy_mean |   composition_accuracy_std |   composition_mean_target_rank_mean |   composition_mean_correct_margin_mean |   composition_mean_context_margin_mean |   composition_mean_wrong_route_activation_mean |   route_table_accuracy_mean |   n_seeds |
|:--------------------------------------|-------------------:|---------------------------:|--------------------------:|----------------------------:|---------------------------:|------------------------------------:|---------------------------------------:|---------------------------------------:|-----------------------------------------------:|----------------------------:|----------:|
| exp8_context_bleed                    |                  1 |                  0.933333  |                 0.0134687 |                   0.901235  |                  0.0349189 |                             1.04904 |                            0.162703    |                             0.172074   |                                       0.452529 |                   0.933333  |         3 |
| exp8_full_self_organizing_route_field |                  1 |                  1         |                 0         |                   1         |                  0         |                             1       |                            0.339052    |                             0.345783   |                                       0.408698 |                   1         |         3 |
| exp8_no_context_binding               |                  1 |                  0.371429  |                 0         |                   0.156379  |                  0.0354005 |                             1.84259 |                           -0.00756061  |                           nan          |                                     nan        |                   0.371429  |         3 |
| exp8_no_homeostasis                   |                  1 |                  1         |                 0         |                   1         |                  0         |                             1       |                            0.339052    |                             0.345783   |                                       0.408698 |                   1         |         3 |
| exp8_no_inhibition                    |                  1 |                  1         |                 0         |                   1         |                  0         |                             1       |                            0.300801    |                             0.308486   |                                       0.416677 |                   1         |         3 |
| exp8_no_recurrence                    |                  1 |                  1         |                 0         |                   0         |                  0         |                             1       |                            0.362791    |                             0.344528   |                                       0.409161 |                   1         |         3 |
| exp8_no_reward_gate                   |                  1 |                  1         |                 0         |                   1         |                  0         |                             1       |                            0.339052    |                             0.345783   |                                       0.408698 |                   1         |         3 |
| exp8_no_structural_plasticity         |                  1 |                  0.0666667 |                 0.0485621 |                   0.0864198 |                  0.0174594 |                             6.16804 |                           -0.000191727 |                             1.2058e-05 |                                       0.499982 |                   0.0666667 |         3 |


## Deterministic baselines

| split       | baseline                            |   accuracy_mean |   accuracy_std |   n |
|:------------|:------------------------------------|----------------:|---------------:|----:|
| composition | lookup_oracle                       |       1         |      0         |  81 |
| composition | transition_table_composition_oracle |       1         |      0         |  81 |
| composition | always_minus_one                    |       0.37037   |      0         |  81 |
| composition | always_plus_one                     |       0.37037   |      0         |  81 |
| composition | always_plus_two                     |       0.259259  |      0         |  81 |
| composition | most_frequent_target                |       0.111111  |      0         |  81 |
| composition | random_uniform                      |       0.111111  |      0.0213833 |  81 |
| composition | identity_start                      |       0         |      0         |  81 |
| transition  | lookup_oracle                       |       1         |      0         |  35 |
| transition  | transition_table_composition_oracle |       1         |      0         |  35 |
| transition  | always_minus_one                    |       0.342857  |      0         |  35 |
| transition  | always_plus_one                     |       0.342857  |      0         |  35 |
| transition  | always_plus_two                     |       0.314286  |      0         |  35 |
| transition  | random_uniform                      |       0.0952381 |      0.0164957 |  35 |
| transition  | most_frequent_target                |       0.0857143 |      0         |  35 |
| transition  | identity_start                      |       0         |      0         |  35 |


## Route-field diagnostics

| run_name                              | phase             |   exposure_repeats |   route_table_accuracy |   mean_target_rank |   mean_correct_margin |   mean_context_margin |   mean_wrong_route_activation |
|:--------------------------------------|:------------------|-------------------:|-----------------------:|-------------------:|----------------------:|----------------------:|------------------------------:|
| exp8_full_self_organizing_route_field | route_acquisition |                  1 |              1         |            1       |           0.347162    |           0.348846    |                      0.407247 |
| exp8_no_homeostasis                   | route_acquisition |                  1 |              1         |            1       |           0.347162    |           0.348846    |                      0.407247 |
| exp8_no_inhibition                    | route_acquisition |                  1 |              1         |            1       |           0.30906     |           0.313216    |                      0.415249 |
| exp8_no_recurrence                    | route_acquisition |                  1 |              1         |            1       |           0.347162    |           0.348846    |                      0.407247 |
| exp8_no_reward_gate                   | route_acquisition |                  1 |              1         |            1       |           0.347162    |           0.348846    |                      0.407247 |
| exp8_context_bleed                    | route_acquisition |                  1 |              0.933333  |            1.10476 |           0.166294    |           0.174475    |                      0.451702 |
| exp8_no_context_binding               | route_acquisition |                  1 |              0.371429  |            1.91429 |          -0.00453562  |         nan           |                    nan        |
| exp8_no_structural_plasticity         | route_acquisition |                  1 |              0.0666667 |            6.51429 |          -0.000212918 |          -5.51919e-05 |                      0.499998 |


## Interpretation guide

- `transition_accuracy`: one-step transition learning.

- `composition_accuracy`: unseen multi-step recurrent traversal.

- `route_table_accuracy`: direct inspection of the learned local route field.

- `mean_target_rank`: whether the target is near the top even when argmax is wrong.

- `mean_correct_margin`: target score minus strongest wrong target.

- `mean_context_margin`: correct mode support minus strongest wrong-mode support for the same target.

- `mean_wrong_route_activation`: bounded proxy for competing route activation.

- failure taxonomy distinguishes first-step failures from mid-route drift and no-recurrence single-step failures.
