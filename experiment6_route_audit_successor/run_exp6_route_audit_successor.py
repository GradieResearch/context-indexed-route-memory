from __future__ import annotations

import argparse
from pathlib import Path

from plastic_graph_mnist.contextual_successor_graph import ContextualSuccessorGraphConfig
from plastic_graph_mnist.contextual_successor_task import ContextualSuccessorTaskConfig
from plastic_graph_mnist.contextual_successor_trainer import ContextualSuccessorExperimentTrainer
from plastic_graph_mnist.logging_utils import configure_logging
from plastic_graph_mnist.storage import ExperimentStore


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Experiment 6: route-audited contextual successor world.")
    parser.add_argument("--db", type=Path, default=Path("runs/exp6_route_audit_successor.sqlite3"))
    parser.add_argument("--run-name", type=str, default="exp6_full_route_audit")
    parser.add_argument("--max-number", type=int, default=24)
    parser.add_argument("--max-steps", type=int, default=5)
    parser.add_argument("--train-sequence-repeats", type=int, default=120)
    parser.add_argument("--training-max-steps", type=int, default=2)
    parser.add_argument("--hidden-units", type=int, default=4096)
    parser.add_argument("--assembly-size", type=int, default=72)
    parser.add_argument("--mode-assembly-size", type=int, default=24)
    parser.add_argument("--active-units", type=int, default=96)
    parser.add_argument("--recurrent-edges-per-unit", type=int, default=48)
    parser.add_argument("--learning-rate", type=float, default=0.08)
    parser.add_argument("--negative-learning-rate", type=float, default=0.02)
    parser.add_argument("--structural-replacements-per-update", type=int, default=8)
    parser.add_argument("--context-routing-bonus", type=float, default=0.5)
    parser.add_argument("--reserved-context-units", type=int, default=16)
    parser.add_argument("--context-source-gain", type=float, default=4.0)
    parser.add_argument("--competing-context-penalty", type=float, default=0.35)
    parser.add_argument("--lingering-activity-penalty", type=float, default=0.08)
    parser.add_argument("--feedback-noise", type=float, default=0.0)
    parser.add_argument("--eval-every", type=int, default=250)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--delayed-reward", action="store_true")
    parser.add_argument("--rule-reversal", action="store_true")
    parser.add_argument("--reversal-fraction", type=float, default=0.5)
    parser.add_argument("--no-recurrence", action="store_true")
    parser.add_argument("--no-structural-plasticity", action="store_true")
    parser.add_argument("--no-homeostasis", action="store_true")
    parser.add_argument("--no-reward-gate", action="store_true")
    parser.add_argument("--no-context-routing", action="store_true")
    parser.add_argument("--no-inhibition", action="store_true")
    return parser.parse_args()


def main() -> None:
    configure_logging()
    args = parse_args()
    store = ExperimentStore(args.db)
    store.initialize()
    task_config = ContextualSuccessorTaskConfig(
        max_number=args.max_number,
        max_steps=args.max_steps,
        train_sequence_repeats=args.train_sequence_repeats,
        training_max_steps=args.training_max_steps,
        feedback_noise=args.feedback_noise,
        delayed_reward=args.delayed_reward,
        rule_reversal=args.rule_reversal,
        reversal_fraction=args.reversal_fraction,
        seed=args.seed,
    )
    graph_config = ContextualSuccessorGraphConfig(
        num_concepts=args.max_number + 1,
        hidden_units=args.hidden_units,
        assembly_size=args.assembly_size,
        mode_assembly_size=args.mode_assembly_size,
        active_units=args.active_units,
        recurrent_edges_per_unit=args.recurrent_edges_per_unit,
        learning_rate=args.learning_rate,
        negative_learning_rate=args.negative_learning_rate,
        structural_replacements_per_update=args.structural_replacements_per_update,
        context_routing_bonus=args.context_routing_bonus,
        reserved_context_units=args.reserved_context_units,
        context_source_gain=args.context_source_gain,
        competing_context_penalty=args.competing_context_penalty,
        lingering_activity_penalty=args.lingering_activity_penalty,
        mode_names=task_config.modes,
        use_recurrence=not args.no_recurrence,
        use_structural_plasticity=not args.no_structural_plasticity,
        use_homeostasis=not args.no_homeostasis,
        use_reward_gate=not args.no_reward_gate,
        use_context_routing=not args.no_context_routing,
        use_inhibition=not args.no_inhibition,
        seed=args.seed,
    )
    trainer = ContextualSuccessorExperimentTrainer(graph_config, task_config, store, args.run_name)
    trainer.train(eval_every=args.eval_every)


if __name__ == "__main__":
    main()
