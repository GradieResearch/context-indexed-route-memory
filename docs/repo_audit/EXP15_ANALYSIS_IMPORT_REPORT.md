# Experiment 15 Analysis Import Report

## Import Summary

Claim -> Experiment 15 analysis digest was imported and local artifacts were verified for run `exp15_full_20260508_092811`.
Evidence -> `docs/imports/experiment15_analysis_digest.zip` contained exactly one root-level markdown file, `experiment15_analysis_digest.md`, which was extracted to `docs/threads/experiment15_analysis_digest.md`.
Caveat -> The imported digest preserves upload-thread wording that marked artifact paths as `local verification pending`; this report records the subsequent local verification pass.
Source path -> `docs/imports/experiment15_analysis_digest.zip`; `docs/threads/experiment15_analysis_digest.md`.

## Verified Run Artifacts

All requested Exp15 artifact paths were present locally:

- `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/run_manifest.json`
- `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_config.json`
- `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/progress.jsonl`
- `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/validation_report.md`
- `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/validation_results.json`
- `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/metrics.csv`
- `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_seed_metrics.csv`
- `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`
- `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_effect_sizes.csv`
- `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_model_runtime.csv`
- `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_report.md`
- `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/experiment_report.md`
- `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/plots/exp15_seen_vs_suffix_composition.png`
- `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/plots/exp15_context_conflict_accuracy.png`
- `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/plots/exp15_retention_after_sequential_worlds.png`
- `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/plots/exp15_route_length_scaling.png`
- `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/plots/exp15_world_count_scaling.png`
- `experiments/experiment15_neural_baseline_comparator/runs/exp15_full_20260508_092811.sqlite3`

Local SQLite inspection found tables `exp15_model_runtime`, `exp15_seed_metrics`, and `run_manifest`. The SQLite `run_manifest` table exists but has 0 rows.

## Missing Or Local Verification Pending

No requested Exp15 artifact path was missing after local verification.

The imported digest itself still contains upload-time `local verification pending` labels for the artifact list. These are historical thread-import labels, not the final local audit status.

Pre-existing manuscript-level novelty artifact `Pasted text.txt` remains local verification pending outside the Exp15 import.

## Documents Updated

- `docs/threads/experiment15_analysis_digest.md`
- `docs/experiments/EXPERIMENT_REGISTRY.md`
- `docs/experiments/exp15_summary.md`
- `experiments/experiment15_neural_baseline_comparator/README.md`
- `docs/manuscript/BASELINE_REQUIREMENTS.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/synthesis/NEXT_EXPERIMENTS.md`
- `docs/repo_audit/THREAD_IMPORT_CONFLICTS.md`
- `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`

`docs/source_data/SOURCE_DATA_MANIFEST.csv` was not updated because no Exp15 source-data mirror files were created or found under `docs/source_data/`.

## Claims Changed

Claim -> C12 changed from neural baselines absent/planned to minimal neural comparator completed, with fixed-profile limitations.
Evidence -> Exp15 validation PASS and local summary/runtime artifacts are present.
Caveat -> Exp15 is not exhaustive neural benchmarking and does not remove the prior-art/novelty import blocker.
Source path -> `docs/threads/experiment15_analysis_digest.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/validation_report.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`.

Claim -> C2 was narrowed: context/world indexing is necessary for incompatible local transitions and first-step/full-route disambiguation, not for every suffix transition.
Evidence -> The no-context transition MLP is near chance on first-step conflict and seen-route composition at the hard slice, but reaches suffix-route composition 1.0000.
Caveat -> This is a generator-specific conflict result.
Source path -> `docs/threads/experiment15_analysis_digest.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`.

Claim -> C4 was strengthened as a route-table/composition/endpoint-memorization dissociation.
Evidence -> Endpoint GRU/Transformer variants show partial or strong seen-route behavior without matching suffix composition or transition accuracy, while transition MLP variants solve the clean transition-composition problem.
Caveat -> This is minimal fixed-profile neural evidence, not an exhaustive model-family conclusion.
Source path -> `docs/threads/experiment15_analysis_digest.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`.

Claim -> C1 now carries an explicit neural-scope caveat.
Evidence -> Context-conditioned transition MLP solves the clean symbolic benchmark.
Caveat -> The manuscript should not claim structural plasticity is required for all route-memory systems or broad CIRM superiority over neural models.
Source path -> `docs/threads/experiment15_analysis_digest.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`.

## Caveats Added

- Exp15 is a minimal comparator, not an exhaustive architecture search.
- Model sizes and hyperparameters are fixed and small.
- No memory-augmented/key-value neural baseline is included.
- Route length 16 is omitted from the default full profile.
- Replay variant performance requires implementation/training-regime audit before scientific interpretation.
- `run_manifest.json` was reconstructed after a final SQLite manifest-write failure.
- SQLite database is present, but its `run_manifest` table is empty; CSV artifacts are treated as authoritative unless a later audit says otherwise.
- No broad neural-superiority claim should be made from Exp15.

## Conflicts Found

Two Exp15 import conflicts/uncertainties were recorded in `docs/repo_audit/THREAD_IMPORT_CONFLICTS.md`:

- Pre-import repository docs described Exp15 as pending or neural baselines as absent, while the imported digest and local artifacts support completed minimal neural comparator status.
- The reconstructed JSON manifest and completed CSV artifacts conflict with an empty SQLite `run_manifest` table; this is treated as a provenance caveat, not a metrics invalidation.

## Source Path Verification

Command: `python scripts/verify_doc_source_paths.py`

Result: PASS.

Summary:

- Files scanned: 114
- OK paths: 5,592
- Missing active paths: 0
- Skipped planned/future paths: 13
- Skipped local-verification-pending paths: 45

Remaining local-verification-pending paths are pre-existing or explicitly marked, including `Pasted text.txt` for prior-art/novelty import. No requested Exp15 local artifact path remains missing.
