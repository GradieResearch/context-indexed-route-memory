# Prompt: Analyze Uploaded Results and Prepare Repository Import

```text
I have uploaded the analysis artifacts for Experiment <ID>: <EXPERIMENT_NAME>.

Repository: GradieResearch/context-indexed-route-memory
Owning experiment directory: experiments/<EXPERIMENT_DIR>/

This prompt matches my workflow:
1. ChatGPT designs/implements an experiment.
2. I run it locally.
3. I upload the generated analysis artifacts.
4. ChatGPT analyzes the results.
5. ChatGPT creates a downloadable thread digest zip for repository import.
6. ChatGPT also provides a ready-to-paste Codex prompt to integrate the staged digest into the repo.

Do not update GitHub directly.
Do not invent local artifact paths.
Do not assume implementation correctness without checking artifacts.
Do not treat planned hypotheses as completed results.
Do not strengthen claims beyond the uploaded artifacts and current repository evidence.
Use current repo-relative `experiments/...` paths where known.
If a path is absent, stale, or only represented by the upload bundle, mark it `local verification pending`.

################################################################################
# Part A — Scientific analysis
################################################################################

Inspect, if present:
- generated report;
- validation report;
- metrics CSVs;
- summary CSVs;
- effect-size/statistics CSVs;
- plots;
- run manifest/config;
- progress logs;
- per-run SQLite database or raw run record;
- owning experiment README completed-runs/results section;
- GPU/device/runtime metadata;
- warnings or failed validation checks.

Use repository context when available:
- `docs/experiments/EXPERIMENT_REGISTRY.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/synthesis/PROJECT_STATUS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/synthesis/NEXT_EXPERIMENTS.md`
- owning experiment README and summary docs.

Output:

# Experiment <ID> Analysis: <short title>

## 1. Executive summary
3-6 paragraphs covering what was tested, what is supported, what is weakened/refined, what remains unresolved, and manuscript status.

## 2. Run integrity and artifact audit
Check run profile, run ID, output directory, seed count, variants/baselines, metrics, plots, database/raw record, validation PASS/WARN/FAIL, missing/suspicious artifacts, and device/runtime metadata.

## 3. Primary hypotheses
For each hypothesis:
Hypothesis:
Result:
Evidence:
Caveat:
Status: supported / partially supported / not supported / unclear

## 4. Key results
For each result:
### Result <N>: <title>
Claim:
Evidence:
Caveat:
Source artifact:
Manuscript status: Strong / Promising / Preliminary / Needs rerun / Needs metric cleanup / Needs baseline / Historical only / Do not use

## 5. Mechanism, ablation, and baseline analysis
Discuss storage, context/world selection, recurrence, structural plasticity, consolidation, capacity, generalization boundaries, replay/parameter isolation, oracle context, and failure modes where relevant.

## 6. Statistical and metric critique
Assess seed count, CIs, effect sizes, aggregation, metric validity, hidden failure modes, and missing splits.

## 7. Figure interpretation
For each plot, state what it shows, what claim it might support, caveat, and main/supplement/do-not-use status.

## 8. Relationship to existing claims
Map to existing claims when relevant:
C1 structural plasticity; C2 world/context indexing; C3 recurrence; C4 route-table/composition dissociation; C5 clean capacity scaling; C6 finite-budget degradation; C7 local-vs-global budget; C8 consolidation stability-plasticity; C9 seen primitive vs unseen primitive boundary; C10 context corruption; C11 continuous/noisy bridge; C12 baselines required.
For each: strengthens / weakens / refines / no change / requires new claim / remains limitation.

## 9. Manuscript implications
Where this belongs, whether it changes the spine, figure status, supplement/limitation/future work status, and whether claims must be narrowed.

## 10. Problems, flaws, or rerun requirements
List reruns, metric cleanup, implementation audits, figure regeneration, baseline needs, revised interpretation, artifact import, and local verification issues.

## 11. Recommended repository updates
List exact docs to update: README, summary, registry, thread index, claims/evidence, figure plan, limitations, TODOs, synthesis docs, source data, artifact index, conflict log, import report.

## 12. Recommended next action
State whether next step is repository integration, rerun, metric cleanup, final figures, manuscript drafting, or next experiment.

End with a concise claim/evidence/caveat table suitable for repository import.

################################################################################
# Part B — Thread digest package
################################################################################

Create a downloadable zip archive for repository import.

Contract:
- Zip contains exactly one markdown digest file at the zip root.
- Name it with a stable lower_snake_case filename, e.g. `experiment14_analysis_digest.md`.
- Do not include generated repo updates in the zip.
- Do not include the Codex import prompt in the zip.
- Expected staging path: `docs/imports/<THREAD_DIGEST_FILENAME>.zip`
- Expected final path: `docs/threads/<THREAD_DIGEST_FILENAME>.md`

Digest structure:

# Thread Digest: Experiment <ID> <short title>

Digest filename: `<THREAD_DIGEST_FILENAME>.md`
Intended repository path: `docs/threads/<THREAD_DIGEST_FILENAME>.md`
Import package expected at: `docs/imports/<THREAD_DIGEST_FILENAME>.zip`

## 1. Thread scope
## 2. Experiment analyzed or designed
- Experiment ID:
- Experiment name:
- Experiment directory:
- Run profile:
- Run ID:
- Uploaded artifact bundle:
- Main local artifact paths, if known:
- Per-run database path, if applicable:
## 3. Experimental design discussed
## 4. Results analyzed
## 5. Key scientific conclusions supported by this thread
## 6. Important flaws, mistakes, or implementation concerns identified
## 7. Figures or artifacts referenced
## 8. Decisions made
## 9. Open questions
## 10. Relationship to first manuscript
## 11. Claims-and-evidence rows contributed by this thread
| Claim | Evidence | Caveat | Experiment(s) | Artifact(s) | Manuscript status |
|---|---|---|---|---|---|
## 12. Required repository updates
## 13. Recommended next action
## 14. Import package checklist
Confirm zip filename, digest filename, root placement, final path, that the zip contains only thread-derived analysis, that the Codex import prompt is separate, and any paths needing verification.

################################################################################
# Part C — Codex repository import prompt
################################################################################

In the final response, after linking the digest zip, provide a ready-to-paste Codex prompt specific to this experiment.

It must include:
- repository;
- import zip path;
- digest path;
- experiment directory;
- run ID(s);
- key artifact paths;
- required docs to update;
- `python scripts/verify_doc_source_paths.py`.

It must instruct Codex:
- do not modify experiment code;
- do not rerun experiments;
- do not delete artifacts or the import zip;
- do not invent conclusions;
- do not strengthen claims beyond digest and artifacts;
- every claim cites the thread digest and local artifact path when available;
- absent local artifact support is `local verification pending`;
- conflicts go to `docs/repo_audit/THREAD_IMPORT_CONFLICTS.md`;
- create `docs/repo_audit/EXP<ID>_ANALYSIS_IMPORT_REPORT.md`;
- do not commit or push.

Final answer:
1. Brief analysis outcome.
2. Link digest zip.
3. Expected staging path.
4. Full ready-to-paste Codex import prompt.
5. Paths needing verification.
```
