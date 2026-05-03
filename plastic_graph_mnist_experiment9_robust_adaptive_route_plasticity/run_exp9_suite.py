from __future__ import annotations

import argparse
import json
import shutil
import sqlite3
import time
from dataclasses import asdict
from pathlib import Path
from typing import Iterable, List, Set

from exp9.core import (
    GraphConfig,
    RobustRouteGraph,
    VariantConfig,
    evaluate_baselines,
    generate_bounded_tasks,
    generate_transition_tasks,
    make_feedback_variants,
    make_interference_variants,
    route_summary,
    summarize_by_mode_and_steps,
    summarize_traces,
)


def parse_float_list(value: str) -> List[float]:
    return [float(x.strip()) for x in value.replace(",", " ").split() if x.strip()]


def parse_int_list(value: str) -> List[int]:
    return [int(x.strip()) for x in value.replace(",", " ").split() if x.strip()]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run Experiment 9 robust adaptive route plasticity suite.")
    p.add_argument("--db", default="runs/exp9_robust_adaptive_route_plasticity.sqlite3")
    p.add_argument("--output-dir", default="analysis/exp9")
    p.add_argument("--max-number", type=int, default=31)
    p.add_argument("--max-steps", type=int, default=8)
    p.add_argument("--transition-train-repeats", type=int, default=1)
    p.add_argument("--seeds", type=int, default=30)
    p.add_argument("--seed-offset", type=int, default=0)
    p.add_argument("--hidden-units", type=int, default=4096)
    p.add_argument("--number-assembly-size", type=int, default=72)
    p.add_argument("--mode-assembly-size", type=int, default=24)
    p.add_argument("--pair-assembly-size", type=int, default=48)
    p.add_argument("--mode-overlap", type=float, default=0.0)
    p.add_argument("--phases", nargs="+", choices=["interference", "feedback"], default=["interference", "feedback"])
    p.add_argument("--context-bleed-sweep", type=parse_float_list, default=parse_float_list("0 0.05 0.10 0.20 0.35 0.50"))
    p.add_argument("--feedback-noise-sweep", type=parse_float_list, default=parse_float_list("0 0.05 0.10 0.20 0.30"))
    p.add_argument("--reward-delay-sweep", type=parse_int_list, default=parse_int_list("0 2 4"))
    p.add_argument("--variants", nargs="*", default=None, help="Optional subset of variant names.")
    p.add_argument("--force", action="store_true")
    p.add_argument("--skip-analysis", action="store_true")
    return p.parse_args()


def reset_outputs(db_path: Path, output_dir: Path, force: bool) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    if force:
        if db_path.exists():
            db_path.unlink()
        for child in output_dir.glob("*"):
            if child.is_file():
                child.unlink()
            elif child.is_dir():
                shutil.rmtree(child)


def init_db(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS runs (
            run_id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_name TEXT NOT NULL,
            seed INTEGER NOT NULL,
            phase TEXT NOT NULL,
            exposure_repeats INTEGER NOT NULL,
            context_bleed REAL NOT NULL,
            feedback_noise REAL NOT NULL,
            reward_delay_steps INTEGER NOT NULL,
            status TEXT NOT NULL,
            started_at REAL NOT NULL,
            completed_at REAL,
            variant_json TEXT NOT NULL,
            graph_json TEXT NOT NULL,
            max_number INTEGER NOT NULL,
            max_steps INTEGER NOT NULL
        );
        CREATE TABLE IF NOT EXISTS metrics (
            run_id INTEGER NOT NULL,
            run_name TEXT NOT NULL,
            seed INTEGER NOT NULL,
            phase TEXT NOT NULL,
            exposure_repeats INTEGER NOT NULL,
            context_bleed REAL NOT NULL,
            feedback_noise REAL NOT NULL,
            reward_delay_steps INTEGER NOT NULL,
            metric TEXT NOT NULL,
            value REAL NOT NULL
        );
        CREATE TABLE IF NOT EXISTS predictions (
            run_id INTEGER NOT NULL,
            run_name TEXT NOT NULL,
            seed INTEGER NOT NULL,
            split TEXT NOT NULL,
            phase TEXT NOT NULL,
            exposure_repeats INTEGER NOT NULL,
            context_bleed REAL NOT NULL,
            feedback_noise REAL NOT NULL,
            reward_delay_steps INTEGER NOT NULL,
            mode TEXT NOT NULL,
            start INTEGER NOT NULL,
            steps INTEGER NOT NULL,
            target INTEGER NOT NULL,
            predicted INTEGER NOT NULL,
            correct INTEGER NOT NULL,
            failure_type TEXT NOT NULL,
            mean_step_target_rank REAL,
            max_step_target_rank REAL,
            mean_correct_margin REAL,
            min_correct_margin REAL,
            mean_context_margin REAL,
            min_context_margin REAL,
            mean_wrong_route_activation REAL,
            expected_path TEXT,
            actual_path TEXT
        );
        CREATE TABLE IF NOT EXISTS route_diagnostics (
            run_id INTEGER NOT NULL,
            run_name TEXT NOT NULL,
            seed INTEGER NOT NULL,
            phase TEXT NOT NULL,
            exposure_repeats INTEGER NOT NULL,
            context_bleed REAL NOT NULL,
            feedback_noise REAL NOT NULL,
            reward_delay_steps INTEGER NOT NULL,
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
        );
        CREATE TABLE IF NOT EXISTS baselines (
            seed INTEGER NOT NULL,
            split TEXT NOT NULL,
            baseline TEXT NOT NULL,
            accuracy REAL NOT NULL,
            n INTEGER NOT NULL
        );
        """
    )
    conn.commit()


def insert_run(conn: sqlite3.Connection, variant: VariantConfig, graph_cfg: GraphConfig, seed: int, phase: str, args: argparse.Namespace) -> int:
    cur = conn.execute(
        """
        INSERT INTO runs(run_name, seed, phase, exposure_repeats, context_bleed, feedback_noise, reward_delay_steps, status, started_at, variant_json, graph_json, max_number, max_steps)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            variant.name,
            seed,
            phase,
            args.transition_train_repeats,
            variant.context_bleed,
            variant.feedback_noise,
            variant.reward_delay_steps,
            "running",
            time.time(),
            json.dumps(asdict(variant), sort_keys=True),
            json.dumps(asdict(graph_cfg), sort_keys=True),
            args.max_number,
            args.max_steps,
        ),
    )
    conn.commit()
    return int(cur.lastrowid)


def finish_run(conn: sqlite3.Connection, run_id: int) -> None:
    conn.execute("UPDATE runs SET status = ?, completed_at = ? WHERE run_id = ?", ("completed", time.time(), run_id))
    conn.commit()


def insert_metrics(conn: sqlite3.Connection, run_id: int, variant: VariantConfig, seed: int, phase: str, exposure: int, metrics: dict) -> None:
    rows = [
        (run_id, variant.name, seed, phase, exposure, variant.context_bleed, variant.feedback_noise, variant.reward_delay_steps, k, float(v))
        for k, v in metrics.items()
        if v == v
    ]
    conn.executemany(
        "INSERT INTO metrics(run_id, run_name, seed, phase, exposure_repeats, context_bleed, feedback_noise, reward_delay_steps, metric, value) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        rows,
    )


def insert_prediction_rows(conn: sqlite3.Connection, run_id: int, rows: List[dict]) -> None:
    if not rows:
        return
    for r in rows:
        r["run_id"] = run_id
    cols = [
        "run_id", "run_name", "seed", "split", "phase", "exposure_repeats", "context_bleed", "feedback_noise", "reward_delay_steps",
        "mode", "start", "steps", "target", "predicted", "correct", "failure_type", "mean_step_target_rank", "max_step_target_rank",
        "mean_correct_margin", "min_correct_margin", "mean_context_margin", "min_context_margin", "mean_wrong_route_activation",
        "expected_path", "actual_path",
    ]
    ph = ",".join(["?"] * len(cols))
    conn.executemany(f"INSERT INTO predictions({','.join(cols)}) VALUES ({ph})", [[r.get(c) for c in cols] for r in rows])


def insert_route_rows(conn: sqlite3.Connection, run_id: int, variant: VariantConfig, seed: int, phase: str, exposure: int, rows: List[dict]) -> None:
    if not rows:
        return
    for r in rows:
        r["run_id"] = run_id
        r["run_name"] = variant.name
        r["seed"] = seed
        r["phase"] = phase
        r["exposure_repeats"] = exposure
        r["context_bleed"] = variant.context_bleed
        r["feedback_noise"] = variant.feedback_noise
        r["reward_delay_steps"] = variant.reward_delay_steps
    cols = [
        "run_id", "run_name", "seed", "phase", "exposure_repeats", "context_bleed", "feedback_noise", "reward_delay_steps",
        "mode", "source", "true_target", "predicted_target", "correct", "target_rank", "correct_margin", "context_margin",
        "wrong_route_activation", "target_score", "best_score", "top_targets",
    ]
    ph = ",".join(["?"] * len(cols))
    conn.executemany(f"INSERT INTO route_diagnostics({','.join(cols)}) VALUES ({ph})", [[r.get(c) for c in cols] for r in rows])


def insert_baselines(conn: sqlite3.Connection, seed: int, split: str, rows: List[dict]) -> None:
    conn.executemany(
        "INSERT INTO baselines(seed, split, baseline, accuracy, n) VALUES (?, ?, ?, ?, ?)",
        [(seed, split, r["baseline"], float(r["accuracy"]), int(r["n"])) for r in rows],
    )


def run_one(conn: sqlite3.Connection, variant: VariantConfig, graph_cfg: GraphConfig, seed: int, phase: str, args: argparse.Namespace, transition_tasks, composition_tasks) -> None:
    run_id = insert_run(conn, variant, graph_cfg, seed, phase, args)
    graph = RobustRouteGraph(graph_cfg, variant, seed)
    graph.train_curriculum(transition_tasks, repeats=args.transition_train_repeats)
    graph.finalize()

    transition_traces = [graph.predict(t) for t in transition_tasks]
    composition_traces = [graph.predict(t) for t in composition_tasks]
    route_rows = graph.route_diagnostics()

    metrics = {}
    metrics.update(summarize_traces(transition_traces, "transition"))
    metrics.update(summarize_by_mode_and_steps(transition_traces, "transition"))
    metrics.update(summarize_traces(composition_traces, "composition"))
    metrics.update(summarize_by_mode_and_steps(composition_traces, "composition"))
    metrics.update(route_summary(route_rows))

    insert_metrics(conn, run_id, variant, seed, phase, args.transition_train_repeats, metrics)
    pred_rows = [
        t.to_row(variant.name, seed, "transition", args.transition_train_repeats, phase, variant.context_bleed, variant.feedback_noise, variant.reward_delay_steps)
        for t in transition_traces
    ]
    pred_rows += [
        t.to_row(variant.name, seed, "composition", args.transition_train_repeats, phase, variant.context_bleed, variant.feedback_noise, variant.reward_delay_steps)
        for t in composition_traces
    ]
    insert_prediction_rows(conn, run_id, pred_rows)
    insert_route_rows(conn, run_id, variant, seed, phase, args.transition_train_repeats, route_rows)
    finish_run(conn, run_id)
    conn.commit()


def filter_variants(variants: List[VariantConfig], requested: Set[str] | None) -> List[VariantConfig]:
    if not requested:
        return variants
    return [v for v in variants if v.name in requested]


def main() -> None:
    args = parse_args()
    db_path = Path(args.db)
    out_dir = Path(args.output_dir)
    reset_outputs(db_path, out_dir, args.force)
    conn = sqlite3.connect(db_path)
    init_db(conn)

    transition_tasks = generate_transition_tasks(args.max_number)
    composition_tasks = generate_bounded_tasks(args.max_number, args.max_steps, min_steps=2)
    graph_cfg = GraphConfig(
        max_number=args.max_number,
        hidden_units=args.hidden_units,
        number_assembly_size=args.number_assembly_size,
        mode_assembly_size=args.mode_assembly_size,
        pair_assembly_size=args.pair_assembly_size,
        mode_overlap=args.mode_overlap,
    )

    for seed in range(args.seed_offset, args.seed_offset + args.seeds):
        insert_baselines(conn, seed, "transition", evaluate_baselines(transition_tasks, args.max_number, seed))
        insert_baselines(conn, seed, "composition", evaluate_baselines(composition_tasks, args.max_number, seed))

    requested = set(args.variants) if args.variants else None
    work: List[tuple[str, VariantConfig]] = []
    if "interference" in args.phases:
        for bleed in args.context_bleed_sweep:
            work.extend(("interference", v) for v in filter_variants(make_interference_variants(bleed), requested))
    if "feedback" in args.phases:
        for noise in args.feedback_noise_sweep:
            for delay in args.reward_delay_sweep:
                work.extend(("feedback", v) for v in filter_variants(make_feedback_variants(noise, delay), requested))

    if requested:
        found = {v.name for _, v in work}
        missing = requested - found
        if missing:
            raise ValueError(f"Unknown variant(s) or not present in selected phases: {sorted(missing)}")

    total = len(work) * args.seeds
    done = 0
    for seed in range(args.seed_offset, args.seed_offset + args.seeds):
        for phase, variant in work:
            done += 1
            print(
                f"[{done}/{total}] phase={phase} seed={seed} variant={variant.name} "
                f"bleed={variant.context_bleed} noise={variant.feedback_noise} delay={variant.reward_delay_steps}",
                flush=True,
            )
            run_one(conn, variant, graph_cfg, seed, phase, args, transition_tasks, composition_tasks)

    conn.close()

    if not args.skip_analysis:
        from analyze_exp9_suite import analyze
        analyze(db_path=db_path, output_dir=out_dir)


if __name__ == "__main__":
    main()
