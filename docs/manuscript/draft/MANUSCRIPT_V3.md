# Context-Indexed Structural Route Memory for Compositional Recall in Interfering Transition Systems

## Abstract

Route-memory systems can fail when identical local cues require different successors in different contexts. We study this pressure in a synthetic symbolic benchmark in which worlds define incompatible transition systems over shared state and action symbols. The benchmark separates four contracts that aggregate route accuracy can otherwise conflate: storage of one-step transitions, indexing by world or context, endpoint memorization, and recurrent execution of multi-step routes.

We evaluate Context-Indexed Route Memory as a family of symbolic route-memory mechanisms rather than as a universal brain model or a general neural architecture. Across the retained claim set, structural route storage, context/world indexing, and recurrent execution play distinct roles. Removing structural route storage collapses route-table formation and route execution within the tested CIRM-family ablations. Removing recurrence can preserve one-step transition access while collapsing multi-step composition. Removing context separation fails conflict-sensitive first-step and full-route disambiguation, although suffix probes can remain misleadingly high when they bypass the conflicting transition.

Under clean supplied context, the full model maintains ceiling route-table and composition accuracy through the tested world counts. Under finite structural budget, route execution shows an observed degradation curve, but we do not fit or claim a general capacity law. A symbolic transition-cue setting reduces the oracle-context limitation by selecting the active symbolic world before route execution; this is not raw sensory latent-world discovery. Symbolic/algorithmic baselines and a minimal fixed-profile neural comparator sharpen the boundary of the claims. In particular, context-conditioned and world-head transition MLP variants solve the clean hard slice, so the evidence does not support broad CIRM-over-neural superiority.

The contribution is therefore a conservative benchmark and mechanism decomposition for symbolic route memory under contextual interference. The work does not establish solved continual learning, biological validation, exhaustive neural benchmarking, or end-to-end perceptual context discovery.

## 1. Introduction

Learning systems often need to preserve incompatible memories over a shared representational substrate. In continual-learning terms, this pressure is often described as catastrophic interference, where new information disrupts prior associations [McCloskeyCohen1989; French1999; Kirkpatrick2017]. In memory-augmented and context-conditioned systems, the same pressure can be framed as a retrieval and routing problem: a system must store the relevant information, retrieve the correct part of it, and execute behavior without mixing incompatible contexts [Graves2014; Graves2016; Weston2014; Sukhbaatar2015].

The route-memory benchmark studied here isolates a small but demanding version of this problem. A world defines a transition system over symbolic states. The same local state/action cue can map to different successors in different worlds. A model that stores transitions without context can overwrite or merge incompatible mappings. A model that memorizes full-route endpoints may succeed on seen complete routes while failing suffix probes that require reusable transition structure. A model that retrieves one-step transitions can still fail if it cannot feed each retrieved successor back into memory to execute a multi-step route.

This setting makes it possible to ask a narrower question than whether a system "has memory." It asks which part of a route-memory contract is being satisfied. The benchmark separates structural transition storage, context/world indexing, endpoint memorization, recurrent route execution, finite-budget pressure, and context selection. These mechanisms are not individually novel. Context gating, recurrence, structural plasticity, modular routing, and memory augmentation all have substantial prior art. The claim is instead that this benchmark exposes their separable roles under controlled symbolic interference.

The retained manuscript claims are deliberately bounded:

- C1: within this symbolic route-memory benchmark and tested CIRM-family ablations, structural route storage is required for reliable route-table formation and route execution.
- C2: context/world indexing is required for incompatible local transitions and conflict-sensitive first-step/full-route disambiguation, not for every suffix transition.
- C3: recurrent execution is required to compose stored one-step route memories into multi-step routes in the tested route-memory contracts.
- C4: route-table storage, endpoint memorization, and multi-step compositional execution are separable in this benchmark.
- C5: under clean supplied context, the full model maintains ceiling route-table and composition accuracy through the tested world counts.
- C6: finite structural budget produces an observed route-execution degradation curve.
- C13: the active symbolic world/context can be selected from partial symbolic transition-cue evidence before route execution.
- C12: symbolic/algorithmic baselines and a minimal fixed-profile neural comparator are present, but baseline coverage is non-exhaustive.

Equally important are the exclusions. The manuscript does not claim broad neural superiority, raw sensory latent-world discovery, biological validation, solved continual learning, inference of unseen primitive transitions, positive lesion evidence from Exp13.1, or a scientific interpretation of Exp15 replay collapse. Boundary evidence on local-versus-global budget pressure, consolidation, context/cue corruption, and continuous/noisy bridges remains supplementary or future-facing.

## 2. Background and Related Work

### 2.1 Interference, Memory, and Context

Continual learning studies how systems acquire new information while preserving prior capabilities. Regularization, replay, architectural expansion, parameter isolation, task inference, distillation, and hybrid methods all address forms of interference [Kirkpatrick2017; Zenke2017; Rebuffi2017; LopezPaz2017; vanDeVenTolias2019]. The present work is related to this literature, but it is not a broad continual-learning benchmark. It does not evaluate class-incremental recognition, domain-incremental perception, or open-ended task-free adaptation. It studies a controlled symbolic transition-memory problem.

Memory-augmented computation also provides important context. Neural Turing Machines, Differentiable Neural Computers, Memory Networks, End-to-End Memory Networks, Matching Networks, and transformer memory systems explore ways to read, write, retrieve, and reuse stored information [Graves2014; Graves2016; Weston2014; Sukhbaatar2015; Santoro2016; Vinyals2016]. CIRM is narrower than these systems. It uses explicit symbolic route-memory tables to make transition storage, indexing, and execution visible as separate experimental contracts.

Context-conditioned computation, modular routing, task masks, and latent-cause models are also directly relevant [Jacobs1991; JordanJacobs1994; Rusu2016; Fernando2017; Shazeer2017; GershmanNiv2010]. The manuscript therefore avoids claiming novelty for context gating itself. The relevant evidence is conflict-specific: when the generator deliberately creates incompatible local mappings, context/world indexing is needed for first-step and full-route disambiguation.

### 2.2 Recurrence, Structural Storage, and Composition

Fast weights, Hebbian mechanisms, Hopfield networks, and differentiable plasticity study systems whose effective memory structure can change rapidly [Hebb1949; Hopfield1982; HintonPlaut1987; Miconi2018; Miconi2019]. Compositional generalization and neural algorithmic reasoning ask whether learned systems can recombine known components into new executions [LakeBaroni2018; Hupkes2020]. The present benchmark is adjacent to both areas, but its claim is not that structural storage or recurrence is newly invented. The claim is that, within this route-memory task, one-step transition storage and multi-step route execution can be dissociated and measured separately.

This distinction matters because endpoint accuracy is not enough. A model can memorize the endpoint of a seen full route without learning reusable transition structure. A model can retrieve one-step transitions without executing a route. A model can execute suffixes correctly while still failing the context-sensitive first transition. V3 keeps these contracts separate rather than collapsing them into a single performance score.

### 2.3 Baseline Scope

The baseline posture changed after the fixed-profile neural comparator was added. The manuscript can no longer say that neural baselines are absent. It should instead say that baseline coverage is present but non-exhaustive. Symbolic/algorithmic baselines clarify that an oracle context-gated transition table can match the full model under clean supplied context. The neural comparator clarifies that conventional context-conditioned transition learning can also solve the clean hard slice. These controls narrow the contribution to benchmark decomposition and mechanism-sensitive measurement.

Citation details and bibliography convention remain citation-finalization pending. This draft preserves the placeholder citation style already used in the prior manuscript draft rather than inventing bibliography metadata.

## 3. Task and Benchmark Setup

The benchmark consists of symbolic worlds, shared state symbols, action or transition cues, and routes. Each world defines a one-step transition function. A route is generated by repeatedly applying the relevant world-specific transition. Interference appears when the same local cue has one successor in one world and a different successor in another.

The core supplied-context setting provides the active world label during storage or execution. This setting tests whether context-indexed storage can preserve incompatible transition systems, but it does not test latent world discovery. A separate symbolic transition-cue setting provides partial evidence about transitions in the active world and asks the system to select a symbolic context before route execution. This setting reduces the direct oracle-label assumption, but the cues remain symbolic.

The main probe families distinguish different contracts:

- Route-table accuracy measures one-step transition storage or retrieval.
- Composition accuracy measures multi-step route execution.
- Seen-route composition measures performance on complete routes already available to an endpoint memorization strategy.
- Suffix-route composition tests reusable route structure after removing the original first step.
- First-step context-conflict accuracy tests the deliberately ambiguous local transition at the beginning of a route.
- Retention after sequential worlds tests whether behavior persists after multiple worlds are introduced.
- World-selection accuracy measures whether a symbolic cue selector chooses the correct active world before execution.

Suffix probes require care. A no-context model can do well on suffixes when the suffix transitions no longer include the conflicting first step. Such success does not refute the need for context on incompatible local mappings; it shows why first-step and full-route conflict metrics must be reported separately.

## 4. Model and Method

Context-Indexed Route Memory stores one-step transition entries in a structure indexed by world or context. During route execution, the model repeatedly reads the next transition from the active context and feeds the retrieved successor into the next step. The mechanism is intentionally explicit: it is designed to expose the roles of storage, indexing, and recurrent execution rather than to hide them inside an aggregate model score.

The retained ablations remove or alter individual contracts. No-structural-storage variants test whether the model can form reliable route-table entries without the structural route memory used by the CIRM family. No-context or shared-lookup variants test whether incompatible local transitions can be kept apart without a world index. No-recurrence variants test whether local transition access is enough for multi-step route execution. Endpoint controls test whether full-route memorization can substitute for reusable transition composition.

The baseline suite includes symbolic and algorithmic controls, including oracle context-gated transition lookup and endpoint memorization controls. These are not defeated competitors. The oracle context-gated table is an upper-bound supplied-context control that helps isolate what is and is not novel in the clean label-provided regime.

The neural comparator is a minimal fixed-profile comparison suite. It includes endpoint sequence models, rollout sequence models, context-conditioned transition MLPs, no-context transition MLPs, a replay transition MLP variant, and a world-head transition MLP. The comparator is useful because it separates endpoint memorization, transition learning, context conflict, suffix behavior, and retention. It is not an exhaustive neural architecture search, and it omits memory-augmented or key-value neural baselines.

## 5. Experiments

The experiments are organized by claim rather than by historical run order.

### 5.1 Structural Storage, Context Indexing, and Recurrence

The core ablation experiments test C1-C4. They compare the full model with variants lacking structural storage, context binding, or recurrent execution. The manuscript-facing descriptive summary is Table 3, with Figure 2 as the candidate core ablation figure. These results are used only as benchmark/model-family-specific evidence.

### 5.2 Clean Supplied-Context Scaling

The clean scaling experiments test C5. They ask whether the full model maintains route-table and route-execution performance as the number of supplied-context worlds increases over the tested grid. These experiments are explicitly ceiling-limited. They do not fit a capacity law or justify extrapolation beyond the tested world counts.

### 5.3 Finite Structural Budget

The finite-budget experiments test C6. They reduce the available structural budget and measure the resulting route-execution degradation. The result is treated descriptively as an observed degradation curve. Local-versus-global pressure is relevant boundary evidence, but C7 is not promoted to a standalone central claim without paired seed-level analysis.

### 5.4 Symbolic Transition-Cue Context Selection

The context-selection experiments test C13. The model receives partial symbolic transition-cue evidence, selects an active world, and then executes routes with the selected context. The oracle context-gated lookup remains an upper-bound control, and cue corruption is treated as symbolic cue-evidence sensitivity rather than generic noise robustness.

### 5.5 Baselines and Neural Comparator

The baseline experiments support C12 and sharpen C1, C2, and C4. Symbolic/algorithmic baselines show that clean supplied-context accuracy can be matched by an oracle context-gated table. The fixed-profile neural comparator shows that context-conditioned transition MLP and world-head transition MLP variants solve the clean hard slice, while endpoint and no-context variants expose different failure modes. Table 4 is therefore a caveated comparator table, not broad evidence of CIRM superiority over neural models.

## 6. Results

The numeric results below are descriptive. They use the compact final-safe Table 3 and the source-data-backed Table 4. Effect-size language is not added because the retained comparison families remain under review.

### 6.1 Storage, Indexing, and Execution Dissociate

The full model reaches route-table and composition accuracy of 1.000 in the core symbolic ablation slice. Removing structural plasticity collapses both route-table accuracy and composition accuracy to 0.0286 and 0.0317, respectively. This supports C1 only within the symbolic benchmark and tested CIRM-family ablations; it does not imply that all possible neural route-memory systems require the same explicit structural storage mechanism.

The no-context-binding ablation separates another failure mode. In the same descriptive summary, no-context binding reaches route-table accuracy of 0.364 and composition accuracy of 0.0467. This supports C2 for incompatible local transitions and conflict-sensitive first-step or full-route disambiguation. It does not support the stronger claim that context is required for every suffix transition.

The no-recurrence-at-evaluation ablation preserves route-table accuracy at 1.000 while reducing composition accuracy to 0.0401. This supports C3: in the tested route-memory contracts, recurrent execution is required to compose stored one-step route memories into multi-step routes. The result is not a claim that recurrence itself is novel.

Together these results support C4. Route-table storage, endpoint memorization, and executable composition are separable. A model can store one-step transitions and fail route execution; another can memorize endpoints and fail reusable suffix composition; another can solve suffixes while failing conflict-sensitive first-step disambiguation. The benchmark is useful because these outcomes can be measured separately.

### 6.2 Clean Supplied-Context Scaling Is Ceiling-Limited

Under clean supplied context, route-table and composition accuracy remain 1.000 across the mirrored grid used for Figure 3, including world counts 2, 4, 8, 16, and 32 and route lengths 1, 2, 4, 8, and 12. This supports C5 as a ceiling result through the tested supplied-context range. It should not be read as a general capacity law, a statement about unsupplied context, or evidence about raw latent-context inference.

### 6.3 Finite Structural Budget Produces an Observed Degradation Curve

When structural budget is constrained in the global finite-budget slice at world_count 32 and route_length 12, composition accuracy rises from 0.276 at budget_ratio 0.25 to 0.517 at 0.50, 0.758 at 0.75, and 1.000 at exact or surplus budget levels. This supports C6 as an observed finite-budget degradation pattern. No fitted capacity law is claimed.

Local-versus-global budget pressure remains a boundary result. The available summaries suggest that local pressure can be more damaging than global pressure, but paired seed-level local/global analysis remains deferred. V3 therefore does not promote C7 into a central claim.

### 6.4 Symbolic Transition Cues Can Select Context Before Execution

In the symbolic transition-cue setting, the CIRM latent selector reaches 1.000 world-selection and seen-composition accuracy at corruption rates 0.00 and 0.10, 0.999 at 0.25, and 0.942 at 0.50 in the compact Table 3 slice. The oracle context-gated lookup remains at 1.000. Shared no-context lookup fails first-step and seen-route metrics near chance, while suffix probes can remain misleadingly high.

These results support C13 in narrow form: partial symbolic transition-cue evidence can select the active symbolic world before route execution. The result does not establish raw sensory latent-world discovery, end-to-end perception, or a general latent-cause inference model.

### 6.5 Baselines Narrow the Claim

The symbolic/algorithmic baseline suite shows that an oracle context-gated transition table matches the full model under clean supplied context. This is important because it prevents overclaiming: clean supplied-world accuracy is not by itself the novelty.

The fixed-profile neural comparator further narrows the claim boundary. In the hardest summarized Exp15 slice, the context-conditioned transition MLP reaches 1.000 across first-step context conflict, retention, seen-route composition, suffix-route composition, and transition accuracy. The world-head transition MLP also reaches 1.000 across the same reported metrics. These results rule out broad claims that neural transition learners cannot solve the clean symbolic transition-composition problem.

The same table shows why the benchmark decomposition remains informative. The endpoint GRU with context reaches 0.9990 seen-route composition but only 0.4040 suffix-route composition and 0.0232 transition accuracy, consistent with endpoint memorization rather than reusable transition learning. The no-context transition MLP reaches 1.000 suffix-route composition and 0.9193 transition accuracy but only 0.0312 first-step context-conflict accuracy and 0.0312 seen-route composition, showing why no-context suffix success must not be interpreted as full disambiguation. The replay variant is shown in Table 4 for completeness but remains a non-claim pending audit.

The correct C12 posture is therefore conservative: symbolic/algorithmic baselines and a minimal fixed-profile neural comparator are present, but baseline coverage is not exhaustive.

### 6.6 Boundary and Supplement Results

Several artifacts are relevant but not central. Local-versus-global budget pressure remains boundary evidence. Consolidation is treated as a stability-plasticity discussion, not as a necessary accuracy mechanism. Context or cue corruption is treated as wrong-world or symbolic cue-evidence sensitivity, not generic robustness. The continuous/noisy bridge remains preliminary and symbolic-decoder based, not end-to-end perception. Seen-versus-unseen primitive claims remain outside the central manuscript until metric cleanup exists.

## 7. Reproducibility and Evidence Traceability

The manuscript is tied to committed claim-scoped artifacts rather than to thread memory. The controlling traceability files are `docs/manuscript/MANUSCRIPT_REPRODUCIBILITY_MAP.md`, `docs/manuscript/source_data/manuscript_claim_artifact_map.csv`, `docs/manuscript/source_data/reproducibility_claim_summary.csv`, `docs/manuscript/source_data/seed_level_core_claim_metrics.csv`, and `docs/manuscript/tables/table_reproducibility_claim_summary.md`.

The descriptive manuscript tables are also committed. Compact Table 3 is `docs/manuscript/tables/table_03_compact_final_safe.md` with source data at `docs/manuscript/source_data/table_03_compact_final_safe.csv`. Table 4 is `docs/manuscript/tables/table_04_exp15_neural_comparator.md` with source data at `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`.

The current reproducibility protocol and reports are `docs/repo_audit/MANUSCRIPT_REPRODUCIBILITY_PROTOCOL.md`, `docs/repo_audit/MANUSCRIPT_REPRODUCIBILITY_REPORT.md`, and `docs/repo_audit/CLAIM_SCOPED_REPRODUCIBILITY_SUMMARY_REPORT.md`. The intended validation commands for this manuscript package are:

```bash
python scripts/verify_doc_source_paths.py
python scripts/reproduce_manuscript.py --profile validate-artifacts
```

These commands validate source-path discipline and committed artifact consistency. They do not rerun expensive experiments, overwrite historical outputs, or promote boundary/non-claim evidence into the retained manuscript claim set.

## 8. Limitations

The benchmark is synthetic and symbolic. This makes the mechanism contracts inspectable, but it limits claims about naturalistic perception, large-scale continual learning, and real-world navigation.

Many experiments use supplied context labels. The symbolic transition-cue experiment reduces this limitation by selecting a world from partial symbolic transition evidence, but it does not learn worlds from raw sensory input and does not solve general latent-cause discovery.

The neural comparator is minimal and fixed-profile. It uses small fixed models and hyperparameters, omits memory-augmented or key-value neural baselines, and should not be treated as exhaustive neural benchmarking. Because context-conditioned transition MLP and world-head transition MLP variants solve the clean hard slice, the manuscript does not claim broad neural inferiority.

No biological validation is provided. The mechanism can be described as computationally inspired by ideas such as indexing, remapping, recurrence, and structural storage, but the evidence is not biological and does not validate a hippocampal theory.

No fitted capacity law is claimed. The finite-budget experiments report an observed degradation curve only.

Boundary and supplement topics are not central claims. Local-versus-global pressure, consolidation, context/cue corruption, and continuous/noisy bridges remain caveated. Seen-versus-unseen primitive transition claims are excluded until metric cleanup is completed.

Several negative or ambiguous artifacts are not interpreted as positive evidence. Exp13.1 positive lesion evidence is excluded because the diagnostic pattern requires audit or rerun. Exp15 replay collapse is excluded as scientific evidence until implementation, training regime, and buffer details are audited.

Statistical reporting remains conservative. Compact Table 3 is used for descriptive manuscript wording, while final comparison-family and effect-size choices remain under review unless separately finalized.

## 9. Discussion

The results suggest that route memory under contextual interference is best evaluated by separating storage, indexing, endpoint recall, and execution. Aggregate route accuracy can hide the difference between a table that stores local transitions, a route endpoint memorizer, a recurrent executor, and a context selector. The benchmark makes these differences explicit.

The most stable interpretation is mechanistic and narrow. Within the tested symbolic route-memory contracts, structural route storage supports route-table formation, context/world indexing separates incompatible local mappings, and recurrence composes one-step memories into multi-step routes. Under supplied clean context, the full model reaches ceiling through the tested world counts; under finite budget, performance degrades descriptively as structural capacity is reduced.

The context-selection result changes the manuscript from a purely oracle-context story to a partly cue-selected one. However, the distinction remains important: selecting a symbolic world from transition cues is not the same as discovering latent worlds from raw sensory streams. The oracle context-gated table remains an upper-bound control.

The neural comparator also changes the manuscript in a constructive way. The paper does not need neural baselines to fail. Instead, the fixed-profile comparator shows that different contracts produce different behaviors. Endpoint models can memorize seen routes without learning reusable transition structure. No-context transition learning can succeed on suffixes while failing first-step/full-route disambiguation. Context-conditioned transition learners can solve the clean hard slice. These outcomes sharpen the benchmark contribution.

Future work should extend the comparator set with stronger memory-augmented or key-value neural baselines, broader hyperparameter searches where appropriate, and richer task families. Perceptual or continuous front ends should be treated as new evidence only when the system learns from such inputs directly. Statistical hardening should finalize comparison families before adding inferential effect-size language. Biological inspiration could motivate future experiments, but biological validation would require distinct evidence.

## 10. Conclusion

This draft presents Context-Indexed Route Memory as a conservative symbolic benchmark and mechanism decomposition. Within the tested route-memory setting, structural transition storage, context/world indexing, endpoint memorization, and recurrent multi-step execution are separable. Clean supplied-context behavior reaches ceiling through the tested world counts, finite structural budget produces an observed degradation curve, and symbolic transition cues can select the active world before route execution.

The contribution is intentionally narrow: a reviewer-facing account of how route storage, context disambiguation, and recurrent composition can be separated under incompatible symbolic transition systems. It is not a claim of broad neural superiority, biological validation, solved continual learning, or raw sensory latent-world discovery.
