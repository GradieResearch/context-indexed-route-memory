# Next Step Prompt: Citation Convention And Figure/Table Human Decisions

Use this prompt after the citation ledger / closest-prior-art table pass has merged.

```text
You are working in the repository:

GradieResearch/context-indexed-route-memory

Task: Convert the newly added citation ledger and closest-prior-art table into final manuscript-facing citation/related-work edits, then resolve figure/table decisions only where the human has explicitly decided.

Starting context:

The repository is post-Exp15, post-Manuscript-V2-capture, post-Analysis-Pass-15A, post-citation/prior-art audit, and post-citation-ledger pass.

New artifacts from the citation-ledger pass:

- `docs/manuscript/REFERENCES.md`
- `docs/manuscript/closest_prior_art_table.md`
- `docs/manuscript/finalization/CITATION_PRIOR_ART_INSERTION_REPORT.md`

Important correction from the citation-ledger pass:

- Do not propagate the earlier `Eichenbaum2017` DOI/title mismatch.
- The checked ledger entry is: Eichenbaum, H. (2017). On the Integration of Space, Time, and Memory. Neuron, 95(5), 1007-1018. DOI: `10.1016/j.neuron.2017.06.036`.

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

- `docs/manuscript/REFERENCES.md`
- `docs/manuscript/closest_prior_art_table.md`
- `docs/manuscript/finalization/CITATION_PRIOR_ART_INSERTION_REPORT.md`
- `docs/manuscript/draft/MANUSCRIPT_V2.md`
- `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`
- `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/synthesis/PUBLICATION_READINESS.md`

Primary objective:

Move from checked citation ledger to final manuscript integration without inventing citation metadata or broadening scientific claims.

Concrete work:

1. Decide or ask for the manuscript citation/export convention if not already known.
   - Acceptable options include Pandoc-style citation keys, BibTeX, CSL JSON, numbered references, or target-journal author-year style.
   - Do not add fake BibTeX.
   - If no convention is chosen, preserve bracketed placeholder keys and treat `docs/manuscript/REFERENCES.md` as the repository bibliography ledger.

2. Integrate the closest-prior-art table.
   - If the human wants it in the manuscript, insert a compact version in Section 2.7 of `MANUSCRIPT_V2.md`.
   - If the human does not decide, preserve `docs/manuscript/closest_prior_art_table.md` as a companion artifact and mark manuscript insertion as pending.
   - Preserve the explicit `what is inherited / what is not claimed / narrow contribution` structure.

3. Fix citation-risk wording.
   - Narrow `modern transformer memory systems` unless exact transformer-memory references are added.
   - Narrow `task masks, adapters, parameter isolation` unless exact references for those families are added.
   - Keep neuroscience citations motivational only.
   - Keep Exp15 neural comparator wording fixed-profile and non-exhaustive.

4. Human figure/table decisions.
   - Use `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md` as the tracker.
   - If the human has not chosen, preserve conservative defaults:
     - Figures 1-3 stay main.
     - Figure 4 stays main-narrow for C6, with C7 boundary caveat.
     - Figure 5 stays main-narrow for V2 hardening, movable to supplement by venue decision.
     - Table 4 stays compact main-text neural comparator, movable to supplement by venue decision.
     - Table 3 remains candidate until grouping/effect-size review is completed.
   - Do not promote Exp15 analysis plots into final figures unless explicitly requested.

5. Update operational docs.
   - Update `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`.
   - Update `docs/manuscript/MANUSCRIPT_TODO.md`.
   - Update `docs/synthesis/PUBLICATION_READINESS.md` if readiness posture changes.
   - Update `docs/manuscript/FIGURE_PLAN.md` only if placement/caption decisions change.
   - Update `docs/manuscript/NOVELTY_POSITIONING.md` only if prior-art positioning changes.

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

- Citation convention is chosen or explicitly left pending.
- `docs/manuscript/REFERENCES.md` remains the checked metadata ledger or is converted into the chosen bibliography convention.
- `Eichenbaum2017` mismatch is not propagated.
- The closest-prior-art table is inserted into the manuscript or explicitly deferred.
- Figure/table decisions are resolved where human direction exists, or conservative defaults are preserved.
- Finalization checklist and manuscript TODO reflect actual progress.
- `python scripts/verify_doc_source_paths.py` passes, or failures/inability to run are listed with exact paths and fixes.
- Final response summarizes changed files, remaining blockers, unresolved human decisions, and verification result.
```
