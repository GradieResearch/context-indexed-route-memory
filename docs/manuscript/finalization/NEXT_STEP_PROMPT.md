# Next Step Prompt: Human Decision Checkpoint And Guarded Manuscript Integration

Use this prompt after the citation-ledger integration status has merged.

```text
You are working in the repository:

GradieResearch/context-indexed-route-memory

Task: Determine whether the required human decisions for final citation style, closest-prior-art placement, and figure/table placement have been made. If decisions are available, apply only those decisions to the manuscript and operational docs. If decisions are not available, call out the missing decisions and pause without inventing them.

Starting context:

The repository is post-Exp15, post-Manuscript-V2-capture, post-Analysis-Pass-15A, post-citation/prior-art audit, post-citation-ledger pass, and post-citation-ledger integration-status pass.

Current completed artifacts:

- `docs/manuscript/draft/MANUSCRIPT_V2.md`
- `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`
- `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`
- `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md`
- `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`
- `docs/manuscript/REFERENCES.md`
- `docs/manuscript/closest_prior_art_table.md`
- `docs/manuscript/finalization/CITATION_PRIOR_ART_INSERTION_REPORT.md`
- `docs/manuscript/finalization/CITATION_LEDGER_INTEGRATION_STATUS.md`
- `docs/manuscript/tables/table_04_exp15_neural_comparator.md`
- `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`

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
- `docs/manuscript/finalization/CITATION_PRIOR_ART_INSERTION_REPORT.md`
- `docs/manuscript/finalization/CITATION_LEDGER_INTEGRATION_STATUS.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/manuscript/REFERENCES.md`
- `docs/manuscript/closest_prior_art_table.md`
- `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md`
- `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`
- `docs/manuscript/draft/MANUSCRIPT_V2.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/NOVELTY_POSITIONING.md`
- `docs/synthesis/PUBLICATION_READINESS.md`

Primary objective:

Move the repo from out-of-sync finalization docs to a clear next actionable state. The next actionable state is either:

1. apply explicit human decisions and update the manuscript/docs; or
2. pause with a concise list of missing human decisions.

Decision checkpoint:

Before editing the manuscript, determine whether the human has explicitly decided each item below.

1. Citation/export convention:
   - Pandoc-style citation keys;
   - BibTeX;
   - CSL JSON;
   - numbered references;
   - target-journal author-year style;
   - or explicitly keep `docs/manuscript/REFERENCES.md` as a venue-neutral ledger for now.

2. Closest-prior-art placement:
   - inline `docs/manuscript/closest_prior_art_table.md` into Section 2.7 as a compact table;
   - convert it into prose in Section 2.7;
   - or keep it as a companion artifact until target-venue formatting.

3. Figure/table placement and review:
   - Figures 1-3 main or changed;
   - Figure 4 main-narrow versus supplement;
   - Figure 5 main-narrow versus supplement;
   - Table 3 grouping/effect-size review status;
   - Table 4 main text versus supplement.

If these decisions have not been made, do not choose for the human. Preserve conservative defaults and pause.

Concrete work if decisions are available:

1. Citation convention integration.
   - Use `docs/manuscript/REFERENCES.md` as the checked metadata source.
   - Convert only to the chosen convention.
   - Do not add fake BibTeX, fake CSL JSON, fake DOIs, or unsupported source claims.
   - Do not propagate the earlier `Eichenbaum2017` DOI/title mismatch. The checked entry is: Eichenbaum, H. (2017). On the Integration of Space, Time, and Memory. Neuron, 95(5), 1007-1018. DOI: `10.1016/j.neuron.2017.06.036`.

2. Closest-prior-art integration.
   - Use `docs/manuscript/closest_prior_art_table.md`.
   - Preserve the `what is inherited / what is not claimed / narrow contribution` structure.
   - Do not claim novelty for context gating, recurrence, replay, task isolation, modular routing, or memory augmentation in isolation.

3. Citation-risk wording cleanup.
   - Narrow `modern transformer memory systems` unless exact transformer-memory references are added.
   - Narrow `task masks, adapters, parameter isolation` unless exact references for those families are added.
   - Keep neuroscience citations motivational only.
   - Keep Exp15 neural comparator wording fixed-profile and non-exhaustive.

4. Figure/table decisions.
   - Use `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md` as the tracker.
   - If the human has not chosen, preserve conservative defaults:
     - Figures 1-3 stay main.
     - Figure 4 stays main-narrow for C6, with C7 boundary caveat.
     - Figure 5 stays main-narrow for V2 hardening, movable to supplement by venue decision.
     - Table 4 stays compact main-text neural comparator, movable to supplement by venue decision.
     - Table 3 remains candidate until grouping/effect-size review is completed.
   - Do not promote Exp15 analysis plots into final figures unless explicitly requested.

5. Operational docs.
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
- Do not add fake citations, fake BibTeX, fake CSL JSON, or unsupported related-work claims.
- Do not broaden claims beyond the retained post-15A posture.

Definition of done:

- The current repository state is checked against the completed citation-ledger artifacts.
- Missing human decisions are listed explicitly, or available decisions are applied.
- `MANUSCRIPT_V2.md` is modified only where a decision exists or a low-risk wording cleanup is clearly supported by existing docs.
- `FINALIZATION_CHECKLIST.md`, `MANUSCRIPT_TODO.md`, and readiness docs reflect the actual current state.
- `python scripts/verify_doc_source_paths.py` passes, or failures/inability to run are listed with exact paths and fixes.
- Final response summarizes changed files, remaining blockers, unresolved human decisions, and verification result.
```
