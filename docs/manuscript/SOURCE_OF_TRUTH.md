# Source of Truth

Purpose: Explain which documents are authoritative when repository docs disagree, especially now that the manuscript package is moving from V2 finalization artifacts toward a real V3 draft.

## Canonical docs

Use these first:

- Current manuscript draft: `docs/manuscript/draft/MANUSCRIPT_V2.md`
- Current manuscript work queue: `docs/manuscript/MANUSCRIPT_TODO.md`
- Current finalization prompt: `docs/manuscript/finalization/NEXT_STEP_PROMPT.md`
- Active finalization checklist: `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`
- Current pre-venue decision status: `docs/manuscript/finalization/HUMAN_REVIEW_VENUE_STATUS.md`
- Submission readiness: `docs/synthesis/PUBLICATION_READINESS.md`
- Claim freeze for the first manuscript: `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`
- Post-Exp15 claim narrowing: `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`
- Post-15A retained-claim/statistical-hardening control document: `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`
- Claims: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- Figures: `docs/manuscript/FIGURE_PLAN.md`
- Checked reference metadata: `docs/manuscript/REFERENCES.md`
- Closest-prior-art positioning source: `docs/manuscript/closest_prior_art_table.md`
- Reproducibility: `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`
- Experiment list: `docs/experiments/EXPERIMENT_REGISTRY.md`

## Historical / audit-trail docs

These are useful provenance, but they are not active instructions unless an active canonical doc points to them:

- `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md`
- `docs/manuscript/finalization/CITATION_PRIOR_ART_INSERTION_REPORT.md`
- `docs/manuscript/finalization/CITATION_LEDGER_INTEGRATION_STATUS.md`
- `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md`
- `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md`
- `docs/manuscript/finalization/TABLE_3_VERIFICATION_ALIGNMENT_STATUS.md`
- `docs/manuscript/finalization/CAPTION_TODO_CLEANUP_STATUS.md`
- `docs/manuscript/finalization/SECTION_2_7_PROSE_PATCH.md`
- `docs/manuscript/finalization/NEXT_STEP_PROMPT_AFTER_CITATION_LEDGER.md`
- `docs/manuscript/finalization/MANUSCRIPT_TODO_CITATION_LEDGER_UPDATE.md`

## Non-authoritative docs and debris

- Thread exports are source material, not final claims.
- Generated reports are local artifacts, not manuscript prose.
- Historical experiment notes may contain outdated framing.
- Roadmaps and issue templates are handoff aids, not evidence.
- The old backup draft file named `bkup.orig` has been removed and was never canonical.

## Rule

If there is a conflict:

1. Generated artifact/source data wins for numeric claims.
2. `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md` wins for post-Exp15 narrowing when it is stricter than earlier claim-freeze language.
3. `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md` wins for post-15A retained-claim role, source-CSV mapping, and retained/boundary/non-claim status.
4. `docs/manuscript/REFERENCES.md` wins for checked citation metadata unless a later chosen bibliography export is created from it.
5. `docs/manuscript/closest_prior_art_table.md` wins for closest-prior-art positioning structure when more detailed traceability is needed.
6. `docs/manuscript/finalization/HUMAN_REVIEW_VENUE_STATUS.md` wins for the current pre-venue decision gate.
7. `docs/manuscript/finalization/NEXT_STEP_PROMPT.md` wins for current next work.
8. `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md` wins for first-manuscript inclusion/exclusion decisions not superseded by post-Exp15 or post-15A docs.
9. `docs/manuscript/CLAIMS_AND_EVIDENCE.md` wins for current claim wording outside the frozen first-manuscript subset and post-Exp15/post-15A controls.
10. `docs/manuscript/LIMITATIONS_AND_THREATS.md` wins for caveats.
11. Thread exports are used only as historical context unless imported into canonical docs.

## Current Scope Note

The repository is now post-Exp15, post-Manuscript-V2-capture, post-Analysis-Pass-15A, post-citation-ledger, post-Section-2.7 prose integration, post-compact Table 3 split, post-caption/TODO cleanup, and post-pre-venue status capture.

The next manuscript-facing milestone is a V3 drafting/flow-review pass, not another finalization-status proliferation pass.

Current retained V2 posture:

- Main scientific spine: C1, C2, C3, C4, C5, C6, and C13.
- Discussion/table baseline claim: C12.
- Boundary or supplement only: C7, C8, C10, and C11.
- Out of the main claim set or non-claims: C9, Exp13.1 positive lesion evidence, Exp15 replay collapse, broad CIRM-over-neural claims, raw sensory latent-world discovery, and biological validation.

This does **not** make the repository submission-ready. Remaining active work is manuscript flow review/V3 drafting, target venue/citation convention selection, final figure/table and supplement decisions, fresh command verification, and license/citation metadata.

Use `docs/manuscript/finalization/NEXT_STEP_PROMPT.md` for the next phase.
