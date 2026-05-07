#!/usr/bin/env python
"""Compute generic seed-level mean/sd/se/95% CI summaries for metric CSVs.

This utility is intentionally mechanical. It does not know which grouping
columns are scientifically valid for a manuscript claim, so generated tables
require human review before citation.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import pandas as pd


def parse_csv_list(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def infer_metric_columns(frame: pd.DataFrame, excluded: set[str]) -> list[str]:
    numeric = frame.select_dtypes(include="number").columns
    return [column for column in numeric if column not in excluded]


def summarize(
    input_path: Path,
    output_path: Path,
    group_columns: list[str],
    metric_columns: list[str] | None,
    seed_column: str,
) -> None:
    frame = pd.read_csv(input_path)

    missing_groups = [column for column in group_columns if column not in frame.columns]
    if missing_groups:
        raise SystemExit(f"Missing group columns in input CSV: {missing_groups}")

    if seed_column not in frame.columns:
        raise SystemExit(f"Missing seed column in input CSV: {seed_column}")

    excluded = set(group_columns)
    excluded.add(seed_column)
    metrics = metric_columns or infer_metric_columns(frame, excluded)
    missing_metrics = [column for column in metrics if column not in frame.columns]
    if missing_metrics:
        raise SystemExit(f"Missing metric columns in input CSV: {missing_metrics}")
    if not metrics:
        raise SystemExit("No metric columns selected or inferred.")

    rows: list[dict[str, object]] = []
    for group_values, group in frame.groupby(group_columns, dropna=False, sort=True):
        if not isinstance(group_values, tuple):
            group_values = (group_values,)
        group_dict = dict(zip(group_columns, group_values))

        seed_level = group.groupby(seed_column, dropna=False, sort=True)[metrics].mean(numeric_only=True)
        for metric in metrics:
            values = seed_level[metric].dropna()
            n = int(values.shape[0])
            mean = float(values.mean()) if n else math.nan
            sd = float(values.std(ddof=1)) if n > 1 else 0.0 if n == 1 else math.nan
            se = float(sd / math.sqrt(n)) if n > 0 else math.nan
            ci95_half_width = float(1.96 * se) if n > 1 else 0.0 if n == 1 else math.nan
            rows.append(
                {
                    **group_dict,
                    "metric": metric,
                    "seed_count": n,
                    "mean": mean,
                    "sd": sd,
                    "se": se,
                    "ci95_low": mean - ci95_half_width if n else math.nan,
                    "ci95_high": mean + ci95_half_width if n else math.nan,
                    "review_status": "human_review_required_before_citation",
                }
            )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(output_path, index=False)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Compute generic seed-level mean/sd/se/95% CI summaries. "
            "Outputs require human review before manuscript citation."
        )
    )
    parser.add_argument("--input", required=True, type=Path, help="Input metric CSV path.")
    parser.add_argument("--output", required=True, type=Path, help="Output summary CSV path.")
    parser.add_argument(
        "--group-by",
        required=True,
        help="Comma-separated grouping columns, for example: phase,run_name,route_length.",
    )
    parser.add_argument(
        "--metrics",
        default="",
        help="Optional comma-separated metric columns. If omitted, numeric non-group/non-seed columns are used.",
    )
    parser.add_argument("--seed-column", default="seed", help="Seed column name. Default: seed.")
    args = parser.parse_args()

    summarize(
        input_path=args.input,
        output_path=args.output,
        group_columns=parse_csv_list(args.group_by),
        metric_columns=parse_csv_list(args.metrics) or None,
        seed_column=args.seed_column,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
