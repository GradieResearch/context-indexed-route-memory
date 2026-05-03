from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Experiment 5 controlled variants.")
    parser.add_argument("--db", type=Path, default=Path("runs/exp5_contextual_successor_suite.sqlite3"))
    parser.add_argument("--max-number", type=int, default=24)
    parser.add_argument("--max-steps", type=int, default=5)
    parser.add_argument("--train-sequence-repeats", type=int, default=120)
    parser.add_argument("--training-max-steps", type=int, default=1)
    parser.add_argument("--hidden-units", type=int, default=4096)
    parser.add_argument("--assembly-size", type=int, default=72)
    parser.add_argument("--mode-assembly-size", type=int, default=24)
    parser.add_argument("--active-units", type=int, default=96)
    parser.add_argument("--recurrent-edges-per-unit", type=int, default=48)
    parser.add_argument("--feedback-noise", type=float, default=0.0)
    parser.add_argument("--eval-every", type=int, default=250)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--delayed-reward", action="store_true")
    parser.add_argument("--rule-reversal", action="store_true")
    parser.add_argument("--reversal-fraction", type=float, default=0.5)
    return parser.parse_args()


def run_variant(args: argparse.Namespace, name: str, extra_flags: list[str]) -> None:
    command = [
        sys.executable,
        "run_exp5_contextual_successor.py",
        "--db",
        str(args.db),
        "--run-name",
        name,
        "--max-number",
        str(args.max_number),
        "--max-steps",
        str(args.max_steps),
        "--train-sequence-repeats",
        str(args.train_sequence_repeats),
        "--training-max-steps",
        str(args.training_max_steps),
        "--hidden-units",
        str(args.hidden_units),
        "--assembly-size",
        str(args.assembly_size),
        "--mode-assembly-size",
        str(args.mode_assembly_size),
        "--active-units",
        str(args.active_units),
        "--recurrent-edges-per-unit",
        str(args.recurrent_edges_per_unit),
        "--feedback-noise",
        str(args.feedback_noise),
        "--eval-every",
        str(args.eval_every),
        "--seed",
        str(args.seed),
        *extra_flags,
    ]
    if args.delayed_reward:
        command.append("--delayed-reward")
    if args.rule_reversal:
        command.extend(["--rule-reversal", "--reversal-fraction", str(args.reversal_fraction)])
    print("\n=== Running", name, "===")
    subprocess.run(command, check=True)


def main() -> None:
    args = parse_args()
    variants = [
        ("exp5_full_contextual_traversal", []),
        ("exp5_no_recurrence", ["--no-recurrence"]),
        ("exp5_no_structural_plasticity", ["--no-structural-plasticity"]),
        ("exp5_no_reward_gate", ["--no-reward-gate"]),
        ("exp5_no_homeostasis", ["--no-homeostasis"]),
        ("exp5_no_context_routing", ["--no-context-routing"]),
        ("exp5_no_inhibition", ["--no-inhibition"]),
    ]
    for name, flags in variants:
        run_variant(args, name, flags)


if __name__ == "__main__":
    main()
