# Experiment 13 — Breaking Point, Context Corruption, and Continuous Front-End Bridge

Experiment 13 is designed as the first serious **boundary-mapping** experiment after Experiment 12.
Experiment 12 showed that the current mechanism can remain saturated at perfect accuracy across many incompatible worlds. That was important, but a manuscript cannot rely only on ceiling effects. Experiment 13 deliberately pushes the model into regimes where it should fail.

The purpose is to make the first manuscript harder to attack:

1. show where the full mechanism succeeds;
2. show where it breaks;
3. show that ablations fail for specific, mechanistically interpretable reasons;
4. separate memory composition from true unseen-transition inference;
5. bridge from symbolic route tables into a simple continuous/noisy input regime.

This implementation is self-contained and uses only Python, NumPy, pandas, and matplotlib. It does **not** require PyTorch, TensorFlow, torchvision, MNIST downloads, or internet access.

---

## Scientific question

Experiment 13 asks:

> When context-indexed structural route memory is exposed to finite memory capacity, corrupted context signals, primitive transition holdout, and noisy continuous inputs, which components preserve behavior, and where does the mechanism fail?

The intended manuscript contribution is not another “the full model gets 100%” result. The intended contribution is a failure map:

> The model succeeds when structural memory, world context, and recurrence are intact; it fails predictably when context, structure, recurrence, memory budget, or primitive transition coverage is selectively degraded.

---

## Variants

The experiment includes these variants:

| Variant | Purpose |
|---|---|
| `exp13_full_context_separated_memory` | Main mechanism: world-indexed structural route memory with recurrence and moderate consolidation. |
| `exp13_world_gated_plasticity` | Tests whether selective plasticity into the active world improves margins and robustness. |
| `exp13_no_consolidation` | Tests whether storage works without stabilization pressure. |
| `exp13_strong_consolidation` | Tests whether high stabilization improves retention but harms adaptation under finite capacity. |
| `exp13_no_world_context` | Forces all incompatible worlds into a shared memory table. Should show interference. |
| `exp13_no_context_binding` | Retains labelled access in clean conditions but weakens endogenous world selectivity under corruption. |
| `exp13_no_recurrence` | Preserves one-step lookup but prevents multi-step route execution. |
| `exp13_no_structural_plasticity` | Prevents route-memory storage. Should remain near chance. |

---

## Phases

### 1. Capacity pressure

Sweeps world count, route length, and global memory budget.

The global budget is expressed as a ratio of the number of edges required to store all world-specific one-step transitions.

- `budget_ratio = 1.0` means exact capacity for one edge per `(world, source_node, mode)` transition.
- `budget_ratio < 1.0` forces forgetting or incomplete storage.
- `budget_ratio > 1.0` provides slack.

Expected result:

- full model succeeds near/exact capacity;
- full model degrades below capacity;
- no-world-context degrades even with enough edge budget because incompatible worlds collide;
- no-recurrence shows high route-table accuracy but poor multi-step composition;
- no-structural-plasticity remains near chance.

### 2. Local capacity pressure

Sweeps a per-world local edge budget. This tests whether each world has enough local structural capacity to store its own route table.

Expected result:

- if each world gets less than enough local capacity, even context separation cannot save missing transitions;
- this helps distinguish global interference from local under-capacity.

### 3. Context corruption

Sweeps three context corruption types:

| Corruption type | Meaning |
|---|---|
| `uniform_bleed` | Correct context remains present, but signal leaks into wrong worlds. |
| `dropout` | Correct context signal is weakened or absent. |
| `adversarial_mixture` | A specific wrong world competes directly with the correct world. |

Experiment 12's context bleed/dropout curves were almost flat. Experiment 13 therefore records not only composition accuracy, but also:

- top-1 world accuracy;
- world margin;
- wrong-world activation.

Expected result:

- uniform bleed may degrade margin before accuracy;
- dropout should progressively reduce world-selection reliability;
- adversarial mixture should produce a sharp failure near/after the point where wrong-world signal exceeds correct-world signal.

### 4. Continual retention under finite memory pressure

Worlds are trained sequentially. After each new world, all previously seen worlds are evaluated.

This produces retention heatmaps under several budget ratios.

Expected result:

- at full capacity, the full model should resemble Experiment 12;
- below capacity, retention should degrade;
- strong consolidation should shift the stability/plasticity tradeoff, often preserving older worlds while making acquisition of later worlds harder;
- no-consolidation should show less stabilized retention under pressure.

### 5. True holdout generalization

This phase separates three claims that are easy to conflate:

1. one-step route-table storage;
2. multi-step composition from seen primitive transitions;
3. inference over genuinely unseen primitive transitions.

The current model is expected to succeed at composing **seen primitives**, but fail when a route requires a primitive transition that was never stored.

That is not a negative result. It is scientifically valuable because it prevents overclaiming.

Recommended manuscript wording:

> The model composes stored transition primitives into held-out multi-step route executions; it does not infer arbitrary unseen primitive transitions in the absence of a learnable rule.

### 6. Continuous front-end bridge

This is a small non-symbolic bridge experiment.

Each symbolic node is represented by a continuous prototype vector. Evaluation begins with a noisy continuous observation of the start node. A nearest-prototype decoder maps the continuous input back into a route-memory node, after which the route-memory mechanism executes the multi-step route.

This is not a full applied benchmark. It is a bridge showing that the route-memory mechanism does not require perfectly discrete symbolic input at test time.

Expected result:

- full model should survive modest input noise;
- performance should degrade when the perceptual decoder fails;
- no-recurrence and no-world-context should retain their characteristic failure modes.

---

## Running locally

### PowerShell

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp13.ps1 -Profile smoke
```

Recommended first run:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp13.ps1 -Profile smoke -Clean
```

Then, once the smoke run succeeds:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp13.ps1 -Profile standard -Clean
```

For manuscript-grade output:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp13.ps1 -Profile full -Clean
```

### Direct Python

```bash
python run_experiment13.py --profile smoke --output-dir analysis --clean
python validate_exp13.py --analysis-dir analysis
```

---

## Profiles

| Profile | Intended use |
|---|---|
| `smoke` | Quick local verification that the experiment works end-to-end. |
| `standard` | Development-grade run suitable for normal analysis. |
| `full` | Larger manuscript-grade run with 30 seeds and broader sweeps. |

The full run can produce a large `metrics.csv`, but it should still be tractable because the implementation is table-based rather than deep-learning based.

---

## Output files

All outputs are written under `analysis/`.

Important files:

| File | Description |
|---|---|
| `metrics.csv` | Raw metric rows across all seeds, phases, variants, and conditions. |
| `runs.csv` | Variant configuration metadata. |
| `progress.jsonl` | Progress log. Useful if a run is interrupted. |
| `capacity_pressure_summary.csv` | Aggregated capacity/budget results. |
| `local_capacity_pressure_summary.csv` | Aggregated local capacity results. |
| `context_corruption_summary.csv` | Aggregated context corruption results. |
| `continual_retention_pressure_summary.csv` | Aggregated sequential retention results. |
| `true_holdout_generalization_summary.csv` | Aggregated primitive-holdout results. |
| `continuous_frontend_bridge_summary.csv` | Aggregated continuous/noisy input results. |
| `exp13_report.md` | Auto-generated report with snapshots and interpretation guide. |
| `validation_report.md` | Checks that the intended scientific contrasts were actually exercised. |
| `plots/*.png` | Plots for capacity, context corruption, retention, holdout, and continuous bridge. |

---

## Validation checks

`validate_exp13.py` checks for the following:

1. all phases executed;
2. full model succeeds at exact/surplus capacity;
3. finite memory pressure creates a breaking curve;
4. no-recurrence separates one-step route storage from multi-step execution;
5. no-world-context shows interference;
6. adversarial context corruption causes world-selection failure;
7. primitive holdout separates composition from unseen-transition inference;
8. continuous front-end degrades under high perceptual noise;
9. consolidation changes behavior under finite memory pressure, at least as a warning-level check.

If a validation fails, inspect `validation_report.md`. A failure may indicate either a bug or a scientifically interesting non-result.

---

## How this ties off the first manuscript

Experiment 13 is designed to support a final manuscript structure like this:

1. **Experiments 1–4:** initial route-field and plasticity evidence.
2. **Experiments 5–8:** ablations, recurrence, and route execution diagnostics.
3. **Experiments 9–11:** context memory and incompatible-world rebinding.
4. **Experiment 12:** capacity scaling and continual retention in the saturated regime.
5. **Experiment 13:** boundary mapping, failure modes, and continuous input bridge.

The key final paper claim should be narrow, defensible, and hard to attack:

> Context-indexed structural plasticity enables non-destructive storage of incompatible route memories, while recurrence is required to execute those memories compositionally. The mechanism scales under adequate structural capacity and fails predictably under finite capacity, corrupted context, missing primitive transitions, or impaired perceptual decoding.

That claim is much stronger than claiming a general theory of intelligence, and much safer than claiming broad biological equivalence.

---

## Suggested next step after Experiment 13

If Experiment 13 behaves as expected, the next experiment should move from this bridge into a more applied benchmark. A good Experiment 14 would be one of:

1. **Permuted / split MNIST with context-indexed route memory**  
   Learn class-to-route or embedding-to-route behavior across many incompatible task contexts.

2. **CIFAR-10 superclasses or Fashion-MNIST continual task routing**  
   Use a simple convolutional or frozen feature front-end and test whether context-indexed structural memory improves retention.

3. **Gridworld navigation with visual observations**  
   Convert routes into actual trajectories in a small environment where worlds correspond to different obstacle layouts or transition rules.

4. **Mini embodied route-following benchmark**  
   The model receives noisy observations and context cues, then executes multi-step plans through incompatible maps.

The strongest next applied bridge is probably **gridworld navigation with visual observations**, because it remains close to route memory while becoming less toy-like than arbitrary symbolic transition tables.
