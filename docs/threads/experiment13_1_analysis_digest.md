# Thread Digest: Experiment 13.1 Publication-Hardening Route-Field Memory Audit

Digest filename: `experiment13_1_analysis_digest.md`
Intended repository path: `docs/threads/experiment13_1_analysis_digest.md`
Import package expected at: `docs/imports/experiment13_1_analysis_digest.zip`

## 1. Thread scope

This thread analyzed the completed full-run artifacts for **Experiment 13.1** in the Context-Indexed Route Memory research program. The purpose was to inspect the uploaded analysis bundle, assess run integrity, evaluate hypotheses, identify supported and unsupported claims, interpret figures and metrics, and determine what should or should not be carried forward into the first manuscript.

The thread did **not** design a new experiment in detail. It analyzed a completed run and recommended a follow-up audit/rerun focused on lesion diagnostics, recurrence-ablation definitions, harder stress settings, and baseline comparison.

## 2. Experiment analyzed or designed

- **Experiment ID:** Experiment 13.1
- **Experiment name:** `exp13_1_publication_hardening`
- **Experiment directory:** `experiments/experiment13_1_publication_hardening/`
- **Run profile:** `full`
- **Run ID:** `exp13_1_full_20260506_214756`
- **Uploaded artifact bundle:** `exp13_1_full_20260506_214756.zip`
- **Main local artifact paths, if known:**

```text
experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/metrics.csv
experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_metrics.csv
experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_summary.csv
experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv
experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_ablation_metrics.csv
experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_context_corruption.csv
experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_lesion_metrics.csv
experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv
experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_freeze_plasticity.csv
experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/run_manifest.json
experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/validation_report.md
experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/validation_results.json
experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/progress.jsonl
```

- **Plots referenced:**

```text
experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/plots/exp13_1_budget_consolidation.png
experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/plots/exp13_1_composition_accuracy.png
experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/plots/exp13_1_context_confusion.png
experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/plots/exp13_1_lesion_sensitivity.png
experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/plots/exp13_1_recurrence_ablation.png
experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/plots/exp13_1_route_table_accuracy.png
```

- **Per-run database path, if applicable:**

```text
experiments/experiment13_1_publication_hardening/runs/exp13_1_full_20260506_214756.sqlite3
```

Validation indicated that this SQLite database existed locally, but the database file was **not included in the uploaded bundle**. Repository status: `local verification pending`.

## 3. Experimental design discussed

### Purpose

Experiment 13.1 was treated as a **publication-hardening audit** for the Context-Indexed Route Memory program. It tested whether the route-field memory mechanism survives internal ablation and diagnostic scrutiny before inclusion in the first manuscript.

### Hypotheses discussed

1. Plastic route-field structure can support clean multi-step memory/composition.
2. Recurrence is required for composed route traversal.
3. Structural plasticity is required for route storage and route-memory behavior.
4. Context/mode binding is required for selecting the correct memory world.
5. World-gated plasticity may be required under multi-world conditions.
6. Targeted critical-edge lesions should impair composition more than matched random lesions.
7. Finite route-field budgets should produce degradation.
8. Local route-field budgets should be more harmful than global route-field budgets.
9. Consolidation should affect stability/plasticity and possibly budget robustness.
10. Freezing plasticity should preserve old worlds while blocking new acquisition.

### Variants/baselines discussed

Observed variants included:

```text
exp13_1_full_model
exp13_1_no_recurrence_at_eval
exp13_1_no_recurrence_throughout
exp13_1_no_structural_plasticity
exp13_1_no_context_binding
exp13_1_no_world_gated_plasticity
exp13_1_no_consolidation
exp13_1_weak_consolidation
exp13_1_aggressive_consolidation
```

No external neural-network or symbolic baselines were analyzed in this thread. This was identified as a limitation.

### Metrics discussed

Metrics included:

- composition accuracy;
- route-table accuracy;
- stored edge count;
- used edge fraction;
- context confusion;
- context corruption sensitivity;
- lesion sensitivity;
- route margin;
- budget-constrained performance;
- freeze/plasticity old-world versus new-world performance;
- validation PASS/WARN/FAIL counts.

### Run profiles

The analyzed run used the `full` profile.

Observed run details:

```text
Run ID: exp13_1_full_20260506_214756
Profile: full
Seeds: 20
Seed range: 0–19
Nodes: 32
Modes: 3
Route lengths: 1, 2, 4, 8, 12, 16
Rows: 3000
Elapsed time: approximately 29,602 seconds, about 8.2 hours
Validation: PASS 27, WARN 0, FAIL 0
```

### Expected outcomes

Expected positive outcomes included:

- full model solves clean composition;
- no-recurrence variants fail composition while possibly preserving local route-table accuracy;
- no-structural-plasticity fails storage and performance;
- no-context-binding fails context/world selection;
- targeted critical-edge lesion is more damaging than random matched lesion;
- constrained budgets degrade performance;
- freeze preserves old worlds and blocks new learning.

### Implementation notes

The thread identified that the artifact-level validation passed cleanly. It also noted that repository documentation should use repo-relative `experiments/...` paths rather than Windows absolute paths.

### Known risks

The thread identified the following risks:

- full-model task saturation;
- lack of external baselines;
- missing uploaded SQLite database;
- absent GPU/device metadata;
- suspicious targeted-lesion result;
- no-recurrence-at-eval and no-recurrence-throughout appearing numerically identical;
- no-world-gated-plasticity performing identically to the full model;
- context dropout/bleed not reducing composition accuracy despite wrong-world injection causing collapse.

## 4. Results analyzed

### Result 1: Full model solves clean route composition

**Claim:** The full model solves the clean route-composition task across tested route lengths.

**Evidence:** Composition accuracy was 1.0000 across route lengths 1, 2, 4, 8, 12, and 16. Route-table accuracy was also 1.0000.

**Caveat:** The task saturated completely, so this supports capability in the harness but not broad generalization or difficult capacity scaling.

**Source artifact:**  
`experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`

**Thread status:** Promising.

---

### Result 2: Recurrence is required for composed traversal

**Claim:** Recurrent evaluation is required for multi-step composition.

**Evidence:** At route length 12, the full model had composition accuracy 1.0000 and route-table accuracy 1.0000. The no-recurrence-at-eval variant had route-table accuracy 1.0000 but composition accuracy approximately 0.0413.

**Caveat:** This supports evaluation-time recurrence. It does not cleanly establish that recurrence during training/formation is necessary.

**Source artifact:**  
`experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`

**Thread status:** Strong.

---

### Result 3: Route-table knowledge and composition dissociate

**Claim:** Local route-table accuracy is not sufficient for memory-like composed traversal.

**Evidence:** No-recurrence-at-eval retained route-table accuracy of 1.0000 while composition accuracy collapsed to near-chance for route lengths greater than 1.

**Caveat:** The manuscript must avoid equating route-table accuracy with memory success.

**Source artifact:**  
`experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`

**Thread status:** Strong.

---

### Result 4: Structural plasticity is required in this harness

**Claim:** Structural plasticity is necessary for the route-memory mechanism in this experiment.

**Evidence:** At route length 12, no-structural-plasticity had stored edge count 0, used edge fraction 0, composition accuracy approximately 0.0307, and route-table accuracy approximately 0.0308.

**Caveat:** This does not compare against external learned baselines. It supports necessity within the route-field implementation.

**Source artifact:**  
`experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`

**Thread status:** Strong internally; Needs baseline.

---

### Result 5: Context binding is important for correct route use

**Claim:** Context/mode binding is important for selecting and using the correct route memory.

**Evidence:** At route length 12, no-context-binding had composition accuracy approximately 0.0452 and route-table accuracy approximately 0.3648.

**Caveat:** The variant still stored many edges, so the failure should be interpreted as a selection/interference failure rather than simple absence of memory.

**Source artifact:**  
`experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`

**Thread status:** Strong internally.

---

### Result 6: Wrong-world context injection causes a sharp failure cliff

**Claim:** The model is sensitive to wrong-world context identity.

**Evidence:** Full-model wrong-world injection remained accurate at low corruption, dropped to approximately 0.5131 at 0.5 injection, and collapsed to approximately 0.0317 at 0.75–0.99 injection.

**Caveat:** Context dropout and context bleed did not reduce composition accuracy in this run. The result supports wrong-world identity corruption more than generic noisy-context degradation.

**Source artifact:**  
`experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_context_corruption.csv`

**Thread status:** Promising.

---

### Result 7: World-gated plasticity was not required in this harness

**Claim:** The current run does not show that world-gated plasticity is necessary.

**Evidence:** No-world-gated-plasticity retained composition accuracy 1.0000 and route-table accuracy 1.0000 across tested route lengths.

**Caveat:** World-gated plasticity may still matter under harder settings, more worlds, heavier interference, noisier contexts, or different schedules. This run does not support the necessity claim.

**Source artifact:**  
`experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`

**Thread status:** Do not use as positive evidence for world-gated necessity.

---

### Result 8: Targeted critical-edge lesion diagnostic failed expected pattern

**Claim:** The current targeted-lesion diagnostic does not support the claim that identified critical edges are more route-critical than matched random edges.

**Evidence:** Targeted critical-edge lesion left composition accuracy around 0.9192, while random count-matched lesion reduced composition accuracy to approximately 0.4915.

**Caveat:** This is directionally opposite to the expected diagnostic result. It may indicate a bug, mismatch in the critical-edge selector, or an invalid lesion-control design.

**Source artifact:**  
`experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_lesion_metrics.csv`

**Thread status:** Do not use; Needs rerun.

---

### Result 9: Local finite budget is more damaging than global finite budget

**Claim:** Local route-field budget pressure is much more damaging to composed traversal than global budget pressure.

**Evidence:** At route length 12, constrained global budget produced composition accuracy around 0.516, while constrained local budget produced composition accuracy around 0.0589. Route-table accuracy under constrained local budget remained around 0.5155.

**Caveat:** The precise budget settings and task configuration need to be documented before manuscript use.

**Source artifact:**  
`experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv`

**Thread status:** Promising.

---

### Result 10: Consolidation strength did not rescue accuracy under budget pressure

**Claim:** In this run, consolidation strength did not materially improve accuracy under budget constraints.

**Evidence:** Under constrained global budget, no, weak, default, and aggressive consolidation all produced composition accuracy around 0.516. Under constrained local budget, all produced composition accuracy around 0.0589.

**Caveat:** Consolidation may affect margins or robustness measures, but this specific result does not support an accuracy-rescue claim.

**Source artifact:**  
`experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv`

**Thread status:** Needs metric cleanup / revised interpretation.

---

### Result 11: Freezing plasticity preserves old worlds but blocks new acquisition

**Claim:** Freezing plasticity preserves already-learned worlds while preventing new-world acquisition.

**Evidence:** Old worlds after freeze retained composition accuracy 1.0000. A new world after freeze had composition accuracy approximately 0.0257 and route-table accuracy approximately 0.0313.

**Caveat:** This is an internal stability/plasticity diagnostic, not a full biological consolidation model.

**Source artifact:**  
`experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_freeze_plasticity.csv`

**Thread status:** Promising.

---

### Result 12: Artifact-level validation passed

**Claim:** The uploaded analysis artifacts passed the run’s validation checks.

**Evidence:** Validation reported PASS 27, WARN 0, FAIL 0. Expected phases and variants were present. Metrics had 3000 rows.

**Caveat:** SQLite was referenced but not included in the uploaded bundle. GPU/device metadata and source-code snapshot/commit SHA were not observed.

**Source artifact:**  
`experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/validation_report.md`  
`experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/validation_results.json`  
`experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/run_manifest.json`

**Thread status:** Strong artifact integrity; incomplete reproducibility package.

## 5. Key scientific conclusions supported by this thread

### Conclusion 1

**Claim:** The strongest supported mechanism result is the dissociation between local route-table knowledge and recurrent composed traversal.

**Evidence:** No-recurrence-at-eval preserved route-table accuracy at 1.0000 but collapsed composition accuracy to approximately 0.0413 at route length 12.

**Caveat:** This supports evaluation-time recurrence dependence, not necessarily formation-time recurrence dependence.

**Experiment:** Experiment 13.1

**Artifact(s):**  
`exp13_1_variant_metrics.csv`  
`exp13_1_recurrence_ablation.png`  
`exp13_1_route_table_accuracy.png`  
`exp13_1_composition_accuracy.png`

**Manuscript relevance:** Main-figure candidate; supports central mechanistic spine.

---

### Conclusion 2

**Claim:** Structural plasticity is necessary for this route-memory implementation.

**Evidence:** Removing structural plasticity produced zero stored edges and near-random composition/route-table performance.

**Caveat:** This does not establish superiority over standard neural baselines.

**Experiment:** Experiment 13.1

**Artifact(s):**  
`exp13_1_variant_metrics.csv`  
`exp13_1_composition_accuracy.png`

**Manuscript relevance:** Supporting claim; needs baseline framing.

---

### Conclusion 3

**Claim:** Context binding supports correct route/world selection.

**Evidence:** Removing context binding produced severe composition failure despite nonzero edge storage.

**Caveat:** Generic context dropout/bleed did not impair composition accuracy in the full model, so the result must be framed as wrong-world/selection sensitivity rather than generic noisy-context fragility.

**Experiment:** Experiment 13.1

**Artifact(s):**  
`exp13_1_variant_metrics.csv`  
`exp13_1_context_corruption.csv`  
`exp13_1_context_confusion.png`

**Manuscript relevance:** Supporting claim with refined interpretation.

---

### Conclusion 4

**Claim:** Local budget constraints are more harmful to composition than global budget constraints.

**Evidence:** Constrained local budget reduced composition accuracy to approximately 0.0589, while constrained global budget remained around 0.516.

**Caveat:** Requires clear budget-setting documentation and possibly harder follow-up.

**Experiment:** Experiment 13.1

**Artifact(s):**  
`exp13_1_budget_consolidation.csv`  
`exp13_1_budget_consolidation.png`

**Manuscript relevance:** Supporting/supplementary claim.

---

### Conclusion 5

**Claim:** The current targeted-lesion diagnostic failed and should not be used as positive mechanism evidence.

**Evidence:** Random count-matched lesions were more damaging than targeted critical-edge lesions.

**Caveat:** Requires implementation audit and rerun.

**Experiment:** Experiment 13.1

**Artifact(s):**  
`exp13_1_lesion_metrics.csv`  
`exp13_1_lesion_sensitivity.png`

**Manuscript relevance:** Limitation/internal audit; do not use as support.

## 6. Important flaws, mistakes, or implementation concerns identified

1. **Targeted lesion result contradicted expected mechanism**
   - Targeted critical-edge lesion was less damaging than random count-matched lesion.
   - This requires implementation audit or rerun.
   - Status: `Do not use`.

2. **No-recurrence-at-eval and no-recurrence-throughout appeared numerically identical**
   - This weakens any claim that training-time recurrence is necessary.
   - Current interpretation should be limited to evaluation-time recurrence.

3. **No-world-gated-plasticity did not fail**
   - It performed identically to the full model on clean route composition.
   - This does not support a world-gated-plasticity necessity claim.

4. **Full-model saturation**
   - Full model achieved 1.0000 accuracy across all tested route lengths.
   - This limits capacity/generalization conclusions.

5. **Context-corruption interpretation needed refinement**
   - Wrong-world injection caused failure.
   - Context dropout and context bleed did not reduce composition accuracy.
   - This weakens a general noisy-context degradation story.

6. **Consolidation strength did not improve accuracy under budget pressure**
   - Consolidation variants did not materially rescue constrained-budget accuracy.
   - The consolidation interpretation should focus on freeze/stability-plasticity or margins, not accuracy rescue.

7. **SQLite database not uploaded**
   - Validation referenced a per-run SQLite database.
   - The database itself was not included in the uploaded zip.
   - Status: `local verification pending`.

8. **GPU/device info missing**
   - No GPU/device information was observed.
   - Reproducibility metadata should be expanded.

9. **External baselines missing**
   - No MLP/RNN/Transformer/symbolic baselines were analyzed.
   - Manuscript claims must remain internal unless baselines are added.

10. **README completed-runs/results section not available in upload**
   - Owning experiment README was not inspected in this thread.
   - Repository update required.

## 7. Figures or artifacts referenced

### CSVs

```text
metrics.csv
exp13_1_metrics.csv
exp13_1_summary.csv
exp13_1_variant_metrics.csv
exp13_1_ablation_metrics.csv
exp13_1_context_corruption.csv
exp13_1_lesion_metrics.csv
exp13_1_budget_consolidation.csv
exp13_1_freeze_plasticity.csv
```

### Reports and manifests

```text
run_manifest.json
validation_report.md
validation_results.json
progress.jsonl
```

### Plots

```text
exp13_1_budget_consolidation.png
exp13_1_composition_accuracy.png
exp13_1_context_confusion.png
exp13_1_lesion_sensitivity.png
exp13_1_recurrence_ablation.png
exp13_1_route_table_accuracy.png
```

### Referenced but not uploaded / not independently inspected

```text
experiments/experiment13_1_publication_hardening/runs/exp13_1_full_20260506_214756.sqlite3
experiments/experiment13_1_publication_hardening/README.md
```

## 8. Decisions made

1. Treat Experiment 13.1 as a **promising internal mechanism audit**, not a complete manuscript proof package.
2. Treat the recurrence/composition dissociation as the strongest manuscript-facing result.
3. Frame recurrence evidence as **evaluation-time recurrence dependence**, not training-time recurrence dependence.
4. Treat structural-plasticity ablation as strong internal evidence, but still requiring baselines for broader claims.
5. Treat context-binding evidence as supportive, but refine context-corruption claims toward wrong-world selection sensitivity.
6. Do **not** use the targeted-lesion result as positive evidence.
7. Do **not** claim world-gated plasticity is necessary based on this run.
8. Treat local-vs-global budget results as promising, likely supplementary unless the manuscript foregrounds finite capacity.
9. Treat freeze-plasticity results as promising stability/plasticity evidence.
10. Recommend metric cleanup, implementation audit, and focused rerun before using Exp 13.1 as a manuscript pillar.

## 9. Open questions

1. Why are targeted critical-edge lesions less damaging than random count-matched lesions?
2. Is the critical-edge selector identifying the wrong edge set?
3. Are random count-matched lesions truly matched to targeted lesions?
4. Are no-recurrence-at-eval and no-recurrence-throughout actually implemented differently?
5. Does recurrence affect route formation/training, or only evaluation-time traversal?
6. Under what harder task settings does world-gated plasticity matter?
7. Would longer routes, more worlds, more modes, or stronger interference break the full model?
8. Do external baselines fail in the same way, or can they solve this synthetic task?
9. Does consolidation affect robustness margins even if it does not affect accuracy?
10. Should the per-run SQLite database be committed, archived, or summarized as source data?

## 10. Relationship to first manuscript

Experiment 13.1 contributes mainly as a **mechanism-hardening experiment**.

### Central claim contribution

It strengthens the claim that route-memory behavior depends on recurrent composed traversal rather than merely storing local next-step transitions.

### Supporting claim contribution

It supports internal claims about:

- structural plasticity;
- context/world selection;
- route-table/composition dissociation;
- finite-budget degradation;
- local-vs-global budget asymmetry;
- freeze/plasticity stability tradeoff.

### Limitation contribution

It exposes important limitations:

- lesion diagnostic failure;
- missing external baselines;
- saturated clean task;
- unclear training-recurrence ablation;
- no support for world-gated plasticity necessity in this harness;
- incomplete reproducibility package.

### Future-work contribution

It motivates a successor experiment focused on:

- audited route-critical lesion selection;
- true recurrence-training ablation;
- harder interference/capacity settings;
- external baseline suite;
- improved source-data packaging.

### Supplementary material contribution

Likely supplementary candidates:

- budget/consolidation figure;
- context-corruption figure;
- freeze/plasticity table or plot;
- full ablation table;
- validation/run-integrity table.

Main-figure candidate:

- composition accuracy versus route-table accuracy under recurrence ablation.

## 11. Claims-and-evidence rows contributed by this thread

| Claim | Evidence | Caveat | Experiment(s) | Artifact(s) | Manuscript status |
|---|---|---|---|---|---|
| Full model solves clean route composition across tested route lengths. | Composition accuracy 1.0000 for route lengths 1–16. | Saturated task; does not prove broad generalization. | Experiment 13.1 | `exp13_1_variant_metrics.csv`, `exp13_1_composition_accuracy.png` | Promising |
| Recurrent evaluation is required for composed traversal. | No-recurrence-at-eval preserved route-table accuracy 1.0000 but composition fell to ~0.0413 at route length 12. | Supports evaluation recurrence, not necessarily training recurrence. | Experiment 13.1 | `exp13_1_variant_metrics.csv`, `exp13_1_recurrence_ablation.png` | Strong |
| Local route-table accuracy is not sufficient for memory-like composition. | Route-table accuracy stayed 1.0000 while composition collapsed under no recurrence. | Must not use route-table accuracy alone as success metric. | Experiment 13.1 | `exp13_1_variant_metrics.csv`, `exp13_1_route_table_accuracy.png` | Strong |
| Structural plasticity is required in this implementation. | No-structural-plasticity had zero stored edges and near-random performance. | Internal evidence only; baselines still required. | Experiment 13.1 | `exp13_1_variant_metrics.csv` | Strong internally; Needs baseline |
| Context binding supports correct route/world selection. | No-context-binding composition accuracy ~0.0452 at route length 12. | Failure likely selection/interference, not no-storage. | Experiment 13.1 | `exp13_1_variant_metrics.csv` | Strong internally |
| Wrong-world context corruption causes failure. | Wrong-world injection caused collapse at high corruption. | Dropout/bleed did not impair accuracy; not generic noisy-context degradation. | Experiment 13.1 | `exp13_1_context_corruption.csv`, `exp13_1_context_confusion.png` | Promising |
| World-gated plasticity is necessary. | No-world-gated-plasticity performed at 1.0000. | Current run does not support this claim. | Experiment 13.1 | `exp13_1_variant_metrics.csv` | Do not use as support |
| Targeted critical-edge lesions identify route-critical structure. | Targeted lesion less damaging than random count-matched lesion. | Expected pattern reversed; audit/rerun required. | Experiment 13.1 | `exp13_1_lesion_metrics.csv`, `exp13_1_lesion_sensitivity.png` | Do not use |
| Local budget is more damaging than global budget. | Constrained local budget composition ~0.0589 versus constrained global ~0.516. | Budget settings need explicit documentation. | Experiment 13.1 | `exp13_1_budget_consolidation.csv`, `exp13_1_budget_consolidation.png` | Promising |
| Consolidation strength improves constrained-budget accuracy. | Accuracy did not materially change across consolidation strengths. | May affect margins, but not accuracy here. | Experiment 13.1 | `exp13_1_budget_consolidation.csv` | Not supported as accuracy claim |
| Freeze preserves old worlds and blocks new acquisition. | Old worlds after freeze retained 1.0000; new world after freeze ~0.0257. | Internal stability/plasticity diagnostic only. | Experiment 13.1 | `exp13_1_freeze_plasticity.csv` | Promising |
| Run artifacts passed validation. | PASS 27, WARN 0, FAIL 0; 3000 rows; expected phases/variants present. | SQLite DB not uploaded; device info missing. | Experiment 13.1 | `validation_report.md`, `validation_results.json`, `run_manifest.json` | Strong artifact integrity; incomplete reproducibility package |

## 12. Required repository updates

Update or create:

```text
experiments/experiment13_1_publication_hardening/README.md
docs/threads/experiment13_1_analysis_digest.md
docs/experiments/experiment13_1_summary.md
docs/experiments/EXPERIMENT_REGISTRY.md
docs/manuscript/CLAIMS_AND_EVIDENCE.md
docs/manuscript/FIGURE_PLAN.md
docs/manuscript/LIMITATIONS_AND_THREATS.md
docs/manuscript/MANUSCRIPT_TODO.md
docs/synthesis/PROJECT_STATUS.md
docs/synthesis/PUBLICATION_READINESS.md
docs/synthesis/NEXT_EXPERIMENTS.md
docs/repo_audit/REPRODUCIBILITY_AUDIT.md
docs/source_data/exp13_1_full_20260506_214756.md
```

Recommended updates by file:

### `experiments/experiment13_1_publication_hardening/README.md`

Add completed-run section:

```text
Run ID: exp13_1_full_20260506_214756
Profile: full
Seeds: 20
Rows: 3000
Validation: PASS 27 / WARN 0 / FAIL 0
Elapsed: approximately 8.2 hours
Primary status: promising internal mechanism audit
Major caveat: targeted lesion diagnostic failed expected pattern
```

### `docs/manuscript/CLAIMS_AND_EVIDENCE.md`

Add conservative rows for:

- recurrence/composition dissociation;
- structural plasticity internal support;
- context binding support;
- local-vs-global budget result;
- freeze/plasticity result;
- lesion diagnostic failure as limitation.

### `docs/manuscript/FIGURE_PLAN.md`

Add:

```text
Main figure candidate:
- recurrence ablation showing composition collapse with preserved route-table accuracy

Supplement candidates:
- composition ablation summary
- route-table accuracy summary
- context corruption/wrong-world injection
- budget consolidation/local-vs-global budget
- freeze/plasticity result

Do not use as positive evidence:
- lesion sensitivity plot until rerun/audit
```

### `docs/manuscript/LIMITATIONS_AND_THREATS.md`

Add limitations:

- targeted lesion diagnostic failure;
- missing external baselines;
- saturated clean task;
- unclear training-recurrence interpretation;
- no support for world-gated-plasticity necessity;
- missing uploaded SQLite/source-data file;
- missing GPU/device metadata.

### `docs/synthesis/NEXT_EXPERIMENTS.md`

Add proposed follow-up:

```text
experiment13_2_route_critical_lesion_and_recurrence_audit
```

Focus:

- audited critical-edge lesion selection;
- matched lesion controls;
- explicit training-time versus evaluation-time recurrence ablations;
- harder route lengths/world counts/interference;
- baseline comparison.

## 13. Recommended next action

The next action should be **implementation audit and focused rerun**, not immediate manuscript drafting.

Recommended sequence:

1. Audit targeted-lesion implementation and random-control matching.
2. Audit the difference between `no_recurrence_at_eval` and `no_recurrence_throughout`.
3. Regenerate figures with confidence intervals/error bars.
4. Add or archive the per-run SQLite database, or explicitly document it as local-only.
5. Add GPU/device/runtime metadata to the run manifest.
6. Run a successor experiment with harder task settings and external baselines.
7. Only after the audit/rerun, promote the strongest results into manuscript main figures.

## 14. Import package checklist

- **Zip filename:** `experiment13_1_analysis_digest.zip`
- **Digest filename inside zip:** `experiment13_1_analysis_digest.md`
- **Digest is at zip root, not nested:** yes
- **Digest final path after repo import:** `docs/threads/experiment13_1_analysis_digest.md`
- **Digest contains only thread-derived analysis, not direct repo edits:** yes
- **Any local artifact paths needing verification:**
  - `experiments/experiment13_1_publication_hardening/runs/exp13_1_full_20260506_214756.sqlite3` — referenced by validation but not included in uploaded bundle; `local verification pending`.
  - `experiments/experiment13_1_publication_hardening/README.md` — not inspected in this thread; `local verification pending`.
