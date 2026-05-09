# Next Step Prompt: Analysis Pass 15A - Retained Claims And Statistical Hardening

Use this prompt in a new session after Experiment 15 has been imported and `docs/manuscript/draft/MANUSCRIPT_V2.md` has been captured.

```text
You are working in the repository:

GradieResearch/context-indexed-route-memory

Task: Advance the manuscript from captured V2 into retained-claim statistical hardening and final source-data-backed figure/table planning. Do not change the experimental record.

Starting context:

The repository is now post-Exp15 and post-Manuscript-V2-capture.

- Experiment 15 is complete and imported as minimal fixed-profile neural comparator evidence.
- The imported Exp15 run is `exp15_full_20260508_092811`.
- `docs/manuscript/draft/MANUSCRIPT_V2.md` exists.
- `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md` exists.
- `docs/manuscript/tables/table_04_exp15_neural_comparator.md` exists.
- `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv` exists.
- The next checklist item is no longer V2 capture. The next checklist item is to decide retained main claims and begin manuscript-grade statistical/source-data hardening.

Current scientific posture to preserve:

- The paper is a controlled symbolic/mechanistic benchmark and evidence-map manuscript.
- Exp15 is minimal neural comparator evidence, not exhaustive neural benchmarking.
- Broad CIRM-over-neural-model claims are not supported.
- Context-conditioned neural transition MLP and world-head transition MLP solve the clean hard slice at ceiling.
- Endpoint neural baselines help separate endpoint memorization from reusable transition composition.
- No-context neural results support conflict-specific context-indexing claims, not a blanket context-is-required-for-every-suffix claim.
- Exp14 supports symbolic transition-cue context selection, not raw sensory latent-world discovery.
- Exp15 replay collapse is a non-claim pending audit.
- The Exp15 manifest/SQLite caveat remains: `run_manifest.json` was reconstructed after a final SQLite manifest-write failure, and the SQLite `run_manifest` table may be empty. Treat CSV artifacts as authoritative unless a later audit says otherwise.

Inputs to inspect first:

- `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`
- `docs/manuscript/finalization/MANUSCRIPT_FINALIZATION_PLAN.md`
- `docs/manuscript/draft/MANUSCRIPT_V2.md`
- `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`
- `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/manuscript/BASELINE_REQUIREMENTS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/source_data/SOURCE_DATA_MANIFEST.csv`
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`
- `docs/manuscript/tables/table_03_statistical_summary.md`
- `docs/manuscript/tables/table_04_exp15_neural_comparator.md`
- `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`
- `docs/threads/experiment15_analysis_digest.md`
- `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`

Primary objective:

Create a retained-claims statistical-hardening pass for the V2 manuscript. This should identify the exact retained main claims, map each claim to source CSVs, determine which statistics are already present, and generate or update manuscript-grade summary tables where possible.

Concrete work:

1. Determine retained V2 main claims.
   - Use `FIRST_MANUSCRIPT_CLAIM_FREEZE.md`, `POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`, `CLAIMS_AND_EVIDENCE.md`, `FIGURE_PLAN.md`, and `MANUSCRIPT_V2.md` together.
   - Produce a clear retained-claim list with claim ID, manuscript role, source artifact paths, and remaining caveats.
   - Keep C9 out of the main claim set unless seen/unseen metrics are cleaned.
   - Keep Exp15 replay collapse out of the retained scientific claim set unless audited.
   - Keep broad neural-superiority, solved continual-learning, raw perceptual latent-world discovery, and biological-validation claims out.

2. Identify source CSVs for every retained main claim.
   - Use generated source-data mirrors where present.
   - Use authoritative experiment analysis CSVs where source-data mirrors are missing.
   - Record missing or incomplete source-data mirrors explicitly.
   - Update `docs/source_data/SOURCE_DATA_MANIFEST.csv` only if new source-data-backed outputs are created or existing rows are corrected.

3. Generate or update manuscript-grade statistical summaries.
   - For each retained main claim, prefer seed-level summaries over aggregate-only rows.
   - Include, where available: mean, standard deviation or standard error, 95% confidence interval, seed count, direct comparison, effect size, source artifact path, and manuscript figure/table reference.
   - Update `docs/manuscript/tables/table_03_statistical_summary.md` if the source evidence is sufficient.
   - Update `docs/source_data/STATISTICAL_REPORTING_READINESS.csv` to distinguish complete, partial, missing, aggregate-only, and needs-human-review items.
   - Do not invent statistics. If a statistic cannot be computed from local artifacts, mark it as missing and explain exactly what source path or grouping is needed.

4. Review figure/table readiness.
   - Decide which candidate figures/tables are retained for V2 hardening.
   - Keep generated candidate analysis plots distinct from final manuscript figures unless they are source-data-backed and reproducibly generated.
   - Record whether Exp14 remains main-narrow Figure 5 or should move to supplement.
   - Keep Exp15 as compact Table 4 unless a human/venue decision moves it to supplement.
   - Do not convert Exp15 plots into final figures unless explicitly requested.

5. Update finalization docs after concrete changes.
   - Update `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md` to reflect completed and remaining Phase 4/5 items.
   - Update `docs/manuscript/MANUSCRIPT_TODO.md` if the active operational priority changes.
   - Update `docs/synthesis/PUBLICATION_READINESS.md` if readiness status changes.

Do not do these unless explicitly requested:

- Do not rerun experiments.
- Do not modify experiment code.
- Do not start Exp16 or any optional successor experiment.
- Do not add a memory-augmented/key-value neural baseline unless the user chooses a venue/reviewer strategy requiring it.
- Do not audit the Exp15 replay implementation unless specifically requested.
- Do not rewrite the manuscript wholesale.
- Do not add fake citations, fake BibTeX, or unsupported related-work claims.

Useful Exp15 hard-slice facts available for conservative citation:

- `neural_transition_mlp_context`: 1.0000 on all hard-slice metrics.
- `neural_transition_mlp_world_heads_context`: 1.0000 on all hard-slice metrics.
- `neural_gru_endpoint_context`: seen-route composition about 0.9990, suffix-route composition about 0.4040, transition accuracy about 0.0232, retention about 0.7015.
- `neural_gru_rollout_context`: first-step context conflict about 0.8794, transition accuracy about 0.5122, suffix-route composition about 0.0777, retention about 0.0612.
- `neural_transformer_sequence_context`: seen-route composition about 0.5435, suffix-route composition about 0.1184, retention about 0.3309.
- `neural_transition_mlp_no_context`: first-step context conflict about 0.0312, seen-route composition about 0.0312, suffix-route composition 1.0000, transition accuracy about 0.9193, retention about 0.5156.
- `neural_transition_mlp_replay_context`: near-zero hard-slice performance; audit before interpretation.

Definition of done:

- Retained main claims are listed explicitly.
- Each retained main claim has source CSVs identified, or the missing source-data gap is documented.
- `docs/manuscript/tables/table_03_statistical_summary.md` is updated if sufficient seed-level evidence exists.
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv` reflects the current state.
- Figure/table readiness is updated without overclaiming candidate plots as final figures.
- `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md` reflects actual progress.
- `python scripts/verify_doc_source_paths.py` passes, or failures are listed with exact paths and fixes.
- Final response summarizes changed files, retained claims, unresolved decisions, and verification result.
```
