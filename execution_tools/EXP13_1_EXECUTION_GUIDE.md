# Experiment 13.1 Execution Guide

Use this guide when you are ready to run Experiment 13.1 locally. The implementation pass did not execute the experiment.

## Experiment Directory

```text
experiments/exp13_1_publication_hardening/
```

## Recommended First Validation Command

```powershell
powershell -ExecutionPolicy Bypass -File .\experiments\exp13_1_publication_hardening\start_exp13_1.ps1 -ValidationOnly
```

Then inspect:

```text
experiments/exp13_1_publication_hardening/analysis/exp13_1_validation/progress.jsonl
experiments/exp13_1_publication_hardening/analysis/exp13_1_validation/validation_report.md
experiments/exp13_1_publication_hardening/analysis/exp13_1_validation/exp13_1_report.md
```

## Standard Run

```powershell
powershell -ExecutionPolicy Bypass -File .\experiments\exp13_1_publication_hardening\start_exp13_1.ps1 -Profile standard
```

## Completion Checklist

- Confirm `validation_report.md` has no failures.
- Confirm `exp13_1_metrics.csv` and all summary CSVs exist.
- Confirm clean and corrupted context rows differ in at least one metric.
- Confirm `exp13_1_no_recurrence_at_eval` and `exp13_1_no_recurrence_throughout` are separate rows with separate recurrence metadata.
- Confirm lesion rows include `targeted_critical_edges`, `random_count_matched_edges`, and `random_weight_distribution_matched_edges`.
- Import the run summary into the experiment README after results exist.
- Use `Claim -> Evidence -> Caveat -> Source path` for every interpreted result.

## Do Not Overwrite Completed Runs

Validation-only and smoke runs write to:

```text
experiments/exp13_1_publication_hardening/analysis/exp13_1_validation/
```

Standard and full runs write to:

```text
experiments/exp13_1_publication_hardening/analysis/exp13_1/
```

If that directory contains a completed run, preserve it. Choose a new `--output-dir` through direct Python invocation or archive the completed run before starting another. Use `-Clean` only for an incomplete local run that you intentionally want to discard.
