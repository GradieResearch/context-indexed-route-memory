# Experiment 12 — Capacity, Interference, and Compositional Generalization

Experiment 12 extends Experiment 11 from a successful context-separated memory demonstration into a paper-facing stress test.

The experiment asks four questions:

1. **Capacity:** how many incompatible route worlds can the model retain?
2. **Continual retention:** after each new world is learned, do previous worlds remain accessible?
3. **Compositional generalization:** after training only one-step transitions, can recurrence execute held-out multi-step routes?
4. **Context robustness:** what happens when world context is noisy, blended, or partially dropped out?
5. **Consolidation pressure:** is consolidation actually useful under heavier capacity/noise pressure, or merely optional in the easy regime?

## Mechanistic hypothesis

Experiment 11 suggested a three-layer mechanism:

```text
structural plasticity  ->  encodes local route transitions
world/context binding ->  separates incompatible route worlds
recurrence            ->  executes multi-step compositions over the learned route field
```

Experiment 12 is designed to test whether that story survives scaling.

## Variants

Core variants:

- `exp12_full_context_separated_memory`
- `exp12_world_gated_plasticity`
- `exp12_no_consolidation`
- `exp12_no_world_context`
- `exp12_no_context_binding`
- `exp12_no_recurrence`
- `exp12_no_structural_plasticity`
- `exp12_strong_consolidation`

Additional available variants:

- `exp12_no_inhibition`
- `exp12_shared_edges_only`

## Outputs

The run writes outputs to `analysis/exp12` by default:

- `metrics.csv` — all observations in long form.
- `runs.csv` — run metadata and variant configuration JSON.
- `progress.jsonl` — progress log suitable for tailing during a long run.
- `exp12_final_memory_index.csv` — compact capacity summary.
- `capacity_final_summary.csv` — final capacity by variant/world-count/route-length.
- `continual_retention_summary.csv` — retention after each newly learned world.
- `heldout_generalization_summary.csv` — single-step vs held-out multi-step route behavior.
- `context_bleed_summary.csv` — behavior under world-context bleed.
- `context_dropout_summary.csv` — behavior under world-context dropout.
- `consolidation_pressure_summary.csv` — consolidation strength sweep.
- `plots/*.png` — manuscript-facing diagnostic plots.
- `exp12_report.md` — generated markdown summary.

## Run locally on Windows PowerShell

From this directory:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp12.ps1 -InstallDependencies
```

To run only the brief validation profile:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp12.ps1 -ValidateOnly -InstallDependencies
```

## Run directly with Python

```bash
python experiment12.py --profile full --out analysis/exp12
```

Validation:

```bash
python experiment12.py --profile validate --out analysis/exp12_validation
```

## Full profile defaults

- seeds: `30`
- world counts: `2, 4, 8, 16, 32`
- route lengths: `1, 2, 4, 8, 12`
- nodes: `32`
- modes: `3`
- context bleed: `0.0, 0.05, 0.10, 0.20, 0.35`
- context dropout: `0.0, 0.05, 0.10, 0.20`
- consolidation strengths: `0.0, 0.025, 0.05, 0.12, 0.25, 0.50, 0.80`

## Expected validation behavior

The validation run is not intended to produce final statistical conclusions. It is a smoke test for implementation completeness.

Expected qualitative checks:

- Full and world-gated variants should show high route-table and composition accuracy.
- No-recurrence should show a route-table/composition gap for multi-step routes.
- No-world-context should degrade as incompatible worlds increase.
- No-structural-plasticity should stay near chance.
- Context bleed/dropout should reduce margins before necessarily destroying accuracy.

## Manuscript role

If Experiment 12 succeeds, it becomes the main scaling/generalization result in the first manuscript draft. Experiment 11 remains the clean ablation proof; Experiment 12 becomes the capacity, retention, and generalization stress test.
