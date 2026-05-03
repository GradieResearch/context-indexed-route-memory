from __future__ import annotations

import argparse
import json
import os
import sqlite3
import time
from dataclasses import asdict
from pathlib import Path
import random
from typing import Iterable, List

import pandas as pd

from exp7.core import (
    ContextualRouteFieldGraph,
    Task,
    VariantConfig,
    evaluate_baselines,
    evaluate_transition_table_oracle,
    generate_bounded_tasks,
    generate_transition_tasks,
    make_variants,
    shuffled_repeated,
    summarize_traces,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Experiment 7 route-field diagnostic suite.")
    parser.add_argument("--output-dir", default="analysis/exp7", help="Directory for CSV/report outputs.")
    parser.add_argument("--db", default="runs/exp7_route_field_diagnostics.sqlite3", help="SQLite output path.")
    parser.add_argument("--max-number", type=int, default=11, help="Highest symbolic number in the bounded world.")
    parser.add_argument("--max-steps", type=int, default=3, help="Maximum composition length to evaluate.")
    parser.add_argument("--train-repeats", type=int, default=40, help="Repeats over one-step transition curriculum.")
    parser.add_argument("--path-train-repeats", type=int, default=2, help="Repeats over multi-step task paths for optional consolidation.")
    parser.add_argument("--seeds", type=int, default=5, help="Number of seeds to run, starting at --seed-offset.")
    parser.add_argument("--seed-offset", type=int, default=0, help="First seed index.")
    parser.add_argument("--variants", nargs="*", default=None, help="Optional list of variant names to run.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing SQLite DB and output directory CSVs.")
    return parser.parse_args()


def reset_outputs(db_path: Path, output_dir: Path, force: bool) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if force and db_path.exists():
        db_path.unlink()


def init_db(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS runs (
            run_id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_name TEXT NOT NULL,
            seed INTEGER NOT NULL,
            status TEXT NOT NULL,
            started_at REAL NOT NULL,
            completed_at REAL,
            config_json TEXT NOT NULL,
            max_number INTEGER NOT NULL,
            max_steps INTEGER NOT NULL,
            train_repeats INTEGER NOT NULL,
            path_train_repeats INTEGER NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS metrics (
            run_id INTEGER NOT NULL,
            metric TEXT NOT NULL,
            value REAL NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS predictions (
            run_id INTEGER NOT NULL,
            run_name TEXT NOT NULL,
            seed INTEGER NOT NULL,
            split TEXT NOT NULL,
            mode TEXT NOT NULL,
            start INTEGER NOT NULL,
            steps INTEGER NOT NULL,
            target INTEGER NOT NULL,
            predicted INTEGER NOT NULL,
            correct INTEGER NOT NULL,
            mean_step_target_rank REAL,
            max_step_target_rank REAL,
            mean_correct_margin REAL,
            min_correct_margin REAL,
            mean_context_margin REAL,
            min_context_margin REAL,
            mean_wrong_route_activation REAL,
            path TEXT
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS route_diagnostics (
            run_id INTEGER NOT NULL,
            run_name TEXT NOT NULL,
            seed INTEGER NOT NULL,
            mode TEXT NOT NULL,
            source INTEGER NOT NULL,
            true_target INTEGER NOT NULL,
            predicted_target INTEGER NOT NULL,
            correct INTEGER NOT NULL,
            target_rank INTEGER NOT NULL,
            correct_margin REAL NOT NULL,
            context_margin REAL,
            wrong_route_activation REAL,
            target_score REAL NOT NULL,
            best_score REAL NOT NULL,
            top_targets TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS baselines (
            seed INTEGER NOT NULL,
            split TEXT NOT NULL,
            baseline TEXT NOT NULL,
            accuracy REAL NOT NULL,
            n INTEGER NOT NULL
        )
        """
    )
    conn.commit()


def insert_run(conn: sqlite3.Connection, variant: VariantConfig, seed: int, args: argparse.Namespace) -> int:
    cur = conn.execute(
        """
        INSERT INTO runs(run_name, seed, status, started_at, config_json, max_number, max_steps, train_repeats, path_train_repeats)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            variant.name,
            seed,
            "running",
            time.time(),
            json.dumps(asdict(variant), sort_keys=True),
            args.max_number,
            args.max_steps,
            args.train_repeats,
            args.path_train_repeats,
        ),
    )
    conn.commit()
    return int(cur.lastrowid)


def finish_run(conn: sqlite3.Connection, run_id: int) -> None:
    conn.execute("UPDATE runs SET status = ?, completed_at = ? WHERE run_id = ?", ("completed", time.time(), run_id))
    conn.commit()


def insert_metrics(conn: sqlite3.Connection, run_id: int, metrics: dict) -> None:
    conn.executemany(
        "INSERT INTO metrics(run_id, metric, value) VALUES (?, ?, ?)",
        [(run_id, key, float(value)) for key, value in metrics.items() if value == value],
    )


def insert_prediction_rows(conn: sqlite3.Connection, run_id: int, rows: List[dict]) -> None:
    if not rows:
        return
    for row in rows:
        row["run_id"] = run_id
    cols = [
        "run_id", "run_name", "seed", "split", "mode", "start", "steps", "target", "predicted", "correct",
        "mean_step_target_rank", "max_step_target_rank", "mean_correct_margin", "min_correct_margin",
        "mean_context_margin", "min_context_margin", "mean_wrong_route_activation", "path",
    ]
    placeholders = ",".join(["?"] * len(cols))
    conn.executemany(
        f"INSERT INTO predictions({','.join(cols)}) VALUES ({placeholders})",
        [[row.get(c) for c in cols] for row in rows],
    )


def insert_route_rows(conn: sqlite3.Connection, run_id: int, run_name: str, seed: int, rows: List[dict]) -> None:
    if not rows:
        return
    for row in rows:
        row["run_id"] = run_id
        row["run_name"] = run_name
        row["seed"] = seed
    cols = [
        "run_id", "run_name", "seed", "mode", "source", "true_target", "predicted_target", "correct",
        "target_rank", "correct_margin", "context_margin", "wrong_route_activation", "target_score", "best_score", "top_targets",
    ]
    placeholders = ",".join(["?"] * len(cols))
    conn.executemany(
        f"INSERT INTO route_diagnostics({','.join(cols)}) VALUES ({placeholders})",
        [[row.get(c) for c in cols] for row in rows],
    )


def insert_baselines(conn: sqlite3.Connection, seed: int, split: str, rows: List[dict]) -> None:
    for row in rows:
        row["seed"] = seed
        row["split"] = split
    conn.executemany(
        "INSERT INTO baselines(seed, split, baseline, accuracy, n) VALUES (?, ?, ?, ?, ?)",
        [(r["seed"], r["split"], r["baseline"], float(r["accuracy"]), int(r["n"])) for r in rows],
    )


def run_variant(conn: sqlite3.Connection, variant: VariantConfig, seed: int, args: argparse.Namespace) -> None:
    run_id = insert_run(conn, variant, seed, args)
    graph = ContextualRouteFieldGraph(max_number=args.max_number, config=variant, seed=seed)
    rng = random.Random(seed)

    transition_tasks = generate_transition_tasks(args.max_number)
    composition_tasks = generate_bounded_tasks(args.max_number, args.max_steps, min_steps=2)
    all_tasks = transition_tasks + composition_tasks

    # Main local curriculum: repeated one-step transitions. If the route field has
    # learned the local transition table correctly, it should compose without being
    # directly trained on each final answer.
    for task in shuffled_repeated(transition_tasks, args.train_repeats, rng):
        graph.train_task_path(task)

    # Optional light consolidation over paths. This still performs local stepwise
    # updates, not final answer memorization.
    for task in shuffled_repeated(composition_tasks, args.path_train_repeats, rng):
        graph.train_task_path(task)

    transition_traces = [graph.predict(task) for task in transition_tasks]
    composition_traces = [graph.predict(task) for task in composition_tasks]
    all_traces = transition_traces + composition_traces

    prediction_rows = []
    for split, traces in [("transition", transition_traces), ("composition", composition_traces), ("all", all_traces)]:
        for trace in traces:
            prediction_rows.append(trace.to_metric_row(variant.name, seed, split))

    metrics = {}
    metrics.update(summarize_traces(transition_traces, prefix="transition/"))
    metrics.update(summarize_traces(composition_traces, prefix="composition/"))
    metrics.update(summarize_traces(all_traces, prefix="all/"))

    for mode in sorted({t.mode for t in composition_tasks}):
        traces = [tr for tr in composition_traces if tr.task.mode == mode]
        metrics[f"composition/accuracy_mode_{mode}"] = sum(t.correct for t in traces) / len(traces) if traces else float("nan")
    for steps in sorted({t.steps for t in composition_tasks}):
        traces = [tr for tr in composition_traces if tr.task.steps == steps]
        metrics[f"composition/accuracy_steps_{steps}"] = sum(t.correct for t in traces) / len(traces) if traces else float("nan")

    route_rows = graph.route_diagnostics()
    insert_metrics(conn, run_id, metrics)
    insert_prediction_rows(conn, run_id, prediction_rows)
    insert_route_rows(conn, run_id, variant.name, seed, route_rows)
    finish_run(conn, run_id)


def export_tables(conn: sqlite3.Connection, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for table in ["runs", "metrics", "predictions", "route_diagnostics", "baselines"]:
        df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
        df.to_csv(output_dir / f"{table}.csv", index=False)


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    db_path = Path(args.db)
    reset_outputs(db_path, output_dir, args.force)
    conn = sqlite3.connect(db_path)
    init_db(conn)

    variants = make_variants()
    if args.variants:
        requested = set(args.variants)
        variants = [v for v in variants if v.name in requested]
        missing = requested - {v.name for v in variants}
        if missing:
            raise SystemExit(f"Unknown variant(s): {', '.join(sorted(missing))}")

    # Baselines are deterministic or seed-controlled and evaluated on the same
    # bounded transition/composition tasks as the graph variants.
    for seed in range(args.seed_offset, args.seed_offset + args.seeds):
        transition_tasks = generate_transition_tasks(args.max_number)
        composition_tasks = generate_bounded_tasks(args.max_number, args.max_steps, min_steps=2)
        insert_baselines(conn, seed, "transition", evaluate_baselines(transition_tasks, args.max_number, seed) + [evaluate_transition_table_oracle(transition_tasks, args.max_number)])
        insert_baselines(conn, seed, "composition", evaluate_baselines(composition_tasks, args.max_number, seed) + [evaluate_transition_table_oracle(composition_tasks, args.max_number)])
        conn.commit()

    for seed in range(args.seed_offset, args.seed_offset + args.seeds):
        for variant in variants:
            print(f"Running {variant.name} seed={seed}")
            run_variant(conn, variant, seed, args)
            conn.commit()

    export_tables(conn, output_dir)
    conn.close()
    print(f"Wrote DB: {db_path}")
    print(f"Wrote CSVs: {output_dir}")


if __name__ == "__main__":
    main()
