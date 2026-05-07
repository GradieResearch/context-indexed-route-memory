# Path Verification Report

## Summary

Command used:

```bash
python scripts/verify_doc_source_paths.py
```

Final result after the non-Exp13.2 P0/P1 publication cleanup: 86 files scanned, 4,462 OK path observations, 0 missing active paths, 11 planned/future skips, and 41 local-verification-pending skips.

## Missing Active Paths

None.

## Skipped Planned/Future Paths

- `AGENTS.md`: `experiments/expNN_descriptive_name/` and `experiments/experimentNN_descriptive_name/` are planned/future naming examples, not active paths.
- `docs/repo_audit/P0_P1_PUBLICATION_CLEANUP_REPORT.md`: `docs/manuscript/BASELINE_RESULTS.md` is explicitly marked as a planned/future file not created in this pass.
- Historical QA reports preserve old planned/future examples.
- `docs/threads/experiment13_2_analysis_digest.md` preserves historical planned references to `docs/manuscript/BASELINE_RESULTS.md`.

## Skipped Local-Verification-Pending Paths

- `Pasted text.txt` remains missing/local verification pending wherever cited as the thread-referenced novelty assessment artifact.
- Future novelty import targets such as `docs/manuscript/NOVELTY_ASSESSMENT_IMPORTED.md` remain local verification pending.
- Historical review and thread-import docs preserve local-verification-pending shorthand paths.
- Exp13.1 and Exp13.2 thread digests preserve upload-bundle shorthand file names as historical source material.

## Current Scope Note

Exp13.2 is intentionally excluded from this cleanup pass. The verifier still scans existing historical Exp13.2 docs/source-data files when they are present, but active canonical docs now mark Exp13.2 claim/figure/source-data integration as deferred to a separate pass.

## Remaining Manual Review

- The novelty assessment artifact named `Pasted text.txt` is still not present locally.
- Seed-level uncertainty/effect-size tables remain to be generated and reviewed.
- Final figure scripts remain missing.
- Exp13.2 baseline alignment remains a separate pass.
