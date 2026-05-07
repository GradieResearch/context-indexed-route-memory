# Prompt: Repository Update QA

```text
You are reviewing the repository update after importing Experiment <ID> analysis.

Do not rewrite broadly.
Your job is adversarial QA.

Inspect:

- new thread digest under `docs/threads/`
- owning experiment README completed-runs/results section
- experiment summary under `docs/experiments/`
- `docs/experiments/EXPERIMENT_REGISTRY.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/synthesis/PROJECT_STATUS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/synthesis/NEXT_EXPERIMENTS.md`
- new import report under `docs/repo_audit/`
- local experiment artifacts

Verify:

1. Thread digest exists and is indexed.
2. Experiment summary cites thread and local artifacts.
3. Owning experiment README records completed runs/results, database paths if present, key config, and summarized results.
4. Claims were not overstrengthened.
5. Every claim has evidence/caveat/source path.
6. Active source paths use current `experiments/...` prefixes, or are marked planned/missing/future/local verification pending.
7. Figure plan paths exist.
8. Limitations include new caveats.
9. TODOs reflect new blockers and completed work.
10. Synthesis docs reflect current status.
11. Path verifier passes.
12. No generated artifact was modified destructively.
13. No completed run was overwritten or appended into a shared historical SQLite database.
14. No planned design is written as completed result.
15. No external baseline is implied unless actually run.
16. No biological or continual-learning overclaim was introduced.

Create:

`docs/repo_audit/EXP<ID>_ANALYSIS_IMPORT_QA.md`

Use this structure:

# Experiment <ID> Analysis Import QA

## Summary

## Checklist

| Check | Result | Evidence | Notes |
|---|---|---|---|

## Problems found

For each problem:
- severity: P0/P1/P2
- file
- issue
- why it matters
- recommended fix

## Final recommendation

Choose one:
- import passed; ready for next experiment planning;
- small cleanup required;
- major evidence-integrity issue; stop and fix before proceeding.

Do not commit.
Do not push.
```
