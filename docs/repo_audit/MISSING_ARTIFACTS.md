# Missing Artifacts

Purpose: Audit each detected experiment for required documentation, runnable entry points, analysis outputs, validation artifacts, thread digests, and reproducibility notes.

## Experiment 1

### Present

- README.md: `experiments/experiment1/README.md`
- Run script(s): `experiments/experiment1/run_mnist_experiment.py`, `experiments/experiment1/start.ps1`, `experiments/experiment1/start.sh`
- Experiment summary doc populated: `docs/experiments/exp1_summary.md`
- Reproducibility/run instructions: local README or launchers detected; commands still need execution verification

### Missing

- metrics.csv or equivalent
- Generated report
- Plots directory or plot images
- Validation script or validation report
- Thread digest

### Ambiguous

- None detected in this pass.

### Recommended action

- Import thread digest and reconcile claims with local evidence.
- Confirm canonical run profile and validation status before manuscript use.

## Experiment 2

### Present

- README.md: `experiments/experiment2/README.md`
- Run script(s): `experiments/experiment2/run_mnist_experiment.py`, `experiments/experiment2/start.ps1`, `experiments/experiment2/start.sh`
- Metrics or equivalent summary CSV(s): `experiments/experiment2/analysis/metrics.csv`
- Generated/design report(s): `experiments/experiment2/analysis/analysis_report.md`
- Plot image(s): 4 indexed in `docs/repo_audit/ARTIFACT_INDEX.csv`
- Experiment summary doc populated: `docs/experiments/exp2_summary.md`
- Reproducibility/run instructions: local README or launchers detected; commands still need execution verification

### Missing

- Validation script or validation report
- Thread digest

### Ambiguous

- None detected in this pass.

### Recommended action

- Import thread digest and reconcile claims with local evidence.
- Confirm canonical run profile and validation status before manuscript use.

## Experiment 3

### Present

- README.md: `experiments/experiment3/README.md`
- Run script(s): `experiments/experiment3/run_experiment_suite.py`, `experiments/experiment3/run_mnist_experiment.py`, `experiments/experiment3/start.ps1`, `experiments/experiment3/start.sh`
- Metrics or equivalent summary CSV(s): `experiments/experiment3/analysis/suite/suite_comparison.csv`
- Generated/design report(s): `experiments/experiment3/analysis/suite/suite_report.md`
- Plot image(s): 1 indexed in `docs/repo_audit/ARTIFACT_INDEX.csv`
- Experiment summary doc populated: `docs/experiments/exp3_summary.md`
- Reproducibility/run instructions: local README or launchers detected; commands still need execution verification

### Missing

- Validation script or validation report
- Thread digest

### Ambiguous

- None detected in this pass.

### Recommended action

- Import thread digest and reconcile claims with local evidence.
- Confirm canonical run profile and validation status before manuscript use.

## Experiment 4

### Present

- README.md: `experiments/experiment4_successor/README.md`
- Run script(s): `experiments/experiment4_successor/run_exp4_successor_experiment.py`, `experiments/experiment4_successor/run_exp4_suite.py`, `experiments/experiment4_successor/run_experiment_suite.py`, `experiments/experiment4_successor/run_mnist_experiment.py`, `experiments/experiment4_successor/start.ps1`, `experiments/experiment4_successor/start.sh`
- Metrics or equivalent summary CSV(s): `experiments/experiment4_successor/analysis/exp4/exp4_comparison.csv`
- Generated/design report(s): `experiments/experiment4_successor/EXPERIMENT_4_SUCCESSOR_TRAVERSAL.md`, `experiments/experiment4_successor/analysis/exp4/exp4_report.md`
- Plot image(s): 3 indexed in `docs/repo_audit/ARTIFACT_INDEX.csv`
- Experiment summary doc populated: `docs/experiments/exp4_summary.md`
- Reproducibility/run instructions: local README or launchers detected; commands still need execution verification

### Missing

- Validation script or validation report
- Thread digest

### Ambiguous

- None detected in this pass.

### Recommended action

- Import thread digest and reconcile claims with local evidence.
- Confirm canonical run profile and validation status before manuscript use.

## Experiment 5

### Present

- README.md: `experiments/experiment5_contextual_successor/README.md`
- Run script(s): `experiments/experiment5_contextual_successor/run_exp5_contextual_successor.py`, `experiments/experiment5_contextual_successor/run_exp5_suite.py`, `experiments/experiment5_contextual_successor/start.ps1`, `experiments/experiment5_contextual_successor/start.sh`
- Metrics or equivalent summary CSV(s): `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_comparison.csv`, `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_comparison.csv`
- Generated/design report(s): `experiments/experiment5_contextual_successor/EXPERIMENT_5_CONTEXTUAL_SUCCESSOR.md`, `experiments/experiment5_contextual_successor/analysis/exp5_smoke/exp5_report.md`, `experiments/experiment5_contextual_successor/analysis/exp5_suite_smoke/exp5_report.md`
- Plot image(s): 14 indexed in `docs/repo_audit/ARTIFACT_INDEX.csv`
- Experiment summary doc populated: `docs/experiments/exp5_summary.md`
- Reproducibility/run instructions: local README or launchers detected; commands still need execution verification

### Missing

- Validation script or validation report
- Thread digest

### Ambiguous

- None detected in this pass.

### Recommended action

- Import thread digest and reconcile claims with local evidence.
- Confirm canonical run profile and validation status before manuscript use.

## Experiment 6

### Present

- README.md: `experiments/experiment6_route_audit_successor/README.md`
- Run script(s): `experiments/experiment6_route_audit_successor/run_exp6_route_audit_successor.py`, `experiments/experiment6_route_audit_successor/run_exp6_suite.py`, `experiments/experiment6_route_audit_successor/start.ps1`, `experiments/experiment6_route_audit_successor/start.sh`
- Metrics or equivalent summary CSV(s): `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_comparison.csv`
- Generated/design report(s): `experiments/experiment6_route_audit_successor/EXPERIMENT_6_ROUTE_AUDIT_SUCCESSOR.md`, `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_report.md`
- Plot image(s): 8 indexed in `docs/repo_audit/ARTIFACT_INDEX.csv`
- Experiment summary doc populated: `docs/experiments/exp6_summary.md`
- Reproducibility/run instructions: local README or launchers detected; commands still need execution verification

### Missing

- Validation script or validation report
- Thread digest

### Ambiguous

- None detected in this pass.

### Recommended action

- Import thread digest and reconcile claims with local evidence.
- Confirm canonical run profile and validation status before manuscript use.

## Experiment 7

### Present

- README.md: `experiments/experiment7_route_field_diagnostics/README.md`
- Run script(s): `experiments/experiment7_route_field_diagnostics/run_exp7_route_field_diagnostics.py`, `experiments/experiment7_route_field_diagnostics/run_exp7_suite.py`, `experiments/experiment7_route_field_diagnostics/start.ps1`, `experiments/experiment7_route_field_diagnostics/start.sh`
- Metrics or equivalent summary CSV(s): `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_baseline_summary.csv`, `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_route_summary.csv`, `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_summary.csv`, `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/metrics.csv`, `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/exp7_baseline_summary.csv`, `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/exp7_route_summary.csv`, `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/exp7_summary.csv`, `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/metrics.csv`; plus 4 more
- Generated/design report(s): `experiments/experiment7_route_field_diagnostics/EXPERIMENT_7_ROUTE_FIELD_DIAGNOSTICS.md`, `experiments/experiment7_route_field_diagnostics/TRACKER_UPDATE_EXP7.md`, `experiments/experiment7_route_field_diagnostics/analysis/exp7.sample/exp7_report.md`, `experiments/experiment7_route_field_diagnostics/analysis/exp7.saturated/exp7_report.md`, `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_report.md`
- Plot image(s): 30 indexed in `docs/repo_audit/ARTIFACT_INDEX.csv`
- Experiment summary doc populated: `docs/experiments/exp7_summary.md`
- Reproducibility/run instructions: local README or launchers detected; commands still need execution verification

### Missing

- Validation script or validation report
- Thread digest

### Ambiguous

- None detected in this pass.

### Recommended action

- Import thread digest and reconcile claims with local evidence.
- Confirm canonical run profile and validation status before manuscript use.

## Experiment 8

### Present

- README.md: `experiments/experiment8_self_organizing_route_acquisition/README.md`
- Run script(s): `experiments/experiment8_self_organizing_route_acquisition/run_exp8_self_organizing_route_acquisition.py`, `experiments/experiment8_self_organizing_route_acquisition/run_exp8_suite.py`, `experiments/experiment8_self_organizing_route_acquisition/start.ps1`, `experiments/experiment8_self_organizing_route_acquisition/start.sh`, `experiments/experiment8_self_organizing_route_acquisition/start_exp8.ps1`
- Metrics or equivalent summary CSV(s): `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_baseline_summary.csv`, `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_route_summary.csv`, `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv`, `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/metrics.csv`, `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_baseline_summary.csv`, `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_route_summary.csv`, `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_summary.csv`, `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/metrics.csv`; plus 4 more
- Generated/design report(s): `experiments/experiment8_self_organizing_route_acquisition/EXPERIMENT_8_SELF_ORGANIZING_ROUTE_ACQUISITION.md`, `experiments/experiment8_self_organizing_route_acquisition/TRACKER_UPDATE_EXP8.md`, `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_report.md`, `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_report.md`, `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation_test/exp8_report.md`
- Plot image(s): 42 indexed in `docs/repo_audit/ARTIFACT_INDEX.csv`
- Validation artifacts present under nonstandard name/location: `experiments/experiment8_self_organizing_route_acquisition/runs/exp8_validation.sqlite3`, `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/baselines.csv`, `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_accuracy_by_mode.png`, `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_accuracy_by_steps.png`, `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_baseline_summary.csv`, `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8_validation/exp8_composition_accuracy.png`; plus 43 more
- Experiment summary doc populated: `docs/experiments/exp8_summary.md`
- Reproducibility/run instructions: local README or launchers detected; commands still need execution verification

### Missing

- Thread digest

### Ambiguous

- Validation exists as validation-named outputs but not as a single `validation_report.md`; confirm canonical validation status.

### Recommended action

- Import thread digest and reconcile claims with local evidence.
- Confirm canonical run profile and validation status before manuscript use.

## Experiment 9

### Present

- README.md: `experiments/experiment9_robust_adaptive_route_plasticity/README.md`
- Run script(s): `experiments/experiment9_robust_adaptive_route_plasticity/run_exp9_robust_adaptive_route_plasticity.py`, `experiments/experiment9_robust_adaptive_route_plasticity/run_exp9_suite.py`, `experiments/experiment9_robust_adaptive_route_plasticity/start.ps1`, `experiments/experiment9_robust_adaptive_route_plasticity/start.sh`, `experiments/experiment9_robust_adaptive_route_plasticity/start_exp9.ps1`
- Metrics or equivalent summary CSV(s): `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_baseline_summary.csv`, `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_route_summary.csv`, `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_summary.csv`, `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/metrics.csv`, `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_baseline_summary.csv`, `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_route_summary.csv`, `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_summary.csv`, `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/metrics.csv`
- Generated/design report(s): `experiments/experiment9_robust_adaptive_route_plasticity/EXPERIMENT_9_ROBUST_ADAPTIVE_ROUTE_PLASTICITY.md`, `experiments/experiment9_robust_adaptive_route_plasticity/TRACKER_UPDATE_EXP9.md`, `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_report.md`, `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_report.md`
- Plot image(s): 41 indexed in `docs/repo_audit/ARTIFACT_INDEX.csv`
- Validation artifacts present under nonstandard name/location: `experiments/experiment9_robust_adaptive_route_plasticity/runs/exp9_validation.sqlite3`, `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/baselines.csv`, `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_baseline_summary.csv`, `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_clean_composition_accuracy.png`, `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_clean_transition_accuracy.png`, `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9_validation/exp9_failure_taxonomy.png`; plus 24 more
- Experiment summary doc populated: `docs/experiments/exp9_summary.md`
- Reproducibility/run instructions: local README or launchers detected; commands still need execution verification

### Missing

- Thread digest

### Ambiguous

- Validation exists as validation-named outputs but not as a single `validation_report.md`; confirm canonical validation status.

### Recommended action

- Import thread digest and reconcile claims with local evidence.
- Confirm canonical run profile and validation status before manuscript use.

## Experiment 10

### Present

- README.md: `experiments/experiment10_adaptive_reversal/README.md`
- Run script(s): `experiments/experiment10_adaptive_reversal/run_exp10_adaptive_reversal.py`, `experiments/experiment10_adaptive_reversal/run_exp10_suite.py`, `experiments/experiment10_adaptive_reversal/start.ps1`, `experiments/experiment10_adaptive_reversal/start.sh`, `experiments/experiment10_adaptive_reversal/start_exp10.ps1`
- Metrics or equivalent summary CSV(s): `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_baseline_summary.csv`, `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_route_summary.csv`, `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_summary.csv`, `experiments/experiment10_adaptive_reversal/analysis/exp10/metrics.csv`, `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_baseline_summary.csv`, `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_route_summary.csv`, `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_summary.csv`, `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/metrics.csv`
- Generated/design report(s): `experiments/experiment10_adaptive_reversal/EXPERIMENT_10_ADAPTIVE_REVERSAL.md`, `experiments/experiment10_adaptive_reversal/TRACKER_UPDATE_EXP10.md`, `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_report.md`, `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_report.md`
- Plot image(s): 18 indexed in `docs/repo_audit/ARTIFACT_INDEX.csv`
- Validation artifacts present under nonstandard name/location: `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/baselines.csv`, `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_adaptation_thresholds.csv`, `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_baseline_summary.csv`, `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_failure_taxonomy_final_new_rule.png`, `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_final_new_rule_composition.png`, `experiments/experiment10_adaptive_reversal/analysis/exp10_validation_full/exp10_final_old_rule_retention.png`; plus 14 more
- Experiment summary doc populated: `docs/experiments/exp10_summary.md`
- Reproducibility/run instructions: local README or launchers detected; commands still need execution verification

### Missing

- Thread digest

### Ambiguous

- Validation exists as validation-named outputs but not as a single `validation_report.md`; confirm canonical validation status.

### Recommended action

- Import thread digest and reconcile claims with local evidence.
- Confirm canonical run profile and validation status before manuscript use.

## Experiment 11

### Present

- README.md: `experiments/experiment11_context_memory/README.md`
- Run script(s): `experiments/experiment11_context_memory/run_exp11_context_memory.py`, `experiments/experiment11_context_memory/run_exp11_suite.py`, `experiments/experiment11_context_memory/start.ps1`, `experiments/experiment11_context_memory/start.sh`, `experiments/experiment11_context_memory/start_exp11.ps1`
- Metrics or equivalent summary CSV(s): `experiments/experiment11_context_memory/analysis/exp11/exp11_baseline_summary.csv`, `experiments/experiment11_context_memory/analysis/exp11/exp11_failure_summary.csv`, `experiments/experiment11_context_memory/analysis/exp11/exp11_final_sequential_summary.csv`, `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`, `experiments/experiment11_context_memory/analysis/exp11/exp11_summary.csv`, `experiments/experiment11_context_memory/analysis/exp11/metrics.csv`, `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_baseline_summary.csv`, `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_failure_summary.csv`; plus 4 more
- Generated/design report(s): `experiments/experiment11_context_memory/EXPERIMENT_11_CONTEXT_MEMORY.md`, `experiments/experiment11_context_memory/TRACKER_UPDATE_EXP11.md`, `experiments/experiment11_context_memory/analysis/exp11/exp11_report.md`, `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_report.md`
- Plot image(s): 38 indexed in `docs/repo_audit/ARTIFACT_INDEX.csv`
- Validation artifacts present under nonstandard name/location: `experiments/experiment11_context_memory/analysis/exp11_validation/baselines.csv`, `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_alternating_composition.png`, `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_alternating_route_table.png`, `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_alternating_world_margin.png`, `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_baseline_summary.csv`, `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_context_bleed_composition.png`; plus 27 more
- Experiment summary doc populated: `docs/experiments/exp11_summary.md`
- Reproducibility/run instructions: local README or launchers detected; commands still need execution verification

### Missing

- Thread digest

### Ambiguous

- Validation exists as validation-named outputs but not as a single `validation_report.md`; confirm canonical validation status.

### Recommended action

- Import thread digest and reconcile claims with local evidence.
- Confirm canonical run profile and validation status before manuscript use.

## Experiment 12

### Present

- README.md: `experiments/experiment12_capacity_generalization/README.md`
- Run script(s): `experiments/experiment12_capacity_generalization/start_exp12.ps1`
- Metrics or equivalent summary CSV(s): `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`, `experiments/experiment12_capacity_generalization/analysis/exp12/consolidation_pressure_summary.csv`, `experiments/experiment12_capacity_generalization/analysis/exp12/context_bleed_summary.csv`, `experiments/experiment12_capacity_generalization/analysis/exp12/context_dropout_summary.csv`, `experiments/experiment12_capacity_generalization/analysis/exp12/continual_retention_summary.csv`, `experiments/experiment12_capacity_generalization/analysis/exp12/heldout_generalization_summary.csv`, `experiments/experiment12_capacity_generalization/analysis/exp12/metrics.csv`, `experiments/experiment12_capacity_generalization/analysis/exp12_validation/capacity_final_summary.csv`; plus 6 more
- Generated/design report(s): `experiments/experiment12_capacity_generalization/HANDOFF.md`, `experiments/experiment12_capacity_generalization/analysis/exp12/exp12_report.md`, `experiments/experiment12_capacity_generalization/analysis/exp12_validation/exp12_report.md`
- Plot image(s): 24 indexed in `docs/repo_audit/ARTIFACT_INDEX.csv`
- Validation artifacts present under nonstandard name/location: `experiments/experiment12_capacity_generalization/analysis/exp12_validation/capacity_final_summary.csv`, `experiments/experiment12_capacity_generalization/analysis/exp12_validation/consolidation_pressure_summary.csv`, `experiments/experiment12_capacity_generalization/analysis/exp12_validation/context_bleed_summary.csv`, `experiments/experiment12_capacity_generalization/analysis/exp12_validation/context_dropout_summary.csv`, `experiments/experiment12_capacity_generalization/analysis/exp12_validation/continual_retention_summary.csv`, `experiments/experiment12_capacity_generalization/analysis/exp12_validation/exp12_final_memory_index.csv`; plus 17 more
- Experiment summary doc populated: `docs/experiments/exp12_summary.md`
- Reproducibility/run instructions: local README or launchers detected; commands still need execution verification

### Missing

- Thread digest

### Ambiguous

- Validation exists as validation-named outputs but not as a single `validation_report.md`; confirm canonical validation status.

### Recommended action

- Import thread digest and reconcile claims with local evidence.
- Confirm canonical run profile and validation status before manuscript use.

## Experiment 13

### Present

- README.md: `experiments/experiment13_breaking_point/README.md`
- Run script(s): `experiments/experiment13_breaking_point/run_experiment13.py`, `experiments/experiment13_breaking_point/start_exp13.ps1`
- Metrics or equivalent summary CSV(s): `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`, `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`, `experiments/experiment13_breaking_point/analysis/continual_retention_pressure_summary.csv`, `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv`, `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv`, `experiments/experiment13_breaking_point/analysis/metrics.csv`, `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv`
- Generated/design report(s): `experiments/experiment13_breaking_point/analysis/exp13_report.md`, `experiments/experiment13_breaking_point/analysis/validation_report.md`, `experiments/experiment13_breaking_point/analysis/validation_report.md`
- Plot image(s): 36 indexed in `docs/repo_audit/ARTIFACT_INDEX.csv`
- Validation report: `experiments/experiment13_breaking_point/analysis/validation_report.md`
- Experiment summary doc populated: `docs/experiments/exp13_summary.md`
- Reproducibility/run instructions: local README or launchers detected; commands still need execution verification

### Missing

- Thread digest

### Ambiguous

- None detected in this pass.

### Recommended action

- Import thread digest and reconcile claims with local evidence.
- Confirm canonical run profile and validation status before manuscript use.

## Audit TODO

- Re-run this audit after thread digests are imported.
- Execute or verify manuscript-critical smoke/standard/full commands.

## Thread-Derived Missing Artifacts And Required Reruns

These items were revealed by the imported thread digests. They should be treated as manuscript blockers or caveats, not as completed findings.

| Item | Why missing / needed | Source thread | Current local status | Recommended action |
|---|---|---|---|---|
| Exp1-Exp4 thread evidence | `docs/threads/experiment1to4_export.md` is empty. | `docs/threads/experiment1to4_export.md` | No digest evidence to import. | Either re-export the digest or keep Exp1-Exp4 historical/local-only. |
| Exp6 README run-result cleanup | Thread reports `README.md` still says the first Exp6 run is pending while `exp6_report.md` has results. | `docs/threads/experiment6_export.md` | Local report exists: `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_report.md`. | Update Exp6 README in a separate docs cleanup if desired; no experiment rerun required. |
| Exp13.1 hardening run | Exp13 no-context-binding, holdout metrics, stochastic corruption, and consolidation dose-response need correction. | `docs/threads/experiment12to13_export.md` | No Exp13.1 directory exists. | Create a new top-level Exp13.1 experiment directory; do not modify Exp13 outputs in place. |
| External baseline suite | Thread novelty assessment says baselines are required before journal readiness. | `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md` | `docs/manuscript/BASELINE_REQUIREMENTS.md` exists, but baseline runs are not present. | Implement shared-table, context-gated, replay, isolation, hypernetwork/superposition, and recurrent non-plastic baselines. |
| Seed-level intervals and effect sizes | Threads cite means and validation summaries but not manuscript-grade uncertainty. | `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md` | Summary CSVs exist for Exp8-Exp13; final CI/effect-size tables are not indexed. | Add statistical summary artifacts before submission. |
| Final reproducible figure scripts | Figure plan cites existing generated plots, but manuscript panels need reproducible source scripts/tables. | `docs/threads/experiment12to13_export.md` | Plot PNGs exist; final figure scripts are not indexed. | Create manuscript figure scripts and source-data manifests. |
| Novelty assessment source artifact | Thread references `Pasted text.txt` as a novelty assessment artifact. | `docs/threads/experiment12to13_export.md` | No matching local artifact is indexed. | Add the novelty assessment to `docs/theory/` or record it as thread-derived only. |
