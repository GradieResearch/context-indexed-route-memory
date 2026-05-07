# Source of Truth

Purpose: Explain which documents are authoritative when repository docs disagree.

## Canonical docs

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
2. `docs/manuscript/CLAIMS_AND_EVIDENCE.md` wins for current claim wording.
3. `docs/manuscript/LIMITATIONS_AND_THREATS.md` wins for caveats.
4. Thread exports are used only as historical context unless imported.

## Current Scope Note

For the current P0/P1 publication-cleanup handoff, Exp13.2 is intentionally excluded. Existing Exp13.2 artifacts or historical import notes do not update active claim wording until a separate Exp13.2 analysis/import/alignment pass updates the canonical docs together.
