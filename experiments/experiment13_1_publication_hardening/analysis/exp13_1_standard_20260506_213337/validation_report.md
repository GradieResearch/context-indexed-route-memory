# Experiment 13.1 Validation Report

## PASS: analysis directory exists

G:\code\OpenSource\GradieResearch\context-indexed-route-memory\experiments\experiment13_1_publication_hardening\analysis\exp13_1_standard_20260506_213337

## PASS: required output files exist

All required files are present.

## PASS: required plots exist under plots/

All required plots are present under plots/.

## PASS: run manifest has required metadata

run_id=exp13_1_standard_20260506_213337

## PASS: SQLite run database exists

G:\code\OpenSource\GradieResearch\context-indexed-route-memory\experiments\experiment13_1_publication_hardening\runs\exp13_1_standard_20260506_213337.sqlite3

## PASS: SQLite contains expected tables

tables=['metadata', 'metrics', 'variants']

## PASS: raw metrics are non-empty

rows=570

## PASS: expected metric and metadata columns present

All expected columns are present.

## PASS: all expected metric columns exist

All expected metric columns exist.

## PASS: no metric column is entirely null

No metric column is entirely null.

## PASS: metric columns are numeric and finite

All metric columns are finite.

## PASS: bounded metrics lie within [0, 1]

All bounded metrics are in range.

## PASS: required variants are present

Variants: ['exp13_1_aggressive_consolidation', 'exp13_1_full_model', 'exp13_1_no_consolidation', 'exp13_1_no_context_binding', 'exp13_1_no_recurrence_at_eval', 'exp13_1_no_recurrence_throughout', 'exp13_1_no_structural_plasticity', 'exp13_1_no_world_gated_plasticity', 'exp13_1_weak_consolidation']

## PASS: required phases are present

Phases: ['budget_consolidation', 'context_corruption', 'freeze_plasticity', 'lesion_test', 'structure_audit', 'variant_comparison']

## PASS: clean and corrupted context conditions are present

Context conditions: ['clean', 'context_bleed', 'context_dropout', 'wrong_world_injection']

## PASS: corrupted context metrics are not identical to clean metrics across all rows

At least one corruption metric differs from clean.

## PASS: no-recurrence-at-eval rows exist

Rows found.

## PASS: no-recurrence-throughout rows exist

Rows found.

## PASS: no-recurrence-at-eval keeps training recurrence metadata separate

Expected recurrence_training=True and recurrence_evaluation=False.

## PASS: no-recurrence-throughout is represented separately

Expected recurrence_training=False and recurrence_evaluation=False.

## PASS: targeted route-field lesion is present

Lesion conditions: ['clean_unlesioned_baseline', 'random_count_matched_edges', 'random_weight_distribution_matched_edges', 'targeted_critical_edges']

## PASS: matched/random lesion baseline is present

Lesion conditions: ['clean_unlesioned_baseline', 'random_count_matched_edges', 'random_weight_distribution_matched_edges', 'targeted_critical_edges']

## PASS: lesion summary conditions match raw lesion rows

Raw lesion conditions: ['clean_unlesioned_baseline', 'random_count_matched_edges', 'random_weight_distribution_matched_edges', 'targeted_critical_edges']

## PASS: progress log includes ETA/rate fields

ETA/rate fields present.

## PASS: progress log reached planned total units

completed=570; manifest_total=570

## PASS: report includes caveats and expected-pattern framing

Report includes caveats and expected-pattern framing.

## PASS: report does not overclaim with forbidden phrases

No forbidden overclaim phrases found.

## Summary

- pass: 27
- warn: 0
- fail: 0