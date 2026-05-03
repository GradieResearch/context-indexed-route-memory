from __future__ import annotations

import argparse
import json
import shutil
import time
from dataclasses import asdict
from pathlib import Path
from typing import Dict, List, Optional, Set

import pandas as pd

from exp10.core import (
    AdaptiveRouteGraph,
    GraphConfig,
    VariantConfig,
    evaluate_baselines,
    failure_counts,
    generate_bounded_tasks,
    generate_transition_tasks,
    make_reversal_variants,
    route_summary,
    summarize_by_mode_and_steps,
    summarize_traces,
)


def parse_int_list(value: str) -> List[int]:
    return [int(x.strip()) for x in value.replace(",", " ").split() if x.strip()]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run Experiment 10 rule reversal/adaptive memory suite.")
    p.add_argument("--output-dir", default="analysis/exp10")
    p.add_argument("--max-number", type=int, default=31)
    p.add_argument("--max-steps", type=int, default=8)
    p.add_argument("--initial-exposure-repeats", type=int, default=1)
    p.add_argument("--reversal-exposure-schedule", type=parse_int_list, default=parse_int_list("0 1 2 3 5 8 13 21"))
    p.add_argument("--switchback-exposure-schedule", type=parse_int_list, default=parse_int_list("0 1 2 3 5 8 13"))
    p.add_argument("--seeds", type=int, default=30)
    p.add_argument("--seed-offset", type=int, default=0)
    p.add_argument("--hidden-units", type=int, default=4096)
    p.add_argument("--number-assembly-size", type=int, default=72)
    p.add_argument("--mode-assembly-size", type=int, default=24)
    p.add_argument("--pair-assembly-size", type=int, default=48)
    p.add_argument("--world-assembly-size", type=int, default=24)
    p.add_argument("--phases", nargs="+", choices=["reversal", "switchback", "stress"], default=["reversal", "switchback"])
    p.add_argument("--feedback-noise", type=float, default=0.0)
    p.add_argument("--reward-delay-steps", type=int, default=0)
    p.add_argument("--stress-feedback-noise", type=float, default=0.10)
    p.add_argument("--stress-reward-delay-steps", type=int, default=2)
    p.add_argument("--variants", nargs="*", default=None, help="Optional subset of variant names.")
    p.add_argument("--save-predictions", action="store_true", help="Write per-task predictions. Disabled by default to keep outputs small.")
    p.add_argument("--force", action="store_true")
    p.add_argument("--skip-analysis", action="store_true")
    return p.parse_args()


def reset_outputs(output_dir: Path, force: bool) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    if force:
        for child in output_dir.glob("*"):
            if child.is_file():
                child.unlink()
            elif child.is_dir():
                shutil.rmtree(child)


def prediction_row(trace, run_name: str, seed: int, phase: str, checkpoint: int, eval_rule: str) -> dict:
    return {
        "run_name": run_name,
        "seed": seed,
        "phase": phase,
        "checkpoint": checkpoint,
        "eval_rule": eval_rule,
        "mode": trace.task.mode,
        "start": trace.task.start,
        "steps": trace.task.steps,
        "target": trace.task.target,
        "predicted": trace.predicted,
        "correct": int(trace.correct),
        "failure_type": trace.failure_type,
        "mean_step_target_rank": float(pd.Series(trace.step_target_ranks).mean()) if trace.step_target_ranks else None,
        "mean_correct_margin": float(pd.Series(trace.step_correct_margins).mean()) if trace.step_correct_margins else None,
        "min_correct_margin": float(pd.Series(trace.step_correct_margins).min()) if trace.step_correct_margins else None,
        "expected_path": "->".join(map(str, [trace.task.start] + trace.step_expected)),
        "actual_path": "->".join(map(str, [trace.task.start] + trace.step_predictions)),
    }


def evaluate_checkpoint(
    graph: AdaptiveRouteGraph,
    variant: VariantConfig,
    seed: int,
    phase: str,
    checkpoint: int,
    composition_tasks_by_rule: Dict[str, list],
    transition_tasks_by_rule: Dict[str, list],
    metrics_rows: List[dict],
    route_rows: List[dict],
    failure_rows: List[dict],
    prediction_rows: Optional[List[dict]],
) -> None:
    graph.finalize()
    for eval_rule in ["A", "B"]:
        comp_traces = [graph.predict(t) for t in composition_tasks_by_rule[eval_rule]]
        trans_traces = [graph.predict(t) for t in transition_tasks_by_rule[eval_rule]]
        m = {}
        m.update(summarize_traces(trans_traces, "transition"))
        m.update(summarize_traces(comp_traces, "composition"))
        m.update(summarize_by_mode_and_steps(comp_traces, "composition"))
        rdiag = graph.route_diagnostics(eval_rule)
        m.update(route_summary(rdiag, "route"))
        for metric, value in m.items():
            if value == value:
                metrics_rows.append({
                    "run_name": variant.name,
                    "seed": seed,
                    "phase": phase,
                    "checkpoint": checkpoint,
                    "eval_rule": eval_rule,
                    "feedback_noise": variant.feedback_noise,
                    "reward_delay_steps": variant.reward_delay_steps,
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
                "feedback_noise": variant.feedback_noise,
                "reward_delay_steps": variant.reward_delay_steps,
            })
            route_rows.append(row)
        failure_rows.extend(failure_counts(comp_traces, variant.name, seed, phase, checkpoint, eval_rule))
        if prediction_rows is not None:
            prediction_rows.extend([prediction_row(t, variant.name, seed, phase, checkpoint, eval_rule) for t in comp_traces])


def run_variant(
    variant: VariantConfig,
    graph_cfg: GraphConfig,
    seed: int,
    args: argparse.Namespace,
    metrics_rows: List[dict],
    route_rows: List[dict],
    failure_rows: List[dict],
    run_rows: List[dict],
    prediction_rows: Optional[List[dict]],
    phase_label: str,
) -> None:
    started = time.time()
    graph = AdaptiveRouteGraph(graph_cfg, variant, seed)
    transition_A = generate_transition_tasks(args.max_number, "A")
    transition_B = generate_transition_tasks(args.max_number, "B")
    composition_A = generate_bounded_tasks(args.max_number, args.max_steps, "A", min_steps=2)
    composition_B = generate_bounded_tasks(args.max_number, args.max_steps, "B", min_steps=2)
    comp_by_rule = {"A": composition_A, "B": composition_B}
    trans_by_rule = {"A": transition_A, "B": transition_B}

    # Initial learning of rule A.
    graph.train_curriculum(transition_A, args.initial_exposure_repeats, phase="initial")
    evaluate_checkpoint(graph, variant, seed, f"{phase_label}_pre_reversal", 0, comp_by_rule, trans_by_rule, metrics_rows, route_rows, failure_rows, prediction_rows)
    graph.consolidate()

    # Reversal: train rule B cumulatively and evaluate both A and B at each checkpoint.
    last = 0
    for ckpt in sorted(set(args.reversal_exposure_schedule)):
        if ckpt > last:
            graph.train_curriculum(transition_B, ckpt - last, phase="reversal")
            last = ckpt
        evaluate_checkpoint(graph, variant, seed, f"{phase_label}_reversal", ckpt, comp_by_rule, trans_by_rule, metrics_rows, route_rows, failure_rows, prediction_rows)

    # Optional switchback: after B has been learned, train A again and evaluate both rules.
    if phase_label == "clean" and "switchback" in args.phases:
        last = 0
        for ckpt in sorted(set(args.switchback_exposure_schedule)):
            if ckpt > last:
                graph.train_curriculum(transition_A, ckpt - last, phase="switchback")
                last = ckpt
            evaluate_checkpoint(graph, variant, seed, "clean_switchback", ckpt, comp_by_rule, trans_by_rule, metrics_rows, route_rows, failure_rows, prediction_rows)

    run_rows.append({
        "run_name": variant.name,
        "seed": seed,
        "phase_label": phase_label,
        "feedback_noise": variant.feedback_noise,
        "reward_delay_steps": variant.reward_delay_steps,
        "variant_json": json.dumps(asdict(variant), sort_keys=True),
        "graph_json": json.dumps(asdict(graph_cfg), sort_keys=True),
        "completed_seconds": time.time() - started,
    })


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    reset_outputs(output_dir, args.force)

    graph_cfg = GraphConfig(
        max_number=args.max_number,
        hidden_units=args.hidden_units,
        number_assembly_size=args.number_assembly_size,
        mode_assembly_size=args.mode_assembly_size,
        pair_assembly_size=args.pair_assembly_size,
        world_assembly_size=args.world_assembly_size,
    )

    selected: Optional[Set[str]] = set(args.variants) if args.variants else None
    metrics_rows: List[dict] = []
    route_rows: List[dict] = []
    failure_rows: List[dict] = []
    run_rows: List[dict] = []
    prediction_rows: Optional[List[dict]] = [] if args.save_predictions else None

    # Baselines are deterministic task-level baselines for each rule.
    baseline_rows: List[dict] = []
    for seed_idx in range(args.seeds):
        seed = args.seed_offset + seed_idx
        for rule in ["A", "B"]:
            for split, tasks in [
                ("transition", generate_transition_tasks(args.max_number, rule)),
                ("composition", generate_bounded_tasks(args.max_number, args.max_steps, rule, min_steps=2)),
            ]:
                for row in evaluate_baselines(tasks, args.max_number, seed):
                    row.update({"seed": seed, "eval_rule": rule, "split": split})
                    baseline_rows.append(row)

    def maybe_variants(noise: float, delay: int) -> List[VariantConfig]:
        vars_ = make_reversal_variants(feedback_noise=noise, reward_delay_steps=delay)
        return [v for v in vars_ if selected is None or v.name in selected]

    for seed_idx in range(args.seeds):
        seed = args.seed_offset + seed_idx
        if "reversal" in args.phases or "switchback" in args.phases:
            for variant in maybe_variants(args.feedback_noise, args.reward_delay_steps):
                run_variant(variant, graph_cfg, seed, args, metrics_rows, route_rows, failure_rows, run_rows, prediction_rows, "clean")
        if "stress" in args.phases:
            for variant in maybe_variants(args.stress_feedback_noise, args.stress_reward_delay_steps):
                run_variant(variant, graph_cfg, seed, args, metrics_rows, route_rows, failure_rows, run_rows, prediction_rows, "stress")

    pd.DataFrame(run_rows).to_csv(output_dir / "runs.csv", index=False)
    pd.DataFrame(metrics_rows).to_csv(output_dir / "metrics.csv", index=False)
    pd.DataFrame(route_rows).to_csv(output_dir / "route_diagnostics.csv", index=False)
    pd.DataFrame(failure_rows).to_csv(output_dir / "failure_taxonomy.csv", index=False)
    pd.DataFrame(baseline_rows).to_csv(output_dir / "baselines.csv", index=False)
    if prediction_rows is not None:
        pd.DataFrame(prediction_rows).to_csv(output_dir / "predictions.csv", index=False)

    if not args.skip_analysis:
        from analyze_exp10_suite import analyze
        analyze(output_dir)


if __name__ == "__main__":
    main()
