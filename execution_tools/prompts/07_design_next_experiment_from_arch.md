# Prompt: Design Next Experiment From Research Architecture

```text
You are helping decide the next experiment in the Context-Indexed Route Memory research program.

Inputs to inspect:
- `docs/experiments/EXPERIMENT_REGISTRY.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/synthesis/NEXT_EXPERIMENTS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- latest experiment summary
- latest analysis import QA report
- latest thread digest
- the relevant owning experiment README and local artifacts

Task:
Recommend the next scientific/repository action.

Do not default to creating a new experiment if repo cleanup, rerun, metric correction, baseline implementation, or manuscript drafting is more important.
Determine the latest actionable state from the registry and local `experiments/` directories; do not assume that a planned placeholder experiment already exists.
If recommending a new or successor experiment, it must be a new self-contained directory under `experiments/`.
If recommending a rerun, keep outputs inside the owning experiment directory with a new run ID and a new per-run database file if SQLite is used.

Output:

# Next Action Recommendation

## 1. Current state

Summarize what the latest experiment changed.

## 2. Manuscript blockers

List remaining blockers:
- metric cleanup;
- baselines;
- confidence intervals;
- final figures;
- prior-art/novelty source import;
- applied bridge;
- others.

## 3. Candidate next actions

Compare at least three options:

| Option | Description | Pros | Cons | Manuscript value | Risk |
|---|---|---|---|---|---|

Possible options:
- rerun latest experiment;
- analyze more deeply;
- implement baseline suite;
- design next experiment;
- write manuscript draft v0;
- improve figure scripts;
- create applied bridge;
- perform literature/prior-art consolidation.

## 4. Recommendation

Choose one primary next action.

## 5. Why this is the next best action

Be explicit.

## 6. Proposed design or task plan

If recommending an experiment, include:
- proposed `experiments/<experiment_dir>/` path;
- purpose;
- hypotheses;
- variants;
- metrics;
- outputs.
- GPU/device plan and run-artifact layout.

If recommending repo/manuscript work, include:
- files to update;
- acceptance criteria;
- QA plan.

## 7. Risks

What could go wrong?

## 8. Success criteria

How will we know this action is complete?

## 9. Prompt for local agent

End with a ready-to-copy local-agent prompt for the recommended next action.
```
