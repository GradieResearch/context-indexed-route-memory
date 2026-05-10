# Human Decision Integration Status

Date: 2026-05-10

Status: human decisions received and recorded for guarded manuscript integration.

## Summary

This pass follows `docs/manuscript/finalization/NEXT_STEP_PROMPT.md` after the required human decisions were explicitly provided.

The repository should now treat the previously blocked human-decision checkpoint as resolved for the following items:

1. citation/export convention;
2. closest-prior-art Section 2.7 placement;
3. figure/table placement posture for Figures 1-5 and Tables 3-4.

No new experiments were started. No experiment code was modified. No broad claims were added.

## Human decisions recorded

### Citation/export convention

Decision: keep `docs/manuscript/REFERENCES.md` as the venue-neutral reference ledger for now.

Rationale: no target venue has been selected yet, so the repository should not prematurely choose BibTeX, CSL JSON, numbered references, Pandoc conversion, or a target-journal author-year style.

Operational consequence:

- Preserve manuscript citation placeholders for now.
- Do not add fake BibTeX, fake CSL JSON, fake DOIs, or journal-specific citation formatting.
- Use `docs/manuscript/REFERENCES.md` as the authoritative checked metadata source until a target venue/convention is chosen.

### Closest-prior-art placement

Decision: convert `docs/manuscript/closest_prior_art_table.md` into prose in Section 2.7, while retaining the table as a companion artifact.

Operational consequence:

- Section 2.7 should contain prose-level positioning derived from the closest-prior-art table.
- `docs/manuscript/closest_prior_art_table.md` remains the source/checking artifact for inherited ideas, non-novel claims, and the narrow contribution.
- The table can still be converted into a venue-specific table or supplement later if needed.

The companion table has been updated to record this placement decision.

### Figure/table placement

Decision:

- Figures 1-3: main.
- Figure 4: supplement unless the finite-budget story is emphasized.
- Figure 5: main-narrow, because Exp14 helps reduce the oracle-context criticism.
- Table 3: keep candidate until grouping/effect-size review is done.
- Table 4: compact main-text table, because Exp15 materially shapes the paper's claims.

Operational consequence:

- Figure 4 should no longer be treated as default main-narrow; it is a supplement/default unless the manuscript intentionally emphasizes finite structural budget.
- Figure 5 remains a main-narrow result with symbolic transition-cue caveats.
- Table 3 remains candidate and should not be cited as final statistical evidence until grouping/effect-size review is complete.
- Table 4 remains a compact main-text Exp15 neural comparator table with fixed-profile/non-exhaustive caveats.

## Recommended Section 2.7 prose integration

Replace the prior Section 2.7 TODO with prose equivalent to the following:

> The contribution is best described as a controlled route-memory decomposition, not as novelty of any single mechanism. Context gating, recurrence, modular routing, differentiable or external memory, fast weights, graph reasoning, and hippocampal indexing all have substantial prior art. The present benchmark deliberately puts these ideas into a narrow symbolic transition setting where each can be probed separately: one-step transition storage, recurrent route execution, supplied versus selected context, endpoint memorization, suffix-route composition, finite structural budget pressure, and minimal neural comparator behavior. This framing also absorbs the Exp13.2 and Exp15 caveats: an oracle context-gated lookup table and context-conditioned neural transition learner can solve the clean supplied-context slice, so clean ceiling accuracy is not the novelty claim. The manuscript contribution is the evidence map showing where these computational contracts diverge under controlled interference.

The underlying source artifact remains `docs/manuscript/closest_prior_art_table.md`.

## Guardrails preserved

- Keep broad CIRM-over-neural-model claims out of the manuscript.
- Keep Exp15 as minimal fixed-profile neural comparator evidence, not exhaustive neural benchmarking.
- Keep Exp14 framed as symbolic transition-cue context selection, not raw sensory latent-world discovery.
- Keep neuroscience references motivational only.
- Keep Exp15 replay collapse as non-claim pending audit.
- Keep Exp13.1 lesion evidence out of the positive mechanism evidence set unless audited/rerun.
- Keep C9 out of the main claim set unless seen/unseen/all metric cleanup is completed.

## Verification

This pass was performed through the GitHub API. The repository could not be cloned into the execution container because direct GitHub network access from the container failed with DNS resolution errors. Therefore `python scripts/verify_doc_source_paths.py` was not run locally in this session.

No new active source paths were introduced except this report file and the already-existing companion table update. A follow-up CI/local pass should run:

```bash
python scripts/verify_doc_source_paths.py
```

## Remaining blockers after this decision pass

- Apply the Section 2.7 prose replacement directly into `docs/manuscript/draft/MANUSCRIPT_V2.md` if not already applied in the PR diff.
- Update `docs/manuscript/FIGURE_PLAN.md` and `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md` to reflect Figure 4 supplement-default, Figure 5 main-narrow, Table 3 candidate, and Table 4 compact main-text status.
- Review and finalize Table 3 grouping/effect-size rows.
- Run the documentation source-path verifier in a local checkout or CI.
- Choose a target venue later; only then convert `docs/manuscript/REFERENCES.md` into the required final bibliography/citation format.
