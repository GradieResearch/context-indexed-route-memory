from __future__ import annotations

import argparse
import logging
from pathlib import Path

from plastic_graph_mnist.config import ExperimentConfig
from plastic_graph_mnist.data import MnistProvider
from plastic_graph_mnist.logging_utils import configure_logging
from plastic_graph_mnist.modulators import RewardModulator
from plastic_graph_mnist.plastic_graph import PlasticGraphNetwork
from plastic_graph_mnist.storage import ExperimentStore
from plastic_graph_mnist.trainer import ExperimentTrainer

logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run persistent plastic graph MNIST experiment")
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--hidden-units", type=int, default=4096)
    parser.add_argument("--input-edges-per-hidden", type=int, default=64)
    parser.add_argument("--active-hidden", type=int, default=128)
    parser.add_argument("--max-train", type=int, default=10000)
    parser.add_argument("--max-test", type=int, default=2000)
    parser.add_argument("--storage-dir", type=Path, default=Path("runs"))
    parser.add_argument("--database-name", type=str, default="plastic_graph_mnist.sqlite3")
    parser.add_argument("--log-every", type=int, default=500)
    parser.add_argument("--eval-every", type=int, default=2500)
    parser.add_argument("--checkpoint-every", type=int, default=5000)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def build_config(args: argparse.Namespace) -> ExperimentConfig:
    return ExperimentConfig(
        seed=args.seed,
        epochs=args.epochs,
        hidden_units=args.hidden_units,
        input_edges_per_hidden=args.input_edges_per_hidden,
        active_hidden=args.active_hidden,
        max_train=args.max_train,
        max_test=args.max_test,
        storage_dir=args.storage_dir,
        database_name=args.database_name,
        log_every=args.log_every,
        eval_every=args.eval_every,
        checkpoint_every=args.checkpoint_every,
    )


def main() -> None:
    configure_logging(logging.INFO)
    args = parse_args()
    config = build_config(args)

    store = ExperimentStore(config.database_path)
    store.initialize()
    run_id = store.create_run(config.run_name, config.to_dict())

    data_provider = MnistProvider(seed=config.seed)
    graph = PlasticGraphNetwork.create(config)
    modulator = RewardModulator(
        min_gate=config.min_plasticity_gate,
        max_gate=config.max_plasticity_gate,
        negative_reward_scale=config.negative_reward_scale,
    )

    trainer = ExperimentTrainer(
        config=config,
        data_provider=data_provider,
        graph=graph,
        modulator=modulator,
        store=store,
        run_id=run_id,
    )
    trainer.train()


if __name__ == "__main__":
    main()
