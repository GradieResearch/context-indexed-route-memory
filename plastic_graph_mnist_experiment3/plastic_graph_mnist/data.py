from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, Tuple

import numpy as np

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Sample:
    x: np.ndarray
    y: int


class MnistProvider:
    """Loads MNIST and exposes online/event-style iterators.

    The training loop intentionally consumes one sample at a time so the graph can
    update from immediate reward/correction signals.
    """

    def __init__(self, data_dir: Path = Path("data"), seed: int = 42):
        self.data_dir = data_dir
        self.seed = seed

    def load(self, max_train: int | None = None, max_test: int | None = None) -> tuple[list[Sample], list[Sample]]:
        try:
            from torchvision import datasets, transforms
        except ImportError as exc:
            raise RuntimeError(
                "torchvision is required for MNIST. Install dependencies with: pip install -r requirements.txt"
            ) from exc

        transform = transforms.Compose([transforms.ToTensor()])
        train_ds = datasets.MNIST(root=str(self.data_dir), train=True, download=True, transform=transform)
        test_ds = datasets.MNIST(root=str(self.data_dir), train=False, download=True, transform=transform)

        train = self._convert(train_ds, max_train)
        test = self._convert(test_ds, max_test)
        logger.info("Loaded MNIST train=%s test=%s", len(train), len(test))
        return train, test

    def shuffled(self, samples: list[Sample], epoch: int) -> Iterator[Sample]:
        rng = np.random.default_rng(self.seed + epoch)
        indices = rng.permutation(len(samples))
        for idx in indices:
            yield samples[int(idx)]

    @staticmethod
    def _convert(dataset, limit: int | None) -> list[Sample]:
        count = len(dataset) if limit is None else min(limit, len(dataset))
        samples: list[Sample] = []
        for i in range(count):
            x_tensor, y = dataset[i]
            x = x_tensor.numpy().astype(np.float32).reshape(-1)
            samples.append(Sample(x=x, y=int(y)))
        return samples
