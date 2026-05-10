# Next Step Prompt: Finalize Table 3 Grouping And Statistical Reporting

Use this prompt after the Section 2.7 closest-prior-art prose patch has been applied to `docs/manuscript/draft/MANUSCRIPT_V2.md` and the initial Table 3 grouping review has been started.

```text
You are working in the repository:

GradieResearch/context-indexed-route-memory

Task: Complete the next manuscript-finalization blocker: Table 3 grouping/effect-size cleanup and statistical-reporting readiness. Do not start new experiments.

Starting context:

The repository is post-Exp15, post-Manuscript-V2-capture, post-Analysis-Pass-15A, post-citation/prior-art audit, post-citation-ledger pass, post-human-decision capture, and post-Section-2.7 closest-prior-art prose integration.

Already completed:

- `docs/manuscript/draft/MANUSCRIPT_V2.md` Section 2.7 now contains closest-prior-art prose derived from `docs/manuscript/closest_prior_art_table.md`.
- `docs/manuscript/closest_prior_art_table.md` remains the companion source artifact.
- `docs/manuscript/REFERENCES.md` remains the venue-neutral citation ledger until target venue/convention selection.
- Figure/table placement decisions are recorded:
  - Figures 1-3: main.
  - Figure 4: supplement by default unless the finite-budget story is emphasized.
  - Figure 5: main-narrow.
  - Table 3: candidate until grouping/effect-size review is complete.
  - Table 4: compact main-text table.
- `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md` has started the Table 3 review and identifies why the current Table 3 remains candidate-only.

Inputs to inspect first:

- `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md`
- `docs/manuscript/tables/table_03_statistical_summary.md`
- `docs/manuscript/tables/table_03_statistical_summary.csv`
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`
- `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`
- `scripts/manuscript_assets/build_manuscript_assets.py`
- `scripts/compute_seed_metric_summary.py` if relevant
- authoritative source CSVs referenced in `STATISTICAL_REPORTING_READINESS.csv`

Immediate work:

1. Decide the safest final Table 3 path:
   - Option A: regenerate/revise Table 3 with explicit grouping/slice columns and final-status flags; or
   - Option B: create a compact final-safe main-text Table 3 and move the full statistical map to supplement/candidate status.

2. Preserve the current claim posture:
   - Do not invent effect sizes, confidence intervals, seed counts, or comparisons.
   - Keep C1 benchmark/model-family-specific.
   - Keep C2 conflict-specific, not a blanket context-is-required-for-every-suffix claim.
   - Keep C5 ceiling-limited and supplied-context only.
   - Keep C6 as observed finite-budget degradation only; no fitted capacity law.
   - Keep C7 boundary/supplement unless paired seed-level local-vs-global grouping exists.
   - Keep C13 symbolic transition-cue context selection only.
   - Keep Exp15 replay collapse as non-claim pending audit.

3. If regenerating/revising Table 3:
   - Add enough grouping/slice metadata to make rows unambiguous, especially for Exp12 clean scaling, Exp13 budget ratios, Exp14 cue-count/corruption-rate rows, and Exp15/Exp13.2 comparison families if included.
   - Include final-status or manuscript-use flags such as `final_safe_descriptive`, `candidate_pending_grouping`, `supplement_only`, or `non_claim`.
   - Keep Table 4 separate unless there is an explicit reason to merge Exp15 neural comparator statistics into Table 3.

4. If creating a compact main-text Table 3:
   - Include only final-safe descriptive rows/claim-level summaries.
   - Move detailed statistical-map material to a supplement/candidate artifact.
   - Make the caveats explicit in captions and operational docs.

5. Sync operational docs after Table 3 work:
   - `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`
   - `docs/manuscript/MANUSCRIPT_TODO.md`
   - `docs/synthesis/PUBLICATION_READINESS.md`
   - `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md` if Table 3 status changes.
   - `docs/source_data/STATISTICAL_REPORTING_READINESS.csv` if final statuses change.

6. Update this `NEXT_STEP_PROMPT.md` at the end so the next prompt points to the next real blocker after Table 3, not back to completed work.

Do not do these unless explicitly requested:

- Do not rerun experiments.
- Do not modify experiment code.
- Do not start Exp16 or optional successor experiments.
- Do not add memory-augmented/key-value neural baselines unless a venue/reviewer strategy requires them.
- Do not audit Exp15 replay unless specifically requested.
- Do not broaden claims beyond the retained post-15A posture.
- Do not create final bibliography files until a venue/citation convention is chosen.

Definition of done:

- Table 3 is either final-safe for manuscript use or explicitly split into compact-main plus supplementary/candidate statistical map.
- Table 3 rows have enough grouping/slice metadata to avoid ambiguity, or the detailed ambiguous rows are removed from main-text use.
- Operational docs no longer describe Table 3 grouping/effect-size review as merely unstarted.
- `python scripts/verify_doc_source_paths.py` passes, or inability to run is documented with exact reason.
- Final response summarizes changed files, verification status, final Table 3 status, and remaining blockers.
```
