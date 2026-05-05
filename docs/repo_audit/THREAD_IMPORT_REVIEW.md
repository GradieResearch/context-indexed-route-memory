## Finding 1

Severity: P1
File: `docs/manuscript/CLAIMS_AND_EVIDENCE.md:20`; `experiments/experiment13_breaking_point/analysis/validation_report.md`
Problem: C1 says "Exp13 validation also marks no-structural-plasticity as a failure mode under boundary mapping" and cites `experiments/experiment13_breaking_point/analysis/validation_report.md`, but the validation report has PASS entries for no-recurrence, no-world-context, context corruption, holdout, continuous front end, and consolidation. It does not mention no-structural-plasticity.
Why it matters: The local artifact path exists, but it does not verify the exact scientific claim. This makes the C1 evidence row look stronger and cleaner than the actual local provenance.
Recommended fix: Either remove the Exp13 validation sentence/path from C1, or cite the actual Exp13 data table that contains the no-structural-plasticity rows, such as `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`, and update the evidence wording accordingly.

## Finding 2

Severity: P1
File: `docs/manuscript/CLAIMS_AND_EVIDENCE.md:31`; `docs/manuscript/BASELINE_REQUIREMENTS.md:7`
Problem: C12 relies on a novelty assessment artifact named `Pasted text.txt`, but that file is explicitly not present locally. The row says "local artifact support pending" rather than the required explicit "local verification pending" label, and the cited local `BASELINE_REQUIREMENTS.md` file is still a TODO scaffold with `Source path: TODO` entries.
Why it matters: This violates the evidence-map rule that every claim needs either a local artifact path or an explicit local-verification-pending label. It also lets a manuscript-readiness claim appear locally supported when its main novelty evidence is thread-derived.
Recommended fix: Add the novelty assessment as a local artifact, or change C12's artifact/status wording to explicitly say `local verification pending`. Fill `BASELINE_REQUIREMENTS.md` with source-backed baseline families and source paths, or stop using it as evidence for C12 until it is populated.

## Finding 3

Severity: P1
File: `docs/manuscript/CLAIMS_AND_EVIDENCE.md:29`; `docs/repo_audit/THREAD_IMPORT_CONFLICTS.md:39`; `docs/manuscript/FIGURE_PLAN.md:37`
Problem: C10 lists Exp11, Exp12, and Exp13 as support for "context corruption creates failure," but the thread/conflict docs say Exp12 context-bleed/dropout was too flat or inconclusive and should be treated as diagnostic only. Exp11/Exp12 margin or wrong-world-activation plots do not establish the failure threshold claimed in C10; the completed failure evidence is Exp13 adversarial corruption.
Why it matters: This blends diagnostic/noise-margin artifacts with completed failure evidence and risks turning an inconclusive planned-hardening area into a result claim.
Recommended fix: Make C10's supporting experiments/evidence center on Exp13 only for the failure claim. Mention Exp11/Exp12 as margin diagnostics in the caveat or supplementary notes, and keep the stochastic corruption rerun as required follow-up.

## Finding 4

Severity: P2
File: `docs/manuscript/CLAIMS_AND_EVIDENCE.md:25`; `docs/manuscript/FIGURE_PLAN.md:48`; `docs/threads/experiment12to13_export.md:1222`
Problem: C6 says finite structural budget exposes "predictable breaking curves," but the same row admits capacity-law fitting has not been performed. The figure plan and thread follow-up both say capacity-law summaries/fitting are still required.
Why it matters: "Predictable" reads like a completed fitted law, while the available evidence is an observed curve from generated summaries and plots.
Recommended fix: Reword C6 to "observed finite-budget breaking curve" or similar, and reserve "predictable" or "failure law" language until Exp13.1 adds capacity-law fitting and confidence intervals.

## Finding 5

Severity: P2
File: `docs/manuscript/CLAIMS_AND_EVIDENCE.md:26`; `docs/repo_audit/THREAD_IMPORT_CONFLICTS.md:82`
Problem: C7 states local structural budget pressure is more damaging than global budget pressure, but the conflict log says the local-vs-global claim lacks a dedicated formal comparison artifact. The cited artifacts are separate local and global summary CSVs, not a paired comparison table.
Why it matters: The direction of the effect is plausible, but the evidence map currently asks readers to infer the comparison manually from two artifacts.
Recommended fix: Downgrade the wording to "appears more damaging" or keep it explicitly preliminary until a paired local-vs-global comparison table or docs-only analysis artifact exists.

## Finding 6

Severity: P2
File: `docs/experiments/exp11_summary.md:6`; `docs/experiments/exp11_summary.md:103`; `docs/experiments/exp12_summary.md:6`; `docs/experiments/exp12_summary.md:106`; `docs/experiments/exp13_summary.md:6`; `docs/experiments/exp13_summary.md:107`
Problem: The experiment summaries say the relevant thread digests were reviewed/imported near the top, but their stale "Known implementation or interpretation caveats" sections still say "Thread digest has not been reviewed." They also retain "Claims validated: local-only first pass" while later thread-integrated sections assign manuscript statuses such as Strong, Promising, or Preliminary.
Why it matters: This is an internal mismatch between thread digests and experiment summaries. A reviewer or future maintainer cannot tell whether the summaries are scaffold-only, thread-integrated, or locally validated.
Recommended fix: Update the summary metadata and stale caveat blocks so they distinguish "thread imported," "local artifact checked," and "human/manuscript validation pending" without contradicting the thread-integrated result sections.

## Finding 7

Severity: P2
File: `docs/experiments/EXPERIMENT_CLAIMS_MATRIX.csv:2`
Problem: The experiment claims matrix is still entirely TODO rows for Exp1-Exp13, while `CLAIMS_AND_EVIDENCE.md` contains C1-C12 with specific statuses and artifact paths.
Why it matters: This leaves the experiment-level claim crosswalk unusable for verifying whether manuscript claims match experiment summaries. It also conflicts with the impression that the thread import produced a complete evidence map.
Recommended fix: Populate the matrix with claim IDs, evidence paths, caveats, and support levels for at least Exp7-Exp13, or clearly label the file as a non-authoritative scaffold and point reviewers to `CLAIMS_AND_EVIDENCE.md`.

## Finding 8

Severity: P2
File: `docs/manuscript/FIGURE_PLAN.md:97`; `docs/manuscript/FIGURE_PLAN.md:123`; `docs/manuscript/FIGURE_PLAN.md:130`; `docs/manuscript/FIGURE_PLAN.md:137`; `docs/manuscript/FIGURE_PLAN.md:144`
Problem: The retained pre-import figure inventory still contains `Claim supported` entries using stale claim IDs. For example, the pre-import breaking-point figure says "C4; C5 only after metric cleanup," but the current claim table maps breaking-point claims to C6/C7.
Why it matters: Even with the disclaimer that the section is not claim-bearing, stale claim IDs can cause exactly the kind of figure-to-claim mismatch this audit is meant to prevent.
Recommended fix: Remove current-looking claim IDs from the pre-import inventory, mark them as legacy IDs, or update the section to the current C1-C12 mapping.

## Finding 9

Severity: P2
File: `docs/manuscript/CLAIMS_AND_EVIDENCE.md:23`
Problem: C4 cites an Exp12 plot for the numeric statement that route-table accuracy is 1.0 while composition is about 0.05-0.06, but it does not cite the machine-readable Exp12 summary CSV that contains those values. Its required follow-up is only a figure panel, while adjacent recurrence claims include external baseline follow-up.
Why it matters: The claim has a local artifact path, but the strongest local evidence for the numbers is a data table, not a plot. The follow-up column also understates the baseline/statistical hardening needed for a strong internal-ablation claim.
Recommended fix: Add `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv` or `experiments/experiment12_capacity_generalization/analysis/exp12/exp12_final_memory_index.csv` to C4's artifacts, and add baseline/effect-size follow-up consistent with C3 and the limitations docs.
