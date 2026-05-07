# Prompt: Update Claims, Figures, and TODOs

```text
You are working inside the local repository:

GradieResearch/context-indexed-route-memory

Your task is a focused manuscript-doc consistency pass after importing a new experiment analysis.

Do not modify experiment code.
Do not rerun experiments.
Do not add new scientific claims unless clearly required.
Do not strengthen claims beyond evidence.

Inspect:

- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/synthesis/PROJECT_STATUS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/synthesis/NEXT_EXPERIMENTS.md`
- the new experiment summary
- the new thread digest
- the owning experiment README completed-runs/results section
- local artifacts for the new experiment

Goal:
Ensure the new experiment analysis is consistently reflected across the manuscript docs.

Check:

1. Every affected claim has:
   - status;
   - evidence;
   - caveat;
   - source thread;
   - source artifact;
   - required follow-up.
   Source artifacts must use current `experiments/...` paths, or be marked planned/missing/future/local verification pending.

2. Claim statuses are conservative:
   - Strong only for robust internal evidence with clear artifacts.
   - Promising for clear but incomplete evidence.
   - Preliminary for early or caveated evidence.
   - Needs metric cleanup / baseline / rerun where appropriate.

3. Figure plan:
   - every figure cites real source artifacts;
   - generated plots are not treated as final figure scripts unless they are;
   - main vs supplement status is clear.

4. Limitations:
   - new caveats are listed;
   - non-claims remain intact.

5. TODOs:
   - completed work is marked complete if appropriate;
   - new required follow-ups are added;
   - next experiment remains clear.

6. Run documentation:
   - completed runs are recorded in the owning experiment README;
   - SQLite/database paths, if any, point to one run-specific file under the owning experiment directory;
   - GPU/CPU limitations are documented where relevant.

Create or update:

`docs/repo_audit/EXP<ID>_MANUSCRIPT_DOC_CONSISTENCY_REPORT.md`

Include:
- inconsistencies found;
- fixes made;
- unresolved issues;
- path verifier result.

Run:

python scripts/verify_doc_source_paths.py

Do not commit.
Do not push.
```
