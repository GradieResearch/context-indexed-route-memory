# Thread Digest: Experiment 15 Minimal Neural Baseline Comparator

Digest filename: `experiment15_analysis_digest.md`
Intended repository path: `docs/threads/experiment15_analysis_digest.md`
Import package expected at: `docs/imports/experiment15_analysis_digest.zip`

## 1. Thread scope

This thread analyzed the uploaded full-run artifact bundle for Experiment 15, the minimal neural baseline comparator for the Context-Indexed Route Memory (CIRM) manuscript. The analysis follows `03_analyze_uploaded_results_and_prepare_repo_import.md`: inspect uploaded artifacts, avoid direct GitHub updates, avoid strengthening claims beyond uploaded evidence, create a single-file digest zip, and provide a Codex prompt for repository import.

The analysis uses the uploaded bundle `E15AnalysisRuns.zip` as source-of-truth for Exp15 results. Current repository context indicates that Exp15 was implemented but awaiting local full-run/result import before manuscript claims could be updated. After this import, Exp15 should become completed neural-baseline evidence, with caveats.

## 2. Experiment analyzed or designed

- Experiment ID: Exp15
- Experiment name: Minimal Neural Baseline Comparator
- Experiment directory: `experiments/experiment15_neural_baseline_comparator/`
- Run profile: `full`
- Run ID: `exp15_full_20260508_092811`
- Uploaded artifact bundle: `E15AnalysisRuns.zip`
- Main local artifact paths, if known:
  - `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/run_manifest.json` — local verification pending
  - `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_config.json` — local verification pending
  - `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/progress.jsonl` — local verification pending
  - `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/validation_report.md` — local verification pending
  - `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/validation_results.json` — local verification pending
  - `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/metrics.csv` — local verification pending
  - `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_seed_metrics.csv` — local verification pending
  - `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv` — local verification pending
  - `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_effect_sizes.csv` — local verification pending
  - `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_model_runtime.csv` — local verification pending
  - `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_report.md` — local verification pending
  - `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/experiment_report.md` — local verification pending
  - `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/plots/exp15_seen_vs_suffix_composition.png` — local verification pending
  - `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/plots/exp15_context_conflict_accuracy.png` — local verification pending
  - `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/plots/exp15_retention_after_sequential_worlds.png` — local verification pending
  - `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/plots/exp15_route_length_scaling.png` — local verification pending
  - `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/plots/exp15_world_count_scaling.png` — local verification pending
- Per-run database path, if applicable:
  - `experiments/experiment15_neural_baseline_comparator/runs/exp15_full_20260508_092811.sqlite3` — local verification pending

## 3. Experimental design discussed

Exp15 asks whether ordinary neural sequence and transition models trained under matched symbolic route-memory conditions can reproduce the storage, context separation, retention, and compositional execution behavior observed in CIRM.

The tested variants are:

| Variant | Family | Context? | Training regime | Role |
|---|---:|---:|---|---|
| `neural_gru_endpoint_context` | GRU endpoint | yes | joint endpoint | Full-route endpoint memorization with supplied context. |
| `neural_gru_endpoint_no_context` | GRU endpoint | no | joint endpoint | Endpoint memorization without context. |
| `neural_gru_rollout_context` | GRU rollout | yes | joint transition rollout | Recurrent transition rollout with context. |
| `neural_gru_rollout_no_context` | GRU rollout | no | joint transition rollout | Recurrent transition rollout without context. |
| `neural_transformer_sequence_context` | Transformer endpoint | yes | joint endpoint | Small attention-based endpoint prediction. |
| `neural_transition_mlp_context` | Transition MLP | yes | joint transition | One-step `(context, state, action) -> next_state`, rolled out recurrently. |
| `neural_transition_mlp_no_context` | Transition MLP | no | joint transition | Same transition learner with context withheld. |
| `neural_transition_mlp_replay_context` | Replay transition MLP | yes | sequential worlds with replay | Bounded replay continual-learning control. |
| `neural_transition_mlp_world_heads_context` | World-head transition MLP | yes | world-specific heads | Parameter-isolated neural control. |

Dataset/probe split:

- `transition_accuracy`: one-step route-table accuracy.
- `seen_route_composition_accuracy`: full routes available to endpoint models during training.
- `suffix_route_composition_accuracy`: suffix full routes withheld as endpoint examples; must be solved by reusable transition composition.
- `first_step_context_conflict_accuracy`: world-specific first transition probes requiring context/world disambiguation.
- `retention_after_sequential_worlds`: sequential-world retention probe.

The benchmark is synthetic and symbolic. It does not test perception, naturalistic navigation, raw latent-world discovery, or broad neural architecture search.

## 4. Results analyzed

### Run integrity and artifact audit

The uploaded bundle contains 19 files:

- README at bundle root.
- Full analysis directory: `analysis/exp15_full_20260508_092811/`.
- SQLite database: `runs/exp15_full_20260508_092811.sqlite3`.
- Metrics CSVs: `metrics.csv`, `exp15_seed_metrics.csv`, `exp15_summary.csv`, `exp15_effect_sizes.csv`, `exp15_model_runtime.csv`.
- Reports: `exp15_report.md`, `experiment_report.md`, `validation_report.md`, `validation_results.json`.
- Metadata: `run_manifest.json`, `exp15_config.json`, `progress.jsonl`.
- Plots: five expected PNGs.

Validation status: `PASS`.

Validation counts:

| Level | Count |
|---|---:|
| PASS | 42 |
| WARN | 0 |
| FAIL | 0 |

Run profile/integrity:

| Field | Value |
|---|---:|
| Run ID | `exp15_full_20260508_092811` |
| Profile | `full` |
| Seeds | 10: `0-9` |
| World counts | `2, 8, 16, 32` |
| Route lengths | `4, 8, 12` |
| Variants | 9 |
| Metrics | 5 |
| Seed metric rows | 5,400 |
| Runtime rows | 1,080 |
| Expected unit count | 1,080 |
| Completed unit count | 1,080 |
| Status values in metrics | `ok` for all 5,400 metric rows |
| Device | `cuda` for all 1,080 runtime rows |
| GPU | NVIDIA TITAN X (Pascal) |
| Runtime | about 17,096.851 seconds, about 4.75 hours |
| Git commit recorded | `4120a3dce763f75081ee873f1565171dab4e4544` |
| Git branch recorded | `main` |

Important integrity caveat: `run_manifest.json` records `recovered_after_failed_sqlite_tail: true` and states that training/evaluation completed, CSV artifacts were preserved, and the manifest was reconstructed without rerunning. The SQLite file is present and contains `exp15_seed_metrics` and `exp15_model_runtime`, but its `run_manifest` table is empty. This is not evidence that the metrics are invalid, because all 1,080 progress units completed and the CSV/database metric rows are complete; however, it is a provenance wrinkle that should be explicitly documented. If Exp15 becomes a central manuscript table, consider a clean rerun after fixing the final SQLite manifest-write path, or document that CSV artifacts are authoritative and the manifest was reconstructed.

### Hardest-slice metric summary

Hardest summarized slice: `world_count=32`, `route_length=12`, `n_seeds=10`.

| Variant | First-step context conflict | Retention after sequential worlds | Seen route composition | Suffix route composition | Transition accuracy |
|---|---:|---:|---:|---:|---:|
| `neural_gru_endpoint_context` | 0.0000 | 0.7015 | 0.9990 | 0.4040 | 0.0232 |
| `neural_gru_endpoint_no_context` | 0.0000 | 0.0231 | 0.0312 | 0.0149 | 0.0009 |
| `neural_gru_rollout_context` | 0.8794 | 0.0612 | 0.0448 | 0.0777 | 0.5122 |
| `neural_gru_rollout_no_context` | 0.0312 | 0.0222 | 0.0008 | 0.0437 | 0.4350 |
| `neural_transformer_sequence_context` | 0.0000 | 0.3309 | 0.5435 | 0.1184 | 0.0070 |
| `neural_transition_mlp_context` | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| `neural_transition_mlp_no_context` | 0.0312 | 0.5156 | 0.0312 | 1.0000 | 0.9193 |
| `neural_transition_mlp_replay_context` | 0.0086 | 0.0005 | 0.0005 | 0.0004 | 0.0120 |
| `neural_transition_mlp_world_heads_context` | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |

Hardest-slice 95% CI examples:

- `neural_gru_endpoint_context`: seen composition 0.9990 ± 0.0016; suffix composition 0.4040 ± 0.0340; retention 0.7015 ± 0.0172.
- `neural_gru_rollout_context`: first-step context conflict 0.8794 ± 0.0142; transition accuracy 0.5122 ± 0.0195; suffix composition 0.0777 ± 0.0088.
- `neural_transformer_sequence_context`: seen composition 0.5435 ± 0.0587; suffix composition 0.1184 ± 0.0109; retention 0.3309 ± 0.0314.
- `neural_transition_mlp_context` and `neural_transition_mlp_world_heads_context`: 1.0000 ± 0.0000 on all hard-slice metrics.
- `neural_transition_mlp_replay_context`: near-zero on all hard-slice metrics.

### Primary hypotheses

#### Hypothesis 1: Endpoint neural sequence models can memorize seen supplied-context routes but will not necessarily learn reusable transition structure.

Result: Supported for the endpoint families.

Evidence: At the hardest slice, `neural_gru_endpoint_context` achieved 0.9990 seen-route composition but only 0.4040 suffix-route composition and 0.0232 transition accuracy. `neural_transformer_sequence_context` achieved 0.5435 seen-route composition, 0.1184 suffix-route composition, and 0.0070 transition accuracy.

Caveat: Endpoint models and transition models answer different questions. This is not a statement about all possible Transformers or GRUs under tuned architecture/search; it is evidence for these deliberately small fixed baselines.

Status: supported.

#### Hypothesis 2: Explicitly context-conditioned transition learning can solve the symbolic route-memory task under this supervised setup.

Result: Supported.

Evidence: At the hardest slice, both `neural_transition_mlp_context` and `neural_transition_mlp_world_heads_context` reached 1.0000 for transition accuracy, seen-route composition, suffix-route composition, first-step context conflict accuracy, and retention after sequential worlds.

Caveat: This weakens any broad claim that ordinary neural models cannot solve the benchmark. The correct interpretation is that a simple supervised transition learner can solve the symbolic transition table when context is supplied. CIRM should therefore be framed as an interpretable mechanism and benchmark decomposition, not as universal neural-performance superiority.

Status: supported.

#### Hypothesis 3: Removing context/world identity should fail context-conflict probes.

Result: Supported, with an important refinement.

Evidence: At the hardest slice, no-context variants were at or near chance on first-step context conflict accuracy: `neural_gru_endpoint_no_context` 0.0000, `neural_gru_rollout_no_context` 0.0312, and `neural_transition_mlp_no_context` 0.0312. This aligns with the generator design: worlds share starts and actions but conflict on the first transition.

Caveat: `neural_transition_mlp_no_context` nevertheless achieved 1.0000 suffix-route composition and 0.9193 transition accuracy at the hard slice. This means context is required for the deliberately conflicting first transition and full seen-route disambiguation, not for every suffix transition. The manuscript should phrase this as context necessity under incompatible local transitions, not as a blanket requirement for all route composition.

Status: supported, but claim wording must be narrowed.

#### Hypothesis 4: Small recurrent rollout and Transformer sequence models will not fully reproduce CIRM-like storage/composition/retention behavior under the bounded profile.

Result: Partially supported.

Evidence: `neural_gru_rollout_context` learned some context-sensitive transition behavior at the hard slice: first-step conflict accuracy 0.8794 and transition accuracy 0.5122. But it did not convert that into strong multi-step composition: seen-route composition 0.0448, suffix-route composition 0.0777, retention 0.0612. The Transformer endpoint baseline remained modest: seen-route composition 0.5435, suffix-route composition 0.1184, retention 0.3309.

Caveat: These are small, fixed-hyperparameter models with 20 epochs and no architecture search. Do not generalize to all recurrent or attention models.

Status: partially supported.

#### Hypothesis 5: Bounded replay protects route memory under sequential-world training.

Result: Not supported by this implementation/run.

Evidence: `neural_transition_mlp_replay_context` collapsed in the hard slice: transition accuracy 0.0120, seen-route composition 0.0005, suffix-route composition 0.0004, first-step context conflict accuracy 0.0086, retention 0.0005.

Caveat: This result is surprising enough that it should be treated as requiring implementation audit before it becomes a scientific claim about replay. The configured replay buffer was `replay_buffer_worlds=3`, which may be insufficient at 32 worlds, or the sequential/replay training path may have a bug or undertraining failure. Do not cite this as general evidence that replay fails.

Status: not supported / requires audit.

#### Hypothesis 6: Parameter isolation can trivially solve context-separated route memory when world identity is supplied.

Result: Supported.

Evidence: `neural_transition_mlp_world_heads_context` reached 1.0000 across all hard-slice metrics, matching `neural_transition_mlp_context`.

Caveat: Parameter isolation is a conventional neural control, not a biological claim. It clarifies that explicit capacity isolation can remove interference in this symbolic setup.

Status: supported.

## 5. Key scientific conclusions supported by this thread

### Result 1: Exp15 resolves the “neural baselines absent” gap, but not by proving CIRM superiority.

Claim: The repository can now treat Exp15 as a completed minimal neural comparator once artifacts are imported.

Evidence: Full run completed all 1,080 units, validation passed, seed metrics contain 5,400 rows, and all requested seeds/variants/world-counts/route-lengths are present.

Caveat: The neural comparator is deliberately minimal. It lacks architecture search, larger models, memory-augmented/key-value neural baselines, and a route length 16 profile. It should satisfy a minimal reviewer-facing baseline gap, not a comprehensive neural benchmarking standard.

Source artifact: `validation_report.md`, `run_manifest.json`, `exp15_seed_metrics.csv`, `exp15_summary.csv`.

Manuscript status: Strong for minimal baseline coverage; not sufficient for broad neural-superiority claims.

### Result 2: Endpoint memorization is separable from reusable transition composition.

Claim: Endpoint models can perform well on seen full routes without learning the transition table or robust suffix composition.

Evidence: `neural_gru_endpoint_context` reached 0.9990 seen-route composition but only 0.4040 suffix-route composition and 0.0232 transition accuracy at the hard slice. The Transformer endpoint model was weaker but showed the same qualitative split: 0.5435 seen-route composition, 0.1184 suffix-route composition, 0.0070 transition accuracy.

Caveat: Endpoint and transition models optimize different objectives. The result supports a decomposition claim, not a universal model ranking.

Source artifact: `exp15_summary.csv`; `plots/exp15_seen_vs_suffix_composition.png`.

Manuscript status: Strong as baseline/decomposition evidence.

### Result 3: A simple context-conditioned transition MLP solves the clean symbolic benchmark.

Claim: A conventional neural transition-table learner can solve this symbolic task when context/world identity is supplied.

Evidence: `neural_transition_mlp_context` achieved 1.0000 on all hard-slice metrics, as did the world-heads parameter-isolated variant.

Caveat: This refines the paper’s posture. CIRM should not claim that neural baselines cannot solve the benchmark. Instead, the contribution is the mechanistic decomposition of storage, context indexing, recurrent execution, capacity/failure boundaries, and interpretability.

Source artifact: `exp15_summary.csv`; `exp15_context_conflict_accuracy.png`; `exp15_retention_after_sequential_worlds.png`.

Manuscript status: Strong, but claim-narrowing required.

### Result 4: Context is necessary for deliberately incompatible first-step mappings, but not for every suffix transition.

Claim: World/context identity is required where the local cue is ambiguous across worlds.

Evidence: No-context variants failed first-step conflict probes at the hard slice: `neural_gru_endpoint_no_context` 0.0000, `neural_gru_rollout_no_context` 0.0312, `neural_transition_mlp_no_context` 0.0312. However, `neural_transition_mlp_no_context` reached 1.0000 suffix-route composition and 0.9193 transition accuracy, implying many suffix transitions are shared/non-conflicting.

Caveat: Existing C2 wording should avoid saying context is always required for route composition. The supported claim is that context/world indexing resolves incompatible local transitions and full-route disambiguation when starts/actions conflict.

Source artifact: `exp15_summary.csv`; `plots/exp15_context_conflict_accuracy.png`; `plots/exp15_seen_vs_suffix_composition.png`.

Manuscript status: Strong, but wording must be refined.

### Result 5: Recurrent rollout partially learns context-conflict behavior but fails long multi-step execution in this small fixed profile.

Claim: The GRU rollout baseline learns some one-step/context-sensitive structure but suffers compounding errors or insufficient transition learning during route execution.

Evidence: At the hard slice, `neural_gru_rollout_context` achieved first-step context conflict accuracy 0.8794 and transition accuracy 0.5122, but seen-route composition 0.0448, suffix composition 0.0777, and retention 0.0612.

Caveat: This should be phrased as a result for the bounded comparator, not as a statement that GRUs cannot solve route-memory tasks.

Source artifact: `exp15_summary.csv`; `plots/exp15_route_length_scaling.png`.

Manuscript status: Promising baseline evidence; likely supplement or baseline table.

### Result 6: Replay variant failure is a red flag, not a clean scientific conclusion.

Claim: The specific bounded replay transition MLP failed under this full profile.

Evidence: At hard slice, `neural_transition_mlp_replay_context` was near zero on all metrics.

Caveat: Requires code/path audit before interpretation. It may reflect a bug, insufficient replay buffer, undertraining, or a meaningful sequential-interference failure. Do not use as a strong manuscript claim without audit.

Source artifact: `exp15_summary.csv`; `exp15_model_runtime.csv`; `run_manifest.json`; source code audit pending.

Manuscript status: Needs implementation audit before central use.

## 6. Important flaws, mistakes, or implementation concerns identified

1. **Final SQLite manifest-write failure / reconstructed manifest.** The manifest explicitly says the run was recovered after completing all units but failing during the final SQLite manifest write. CSV artifacts appear complete, but the SQLite `run_manifest` table is empty. Repository import should record this exactly.

2. **Replay failure requires audit.** The replay transition MLP result is severe enough to require source-code review before being interpreted scientifically.

3. **No route length 16.** The full profile intentionally omitted route length 16. This is acceptable for a bounded comparator but should be stated if comparing to Exp14 or earlier route-length-16 hard slices.

4. **No architecture search.** Fixed small neural models and hyperparameters are a strength for bounded reviewer response but a limitation for broad claims.

5. **No memory-augmented neural baseline.** The optional key-value / memory-augmented lookup baseline was intentionally omitted. Add only if target reviewers require it.

6. **Suffix metric interpretation is subtle.** Because only the first transition is world-specific/conflicting, suffix-route success does not necessarily imply context-sensitive full-route execution. The no-context MLP’s perfect suffix composition exposes this clearly.

7. **Effect-size infinities.** Some Cohen’s d values are infinite because one side has zero variance at ceiling/floor. Effect-size tables should be treated as compact directional comparisons, not exact magnitude claims.

8. **Uploaded bundle does not itself include source `.py` and `.ps1` files.** The validation report says they existed during validation; Codex should verify them in the repository. Do not infer local source state only from the uploaded artifact bundle.

## 7. Figures or artifacts referenced

### `plots/exp15_seen_vs_suffix_composition.png`

What it shows: Hard-slice seen vs suffix composition by neural variant.

Claim it may support: Endpoint memorization and transition composition are separable. GRU endpoint context nearly solves seen routes but only partially composes suffix routes; Transformer endpoint is weaker; transition MLP context and world-heads solve both; no-context MLP solves suffix but not seen conflict-sensitive routes.

Caveat: The no-context MLP’s suffix success means suffix routes do not fully test first-step context conflict. This plot is scientifically useful but needs careful captioning.

Status: Strong supplemental/baseline figure; possible main baseline panel only with final figure script and precise caption.

### `plots/exp15_context_conflict_accuracy.png`

What it shows: Hard-slice first-step context-conflict accuracy.

Claim it may support: Context/world identity is necessary when the local transition cue conflicts across worlds. Context MLP and world-heads solve it; no-context variants remain at chance/floor; GRU rollout context partially solves; endpoint models do not solve first-step transition disambiguation.

Caveat: Endpoint models are not trained for one-step transition prediction, so their failure should not be overinterpreted as a model-family failure.

Status: Strong baseline/context-disambiguation figure; candidate supplement or main baseline panel.

### `plots/exp15_retention_after_sequential_worlds.png`

What it shows: Hard-slice retention under sequential-world probe.

Claim it may support: Context MLP and parameter isolation show stable retention in the tested setting; endpoint context has partial retention; Transformer partial; rollout and replay collapse.

Caveat: Replay collapse needs audit. Retention metric must be interpreted alongside training regime differences.

Status: Promising, but replay caveat makes it better as supplementary until audited.

### `plots/exp15_route_length_scaling.png`

What it shows: Suffix-route composition across route lengths at `world_count=32`.

Claim it may support: Transition MLP context/no-context/world-heads remain stable on suffix composition; GRU rollout degrades with length; endpoint context remains around 0.4; replay collapses with route length.

Caveat: Suffix routes do not necessarily include first-step world conflict, so this is a composition/stability plot, not a context-disambiguation plot.

Status: Useful supplemental scaling plot; not a main claim figure without caption cleanup.

### `plots/exp15_world_count_scaling.png`

What it shows: Suffix-route composition across world counts at `route_length=12`.

Claim it may support: Transition MLP context and no-context variants reach 1.0 for suffix composition at world counts 8, 16, and 32; world-heads also reach 1.0; replay collapses as world count increases.

Caveat: Some curves behave counterintuitively because suffix composition is not the same as conflict-sensitive full-route execution. Use with caution.

Status: Supplementary only unless regenerated with clearer metric panels.

## 8. Decisions made

1. Treat Exp15 as a completed full run for repository-import purposes, with the reconstructed-manifest caveat.
2. Do not rerun immediately unless a clean SQLite manifest is required for manuscript provenance or the replay variant is intended as a claim.
3. Use Exp15 primarily to update C12/neural-baseline coverage and to refine C2/C4 wording.
4. Do not use Exp15 to claim CIRM outperforms all neural models. The context transition MLP and world-heads solve the benchmark.
5. Treat the replay variant as requiring audit before use as scientific evidence.
6. Treat existing Exp15 plots as analysis figures, not final manuscript figures, until a source-data-backed manuscript asset script imports them.

## 9. Open questions

1. Why does `neural_transition_mlp_replay_context` collapse so severely? Is this intended sequential-interference behavior, insufficient replay-buffer coverage, undertraining, or an implementation issue?
2. Should a memory-augmented/key-value neural baseline be added if the target venue is ML-heavy?
3. Should route length 16 be added for a more direct comparison with Exp14 hard-slice convention?
4. Should the full run be repeated after fixing the final SQLite manifest-write path?
5. Should baseline reporting use hard-slice values only, or a table stratified by model family, training regime, and metric family?
6. Should manuscript figures include Exp15 as a main figure/table, or keep it in supplemental baseline coverage?

## 10. Relationship to first manuscript

Exp15 materially changes the manuscript baseline posture. Before this run, the repository state said neural baselines were absent and Exp15 was awaiting local results. After import, C12 can be updated from “neural baselines absent/planned” to “minimal neural comparator completed, with fixed-profile limitations.”

However, Exp15 also forces narrower language. It shows that a simple supervised transition MLP with supplied context and a world-head parameter-isolated neural control can solve the clean symbolic route-memory task. Therefore, the first manuscript should not claim broad CIRM superiority over neural networks. A safer spine is:

- CIRM provides an interpretable route-memory mechanism and benchmark decomposition.
- Structural storage, context/world indexing, recurrence, capacity, and failure modes are separable in the CIRM experiments.
- Endpoint memorization alone is not enough for transition composition.
- Context/world identity is required for deliberately incompatible local transitions.
- Conventional neural transition learners can solve the clean symbolic transition table when given explicit context, so the contribution is mechanistic interpretation and controlled decomposition rather than raw performance dominance.

Suggested manuscript placement:

- Methods: neural baseline definitions, training regimes, fixed hyperparameters, profiles.
- Results or supplement: “Minimal neural comparator” table/figure.
- Discussion: limits of baseline coverage; why transition MLP success narrows the claims; why endpoint-vs-transition results support decomposition.
- Limitations: synthetic symbolic benchmark, no architecture search, no memory-augmented neural baseline, replay audit pending, reconstructed manifest caveat.

## 11. Claims-and-evidence rows contributed by this thread

| Claim | Evidence | Caveat | Experiment(s) | Artifact(s) | Manuscript status |
|---|---|---|---|---|---|
| Minimal neural comparator coverage now exists for the route-memory benchmark. | Full profile completed 1,080/1,080 units; validation PASS 42/WARN 0/FAIL 0; 5,400 metric rows and 1,080 runtime rows present. | Manifest was reconstructed after final SQLite-tail failure; SQLite `run_manifest` table is empty; local artifact paths need repository verification. | Exp15 | `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/validation_report.md`; `run_manifest.json`; `exp15_seed_metrics.csv`; `exp15_summary.csv` | Strong for baseline coverage; provenance caveat. |
| Endpoint memorization and transition composition are separable. | At hard slice, GRU endpoint context: seen 0.9990, suffix 0.4040, transition 0.0232. Transformer endpoint: seen 0.5435, suffix 0.1184, transition 0.0070. | Endpoint models optimize endpoint prediction; do not overgeneralize beyond fixed small baselines. | Exp15 | `exp15_summary.csv`; `plots/exp15_seen_vs_suffix_composition.png` | Strong baseline/decomposition evidence. |
| A context-conditioned neural transition learner can solve the clean symbolic benchmark. | `neural_transition_mlp_context` and `neural_transition_mlp_world_heads_context` reached 1.0000 on all hard-slice metrics. | Weakens any broad claim of CIRM performance superiority; supports mechanism framing instead. | Exp15 | `exp15_summary.csv`; `exp15_effect_sizes.csv` | Strong; requires claim narrowing. |
| Context/world identity is necessary for deliberately incompatible first-step transitions. | No-context variants were floor/chance on first-step conflict accuracy at hard slice: 0.0000 or 0.0312, while context MLP/world-heads were 1.0000. | No-context transition MLP still solved suffix composition, so context necessity is conflict-specific rather than universal for all composition. | Exp15 | `exp15_summary.csv`; `plots/exp15_context_conflict_accuracy.png` | Strong, but wording must be precise. |
| Small GRU rollout learns some transition/context signal but does not robustly compose long routes in this fixed profile. | Hard slice GRU rollout context: first-step conflict 0.8794, transition 0.5122, suffix composition 0.0777, retention 0.0612. | Fixed hyperparameters, small model, no architecture search. | Exp15 | `exp15_summary.csv`; `plots/exp15_route_length_scaling.png` | Promising / supplement. |
| Replay transition MLP failed in this run. | Hard slice replay variant near zero across all metrics. | Requires source-code and training-regime audit before scientific interpretation. | Exp15 | `exp15_summary.csv`; `exp15_model_runtime.csv`; source-code audit pending | Needs implementation audit; do not use centrally yet. |

## 12. Required repository updates

Update or create the following paths:

1. `docs/threads/experiment15_analysis_digest.md`
   - Import this digest from `docs/imports/experiment15_analysis_digest.zip`.

2. `docs/experiments/EXPERIMENT_REGISTRY.md`
   - Change Exp15 from planned/awaiting results to completed full-run neural baseline evidence.
   - Add artifact paths and integrity caveat.

3. `experiments/experiment15_neural_baseline_comparator/README.md`
   - Add a completed-runs/results section for `exp15_full_20260508_092811`.
   - Record validation PASS, run dimensions, key hardest-slice results, and the reconstructed-manifest caveat.

4. `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
   - Update C12 from neural-baseline absence to minimal neural comparator completed, but still not exhaustive.
   - Refine C2 wording: context is necessary for incompatible local transitions and first-step conflict, not for every suffix transition.
   - Refine C4 wording using endpoint-vs-transition evidence.
   - Add caveat to C1 if it could be read as “structural plasticity is required for all models.” Exp15 shows a conventional neural transition MLP can solve the clean symbolic transition task with context.

5. `docs/manuscript/LIMITATIONS_AND_THREATS.md`
   - Replace “neural baselines absent” language with “minimal neural baseline comparator completed; not exhaustive.”
   - Add fixed-hyperparameter/no-architecture-search limitation.
   - Add memory-augmented baseline omission as future work.
   - Add replay audit caution.
   - Add reconstructed-manifest provenance caveat if manuscript-critical.

6. `docs/manuscript/FIGURE_PLAN.md`
   - Add Exp15 baseline table/figure candidate.
   - Mark existing plots as analysis plots, not final manuscript figures.
   - Decide whether Exp15 is a main-text comparator table or supplement.

7. `docs/manuscript/MANUSCRIPT_TODO.md`
   - Mark neural-baseline run/import as completed after integration.
   - Add follow-ups: replay audit, optional memory-augmented baseline decision, final baseline figure/table generation.

8. `docs/synthesis/PUBLICATION_READINESS.md`
   - Update weakest-evidence section: neural baselines are no longer absent, but minimal/fixed-profile and not exhaustive.
   - Keep prior-art/novelty import and final figures as open.

9. `docs/synthesis/NEXT_EXPERIMENTS.md`
   - Remove or close the immediate “run Exp15” item.
   - Replace with “audit replay variant only if used” and “decide optional memory-augmented neural baseline based on target venue.”

10. `docs/source_data/SOURCE_DATA_MANIFEST.csv` and/or manuscript source-data files
    - Add Exp15 source-data mirrors if used for final figures/tables.

11. `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`
    - Create an import report summarizing files imported, docs updated, conflicts, verification status, and source-path validation results.

12. `docs/repo_audit/THREAD_IMPORT_CONFLICTS.md`
    - Add any conflicts between digest, current docs, and local artifact paths.

13. `scripts/verify_doc_source_paths.py`
    - Run after docs are updated.

## 13. Recommended next action

Recommended next action: repository integration, not another experiment.

Priority order:

1. Import `docs/imports/experiment15_analysis_digest.zip` and create `docs/threads/experiment15_analysis_digest.md`.
2. Copy or verify the local Exp15 artifacts under `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/` and `experiments/experiment15_neural_baseline_comparator/runs/exp15_full_20260508_092811.sqlite3`.
3. Update registry, README, claims/evidence, limitations, manuscript TODO, publication readiness, figure plan, and source-data manifest if needed.
4. Create `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`.
5. Run `python scripts/verify_doc_source_paths.py`.
6. Only after integration, decide whether a clean rerun or replay audit is needed. A full rerun is not mandatory for basic import, but a targeted replay audit is recommended before citing replay failure.

## 14. Import package checklist

- Zip filename: `experiment15_analysis_digest.zip`.
- Digest filename: `experiment15_analysis_digest.md`.
- Zip root placement: the zip contains exactly one markdown file at the root.
- Expected staging path: `docs/imports/experiment15_analysis_digest.zip`.
- Expected final path: `docs/threads/experiment15_analysis_digest.md`.
- The zip contains only thread-derived analysis.
- The zip does not contain generated repository updates.
- The zip does not contain the Codex import prompt.
- Codex prompt is separate and should be pasted manually.
- Paths needing verification:
  - all `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/...` paths;
  - `experiments/experiment15_neural_baseline_comparator/runs/exp15_full_20260508_092811.sqlite3`;
  - source scripts referenced by validation report: `run_experiment15.py`, `analyze_experiment15.py`, `validate_experiment15.py`, `start_exp15_validation.ps1`, `start_exp15_full.ps1`;
  - source-data mirror paths if Codex creates them;
  - any final manuscript asset paths if Codex updates figure/table manifests.
