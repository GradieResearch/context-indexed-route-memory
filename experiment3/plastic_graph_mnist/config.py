from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict


@dataclass(frozen=True)
class ExperimentConfig:
    """Configuration for one plastic-graph MNIST experiment."""

    seed: int = 42
    input_dim: int = 28 * 28
    output_dim: int = 10

    # Graph size / sparsity
    hidden_units: int = 4096
    input_edges_per_hidden: int = 64
    active_hidden: int = 128

    # Recurrent graph traversal. This is the main "next experiment" addition.
    use_recurrence: bool = True
    hidden_recurrent_edges_per_hidden: int = 16
    recurrent_steps: int = 2
    recurrent_weight_scale: float = 0.025
    recurrent_lr: float = 0.0015
    recurrent_decay: float = 0.000005
    recurrent_mix: float = 0.65

    # Dynamics
    activation_temperature: float = 1.0
    target_activation_rate: float = 0.03
    threshold_lr: float = 0.002
    trace_decay: float = 0.92
    use_thresholds: bool = True
    use_traces: bool = True

    # Plasticity
    learning_rate_hidden_output: float = 0.035
    learning_rate_input_hidden: float = 0.002
    weight_decay: float = 0.00001
    negative_reward_scale: float = 0.35
    max_plasticity_gate: float = 1.0
    min_plasticity_gate: float = 0.05
    use_input_plasticity: bool = True
    use_reward_modulation: bool = True

    # Training
    epochs: int = 3
    batch_size: int = 1  # event-driven online learning; intentionally one sample at a time
    max_train: int | None = 10000
    max_test: int | None = 2000
    log_every: int = 500
    eval_every: int = 2500
    checkpoint_every: int = 5000

    # Persistence
    run_name: str = "plastic_graph_recurrent_mnist"
    storage_dir: Path = Path("runs")
    database_name: str = "plastic_graph_mnist.sqlite3"

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data["storage_dir"] = str(self.storage_dir)
        return data

    @property
    def database_path(self) -> Path:
        return self.storage_dir / self.database_name
