from __future__ import annotations

import io
import json
import logging
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterator, Mapping

import numpy as np
from sqlalchemy import DateTime, Float, ForeignKey, Integer, LargeBinary, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship, sessionmaker

logger = logging.getLogger(__name__)


class Base(DeclarativeBase):
    pass


class ExperimentRun(Base):
    __tablename__ = "experiment_runs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    run_name: Mapped[str] = mapped_column(String(256), nullable=False)
    config_json: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str] = mapped_column(String(64), nullable=False, default="running")
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    best_accuracy: Mapped[float | None] = mapped_column(Float, nullable=True)

    metrics: Mapped[list["MetricRecord"]] = relationship(back_populates="run")
    checkpoints: Mapped[list["CheckpointRecord"]] = relationship(back_populates="run")


class MetricRecord(Base):
    __tablename__ = "metric_records"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    run_id: Mapped[int] = mapped_column(ForeignKey("experiment_runs.id"), nullable=False)
    epoch: Mapped[int] = mapped_column(Integer, nullable=False)
    step: Mapped[int] = mapped_column(Integer, nullable=False)
    split: Mapped[str] = mapped_column(String(32), nullable=False)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    value: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    run: Mapped[ExperimentRun] = relationship(back_populates="metrics")


class CheckpointRecord(Base):
    __tablename__ = "checkpoint_records"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    run_id: Mapped[int] = mapped_column(ForeignKey("experiment_runs.id"), nullable=False)
    epoch: Mapped[int] = mapped_column(Integer, nullable=False)
    step: Mapped[int] = mapped_column(Integer, nullable=False)
    artifact_name: Mapped[str] = mapped_column(String(256), nullable=False)
    payload: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    run: Mapped[ExperimentRun] = relationship(back_populates="checkpoints")


class ExperimentStore:
    """Small SQLite-backed experiment store.

    Checkpoints are stored as compressed NumPy .npz blobs. This is not intended as
    the fastest storage layer for large models; it is a clear, inspectable starting
    point for experiments.
    """

    def __init__(self, database_path: Path):
        self.database_path = database_path
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        self.engine = create_engine(f"sqlite:///{database_path}", future=True)
        self.session_factory = sessionmaker(self.engine, expire_on_commit=False, future=True)

    def initialize(self) -> None:
        Base.metadata.create_all(self.engine)
        logger.info("Experiment database ready at %s", self.database_path)

    @contextmanager
    def session(self) -> Iterator[Session]:
        session = self.session_factory()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def create_run(self, run_name: str, config: Mapping[str, object]) -> int:
        with self.session() as session:
            run = ExperimentRun(
                run_name=run_name,
                config_json=json.dumps(config, indent=2, sort_keys=True),
                status="running",
                started_at=datetime.now(timezone.utc),
            )
            session.add(run)
            session.flush()
            logger.info("Created experiment run id=%s name=%s", run.id, run_name)
            return run.id

    def record_metric(self, run_id: int, epoch: int, step: int, split: str, name: str, value: float) -> None:
        with self.session() as session:
            session.add(
                MetricRecord(
                    run_id=run_id,
                    epoch=epoch,
                    step=step,
                    split=split,
                    name=name,
                    value=float(value),
                    created_at=datetime.now(timezone.utc),
                )
            )

    def save_checkpoint(
        self,
        run_id: int,
        epoch: int,
        step: int,
        artifact_name: str,
        arrays: Dict[str, np.ndarray],
    ) -> None:
        buffer = io.BytesIO()
        np.savez_compressed(buffer, **arrays)
        with self.session() as session:
            session.add(
                CheckpointRecord(
                    run_id=run_id,
                    epoch=epoch,
                    step=step,
                    artifact_name=artifact_name,
                    payload=buffer.getvalue(),
                    created_at=datetime.now(timezone.utc),
                )
            )
        logger.info("Saved checkpoint '%s' at epoch=%s step=%s", artifact_name, epoch, step)

    def complete_run(self, run_id: int, status: str, best_accuracy: float | None) -> None:
        with self.session() as session:
            run = session.get(ExperimentRun, run_id)
            if run is None:
                raise ValueError(f"Unknown run id {run_id}")
            run.status = status
            run.best_accuracy = best_accuracy
            run.completed_at = datetime.now(timezone.utc)
            logger.info("Completed run id=%s status=%s best_accuracy=%s", run_id, status, best_accuracy)
