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
Recommended resolution: Use Exp13.1 as the cleaner context-binding evidence source and avoid using stale Exp13 no-context-binding as the main support for C2.
Resolution status: partially resolved by Exp13.1 import; Exp13 historical caveat remains.

## Conflict / uncertainty 4

Issue: Exp13 holdout route-table metrics appear to mix all transitions rather than separating seen and unseen primitive subsets.
Thread source: `docs/threads/experiment12to13_export.md`.
Local artifact status: `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv` exists, but split route-table metrics are not present.
Risk: The manuscript could overstate generalization or hide unseen-transition failure.
Recommended resolution: Add `route_table_accuracy_all`, `route_table_accuracy_seen`, `route_table_accuracy_unseen`, `composition_accuracy_seen_routes`, and `composition_accuracy_unseen_required_routes` in a successor or targeted rerun if Exp13 holdout claims remain central.
Resolution status: unresolved; Exp13.1 did not import holdout split artifacts.

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
Recommended resolution: Frame consolidation as preliminary stability-plasticity bias; Exp13.1 supports the conservative wording because it did not show an accuracy rescue from consolidation strength.
Resolution status: partially resolved in active claim map; consolidation remains caveated and supplementary.

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
Recommended resolution: Use the docs-only Exp13 comparison for transparency and the Exp13.1 aggregate budget-consolidation CSV as the stronger internal source; still add uncertainty/final figure scripts before submission.
Resolution status: partially resolved. C7 is now promising internal evidence, but seed-level intervals/effect sizes remain deferred.

## Conflict / uncertainty 11

Issue: Exp13.1 targeted critical-edge lesion diagnostic failed the expected pattern; targeted lesion sensitivity was lower than random count-matched lesion sensitivity.
Thread source: `docs/threads/experiment13_1_analysis_digest.md`.
Local artifact status: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_lesion_metrics.csv` exists and reports targeted lesion sensitivity about 0.0808 versus random count-matched lesion sensitivity about 0.5085.
Risk: A manuscript could overstate route-critical structural evidence if the lesion plot is used as positive support.
Recommended resolution: Audit critical-edge selection and matched lesion controls; rerun before using lesion sensitivity as mechanism evidence.
Resolution status: active caveat. The claim map and figure plan now mark lesion evidence as negative/diagnostic only.

## Conflict / uncertainty 12

Issue: Exp13.1 validation passed, but the run manifest lacks explicit GPU/device/runtime metadata.
Thread source: `docs/threads/experiment13_1_analysis_digest.md`.
Local artifact status: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/run_manifest.json` exists; `experiments/experiment13_1_publication_hardening/README.md` documents the implementation as table-based and CPU-oriented.
Risk: Reproducibility documentation is weaker than manuscript-grade expectations, even though GPU acceleration is not technically expected for this harness.
Recommended resolution: Add device/runtime metadata to future manifests and keep CPU-only rationale in the README.
Resolution status: recorded as TODO and limitation.

## Conflict / uncertainty 13

Issue: The Exp13.2 thread digest says the uploaded analysis bundle did not include the SQLite database, while the run manifest and validation report referenced `runs/exp13_2_full_20260507_165813.sqlite3`.
Thread source: `docs/threads/experiment13_2_analysis_digest.md`.
Local artifact status: The database is present locally at `experiments/experiment13_2_baseline_suite/runs/exp13_2_full_20260507_165813.sqlite3`; validation also reports the SQLite database and expected tables.
Risk: Documentation could incorrectly mark the raw run DB as missing if it relies only on the uploaded digest bundle contents.
Recommended resolution: Cite the DB as a locally verified repository artifact, while preserving the packaging caveat that it was absent from the uploaded digest bundle.
Resolution status: resolved locally during Exp13.2 import; no digest/artifact conflict remains.

## Conflict / uncertainty 14

Issue: Exp13.2 shows the oracle context-gated transition table matches CIRM on the clean supplied-context benchmark.
Thread source: `docs/threads/experiment13_2_analysis_digest.md`.
Local artifact status: `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv` reports both `exp13_2_cirm_full` and `baseline_context_gated_transition_table` at `1.0000` on route-table, seen-route composition, suffix-route composition, and first-step context accuracy for the hard clean slice.
Risk: A manuscript could overclaim raw accuracy superiority over a supplied-context oracle lookup table.
Recommended resolution: Treat this as claim refinement: clean supplied-context symbolic route memory can be solved by oracle context-gated lookup; frame CIRM through mechanism and failure modes instead.
Resolution status: active caveat in claims, limitations, figure plan, and synthesis docs.

## Conflict / uncertainty 15

Issue: Pre-import active docs described Exp15 as pending or neural baselines as absent, while the imported Exp15 digest and local artifacts support completed minimal neural-comparator status.
Thread source: `docs/threads/experiment15_analysis_digest.md`.
Local artifact status: Local artifacts exist under `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/`, and `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/validation_report.md` reports PASS 42, WARN 0, FAIL 0.
Risk: Manuscript/readiness docs could simultaneously claim neural baselines are absent and cite Exp15 results.
Recommended resolution: Update active registry, experiment summary, claims, limitations, figure planning, TODO, and synthesis docs to describe Exp15 as completed minimal fixed-profile neural evidence, while preserving non-exhaustive caveats.
Resolution status: resolved in active docs during Exp15 import; historical drafts and planning prompts may still preserve pre-import wording.

## Conflict / uncertainty 16

Issue: `run_manifest.json` was reconstructed after a final SQLite manifest-write failure, and local SQLite inspection found the `run_manifest` table empty.
Thread source: `docs/threads/experiment15_analysis_digest.md`.
Local artifact status: `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/run_manifest.json` records `recovered_after_failed_sqlite_tail: true`; `experiments/experiment15_neural_baseline_comparator/runs/exp15_full_20260508_092811.sqlite3` is present with `exp15_seed_metrics` and `exp15_model_runtime` tables, but the SQLite `run_manifest` table has 0 rows.
Risk: Provenance could be overstated if docs imply the SQLite manifest is complete.
Recommended resolution: Treat CSV artifacts as authoritative unless a later audit says otherwise; explicitly cite the reconstructed-manifest/empty-SQLite-manifest caveat wherever Exp15 is used for manuscript claims.
Resolution status: active provenance caveat in registry, Exp15 README, claims, limitations, figure planning, synthesis docs, and this import report.
