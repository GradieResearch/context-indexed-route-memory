# Experiment 15: Minimal Neural Baseline Comparator

This experiment implements the next manuscript-finalization item: a deliberately small neural baseline suite for Context-Indexed Route Memory (CIRM).

The purpose is not to run an architecture search or prove that one family of models is universally better than another. The purpose is to answer a reviewer-facing question left open after Experiment 13.2 and Experiment 14:

> Can ordinary neural sequence models trained under matched symbolic route-memory conditions reproduce the same storage, context separation, retention, and compositional execution behavior observed in CIRM?

Experiment 13.2 supplied symbolic/algorithmic baselines. Experiment 14 addressed oracle-context criticism by testing symbolic transition-cue context selection. Experiment 15 adds neural comparators so the manuscript can more honestly state what the current symbolic/mechanistic evidence does and does not show.

## Directory

```text
experiments/experiment15_neural_baseline_comparator/
```

## Required dependencies

Minimum Python dependencies:

```bash
pip install numpy pandas matplotlib torch
```

Optional but useful:

```bash
pip install psutil tabulate
```

`psutil` allows richer RAM metadata in `run_manifest.json`. `tabulate` improves markdown table formatting in the generated report when pandas uses `to_markdown`.

## Model variants

| Variant | Family | Context? | Training regime | Purpose |
|---|---|---:|---|---|
| `neural_gru_endpoint_context` | GRU endpoint | yes | joint endpoint | Tests whether a recurrent sequence model can memorize supplied-context full-route endpoints. |
| `neural_gru_endpoint_no_context` | GRU endpoint | no | joint endpoint | Same model with context withheld, used for conflict sensitivity. |
| `neural_gru_rollout_context` | GRU rollout | yes | joint transition rollout | Tests whether a recurrent neural model trained on stepwise rollouts learns reusable transition structure. |
| `neural_gru_rollout_no_context` | GRU rollout | no | joint transition rollout | Same rollout model with context withheld. |
| `neural_transformer_sequence_context` | Transformer endpoint | yes | joint endpoint | Tests a small attention-based sequence model on supplied-context endpoint prediction. |
| `neural_transition_mlp_context` | Transition MLP | yes | joint transition | One-step `(context, state, action) -> next_state` model rolled out recurrently. |
| `neural_transition_mlp_no_context` | Transition MLP | no | joint transition | Same transition MLP with context withheld. |
| `neural_transition_mlp_replay_context` | Replay transition MLP | yes | sequential worlds with replay | Tests whether bounded replay protects route memory under sequential world training. |
| `neural_transition_mlp_world_heads_context` | Parameter-isolated transition MLP | yes | world-specific heads | Tests whether neural parameter isolation explains retention when context/world identity is supplied. |

The optional neural key-value / memory-augmented lookup baseline is intentionally not included in this first implementation. It would be reasonable future work if reviewers specifically ask for a memory-augmented neural baseline, but it would also broaden Exp15 beyond the minimal comparator needed for finalization.

## Dataset and probe design

The generator creates symbolic route worlds aligned with the manuscript’s route-memory decomposition.

Each world shares route start nodes and mode/action sequences, but the first transition is world-specific. This creates conflict-heavy first-step probes where the same local cue can map to incompatible successors across worlds.

The split is explicit:

- **transition examples** train/evaluate one-step route-table accuracy;
- **seen full-route examples** are available to endpoint models during training;
- **suffix routes** are never presented as full endpoint examples and must be solved by reusable transition composition;
- **first-step context-conflict probes** evaluate whether context/world input resolves incompatible local transitions.

This remains a symbolic benchmark. It does not test perception, raw latent-world discovery, or naturalistic navigation.

## Metrics

The seed-level metric table includes:

- `transition_accuracy`;
- `seen_route_composition_accuracy`;
- `suffix_route_composition_accuracy`;
- `first_step_context_conflict_accuracy`;
- `retention_after_sequential_worlds`;
- runtime and training-cost columns.

The analysis script then derives:

- mean, standard deviation, SEM, and 95% CI by variant/slice/metric;
- compact effect-size comparisons against context-aware neural anchors;
- model runtime summaries;
- route-length and world-count scaling plots.

## Profiles

| Profile | Purpose | Seeds | World counts | Route lengths | Routes/world | Epochs | Use first |
|---|---:|---:|---:|---:|---:|---:|---|
| `smoke` | Syntax/artifact sanity | 1 | 2 | 4 | 4 | 3 | Optional quick local check |
| `validation` | Verify all variants, metrics, plots, and validation checks | 2 | 2, 8 | 4, 8 | 6 | 8 | Yes |
| `full` | Minimal manuscript-facing neural comparator | 10 | 2, 8, 16, 32 | 4, 8, 12 | 12 | 20 | After validation passes |

Route length 16 is intentionally omitted from the default full profile to keep this first neural comparator bounded. Add it only after the validation/full run profile is known to be tractable on the local machine.

## How to run validation on Windows PowerShell

From this experiment directory:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp15_validation.ps1
```

This runs:

1. `python run_experiment15.py --profile validation`
2. `python analyze_experiment15.py --analysis-root analysis`
3. `python validate_experiment15.py --analysis-root analysis`

## How to run the full profile

After validation passes:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp15_full.ps1
```

The full profile can take substantially longer because every seed/world-count/route-length/variant slice trains a small neural model. Console progress and `analysis/<run_id>/progress.jsonl` include seed, variant, slice, elapsed time, rate, and estimated remaining time.

## Python-only usage

```bash
python run_experiment15.py --profile smoke
python analyze_experiment15.py --analysis-root analysis
python validate_experiment15.py --analysis-root analysis
```

Advanced options:

```bash
python run_experiment15.py --profile validation --device cpu
python run_experiment15.py --profile full --device auto --progress-every 5
python run_experiment15.py --profile smoke --no-sqlite
python validate_experiment15.py --source-only
```

## Expected output layout

Each run writes a new directory:

```text
analysis/exp15_<profile>_<timestamp>/
  validation_report.md
  validation_results.json
  run_manifest.json
  exp15_config.json
  progress.jsonl
  metrics.csv
  exp15_seed_metrics.csv
  exp15_summary.csv
  exp15_effect_sizes.csv
  exp15_model_runtime.csv
  exp15_report.md
  experiment_report.md
  plots/
    exp15_seen_vs_suffix_composition.png
    exp15_context_conflict_accuracy.png
    exp15_retention_after_sequential_worlds.png
    exp15_route_length_scaling.png
    exp15_world_count_scaling.png
runs/
  exp15_<profile>_<timestamp>.sqlite3
```

`runs/*.sqlite3` is optional and can be skipped with `--no-sqlite`.

## Manifest and reproducibility metadata

`run_manifest.json` captures:

- Python, platform, processor, CPU count, RAM if `psutil` is installed;
- GPU availability/name, CUDA version, PyTorch version, NumPy/Pandas versions;
- Git commit/branch when available;
- command, profile, start/end time, duration;
- requested and completed seeds/variants/world-counts/route-lengths.

## How to interpret outcomes without overclaiming

Possible outcomes and manuscript consequences:

| Outcome | Interpretation |
|---|---|
| Neural baselines fail broadly. | Strengthens the controlled mechanism result, but still does not prove biological plausibility or universal superiority. |
| Neural baselines solve seen supplied-context routes but fail suffix/context/retention probes. | Supports the route-table/composition/context decomposition and weakens endpoint-memorization explanations. |
| Neural rollout or transition models match CIRM on clean symbolic probes. | The manuscript remains viable as an interpretable mechanism and benchmark paper, but should avoid performance-superiority language. |
| Replay or parameter isolation performs best. | This clarifies that conventional continual-learning controls can close some gaps when given replay or isolated capacity. |
| No-context neural variants fail first-step conflict probes. | Supports the claim that context/world information is necessary under deliberately incompatible route systems. |

Do not describe Exp15 as exhaustive neural benchmarking. It is a minimal comparator suite designed to close the largest remaining baseline vulnerability before manuscript statistical hardening.

## Known limitations

- The task is synthetic and symbolic.
- Model sizes and epochs are intentionally small.
- Hyperparameters are fixed; there is no architecture search.
- Endpoint and transition-trained models answer different questions and should not be collapsed into a single winner/loser story.
- The optional neural key-value / memory-augmented baseline is omitted for scope control.
- Validation confirms artifact and metric integrity, not scientific significance.

## Completed Runs And Results

### `exp15_full_20260508_092811`

Claim -> Exp15 completed the minimal fixed-profile neural comparator, but it is not an exhaustive neural architecture search.
Evidence -> `validation_report.md` reports PASS with 42 PASS, 0 WARN, and 0 FAIL checks for 10 seeds, 9 variants, world counts 2, 8, 16, and 32, route lengths 4, 8, and 12, 5,400 seed metric rows, and 1,080 runtime rows.
Caveat -> `run_manifest.json` was reconstructed after training/evaluation completed but the final SQLite manifest write failed. The SQLite database is present, but local verification found its `run_manifest` table empty; use the CSV artifacts as authoritative unless a later provenance audit says otherwise.
Source path -> `docs/threads/experiment15_analysis_digest.md`; `analysis/exp15_full_20260508_092811/validation_report.md`; `analysis/exp15_full_20260508_092811/run_manifest.json`; `analysis/exp15_full_20260508_092811/exp15_summary.csv`; `analysis/exp15_full_20260508_092811/exp15_seed_metrics.csv`; `analysis/exp15_full_20260508_092811/exp15_model_runtime.csv`; `runs/exp15_full_20260508_092811.sqlite3`.

Hardest-slice summary for `world_count=32`, `route_length=12`, `n_seeds=10`:

| Variant | Conservative hard-slice summary |
|---|---|
| `neural_gru_endpoint_context` | Seen-route composition about 0.9990; suffix-route composition about 0.4040; transition accuracy about 0.0232; retention about 0.7015. |
| `neural_gru_rollout_context` | First-step context conflict about 0.8794; transition accuracy about 0.5122; suffix-route composition about 0.0777; retention about 0.0612. |
| `neural_transformer_sequence_context` | Seen-route composition about 0.5435; suffix-route composition about 0.1184; retention about 0.3309. |
| `neural_transition_mlp_context` | 1.0000 on all hard-slice metrics. |
| `neural_transition_mlp_world_heads_context` | 1.0000 on all hard-slice metrics. |
| `neural_transition_mlp_no_context` | First-step context conflict about 0.0312; seen-route composition about 0.0312; suffix-route composition 1.0000; transition accuracy about 0.9193; retention about 0.5156. |
| `neural_transition_mlp_replay_context` | Near-zero hard-slice performance; this requires implementation/training-regime audit before scientific interpretation. |

Claim -> The completed comparator strengthens the distinction between endpoint memorization, local transition learning, and recurrent route composition.
Evidence -> At the hardest slice, endpoint-style GRU and Transformer models show partial or strong seen-route endpoint behavior without matching suffix composition or transition accuracy, while context-conditioned transition MLP variants solve the clean symbolic benchmark.
Caveat -> The context-conditioned transition MLP result means the manuscript should not claim broad CIRM superiority over neural models or that structural plasticity is required for all route-memory systems.
Source path -> `docs/threads/experiment15_analysis_digest.md`; `analysis/exp15_full_20260508_092811/exp15_summary.csv`; `analysis/exp15_full_20260508_092811/exp15_report.md`.

Claim -> Context/world information is necessary for deliberately conflicting first-step and full-route disambiguation, not universal for every suffix transition.
Evidence -> `neural_transition_mlp_no_context` is near chance on first-step context conflict and seen-route composition at the hard slice, but reaches suffix-route composition 1.0000 and transition accuracy about 0.9193.
Caveat -> Phrase context necessity as conflict-specific. Do not imply that every suffix transition in this generator requires context.
Source path -> `docs/threads/experiment15_analysis_digest.md`; `analysis/exp15_full_20260508_092811/exp15_summary.csv`.
