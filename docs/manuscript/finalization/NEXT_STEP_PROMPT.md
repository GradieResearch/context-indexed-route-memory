# Next Step Prompt: Design and Implement Experiment 15

Use this prompt with a local coding agent to kick off the next manuscript-finalization item.

```text
You are working in the repository:

https://github.com/GradieResearch/context-indexed-route-memory

Task: Design and implement, but do not execute the full run for, Experiment 15: Minimal Neural Baseline Comparator.

Purpose:

The manuscript currently has strong internal symbolic/mechanistic evidence and a completed symbolic/algorithmic baseline suite from Exp13.2, but it lacks ordinary neural sequence-model comparators. Experiment 15 should test whether basic neural baselines trained under comparable symbolic route-memory conditions reproduce, fail, or partially reproduce the same storage, composition, context-interference, retention, and suffix-route behavior as Context-Indexed Route Memory.

Important controlling docs to inspect first:

- `docs/manuscript/finalization/MANUSCRIPT_FINALIZATION_PLAN.md`
- `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`
- `docs/manuscript/draft/MANUSCRIPT_V1.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/BASELINE_REQUIREMENTS.md`
- `docs/experiments/EXPERIMENT_REGISTRY.md`
- `docs/experiments/exp13_2_summary.md`
- `docs/experiments/exp14_summary.md`
- relevant implementation patterns in `experiments/experiment13_2_baseline_suite/`
- relevant implementation patterns in `experiments/experiment14_latent_context_inference/`

Primary deliverable:

Create the planned self-contained experiment directory:

`experiments/experiment15_neural_baseline_comparator/`

Do not run the full experiment. Implement it, run only minimal syntax/import checks or a tiny smoke path if safe, and document exactly how Paul should run validation and full profiles locally.

Required files:

```text
experiments/experiment15_neural_baseline_comparator/
  README.md
  run_experiment15.py
  analyze_experiment15.py
  validate_experiment15.py
  start_exp15_validation.ps1
  start_exp15_full.ps1
```

Add additional helper modules if needed, but keep the experiment self-contained unless a repository-level utility already clearly exists and is safe to reuse.

Scientific question:

Can standard neural sequence models trained under matched symbolic route-memory conditions reproduce the storage, context separation, retention, and compositional execution behavior observed in CIRM?

Hypotheses:

1. Neural baselines may perform well on clean supplied-context seen routes when given enough training.
2. Endpoint-trained neural baselines should be vulnerable to suffix-route composition failures unless explicitly trained on reusable transition rollouts.
3. No-context neural baselines should suffer on conflict-sensitive first-step probes when identical local cues map to incompatible successors across worlds.
4. Sequentially trained neural baselines should show forgetting/interference unless replay, parameter isolation, or sufficient capacity is supplied.
5. Even if some neural baselines perform well, the route-table/composition/context/suffix metric split should clarify whether they learned reusable transition structure or endpoint memorization.

Required baseline variants:

1. GRU or LSTM endpoint model.
2. GRU or LSTM rollout model.
3. Small Transformer sequence model.
4. Neural one-step transition model, such as MLP/embedding model for `(context, state, action) -> next_state`, rolled out recurrently.
5. Replay-trained neural baseline.
6. Parameter-isolated neural baseline using world-specific heads, adapters, masks, or heads.

Optional only if inexpensive:

7. Neural key-value / memory-augmented lookup baseline.

Required metrics:

- one-step route-table / transition accuracy;
- seen-route composition accuracy;
- suffix-route composition accuracy;
- first-step context-conflict accuracy;
- retention after sequential worlds;
- route-length scaling;
- world-count scaling;
- train/runtime cost;
- seed-level metrics suitable for confidence intervals and effect sizes.

Recommended profiles:

- `smoke`: tiny, fast, sanity only.
- `validation`: enough to verify all variants, metrics, manifests, and plots run.
- `full`: manuscript-grade local run, not to be executed by the agent unless explicitly asked later.

Recommended hard slices:

Use a small but meaningful subset aligned to Exp13.2/Exp14 manuscript probes:

- world counts: 2, 8, 16, 32;
- route lengths: 4, 8, 12, and optionally 16 if runtime remains reasonable;
- conflict-heavy worlds;
- seen full routes;
- suffix routes;
- first-step context-conflict probes;
- sequential-world training / retention;
- context vs no-context variants.

Implementation requirements:

- Use deterministic seed handling.
- Provide clear progress logging with seed, variant, slice, elapsed time, and rough remaining work.
- Capture runtime and hardware metadata in `run_manifest.json`.
- Avoid data leakage between train and suffix/holdout probes.
- Ensure no-context and context variants differ only by availability of context input.
- Ensure replay and parameter-isolation configurations are explicit in output artifacts.
- Keep model sizes small and runtime bounded. This is a minimal comparator, not architecture search.
- Prefer PyTorch if adding neural models, unless the repository already standardizes differently.
- Make dependencies explicit in the README. Avoid adding heavyweight dependencies unless necessary.

Expected analysis output after a run:

```text
analysis/exp15_<profile>_<timestamp>/
  validation_report.md
  run_manifest.json
  exp15_summary.csv
  exp15_seed_metrics.csv
  exp15_effect_sizes.csv
  exp15_model_runtime.csv
  plots/
    exp15_seen_vs_suffix_composition.png
    exp15_context_conflict_accuracy.png
    exp15_retention_after_sequential_worlds.png
    exp15_route_length_scaling.png
    exp15_world_count_scaling.png
```

Validation script requirements:

`validate_experiment15.py` should check at minimum:

- expected files exist;
- expected variants are present;
- expected profile metadata exists;
- metrics are within valid ranges;
- no NaN or infinite metrics;
- all requested seeds completed;
- train/eval split metadata exists;
- suffix probes are identified separately from seen full-route probes;
- context/no-context variants are distinguishable in config columns;
- replay/parameter-isolation configs are recorded;
- runtime/hardware manifest fields are present;
- validation report emits PASS/WARN/FAIL counts.

README requirements:

Explain in plain language:

- purpose of Exp15;
- how it relates to the manuscript limitation register;
- model variants;
- metrics;
- expected outputs;
- how to run validation;
- how to run the full profile;
- how to interpret possible outcomes without overclaiming.

PowerShell scripts:

- `start_exp15_validation.ps1` should run the validation profile and analysis/validation steps.
- `start_exp15_full.ps1` should run the full profile and analysis/validation steps.
- Include clear comments and fail-fast behavior.
- Do not hide failures.

Repository updates:

After creating the experiment directory, update only lightweight planning/index docs if appropriate:

- `docs/experiments/EXPERIMENT_REGISTRY.md` with Exp15 planned/implemented status.
- `docs/synthesis/NEXT_EXPERIMENTS.md` if it exists and clearly needs the next-action pointer.

Do not update manuscript claims as if results exist. Exp15 is implementation-only until Paul runs it and imports results.

Definition of done:

- Experiment 15 directory exists and is self-contained.
- Validation and full run scripts exist.
- Analysis and validation scripts exist.
- README clearly explains how to run and interpret the experiment.
- The implementation supports smoke/validation/full profiles.
- Runtime/hardware metadata capture exists.
- Progress logging is clear enough for a long local run.
- The repository does not claim Exp15 results before they exist.

Final response should summarize:

1. files created/modified;
2. how to run validation;
3. how to run full profile;
4. known limitations;
5. anything intentionally not done.
```
