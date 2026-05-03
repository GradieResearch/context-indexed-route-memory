from __future__ import annotations

import argparse
import json
import logging
import shutil
import sys
import time
from dataclasses import asdict
from pathlib import Path
from typing import Dict, List, Optional, Set, Sequence

import pandas as pd

from exp11.core import (
    ContextMemoryGraph,
    GraphConfig,
    VariantConfig,
    evaluate_baselines,
    failure_counts,
    generate_bounded_tasks,
    generate_transition_tasks,
    make_variants,
    route_summary,
    summarize_by_mode_and_steps,
    summarize_traces,
)


def parse_int_list(value: str) -> List[int]:
    return [int(x.strip()) for x in value.replace(",", " ").split() if x.strip()]


def parse_float_list(value: str) -> List[float]:
    return [float(x.strip()) for x in value.replace(",", " ").split() if x.strip()]


def parse_worlds(value: str) -> List[str]:
    return [x.strip().upper() for x in value.replace(",", " ").split() if x.strip()]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run Experiment 11 context-separated memory suite.")
    p.add_argument("--output-dir", default="analysis/exp11")
    p.add_argument("--max-number", type=int, default=31)
    p.add_argument("--max-steps", type=int, default=8)
    p.add_argument("--worlds", type=parse_worlds, default=parse_worlds("A B C D"))
    p.add_argument("--seeds", type=int, default=30)
    p.add_argument("--seed-offset", type=int, default=0)
    p.add_argument("--initial-exposure-repeats", type=int, default=1)
    p.add_argument("--new-world-exposure-schedule", type=parse_int_list, default=parse_int_list("0 1 2 3 5 8 13 21"))
    p.add_argument("--alternation-cycles", type=int, default=21)
    p.add_argument("--alternation-eval-schedule", type=parse_int_list, default=parse_int_list("0 1 2 3 5 8 13 21"))
    p.add_argument("--scaling-exposure-repeats", type=int, default=3)
    p.add_argument("--context-bleed-sweep", type=parse_float_list, default=parse_float_list("0 0.05 0.10 0.20 0.35"))
    p.add_argument("--context-dropout-sweep", type=parse_float_list, default=parse_float_list("0 0.05 0.10 0.20"))
    p.add_argument("--phases", nargs="+", choices=["sequential", "alternating", "scaling", "context_noise"], default=["sequential", "alternating", "scaling", "context_noise"])
    p.add_argument("--variants", nargs="*", default=None, help="Optional subset of variant names.")
    p.add_argument("--save-predictions", action="store_true", help="Write per-composition prediction rows. Disabled by default.")
    p.add_argument("--force", action="store_true")
    p.add_argument("--skip-analysis", action="store_true")
    p.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    p.add_argument("--log-every-seed", type=int, default=1)
    return p.parse_args()


def reset_outputs(output_dir: Path, force: bool) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    if force:
        for child in output_dir.glob("*"):
            if child.is_file():
                child.unlink()
            elif child.is_dir():
                shutil.rmtree(child)


def configure_logging(output_dir: Path, level: str) -> logging.Logger:
    logger = logging.getLogger("exp11")
    logger.setLevel(getattr(logging, level))
    logger.handlers.clear()
    fmt = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(fmt)
    stream.setLevel(getattr(logging, level))
    logger.addHandler(stream)
    output_dir.mkdir(parents=True, exist_ok=True)
    file_handler = logging.FileHandler(output_dir / "exp11_run.log", mode="w", encoding="utf-8")
    file_handler.setFormatter(fmt)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    return logger


def write_progress(output_dir: Path, event: dict) -> None:
    path = output_dir / "progress.jsonl"
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")


def prediction_row(trace, run_name: str, seed: int, phase: str, checkpoint: int, eval_world: str, bleed: float, dropout: float) -> dict:
    return {
        "run_name": run_name,
        "seed": seed,
        "phase": phase,
        "checkpoint": checkpoint,
        "eval_world": eval_world,
        "world_context_bleed": bleed,
        "world_context_dropout": dropout,
        "mode": trace.task.mode,
        "start": trace.task.start,
        "steps": trace.task.steps,
        "target": trace.task.target,
        "predicted": trace.predicted,
        "correct": int(trace.correct),
        "failure_type": trace.failure_type,
        "mean_step_target_rank": float(pd.Series(trace.step_target_ranks).mean()) if trace.step_target_ranks else None,
        "mean_correct_margin": float(pd.Series(trace.step_correct_margins).mean()) if trace.step_correct_margins else None,
        "mean_world_margin": float(pd.Series(trace.step_world_margins).mean()) if trace.step_world_margins else None,
        "mean_mode_margin": float(pd.Series(trace.step_mode_margins).mean()) if trace.step_mode_margins else None,
        "expected_path": "->".join(map(str, [trace.task.start] + trace.step_expected)),
        "actual_path": "->".join(map(str, [trace.task.start] + trace.step_predictions)),
    }


def evaluate_checkpoint(
    graph: ContextMemoryGraph,
    variant: VariantConfig,
    seed: int,
    phase: str,
    checkpoint: int,
    eval_worlds: Sequence[str],
    composition_tasks_by_world: Dict[str, list],
    transition_tasks_by_world: Dict[str, list],
    metrics_rows: List[dict],
    route_rows: List[dict],
    failure_rows: List[dict],
    prediction_rows: Optional[List[dict]],
    world_context_bleed: float = 0.0,
    world_context_dropout: float = 0.0,
) -> None:
    for eval_world in eval_worlds:
        comp_traces = [graph.predict(t, world_context_bleed, world_context_dropout) for t in composition_tasks_by_world[eval_world]]
        trans_traces = [graph.predict(t, world_context_bleed, world_context_dropout) for t in transition_tasks_by_world[eval_world]]
        m = {}
        m.update(summarize_traces(trans_traces, "transition"))
        m.update(summarize_traces(comp_traces, "composition"))
        m.update(summarize_by_mode_and_steps(comp_traces, "composition"))
        rdiag = graph.route_diagnostics(eval_world, world_context_bleed, world_context_dropout)
        m.update(route_summary(rdiag, "route"))
        for metric, value in m.items():
            if value == value:
                metrics_rows.append({
                    "run_name": variant.name,
                    "seed": seed,
                    "phase": phase,
                    "checkpoint": checkpoint,
                    "eval_world": eval_world,
                    "world_context_bleed": world_context_bleed,
                    "world_context_dropout": world_context_dropout,
                    "metric": metric,
                    "value": float(value),
                })
        for rr in rdiag:
            row = dict(rr)
            row.update({
                "run_name": variant.name,
                "seed": seed,
                "phase": phase,
                "checkpoint": checkpoint,
                "world_context_bleed": world_context_bleed,
                "world_context_dropout": world_context_dropout,
            })
            route_rows.append(row)
        failure_rows.extend(failure_counts(comp_traces, variant.name, seed, phase, checkpoint, eval_world))
        if prediction_rows is not None:
            prediction_rows.extend([prediction_row(t, variant.name, seed, phase, checkpoint, eval_world, world_context_bleed, world_context_dropout) for t in comp_traces])


def make_graph(args: argparse.Namespace, variant: VariantConfig, seed: int) -> ContextMemoryGraph:
    return ContextMemoryGraph(GraphConfig(max_number=args.max_number, max_steps=args.max_steps, worlds=tuple(args.worlds)), variant, seed)


def make_task_maps(args: argparse.Namespace) -> tuple[Dict[str, list], Dict[str, list]]:
    transition = {w: generate_transition_tasks(args.max_number, w) for w in args.worlds}
    composition = {w: generate_bounded_tasks(args.max_number, args.max_steps, w, min_steps=2) for w in args.worlds}
    return transition, composition


def run_sequential(
    args: argparse.Namespace,
    logger: logging.Logger,
    output_dir: Path,
    variant: VariantConfig,
    seed: int,
    transition: Dict[str, list],
    composition: Dict[str, list],
    metrics_rows: List[dict],
    route_rows: List[dict],
    failure_rows: List[dict],
    run_rows: List[dict],
    prediction_rows: Optional[List[dict]],
) -> None:
    start_t = time.time()
    worlds = args.worlds[:2]
    if len(worlds) < 2:
        return
    initial_world, new_world = worlds[0], worlds[1]
    graph = make_graph(args, variant, seed)
    logger.debug("sequential seed=%s variant=%s: train initial world %s", seed, variant.name, initial_world)
    graph.train_curriculum(transition[initial_world], args.initial_exposure_repeats, phase="initial")
    graph.consolidate()
    evaluate_checkpoint(graph, variant, seed, "sequential_after_initial", 0, worlds, composition, transition, metrics_rows, route_rows, failure_rows, prediction_rows)
    last = 0
    for ckpt in sorted(set(args.new_world_exposure_schedule)):
        if ckpt > last:
            graph.train_curriculum(transition[new_world], ckpt - last, phase="new_world")
            last = ckpt
        evaluate_checkpoint(graph, variant, seed, "sequential_learn_B", ckpt, worlds, composition, transition, metrics_rows, route_rows, failure_rows, prediction_rows)
        if ckpt in {0, 1, 2, max(args.new_world_exposure_schedule)}:
            logger.debug("sequential seed=%s variant=%s ckpt=%s evaluated A/B", seed, variant.name, ckpt)
    run_rows.append({
        "run_name": variant.name,
        "seed": seed,
        "phase": "sequential",
        "variant_json": json.dumps(asdict(variant), sort_keys=True),
        "completed_seconds": time.time() - start_t,
    })


def run_alternating(
    args: argparse.Namespace,
    logger: logging.Logger,
    output_dir: Path,
    variant: VariantConfig,
    seed: int,
    transition: Dict[str, list],
    composition: Dict[str, list],
    metrics_rows: List[dict],
    route_rows: List[dict],
    failure_rows: List[dict],
    run_rows: List[dict],
    prediction_rows: Optional[List[dict]],
) -> None:
    start_t = time.time()
    worlds = args.worlds[:2]
    if len(worlds) < 2:
        return
    graph = make_graph(args, variant, seed + 10_000)
    eval_points = set(args.alternation_eval_schedule)
    if 0 in eval_points:
        evaluate_checkpoint(graph, variant, seed, "alternating", 0, worlds, composition, transition, metrics_rows, route_rows, failure_rows, prediction_rows)
    for cycle in range(1, args.alternation_cycles + 1):
        phase = "alternating_initial" if cycle == 1 else "alternating"
        for w in worlds:
            graph.train_curriculum(transition[w], 1, phase=phase)
        if cycle == 1:
            graph.consolidate()
        if cycle in eval_points:
            evaluate_checkpoint(graph, variant, seed, "alternating", cycle, worlds, composition, transition, metrics_rows, route_rows, failure_rows, prediction_rows)
            logger.debug("alternating seed=%s variant=%s cycle=%s evaluated", seed, variant.name, cycle)
    run_rows.append({"run_name": variant.name, "seed": seed, "phase": "alternating", "variant_json": json.dumps(asdict(variant), sort_keys=True), "completed_seconds": time.time() - start_t})


def run_scaling(
    args: argparse.Namespace,
    logger: logging.Logger,
    output_dir: Path,
    variant: VariantConfig,
    seed: int,
    transition: Dict[str, list],
    composition: Dict[str, list],
    metrics_rows: List[dict],
    route_rows: List[dict],
    failure_rows: List[dict],
    run_rows: List[dict],
    prediction_rows: Optional[List[dict]],
) -> None:
    start_t = time.time()
    worlds = args.worlds
    graph = make_graph(args, variant, seed + 20_000)
    learned: List[str] = []
    evaluate_checkpoint(graph, variant, seed, "scaling", 0, worlds, composition, transition, metrics_rows, route_rows, failure_rows, prediction_rows)
    for idx, w in enumerate(worlds, start=1):
        phase = "initial" if idx == 1 else "new_world"
        graph.train_curriculum(transition[w], args.scaling_exposure_repeats, phase=phase)
        if idx == 1:
            graph.consolidate()
        learned.append(w)
        evaluate_checkpoint(graph, variant, seed, "scaling", idx, worlds, composition, transition, metrics_rows, route_rows, failure_rows, prediction_rows)
        logger.debug("scaling seed=%s variant=%s learned_worlds=%s", seed, variant.name, ''.join(learned))
    run_rows.append({"run_name": variant.name, "seed": seed, "phase": "scaling", "variant_json": json.dumps(asdict(variant), sort_keys=True), "completed_seconds": time.time() - start_t})


def run_context_noise(
    args: argparse.Namespace,
    logger: logging.Logger,
    output_dir: Path,
    variant: VariantConfig,
    seed: int,
    transition: Dict[str, list],
    composition: Dict[str, list],
    metrics_rows: List[dict],
    route_rows: List[dict],
    failure_rows: List[dict],
    run_rows: List[dict],
    prediction_rows: Optional[List[dict]],
) -> None:
    start_t = time.time()
    worlds = args.worlds[:2]
    if len(worlds) < 2:
        return
    graph = make_graph(args, variant, seed + 30_000)
    # Train A and B cleanly under explicit world context, then corrupt retrieval context at evaluation.
    for idx, w in enumerate(worlds):
        graph.train_curriculum(transition[w], args.scaling_exposure_repeats, phase="initial" if idx == 0 else "new_world")
        if idx == 0:
            graph.consolidate()
    for bleed in args.context_bleed_sweep:
        evaluate_checkpoint(graph, variant, seed, "context_bleed", int(round(bleed * 1000)), worlds, composition, transition, metrics_rows, route_rows, failure_rows, prediction_rows, world_context_bleed=bleed, world_context_dropout=0.0)
    for dropout in args.context_dropout_sweep:
        evaluate_checkpoint(graph, variant, seed, "context_dropout", int(round(dropout * 1000)), worlds, composition, transition, metrics_rows, route_rows, failure_rows, prediction_rows, world_context_bleed=0.0, world_context_dropout=dropout)
    logger.debug("context_noise seed=%s variant=%s evaluated %d bleed + %d dropout levels", seed, variant.name, len(args.context_bleed_sweep), len(args.context_dropout_sweep))
    run_rows.append({"run_name": variant.name, "seed": seed, "phase": "context_noise", "variant_json": json.dumps(asdict(variant), sort_keys=True), "completed_seconds": time.time() - start_t})


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    reset_outputs(output_dir, args.force)
    logger = configure_logging(output_dir, args.log_level)
    logger.info("Experiment 11 started")
    logger.info("Output directory: %s", output_dir)
    logger.info("Seeds=%s, worlds=%s, phases=%s", args.seeds, args.worlds, args.phases)
    logger.info("Large raw predictions are disabled unless --save-predictions is provided")

    selected: Optional[Set[str]] = set(args.variants) if args.variants else None
    variants = [v for v in make_variants() if selected is None or v.name in selected]
    logger.info("Variants: %s", ", ".join(v.name for v in variants))

    transition, composition = make_task_maps(args)
    metrics_rows: List[dict] = []
    route_rows: List[dict] = []
    failure_rows: List[dict] = []
    run_rows: List[dict] = []
    prediction_rows: Optional[List[dict]] = [] if args.save_predictions else None
    baseline_rows: List[dict] = []

    for seed_idx in range(args.seeds):
        seed = args.seed_offset + seed_idx
        for world in args.worlds:
            for split, tasks in [("transition", transition[world]), ("composition", composition[world])]:
                for row in evaluate_baselines(tasks, args.max_number, seed, args.worlds):
                    row.update({"seed": seed, "eval_world": world, "split": split})
                    baseline_rows.append(row)

    total_jobs = args.seeds * len(variants) * len(args.phases)
    done_jobs = 0
    global_start = time.time()
    for seed_idx in range(args.seeds):
        seed = args.seed_offset + seed_idx
        if seed_idx % max(1, args.log_every_seed) == 0:
            logger.info("Starting seed %s/%s (seed=%s)", seed_idx + 1, args.seeds, seed)
        for variant in variants:
            for phase in args.phases:
                job_start = time.time()
                logger.info("Job %s/%s: seed=%s variant=%s phase=%s", done_jobs + 1, total_jobs, seed, variant.name, phase)
                if phase == "sequential":
                    run_sequential(args, logger, output_dir, variant, seed, transition, composition, metrics_rows, route_rows, failure_rows, run_rows, prediction_rows)
                elif phase == "alternating":
                    run_alternating(args, logger, output_dir, variant, seed, transition, composition, metrics_rows, route_rows, failure_rows, run_rows, prediction_rows)
                elif phase == "scaling":
                    run_scaling(args, logger, output_dir, variant, seed, transition, composition, metrics_rows, route_rows, failure_rows, run_rows, prediction_rows)
                elif phase == "context_noise":
                    run_context_noise(args, logger, output_dir, variant, seed, transition, composition, metrics_rows, route_rows, failure_rows, run_rows, prediction_rows)
                done_jobs += 1
                event = {"event": "job_completed", "job": done_jobs, "total_jobs": total_jobs, "seed": seed, "variant": variant.name, "phase": phase, "seconds": time.time() - job_start}
                write_progress(output_dir, event)
                logger.info("Completed job %s/%s in %.2fs", done_jobs, total_jobs, event["seconds"])

    logger.info("Writing CSV outputs")
    pd.DataFrame(run_rows).to_csv(output_dir / "runs.csv", index=False)
    pd.DataFrame(metrics_rows).to_csv(output_dir / "metrics.csv", index=False)
    pd.DataFrame(route_rows).to_csv(output_dir / "route_diagnostics.csv", index=False)
    pd.DataFrame(failure_rows).to_csv(output_dir / "failure_taxonomy.csv", index=False)
    pd.DataFrame(baseline_rows).to_csv(output_dir / "baselines.csv", index=False)
    if prediction_rows is not None:
        pd.DataFrame(prediction_rows).to_csv(output_dir / "predictions.csv", index=False)

    logger.info("Raw run completed in %.2fs", time.time() - global_start)
    if not args.skip_analysis:
        logger.info("Starting analysis")
        from analyze_exp11_suite import analyze
        analyze(output_dir)
        logger.info("Analysis complete")
    logger.info("Experiment 11 finished")


if __name__ == "__main__":
    main()
