# Thread Import Conflicts And Uncertainties

Purpose: Record claims, artifact references, and interpretation issues found while importing exported thread digests.

## Conflict / uncertainty 1

Issue: `docs/threads/experiment1to4_export.md` is present but empty, so no Exp1-Exp4 thread claims could be imported from that file.
Thread source: `docs/threads/experiment1to4_export.md`.
Local artifact status: Exp1-Exp4 local artifacts exist, but thread-level analysis for the named export is absent.
Risk: Early-experiment summaries may remain local-only or rely only on later threads' background mentions.
Recommended resolution: Re-export the Exp1-Exp4 digest or keep Exp1-Exp4 as historical context.

## Conflict / uncertainty 2

Issue: Exp6 thread says the local README still contains stale "Pending first Experiment 6 run" wording while completed Exp6 report artifacts exist.
Thread source: `docs/threads/experiment6_export.md`.
Local artifact status: Completed local artifacts exist at `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_report.md` and `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_comparison.csv`.
Risk: Repository docs may contradict generated results.
Recommended resolution: Update the Exp6 experiment README in a separate docs cleanup without changing run artifacts.

## Conflict / uncertainty 3

Issue: Exp13 `no_context_binding` may not be a pure no-context-binding ablation; the thread describes it as weak-binding or oracle-clean-context because it may retain `context_binding_strength = 0.15` and true-world access when clean.
Thread source: `docs/threads/experiment12to13_export.md`.
Local artifact status: Exp13 run artifacts exist, but the ablation-definition caveat is not resolved by the summary CSVs alone.
Risk: A reviewer could reject no-context-binding claims as mislabeled.
Recommended resolution: Rename the current condition conservatively and rerun a true no-context-binding condition in Exp13.1.

## Conflict / uncertainty 4

Issue: Exp13 holdout route-table metrics appear to mix all transitions rather than separating seen and unseen primitive subsets.
Thread source: `docs/threads/experiment12to13_export.md`.
Local artifact status: `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv` exists, but split route-table metrics are not present.
Risk: The manuscript could overstate generalization or hide unseen-transition failure.
Recommended resolution: Add `route_table_accuracy_all`, `route_table_accuracy_seen`, `route_table_accuracy_unseen`, `composition_accuracy_seen_routes`, and `composition_accuracy_unseen_required_routes` in Exp13.1.

## Conflict / uncertainty 5

Issue: Exp12 context-bleed/dropout curves were discussed as too flat or inconclusive, while artifact filenames could tempt a robustness claim.
Thread source: `docs/threads/experiment12to13_export.md`.
Local artifact status: `experiments/experiment12_capacity_generalization/analysis/exp12/context_bleed_summary.csv`, `context_dropout_summary.csv`, and plots exist.
Risk: Overclaiming robustness from a perturbation that may not affect the decision path.
Recommended resolution: Treat Exp12 context-noise artifacts as diagnostics only; use Exp13/Exp13.1 for context-corruption claims.
Resolution status: resolved in active claim map. C10 now uses Exp13 adversarial context corruption as failure evidence; Exp11/Exp12 are retained only as supplementary diagnostics in the figure plan and caveats.

## Conflict / uncertainty 6

Issue: Exp13 consolidation interpretation is promising in thread heatmap discussion, but the local validation report warns the finite-pressure consolidation delta is small.
Thread source: `docs/threads/experiment12to13_export.md`.
Local artifact status: `experiments/experiment13_breaking_point/analysis/validation_report.md` reports `no_consolidation=0.7661`, `strong=0.7676`, `delta=0.0016`; retention heatmaps exist.
Risk: Manuscript could overstate consolidation as behaviorally necessary.
Recommended resolution: Frame consolidation as preliminary stability-plasticity bias and run dose-response in Exp13.1.

## Conflict / uncertainty 7

Issue: The novelty assessment artifact is referenced as `Pasted text.txt` in the thread but is not indexed locally.
Thread source: `docs/threads/experiment12to13_export.md`.
Local artifact status: No matching file found in repository search or `docs/repo_audit/ARTIFACT_INDEX.csv`.
Risk: Baseline and novelty-readiness claims may appear thread-derived without local provenance.
Recommended resolution: Add the novelty assessment to the repo or keep related claims labeled as thread-derived.
Resolution status: partially resolved. C12 now uses the explicit label `local verification pending`, and `docs/manuscript/BASELINE_REQUIREMENTS.md` is marked as planning only until the novelty assessment is imported.

## Conflict / uncertainty 8

Issue: Early thread exports cite conversation-uploaded plots or zip packages for Exp5-Exp10; many have matching local artifacts, but not all names map one-to-one.
Thread source: `docs/threads/experiment5to10_export.md`; `docs/threads/experiment6_export.md`.
Local artifact status: Local plot/report artifacts exist for Exp5-Exp10, but generated zip package names are not the primary local evidence.
Risk: Source paths could become ambiguous if plot titles are cited instead of repo paths.
Recommended resolution: Cite local CSV/report/plot paths from `docs/repo_audit/ARTIFACT_INDEX.csv`; label unmatched plot-title references as thread-derived.

## Conflict / uncertainty 9

Issue: Exp11 status differs by thread chronology: `experiment5to10_export.md` says Exp11 was implemented but not fully locally analyzed, while `experiment11_export` analyzes completed Exp11 results.
Thread source: `docs/threads/experiment5to10_export.md`; `docs/threads/experiment11_export`.
Local artifact status: Completed Exp11 artifacts exist under `experiments/experiment11_context_memory/analysis/exp11/`.
Risk: A summary could mistakenly treat Exp11 as both pending and completed.
Recommended resolution: Interpret the earlier thread as historical design state; use `docs/threads/experiment11_export` for Exp11 result claims.

## Conflict / uncertainty 10

Issue: Local-vs-global capacity damage in Exp13 is compelling but lacks a dedicated formal comparison artifact.
Thread source: `docs/threads/experiment12to13_export.md`.
Local artifact status: `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`, `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv`, and `docs/experiments/exp13_local_vs_global_budget_comparison.md` exist.
Risk: The local-budget claim could still be too strong without a formal paired seed-level comparison and confidence intervals.
Recommended resolution: Use the docs-only comparison for transparency, keep C7 preliminary, and generate a formal paired comparison in Exp13.1.
Resolution status: partially resolved. The aggregate comparison artifact was added, but paired seed-level analysis remains deferred.
