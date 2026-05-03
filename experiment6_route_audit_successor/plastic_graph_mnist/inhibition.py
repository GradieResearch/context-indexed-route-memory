from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class InhibitionConfig:
    """Simple competition controller for contextual traversal."""

    competing_context_penalty: float = 0.35
    lingering_activity_penalty: float = 0.08


class ContextualInhibitionController:
    """Suppresses competing contexts and stale recurrent activity."""

    def __init__(self, config: InhibitionConfig):
        self.config = config

    def apply(
        self,
        drive: np.ndarray,
        current_context_units: np.ndarray,
        competing_context_units: np.ndarray,
        previous_active: np.ndarray,
    ) -> np.ndarray:
        inhibited = drive.copy()
        if self.config.competing_context_penalty > 0.0 and len(competing_context_units) > 0:
            inhibited[competing_context_units] -= self.config.competing_context_penalty

        if self.config.lingering_activity_penalty > 0.0 and len(previous_active) > 0:
            stale = np.setdiff1d(previous_active, current_context_units, assume_unique=False)
            if len(stale) > 0:
                inhibited[stale] -= self.config.lingering_activity_penalty
        return inhibited
