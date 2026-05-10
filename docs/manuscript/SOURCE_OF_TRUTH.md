# Source of Truth

Purpose: Explain which documents are authoritative when repository docs disagree.

## Canonical docs

- Claim freeze for the first manuscript: `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`
- Post-Exp15 claim narrowing: `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`
- Post-15A retained-claim/statistical-hardening control document: `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`
- Current manuscript draft: `docs/manuscript/draft/MANUSCRIPT_V2.md`
- Claims: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- Figures: `docs/manuscript/FIGURE_PLAN.md`
- Checked reference metadata: `docs/manuscript/REFERENCES.md`
- Closest-prior-art positioning source: `docs/manuscript/closest_prior_art_table.md`
- Citation-ledger integration status: `docs/manuscript/finalization/CITATION_LEDGER_INTEGRATION_STATUS.md`
- Submission readiness: `docs/synthesis/PUBLICATION_READINESS.md`
- Experiment list: `docs/experiments/EXPERIMENT_REGISTRY.md`
- Next work: `docs/manuscript/finalization/NEXT_STEP_PROMPT.md`; `docs/manuscript/MANUSCRIPT_TODO.md`
- Reproducibility: `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`

## Non-authoritative docs

- Thread exports are source material, not final claims.
- Generated reports are local artifacts, not manuscript prose.
- Historical experiment notes may contain outdated framing.
- Roadmaps and issue templates are handoff aids, not evidence.
- `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md` is now an audit trail rather than the active citation metadata source; use `docs/manuscript/REFERENCES.md` for checked reference metadata.
- `docs/manuscript/finalization/NEXT_STEP_PROMPT_AFTER_CITATION_LEDGER.md` is a historical handoff prompt; use `docs/manuscript/finalization/NEXT_STEP_PROMPT.md` for current next work.

## Rule

If there is a conflict:

1. Generated artifact/source data wins for numeric claims.
2. `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md` wins for post-Exp15 narrowing when it is stricter than earlier claim-freeze language.
3. `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md` wins for post-15A retained-claim role, source-CSV mapping, and retained/boundary/non-claim status.
4. `docs/manuscript/REFERENCES.md` wins for checked citation metadata unless a later chosen bibliography export is created from it.
5. `docs/manuscript/closest_prior_art_table.md` wins for closest-prior-art positioning structure until the human chooses inline table/prose/companion-artifact handling.
6. `docs/manuscript/finalization/CITATION_LEDGER_INTEGRATION_STATUS.md` wins for current citation-convention and closest-prior-art insertion status.
7. `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md` wins for first-manuscript inclusion/exclusion decisions not superseded by post-Exp15 or post-15A docs.
8. `docs/manuscript/CLAIMS_AND_EVIDENCE.md` wins for current claim wording outside the frozen first-manuscript subset and post-Exp15/post-15A controls.
9. `docs/manuscript/LIMITATIONS_AND_THREATS.md` wins for caveats.
10. Thread exports are used only as historical context unless imported.

## Current Scope Note

The repository is now in a post-Exp15, post-Manuscript-V2-capture, post-Analysis-Pass-15A, post-citation-ledger, and post-citation-ledger-integration-status finalization state. Exp13.2 has been imported as completed symbolic/algorithmic baseline-suite evidence, Exp14 has been imported as completed symbolic transition-cue context-selection evidence, and Exp15 has been imported as completed minimal fixed-profile neural-comparator evidence.

`docs/manuscript/draft/MANUSCRIPT_V2.md` has been captured. `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md` narrows the first-manuscript claim posture after Exp15, and `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md` records the post-15A retained claim set and source-CSV mapping.

Citation/prior-art status:

- `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md` is the audit trail.
- `docs/manuscript/REFERENCES.md` is the checked venue-neutral reference ledger.
- `docs/manuscript/closest_prior_art_table.md` is the checked closest-prior-art companion artifact.
- `docs/manuscript/finalization/CITATION_PRIOR_ART_INSERTION_REPORT.md` records the citation-ledger pass.
- `docs/manuscript/finalization/CITATION_LEDGER_INTEGRATION_STATUS.md` records why final citation conversion and closest-prior-art manuscript insertion remain pending.

Current retained V2 posture:

- Main scientific spine: C1, C2, C3, C4, C5, C6, and C13.
- Discussion/table baseline claim: C12.
- Boundary or supplement only: C7, C8, C10, and C11.
- Out of the main claim set or non-claims: C9, Exp13.1 positive lesion evidence, Exp15 replay collapse, broad CIRM-over-neural claims, raw sensory latent-world discovery, and biological validation.

This does **not** make the repository submission-ready. Remaining active work is human choice of citation/export convention, closest-prior-art placement, human review of generated Figures 1-5 and Tables 1-4, final seed-level statistical grouping/effect-size review, fresh command verification, and license/citation metadata.

Use `docs/manuscript/finalization/NEXT_STEP_PROMPT.md` for the next phase: human decision checkpoint and guarded manuscript integration.
