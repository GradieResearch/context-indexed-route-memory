# Manuscript Finalization

Purpose: collect the final manuscript-readiness plan, working checklist, status reports, and handoff prompts for the Context-Indexed Route Memory manuscript.

This folder is the operating area for the finalization phase after `MANUSCRIPT_V2.md`, Exp13.2 import, Exp14 import, Exp15 import, Analysis Pass 15A retained-claim hardening, the citation/prior-art audit, and the checked citation-ledger pass.

## Files

- [`MANUSCRIPT_FINALIZATION_PLAN.md`](MANUSCRIPT_FINALIZATION_PLAN.md) - limitation-by-limitation plan for closing or explicitly retaining reviewer-risk items.
- [`FINALIZATION_CHECKLIST.md`](FINALIZATION_CHECKLIST.md) - practical checklist for tracking manuscript finalization work.
- [`NEXT_STEP_PROMPT.md`](NEXT_STEP_PROMPT.md) - current agent-ready prompt for the next finalization action: human decision checkpoint plus guarded manuscript integration where decisions are available.
- [`CITATION_PRIOR_ART_INSERTION_REPORT.md`](CITATION_PRIOR_ART_INSERTION_REPORT.md) - report from the checked citation-ledger and closest-prior-art table creation pass.
- [`CITATION_LEDGER_INTEGRATION_STATUS.md`](CITATION_LEDGER_INTEGRATION_STATUS.md) - current status of citation-ledger integration after the follow-up pass.
- [`NEXT_STEP_PROMPT_AFTER_CITATION_LEDGER.md`](NEXT_STEP_PROMPT_AFTER_CITATION_LEDGER.md) - historical handoff prompt used after the citation-ledger pass; retained as an audit trail and superseded by `NEXT_STEP_PROMPT.md`.

## Current Finalization Posture

The first manuscript remains a controlled symbolic/mechanistic benchmark paper. `MANUSCRIPT_V2.md` has been captured, Exp15 is imported as completed minimal fixed-profile neural-comparator evidence, Table 4 is present as a compact source-data-backed comparator table, and `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md` records the post-15A retained claim posture.

The citation/prior-art work is no longer at the raw-audit stage:

- `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md` is retained as the audit trail.
- `docs/manuscript/REFERENCES.md` is the checked venue-neutral reference ledger.
- `docs/manuscript/closest_prior_art_table.md` is the checked closest-prior-art companion artifact.
- `docs/manuscript/finalization/CITATION_PRIOR_ART_INSERTION_REPORT.md` records the citation-ledger pass.
- `docs/manuscript/finalization/CITATION_LEDGER_INTEGRATION_STATUS.md` records why the manuscript was not mechanically converted to a final citation style yet.

Current retained V2 posture:

- Main scientific spine: C1, C2, C3, C4, C5, C6, and C13.
- Discussion/table baseline claim: C12.
- Boundary or supplement only: C7, C8, C10, and C11.
- Out of the main claim set or non-claims: C9, Exp13.1 positive lesion evidence, Exp15 replay collapse, broad CIRM-over-neural claims, raw sensory latent-world discovery, and biological validation.

Exp15 does not justify broad neural-superiority claims or exhaustive neural-benchmark framing. The post-Exp15 posture is controlled by `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md` when it is stricter than earlier claim-freeze language, and by `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md` for retained/boundary/non-claim status.

## Current Next Action

Use `NEXT_STEP_PROMPT.md` for the next phase.

The next step is not another citation-audit pass. It is a human-decision checkpoint followed by guarded manuscript integration:

1. Choose the citation/export convention, or explicitly keep `docs/manuscript/REFERENCES.md` as the venue-neutral ledger for now.
2. Decide whether `docs/manuscript/closest_prior_art_table.md` should be inserted into Section 2.7 as a compact table, converted into prose, or retained as a companion artifact.
3. Resolve human figure/table decisions where possible: Figure 4, Figure 5, Table 3, and Table 4 are the main open items.
4. After those decisions are available, update `MANUSCRIPT_V2.md`, `MANUSCRIPT_TODO.md`, `FINALIZATION_CHECKLIST.md`, and readiness docs accordingly.
5. Run `python scripts/verify_doc_source_paths.py` in a local checkout or CI environment before merging a final readiness handoff.
