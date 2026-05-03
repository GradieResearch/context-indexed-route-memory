from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ContextRouterConfig:
    """Keeps a mode/context signal alive during recurrent traversal."""

    routing_bonus: float = 0.5
    reserved_context_units: int = 16


class PersistentContextRouter:
    """Biases selection toward the currently relevant context assembly."""

    def __init__(self, config: ContextRouterConfig):
        self.config = config

    def boost(self, drive: np.ndarray, context_units: np.ndarray) -> np.ndarray:
        boosted = drive.copy()
        if self.config.routing_bonus > 0.0 and len(context_units) > 0:
            boosted[context_units] += self.config.routing_bonus
        return boosted

    def select_active(
        self,
        drive: np.ndarray,
        context_units: np.ndarray,
        active_units: int,
    ) -> np.ndarray:
        if active_units <= 0:
            return np.zeros(0, dtype=np.int32)

        reserve = min(self.config.reserved_context_units, active_units, len(context_units))
        reserved = np.zeros(0, dtype=np.int32)
        if reserve > 0:
            context_scores = drive[context_units]
            top_context = np.argpartition(context_scores, -reserve)[-reserve:]
            reserved = context_units[top_context[np.argsort(context_scores[top_context])[::-1]]].astype(np.int32)

        remaining = active_units - len(reserved)
        available_mask = np.ones(len(drive), dtype=bool)
        if len(reserved) > 0:
            available_mask[reserved] = False
        available = np.flatnonzero(available_mask)

        selected = np.zeros(0, dtype=np.int32)
        if remaining > 0 and len(available) > 0:
            if remaining >= len(available):
                top_other = available[np.argsort(drive[available])[::-1]]
            else:
                other_scores = drive[available]
                top_idx = np.argpartition(other_scores, -remaining)[-remaining:]
                top_other = available[top_idx[np.argsort(other_scores[top_idx])[::-1]]]
            selected = top_other.astype(np.int32)

        if len(reserved) == 0:
            return selected
        if len(selected) == 0:
            return reserved
        return np.concatenate([reserved, selected]).astype(np.int32)
