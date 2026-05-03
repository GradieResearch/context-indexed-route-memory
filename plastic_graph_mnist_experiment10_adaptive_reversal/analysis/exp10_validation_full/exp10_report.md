# Experiment 10 Analysis - Rule Reversal, Retention, and Adaptive Rebinding

Experiment 10 tests whether a route field learned under rule A can adapt when the meaning of mode labels is changed to rule B. It also tests whether consolidation, inhibition, reward gating, eligibility traces, and dual world context affect the stability-plasticity tradeoff.

## Variant summary

| run_name                       | phase              |   checkpoint | eval_rule   |   composition/accuracy |   route/route_table_accuracy |   composition/mean_correct_margin |   route/mean_wrong_route_activation |   feedback_noise |   reward_delay_steps |
|:-------------------------------|:-------------------|-------------:|:------------|-----------------------:|-----------------------------:|----------------------------------:|------------------------------------:|-----------------:|---------------------:|
| exp10_full_adaptive_reversal   | clean_pre_reversal |            0 | A           |              1         |                         1    |                       0.304137    |                            0.408394 |                0 |                    0 |
| exp10_full_adaptive_reversal   | clean_pre_reversal |            0 | B           |              0.214286  |                         0.4  |                      -0.0865352   |                            0.501527 |                0 |                    0 |
| exp10_full_adaptive_reversal   | clean_reversal     |            0 | A           |              1         |                         1    |                       0.304137    |                            0.408394 |                0 |                    0 |
| exp10_full_adaptive_reversal   | clean_reversal     |            0 | B           |              0.214286  |                         0.4  |                      -0.0865352   |                            0.501527 |                0 |                    0 |
| exp10_full_adaptive_reversal   | clean_reversal     |            2 | A           |              0.357143  |                         0.6  |                       0.130828    |                            0.417194 |                0 |                    0 |
| exp10_full_adaptive_reversal   | clean_reversal     |            2 | B           |              0.607143  |                         0.8  |                       0.436519    |                            0.356577 |                0 |                    0 |
| exp10_full_adaptive_reversal   | clean_switchback   |            0 | A           |              0.357143  |                         0.6  |                       0.130828    |                            0.417194 |                0 |                    0 |
| exp10_full_adaptive_reversal   | clean_switchback   |            0 | B           |              0.607143  |                         0.8  |                       0.436519    |                            0.356577 |                0 |                    0 |
| exp10_full_adaptive_reversal   | clean_switchback   |            1 | A           |              0.607143  |                         0.8  |                       0.450438    |                            0.344605 |                0 |                    0 |
| exp10_full_adaptive_reversal   | clean_switchback   |            1 | B           |              0.357143  |                         0.6  |                       0.300003    |                            0.375554 |                0 |                    0 |
| exp10_no_structural_plasticity | clean_pre_reversal |            0 | A           |              0.0714286 |                         0.05 |                      -0.000126511 |                            0.500001 |                0 |                    0 |
| exp10_no_structural_plasticity | clean_pre_reversal |            0 | B           |              0.214286  |                         0.15 |                      -8.99492e-05 |                            0.499997 |                0 |                    0 |
| exp10_no_structural_plasticity | clean_reversal     |            0 | A           |              0.0714286 |                         0.05 |                      -0.000126511 |                            0.500001 |                0 |                    0 |
| exp10_no_structural_plasticity | clean_reversal     |            0 | B           |              0.214286  |                         0.15 |                      -8.99492e-05 |                            0.499997 |                0 |                    0 |
| exp10_no_structural_plasticity | clean_reversal     |            2 | A           |              0.0714286 |                         0.05 |                      -0.000126511 |                            0.500001 |                0 |                    0 |
| exp10_no_structural_plasticity | clean_reversal     |            2 | B           |              0.214286  |                         0.15 |                      -8.99492e-05 |                            0.499997 |                0 |                    0 |
| exp10_no_structural_plasticity | clean_switchback   |            0 | A           |              0.0714286 |                         0.05 |                      -0.000126511 |                            0.500001 |                0 |                    0 |
| exp10_no_structural_plasticity | clean_switchback   |            0 | B           |              0.214286  |                         0.15 |                      -8.99492e-05 |                            0.499997 |                0 |                    0 |
| exp10_no_structural_plasticity | clean_switchback   |            1 | A           |              0.0714286 |                         0.05 |                      -0.000126511 |                            0.500001 |                0 |                    0 |
| exp10_no_structural_plasticity | clean_switchback   |            1 | B           |              0.214286  |                         0.15 |                      -8.99492e-05 |                            0.499997 |                0 |                    0 |
| exp10_strong_consolidation     | clean_pre_reversal |            0 | A           |              1         |                         1    |                       0.304137    |                            0.408394 |                0 |                    0 |
| exp10_strong_consolidation     | clean_pre_reversal |            0 | B           |              0.214286  |                         0.4  |                      -0.0865352   |                            0.501527 |                0 |                    0 |
| exp10_strong_consolidation     | clean_reversal     |            0 | A           |              1         |                         1    |                       0.304137    |                            0.408394 |                0 |                    0 |
| exp10_strong_consolidation     | clean_reversal     |            0 | B           |              0.214286  |                         0.4  |                      -0.0865352   |                            0.501527 |                0 |                    0 |
| exp10_strong_consolidation     | clean_reversal     |            2 | A           |              0.785714  |                         0.85 |                       0.249018    |                            0.411155 |                0 |                    0 |
| exp10_strong_consolidation     | clean_reversal     |            2 | B           |              0.25      |                         0.5  |                       0.0426562   |                            0.456651 |                0 |                    0 |
| exp10_strong_consolidation     | clean_switchback   |            0 | A           |              0.785714  |                         0.85 |                       0.249018    |                            0.411155 |                0 |                    0 |
| exp10_strong_consolidation     | clean_switchback   |            0 | B           |              0.25      |                         0.5  |                       0.0426562   |                            0.456651 |                0 |                    0 |
| exp10_strong_consolidation     | clean_switchback   |            1 | A           |              0.857143  |                         0.9  |                       0.377696    |                            0.381158 |                0 |                    0 |
| exp10_strong_consolidation     | clean_switchback   |            1 | B           |              0.214286  |                         0.45 |                      -0.0163908   |                            0.47671  |                0 |                    0 |


## Deterministic baselines

| split       | eval_rule   | baseline             |   accuracy_mean |   accuracy_std |   n |
|:------------|:------------|:---------------------|----------------:|---------------:|----:|
| composition | A           | always_rule_A        |        1        |            nan |  28 |
| composition | A           | always_rule_B        |        0.214286 |            nan |  28 |
| composition | A           | identity_start       |        0        |            nan |  28 |
| composition | A           | lookup_oracle        |        1        |            nan |  28 |
| composition | A           | most_frequent_target |        0.178571 |            nan |  28 |
| composition | A           | random_uniform       |        0.214286 |            nan |  28 |
| composition | B           | always_rule_A        |        0.214286 |            nan |  28 |
| composition | B           | always_rule_B        |        1        |            nan |  28 |
| composition | B           | identity_start       |        0        |            nan |  28 |
| composition | B           | lookup_oracle        |        1        |            nan |  28 |
| composition | B           | most_frequent_target |        0.178571 |            nan |  28 |
| composition | B           | random_uniform       |        0.142857 |            nan |  28 |
| transition  | A           | always_rule_A        |        1        |            nan |  20 |
| transition  | A           | always_rule_B        |        0.3      |            nan |  20 |
| transition  | A           | identity_start       |        0        |            nan |  20 |
| transition  | A           | lookup_oracle        |        1        |            nan |  20 |
| transition  | A           | most_frequent_target |        0.15     |            nan |  20 |
| transition  | A           | random_uniform       |        0.1      |            nan |  20 |
| transition  | B           | always_rule_A        |        0.3      |            nan |  20 |
| transition  | B           | always_rule_B        |        1        |            nan |  20 |
| transition  | B           | identity_start       |        0        |            nan |  20 |
| transition  | B           | lookup_oracle        |        1        |            nan |  20 |
| transition  | B           | most_frequent_target |        0.15     |            nan |  20 |
| transition  | B           | random_uniform       |        0.2      |            nan |  20 |


## Interpretation guide

- `eval_rule=A` measures old-rule retention. `eval_rule=B` measures new-rule adaptation.

- `checkpoint=0` in the reversal phase is immediately after the rule change, before any B training.

- New-rule adaptation should increase with reversal exposures; old-rule retention should decrease if the same context labels are overwritten.

- `exp10_dual_context_worlds` tests whether adding higher-level world context can retain both rule sets.

- `exp10_strong_consolidation` should preserve old routes but slow new-rule acquisition.

- `exp10_no_consolidation` should adapt quickly but forget more aggressively.

- `exp10_no_inhibition` should show more old-route interference.

- `exp10_no_reward_gate` and `exp10_no_eligibility_trace` are most meaningful in the optional noisy/delayed stress phase.
