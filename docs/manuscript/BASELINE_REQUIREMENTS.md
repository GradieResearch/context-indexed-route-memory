# Baseline Requirements

Purpose: Define the baseline and prior-art evidence required before the manuscript can claim submission readiness.

## Current status after Exp13.2, Exp14, Exp15, and Analysis Pass 15A

Claim: Exp13.2 partially satisfies the symbolic/algorithmic baseline requirement, and Exp15 partially satisfies the neural-comparator requirement, but baseline and prior-art coverage are still not complete enough to claim submission readiness.

Evidence: The completed Exp13.2 baseline-suite import reports a locally verified full run with `PASS: 28`, `WARN: 0`, `FAIL: 0`, 20 seeds, 15,040 metrics rows, 748 summary rows, 624 effect-size rows, and a local SQLite database. The imported suite includes shared no-context lookup, oracle context-gated lookup, endpoint memorization, recurrent non-plastic rules, superposition/hash-slot baselines, bounded LRU variants, replay variants, and parameter-isolation controls. The completed Exp15 import reports validation PASS for 10 seeds, 9 neural variants, 5,400 seed metric rows, 540 summary rows, and 1,080 runtime rows. Analysis Pass 15A retains C12 as a discussion/table baseline claim rather than a broad submission-readiness claim.

Caveat: Exp15 is a minimal fixed-profile comparator, not exhaustive neural benchmarking. It uses fixed small model sizes/hyperparameters, omits memory-augmented/key-value neural baselines, and includes a reconstructed-manifest/empty-SQLite-`run_manifest` provenance caveat. The missing novelty/prior-art source artifact is still not present locally, and the manuscript still needs venue-appropriate prior-art positioning and a decision about whether broader neural baselines are required.

Source path: `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`; `docs/experiments/exp13_2_summary.md`; `docs/threads/experiment13_2_analysis_digest.md`; `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`; `docs/threads/experiment15_analysis_digest.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/validation_report.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`; `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`.

## Required Baseline Families

| ID | Baseline family | Purpose | Minimum contract | Metrics | Current status |
|---|---|---|---|---|---|
| B1 | Shared transition table | Test whether a global table without context separation is sufficient. | Same train/eval route protocol, no per-world index. | Composition accuracy, route-table accuracy, retention, conflict-sensitive first-step accuracy. | Present in Exp13.2 symbolic/algorithmic baseline suite. |
| B2 | Context-gated transition table / task mask | Test whether supplied context labels plus per-world lookup explain clean performance. | Oracle world/context label selects a per-world table. | Composition accuracy, route-table accuracy, first-step context accuracy, capacity usage. | Present in Exp13.2; matches CIRM on clean supplied-context benchmark and remains an oracle upper bound in Exp14. |
| B3 | Recurrent non-plastic executor | Test whether recurrence alone explains composition. | Recurrent execution without structural route-memory updates. | Route-table accuracy, multi-step composition, route-length sensitivity. | Present in Exp13.2. |
| B4 | Replay or finite-memory learner | Test whether conventional finite memory/replay can preserve routes. | Documented memory budget and replay/refresh policy. | Composition, retention, evictions/capacity use. | Present symbolically/algorithmically in Exp13.2. Present as a neural Exp15 variant, but the replay result requires implementation/training-regime audit before scientific interpretation. |
| B5 | Parameter isolation / mask-based baseline | Test whether isolated task capacity explains retention. | World-specific partitions or masks with explicit capacity accounting. | Composition, retention, capacity pressure curves. | Present in Exp13.2. |
| B6 | Context-conditioned compact storage | Test whether compact context-conditioned storage matches route memory. | Context-conditioned lookup or hypernetwork/superposition-style storage. | Composition, route-table accuracy, collision/capacity diagnostics. | Present in Exp13.2 as hash/superposition-style symbolic controls. |
| B7 | Prior-art novelty import | Establish what is and is not novel relative to existing work. | Local source artifact with citations or imported novelty assessment. | Not a metric table; supports claim framing and related work. | Missing/local verification pending. |
| B8 | Neural baselines | Determine whether claims can be submitted to a stronger ML venue. | At minimum: recurrent neural baseline with context/task embedding, transformer/sequence baseline with context tokens, replay-based continual-learning baseline, parameter-isolation/mask neural baseline, and/or memory-augmented lookup baseline. | Same route-table, seen-route, suffix-route, first-step context, retention, and capacity metrics. | Minimal fixed-profile comparator present in Exp15; memory-augmented/key-value neural baseline remains omitted and broader neural benchmarking remains venue-dependent. |

## Acceptance Criteria

- Baseline claims must cite generated artifacts under `experiments/...`, not only thread text.
- Numeric claims must use generated CSVs or validation reports.
- Internal ablations must not be described as external baselines.
- Exp13.2 may now be cited as symbolic/algorithmic baseline evidence, but not as neural-baseline evidence.
- Exp15 may now be cited as minimal neural-comparator evidence, but not as exhaustive neural benchmarking.
- Prior-art and novelty claims require local source artifacts or proper citations before submission.
- The oracle context-gated table must be described as a clean supplied-context upper bound, not as a defeated competitor.
- The context-conditioned transition MLP result means the manuscript must avoid broad CIRM superiority over neural models.

## Current Manuscript Consequence

Claim: Baseline work is partially complete but remains a submission-readiness blocker.

Evidence: Exp13.2 supplies a completed symbolic/algorithmic baseline suite, Exp14 clarifies the oracle-context limitation by testing symbolic transition-cue context selection, Exp15 supplies a completed minimal neural comparator, and Analysis Pass 15A records C12 as a discussion/table claim rather than a broad readiness claim.

Caveat: Prior-art/novelty import and broader neural-baseline decisions remain open. The first manuscript may proceed as a controlled symbolic/mechanistic benchmark if it explicitly states these limits; a stronger ML-venue submission may require memory-augmented or broader neural baselines.

Source path: `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`; `docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md`; `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`; `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`; `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`.
