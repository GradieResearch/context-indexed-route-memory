from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


@dataclass(frozen=True)
class Variant:
    name: str
    args: tuple[str, ...]
    purpose: str


def variants() -> list[Variant]:
    return [
        Variant(
            name="full_recurrent_plastic_graph",
            args=("--use-recurrence", "--use-thresholds", "--use-traces", "--use-input-plasticity", "--use-reward-modulation"),
            purpose="Main hypothesis: recurrent graph traversal plus traces, thresholds, input plasticity, and reward gating.",
        ),
        Variant(
            name="no_recurrence_sparse_plastic_readout",
            args=("--no-use-recurrence", "--use-thresholds", "--use-traces", "--use-input-plasticity", "--use-reward-modulation"),
            purpose="Control: previous-style sparse plastic classifier without hidden-to-hidden traversal.",
        ),
        Variant(
            name="frozen_input_projection",
            args=("--use-recurrence", "--use-thresholds", "--use-traces", "--no-use-input-plasticity", "--use-reward-modulation"),
            purpose="Ablation: tests whether input-side plasticity contributes beyond a random feature projection.",
        ),
        Variant(
            name="no_homeostasis",
            args=("--use-recurrence", "--no-use-thresholds", "--use-traces", "--use-input-plasticity", "--use-reward-modulation"),
            purpose="Ablation: tests whether threshold homeostasis prevents active population collapse.",
        ),
        Variant(
            name="no_reward_modulation",
            args=("--use-recurrence", "--use-thresholds", "--use-traces", "--use-input-plasticity", "--no-use-reward-modulation"),
            purpose="Ablation: tests whether confidence/novelty-style plasticity gates matter.",
        ),
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a controlled suite of plastic graph MNIST variants")
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--hidden-units", type=int, default=4096)
    parser.add_argument("--input-edges-per-hidden", type=int, default=64)
    parser.add_argument("--active-hidden", type=int, default=128)
    parser.add_argument("--max-train", type=int, default=10000)
    parser.add_argument("--max-test", type=int, default=2000)
    parser.add_argument("--storage-dir", type=Path, default=Path("runs"))
    parser.add_argument("--database-name", type=str, default="plastic_graph_suite.sqlite3")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--only", nargs="*", default=None, help="Optional subset of variant names to run")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def build_base_args(args: argparse.Namespace) -> list[str]:
    return [
        sys.executable,
        "run_mnist_experiment.py",
        "--epochs", str(args.epochs),
        "--hidden-units", str(args.hidden_units),
        "--input-edges-per-hidden", str(args.input_edges_per_hidden),
        "--active-hidden", str(args.active_hidden),
        "--max-train", str(args.max_train),
        "--max-test", str(args.max_test),
        "--storage-dir", str(args.storage_dir),
        "--database-name", args.database_name,
        "--seed", str(args.seed),
    ]


def main() -> None:
    args = parse_args()
    selected = variants()
    if args.only:
        allowed = set(args.only)
        selected = [v for v in selected if v.name in allowed]
        missing = allowed - {v.name for v in selected}
        if missing:
            raise SystemExit(f"Unknown variant(s): {sorted(missing)}")

    print("Experiment suite variants:")
    for variant in selected:
        print(f"- {variant.name}: {variant.purpose}")

    base = build_base_args(args)
    for variant in selected:
        command = base + ["--run-name", variant.name] + list(variant.args)
        print("\n$", " ".join(command))
        if args.dry_run:
            continue
        subprocess.run(command, check=True)

    if not args.dry_run:
        print("\nSuite complete. Compare runs with:")
        print(f"  {sys.executable} analyze_experiment_suite.py --db {args.storage_dir / args.database_name} --output-dir analysis/suite")


if __name__ == "__main__":
    main()
