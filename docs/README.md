# Documentation Index

Purpose: Make the `docs/` tree navigable for humans and future local agents.

## Start here

Recommended reading order:

1. `../README.md`
2. `docs/manuscript/SOURCE_OF_TRUTH.md`
3. `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`
4. `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`
5. `docs/manuscript/draft/MANUSCRIPT_V2.md`
6. `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
7. `docs/manuscript/finalization/README.md`
8. `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`
9. `docs/manuscript/finalization/NEXT_STEP_PROMPT.md`
10. `docs/synthesis/PUBLICATION_READINESS.md`
11. `docs/manuscript/LIMITATIONS_AND_THREATS.md`
12. `docs/experiments/EXPERIMENT_REGISTRY.md`
13. `docs/manuscript/FIGURE_PLAN.md`
14. `docs/synthesis/NEXT_EXPERIMENTS.md`

## Manuscript docs

| Document | Purpose | Status | When to edit |
|---|---|---|---|
| `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md` | Frozen first-manuscript claim boundary and handoff into figure/table generation. | Active phase-control doc | Edit only when the first-manuscript inclusion/exclusion decision changes with local evidence. |
| `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md` | Post-Exp15 narrowing of the first-manuscript claim posture. | Active; stricter than earlier claim-freeze language where conflicts exist | Edit when Exp15 interpretation, neural-baseline posture, or post-Exp15 claim wording changes. |
| `docs/manuscript/draft/MANUSCRIPT_V2.md` | Captured post-Exp15 manuscript draft. | Active V2 draft; not submission-ready | Edit when manuscript prose changes after retained-claim/statistical hardening, citation verification, or figure/table decisions. |
| `docs/manuscript/finalization/README.md` | Index for manuscript finalization planning, checklist, and handoff prompt. | Active finalization entrypoint | Edit when the current finalization phase or handoff prompt changes. |
| `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md` | Operational checklist for the finalization phase. | Active tracker | Edit when checklist items are completed, deferred, or re-scoped. |
| `docs/manuscript/finalization/NEXT_STEP_PROMPT.md` | Agent-ready prompt for the next finalization action. | Active handoff prompt | Edit whenever the recommended next action changes. |
| `docs/manuscript/CLAIMS_AND_EVIDENCE.md` | Canonical claim map using Claim -> Evidence -> Caveat -> Source path. | Active source of truth | Edit whenever claim wording, status, evidence, caveat, or source paths change. |
| `docs/manuscript/MANUSCRIPT_SPINE.md` | Provisional manuscript architecture and section plan. | Active draft scaffold; needs refresh from the V2/finalization state | Edit when the manuscript structure changes after claim freeze, baseline decisions, or figure decisions. |
| `docs/manuscript/MANUSCRIPT_TODO.md` | Conservative work queue for manuscript readiness. | Active work queue | Edit when work status changes or a blocker is completed with local evidence. |
| `docs/manuscript/FIGURE_PLAN.md` | Candidate main and supplementary figure map. | Active planning doc | Edit whenever a figure, panel, source artifact, or caveat changes. |
| `docs/manuscript/LIMITATIONS_AND_THREATS.md` | Reviewer-risk and non-claim tracker. | Active caveat doc | Edit when a limitation is resolved or a new risk appears. |
| `docs/manuscript/BASELINE_REQUIREMENTS.md` | Baseline suite contracts and acceptance criteria. | Active; Exp13.2 symbolic/algorithmic baselines and Exp15 minimal neural comparator imported | Edit when baseline interpretation, neural-baseline posture, or prior-art requirements change. |
| `docs/manuscript/SOURCE_OF_TRUTH.md` | Rules for resolving conflicts between docs, artifacts, and thread exports. | Active handoff note | Edit only when canonical-document ownership changes. |

## Experiment docs

| Document | Purpose | Status |
|---|---|---|
| `docs/experiments/EXPERIMENT_REGISTRY.md` | Conservative index of experiment directories, thread digests, artifacts, roles, and follow-up needs. | Active registry |
| `docs/experiments/HISTORICAL_EXPERIMENTS.md` | Separates manuscript-critical, supporting, and historical experiments. | Active navigation aid |
| `docs/experiments/exp*_summary.md` | Per-experiment summaries imported from local artifacts and thread digests. | Active summaries with human/manuscript validation pending |
| `docs/experiments/exp13_local_vs_global_budget_comparison.md` | Docs-only aggregate comparison for Exp13 local-vs-global pressure. | Preliminary; paired seed-level analysis pending |
| `EXPERIMENT_ARTIFACTS_INDEX.csv` | Index of detected experiment artifacts. | Review aid |
| `EXPERIMENT_CLAIMS_MATRIX.csv` | Experiment-to-claim mapping aid. | Review aid |

## Repo audit docs

| Document | Purpose | Status |
|---|---|---|
| `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md` | Documents Exp13.2 symbolic/algorithmic baseline-suite import. | Completed import record |
| `docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md` | Documents Exp14 symbolic transition-cue context-selection import. | Completed import record |
| `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md` | Documents Exp15 minimal neural-comparator import and caveats. | Completed import record |
| `docs/repo_audit/P0_REMEDIATION_REPORT.md` | Documents P0 fixes for paths, docs CSV reviewability, and path verification. | Completed repo-readiness record |
| `docs/repo_audit/P0_REMEDIATION_QA.md` | QA result for P0 remediation. | Completed QA record |
| `docs/repo_audit/P1_REMEDIATION_REPORT.md` | Documents P1 onboarding, reproducibility, baseline planning, and manuscript-spine cleanup. | Completed repo-readiness record |
| `docs/repo_audit/P1_REMEDIATION_QA.md` | QA result for P1 remediation. | Completed QA record |
| `docs/repo_audit/P2_REMEDIATION_REPORT.md` | Documents P2 polish pass. | Completed/legacy record |
| `docs/repo_audit/REPRODUCIBILITY_AUDIT.md` | Run-interface and reproducibility map. | Active audit; commands inspected, not freshly rerun here |
| `docs/repo_audit/PATH_VERIFICATION_REPORT.md` | Records path-verifier expectations and prior results. | Active audit support |
| `docs/repo_audit/MISSING_ARTIFACTS.md` | Tracks missing or local-verification-pending artifacts. | Active caveat tracker |
| `docs/repo_audit/P0_P1_PUBLICATION_CLEANUP_REPORT.md` | Earlier non-Exp13.2 publication-cleanup handoff report. | Legacy handoff record; superseded by post-Exp13.2/Exp14/Exp15/V2 finalization docs for active manuscript planning |

## Theory docs

| Document | Purpose | Status |
|---|---|---|
| `docs/theory/GLOSSARY.md` | Project-specific terminology definitions. | Active terminology guide |
| `docs/theory/CORE_THEORY.md` | Early core-theory scaffold. | Framing only |
| `docs/theory/BIOLOGICAL_FRAMING.md` | Biological-inspiration caveats. | Framing only |
| `docs/theory/PRIOR_ART_MAP.md` | Prior-art map scaffold. | Planned; citation import pending |

## Thread imports

Thread exports under `docs/threads/` are source material. They may preserve historical wording, old paths, or exploratory interpretations from earlier conversations.

Active first-manuscript claim inclusion decisions live in `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`. Post-Exp15 claim narrowing lives in `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`. Active claim wording lives in `docs/manuscript/CLAIMS_AND_EVIDENCE.md`. Use thread exports as historical context unless their interpretation has been imported into current evidence docs with a local source path and caveat.

## Rule for future edits

- Update `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md` when Exp15 materially narrows a claim.
- Update `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md` when first-manuscript inclusion status changes.
- Update `docs/manuscript/CLAIMS_AND_EVIDENCE.md` when a claim changes.
- Update `docs/manuscript/FIGURE_PLAN.md` when a figure changes.
- Update `docs/manuscript/MANUSCRIPT_TODO.md` when work status changes.
- Update `docs/manuscript/finalization/NEXT_STEP_PROMPT.md` when the next operational handoff changes.
- Keep source-data and statistical-readiness manifests synchronized with retained figures/claims.
- Run `python scripts/verify_doc_source_paths.py` after source-path-heavy edits.
