# CI Manuscript Reproducibility Foundation Run

Run ID: 2026-05-12_ci_foundation_a21ea4b

Purpose: fresh GitHub Actions foundation run covering artifact validation, manuscript asset rebuild attempt, smoke execution planning, source-path verification, and git-state capture.

Commands run:

```bash
python scripts/reproduce_manuscript.py --profile foundation
python scripts/verify_doc_source_paths.py
git status --short
git diff --stat
git diff -- docs/manuscript docs/repo_audit docs/source_data scripts
```

Interpretation:

- See `driver/MANUSCRIPT_REPRODUCIBILITY_REPORT.md` for profile-level results.
- See `source_path_verification/verify_doc_source_paths.log` for source-path verification.
- See `git_state/` for generated-file differences.
