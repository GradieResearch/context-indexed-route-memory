# Baseline Requirements

Purpose: Define the baseline and prior-art evidence required before the manuscript can claim submission readiness.

Scope note for the current P0/P1 cleanup: Exp13.2 is intentionally excluded. The repository may contain Exp13.2 artifacts or historical import notes, but this document treats baseline integration as deferred to a separate Exp13.2 analysis/import/alignment pass and makes no Exp13.2 result claims.

Claim: External baseline and prior-art comparison are required before submission-readiness can be claimed.
Evidence: Current central claims rely on internal ablations across Exp11, Exp12, Exp13, and Exp13.1; thread-derived novelty notes warn that context gating, task masks, recurrence, and continual learning are not novel individually.
Caveat: The novelty assessment source artifact named `Pasted text.txt` is not present locally; local verification pending. Exp13.2 must be handled separately before any baseline result claims are imported into C12.
Source path: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/threads/experiment12to13_export.md`; `docs/threads/experiment11_export`; local verification pending for `Pasted text.txt`

## Required Baseline Families

| ID | Baseline family | Purpose | Minimum contract | Metrics | Status in this cleanup pass |
|---|---|---|---|---|---|
| B1 | Shared transition table | Test whether a global table without context separation is sufficient. | Same train/eval route protocol, no per-world index. | Composition accuracy, route-table accuracy, retention, conflict-sensitive first-step accuracy. | Deferred to separate Exp13.2 pass. |
| B2 | Context-gated transition table / task mask | Test whether supplied context labels plus per-world lookup explain clean performance. | Oracle world/context label selects a per-world table. | Composition accuracy, route-table accuracy, first-step context accuracy, capacity usage. | Deferred to separate Exp13.2 pass. |
| B3 | Recurrent non-plastic executor | Test whether recurrence alone explains composition. | Recurrent execution without structural route-memory updates. | Route-table accuracy, multi-step composition, route-length sensitivity. | Deferred to separate Exp13.2 pass. |
| B4 | Replay or finite-memory learner | Test whether conventional finite memory/replay can preserve routes. | Documented memory budget and replay/refresh policy. | Composition, retention, evictions/capacity use. | Deferred to separate Exp13.2 pass. |
| B5 | Parameter isolation / mask-based baseline | Test whether isolated task capacity explains retention. | World-specific partitions or masks with explicit capacity accounting. | Composition, retention, capacity pressure curves. | Deferred to separate Exp13.2 pass. |
| B6 | Context-conditioned compact storage | Test whether compact context-conditioned storage matches route memory. | Context-conditioned lookup or hypernetwork/superposition-style storage. | Composition, route-table accuracy, collision/capacity diagnostics. | Deferred to separate Exp13.2 pass. |
| B7 | Prior-art novelty import | Establish what is and is not novel relative to existing work. | Local source artifact with citations or imported novelty assessment. | Not a metric table; supports claim framing and related work. | Missing/local verification pending. |

## Acceptance Criteria

- Baseline claims must cite generated artifacts under `experiments/...`, not only thread text.
- Numeric claims must use generated CSVs or validation reports.
- Internal ablations must not be described as external baselines.
- Any Exp13.2 result integration must happen in a separate pass and update `docs/manuscript/CLAIMS_AND_EVIDENCE.md`, `docs/manuscript/LIMITATIONS_AND_THREATS.md`, `docs/manuscript/FIGURE_PLAN.md`, and source-data manifests together.
- If neural baselines remain absent after Exp13.2 import, the manuscript must say so explicitly.

## Current Manuscript Consequence

Claim: Baseline work remains a P0 blocker in this cleanup pass.
Evidence: `docs/manuscript/CLAIMS_AND_EVIDENCE.md` keeps C12 at `Needs baseline`, and `docs/manuscript/MANUSCRIPT_TODO.md` defers Exp13.2 to a separate import/alignment pass.
Caveat: This is a scope decision for this pass, not a statement about the validity of any unreviewed Exp13.2 artifacts.
Source path: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/manuscript/MANUSCRIPT_TODO.md`
