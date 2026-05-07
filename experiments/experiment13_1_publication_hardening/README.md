# Experiment 13.1 — Publication-Hardening Route-Field Memory Audit

Experiment 13.1 is a successor protocol in the Context-Indexed Route Memory research program. It preserves the Experiment 13 breaking-point theme, but hardens the protocol for manuscript-readiness by separating controls that a reviewer could otherwise conflate.

The core question is:

> Is memory-like behavior in this system encoded partly in the plastic structure of recurrent route fields, rather than only in static learned weights or symbolic lookup tables?

This implementation is self-contained and table-based. It uses Python, NumPy, pandas, matplotlib, and the Python standard-library `sqlite3` module. It does not require PyTorch or dataset downloads.

## 1. Purpose

Experiment 13.1 is intended to cleanly audit whether route-field structure is doing mechanistic work. It separates:

- recurrence during evaluation from recurrence throughout the variant;
- route-table storage from composed traversal;
- live plasticity from previously formed structure;
- clean context from actually corrupted context;
- targeted route-field lesions from matched random lesions;
- local budget pressure from global budget pressure;
- no, weak, default, and aggressive consolidation.

The evidence discipline for interpreting results is:

```text
Claim -> Evidence -> Caveat -> Source path
```

## 2. Hypotheses

### Primary hypothesis

If memory-like behavior is partly encoded in plastic recurrent route-field structure, then disabling recurrence, freezing plasticity, corrupting context, or lesioning route-critical structure should produce specific, dissociable failures. In particular, local route-table accuracy may remain high while multi-step composition collapses, and targeted route-field lesions should impair performance more than matched random lesions.

### Secondary hypotheses

- Evaluation-only recurrence ablation should distinguish route storage from recurrent route execution.
- Recurrence-disabled-throughout should remain analytically distinct from eval-only recurrence ablation.
- Freeze-after-consolidation controls should preserve old-world structure while blocking adaptation to a new world.
- Context corruption should reduce world margin and increase context confusion before, or along with, composition failure.
- Local and global capacity limits should fail differently under consolidation pressure.

## 3. Design

The experiment generates incompatible transition worlds over a shared node/mode substrate. A route-memory model stores plastic route-field edges keyed by context slot, source node, mode slot, and target node.

The model explicitly guards the historical mode-slot bug from the Experiment 11/13 lineage:

- `mode_slot_count = modes + 1`;
- when `context_binding=False`, `_mode_slot()` returns the extra unbound slot `modes`;
- `_mode_slot()` raises an actionable `IndexError` if a slot is outside `[0, modes]`.

## 4. Variants

| Variant | Purpose |
|---|---|
| `exp13_1_full_model` | Main route-field memory model. |
| `exp13_1_no_recurrence_at_eval` | Keeps training/formation intact but disables recurrent traversal at evaluation. |
| `exp13_1_no_recurrence_throughout` | Represents recurrence-disabled-throughout separately from eval-only recurrence ablation. |
| `exp13_1_no_structural_plasticity` | Removes structural route updates. |
| `exp13_1_no_context_binding` | Collapses mode/context binding into the explicit unbound mode slot. |
| `exp13_1_no_world_gated_plasticity` | Removes the active-world plasticity advantage. |
| `exp13_1_no_consolidation` | Dose-response control with no consolidation. |
| `exp13_1_weak_consolidation` | Dose-response control with weak consolidation. |
| `exp13_1_aggressive_consolidation` | Dose-response control with aggressive consolidation. |

## 5. Phases

| Phase | Purpose |
|---|---|
| `variant_comparison` | Compare core variants across one-step and multi-step routes. |
| `structure_audit` | Audit whether route knowledge is recoverable from learned structure. |
| `freeze_plasticity` | Separate formed structure from ongoing structural updates. |
| `context_corruption` | Evaluate clean, dropout, bleed, and wrong-world context injection using corrupted query context. |
| `lesion_test` | Compare clean baseline, targeted route-critical lesions, random count-matched lesions, and random weight-distribution-matched lesions. |
| `budget_consolidation` | Compare default global budget, constrained global budget, and constrained local budget across consolidation settings. |

## 6. Metrics

Key metrics include:

| Metric | Interpretation |
|---|---|
| `composition_accuracy` | Multi-step route execution accuracy. |
| `route_table_accuracy` | One-step local transition lookup accuracy. |
| `structure_transition_accuracy` | Whether the correct edge is directly recoverable from learned structure. |
| `composition_route_gap` | Route-table accuracy minus composition accuracy. |
| `route_margin` | Correct route-edge score over strongest wrong target. |
| `world_margin` | Correct-world context activation over strongest wrong-world activation. |
| `mode_margin` | Correct route-edge score over same-target wrong-mode activation. |
| `wrong_route_activation` | Strongest wrong target under selected context/mode. |
| `wrong_world_activation` | Strongest wrong-world context activation. |
| `wrong_mode_activation` | Same-target activation through an incorrect mode slot. |
| `structural_wrong_world_activation` | Correct target through a wrong-world structural slot. |
| `context_confusion` | Whether wrong-world context activation ties or exceeds correct-world activation. |
| `top1_world_accuracy` | Whether context selection chooses the true world. |
| `used_edge_fraction` | Fraction of route execution steps backed by stored edges. |
| `lesion_sensitivity` | Baseline composition accuracy minus lesioned composition accuracy. |

## 7. Run commands

Run from this experiment directory after installing dependencies:

```powershell
pip install -r requirements.txt
```

### Smoke run

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp13_1.ps1 -Profile smoke
```

or directly:

```powershell
python .\run_exp13_1_publication_hardening.py --profile smoke
```

### Standard run

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp13_1_standard.ps1
```

or:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp13_1_run.ps1 -Profile standard
```

### Full manuscript-grade run

The full run is intentionally separated from validation.

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp13_1_full.ps1
```

Equivalent direct command:

```powershell
python .\run_exp13_1_publication_hardening.py --profile full
```

### Validation-only run

Validation is a separate script.

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp13_1_validate.ps1 -RunId latest
```

or directly:

```powershell
python .\validate_exp13_1.py --run-id latest
```

To validate a specific run:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp13_1_validate.ps1 -RunId exp13_1_full_20260506_210000
```

## 8. Expected outputs

By default, each run writes immutable artifacts under a generated run ID:

```text
experiments/exp13_1_publication_hardening/
  runs/
    <run_id>.sqlite3
  analysis/
    <run_id>/
      run_manifest.json
      progress.jsonl
      metrics.csv
      exp13_1_metrics.csv
      exp13_1_summary.csv
      exp13_1_variant_metrics.csv
      exp13_1_ablation_metrics.csv
      exp13_1_context_corruption.csv
      exp13_1_lesion_metrics.csv
      exp13_1_budget_consolidation.csv
      exp13_1_freeze_plasticity.csv
      experiment_report.md
      exp13_1_report.md
      validation_report.md
      validation_results.json
      plots/
        exp13_1_composition_accuracy.png
        exp13_1_route_table_accuracy.png
        exp13_1_context_confusion.png
        exp13_1_lesion_sensitivity.png
        exp13_1_recurrence_ablation.png
        exp13_1_budget_consolidation.png
```

The `progress.jsonl` file includes:

- completed units;
- total units;
- phase completed/total;
- elapsed seconds;
- unit rate;
- ETA seconds;
- percent complete;
- detail strings such as seed, variant, corruption condition, or lesion condition.

## 9. Validation

The validator emits PASS/WARN/FAIL checks and writes:

```text
analysis/<run_id>/validation_report.md
analysis/<run_id>/validation_results.json
```

Validation checks include:

- required files and plots exist;
- `run_manifest.json` is loadable;
- SQLite exists and contains `metrics`, `metadata`, and `variants` tables;
- raw metrics are non-empty;
- required metadata and metric columns exist;
- metric columns are finite;
- bounded metrics lie in `[0, 1]`;
- required variants and phases are present;
- corrupted context conditions are present and not all identical to clean context;
- recurrence-ablation metadata distinguishes eval-only and throughout controls;
- lesion summaries include targeted and matched/random baselines;
- progress log includes ETA/rate fields;
- report includes caveats and avoids forbidden overclaiming phrases.

## 10. Known caveats

- This is an internal ablation harness, not an external baseline comparison.
- The table-based implementation is intentionally controlled; it is not a biological model by itself.
- Route-table accuracy is local transition knowledge and must not be interpreted as composed traversal.
- Smoke runs are only for artifact and sanity validation.
- Full profile results should still be interpreted with confidence intervals/effect sizes before manuscript use.
- Strong results would support the route-field memory interpretation only within this controlled task family.

## 11. How to interpret results

Use the report and CSVs to build claims conservatively:

```text
Claim:
Evidence:
Caveat:
Source path:
```

Examples of valid interpretations:

- A large route-table/composition gap in recurrence-disabled variants supports a storage/execution dissociation.
- A larger targeted-lesion sensitivity than random-lesion sensitivity supports route-critical structural dependence.
- Context corruption effects on world margin/context confusion support context-indexing vulnerability.

Avoid interpretations such as:

- claiming biological memory has been proven;
- treating internal ablations as external baselines;
- treating route-table accuracy as full composed reasoning;
- using smoke results as manuscript-grade evidence.

## 12. Repository integration after analysis

After a completed standard or full run has been analyzed, update:

- this README completed-runs/results section;
- `docs/experiments/exp13_1_summary.md`;
- `docs/experiments/EXPERIMENT_REGISTRY.md`;
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`;
- `docs/manuscript/FIGURE_PLAN.md`;
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`;
- `docs/manuscript/MANUSCRIPT_TODO.md`;
- `docs/synthesis/PROJECT_STATUS.md`;
- `docs/synthesis/PUBLICATION_READINESS.md`;
- `docs/synthesis/NEXT_EXPERIMENTS.md`.

Do not mutate historical completed run artifacts.

## 13. GPU support

This experiment is table-based and currently CPU-oriented. It does not train neural networks and does not use PyTorch. GPU acceleration is therefore not used in the current implementation. This should be documented as a CPU-only limitation when importing results into synthesis/manuscript docs.

## 14. Completed runs and results

No run has been executed as part of this implementation package.

When you execute a run locally, add a row like:

| Run ID | Profile | SQLite path | Analysis path | Validation | Notes |
|---|---|---|---|---|---|
| `<run_id>` | `standard` | `runs/<run_id>.sqlite3` | `analysis/<run_id>/` | PASS/WARN/FAIL | Summary of key metrics and caveats. |
