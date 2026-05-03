# Experiment 10 Analysis - Rule Reversal, Retention, and Adaptive Rebinding

Experiment 10 tests whether a route field learned under rule A can adapt when the meaning of mode labels is changed to rule B. It also tests whether consolidation, inhibition, reward gating, eligibility traces, and dual world context affect the stability-plasticity tradeoff.

## Variant summary

| run_name                       | phase              |   checkpoint | eval_rule   |   composition/accuracy |   route/route_table_accuracy |   composition/mean_correct_margin |   route/mean_wrong_route_activation |   feedback_noise |   reward_delay_steps |
|:-------------------------------|:-------------------|-------------:|:------------|-----------------------:|-----------------------------:|----------------------------------:|------------------------------------:|-----------------:|---------------------:|
| exp10_dual_context_worlds      | clean_pre_reversal |            0 | A           |              0.986404  |                    0.988768  |                       0.994338    |                         0.320829    |                0 |                    0 |
| exp10_dual_context_worlds      | clean_pre_reversal |            0 | B           |              0.0306391 |                    0.0275362 |                      -0.108673    |                         0.427508    |                0 |                    0 |
| exp10_dual_context_worlds      | clean_reversal     |            0 | A           |              0.986404  |                    0.988768  |                       0.994338    |                         0.320829    |                0 |                    0 |
| exp10_dual_context_worlds      | clean_reversal     |            0 | B           |              0.0306391 |                    0.0275362 |                      -0.108673    |                         0.427508    |                0 |                    0 |
| exp10_dual_context_worlds      | clean_reversal     |           21 | A           |              0.0379073 |                    0.19058   |                      -1.09942     |                         0.298145    |                0 |                    0 |
| exp10_dual_context_worlds      | clean_reversal     |           21 | B           |              1         |                    1         |                      21.2661      |                         0.00308687  |                0 |                    0 |
| exp10_dual_context_worlds      | clean_switchback   |            0 | A           |              0.0379073 |                    0.19058   |                      -1.09942     |                         0.298145    |                0 |                    0 |
| exp10_dual_context_worlds      | clean_switchback   |            0 | B           |              1         |                    1         |                      21.2661      |                         0.00308687  |                0 |                    0 |
| exp10_dual_context_worlds      | clean_switchback   |           13 | A           |              0.987281  |                    0.989493  |                      13.1866      |                         0.18953     |                0 |                    0 |
| exp10_dual_context_worlds      | clean_switchback   |           13 | B           |              1         |                    1         |                      21.1177      |                         0.0104704   |                0 |                    0 |
| exp10_full_adaptive_reversal   | clean_pre_reversal |            0 | A           |              1         |                    1         |                       0.340624    |                         0.411265    |                0 |                    0 |
| exp10_full_adaptive_reversal   | clean_pre_reversal |            0 | B           |              0.289474  |                    0.34058   |                      -0.127646    |                         0.500983    |                0 |                    0 |
| exp10_full_adaptive_reversal   | clean_reversal     |            0 | A           |              1         |                    1         |                       0.340624    |                         0.411265    |                0 |                    0 |
| exp10_full_adaptive_reversal   | clean_reversal     |            0 | B           |              0.289474  |                    0.34058   |                      -0.127646    |                         0.500983    |                0 |                    0 |
| exp10_full_adaptive_reversal   | clean_reversal     |           21 | A           |              0.289474  |                    0.347464  |                       0.00526428  |                         0.427733    |                0 |                    0 |
| exp10_full_adaptive_reversal   | clean_reversal     |           21 | B           |              0.999561  |                    0.999638  |                       0.858738    |                         0.268963    |                0 |                    0 |
| exp10_full_adaptive_reversal   | clean_switchback   |            0 | A           |              0.289474  |                    0.347464  |                       0.00526428  |                         0.427733    |                0 |                    0 |
| exp10_full_adaptive_reversal   | clean_switchback   |            0 | B           |              0.999561  |                    0.999638  |                       0.858738    |                         0.268963    |                0 |                    0 |
| exp10_full_adaptive_reversal   | clean_switchback   |           13 | A           |              1         |                    1         |                       1.30018     |                         0.202929    |                0 |                    0 |
| exp10_full_adaptive_reversal   | clean_switchback   |           13 | B           |              0.289474  |                    0.340942  |                      -0.474863    |                         0.501083    |                0 |                    0 |
| exp10_no_consolidation         | clean_pre_reversal |            0 | A           |              1         |                    1         |                       0.340624    |                         0.411265    |                0 |                    0 |
| exp10_no_consolidation         | clean_pre_reversal |            0 | B           |              0.289474  |                    0.34058   |                      -0.127646    |                         0.500983    |                0 |                    0 |
| exp10_no_consolidation         | clean_reversal     |            0 | A           |              1         |                    1         |                       0.340624    |                         0.411265    |                0 |                    0 |
| exp10_no_consolidation         | clean_reversal     |            0 | B           |              0.289474  |                    0.34058   |                      -0.127646    |                         0.500983    |                0 |                    0 |
| exp10_no_consolidation         | clean_reversal     |           21 | A           |              0.289474  |                    0.34058   |                      -2.30252     |                         0.492246    |                0 |                    0 |
| exp10_no_consolidation         | clean_reversal     |           21 | B           |              1         |                    1         |                       7.08348     |                         0.000736237 |                0 |                    0 |
| exp10_no_consolidation         | clean_switchback   |            0 | A           |              0.289474  |                    0.34058   |                      -2.30252     |                         0.492246    |                0 |                    0 |
| exp10_no_consolidation         | clean_switchback   |            0 | B           |              1         |                    1         |                       7.08348     |                         0.000736237 |                0 |                    0 |
| exp10_no_consolidation         | clean_switchback   |           13 | A           |              0.292607  |                    0.382609  |                       2.19231     |                         0.311355    |                0 |                    0 |
| exp10_no_consolidation         | clean_switchback   |           13 | B           |              0.886591  |                    0.965217  |                       5.25527     |                         0.032578    |                0 |                    0 |
| exp10_no_eligibility_trace     | clean_pre_reversal |            0 | A           |              1         |                    1         |                       0.340624    |                         0.411265    |                0 |                    0 |
| exp10_no_eligibility_trace     | clean_pre_reversal |            0 | B           |              0.289474  |                    0.34058   |                      -0.127646    |                         0.500983    |                0 |                    0 |
| exp10_no_eligibility_trace     | clean_reversal     |            0 | A           |              1         |                    1         |                       0.340624    |                         0.411265    |                0 |                    0 |
| exp10_no_eligibility_trace     | clean_reversal     |            0 | B           |              0.289474  |                    0.34058   |                      -0.127646    |                         0.500983    |                0 |                    0 |
| exp10_no_eligibility_trace     | clean_reversal     |           21 | A           |              0.289474  |                    0.347464  |                       0.00526428  |                         0.427733    |                0 |                    0 |
| exp10_no_eligibility_trace     | clean_reversal     |           21 | B           |              0.999561  |                    0.999638  |                       0.858738    |                         0.268963    |                0 |                    0 |
| exp10_no_eligibility_trace     | clean_switchback   |            0 | A           |              0.289474  |                    0.347464  |                       0.00526428  |                         0.427733    |                0 |                    0 |
| exp10_no_eligibility_trace     | clean_switchback   |            0 | B           |              0.999561  |                    0.999638  |                       0.858738    |                         0.268963    |                0 |                    0 |
| exp10_no_eligibility_trace     | clean_switchback   |           13 | A           |              1         |                    1         |                       1.30018     |                         0.202929    |                0 |                    0 |
| exp10_no_eligibility_trace     | clean_switchback   |           13 | B           |              0.289474  |                    0.340942  |                      -0.474863    |                         0.501083    |                0 |                    0 |
| exp10_no_homeostasis           | clean_pre_reversal |            0 | A           |              1         |                    1         |                       0.340624    |                         0.411265    |                0 |                    0 |
| exp10_no_homeostasis           | clean_pre_reversal |            0 | B           |              0.289474  |                    0.34058   |                      -0.127646    |                         0.500983    |                0 |                    0 |
| exp10_no_homeostasis           | clean_reversal     |            0 | A           |              1         |                    1         |                       0.340624    |                         0.411265    |                0 |                    0 |
| exp10_no_homeostasis           | clean_reversal     |            0 | B           |              0.289474  |                    0.34058   |                      -0.127646    |                         0.500983    |                0 |                    0 |
| exp10_no_homeostasis           | clean_reversal     |           21 | A           |              0.289474  |                    0.347464  |                       0.00526428  |                         0.427733    |                0 |                    0 |
| exp10_no_homeostasis           | clean_reversal     |           21 | B           |              0.999561  |                    0.999638  |                       0.858738    |                         0.268963    |                0 |                    0 |
| exp10_no_homeostasis           | clean_switchback   |            0 | A           |              0.289474  |                    0.347464  |                       0.00526428  |                         0.427733    |                0 |                    0 |
| exp10_no_homeostasis           | clean_switchback   |            0 | B           |              0.999561  |                    0.999638  |                       0.858738    |                         0.268963    |                0 |                    0 |
| exp10_no_homeostasis           | clean_switchback   |           13 | A           |              1         |                    1         |                       1.30018     |                         0.202929    |                0 |                    0 |
| exp10_no_homeostasis           | clean_switchback   |           13 | B           |              0.289474  |                    0.340942  |                      -0.474863    |                         0.501083    |                0 |                    0 |
| exp10_no_inhibition            | clean_pre_reversal |            0 | A           |              1         |                    1         |                       0.307269    |                         0.418753    |                0 |                    0 |
| exp10_no_inhibition            | clean_pre_reversal |            0 | B           |              0.289474  |                    0.339855  |                      -0.114871    |                         0.500875    |                0 |                    0 |
| exp10_no_inhibition            | clean_reversal     |            0 | A           |              1         |                    1         |                       0.307269    |                         0.418753    |                0 |                    0 |
| exp10_no_inhibition            | clean_reversal     |            0 | B           |              0.289474  |                    0.339855  |                      -0.114871    |                         0.500875    |                0 |                    0 |
| exp10_no_inhibition            | clean_reversal     |           21 | A           |              0.289536  |                    0.348188  |                       0.00911346  |                         0.43097     |                0 |                    0 |
| exp10_no_inhibition            | clean_reversal     |           21 | B           |              0.992105  |                    0.997826  |                       0.777271    |                         0.285163    |                0 |                    0 |
| exp10_no_inhibition            | clean_switchback   |            0 | A           |              0.289536  |                    0.348188  |                       0.00911346  |                         0.43097     |                0 |                    0 |
| exp10_no_inhibition            | clean_switchback   |            0 | B           |              0.992105  |                    0.997826  |                       0.777271    |                         0.285163    |                0 |                    0 |
| exp10_no_inhibition            | clean_switchback   |           13 | A           |              1         |                    1         |                       1.17204     |                         0.222492    |                0 |                    0 |
| exp10_no_inhibition            | clean_switchback   |           13 | B           |              0.289474  |                    0.339855  |                      -0.427398    |                         0.499724    |                0 |                    0 |
| exp10_no_reward_gate           | clean_pre_reversal |            0 | A           |              1         |                    1         |                       0.340624    |                         0.411265    |                0 |                    0 |
| exp10_no_reward_gate           | clean_pre_reversal |            0 | B           |              0.289474  |                    0.34058   |                      -0.127646    |                         0.500983    |                0 |                    0 |
| exp10_no_reward_gate           | clean_reversal     |            0 | A           |              1         |                    1         |                       0.340624    |                         0.411265    |                0 |                    0 |
| exp10_no_reward_gate           | clean_reversal     |            0 | B           |              0.289474  |                    0.34058   |                      -0.127646    |                         0.500983    |                0 |                    0 |
| exp10_no_reward_gate           | clean_reversal     |           21 | A           |              0.289474  |                    0.347464  |                       0.00526428  |                         0.427733    |                0 |                    0 |
| exp10_no_reward_gate           | clean_reversal     |           21 | B           |              0.999561  |                    0.999638  |                       0.858738    |                         0.268963    |                0 |                    0 |
| exp10_no_reward_gate           | clean_switchback   |            0 | A           |              0.289474  |                    0.347464  |                       0.00526428  |                         0.427733    |                0 |                    0 |
| exp10_no_reward_gate           | clean_switchback   |            0 | B           |              0.999561  |                    0.999638  |                       0.858738    |                         0.268963    |                0 |                    0 |
| exp10_no_reward_gate           | clean_switchback   |           13 | A           |              1         |                    1         |                       1.30018     |                         0.202929    |                0 |                    0 |
| exp10_no_reward_gate           | clean_switchback   |           13 | B           |              0.289474  |                    0.340942  |                      -0.474863    |                         0.501083    |                0 |                    0 |
| exp10_no_structural_plasticity | clean_pre_reversal |            0 | A           |              0.029198  |                    0.0315217 |                      -0.000283376 |                         0.5         |                0 |                    0 |
| exp10_no_structural_plasticity | clean_pre_reversal |            0 | B           |              0.0304511 |                    0.0307971 |                      -0.000290153 |                         0.500001    |                0 |                    0 |
| exp10_no_structural_plasticity | clean_reversal     |            0 | A           |              0.029198  |                    0.0315217 |                      -0.000283376 |                         0.5         |                0 |                    0 |
| exp10_no_structural_plasticity | clean_reversal     |            0 | B           |              0.0304511 |                    0.0307971 |                      -0.000290153 |                         0.500001    |                0 |                    0 |
| exp10_no_structural_plasticity | clean_reversal     |           21 | A           |              0.029198  |                    0.0315217 |                      -0.000283376 |                         0.5         |                0 |                    0 |
| exp10_no_structural_plasticity | clean_reversal     |           21 | B           |              0.0304511 |                    0.0307971 |                      -0.000290153 |                         0.500001    |                0 |                    0 |
| exp10_no_structural_plasticity | clean_switchback   |            0 | A           |              0.029198  |                    0.0315217 |                      -0.000283376 |                         0.5         |                0 |                    0 |
| exp10_no_structural_plasticity | clean_switchback   |            0 | B           |              0.0304511 |                    0.0307971 |                      -0.000290153 |                         0.500001    |                0 |                    0 |
| exp10_no_structural_plasticity | clean_switchback   |           13 | A           |              0.029198  |                    0.0315217 |                      -0.000283376 |                         0.5         |                0 |                    0 |
| exp10_no_structural_plasticity | clean_switchback   |           13 | B           |              0.0304511 |                    0.0307971 |                      -0.000290153 |                         0.500001    |                0 |                    0 |
| exp10_strong_consolidation     | clean_pre_reversal |            0 | A           |              1         |                    1         |                       0.340624    |                         0.411265    |                0 |                    0 |
| exp10_strong_consolidation     | clean_pre_reversal |            0 | B           |              0.289474  |                    0.34058   |                      -0.127646    |                         0.500983    |                0 |                    0 |
| exp10_strong_consolidation     | clean_reversal     |            0 | A           |              1         |                    1         |                       0.340624    |                         0.411265    |                0 |                    0 |
| exp10_strong_consolidation     | clean_reversal     |            0 | B           |              0.289474  |                    0.34058   |                      -0.127646    |                         0.500983    |                0 |                    0 |
| exp10_strong_consolidation     | clean_reversal     |           21 | A           |              0.927632  |                    0.985145  |                       0.301878    |                         0.411634    |                0 |                    0 |
| exp10_strong_consolidation     | clean_reversal     |           21 | B           |              0.289724  |                    0.35942   |                      -0.0673801   |                         0.486457    |                0 |                    0 |
| exp10_strong_consolidation     | clean_switchback   |            0 | A           |              0.927632  |                    0.985145  |                       0.301878    |                         0.411634    |                0 |                    0 |
| exp10_strong_consolidation     | clean_switchback   |            0 | B           |              0.289724  |                    0.35942   |                      -0.0673801   |                         0.486457    |                0 |                    0 |
| exp10_strong_consolidation     | clean_switchback   |           13 | A           |              0.999561  |                    0.999638  |                       0.381454    |                         0.397032    |                0 |                    0 |
| exp10_strong_consolidation     | clean_switchback   |           13 | B           |              0.289474  |                    0.342029  |                      -0.153472    |                         0.501239    |                0 |                    0 |


## Deterministic baselines

| split       | eval_rule   | baseline             |   accuracy_mean |   accuracy_std |   n |
|:------------|:------------|:---------------------|----------------:|---------------:|----:|
| composition | A           | always_rule_A        |       1         |     0          | 532 |
| composition | A           | always_rule_B        |       0.289474  |     0          | 532 |
| composition | A           | identity_start       |       0         |     0          | 532 |
| composition | A           | lookup_oracle        |       1         |     0          | 532 |
| composition | A           | most_frequent_target |       0.0394737 |     0          | 532 |
| composition | A           | random_uniform       |       0.0296366 |     0.00786231 | 532 |
| composition | B           | always_rule_A        |       0.289474  |     0          | 532 |
| composition | B           | always_rule_B        |       1         |     0          | 532 |
| composition | B           | identity_start       |       0         |     0          | 532 |
| composition | B           | lookup_oracle        |       1         |     0          | 532 |
| composition | B           | most_frequent_target |       0.0394737 |     0          | 532 |
| composition | B           | random_uniform       |       0.0299499 |     0.00817009 | 532 |
| transition  | A           | always_rule_A        |       1         |     0          |  92 |
| transition  | A           | always_rule_B        |       0.326087  |     0          |  92 |
| transition  | A           | identity_start       |       0         |     0          |  92 |
| transition  | A           | lookup_oracle        |       1         |     0          |  92 |
| transition  | A           | most_frequent_target |       0.0326087 |     0          |  92 |
| transition  | A           | random_uniform       |       0.0297101 |     0.015876   |  92 |
| transition  | B           | always_rule_A        |       0.326087  |     0          |  92 |
| transition  | B           | always_rule_B        |       1         |     0          |  92 |
| transition  | B           | identity_start       |       0         |     0          |  92 |
| transition  | B           | lookup_oracle        |       1         |     0          |  92 |
| transition  | B           | most_frequent_target |       0.0326087 |     0          |  92 |
| transition  | B           | random_uniform       |       0.0300725 |     0.0211084  |  92 |


## Interpretation guide

- `eval_rule=A` measures old-rule retention. `eval_rule=B` measures new-rule adaptation.

- `checkpoint=0` in the reversal phase is immediately after the rule change, before any B training.

- New-rule adaptation should increase with reversal exposures; old-rule retention should decrease if the same context labels are overwritten.

- `exp10_dual_context_worlds` tests whether adding higher-level world context can retain both rule sets.

- `exp10_strong_consolidation` should preserve old routes but slow new-rule acquisition.

- `exp10_no_consolidation` should adapt quickly but forget more aggressively.

- `exp10_no_inhibition` should show more old-route interference.

- `exp10_no_reward_gate` and `exp10_no_eligibility_trace` are most meaningful in the optional noisy/delayed stress phase.
