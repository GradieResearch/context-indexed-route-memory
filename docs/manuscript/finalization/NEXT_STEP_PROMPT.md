# Next Step Prompt: Apply Manuscript Prose Patch And Begin Table 3 Review

Use this prompt after the human-decision integration status has merged.

```text
You are working in the repository:

GradieResearch/context-indexed-route-memory

Task: Complete the remaining guarded manuscript integration work after the human decisions captured in `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md`, then begin the next manuscript-finalization blocker: Table 3 grouping/effect-size review.

Starting context:

The repository is post-Exp15, post-Manuscript-V2-capture, post-Analysis-Pass-15A, post-citation/prior-art audit, post-citation-ledger pass, post-citation-ledger integration-status pass, and post-human-decision capture.

Human decisions now made:

1. Citation/export convention:
   - Keep `docs/manuscript/REFERENCES.md` as the venue-neutral ledger for now.
   - Do not create BibTeX, CSL JSON, numbered references, or target-journal formatting until a target venue/convention is selected.

2. Closest-prior-art placement:
   - Convert `docs/manuscript/closest_prior_art_table.md` into prose in Section 2.7.
   - Retain `docs/manuscript/closest_prior_art_table.md` as the companion source artifact.

3. Figure/table placement:
   - Figures 1-3: main.
   - Figure 4: supplement by default unless the finite-budget story is intentionally emphasized.
   - Figure 5: main-narrow, because Exp14 helps reduce the oracle-context criticism.
   - Table 3: candidate until grouping/effect-size review is complete.
   - Table 4: compact main-text table, because Exp15 materially shapes the paper's claims.

Inputs to inspect first:

- `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md`
- `docs/manuscript/closest_prior_art_table.md`
- `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`
- `docs/manuscript/draft/MANUSCRIPT_V2.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`
- `docs/manuscript/tables/table_03_statistical_summary.md`

Immediate work:

1. Apply the Section 2.7 prose replacement directly to `docs/manuscript/draft/MANUSCRIPT_V2.md`.
   - Replace the old Section 2.7 closest-prior-art TODO with prose derived from `docs/manuscript/closest_prior_art_table.md`.
   - Preserve the narrow novelty posture: controlled route-memory decomposition and evidence map, not novelty of context gating, recurrence, memory, modular routing, graph reasoning, or biological indexing in isolation.
   - Preserve Exp13.2 and Exp15 caveats: oracle context-gated lookup and context-conditioned neural transition learning solve the clean supplied-context slice.

2. Sync operational docs after the manuscript patch.
   - Update `docs/manuscript/FIGURE_PLAN.md` if it still describes Figure 4/Figure 5/Table 4 as unresolved.
   - Update `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md` so the human decision checkpoint is marked complete and the next active blocker is Table 3 grouping/effect-size review plus direct manuscript polish.
   - Update `docs/manuscript/MANUSCRIPT_TODO.md` and `docs/synthesis/PUBLICATION_READINESS.md` if they still describe citation convention / closest-prior-art placement / figure placement as unresolved.

3. Begin Table 3 review only after the above docs are synchronized.
   - Inspect `docs/manuscript/tables/table_03_statistical_summary.md`.
   - Inspect `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`.
   - Identify which rows are safe final manuscript statistics and which require regrouping or caveats.
   - Do not invent effect sizes or confidence intervals.

Do not do these unless explicitly requested:

- Do not rerun experiments.
- Do not modify experiment code.
- Do not start Exp16 or optional successor experiments.
- Do not add memory-augmented/key-value neural baselines unless a venue/reviewer strategy requires them.
- Do not audit Exp15 replay unless specifically requested.
- Do not broaden claims beyond the retained post-15A posture.
- Do not create final bibliography files until a venue/citation convention is chosen.

Definition of done:

- `MANUSCRIPT_V2.md` Section 2.7 contains prose derived from `docs/manuscript/closest_prior_art_table.md`.
- `FIGURE_PLAN.md`, `FINALIZATION_CHECKLIST.md`, `MANUSCRIPT_TODO.md`, and `PUBLICATION_READINESS.md` no longer describe the now-made human decisions as unresolved.
- Table 3 grouping/effect-size review is either started with explicit findings or deferred with a clear reason.
- `python scripts/verify_doc_source_paths.py` passes, or inability to run is documented with exact reason.
- Final response summarizes changed files, verification status, and remaining blockers.
```
