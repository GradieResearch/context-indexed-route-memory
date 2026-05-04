# Experiment 12 Handoff

## What was implemented

A complete local experiment package for Experiment 12:

- `experiment12.py` — main experiment runner.
- `start_exp12.ps1` — PowerShell launcher for Windows.
- `requirements.txt` — minimal dependencies.
- `README.md` — design, expected behavior, outputs, and run instructions.
- `analysis/exp12_validation/` — completed validation pass outputs.

## Validation pass performed

Command executed:

```bash
python experiment12.py --profile validate --out analysis/exp12_validation
```

Validation profile:

- seeds: `2`
- world counts: `2, 4`
- route lengths: `1, 2, 4`
- nodes: `16`
- modes: `3`
- variants:
  - `exp12_full_context_separated_memory`
  - `exp12_world_gated_plasticity`
  - `exp12_no_world_context`
  - `exp12_no_recurrence`
  - `exp12_no_structural_plasticity`

Validation checks passed:

- Full model reached perfect composition and route-table accuracy at 2 and 4 worlds.
- World-gated plasticity reached perfect composition and route-table accuracy at 2 and 4 worlds.
- No-recurrence preserved route-table accuracy but failed multi-step composition, producing the intended route-table/composition gap.
- No-world-context degraded as world count increased.
- No-structural-plasticity stayed near chance.
- Plots and all expected CSV summaries were generated.

## Recommended local full run

From this directory on Windows PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp12.ps1 -InstallDependencies
```

Or, if dependencies are already installed:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp12.ps1
```

Outputs will be written to:

```text
analysis/exp12
```

## Full profile defaults

- seeds: `30`
- world counts: `2, 4, 8, 16, 32`
- route lengths: `1, 2, 4, 8, 12`
- nodes: `32`
- modes: `3`
- core variants: `8`
- context bleed sweep: `0.0, 0.05, 0.10, 0.20, 0.35`
- context dropout sweep: `0.0, 0.05, 0.10, 0.20`
- consolidation strengths: `0.0, 0.025, 0.05, 0.12, 0.25, 0.50, 0.80`
- consolidation world counts: `4, 8, 16`

## After the full run

Upload the full `analysis/exp12` directory. The most important files for review are:

- `exp12_report.md`
- `exp12_final_memory_index.csv`
- `capacity_final_summary.csv`
- `continual_retention_summary.csv`
- `heldout_generalization_summary.csv`
- `context_bleed_summary.csv`
- `context_dropout_summary.csv`
- `consolidation_pressure_summary.csv`
- `plots/*.png`
