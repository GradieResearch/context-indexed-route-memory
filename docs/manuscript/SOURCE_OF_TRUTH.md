# Source of Truth

Purpose: Explain which documents are authoritative when repository docs disagree.

## Canonical docs

- Claim freeze for the first manuscript: `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`
- Claims: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- Figures: `docs/manuscript/FIGURE_PLAN.md`
- Submission readiness: `docs/synthesis/PUBLICATION_READINESS.md`
- Experiment list: `docs/experiments/EXPERIMENT_REGISTRY.md`
- Next work: `docs/manuscript/MANUSCRIPT_TODO.md`
- Reproducibility: `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`

## Non-authoritative docs

- Thread exports are source material, not final claims.
- Generated reports are local artifacts, not manuscript prose.
- Historical experiment notes may contain outdated framing.
- Roadmaps and issue templates are handoff aids, not evidence.

## Rule

If there is a conflict:

1. Generated artifact/source data wins for numeric claims.
2. `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md` wins for first-manuscript inclusion/exclusion decisions once present.
3. `docs/manuscript/CLAIMS_AND_EVIDENCE.md` wins for current claim wording outside the frozen first-manuscript subset.
4. `docs/manuscript/LIMITATIONS_AND_THREATS.md` wins for caveats.
5. Thread exports are used only as historical context unless imported.

## Current Scope Note

The repository is now in a post-Exp14 manuscript-readiness state. Exp13.2 has been imported as a completed symbolic/algorithmic baseline suite, and Exp14 has been imported as completed symbolic transition-cue context-selection evidence.

This does **not** make the repository submission-ready. Exp13.2 partially satisfies symbolic/algorithmic baseline coverage, but neural baselines, prior-art/novelty import, manuscript-grade uncertainty tables, final figure scripts, command verification, and license/citation metadata remain open readiness items.

Use the first-manuscript claim-freeze document for the next phase: it decides which claims are main-text candidates, which are supplement-only, and which must remain future work or non-claims.
