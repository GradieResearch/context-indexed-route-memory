#!/usr/bin/env python3
"""Validate Experiment 15 neural baseline comparator artifacts."""
from __future__ import annotations

import argparse, json, math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Sequence
import pandas as pd

REQUIRED_SOURCE_FILES=("README.md","run_experiment15.py","analyze_experiment15.py","validate_experiment15.py","start_exp15_validation.ps1","start_exp15_full.ps1")
REQUIRED_VARIANTS=("neural_gru_endpoint_context","neural_gru_endpoint_no_context","neural_gru_rollout_context","neural_gru_rollout_no_context","neural_transformer_sequence_context","neural_transition_mlp_context","neural_transition_mlp_no_context","neural_transition_mlp_replay_context","neural_transition_mlp_world_heads_context")
REQUIRED_METRICS=("transition_accuracy","seen_route_composition_accuracy","suffix_route_composition_accuracy","first_step_context_conflict_accuracy","retention_after_sequential_worlds")
REQUIRED_ARTIFACTS=("run_manifest.json","exp15_config.json","progress.jsonl","exp15_seed_metrics.csv","metrics.csv","exp15_summary.csv","exp15_effect_sizes.csv","exp15_model_runtime.csv","exp15_report.md","experiment_report.md","plots/exp15_seen_vs_suffix_composition.png","plots/exp15_context_conflict_accuracy.png","plots/exp15_retention_after_sequential_worlds.png","plots/exp15_route_length_scaling.png","plots/exp15_world_count_scaling.png")
REQUIRED_MANIFEST_FIELDS=("python_version","platform","processor","cpu_count","ram_gb","gpu_available","gpu_name","cuda_version","torch_version","numpy_version","start_time_utc","end_time_utc","duration_seconds","git_commit","git_branch","command","profile","requested_seeds","completed_seeds","requested_variants","completed_variants")

@dataclass
class Check:
    level: str
    name: str
    message: str

class Validator:
    def __init__(self): self.results: List[Check]=[]
    def add(self,level,name,msg): self.results.append(Check(level,name,msg))
    def pass_(self,name,msg): self.add("PASS",name,msg)
    def warn(self,name,msg): self.add("WARN",name,msg)
    def fail(self,name,msg): self.add("FAIL",name,msg)
    def expect(self,cond,name,ok,bad): self.pass_(name,ok) if cond else self.fail(name,bad)
    def counts(self): return {k:sum(1 for r in self.results if r.level==k) for k in ("PASS","WARN","FAIL")}

def latest(root: Path) -> Path:
    runs=sorted([p for p in root.glob("exp15_*") if p.is_dir()], key=lambda p:p.stat().st_mtime, reverse=True)
    if not runs: raise FileNotFoundError(f"No exp15_* directories found under {root}")
    return runs[0]

def valid_values(series: pd.Series) -> bool:
    vals=pd.to_numeric(series,errors="coerce")
    return bool(vals.notna().all() and vals.apply(math.isfinite).all() and ((vals>=0)&(vals<=1)).all())

def validate_source(exp_dir: Path, v: Validator):
    for f in REQUIRED_SOURCE_FILES:
        v.expect((exp_dir/f).exists(), f"source_file:{f}", f"Found {f}.", f"Missing expected source file {f}.")

def validate_run(run_dir: Path, v: Validator):
    for f in REQUIRED_ARTIFACTS:
        v.expect((run_dir/f).exists(), f"artifact:{f}", f"Found {f}.", f"Missing expected artifact {f}.")
    manifest_path=run_dir/"run_manifest.json"; config_path=run_dir/"exp15_config.json"; metrics_path=run_dir/"exp15_seed_metrics.csv"; summary_path=run_dir/"exp15_summary.csv"; runtime_path=run_dir/"exp15_model_runtime.csv"
    if not manifest_path.exists() or not metrics_path.exists(): return
    manifest=json.loads(manifest_path.read_text(encoding="utf-8")); config=json.loads(config_path.read_text(encoding="utf-8")) if config_path.exists() else {}; metrics=pd.read_csv(metrics_path); summary=pd.read_csv(summary_path) if summary_path.exists() else pd.DataFrame(); runtime=pd.read_csv(runtime_path) if runtime_path.exists() else pd.DataFrame()
    missing=[f for f in REQUIRED_MANIFEST_FIELDS if f not in manifest]
    v.expect(not missing,"manifest:required_fields","Runtime/hardware manifest fields are present.",f"Manifest missing required fields: {missing}")
    observed=set(metrics.get("variant",pd.Series(dtype=str)).dropna().unique().tolist()); missing_variants=sorted(set(REQUIRED_VARIANTS)-observed)
    v.expect(not missing_variants,"metrics:required_variants","All required variants are present in seed metrics.",f"Missing required variants: {missing_variants}")
    observed_metrics=set(metrics.get("metric_name",pd.Series(dtype=str)).dropna().unique().tolist()); missing_metrics=sorted(set(REQUIRED_METRICS)-observed_metrics)
    v.expect(not missing_metrics,"metrics:required_metric_names","All required metric names are present.",f"Missing required metric names: {missing_metrics}")
    v.expect("metric_value" in metrics.columns and valid_values(metrics["metric_value"]),"metrics:valid_range","All metric values are finite and within [0, 1].","Metric values contain NaN, infinity, or values outside [0, 1].")
    req=set(manifest.get("requested_seeds",[])); comp=set(manifest.get("completed_seeds",[])); obs=set(metrics.get("seed",pd.Series(dtype=int)).dropna().astype(int).unique().tolist()) if "seed" in metrics.columns else set()
    v.expect(req==comp==obs,"seeds:all_requested_completed","All requested seeds completed and are present in metrics.",f"Seed mismatch. requested={sorted(req)}, completed={sorted(comp)}, observed={sorted(obs)}")
    for col in ("split_id","train_eval_split_metadata_present","suffix_holdout_protocol"):
        v.expect(col in metrics.columns and metrics[col].notna().all(), f"split_metadata:{col}", f"Split metadata column {col} exists and is populated.", f"Split metadata column {col} missing or contains null values.")
    probes=set(metrics.get("probe_type",pd.Series(dtype=str)).dropna().unique().tolist())
    v.expect({"seen_route","suffix_route"}.issubset(probes),"probe_type:seen_suffix_distinguishable","Seen full-route and suffix probes are explicitly distinguishable.",f"Probe types do not include both seen_route and suffix_route: {sorted(probes)}")
    if "context_available" in metrics.columns:
        cv=set(metrics["context_available"].dropna().astype(str).str.lower().unique().tolist())
        v.expect({"true","false"}.issubset(cv),"config:context_vs_no_context","Context and no-context variants are distinguishable in config columns.",f"Expected true and false context_available; observed {sorted(cv)}")
    else: v.fail("config:context_vs_no_context","context_available column is missing.")
    for col, name in (("replay_enabled","config:replay_recorded"),("parameter_isolated","config:parameter_isolation_recorded")):
        if col not in metrics.columns: v.fail(name, f"{col} column is missing.")
        else:
            vals=set(metrics[col].dropna().astype(str).str.lower().unique().tolist())
            v.expect("true" in vals, name, f"{col} explicitly records true for at least one variant.", f"{col} never records true; observed {sorted(vals)}")
    if summary.empty: v.fail("summary:nonempty","exp15_summary.csv is missing or empty.")
    else:
        v.pass_("summary:nonempty",f"Summary contains {len(summary)} rows."); missing_cols=sorted({"mean","sd","sem","ci95","n_seeds"}-set(summary.columns)); v.expect(not missing_cols,"summary:statistical_columns","Summary contains mean/sd/sem/ci95/n_seeds columns.",f"Summary missing statistical columns: {missing_cols}")
    if runtime.empty: v.fail("runtime:nonempty","exp15_model_runtime.csv is missing or empty.")
    else:
        v.pass_("runtime:nonempty",f"Runtime table contains {len(runtime)} rows.")
        for col in ("training_seconds","evaluation_seconds","runtime_seconds","device"): v.expect(col in runtime.columns, f"runtime:{col}", f"Runtime column {col} exists.", f"Runtime column {col} is missing.")
    if config:
        protocol=config.get("train_eval_split_protocol",{})
        v.expect("suffix_routes" in protocol,"config:suffix_protocol_documented","Config documents suffix holdout protocol.","Config does not document suffix holdout protocol.")
        v.expect(config.get("optional_neural_key_value_baseline_included") is False,"config:optional_kv_decision_recorded","Optional neural key-value baseline omission is explicitly recorded.","Optional neural key-value decision is not recorded as false.")

def write_report(run_dir: Path, v: Validator):
    counts=v.counts(); lines=["# Experiment 15 Validation Report","",f"Status: {'PASS' if counts['FAIL']==0 else 'FAIL'}","","## Counts","",f"- PASS: {counts['PASS']}",f"- WARN: {counts['WARN']}",f"- FAIL: {counts['FAIL']}","","## Checks",""]
    for r in v.results: lines.append(f"- **{r.level}** `{r.name}` — {r.message}")
    (run_dir/"validation_report.md").write_text("\n".join(lines)+"\n",encoding="utf-8"); (run_dir/"validation_results.json").write_text(json.dumps({"counts":counts,"results":[r.__dict__ for r in v.results]},indent=2,sort_keys=True),encoding="utf-8")

def parse_args(argv: Optional[Sequence[str]]=None):
    p=argparse.ArgumentParser(); p.add_argument("--analysis-root",default="analysis"); p.add_argument("--run-dir",default=None); p.add_argument("--source-only",action="store_true"); return p.parse_args(argv)

def main(argv: Optional[Sequence[str]]=None) -> int:
    args=parse_args(argv); exp_dir=Path(__file__).resolve().parent; v=Validator(); validate_source(exp_dir,v)
    run_dir=exp_dir if args.source_only else (Path(args.run_dir) if args.run_dir else latest(Path(args.analysis_root)))
    if not args.source_only: validate_run(run_dir,v)
    write_report(run_dir,v); c=v.counts(); print(f"Experiment 15 validation: PASS={c['PASS']} WARN={c['WARN']} FAIL={c['FAIL']}"); return 0 if c["FAIL"]==0 else 1
if __name__=="__main__": raise SystemExit(main())
