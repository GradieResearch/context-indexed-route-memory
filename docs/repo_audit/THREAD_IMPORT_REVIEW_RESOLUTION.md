# Thread Import Review Resolution

## Summary

This pass corrected the active manuscript evidence map after the adversarial thread-import review. The changes are docs-only: no experiment code was modified, no experiments were rerun, and no generated artifacts were deleted.

The main changes were provenance fixes, claim downgrades, and explicit pending labels. C1 now cites the Exp13 capacity-pressure CSV rather than the validation report for no-structural-plasticity. C10 now treats Exp13 adversarial context corruption as the failure evidence and leaves Exp11/Exp12 as diagnostics. C6 is worded as an observed degradation curve, C7 is preliminary with a docs-only comparison artifact, and C12 is marked `local verification pending` because the novelty assessment artifact is missing locally. I also source-backed the manuscript spine/novelty-positioning scaffolds so they do not present unsupported TODO claims in the active manuscript docs.

## Findings Addressed

### Finding 1

Original issue: C1 cited `experiments/experiment13_breaking_point/analysis/validation_report.md` for no-structural-plasticity, but that validation report does not mention the variant.

Action taken: Replaced the Exp13 validation citation with `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`, which contains `exp13_no_structural_plasticity` rows. Added a caveat that the validation report should not be cited for this subclaim.

Files changed: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/experiments/exp13_summary.md`; `docs/experiments/EXPERIMENT_CLAIMS_MATRIX.csv`

Remaining caveat: Internal ablation evidence only; external baselines and seed-level effect sizes remain pending.

Status: resolved

### Finding 2

Original issue: C12 relied on missing `Pasted text.txt`, used a nonstandard pending-evidence phrase instead of `local verification pending`, and cited a baseline scaffold as evidence.

Action taken: Searched the repository for the novelty assessment and related baseline terms; no local novelty assessment artifact was found. Updated C12 to use `local verification pending`, marked `BASELINE_REQUIREMENTS.md` as planning only, populated source-backed baseline families from local thread/import docs, and added a P0 TODO to import the novelty assessment.

Files changed: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md`; `docs/manuscript/MANUSCRIPT_TODO.md`; `docs/manuscript/LIMITATIONS_AND_THREATS.md`; `docs/manuscript/NOVELTY_POSITIONING.md`; `docs/repo_audit/THREAD_IMPORT_CONFLICTS.md`; `docs/experiments/EXPERIMENT_CLAIMS_MATRIX.csv`

Remaining caveat: The novelty assessment artifact is still missing locally.

Status: partially resolved

### Finding 3

Original issue: C10 treated Exp11, Exp12, and Exp13 as support for context-corruption failure even though Exp12 context bleed/dropout was inconclusive and diagnostic.

Action taken: Rewrote C10 around Exp13 adversarial context corruption only. Exp11/Exp12 are now described as supplementary diagnostics in the caveat and figure plan.

Files changed: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/manuscript/FIGURE_PLAN.md`; `docs/manuscript/RESULTS_STORYBOARD.md`; `docs/repo_audit/THREAD_IMPORT_CONFLICTS.md`; `docs/experiments/EXPERIMENT_CLAIMS_MATRIX.csv`

Remaining caveat: Stochastic/graded context corruption remains an Exp13.1 follow-up.

Status: resolved

### Finding 4

Original issue: C6 used over-strong breaking-curve wording before capacity-law fitting had been performed.

Action taken: Reworded C6 and related manuscript planning docs to describe an observed performance degradation curve. Kept capacity-law fitting as future work.

Files changed: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/manuscript/FIGURE_PLAN.md`; `docs/manuscript/RESULTS_STORYBOARD.md`; `docs/manuscript/MANUSCRIPT_TODO.md`; `docs/experiments/exp12_summary.md`; `docs/experiments/exp13_summary.md`

Remaining caveat: Capacity-law fitting, paired summaries, and confidence intervals remain pending.

Status: resolved

### Finding 5

Original issue: C7 stated that local budget pressure is more damaging than global budget pressure without a paired comparison artifact.

Action taken: Created `docs/experiments/exp13_local_vs_global_budget_comparison.md` from existing Exp13 aggregate CSVs and downgraded C7 to "appears more damaging" with Preliminary status.

Files changed: `docs/experiments/exp13_local_vs_global_budget_comparison.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/manuscript/FIGURE_PLAN.md`; `docs/manuscript/RESULTS_STORYBOARD.md`; `docs/experiments/exp13_summary.md`; `docs/repo_audit/THREAD_IMPORT_CONFLICTS.md`; `docs/experiments/EXPERIMENT_CLAIMS_MATRIX.csv`

Remaining caveat: Formal paired seed-level comparison and confidence intervals remain pending.

Status: partially resolved

### Finding 6

Original issue: Exp11/Exp12/Exp13 summaries had contradictory metadata saying thread digests were imported while stale caveats said the thread digest had not been reviewed.

Action taken: Replaced the top metadata and stale caveat phrases with explicit status fields: local artifacts indexed, key claims partially checked, thread imported, manuscript validation pending, and claims not fully validated for publication.

Files changed: `docs/experiments/exp11_summary.md`; `docs/experiments/exp12_summary.md`; `docs/experiments/exp13_summary.md`

Remaining caveat: Human/manuscript validation remains pending.

Status: resolved

### Finding 7

Original issue: `EXPERIMENT_CLAIMS_MATRIX.csv` was all TODO rows.

Action taken: Replaced the scaffold with a populated matrix for Exp7-Exp13 plus historical/local-verification-pending rows for Exp1-Exp6 and a manuscript-level C12 row.

Files changed: `docs/experiments/EXPERIMENT_CLAIMS_MATRIX.csv`

Remaining caveat: Exp1-Exp6 and Exp9 remain historical or local verification pending for current C1-C12 mapping.

Status: resolved

### Finding 8

Original issue: The pre-import figure inventory retained stale current-looking claim IDs.

Action taken: Added a legacy inventory warning and removed current-looking claim IDs from the pre-import inventory entries. Active figure entries now use the current C1-C12 mapping, including C10 for the Exp13 context corruption figure.

Files changed: `docs/manuscript/FIGURE_PLAN.md`

Remaining caveat: The pre-import artifact inventory is still a convenience list, not the claim-bearing figure plan.

Status: resolved

### Finding 9

Original issue: C4 cited an Exp12 plot for a numeric route-table/composition statement without citing the machine-readable CSV.

Action taken: Added `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv` to C4 evidence and updated required follow-up to include external recurrent baselines, effect sizes/confidence intervals, and a publication-grade figure panel.

Files changed: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/manuscript/RESULTS_STORYBOARD.md`; `docs/experiments/EXPERIMENT_CLAIMS_MATRIX.csv`

Remaining caveat: Statistical hardening and baseline comparison remain pending.

Status: resolved

## Claims Changed

| Claim ID | Old wording/status | New wording/status | Reason |
|---|---|---|---|
| C1 | Strong; Exp13 validation marks no-structural-plasticity as a failure mode | Strong; Exp13 capacity-pressure data include no-structural-plasticity near-chance rows | Validation report did not mention the variant; CSV does. |
| C4 | Strong; numeric Exp12 route-table/composition split cited plot | Strong; numeric split cites machine-readable Exp12 capacity CSV | Numeric claims should cite tables, not only plots. |
| C6 | Over-strong breaking-curve wording; Promising | "Finite structural budget produces an observed performance degradation curve"; Promising | Capacity-law fitting has not been performed. |
| C7 | "Local structural budget pressure is more damaging"; Promising | "Local structural budget pressure appears more damaging"; Preliminary | Dedicated aggregate comparison added, but formal paired comparison is pending. |
| C10 | Context corruption creates failure; Exp11/Exp12/Exp13 support | Adversarial context corruption can collapse route execution; Exp13 support only | Exp11/Exp12 are diagnostics, not completed failure evidence. |
| C12 | Baseline requirement supported by missing novelty artifact and baseline scaffold; Needs baseline | Baseline and prior-art comparison required, with `local verification pending`; Needs baseline | Novelty assessment artifact is missing locally; baseline doc is planning only. |

## Evidence Paths Changed

| Claim ID | Removed path | Added path | Reason |
|---|---|---|---|
| C1 | `experiments/experiment13_breaking_point/analysis/validation_report.md` | `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | Validation report does not mention no-structural-plasticity; capacity CSV does. |
| C4 | none | `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv` | Machine-readable source for route-table 1.0 and composition about 0.05-0.06. |
| C6 | `experiments/experiment13_breaking_point/analysis/validation_report.md` | none | CSV/plot are enough for observed curve; validation report is not needed for fitted-law framing. |
| C7 | none | `docs/experiments/exp13_local_vs_global_budget_comparison.md` | Adds explicit aggregate local-vs-global comparison from existing CSVs. |
| C10 | `experiments/experiment11_context_memory/analysis/exp11/exp11_context_bleed_world_margin.png`; `experiments/experiment12_capacity_generalization/analysis/exp12/context_bleed_summary.csv` | `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`; `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_world_margin.png` | Exp11/Exp12 are diagnostics; Exp13 adversarial corruption is the failure evidence. |
| C12 | `docs/manuscript/BASELINE_REQUIREMENTS.md`; thread-referenced `Pasted text.txt` as apparent artifact support | `local verification pending` | Novelty artifact is missing; baseline requirements are planning only. |

## Deferred Items

- Experiment 13.1: capacity-law fitting, confidence intervals, paired local-vs-global comparison, stochastic/graded context corruption, no-context-binding cleanup, and holdout metric splits.
- External baselines: context-dependent gating / XdG-style comparator, SI or stabilization-plus-gating, replay, HAT/task-mask, PackNet/PathNet parameter isolation, hypernetwork, superposition, and CSCG/TEM-style comparator.
- Human review: manuscript-level validation and source-backed prior-art positioning.
- Missing artifact import: novelty assessment currently referenced as `Pasted text.txt`.
- Metric cleanup: Exp13 seen/unseen route-table splits and confidence intervals.

## Final Consistency Check

| Check | Result |
|---|---|
| Every claim in `CLAIMS_AND_EVIDENCE.md` has status, evidence, caveat, source thread/artifact path or `local verification pending`, required follow-up | pass |
| Claims no longer cite files that fail to support the specific active wording | pass for active claim rows |
| Overclaim phrases removed or caveated in active manuscript/evidence docs | pass; remaining occurrences are in source review or historical thread/source files, not active claim rows |
| C10 does not treat Exp12 context bleed/dropout as completed failure evidence | pass |
| C12 cites local novelty artifact or says `local verification pending` | pass |
| Exp11/Exp12/Exp13 summaries do not contain stale "thread not reviewed" language | pass |
| `FIGURE_PLAN.md` uses current claim IDs or marks old IDs as legacy | pass |
| `EXPERIMENT_CLAIMS_MATRIX.csv` populated for Exp7-Exp13 | pass |
