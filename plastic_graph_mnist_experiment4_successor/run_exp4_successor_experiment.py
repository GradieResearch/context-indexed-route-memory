from __future__ import annotations

import argparse
from pathlib import Path

from plastic_graph_mnist.logging_utils import configure_logging
from plastic_graph_mnist.storage import ExperimentStore
from plastic_graph_mnist.successor_graph import SuccessorGraphConfig
from plastic_graph_mnist.successor_task import SuccessorTaskConfig
from plastic_graph_mnist.successor_trainer import SuccessorExperimentTrainer


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Experiment 4: successor traversal plastic graph.")
    parser.add_argument("--db", type=Path, default=Path("runs/exp4_successor.sqlite3"))
    parser.add_argument("--run-name", type=str, default="exp4_full_successor_traversal")
    parser.add_argument("--max-number", type=int, default=24)
    parser.add_argument("--max-addend", type=int, default=5)
    parser.add_argument("--train-transition-repeats", type=int, default=120)
    parser.add_argument("--hidden-units", type=int, default=4096)
    parser.add_argument("--assembly-size", type=int, default=96)
    parser.add_argument("--active-units", type=int, default=96)
    parser.add_argument("--recurrent-edges-per-unit", type=int, default=48)
    parser.add_argument("--learning-rate", type=float, default=0.08)
    parser.add_argument("--negative-learning-rate", type=float, default=0.02)
    parser.add_argument("--structural-replacements-per-update", type=int, default=8)
    parser.add_argument("--eval-every", type=int, default=250)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--no-recurrence", action="store_true")
    parser.add_argument("--no-structural-plasticity", action="store_true")
    parser.add_argument("--no-homeostasis", action="store_true")
    parser.add_argument("--no-reward-gate", action="store_true")
    return parser.parse_args()


def main() -> None:
    configure_logging()
    args = parse_args()
    store = ExperimentStore(args.db)
    store.initialize()
    task_config = SuccessorTaskConfig(
        max_number=args.max_number,
        max_addend=args.max_addend,
        train_transition_repeats=args.train_transition_repeats,
        seed=args.seed,
    )
    graph_config = SuccessorGraphConfig(
        num_concepts=args.max_number + 1,
        hidden_units=args.hidden_units,
        assembly_size=args.assembly_size,
        active_units=args.active_units,
        recurrent_edges_per_unit=args.recurrent_edges_per_unit,
        learning_rate=args.learning_rate,
        negative_learning_rate=args.negative_learning_rate,
        structural_replacements_per_update=args.structural_replacements_per_update,
        use_recurrence=not args.no_recurrence,
        use_structural_plasticity=not args.no_structural_plasticity,
        use_homeostasis=not args.no_homeostasis,
        use_reward_gate=not args.no_reward_gate,
        seed=args.seed,
    )
    trainer = SuccessorExperimentTrainer(graph_config, task_config, store, args.run_name)
    trainer.train(eval_every=args.eval_every)


if __name__ == "__main__":
    main()
