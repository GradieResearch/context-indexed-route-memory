#!/usr/bin/env python3
"""Experiment 15: Minimal Neural Baseline Comparator.

Self-contained neural baseline suite for symbolic route-memory probes.
The full run is intentionally not executed by repository-maintenance agents.
"""
from __future__ import annotations

import argparse, dataclasses, json, math, os, platform, random, shutil, sqlite3, subprocess, sys, time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple

import numpy as np
import pandas as pd
import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset

# Tiny symbolic batches are faster and more predictable with one CPU thread.
torch.set_num_threads(max(1, int(os.environ.get("EXP15_TORCH_THREADS", "1"))))

SCHEMA_VERSION = "exp15_neural_metrics_v1"
NULL_CONTEXT_ID = 0

@dataclass(frozen=True)
class ProfileConfig:
    profile: str
    seeds: Tuple[int, ...]
    world_counts: Tuple[int, ...]
    route_lengths: Tuple[int, ...]
    routes_per_world: int
    modes: int
    suffix_min_length: int
    batch_size: int
    epochs: int
    learning_rate: float
    hidden_dim: int
    embedding_dim: int
    transformer_layers: int
    replay_buffer_worlds: int
    progress_every: int

@dataclass(frozen=True)
class VariantSpec:
    variant: str
    family: str
    model_kind: str
    training_regime: str
    context_available: bool
    replay_enabled: bool = False
    parameter_isolated: bool = False
    endpoint_model: bool = False
    sequence_model: bool = False
    transition_model: bool = False

VARIANTS: Tuple[VariantSpec, ...] = (
    VariantSpec("neural_gru_endpoint_context", "gru_endpoint", "gru_endpoint", "joint_endpoint", True, endpoint_model=True, sequence_model=True),
    VariantSpec("neural_gru_endpoint_no_context", "gru_endpoint", "gru_endpoint", "joint_endpoint", False, endpoint_model=True, sequence_model=True),
    VariantSpec("neural_gru_rollout_context", "gru_rollout", "gru_rollout", "joint_transition_rollout", True, sequence_model=True, transition_model=True),
    VariantSpec("neural_gru_rollout_no_context", "gru_rollout", "gru_rollout", "joint_transition_rollout", False, sequence_model=True, transition_model=True),
    VariantSpec("neural_transformer_sequence_context", "transformer_sequence", "transformer_endpoint", "joint_endpoint", True, endpoint_model=True, sequence_model=True),
    VariantSpec("neural_transition_mlp_context", "transition_mlp", "transition_mlp", "joint_transition", True, transition_model=True),
    VariantSpec("neural_transition_mlp_no_context", "transition_mlp", "transition_mlp", "joint_transition", False, transition_model=True),
    VariantSpec("neural_transition_mlp_replay_context", "replay_transition_mlp", "transition_mlp", "sequential_worlds_with_replay", True, replay_enabled=True, transition_model=True),
    VariantSpec("neural_transition_mlp_world_heads_context", "parameter_isolated_transition_mlp", "world_head_transition_mlp", "world_specific_heads", True, parameter_isolated=True, transition_model=True),
)
REQUIRED_VARIANTS = tuple(v.variant for v in VARIANTS)

@dataclass(frozen=True)
class RouteWorld:
    seed: int
    world_count: int
    route_length: int
    routes_per_world: int
    modes: int
    node_count: int
    transition_examples: Tuple[Dict[str, Any], ...]
    route_examples: Tuple[Dict[str, Any], ...]
    suffix_examples: Tuple[Dict[str, Any], ...]
    first_step_examples: Tuple[Dict[str, Any], ...]
    @property
    def context_count(self) -> int:
        return self.world_count + 1

def make_config(profile: str, progress_every: Optional[int] = None) -> ProfileConfig:
    profile = profile.lower().strip()
    if profile == "smoke":
        cfg = ProfileConfig("smoke", (0,), (2,), (4,), 4, 4, 2, 16, 3, 3e-3, 32, 24, 1, 2, 1)
    elif profile == "validation":
        cfg = ProfileConfig("validation", (0, 1), (2, 8), (4, 8), 6, 4, 2, 32, 8, 2e-3, 48, 32, 1, 2, 10)
    elif profile == "full":
        cfg = ProfileConfig("full", tuple(range(10)), (2, 8, 16, 32), (4, 8, 12), 12, 4, 2, 64, 20, 1.5e-3, 64, 48, 2, 3, 25)
    else:
        raise ValueError("profile must be smoke, validation, or full")
    return dataclasses.replace(cfg, progress_every=max(1, int(progress_every))) if progress_every else cfg

def stable_seed(*parts: Any) -> int:
    total = 0
    for b in "|".join(str(p) for p in parts).encode("utf-8"):
        total = (total * 131 + b) % (2**31 - 1)
    return total

def set_seeds(seed: int) -> None:
    random.seed(seed); np.random.seed(seed % (2**32 - 1)); torch.manual_seed(seed)
    if torch.cuda.is_available(): torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True; torch.backends.cudnn.benchmark = False

def make_route_world(seed: int, world_count: int, route_length: int, routes_per_world: int, modes: int, suffix_min_length: int) -> RouteWorld:
    rng = random.Random(stable_seed("exp15", seed, world_count, route_length, routes_per_world, modes))
    start_offset, cont_offset = 1, 1 + routes_per_world + 10
    node_count = cont_offset + world_count * routes_per_world * route_length + 10
    route_modes = {}
    for rid in range(routes_per_world):
        seq = tuple(rng.randrange(modes) for _ in range(route_length))
        if route_length > 1 and len(set(seq)) == 1: seq = tuple((seq[i] + i) % modes for i in range(route_length))
        route_modes[rid] = seq
    transitions, routes, suffixes, first_steps = [], [], [], []
    split_id = f"seed{seed}_w{world_count}_l{route_length}_rpw{routes_per_world}"
    for world in range(world_count):
        ctx = world + 1
        for rid in range(routes_per_world):
            start = start_offset + rid
            path = [start] + [cont_offset + world * routes_per_world * route_length + rid * route_length + step for step in range(route_length)]
            seq = route_modes[rid]
            routes.append({"seed": seed, "world": world, "context_id": ctx, "route_id": rid, "start": start, "modes": seq, "target": path[-1], "route_length": route_length, "probe_type": "seen_route", "split_id": split_id, "is_train_seen_full_route": True, "is_suffix_holdout": False})
            for step, mode in enumerate(seq):
                ex = {"seed": seed, "world": world, "context_id": ctx, "route_id": rid, "source": path[step], "mode": int(mode), "target": path[step+1], "step": step, "route_length": route_length, "probe_type": "transition", "split_id": split_id, "is_train_seen_full_route": True, "is_suffix_holdout": False}
                transitions.append(ex)
                if step == 0:
                    fs = dict(ex); fs["probe_type"] = "first_step_context_conflict"; first_steps.append(fs)
            for suffix_start in range(1, max(1, route_length - 1)):
                modes_suffix = seq[suffix_start:]
                if len(modes_suffix) < suffix_min_length: continue
                suffixes.append({"seed": seed, "world": world, "context_id": ctx, "route_id": rid, "start": path[suffix_start], "modes": modes_suffix, "target": path[-1], "route_length": len(modes_suffix), "parent_route_length": route_length, "suffix_start_step": suffix_start, "probe_type": "suffix_route", "split_id": split_id, "is_train_seen_full_route": False, "is_suffix_holdout": True})
    return RouteWorld(seed, world_count, route_length, routes_per_world, modes, node_count, tuple(transitions), tuple(routes), tuple(suffixes), tuple(first_steps))

class TransitionDataset(Dataset):
    def __init__(self, examples: Sequence[Dict[str, Any]], context_available: bool): self.examples=list(examples); self.context_available=context_available
    def __len__(self): return len(self.examples)
    def __getitem__(self, i):
        ex = self.examples[i]; ctx = int(ex["context_id"]) if self.context_available else NULL_CONTEXT_ID
        return torch.tensor(int(ex["source"])), torch.tensor(int(ex["mode"])), torch.tensor(ctx), torch.tensor(int(ex["target"]))

class RouteDataset(Dataset):
    def __init__(self, examples: Sequence[Dict[str, Any]], context_available: bool, max_len: int, step_targets: bool=False):
        self.examples=list(examples); self.context_available=context_available; self.max_len=max_len; self.step_targets=step_targets
    def __len__(self): return len(self.examples)
    def __getitem__(self, i):
        ex = self.examples[i]; modes=list(ex["modes"]); ctx=int(ex["context_id"]) if self.context_available else NULL_CONTEXT_ID
        item = {"start": torch.tensor(int(ex["start"])), "modes": torch.tensor(modes + [0]*(self.max_len-len(modes))), "length": torch.tensor(len(modes)), "context_id": torch.tensor(ctx), "target": torch.tensor(int(ex["target"]))}
        if self.step_targets:
            item["step_targets"] = torch.tensor(list(ex["step_targets"]) + [-100]*(self.max_len-len(modes)))
            item["step_sources"] = torch.tensor(list(ex["step_sources"]) + [0]*(self.max_len-len(modes)))
        return item

class TransitionMLP(nn.Module):
    def __init__(self, node_count, mode_count, context_count, emb, hid):
        super().__init__(); self.se=nn.Embedding(node_count+1, emb); self.me=nn.Embedding(mode_count+1, emb); self.ce=nn.Embedding(context_count+1, emb)
        self.net=nn.Sequential(nn.Linear(emb*3,hid),nn.ReLU(),nn.Linear(hid,hid),nn.ReLU(),nn.Linear(hid,node_count+1))
    def forward(self, source, mode, context_id): return self.net(torch.cat([self.se(source), self.me(mode), self.ce(context_id)], dim=-1))

class WorldHeadTransitionMLP(nn.Module):
    def __init__(self, node_count, mode_count, world_count, emb, hid):
        super().__init__(); self.node_count=node_count; self.world_count=world_count; self.se=nn.Embedding(node_count+1, emb); self.me=nn.Embedding(mode_count+1, emb); self.shared=nn.Sequential(nn.Linear(emb*2,hid),nn.ReLU(),nn.Linear(hid,hid),nn.ReLU()); self.heads=nn.ModuleList([nn.Linear(hid,node_count+1) for _ in range(world_count)])
    def forward(self, source, mode, context_id):
        h=self.shared(torch.cat([self.se(source), self.me(mode)], dim=-1)); out=torch.empty((source.shape[0], self.node_count+1), device=h.device, dtype=h.dtype); worlds=torch.clamp(context_id-1,0,self.world_count-1)
        for w in range(self.world_count):
            m=worlds==w
            if m.any(): out[m]=self.heads[w](h[m])
        return out

class GRUEndpointModel(nn.Module):
    def __init__(self, node_count, mode_count, context_count, emb, hid):
        super().__init__(); self.se=nn.Embedding(node_count+1,emb); self.me=nn.Embedding(mode_count+1,emb); self.ce=nn.Embedding(context_count+1,emb); self.gru=nn.GRU(emb*2,hid,batch_first=True); self.out=nn.Linear(hid+emb,node_count+1)
    def forward(self,start,modes,length,context_id):
        st=self.se(start); seq=torch.cat([st.unsqueeze(1).expand(-1,modes.shape[1],-1), self.me(modes)], dim=-1); packed=nn.utils.rnn.pack_padded_sequence(seq, length.cpu(), batch_first=True, enforce_sorted=False); _,h=self.gru(packed); return self.out(torch.cat([h[-1], self.ce(context_id)], dim=-1))

class GRURolloutModel(nn.Module):
    def __init__(self, node_count, mode_count, context_count, emb, hid):
        super().__init__(); self.se=nn.Embedding(node_count+1,emb); self.me=nn.Embedding(mode_count+1,emb); self.ce=nn.Embedding(context_count+1,emb); self.gru=nn.GRU(emb*3,hid,batch_first=True); self.out=nn.Linear(hid,node_count+1)
    def forward(self, step_sources, modes, context_id):
        ctx=self.ce(context_id).unsqueeze(1).expand(-1,modes.shape[1],-1); h,_=self.gru(torch.cat([self.se(step_sources), self.me(modes), ctx], dim=-1)); return self.out(h)
    def predict_next(self, source, mode, context_id): return self.forward(source.view(1,1), mode.view(1,1), context_id.view(1))[0,0]

class TinyAttentionBlock(nn.Module):
    def __init__(self, emb, hid):
        super().__init__(); self.q=nn.Linear(emb,emb); self.k=nn.Linear(emb,emb); self.v=nn.Linear(emb,emb); self.p=nn.Linear(emb,emb); self.n1=nn.LayerNorm(emb); self.ff=nn.Sequential(nn.Linear(emb,hid),nn.ReLU(),nn.Linear(hid,emb)); self.n2=nn.LayerNorm(emb); self.scale=math.sqrt(float(emb))
    def forward(self,x):
        w=torch.softmax(torch.matmul(self.q(x), self.k(x).transpose(-1,-2))/self.scale, dim=-1); x=self.n1(x+self.p(torch.matmul(w,self.v(x)))); return self.n2(x+self.ff(x))

class TransformerEndpointModel(nn.Module):
    def __init__(self, node_count, mode_count, context_count, emb, hid, layers, max_len):
        super().__init__(); self.se=nn.Embedding(node_count+1,emb); self.me=nn.Embedding(mode_count+1,emb); self.ce=nn.Embedding(context_count+1,emb); self.pe=nn.Embedding(max_len+2,emb); self.blocks=nn.ModuleList([TinyAttentionBlock(emb,hid) for _ in range(layers)]); self.out=nn.Linear(emb,node_count+1)
    def forward(self,start,modes,length,context_id):
        b,L=modes.shape; pos=torch.arange(L+2,device=modes.device).unsqueeze(0).expand(b,-1); x=torch.cat([self.ce(context_id).unsqueeze(1), self.se(start).unsqueeze(1), self.me(modes)], dim=1)+self.pe(pos)
        for block in self.blocks: x=block(x)
        return self.out(x[:,0,:])

def build_model(spec: VariantSpec, world: RouteWorld, cfg: ProfileConfig) -> nn.Module:
    ctx_count = world.context_count if spec.context_available else 1
    if spec.model_kind == "transition_mlp": return TransitionMLP(world.node_count, cfg.modes, ctx_count, cfg.embedding_dim, cfg.hidden_dim)
    if spec.model_kind == "world_head_transition_mlp": return WorldHeadTransitionMLP(world.node_count, cfg.modes, world.world_count, cfg.embedding_dim, cfg.hidden_dim)
    if spec.model_kind == "gru_endpoint": return GRUEndpointModel(world.node_count, cfg.modes, ctx_count, cfg.embedding_dim, cfg.hidden_dim)
    if spec.model_kind == "gru_rollout": return GRURolloutModel(world.node_count, cfg.modes, ctx_count, cfg.embedding_dim, cfg.hidden_dim)
    if spec.model_kind == "transformer_endpoint": return TransformerEndpointModel(world.node_count, cfg.modes, ctx_count, cfg.embedding_dim, cfg.hidden_dim, cfg.transformer_layers, world.route_length)
    raise ValueError(spec.model_kind)

def attach_step_targets(world: RouteWorld) -> List[Dict[str, Any]]:
    table={(ex["world"],ex["source"],ex["mode"]): ex["target"] for ex in world.transition_examples}; out=[]
    for route in world.route_examples:
        cur=int(route["start"]); sources=[]; targets=[]
        for mode in route["modes"]:
            sources.append(cur); cur=int(table[(route["world"],cur,int(mode))]); targets.append(cur)
        r=dict(route); r["step_sources"]=tuple(sources); r["step_targets"]=tuple(targets); out.append(r)
    return out

def train_transition_model(model, examples, spec, cfg, device, sequential_worlds=False):
    t=time.time(); model.to(device); opt=torch.optim.Adam(model.parameters(), lr=cfg.learning_rate); loss_fn=nn.CrossEntropyLoss(); seen=0
    batches=[]
    if sequential_worlds:
        by_world={}
        for ex in examples: by_world.setdefault(int(ex["world"]),[]).append(ex)
        replay=[]
        for w in sorted(by_world):
            batches.append(list(by_world[w])+replay); replay.extend(by_world[w]); replay=[e for e in replay if int(e["world"])>=max(0,w-cfg.replay_buffer_worlds+1)]
    else: batches=[list(examples)]
    for examples_batch in batches:
        loader=DataLoader(TransitionDataset(examples_batch, spec.context_available), batch_size=cfg.batch_size, shuffle=True)
        for _ in range(cfg.epochs):
            for source,mode,ctx,target in loader:
                opt.zero_grad(set_to_none=True); loss=loss_fn(model(source.to(device),mode.to(device),ctx.to(device)), target.to(device)); loss.backward(); opt.step(); seen += len(target)
    return {"training_seconds": time.time()-t, "train_examples_seen": seen}

def train_endpoint_model(model, examples, spec, cfg, device, step_targets=False):
    t=time.time(); model.to(device); opt=torch.optim.Adam(model.parameters(), lr=cfg.learning_rate); loss_fn=nn.CrossEntropyLoss(ignore_index=-100); max_len=max(int(e["route_length"]) for e in examples); loader=DataLoader(RouteDataset(examples, spec.context_available, max_len, step_targets), batch_size=cfg.batch_size, shuffle=True); seen=0
    for _ in range(cfg.epochs):
        for batch in loader:
            opt.zero_grad(set_to_none=True)
            if step_targets:
                logits=model(batch["step_sources"].to(device), batch["modes"].to(device), batch["context_id"].to(device)); loss=loss_fn(logits.reshape(-1,logits.shape[-1]), batch["step_targets"].to(device).reshape(-1))
            else:
                logits=model(batch["start"].to(device), batch["modes"].to(device), batch["length"].to(device), batch["context_id"].to(device)); loss=loss_fn(logits,batch["target"].to(device))
            loss.backward(); opt.step(); seen += int(batch["target"].shape[0])
    return {"training_seconds": time.time()-t, "train_examples_seen": seen}

def pred_transition(model, spec, source, mode, ctx, device):
    model.eval(); ctx = ctx if spec.context_available else NULL_CONTEXT_ID
    with torch.no_grad():
        if isinstance(model, GRURolloutModel): logits=model.predict_next(torch.tensor(source,device=device), torch.tensor(mode,device=device), torch.tensor(ctx,device=device))
        else: logits=model(torch.tensor([source],device=device), torch.tensor([mode],device=device), torch.tensor([ctx],device=device))[0]
    return int(torch.argmax(logits).cpu().item())

def pred_endpoint(model, spec, start, modes, ctx, device):
    model.eval(); ctx = ctx if spec.context_available else NULL_CONTEXT_ID
    with torch.no_grad(): logits=model(torch.tensor([start],device=device), torch.tensor([list(modes)],device=device), torch.tensor([len(modes)],device=device), torch.tensor([ctx],device=device))[0]
    return int(torch.argmax(logits).cpu().item())

def acc(ok,total): return float(ok)/float(total) if total else float("nan")

def evaluate(model, spec, world, train_meta, cfg, device):
    t=time.time(); rows=[]
    def row(metric, value, n, probe):
        return {"experiment":"exp15","schema_version":SCHEMA_VERSION,"profile":cfg.profile,"seed":world.seed,"world_count":world.world_count,"route_length":world.route_length,"routes_per_world":world.routes_per_world,"modes":world.modes,"node_count":world.node_count,"variant":spec.variant,"variant_family":spec.family,"model_kind":spec.model_kind,"training_regime":spec.training_regime,"context_available":spec.context_available,"replay_enabled":spec.replay_enabled,"parameter_isolated":spec.parameter_isolated,"endpoint_model":spec.endpoint_model,"sequence_model":spec.sequence_model,"transition_model":spec.transition_model,"metric_name":metric,"metric_value":value,"n_eval":n,"probe_type":probe,"split_id":f"seed{world.seed}_w{world.world_count}_l{world.route_length}_rpw{world.routes_per_world}","train_eval_split_metadata_present":True,"suffix_holdout_protocol":"suffix routes are composed from trained primitives but withheld as full-route endpoint examples","seen_full_routes_in_train":True,"suffix_routes_in_endpoint_train":False,"sequential_retention_eval":spec.training_regime.startswith("sequential"),"train_epochs":cfg.epochs,"train_examples_seen":train_meta.get("train_examples_seen",0),"training_seconds":train_meta.get("training_seconds",float("nan")),"eval_device":str(device),"status":"ok"}
    endpoint_only = spec.endpoint_model and not spec.transition_model
    def route_pred(route):
        if endpoint_only: return pred_endpoint(model,spec,int(route["start"]),route["modes"],int(route["context_id"]),device)
        cur=int(route["start"])
        for m in route["modes"]: cur=pred_transition(model,spec,cur,int(m),int(route["context_id"]),device)
        return cur
    trans_ok=0
    for ex in world.transition_examples:
        p = pred_endpoint(model,spec,int(ex["source"]),[int(ex["mode"])],int(ex["context_id"]),device) if endpoint_only else pred_transition(model,spec,int(ex["source"]),int(ex["mode"]),int(ex["context_id"]),device)
        trans_ok += int(p == int(ex["target"]))
    rows.append(row("transition_accuracy", acc(trans_ok,len(world.transition_examples)), len(world.transition_examples), "transition"))
    seen_ok=sum(int(route_pred(r)==int(r["target"])) for r in world.route_examples); rows.append(row("seen_route_composition_accuracy", acc(seen_ok,len(world.route_examples)), len(world.route_examples), "seen_route"))
    suffix_ok=sum(int(route_pred(r)==int(r["target"])) for r in world.suffix_examples); rows.append(row("suffix_route_composition_accuracy", acc(suffix_ok,len(world.suffix_examples)), len(world.suffix_examples), "suffix_route"))
    first_ok=0
    for ex in world.first_step_examples:
        p = pred_endpoint(model,spec,int(ex["source"]),[int(ex["mode"])],int(ex["context_id"]),device) if endpoint_only else pred_transition(model,spec,int(ex["source"]),int(ex["mode"]),int(ex["context_id"]),device)
        first_ok += int(p == int(ex["target"]))
    rows.append(row("first_step_context_conflict_accuracy", acc(first_ok,len(world.first_step_examples)), len(world.first_step_examples), "first_step_context_conflict"))
    rows.append(row("retention_after_sequential_worlds", float((acc(seen_ok,len(world.route_examples))+acc(suffix_ok,len(world.suffix_examples)))/2.0), len(world.route_examples)+len(world.suffix_examples), "retention"))
    eval_s=time.time()-t
    for r in rows: r["evaluation_seconds"]=eval_s; r["runtime_seconds"]=float(r["training_seconds"])+eval_s
    return rows, {"evaluation_seconds":eval_s}

def train_and_eval(world, spec, cfg, device):
    set_seeds(stable_seed("variant",world.seed,world.world_count,world.route_length,spec.variant)); model=build_model(spec,world,cfg)
    if spec.model_kind in ("gru_endpoint","transformer_endpoint"): train_meta=train_endpoint_model(model, world.route_examples, spec, cfg, device)
    elif spec.model_kind == "gru_rollout": train_meta=train_endpoint_model(model, attach_step_targets(world), spec, cfg, device, step_targets=True)
    else: train_meta=train_transition_model(model, world.transition_examples, spec, cfg, device, sequential_worlds=spec.replay_enabled)
    rows, emeta = evaluate(model,spec,world,train_meta,cfg,device)
    rt={"seed":world.seed,"world_count":world.world_count,"route_length":world.route_length,"variant":spec.variant,"variant_family":spec.family,"model_kind":spec.model_kind,"context_available":spec.context_available,"training_regime":spec.training_regime,"replay_enabled":spec.replay_enabled,"parameter_isolated":spec.parameter_isolated,"train_examples_seen":train_meta.get("train_examples_seen",0),"train_epochs":cfg.epochs,"training_seconds":train_meta.get("training_seconds",float("nan")),"evaluation_seconds":emeta["evaluation_seconds"],"runtime_seconds":train_meta.get("training_seconds",0.0)+emeta["evaluation_seconds"],"device":str(device)}
    return rows, rt

class ProgressLogger:
    def __init__(self,path,total,progress_every): self.path=path; self.total=max(1,total); self.every=max(1,progress_every); self.start=time.time(); self.done=0; self.last=0; path.parent.mkdir(parents=True,exist_ok=True); path.write_text("",encoding="utf-8")
    @staticmethod
    def fmt(s):
        if not math.isfinite(s): return "unknown"
        s=int(max(0,round(s))); h,rem=divmod(s,3600); m,sec=divmod(rem,60); return f"{h}h {m}m {sec}s" if h else (f"{m}m {sec}s" if m else f"{sec}s")
    def event(self,event,**payload):
        elapsed=time.time()-self.start; rate=self.done/max(elapsed,1e-9); eta=(self.total-self.done)/max(rate,1e-9) if self.done else float("nan")
        rec={"timestamp_utc":datetime.now(timezone.utc).isoformat(),"event":event,"completed_units":self.done,"total_units":self.total,"percent_complete":round(100*self.done/self.total,3),"elapsed_seconds":round(elapsed,3),"eta_seconds":None if not math.isfinite(eta) else round(eta,3),**payload}
        with self.path.open("a",encoding="utf-8") as f: f.write(json.dumps(rec,sort_keys=True)+"\n")
    def unit_done(self,**payload):
        self.done+=1; self.event("unit_complete",**payload); now=time.time(); elapsed=now-self.start; rate=self.done/max(elapsed,1e-9); eta=(self.total-self.done)/max(rate,1e-9)
        if self.done==1 or self.done%self.every==0 or self.done==self.total or now-self.last>15:
            self.last=now; print(f"[exp15] {self.done}/{self.total} ({100*self.done/self.total:5.1f}%) | seed={payload.get('seed')} variant={payload.get('variant')} world_count={payload.get('world_count')} route_length={payload.get('route_length')} | elapsed={self.fmt(elapsed)} | rate={rate:.3f} units/s | eta={self.fmt(eta)}", flush=True)

def choose_device(requested): return torch.device("cuda" if requested in ("auto","cuda") and torch.cuda.is_available() else "cpu")

def hardware(device):
    try:
        import psutil; ram=round(psutil.virtual_memory().total/(1024**3),3)
    except Exception: ram=None
    def git(args):
        try: return subprocess.check_output(["git",*args],text=True,stderr=subprocess.DEVNULL).strip()
        except Exception: return None
    return {"python_version":sys.version.replace("\n"," "),"platform":platform.platform(),"processor":platform.processor(),"cpu_count":os.cpu_count(),"ram_gb":ram,"gpu_available":torch.cuda.is_available(),"gpu_name":torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,"cuda_version":torch.version.cuda,"torch_version":torch.__version__,"numpy_version":np.__version__,"pandas_version":pd.__version__,"device_selected":str(device),"git_commit":git(["rev-parse","HEAD"]),"git_branch":git(["rev-parse","--abbrev-ref","HEAD"]),"command":" ".join(sys.argv)}

def write_sqlite(sqlite_path, metrics, runtime, manifest):
    sqlite_path.parent.mkdir(parents=True,exist_ok=True)
    with sqlite3.connect(sqlite_path) as con:
        pd.DataFrame(metrics).to_sql("exp15_seed_metrics",con,if_exists="replace",index=False); pd.DataFrame(runtime).to_sql("exp15_model_runtime",con,if_exists="replace",index=False); pd.DataFrame([manifest]).to_sql("run_manifest",con,if_exists="replace",index=False)

def run(args):
    cfg=make_config(args.profile,args.progress_every); device=choose_device(args.device); start=datetime.now(timezone.utc); run_id=f"exp15_{cfg.profile}_{start.strftime('%Y%m%d_%H%M%S')}"; base=Path(__file__).resolve().parent; run_dir=base/"analysis"/run_id; run_dir.mkdir(parents=True,exist_ok=False)
    cfg_json=dataclasses.asdict(cfg); cfg_json.update({"seeds":list(cfg.seeds),"world_counts":list(cfg.world_counts),"route_lengths":list(cfg.route_lengths),"required_variants":list(REQUIRED_VARIANTS),"variant_specs":[dataclasses.asdict(v) for v in VARIANTS],"optional_neural_key_value_baseline_included":False,"optional_neural_key_value_baseline_reason":"Omitted to keep Exp15 bounded; add only if reviewers require a memory-augmented neural comparator.","train_eval_split_protocol":{"seen_full_routes":"used for endpoint training and seen-route evaluation","transition_examples":"used for transition/rollout training","suffix_routes":"withheld as full-route endpoint examples; composed from trained primitives only","first_step_context_conflict":"first transition of each shared-start route; requires context disambiguation"}})
    (run_dir/"exp15_config.json").write_text(json.dumps(cfg_json,indent=2,sort_keys=True),encoding="utf-8")
    total=len(cfg.seeds)*len(cfg.world_counts)*len(cfg.route_lengths)*len(VARIANTS); log=ProgressLogger(run_dir/"progress.jsonl",total,cfg.progress_every); log.event("run_start",profile=cfg.profile,run_id=run_id,device=str(device),total_units=total)
    metrics=[]; runtime=[]; print(f"Experiment 15 neural baseline comparator | run_id={run_id} | profile={cfg.profile} | device={device}\nUnits: {total}")
    for seed in cfg.seeds:
        for wc in cfg.world_counts:
            for rl in cfg.route_lengths:
                world=make_route_world(seed,wc,rl,cfg.routes_per_world,cfg.modes,cfg.suffix_min_length)
                for spec in VARIANTS:
                    u=time.time(); rows, rt = train_and_eval(world,spec,cfg,device)
                    for r in rows: r["run_id"]=run_id
                    rt["run_id"]=run_id; metrics.extend(rows); runtime.append(rt); log.unit_done(seed=seed,world_count=wc,route_length=rl,variant=spec.variant,training_regime=spec.training_regime,context_available=spec.context_available,replay_enabled=spec.replay_enabled,parameter_isolated=spec.parameter_isolated,unit_seconds=round(time.time()-u,3))
    pd.DataFrame(metrics).to_csv(run_dir/"exp15_seed_metrics.csv",index=False); pd.DataFrame(metrics).to_csv(run_dir/"metrics.csv",index=False); pd.DataFrame(runtime).to_csv(run_dir/"exp15_model_runtime.csv",index=False)
    end=datetime.now(timezone.utc); manifest={"experiment":"exp15_neural_baseline_comparator","run_id":run_id,"profile":cfg.profile,"schema_version":SCHEMA_VERSION,"start_time_utc":start.isoformat(),"end_time_utc":end.isoformat(),"duration_seconds":(end-start).total_seconds(),"analysis_dir":str(run_dir),"metric_rows":len(metrics),"runtime_rows":len(runtime),"requested_seeds":list(cfg.seeds),"completed_seeds":sorted(pd.DataFrame(metrics)["seed"].unique().tolist()),"requested_world_counts":list(cfg.world_counts),"requested_route_lengths":list(cfg.route_lengths),"requested_variants":list(REQUIRED_VARIANTS),"completed_variants":sorted(pd.DataFrame(metrics)["variant"].unique().tolist()),"full_profile_note":"Minimal manuscript-facing neural comparator; not an architecture search.",**hardware(device)}
    if not args.no_sqlite:
        sqlite_path=base/"runs"/f"{run_id}.sqlite3"; write_sqlite(sqlite_path,metrics,runtime,manifest); manifest["sqlite_path"]=str(sqlite_path)
    (run_dir/"run_manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True),encoding="utf-8"); log.event("run_complete",run_id=run_id,metric_rows=len(metrics),runtime_rows=len(runtime)); print(f"\nExp15 run complete. Raw artifacts written to: {run_dir}\nNext: python analyze_experiment15.py --analysis-root analysis")
    return run_dir

def parse_args(argv=None):
    p=argparse.ArgumentParser(description="Run Experiment 15 neural baseline comparator."); p.add_argument("--profile",choices=("smoke","validation","full"),default="smoke"); p.add_argument("--device",choices=("auto","cpu","cuda"),default="auto"); p.add_argument("--progress-every",type=int,default=None); p.add_argument("--no-sqlite",action="store_true"); return p.parse_args(argv)

def main(argv=None): run(parse_args(argv)); return 0
if __name__ == "__main__": raise SystemExit(main())
