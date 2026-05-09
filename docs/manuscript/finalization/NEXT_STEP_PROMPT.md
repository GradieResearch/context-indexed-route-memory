# Next Step Prompt: Post-15A Citation, Prior-Art, And Figure/Table Review

Use this prompt in a new session after Analysis Pass 15A has been completed.

```text
You are working in the repository:

GradieResearch/context-indexed-route-memory

Task: Advance the manuscript from retained-claim/statistical hardening into citation/prior-art hardening and human-review preparation for the generated candidate figure/table package. Do not change the experimental record.

Starting context:

The repository is now post-Exp15, post-Manuscript-V2-capture, and post-Analysis-Pass-15A.

- Experiment 15 is complete and imported as minimal fixed-profile neural comparator evidence.
- The imported Exp15 run is `exp15_full_20260508_092811`.
- `docs/manuscript/draft/MANUSCRIPT_V2.md` exists.
- `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md` exists.
- `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md` exists.
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv` has been updated for retained, boundary, supplement, blocked, and non-claim evidence.
- `docs/manuscript/tables/table_04_exp15_neural_comparator.md` exists.
- `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv` exists.
- The next checklist item is no longer retained-claim selection. The next checklist item is citation/prior-art hardening plus human review of generated Figures 1-5 and Tables 1-4.

Current scientific posture to preserve:

- The paper is a controlled symbolic/mechanistic benchmark and evidence-map manuscript.
- Retained main scientific spine: C1, C2, C3, C4, C5, C6, and C13.
- Retained discussion/table baseline claim: C12.
- Boundary or supplement only: C7, C8, C10, and C11.
- Out of main claim set: C9 unless seen/unseen/all metric cleanup is completed.
- Exp15 is minimal neural comparator evidence, not exhaustive neural benchmarking.
- Broad CIRM-over-neural-model claims are not supported.
- Context-conditioned neural transition MLP and world-head transition MLP solve the clean hard slice at ceiling.
- No-context neural results support conflict-specific context-indexing claims, not a blanket context-is-required-for-every-suffix claim.
- Exp14 supports symbolic transition-cue context selection, not raw sensory latent-world discovery.
- Exp15 replay collapse is a non-claim pending audit.
- Do not cite Exp13.1 lesion evidence as positive mechanism evidence unless audited/rerun.

Inputs to inspect first:

- `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`
- `docs/manuscript/finalization/MANUSCRIPT_FINALIZATION_PLAN.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`
- `docs/manuscript/draft/MANUSCRIPT_V2.md`
- `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`
- `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/BASELINE_REQUIREMENTS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/source_data/SOURCE_DATA_MANIFEST.csv`
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`
- `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`
- `docs/manuscript/tables/table_01_claim_evidence.md`
- `docs/manuscript/tables/table_02_run_integrity.md`
- `docs/manuscript/tables/table_03_statistical_summary.md`
- `docs/manuscript/tables/table_04_exp15_neural_comparator.md`

Primary objective:

Prepare the manuscript package for citation/prior-art hardening and human figure/table review. This should identify all citation placeholders and related-work claims that need real metadata, document the disposition of the missing novelty/prior-art source artifact, and produce a clear human-review checklist for Figures 1-5 and Tables 1-4.

Concrete work:

1. Citation and related-work audit.
   - Scan `MANUSCRIPT_V2.md` and manuscript-support docs for citation placeholders, TODO citation markers, unsupported related-work claims, or fake-looking references.
   - Produce a clear list of citation placeholders with exact surrounding context and the metadata/source needed.
   - Do not add fake citations, fake BibTeX, or unsupported prior-art claims.
   - If browsing/literature search is available in the environment, use current source metadata and prefer primary sources for technical claims.

2. Missing novelty/prior-art artifact disposition.
   - Locate/import or recreate the missing novelty/prior-art source artifact, if it is still relevant and available.
   - If it cannot be found, document that explicitly and remove dependency on it as a blocker where appropriate.
   - Do not invent its contents.

3. Human-review figure/table package.
   - Review generated Figures 1-5 and Tables 1-4 against `RETAINED_CLAIMS_STATISTICAL_HARDENING.md`.
   - For each figure/table, record: retained placement, claim role, caption caveat, source-data status, and unresolved human decision.
   - Keep Exp14 as main-narrow Figure 5 for V2 hardening unless a human/venue decision moves it to supplement.
   - Keep Exp15 as compact Table 4 unless a human/venue decision moves it to supplement.
   - Do not promote Exp15 analysis plots into final figures unless explicitly requested.

4. Update operational docs after concrete changes.
   - Update `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`.
   - Update `docs/manuscript/MANUSCRIPT_TODO.md`.
   - Update `docs/synthesis/PUBLICATION_READINESS.md` if readiness status changes.
   - Update `docs/manuscript/FIGURE_PLAN.md` only if figure/table placement or caption-readiness decisions change.

Do not do these unless explicitly requested:

- Do not rerun experiments.
- Do not modify experiment code.
- Do not start Exp16 or any optional successor experiment.
- Do not add a memory-augmented/key-value neural baseline unless the user chooses a venue/reviewer strategy requiring it.
- Do not audit the Exp15 replay implementation unless specifically requested.
- Do not rewrite the manuscript wholesale.
- Do not add fake citations, fake BibTeX, or unsupported related-work claims.
- Do not broaden claims beyond the retained post-15A posture.

Definition of done:

- Citation placeholders and unsupported related-work risks are listed with exact locations/context.
- The missing novelty/prior-art source artifact is imported/recreated, or its absence is explicitly documented.
- Figures 1-5 and Tables 1-4 have a human-review checklist with placement, caveats, source-data status, and unresolved decisions.
- Finalization checklist and manuscript TODO reflect actual progress.
- `docs/synthesis/PUBLICATION_READINESS.md` reflects the post-15A readiness posture.
- `python scripts/verify_doc_source_paths.py` passes, or failures/inability to run are listed with exact paths and fixes.
- Final response summarizes changed files, remaining blockers, unresolved human decisions, and verification result.
```
