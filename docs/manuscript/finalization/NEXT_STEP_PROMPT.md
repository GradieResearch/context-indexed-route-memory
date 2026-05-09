# Next Step Prompt: Final Citation Insertion And Human Figure/Table Decisions

Use this prompt in a new session after the post-15A citation/prior-art audit and figure/table human-review checklist have been merged.

```text
You are working in the repository:

GradieResearch/context-indexed-route-memory

Task: Convert the post-15A citation/prior-art audit into final manuscript citation work and perform human-directed review of the generated candidate figure/table package. Do not change the experimental record.

Starting context:

The repository is now post-Exp15, post-Manuscript-V2-capture, post-Analysis-Pass-15A, and post-citation/figure-review-audit.

- Experiment 15 is complete and imported as minimal fixed-profile neural comparator evidence.
- The imported Exp15 run is `exp15_full_20260508_092811`.
- `docs/manuscript/draft/MANUSCRIPT_V2.md` exists.
- `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md` exists.
- `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md` exists.
- `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md` exists.
- `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md` exists.
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv` separates retained, boundary, supplement, blocked, and non-claim evidence.
- `docs/manuscript/tables/table_04_exp15_neural_comparator.md` exists.
- `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv` exists.

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
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md`
- `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`
- `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`
- `docs/manuscript/draft/MANUSCRIPT_V2.md`
- `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`
- `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/BASELINE_REQUIREMENTS.md`
- `docs/manuscript/NOVELTY_POSITIONING.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/source_data/SOURCE_DATA_MANIFEST.csv`
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`
- `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`
- `docs/manuscript/tables/table_01_claim_evidence.md`
- `docs/manuscript/tables/table_02_run_integrity.md`
- `docs/manuscript/tables/table_03_statistical_summary.md`
- `docs/manuscript/tables/table_04_exp15_neural_comparator.md`

Primary objective:

Move from audit artifacts to manuscript-facing deliverables: verified bibliography/citation insertion, closest-prior-art risk table prose, and resolved figure/table placement/caption decisions where a human decision is available.

Concrete work:

1. Final citation insertion.
   - Use `docs/manuscript/CITATION_PRIOR_ART_AUDIT.md` as the source-backed starting point.
   - Verify metadata against primary sources before creating final bibliography entries.
   - Add or update the repository bibliography file only if the repository convention supports one.
   - Replace manuscript placeholder keys with final citation keys or a consistent citation format.
   - Do not add fake citations, fake BibTeX, or unsupported prior-art claims.

2. Closest-prior-art table.
   - If retained in Section 2.7, add a compact table comparing CIRM to closest prior-art families.
   - Include task-gated lookup, mixture-of-experts/modular routing, fast weights/linear attention, differentiable/external memory, neural algorithmic reasoning, symbolic graph/path algorithms, hippocampal/CLS inspiration, and memory-augmented neural baselines where appropriate.
   - The table must state what is inherited, what is not claimed as novel, and what the paper contributes narrowly.

3. Human figure/table decisions.
   - Use `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md` as the decision tracker.
   - Resolve any decisions the human has explicitly made.
   - If the human has not chosen, preserve the current conservative defaults:
     - Figures 1-3 stay main.
     - Figure 4 stays main-narrow for C6, with C7 boundary caveat.
     - Figure 5 stays main-narrow for V2 hardening, movable to supplement by venue decision.
     - Table 4 stays compact main-text neural comparator, movable to supplement by venue decision.
     - Table 3 remains candidate until grouping/effect-size review is completed.
   - Do not promote Exp15 analysis plots into final figures unless explicitly requested.

4. Update operational docs after concrete changes.
   - Update `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`.
   - Update `docs/manuscript/MANUSCRIPT_TODO.md`.
   - Update `docs/synthesis/PUBLICATION_READINESS.md` if readiness status changes.
   - Update `docs/manuscript/FIGURE_PLAN.md` only if figure/table placement or caption-readiness decisions change.
   - Update `docs/manuscript/NOVELTY_POSITIONING.md` if prior-art positioning changes.

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

- Citation placeholders in `MANUSCRIPT_V2.md` are replaced or explicitly left as tracked TODOs with a reason.
- Bibliography metadata is verified and stored using the repository's chosen convention, if one exists.
- The closest-prior-art table is added or explicitly deferred.
- Figure/table decisions from `FIGURE_TABLE_HUMAN_REVIEW.md` are resolved where human direction exists, or conservative defaults are preserved.
- Finalization checklist and manuscript TODO reflect actual progress.
- `docs/synthesis/PUBLICATION_READINESS.md` reflects the new readiness posture if it changed.
- `python scripts/verify_doc_source_paths.py` passes, or failures/inability to run are listed with exact paths and fixes.
- Final response summarizes changed files, remaining blockers, unresolved human decisions, and verification result.
```
