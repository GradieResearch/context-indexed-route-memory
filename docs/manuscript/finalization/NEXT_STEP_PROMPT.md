# Next Step Prompt: Manuscript V2 Integration And Finalization Hardening

Use this prompt in a new session after drafting `MANUSCRIPT_V2.md` from the completed Experiment 15 results.

```text
You are working in the repository:

GradieResearch/context-indexed-route-memory

Task: Capture the manuscript V2 draft and advance the manuscript-finalization checklist without changing the experimental record.

Starting context:

Experiment 15 is complete and imported. The current scientific posture is post-Exp15:

- Exp15 is no longer a planned neural comparator. It has completed full-run artifacts.
- The imported run is `exp15_full_20260508_092811`.
- Exp15 closes the "neural baselines are absent" limitation only in a minimal fixed-profile sense.
- Exp15 does not support broad CIRM-over-neural-model claims.
- The context-conditioned transition MLP and world-head transition MLP solve the clean hard slice at ceiling.
- Endpoint neural models help demonstrate endpoint memorization versus reusable transition composition.
- No-context neural models support a conflict-specific context-indexing claim, not a blanket context-is-required-for-every-suffix claim.
- The replay variant must not be interpreted scientifically unless audited.
- The Exp15 manifest/SQLite caveat remains: `run_manifest.json` was reconstructed after a final SQLite manifest-write failure, and the SQLite `run_manifest` table may be empty. Treat CSV artifacts as authoritative unless a later audit says otherwise.

Primary objective:

Move from "V2 drafted in discussion" to "V2 captured and ready for statistical/source-data hardening".

Inputs to inspect first:

- `docs/manuscript/finalization/MANUSCRIPT_FINALIZATION_PLAN.md`
- `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`
- `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/manuscript/BASELINE_REQUIREMENTS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/source_data/SOURCE_DATA_MANIFEST.csv`
- `docs/threads/experiment15_analysis_digest.md`
- `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`
- `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`

If the user provides the V2 draft in the session:

1. Create or update `docs/manuscript/draft/MANUSCRIPT_V2.md` with the supplied draft.
2. Preserve the draft's cautious claim posture.
3. Make only light formatting/path corrections unless the user explicitly asks for substantive rewriting.
4. Do not invent citations, statistics, or new experimental conclusions.

If `docs/manuscript/draft/MANUSCRIPT_V2.md` already exists:

1. Inspect it before editing.
2. Prefer targeted edits over rewriting.
3. Preserve any user-authored text unless it conflicts with repository evidence or finalization constraints.

Recommended V2 manuscript posture to preserve:

- The paper is a controlled symbolic/mechanistic benchmark and evidence map.
- The contribution is the decomposition of route storage, context indexing, recurrent execution, endpoint memorization, finite capacity, symbolic context selection, and neural baseline contracts.
- Exp14 should be treated as symbolic transition-cue context selection, not raw latent-world discovery.
- Exp15 should be treated as a minimal neural comparator, not exhaustive neural benchmarking.
- Exp15 is best represented as a compact main-text neural comparator table unless a human decides to move it to supplement.
- Broad claims that ordinary neural models cannot solve the benchmark must be removed.
- Broad claims that CIRM is superior to neural models must be removed.
- Context necessity must be framed around incompatible local transitions and first-step/full-route disambiguation.
- Suffix-route results must be interpreted carefully because some suffix probes bypass the deliberately conflicting first transition.

Concrete follow-up edits:

1. Create `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md` if no equivalent post-Exp15 claim-freeze artifact exists.
   - Use Claim -> Evidence -> Caveat -> Source path format.
   - Record that Exp15 narrows C1, C2, C4, and C12.
   - Record that Exp14 supports only symbolic transition-cue context selection.
   - Record that Exp15 replay collapse is not a retained scientific claim unless audited.

2. Generate a source-data-backed Exp15 table if Exp15 is retained in the manuscript.
   Suggested outputs:
   - `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`
   - `docs/manuscript/tables/table_04_exp15_neural_comparator.md`

   Source artifact:
   - `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`

   Hard-slice filter:
   - `world_count = 32`
   - `route_length = 12`
   - `n_seeds = 10`, if the summary source exposes seed count directly or indirectly

   Include at minimum:
   - variant
   - first-step context conflict accuracy
   - retention after sequential worlds
   - seen-route composition accuracy
   - suffix-route composition accuracy
   - transition accuracy
   - interpretation/caveat column

3. Update source-data and figure/table tracking:
   - `docs/source_data/SOURCE_DATA_MANIFEST.csv`
   - `docs/manuscript/FIGURE_PLAN.md`
   - `docs/manuscript/MANUSCRIPT_TODO.md`
   - `docs/manuscript/BASELINE_REQUIREMENTS.md`
   - `docs/synthesis/PUBLICATION_READINESS.md`

4. Update `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md` after making concrete changes.
   - Mark `MANUSCRIPT_V2.md` captured only if the file exists.
   - Mark post-Exp15 claim freeze/addendum complete only if the artifact exists.
   - Mark Exp15 source-data-backed table complete only if the source-data CSV and markdown table exist.

Do not do these unless explicitly requested:

- Do not rerun experiments.
- Do not modify experiment code.
- Do not start Exp16 or any optional successor experiment.
- Do not add a memory-augmented/key-value neural baseline unless the user chooses a venue/reviewer strategy requiring it.
- Do not audit the replay implementation unless specifically requested.
- Do not convert analysis plots into final manuscript figures without source-data-backed generation.
- Do not claim solved continual learning, raw perceptual latent-world discovery, biological validation, broad neural superiority, or unseen primitive transition inference.

Useful Exp15 hard-slice facts available for conservative citation:

- `neural_transition_mlp_context`: 1.0000 on all hard-slice metrics.
- `neural_transition_mlp_world_heads_context`: 1.0000 on all hard-slice metrics.
- `neural_gru_endpoint_context`: seen-route composition about 0.9990, suffix-route composition about 0.4040, transition accuracy about 0.0232, retention about 0.7015.
- `neural_gru_rollout_context`: first-step context conflict about 0.8794, transition accuracy about 0.5122, suffix-route composition about 0.0777, retention about 0.0612.
- `neural_transformer_sequence_context`: seen-route composition about 0.5435, suffix-route composition about 0.1184, retention about 0.3309.
- `neural_transition_mlp_no_context`: first-step context conflict about 0.0312, seen-route composition about 0.0312, suffix-route composition 1.0000, transition accuracy about 0.9193, retention about 0.5156.
- `neural_transition_mlp_replay_context`: near-zero hard-slice performance; audit before interpretation.

Definition of done:

- `docs/manuscript/draft/MANUSCRIPT_V2.md` exists or the user has been told exactly what is still needed to create it.
- The post-Exp15 claim posture is captured in a claim-freeze addendum or equivalent artifact.
- Exp15 placement is either decided or explicitly recorded as a remaining human decision.
- If Exp15 is retained, a source-data-backed Table 4 artifact exists or is listed as the immediate next checklist item.
- Finalization checklist reflects the actual repository state.
- `python scripts/verify_doc_source_paths.py` passes, or any failures are listed with exact paths and fixes.
- Final response summarizes changed files, claim posture, unresolved decisions, and verification result.
```
