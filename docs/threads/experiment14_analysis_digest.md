# Thread Digest: Experiment 14 Latent Context Inference

Digest filename: `experiment14_analysis_digest.md`
Intended repository path: `docs/threads/experiment14_analysis_digest.md`
Import package expected at: `docs/imports/experiment14_analysis_digest.zip`

## 1. Thread scope

This thread analyzed uploaded Experiment 14 artifacts for `exp14_latent_context_inference`. The analysis focused on whether Context-Indexed Route Memory can infer an active symbolic world/context from partial transition cues rather than being given an oracle world label, and how that latent selection degrades under stochastic cue corruption.

The uploaded artifact bundle was `e14_analysis.zip`. It contained smoke, validation, and full run outputs, six plots for each run profile, validation reports, progress logs, manifests/configs, summary/effect-size/metrics CSVs, and SQLite databases.

No GitHub write action was performed. The repository import should be handled by Codex using this digest plus local artifact verification.

## 2. Experiment analyzed or designed

- Experiment ID: Experiment 14
- Experiment name: Latent Context Inference
- Experiment directory: `experiments/experiment14_latent_context_inference/`
- Run profile: `full` is the manuscript-facing analyzed run; `smoke` and `validation` were also present and passed validation.
- Primary run ID: `exp14_full_20260507_210712`
- Additional run IDs: `exp14_smoke_20260507_210610`; `exp14_validation_20260507_210649`
- Uploaded artifact bundle: `e14_analysis.zip`
- Main local artifact paths, if known:
  - `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_report.md`
  - `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/experiment_report.md`
  - `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_report.md`
  - `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_results.json`
  - `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/run_manifest.json`
  - `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_config.json`
  - `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_metrics.csv`
  - `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/metrics.csv`
  - `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`
  - `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_effect_sizes.csv`
  - `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/progress.jsonl`
  - `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/plots/exp14_world_selection_vs_corruption.png`
  - `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/plots/exp14_seen_composition_vs_corruption.png`
  - `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/plots/exp14_suffix_composition_vs_corruption.png`
  - `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/plots/exp14_margin_vs_corruption.png`
  - `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/plots/exp14_cue_count_selection_sensitivity.png`
  - `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/plots/exp14_cue_count_composition_sensitivity.png`
- Per-run database path:
  - `experiments/experiment14_latent_context_inference/runs/exp14_full_20260507_210712.sqlite3`
  - `experiments/experiment14_latent_context_inference/runs/exp14_validation_20260507_210649.sqlite3`
  - `experiments/experiment14_latent_context_inference/runs/exp14_smoke_20260507_210610.sqlite3`

## 3. Experimental design discussed

Experiment 14 was designed as a direct follow-up to Exp13.2. Exp13.2 showed that clean supplied-context symbolic route memory is solvable by an oracle context-gated lookup table, so Experiment 14 removes the supplied world label at evaluation time and requires context/world selection from partial transition evidence before route execution.

The main model is `exp14_cirm_latent_selector`: a world-indexed structural route table selected from transition cues, followed by recurrent route execution. The comparator set includes an oracle context-gated table, shared no-context table, endpoint memorizer with the same latent selector, random selector, recency selector, and compact hash-slot selectors with context collisions.

The full profile used 20 seeds; world counts 4, 8, 16, and 32; route lengths 4, 8, 12, and 16; cue counts 1, 2, 4, and 8; corruption rates 0.0, 0.1, 0.25, and 0.5; 24 routes per world; one sampled suffix per route; and hash-slot divisors 2, 4, and 8.

The experiment remains symbolic and controlled. It is not evidence of raw perceptual latent-world discovery, solved continual learning, or a biological theory of hippocampal indexing.

## 4. Results analyzed

### Run integrity

The uploaded bundle contained 61 entries, including three run directories and three SQLite databases. The full run `exp14_full_20260507_210712` had:

- `exp14_metrics.csv`: 46,080 rows
- `exp14_summary.csv`: 2,304 rows
- `exp14_effect_sizes.csv`: 12,288 rows
- SQLite tables: `metrics`, `summary`, `effect_sizes`, `manifest`
- validation status: PASS, 27 pass, 0 warn, 0 fail
- progress log: 46,083 events including `run_complete`
- device/runtime metadata: Windows 10, CPU-only symbolic/table experiment, Python 3.12.10, NumPy 2.4.4, pandas 3.0.2, matplotlib 3.10.9, `gpu_used=false`

Smoke and validation profiles also passed with 27 pass, 0 warn, 0 fail.

### Hard clean setting

At the hard clean slice `world_count=32`, `route_length=16`, `cue_count=8`, `corruption_rate=0.0`:

- CIRM latent selector:
  - world-selection accuracy, seen route: 1.0000
  - seen-route composition accuracy: 1.0000
  - suffix-route composition accuracy: 1.0000
  - first-step context accuracy: 1.0000
- Oracle context-gated table:
  - seen-route composition accuracy: 1.0000
  - suffix-route composition accuracy: 1.0000
- Shared no-context table:
  - seen-route composition accuracy: 0.03125
  - first-step context accuracy: 0.03125
  - suffix-route composition accuracy: 1.0000
- Endpoint memorizer with latent selector:
  - seen-route composition accuracy: 1.0000
  - suffix-route composition accuracy: 0.0000
- Random selector:
  - seen-route composition accuracy: approximately 0.030664
- Recency selector:
  - seen-route composition accuracy: 0.03125

Interpretation: clean symbolic cues are sufficient for the CIRM latent selector to select the right world and execute routes at ceiling. This strengthens the claim that context-indexed storage can be selected from partial symbolic evidence. It does not show superiority over an oracle context-gated lookup table, because the oracle remains at ceiling.

### Hard highest-corruption setting

At `world_count=32`, `route_length=16`, `cue_count=8`, `corruption_rate=0.5`:

- CIRM latent selector:
  - world-selection accuracy, seen route: 0.941602
  - seen-route composition accuracy: 0.941602
  - suffix-route composition accuracy: 0.939193
  - mean world margin, seen route: 0.353825
  - mean world confidence, seen route: 0.502002
- Oracle context-gated table:
  - seen-route composition accuracy: 1.0000
  - suffix-route composition accuracy: 1.0000
- Endpoint memorizer with latent selector:
  - seen-route composition accuracy: 0.941602
  - suffix-route composition accuracy: 0.0000
- Shared no-context table:
  - seen-route composition accuracy: 0.03125
  - suffix-route composition accuracy: 1.0000
- Hash-slot selectors:
  - div2 / 16 slots: seen-route composition 0.464258; suffix-route composition 0.920638
  - div4 / 8 slots: seen-route composition 0.231185; suffix-route composition 0.904427
  - div8 / 4 slots: seen-route composition 0.114844; suffix-route composition 0.897917

Interpretation: stochastic cue corruption degrades latent context selection and downstream route execution, but the high-cue hard setting remains substantially above random/recency/no-context baselines. The oracle context-gated table remains an upper bound because it does not have to infer context from corrupted cue evidence.

### Cue-count sensitivity

For CIRM at `world_count=32`, `route_length=16`, `corruption_rate=0.25`:

| cue_count | seen composition | suffix composition | seen world selection | mean seen margin |
|---:|---:|---:|---:|---:|
| 1 | 0.747331 | 0.752409 | 0.747331 | 1.000000 |
| 2 | 0.751302 | 0.753971 | 0.751302 | 0.561198 |
| 4 | 0.956445 | 0.956510 | 0.956445 | 0.580469 |
| 8 | 0.999219 | 0.998763 | 0.999219 | 0.630184 |

Interpretation: more independent transition cues strongly improve latent context selection under moderate corruption. Cue-count sensitivity is one of the clearest manuscript-safe findings from Exp14.

### CIRM corruption sweep in the hard setting

For CIRM at `world_count=32`, `route_length=16`, `cue_count=8`:

| corruption_rate | seen composition | suffix composition | seen world selection | first-step context | mean seen margin | mean confidence |
|---:|---:|---:|---:|---:|---:|---:|
| 0.00 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 |
| 0.10 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.827767 | 0.899927 |
| 0.25 | 0.999219 | 0.998763 | 0.999219 | 0.999219 | 0.630184 | 0.749618 |
| 0.50 | 0.941602 | 0.939193 | 0.941602 | 0.941602 | 0.353825 | 0.502002 |

Interpretation: accuracy remains near ceiling through 0.25 corruption in this high-cue hard slice, but margin and confidence degrade monotonically. At 0.5 corruption, behavioral accuracy is still high but no longer ceiling. This supports a robustness-with-boundary framing, not a solved-noise claim.

## 5. Key scientific conclusions supported by this thread

### Claim 1

Claim: CIRM-style context-indexed route memory can select the correct symbolic world from partial transition evidence in clean conditions.

Evidence: In the full run, CIRM clean accuracy was 1.0000 across all clean combinations for seen-route composition, suffix-route composition, seen/suffix world selection, and first-step context accuracy. At the hard clean slice `world_count=32`, `route_length=16`, `cue_count=8`, CIRM achieved 1.0000 for seen-route world selection and composition.

Caveat: This is symbolic transition-cue inference, not autonomous context discovery from raw sensory streams.

Manuscript status: Promising / likely main or near-main evidence for refined C2 and a new latent-context subsection.

### Claim 2

Claim: Latent context selection introduces a real cost relative to oracle context gating under corrupted cue evidence.

Evidence: At `world_count=32`, `route_length=16`, `cue_count=8`, CIRM drops from 1.0000 seen-route composition at corruption 0.0 to 0.941602 at corruption 0.5, while the oracle context-gated table remains at 1.0000.

Caveat: The oracle is not a fair latent-selector baseline; it is an upper bound. This result should not be framed as a failure to beat oracle lookup.

Manuscript status: Strong caveat / claim refinement evidence.

### Claim 3

Claim: Multiple transition cues protect latent context selection under stochastic corruption.

Evidence: At `world_count=32`, `route_length=16`, `corruption_rate=0.25`, CIRM seen-route composition rises from 0.747331 with one cue to 0.956445 with four cues and 0.999219 with eight cues.

Caveat: The cue corruption process is synthetic. The non-monotonic and world-count-dependent behavior of some corruption conditions should be implementation-audited before over-interpreting the exact curve.

Manuscript status: Promising.

### Claim 4

Claim: Endpoint memorization can solve seen full-route endpoints when supplied the same latent context selector, but fails suffix composition completely.

Evidence: At the hard clean slice, the endpoint memorizer has seen-route composition 1.0000 and suffix-route composition 0.0000. Under `corruption_rate=0.5`, its seen-route composition follows CIRM selection accuracy at 0.941602, while suffix-route composition remains 0.0000.

Caveat: This baseline isolates whole-route endpoint memorization but is still symbolic and uses the same latent selector.

Manuscript status: Strong support for route execution/composition distinction; likely supplement or baseline panel.

### Claim 5

Claim: Shared no-context lookup fails the conflict-sensitive first-step/seen-route context query while suffix probes can be misleading.

Evidence: At `world_count=32`, `route_length=16`, `cue_count=8`, the shared no-context table has seen-route composition 0.03125 and first-step context accuracy 0.03125, but suffix-route composition 1.0000.

Caveat: Suffix probes can start after the disambiguating first transition, so suffix accuracy should not be used alone as evidence that no-context lookup is viable.

Manuscript status: Strong cautionary evidence; should refine Exp13.2 caveat and figure design.

### Claim 6

Claim: Compact hash-slot selectors expose context-compression/collision limits rather than world-selection failure alone.

Evidence: In the hard clean slice, hash-slot div2 / 16 slots has world-selection accuracy 1.0000 and suffix composition 1.0000, but seen-route composition 0.500000 and first-step context accuracy 0.500000. Div4 / 8 slots drops seen-route composition to 0.250000; div8 / 4 slots drops to 0.125000.

Caveat: The metrics suggest that the selector can identify the world, while compact slot collisions break conflict-sensitive route execution. This needs careful wording and perhaps a short implementation note.

Manuscript status: Promising supplement / capacity-resource interpretation.

## 6. Important flaws, mistakes, or implementation concerns identified

1. The uploaded artifacts are sufficient for scientific analysis, but the experiment code itself was not included in `e14_analysis.zip`. Codex should verify source code, scripts, and README alignment in `experiments/experiment14_latent_context_inference/` before treating the implementation as fully audited.

2. The repository registry may be stale relative to the experiment directory and artifacts. The fetched registry still described Exp14 as `not yet created` / `design only`, while the experiment README and LFS-backed artifacts appear to exist. This should be reconciled during import.

3. Shared no-context suffix-route accuracy is misleading. It reaches 1.0000 in the hard slice even while first-step/seen-route metrics are near chance. Manuscript figures must separate seen-route/first-step conflict metrics from suffix probes.

4. Hash-slot selectors can show high world-selection and suffix-route accuracy while seen-route composition degrades proportionally to collisions. This is not a generic selector failure. It is likely a compact-context collision effect.

5. The corruption model is synthetic. It supports cue-evidence sensitivity, not generic noisy context robustness. Do not treat Exp14 as an end-to-end noisy perception or latent-world discovery result.

6. At high corruption, accuracy behavior varies with world count in a way that may be a property of the synthetic corruption/voting process. This should not be biologically interpreted without an implementation note and possibly an expected-theory sanity derivation.

7. No neural baseline is added by Exp14. C12 remains only partially satisfied by Exp13.2 and Exp14's symbolic/algorithmic comparators.

8. Exp14 does not resolve the Exp13.1 lesion diagnostic failure, primitive unseen-transition cleanup, consolidation dose-response question, prior-art import, or final figure reproducibility requirement.

## 7. Figures or artifacts referenced

### `exp14_world_selection_vs_corruption.png`

Shows latent world-selection accuracy as cue corruption increases at the hard plotted slice. CIRM remains near ceiling at corruption 0.0 through 0.25 and degrades at 0.5; random/recency remain near chance; oracle remains ceiling. Use as a main or near-main figure candidate if Exp14 becomes part of the manuscript spine. Caveat: symbolic stochastic corruption only.

### `exp14_seen_composition_vs_corruption.png`

Shows downstream seen-route composition after latent context selection. CIRM tracks its world-selection curve; oracle remains ceiling; shared no-context and chance baselines remain low; endpoint memorizer follows seen-route selection because it memorizes whole routes. Good main-panel candidate for latent-selection result. Caveat: seen-route success alone does not rule out endpoint memorization.

### `exp14_suffix_composition_vs_corruption.png`

Shows suffix-route composition. CIRM remains high but degrades under corruption; endpoint memorizer stays at 0.0; shared no-context can appear strong in suffix probes. Use carefully, likely paired with seen-route and first-step panels. Caveat: suffix probes can hide first-step context conflict.

### `exp14_margin_vs_corruption.png`

Shows world-selection margin declining monotonically under cue corruption. This is useful for mechanism/diagnostic interpretation, especially because margins fall before or alongside accuracy degradation. Good supplement or mechanism panel.

### `exp14_cue_count_selection_sensitivity.png`

Shows that more cues improve world selection under fixed corruption. Strong candidate figure for the key Exp14 contribution.

### `exp14_cue_count_composition_sensitivity.png`

Shows downstream seen-route composition improving with more cues. Good companion to the selection-sensitivity panel.

## 8. Decisions made

- Treat Exp14 as a completed analysis run with all uploaded profiles passing validation.
- Use the full profile `exp14_full_20260507_210712` as the manuscript-facing source of evidence.
- Do not use Exp14 to claim solved latent-world discovery, raw sensory inference, biological explanation, or superiority over oracle context-gated lookup.
- Use Exp14 to refine C2 and C10 and to reduce the oracle-context limitation by showing latent selection from symbolic cues.
- Keep C12 only partially satisfied; Exp14 remains symbolic/algorithmic and does not replace prior-art import or neural baselines.
- Import this thread digest before strengthening claims in manuscript docs.

## 9. Open questions

1. Should Exp14 become a main result or remain a supplementary latent-context bridge?
2. Does the first manuscript need latent-context inference, or is Exp14 stronger as a follow-up/future-work result after Exp13.2?
3. Should a short theoretical expectation be added for cue-count/corruption behavior under the synthetic corruption process?
4. Should additional neural baselines be run before submission?
5. Should final figure scripts regenerate Exp14 panels as publication-grade source-data-backed figures?
6. Should hash-slot collision behavior be summarized as a separate capacity/resource result, or treated only as a baseline caveat?

## 10. Relationship to first manuscript

Exp14 is valuable because it directly addresses the oracle context/world-label limitation exposed by Exp13.2. It does not overturn the manuscript spine, but it refines it:

- The clean supplied-context benchmark is still solvable by oracle lookup.
- CIRM's more interesting claim becomes the combination of context-indexed storage, recurrent execution, and context selection from evidence.
- Exp14 is the first completed run in this sequence that demonstrates latent symbolic context selection rather than supplied oracle context labels.
- The result is still symbolic and should not be used to claim end-to-end latent-world discovery.

Potential manuscript placement:

- Main figure if the manuscript needs to answer the reviewer criticism “you are just giving it a context label.”
- Supplement if the first manuscript remains focused on mechanism decomposition, finite capacity, and baseline framing.
- Limitations section should still state that the task uses symbolic transition cues, not perception.

## 11. Claims-and-evidence rows contributed by this thread

| Claim | Evidence | Caveat | Experiment(s) | Artifact(s) | Manuscript status |
|---|---|---|---|---|---|
| Context-indexed route memory can infer the active symbolic world from clean transition cues. | CIRM has 1.0000 clean seen/suffix composition and world selection across the clean full-run grid; hard clean slice is 1.0000. | Symbolic transition-cue inference, not raw sensory latent-world discovery. | Exp14 | `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `validation_report.md`; `exp14_report.md` | Promising / candidate main |
| Latent selection incurs a measurable cost relative to oracle context gating under corrupted cue evidence. | At world_count=32, route_length=16, cue_count=8, corruption=0.5, CIRM seen composition is 0.941602 while oracle remains 1.0000. | Oracle is an upper bound, not a fair non-oracle selector. | Exp14 | `exp14_summary.csv`; `exp14_effect_sizes.csv`; `exp14_seen_composition_vs_corruption.png` | Strong caveat / claim refinement |
| More transition cues improve latent context selection under stochastic corruption. | At world_count=32, route_length=16, corruption=0.25, CIRM seen composition rises from 0.747331 with one cue to 0.999219 with eight cues. | Synthetic corruption process; exact curve should not be over-generalized. | Exp14 | `exp14_summary.csv`; `exp14_cue_count_selection_sensitivity.png`; `exp14_cue_count_composition_sensitivity.png` | Promising |
| Endpoint memorization is separable from recurrent suffix composition. | Endpoint memorizer gets seen-route composition 1.0000 at clean hard slice but suffix composition 0.0000; under corruption 0.5 suffix remains 0.0000. | Uses the same latent selector; symbolic control only. | Exp14 | `exp14_summary.csv`; `exp14_suffix_composition_vs_corruption.png` | Strong baseline/supplement |
| Shared no-context lookup failure should be evaluated on seen-route/first-step conflict-sensitive metrics, not suffix probes alone. | At hard clean slice, shared no-context seen composition and first-step context are 0.03125, while suffix composition is 1.0000. | Suffix routes can bypass first-step conflicts. | Exp14, Exp13.2 | `exp14_summary.csv`; `exp14_seen_composition_vs_corruption.png`; `exp14_suffix_composition_vs_corruption.png` | Strong cautionary evidence |
| Compact context collisions degrade conflict-sensitive seen-route execution even when selection metrics can look high. | At hard clean slice, hash div2/16 slots has world selection 1.0000 but seen composition 0.500000; div4/8 slots seen composition 0.250000; div8/4 slots seen composition 0.125000. | Needs careful explanation of slot collisions versus world-selection accuracy. | Exp14 | `exp14_summary.csv`; `exp14_effect_sizes.csv` | Promising supplement |

## 12. Required repository updates

Update or verify:

- `experiments/experiment14_latent_context_inference/README.md`
- `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/` artifact inventory
- `experiments/experiment14_latent_context_inference/runs/exp14_full_20260507_210712.sqlite3`
- `docs/threads/THREAD_INDEX.md`
- `docs/experiments/EXPERIMENT_REGISTRY.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/synthesis/PROJECT_STATUS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/synthesis/NEXT_EXPERIMENTS.md`
- `docs/source_data/` if small source-data mirrors are created
- `docs/repo_audit/THREAD_IMPORT_CONFLICTS.md` if any stale/inconsistent docs are encountered
- `docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md`

After import, run:

```bash
python scripts/verify_doc_source_paths.py
```

## 13. Recommended next action

Immediate next action: repository integration of Exp14 analysis digest and artifact references, followed by doc-source-path verification.

Scientific next action after import: decide whether Exp14 belongs in the first manuscript as a main result that answers the oracle-context criticism, or whether it should remain a supplement/follow-up while the manuscript first resolves prior-art import, neural baseline decisions, lesion audit, holdout cleanup, and final reproducible figures.

Do not rerun Exp14 immediately unless the code audit finds implementation issues or the corruption model requires a targeted sanity rerun.

## 14. Import package checklist

- Zip filename: `experiment14_analysis_digest.zip`
- Digest filename: `experiment14_analysis_digest.md`
- Zip root placement: the zip contains exactly one markdown file at the root.
- Final repository digest path: `docs/threads/experiment14_analysis_digest.md`
- Import package staging path: `docs/imports/experiment14_analysis_digest.zip`
- Contents: thread-derived analysis only; no generated repo updates.
- Codex import prompt: separate from the zip; not included in the zip.
- Paths needing verification:
  - Whether all Exp14 artifacts are already present under `experiments/experiment14_latent_context_inference/` or must be staged from the uploaded bundle.
  - Whether `docs/experiments/EXPERIMENT_REGISTRY.md` still marks Exp14 as design-only.
  - Whether the SQLite database is tracked or local-only/LFS-backed.
  - Whether all plot, CSV, and manifest paths pass `python scripts/verify_doc_source_paths.py`.
