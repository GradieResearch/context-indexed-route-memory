# Path Verification Report

## Summary

Command used:

```bash
python scripts/verify_doc_source_paths.py
```

Final result after this P0 cleanup: 58 files scanned, 4,266 OK path observations, 0 missing active paths, 8 planned/future skips, and 27 local-verification-pending skips. Paths that remain unresolved are explicitly marked as planned/future, stale examples, or local verification pending.

## Missing Active Paths

None.

## Skipped Planned/Future Paths

- `AGENTS.md`: `experiments/expNN_descriptive_name/` and `experiments/experimentNN_descriptive_name/` are planned/future naming examples, not active paths.
- `AGENTS.md`: `experiments/exp13_1_publication_hardening/` is an example future successor protocol directory, not an active path.
- `docs/manuscript/MANUSCRIPT_TODO.md`: `docs/experiments/exp13_1_summary.md` is planned for Exp13.1 and is not yet created.

## Skipped Local-Verification-Pending Paths

- `AGENTS.md`: do not cite stale paths such as `experiment12_capacity_generalization/analysis/`; this is a stale-path example used in a "do not cite" rule, not an active source path.
- `Pasted text.txt` remains missing/local verification pending wherever cited as the thread-referenced novelty assessment artifact.
- `docs/manuscript/NOVELTY_ASSESSMENT_IMPORTED.md` and `docs/repo_audit/source_imports/NOVELTY_ASSESSMENT.md` remain planned/local verification pending import targets for the missing novelty assessment.
- A few review-resolution files refer to shorthand filenames such as `BASELINE_REQUIREMENTS.md` or `CLAIMS_AND_EVIDENCE.md` only in local-verification-pending review text; the active canonical docs use full paths.

## Files Scanned

The verifier scanned 58 active documentation files: docs under `docs/` plus root-level `README.md`, `AGENTS.md`, `EXPERIMENT_TRACKER.md`, and `Experiment.md`. It intentionally skips generated historical thread transcripts named `docs/threads/experiment*_export.md`.

## Remaining Manual Review

- Historical thread exports may still preserve old paths as source conversation text.
- The novelty assessment artifact named `Pasted text.txt` is still not present locally.
- Exp13.1, external baselines, statistical hardening, and final figure scripts remain planned work rather than completed artifacts.
