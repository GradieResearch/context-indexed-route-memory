# Context-Indexed Structural Route Memory for Compositional Recall in Interfering Transition Systems

[DRAFT STATUS NOTE]

This is `MANUSCRIPT_V2`, integrated after Experiment 15 import and post-Exp15 claim hardening.

Intended repository path:

`docs/manuscript/draft/MANUSCRIPT_V2.md`

This draft is intentionally conservative. It frames the repository as a controlled symbolic/mechanistic benchmark and evidence map. It does **not** claim solved continual learning, broad neural-network superiority, raw sensory latent-world discovery, end-to-end perception, broad biological validation, or inference of unseen primitive transitions.

Controlling repository artifacts:

- `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`
- `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/manuscript/BASELINE_REQUIREMENTS.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/threads/experiment15_analysis_digest.md`
- `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`
- `docs/manuscript/tables/table_04_exp15_neural_comparator.md`
- `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`

Main V2 posture:

- The manuscript is a controlled symbolic/mechanistic benchmark paper.
- Exp15 is a minimal fixed-profile neural comparator, not an exhaustive neural benchmark.
- The "neural baselines are absent" limitation is no longer accurate.
- Broad CIRM-over-neural-model claims are not supported and should remain absent.
- A context-conditioned transition MLP and a world-head transition MLP solve the clean hard slice at ceiling across reported metrics.
- Endpoint neural baselines help separate endpoint memorization from reusable transition composition.
- No-context neural results support a conflict-specific context-indexing claim, not a blanket claim that context is required for every suffix transition.
- Exp14 supports symbolic transition-cue context selection, not raw sensory latent-world discovery.
- Exp15 replay collapse is not interpreted scientifically unless audited.

V2 placement decisions:

- Exp14 remains a main-narrow Figure 5 versus supplement decision.
- Exp15 is retained in V2 as compact main-text Table 4, with the option to move it to supplement during venue/journal formatting.
- Full Exp15 plots and implementation details should remain supplementary unless the target venue asks for broader neural-comparator detail.

Citation status:

This draft preserves manuscript-style citation placeholders from V1/local V2. Final submission still requires BibTeX verification, DOI/venue checks, and local prior-art/novelty import.

---

## Title options

1. Context-Indexed Structural Route Memory for Compositional Recall in Interfering Transition Systems
2. Storage, Context, and Execution in a Synthetic Route-Memory Benchmark
3. Context-Indexed Route Memory Separates Storage and Execution under Transition Interference
4. Recurrent Route Execution over Context-Indexed Transition Memory
5. A Controlled Benchmark for Structural Route Memory, Context Selection, and Compositional Recall

Working title:

**Context-Indexed Structural Route Memory for Compositional Recall in Interfering Transition Systems**

---

## Abstract

Memory systems operating under contextual interference must preserve different transition structures over a shared substrate. In route-memory tasks, the same local cue can imply different successors in different worlds, so a learner must distinguish between storing one-step transitions, remembering full-route endpoints, selecting the relevant context, and executing multi-step routes.

We study this problem in a controlled symbolic benchmark designed to separate route storage, context indexing, recurrent execution, capacity pressure, and context selection. The tested mechanism, Context-Indexed Route Memory, stores one-step transitions in context-indexed structural route tables and executes routes by recurrently applying the stored transition structure. Across manuscript-relevant experiments, removing structural route storage collapses route-table formation and multi-step route execution; removing recurrence can preserve one-step transition access while collapsing composition; and removing context separation causes failures on conflict-sensitive first-step and full-route probes.

Clean supplied-context scaling reaches ceiling accuracy through the tested world counts, while finite structural budget experiments produce an observed degradation curve rather than a fitted capacity law. A symbolic/algorithmic baseline suite shows that an oracle context-gated transition table matches the full model under clean supplied context, clarifying that clean performance with supplied world labels is not by itself the novelty claim. Endpoint memorization controls succeed on seen full routes while failing suffix-route composition, separating endpoint recall from reusable transition composition.

Experiment 14 reduces the oracle-context limitation in a controlled symbolic setting: the active world can be selected from partial transition-cue evidence before recurrent route execution. In the hard clean slice, symbolic context selection and route composition reach ceiling; under cue corruption, performance degrades while an oracle context-gated table remains an upper-bound control.

Experiment 15 adds a minimal neural comparator. It shows that small endpoint sequence models can memorize seen supplied-context routes without reliably learning reusable transition structure, while a conventional context-conditioned transition MLP and a world-head transition MLP solve the clean hard slice at ceiling. No-context neural variants fail conflict-sensitive first-step disambiguation, but a no-context transition MLP can still solve suffix composition where suffix transitions bypass the conflicting first transition. These results refine the manuscript’s claim posture: the contribution is not broad superiority over neural models, but a mechanism-sensitive benchmark decomposition showing where context indexing, transition storage, recurrence, endpoint memorization, and supplied-versus-selected context diverge.

The work is therefore a narrow benchmark and evidence map for studying compositional route memory under symbolic interference. It does not establish broad continual learning, raw perceptual latent-world discovery, biological validity, or exhaustive neural benchmarking.

**Draft note.** Final target-venue word count and any inferential confidence-interval/effect-size reporting remain venue- and comparison-family-dependent. The current abstract is claim-safe for the repository manuscript draft and should not be expanded into final inferential statistics until Table 3 comparison families are explicitly approved.

---

## 1. Introduction

Learning systems often encounter new information that conflicts with previously learned information. In continual learning, this is usually discussed as catastrophic forgetting: new updates can overwrite or interfere with previous capabilities [McCloskeyCohen1989; French1999; Kirkpatrick2017]. In memory-augmented, modular, and context-conditioned systems, the same pressure appears as a storage and retrieval problem: how can a system preserve distinct memories, retrieve the relevant one, and act on it without destructively mixing incompatible contexts [Graves2014; Graves2016; Weston2014; Sukhbaatar2015]?

The route-memory problem studied here isolates one form of this challenge. A world or context defines a transition system over symbolic states. The same state/action cue can imply one successor in world A and a different successor in world B. A model that stores all transitions in a shared table will overwrite, average, or otherwise collapse incompatible transitions. A model that memorizes full-route endpoints may succeed on seen full routes but fail on suffix probes that require reusable transition composition. A model that retrieves one-step transitions may still fail multi-step behavior if it cannot recurrently feed each successor back into the transition memory.

This makes route memory a useful controlled setting for separating four mechanisms:

1. structural transition storage;
2. context/world indexing;
3. recurrent multi-step execution;
4. context selection.

The core hypothesis tested in this repository is not that any individual ingredient is novel in isolation. Context gating, recurrence, structural plasticity, task masks, replay, parameter isolation, and memory augmentation all have substantial prior art. The safer and better-supported hypothesis is that a controlled route-memory benchmark can empirically separate these mechanisms and reveal failure modes hidden by aggregate accuracy.

The current evidence supports a conservative manuscript spine. Within this symbolic benchmark, structural route storage is required for reliable route-table formation and route execution under the tested ablations. Recurrent execution is required to turn stored one-step transitions into multi-step routes. Context/world indexing is required for incompatible first-step and full-route disambiguation. Clean supplied-context performance can reach ceiling through tested world counts, but finite structural budget produces measurable degradation under pressure.

The oracle-context limitation is central. Many experiments provide the active world label directly. This is useful for testing whether context-indexed storage can preserve incompatible transition systems, but it does not establish latent context inference. Experiment 13.2 sharpens this limitation by showing that an oracle context-gated transition table matches CIRM on the clean supplied-context benchmark. Therefore, the manuscript must not claim that clean supplied-context accuracy is the novelty.

Experiment 14 partially reduces this limitation by replacing direct supplied context with symbolic transition-cue context selection. The model receives partial evidence about transitions in the active world, selects a symbolic world/context, and then executes routes using the selected route memory. This supports a narrow claim: within the symbolic benchmark, transition cues can select the active world before route execution. It does not establish raw sensory latent-world discovery, perception, or general latent-cause inference.

Experiment 15 adds a minimal neural comparator. This is an important v2 change. The manuscript can no longer say neural baselines are absent. It should instead say that minimal fixed-profile neural comparator coverage is present but non-exhaustive. Exp15 also prevents broad overclaiming: a context-conditioned transition MLP and a world-head transition MLP solve the clean hard slice at ceiling. The correct interpretation is not that CIRM defeats neural baselines, but that the benchmark exposes which neural and symbolic variants learn endpoints, one-step transitions, reusable suffix structure, context-conflict disambiguation, and retention.

This manuscript makes the following publication-safe contributions:

* It defines a controlled symbolic route-memory benchmark for incompatible transition systems.
* It separates route-table storage, recurrent route execution, context conflict, suffix composition, capacity pressure, and symbolic context selection.
* It shows, within this benchmark, that removing structural route storage collapses route-table formation and route execution.
* It shows that route-table storage and executable multi-step composition dissociate: no-recurrence controls can preserve local transition access while failing route execution.
* It shows that supplied context/world indexing separates incompatible transition systems, while no-context variants fail conflict-sensitive first-step and full-route probes.
* It shows that symbolic transition cues can select the active world/context before route execution, reducing but not eliminating the oracle-context limitation.
* It adds symbolic/algorithmic and minimal neural baselines that sharpen the claim boundary rather than broadening it.
* It identifies remaining submission blockers: prior-art import, final source-data-backed figures/tables, confidence intervals/effect-size review, optional memory-augmented neural baselines depending on venue, replay audit if cited, and final reproducibility checks.

**Table 1 placeholder.** Claim-evidence summary. Source: `docs/manuscript/tables/table_01_claim_evidence.md`. Use as a main/supporting evidence map for retained claims C1-C6, C13, and C12, while preserving boundary/supplement and non-claim labels for C7-C11, C9, Exp13.1 positive lesion evidence, Exp15 replay collapse, broad neural-superiority claims, raw sensory latent-world discovery, and biological validation.

**Table 2 placeholder.** Run-integrity summary. Source: `docs/manuscript/tables/table_02_run_integrity.md`. Use as provenance support for the manuscript-relevant experiment package, while preserving older-run caveats and the Exp15 reconstructed-manifest/SQLite-tail caveat recorded in `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`, `docs/threads/experiment15_analysis_digest.md`, and Table 4.

**Table 3 placeholder.** Compact final-safe descriptive statistical summary. Source: `docs/manuscript/tables/table_03_compact_final_safe.md`; source data: `docs/manuscript/source_data/table_03_compact_final_safe.csv`. This is the main-text descriptive Table 3 for the current manuscript pass. The detailed generated statistical map remains candidate/supplementary audit support at `docs/manuscript/tables/table_03_statistical_summary.md` and `docs/manuscript/tables/table_03_statistical_summary.csv`; do not treat it as final inferential effect-size evidence or approved comparison-family statistics.

**Table 4 placeholder.** Minimal neural comparator hard-slice summary from Exp15. Source table: `docs/manuscript/tables/table_04_exp15_neural_comparator.md`; source data: `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`; authoritative source artifact: `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`. Caption caveat: Exp15 is a fixed-profile comparator, not exhaustive neural benchmarking; context-conditioned and world-head transition MLPs solve the clean hard slice, and replay collapse remains a non-claim pending audit.

---

## 2. Background and related work

### 2.1 Continual learning and catastrophic interference

Continual learning studies systems that acquire new knowledge while preserving prior capabilities. Classic work identified catastrophic interference when sequential training overwrote prior associations [McCloskeyCohen1989; French1999]. Modern continual-learning methods are often grouped into replay, regularization, architectural expansion, parameter isolation, task inference, distillation, and hybrid approaches [Kirkpatrick2017; Zenke2017; Rebuffi2017; LopezPaz2017; vanDeVenTolias2019].

The current work is related to continual learning because it studies incompatible transition systems over time and under capacity pressure. However, it is not a broad continual-learning benchmark. It does not evaluate class-incremental recognition, domain-incremental perception, multimodal streams, or open-ended task-free adaptation. It is closer to a controlled symbolic task/context-memory setting. The manuscript should therefore avoid claims such as “solves continual learning” or “prevents catastrophic forgetting generally.”

### 2.2 Memory-augmented computation

Memory-augmented neural systems separate computation from storage by providing external or differentiable memory mechanisms. Neural Turing Machines, Differentiable Neural Computers, Memory Networks, End-to-End Memory Networks, Matching Networks, and modern transformer memory systems all explore ways to read, write, retrieve, and reuse information [Graves2014; Graves2016; Weston2014; Sukhbaatar2015; Santoro2016; Vinyals2016].

CIRM is narrower. It is not a transformer memory architecture, differentiable external-memory model, or LLM-agent memory system. It uses explicit symbolic route-memory tables to separate transition storage, context indexing, recurrent execution, suffix composition, and capacity pressure. The benchmark contribution is not “memory exists,” but “these memory operations can be separately probed in a controlled route setting.”

Experiment 15 makes this boundary sharper. A conventional context-conditioned transition MLP can solve the clean symbolic route-transition task when context is supplied. Therefore, the manuscript should position CIRM as an interpretable symbolic mechanism and benchmark decomposition, not as evidence that learned neural transition models are incapable of the task.

### 2.3 Fast weights, structural plasticity, and differentiable plasticity

Fast weights, Hebbian updates, Hopfield networks, and differentiable plasticity all explore mechanisms by which connection strengths or memory structures change rapidly [Hebb1949; Hopfield1982; HintonPlaut1987; Miconi2018; Miconi2019]. Modern work also connects attention and fast-weight programming, blurring the distinction between learned attention, associative memory, and temporary key-value storage [Schlag2021FastWeights].

The present manuscript should not claim that dynamic memory writing or plasticity is novel. The supported claim is internal to the route-memory benchmark: when structural transition storage is removed from the model family being studied, route-table formation and route execution collapse. Exp15 further narrows this: a neural transition learner with supplied context can solve the clean transition problem without being the same mechanism as CIRM. Thus, C1 should remain benchmark-specific and should not be phrased as a universal requirement for all possible route-memory systems.

### 2.4 Context, gating, modularity, and latent task inference

Context-conditioned computation and modular routing are long-standing ideas. Mixture-of-experts models use gating to select specialized components [Jacobs1991; JordanJacobs1994]. Task masks, adapters, parameter isolation, architectural expansion, sparse routing, and modular continual-learning systems all seek to reduce interference by separating task- or context-relevant computation [Rusu2016; Fernando2017; Shazeer2017].

Cognitive science and computational neuroscience also provide latent-cause models in which agents segment experience into hidden contexts [GershmanNiv2010]. These literatures are direct prior-art risks. The manuscript should not claim that context gating, task masks, modular routing, or latent-cause inference are novel.

Experiment 14 should be framed narrowly: it shows symbolic transition-cue selection in the route-memory benchmark. The active world is selected from symbolic transition evidence before route execution. This reduces the supplied-label limitation but does not solve general latent task inference or raw sensory world discovery.

Experiment 15 reinforces this boundary. No-context neural variants fail first-step conflict probes, while context-conditioned or parameter-isolated transition MLPs solve the clean hard slice. This supports the importance of context for deliberately incompatible local mappings, but not the novelty of context conditioning itself.

### 2.5 Compositional route execution and graph/path reasoning

Route execution overlaps with compositional generalization, graph reasoning, and neural algorithmic reasoning. Compositional generalization asks whether a system can recombine known components in novel ways [LakeBaroni2018; Hupkes2020]. Neural algorithmic reasoning studies whether neural networks can learn or execute algorithmic procedures, often over graph-like inputs [Scarselli2009; Li2016; Battaglia2018; Velickovic2020].

The CIRM benchmark is narrower than general graph reasoning. It does not test shortest paths, arbitrary graph algorithms, broad extrapolation, or unrestricted systematic generalization. Its contribution is the explicit separation between:

* local transition storage;
* endpoint memorization;
* suffix-route composition;
* first-step context conflict;
* recurrent route execution;
* finite route-memory capacity.

Experiment 15 strengthens this decomposition. Endpoint neural models can perform well on seen routes while failing transition accuracy and suffix composition. Transition MLPs can solve reusable transition composition. A no-context transition MLP can solve suffixes while failing context-conflict starts. These results demonstrate why route-memory evaluation needs multiple probes rather than one aggregate accuracy.

### 2.6 Neuroscience motivation

The project is computationally inspired by hippocampal indexing, recurrence, pattern separation/completion, cognitive maps, sequence memory, and structural plasticity [OkeefeNadel1978; TeylerDiScenna1986; McClelland1995; NormanOReilly2003; Eichenbaum2017]. Complementary learning systems theory motivates the stability-plasticity framing [McClelland1995; Kumaran2016].

However, the current evidence is symbolic and synthetic. It does not prove a hippocampal mechanism, biological implementation, or neural sufficiency. Terms such as indexing, route fields, consolidation, inhibition, and structural plasticity should be used as computational inspiration unless directly tied to measured benchmark operations.

### 2.7 Closest prior-art positioning and narrow contribution

The contribution is best described as a controlled route-memory decomposition, not as novelty of any single mechanism. Context gating, recurrence, modular routing, differentiable or external memory, fast weights, graph reasoning, and hippocampal indexing all have substantial prior art. The present benchmark deliberately puts these ideas into a narrow symbolic transition setting where each can be probed separately: one-step transition storage, recurrent route execution, supplied versus selected context, endpoint memorization, suffix-route composition, finite structural budget pressure, and minimal neural comparator behavior.

This framing is important after Exp13.2 and Exp15. Exp13.2 shows that an oracle context-gated transition table can match the full model in the clean supplied-context setting. Exp15 shows that a conventional context-conditioned neural transition learner and a world-head transition learner can solve the clean hard slice when context is supplied. Therefore, clean ceiling accuracy with supplied world labels is not the novelty claim.

The manuscript's narrow contribution is the evidence map: it shows where different computational contracts diverge under controlled interference. Endpoint memorization, reusable one-step transition learning, recurrent rollout, no-context sharing, supplied context, selected symbolic context, finite structural budget, and parameter/world-head isolation produce different failure modes. The paper should therefore be read as a mechanism-sensitive benchmark and decomposition study rather than a claim that CIRM invents context gating, recurrence, neural memory, modular routing, graph reasoning, biological indexing, or general neural superiority.

The companion source artifact for this positioning is `docs/manuscript/closest_prior_art_table.md`. It should remain available for reviewer-facing traceability and possible later conversion into a venue-specific table or supplement.

---

## 3. Problem setup: route memory under contextual interference

We define a route-memory problem over symbolic transition systems.

Let there be a set of worlds or contexts:

`W = {w_1, ..., w_K}`

and a shared set of symbolic states:

`S = {s_1, ..., s_N}`.

Each world defines a transition function over states and actions or route modes:

`T_w: S × A -> S`.

A context conflict occurs when two worlds assign different successors to the same local cue:

`T_{w_i}(s, a) != T_{w_j}(s, a)` for some `i != j`.

A route is generated by repeated transition application:

`r = (s_0, a_0, s_1, a_1, ..., s_L)`

where:

`s_{t+1} = T_w(s_t, a_t)`.

The benchmark separates several evaluation targets:

* **Route-table storage**: whether the model stores or retrieves one-step transition entries.
* **Route execution**: whether the model can execute a multi-step route by iterating through stored transitions.
* **Seen-route composition**: performance on full routes available under the benchmark’s seen-route condition.
* **Suffix-route composition**: performance when the model must execute a suffix of a route rather than retrieve a memorized full-route endpoint.
* **First-step context conflict accuracy**: whether the model chooses the correct first transition when the same local cue has different successors in different worlds.
* **World/context selection**: whether the model uses the appropriate world index, supplied directly or selected from symbolic cues.
* **Retention after sequential worlds**: whether performance on prior worlds is preserved under sequential training/evaluation regimes.
* **Capacity scaling**: behavior as world count, route length, or structural budget pressure increases.
* **Cue/context corruption**: sensitivity to wrong-world evidence or corrupted transition cues.

In supplied-context experiments, the active world label is provided. This isolates whether context-indexed storage can avoid interference, but it does not establish context inference. In Exp14-style cue-selection experiments, the model receives partial symbolic transition evidence and selects a world before route execution. This reduces the oracle-label assumption but remains symbolic and controlled.

**Figure 1 placeholder.** Conceptual route-memory schematic. Source assets: `docs/manuscript/figures/figure_01_conceptual_route_memory.png` and `docs/manuscript/figures/figure_01_conceptual_route_memory.svg`; source data: `docs/manuscript/source_data/figure_01_conceptual_route_memory.csv`. Caption caveat: conceptual only; do not imply biological validation, raw latent-world discovery, or novelty of context gating/recurrence alone.

---

## 4. Model and mechanism

The manuscript-relevant mechanism is context-indexed structural route memory. At a high level, the model stores one-step transitions as route-memory entries indexed by world/context. A query consists of a current symbolic state, an action or route mode where relevant, and an active world/context. The active context selects the transition table or route field used to retrieve the next state.

Multi-step route execution is recurrent. The successor produced at one step becomes the current state for the next step, and this process repeats until the route length is reached.

This gives three analytically separable components:

1. **Structural transition storage**: the mechanism must allocate or store one-step transitions.
2. **Context/world indexing**: the mechanism must keep incompatible transitions separated across worlds.
3. **Recurrent execution**: the mechanism must repeatedly apply stored transitions.

A model can have an accurate one-step route table and still fail multi-step route execution if it cannot recurrently compose transitions. A model can memorize full endpoints and still fail suffix composition if it has not stored reusable transition primitives. A model can solve suffixes that bypass a conflict but fail first-step context conflicts where the same start/action pair maps differently across worlds.

Exp14 adds symbolic context selection. Instead of receiving an oracle world label, the model receives partial symbolic transition cues. The selector chooses a world/context, after which context-indexed route memory executes the route recurrently. Cue corruption means some cue evidence points away from the correct world under a synthetic corruption process.

Exp15 adds neural comparators. The most important neural families are:

* endpoint sequence models, which predict full-route endpoints;
* rollout models, which attempt recurrent transition execution;
* transition MLPs, which learn one-step transitions and are rolled out;
* no-context variants, which remove world identity;
* world-head transition MLPs, which isolate parameters by world;
* replay transition MLPs, which attempt sequential-world retention with bounded replay.

These baselines clarify the mechanism boundary. Endpoint prediction, transition learning, context conditioning, parameter isolation, and recurrent rollout are different computational contracts. They should not be collapsed into a single “neural baseline” result.

### 4.1 What the model is not

The model is not a complete biological brain model. It is not an end-to-end perceptual model. It is not a general continual-learning solution. It is not proof of a hippocampal indexing mechanism. It is not a claim that neural networks cannot solve symbolic transition tasks.

The model should be described as a controlled mechanism for studying context-indexed symbolic route memory. The benchmark is useful because it exposes distinctions between storage, context, execution, endpoint memorization, capacity, and context selection.

---

## 5. Experimental overview

| Experiment | Purpose                                                                            | Main claim supported                  | Manuscript role                                                                                      |
| ---------- | ---------------------------------------------------------------------------------- | ------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Exp11      | Test context-separated memory for incompatible worlds and early ablations.         | C2, C3, C4                            | Supporting historical evidence.                                                                      |
| Exp12      | Test clean supplied-context capacity scaling.                                      | C5 plus C2-C4 support                 | Main evidence for clean ceiling scaling through tested world counts.                                 |
| Exp13      | Push the system under finite structural budget and failure pressure.               | C6, C7                                | Main/narrow evidence for observed budget degradation; no fitted capacity law.                        |
| Exp13.1    | Publication-hardening ablations and diagnostics.                                   | C1-C4, C7 caveated                    | Main evidence for core ablation figure; lesion diagnostic is negative/caveated.                      |
| Exp13.2    | Symbolic/algorithmic baseline suite.                                               | C12; C2-C4 controls                   | Baseline evidence; oracle context-gated lookup matches CIRM under clean supplied context.            |
| Exp14      | Select symbolic world/context from partial transition cues before route execution. | C13; narrows C2/C10                   | Main-narrow or high-priority supplement; reduces oracle-context criticism within symbolic benchmark. |
| Exp15      | Minimal neural baseline comparator.                                                | C12; strengthens C4 and narrows C1/C2 | Recommended compact main-text neural comparator table; not exhaustive neural benchmarking.           |

Excluded or non-central experiments:

Exp1-Exp6 are exploratory or methodological precursors. Exp7-Exp10 provide useful background for route composition, plasticity, and consolidation but are not the central manuscript evidence. C8 consolidation, C9 seen/unseen primitive boundary, C10 context corruption, and C11 continuous/noisy bridge should remain supplementary/future-work unless metric and framing gaps are resolved.

---

## 6. Results

### 6.1 Structural route storage supports route-table formation and execution

The C1 claim is benchmark-specific: within this symbolic route-memory benchmark, removing structural route storage collapses route-table formation and route execution. The strongest manuscript-facing evidence comes from the publication-hardening ablations and baseline suite. Exp13.1 reports near-chance performance for no-structural-plasticity variants at the hard route setting, while the full model reaches ceiling in the corresponding core ablation summaries. Exp13.2 reinforces this pattern in the symbolic baseline suite.

**Figure 2 placeholder.** Structural storage and recurrence ablation. Source assets: `docs/manuscript/figures/figure_02_structural_plasticity_recurrence_ablation.png` and `docs/manuscript/figures/figure_02_structural_plasticity_recurrence_ablation.svg`; source data: `docs/manuscript/source_data/figure_02_structural_plasticity_recurrence_ablation.csv`; source artifact: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_ablation_metrics.csv`. Caption caveat: benchmark/model-family-specific; do not imply universal structural-plasticity necessity or broad neural-model inferiority.

This result should not be overgeneralized. It does not show that all neural systems require explicit structural plasticity. Experiment 15 specifically shows that a context-conditioned neural transition MLP can solve the clean symbolic transition task when context is supplied. The safe interpretation is that structural route storage is required for the tested CIRM mechanism and its ablations, not for all possible route-memory systems.

**Claim-language note.** C1 should remain benchmark/model-family-specific: structural route storage is required for the tested CIRM mechanism and ablations, not universally required for all possible route-memory systems or neural implementations.

### 6.2 Recurrent execution is required for multi-step composition

C3 states that recurrent execution is required to compose stored one-step route memories into multi-step routes. Exp13.1 provides the clearest manuscript-facing ablation: no-recurrence-at-eval preserves route-table accuracy while composition collapses. Exp13.2 reinforces this boundary: no-recurrence controls can preserve route-table or first-step access while failing seen and suffix composition.

This dissociation is central. If the system can retrieve a local transition but cannot repeatedly feed each successor back into transition memory, then it has storage without route execution. Recurrence is not claimed as novel. It is the mechanism required, in this benchmark, to animate stored one-step transitions into multi-step behavior.

Experiment 15 sharpens the wording. The context-conditioned transition MLP solves one-step transitions and, when rolled out, solves composition. The endpoint neural models do not show the same reusable transition structure. The correct comparison is therefore not “recurrent versus neural,” but “endpoint prediction versus reusable transition learning plus rollout.”

### 6.3 Route-table storage, endpoint memorization, and composition dissociate

C4 states that route-table storage and multi-step compositional execution are separable. The no-recurrence ablation is one form of evidence. Endpoint memorization controls provide another.

Exp13.2 reports that endpoint memorization can solve seen full-route endpoints while failing suffix composition. Exp14 repeats this conceptual control under symbolic transition-cue selection. Exp15 extends the dissociation to neural baselines: the context GRU endpoint model nearly solves seen-route composition in the hard slice but has much lower suffix-route composition and near-zero transition accuracy. The Transformer endpoint model shows the same qualitative pattern at lower seen-route accuracy.

This matters because endpoint recall is not the same as transition composition. A model can memorize “from this start, under this route, output this endpoint” without learning reusable one-step transitions. Suffix-route probes help distinguish endpoint memorization from route execution.

[Table 4 here: Exp15 minimal neural comparator hard-slice summary. Source table: `docs/manuscript/tables/table_04_exp15_neural_comparator.md`; source data: `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`; authoritative source artifact: `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`.]

Table 4 is maintained as a separate source-data-backed manuscript artifact:

- Table: `docs/manuscript/tables/table_04_exp15_neural_comparator.md`
- Source data: `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`
- Authoritative Exp15 source artifact: `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`

Caption draft:

Table 4. Minimal neural comparator on the hardest Exp15 summarized slice (`world_count=32`, `route_length=12`, `n_seeds=10`). Endpoint sequence models can perform well on seen full routes without learning reusable transition structure, while context-conditioned transition MLPs solve the clean transition-composition problem. No-context transition learning fails conflict-sensitive first-step and seen-route disambiguation despite solving suffix composition, showing that context is required for deliberately incompatible local mappings rather than for every suffix transition. The replay variant is shown for completeness but should not be interpreted until audited. Exp15 is a fixed-profile comparator, not an exhaustive neural architecture search.

### 6.4 Context indexing separates incompatible transition systems, but the claim must be conflict-specific

C2 states that context/world indexing prevents destructive interference between incompatible route systems. Supplied-context experiments support this claim where worlds share local cues but require different successors. Exp13.2 shows that shared no-context lookup fails conflict-sensitive seen-route and first-step probes, while CIRM and oracle context-gated lookup solve the clean supplied-context benchmark.

Exp15 strengthens but also narrows this claim. No-context neural variants are at or near chance on first-step context conflict accuracy in the hard slice. This supports the necessity of context/world identity when local cues are incompatible. However, the no-context transition MLP reaches 1.0000 suffix-route composition and high transition accuracy in the same hard slice. This means context is not required for every suffix transition. It is required where the local cue is ambiguous across worlds, especially the deliberately conflicting first transition and full-route disambiguation.

The final wording should therefore be:

Context/world indexing is necessary for incompatible local transitions and full-route disambiguation in this benchmark. It should not be phrased as a blanket requirement for all route composition.

### 6.5 Clean capacity scaling and finite-budget degradation

C5 is ceiling-limited. Under clean supplied context, the full model maintains ceiling route-table and composition accuracy through the tested world counts. Exp12 reports ceiling performance at world counts 2, 4, 8, 16, and 32 under the clean supplied-context full profile.

**Figure 3 placeholder.** Clean supplied-context capacity scaling. Source assets: `docs/manuscript/figures/figure_03_capacity_scaling.png` and `docs/manuscript/figures/figure_03_capacity_scaling.svg`; source data: `docs/manuscript/source_data/figure_03_capacity_scaling.csv`; source artifact: `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`. Caption caveat: ceiling-limited supplied-context result over the tested range only; no fitted capacity law or broad generalization claim.

C6 is narrower. Finite structural budget produces an observed route-execution degradation curve. Exp13 shows degradation under severe global budget pressure and recovery at exact or surplus budget. This supports an observed degradation curve, not a fitted capacity law.

C7, local-versus-global budget pressure, is promising but should remain narrow main or supplement unless paired seed-level local/global statistics are added. The existing evidence suggests local budget pressure is more damaging than global pressure, but manuscript-grade statistical comparison remains pending.

**Figure 4 placeholder.** Finite structural budget and local/global pressure. Source assets: `docs/manuscript/figures/figure_04_finite_structural_budget_local_global.png` and `docs/manuscript/figures/figure_04_finite_structural_budget_local_global.svg`; source data: `docs/manuscript/source_data/figure_04_finite_structural_budget_local_global.csv`. Placement/caption caveat: supplement-default unless the manuscript deliberately emphasizes the finite-budget story; use as observed degradation evidence only, with no fitted law and no C7 promotion without paired seed-level local/global analysis.

Caption caveat:

No fitted capacity law is claimed. This figure shows observed degradation under finite structural budget pressure in the tested symbolic route-memory setting.

### 6.6 Symbolic context selection reduces but does not eliminate the oracle-context limitation

Supplied-context experiments show that context-indexed storage can preserve incompatible transition systems, but they leave open a serious criticism: if the correct world label is supplied, then an oracle context-gated lookup table can solve the clean benchmark.

Exp13.2 confirms this. At the hard clean supplied-context slice, CIRM and oracle context-gated lookup both reach ceiling on route-table, seen-route composition, suffix-route composition, and first-step context accuracy. This is why clean supplied-context accuracy is not the novelty claim.

Exp14 addresses the limitation in a narrow symbolic way. The model receives partial symbolic transition cues, selects a world/context, and then executes the route recurrently. In the hard clean slice (`world_count=32`, `route_length=16`, `cue_count=8`, `corruption_rate=0.0`), the CIRM latent selector reaches ceiling seen-route world selection, seen-route composition, suffix-route composition, and first-step context accuracy. Under high corruption, selection and composition degrade while the oracle context-gated table remains an upper bound.

[Figure 5 here: symbolic context selection from transition cues. Source: `docs/manuscript/figures/figure_05_symbolic_context_selection.png` and `.svg`; source data: `docs/manuscript/source_data/figure_05_symbolic_context_selection.csv`; source artifact: `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`.]

This result supports C13: the active symbolic world/context can be selected from partial transition-cue evidence before route execution. It also clarifies C2: supplied context and cue-selected context are different experimental contracts. Exp14 reduces the oracle-context criticism, but it does not eliminate it because the cues are symbolic, the corruption process is synthetic, and the oracle context-gated table remains a ceiling upper-bound control.

### 6.7 Minimal neural comparator: what Exp15 does and does not show

Exp15 was designed to test whether ordinary neural sequence and transition models trained under comparable symbolic route-memory conditions reproduce the same storage, context, retention, and composition behavior observed in CIRM.

The full run completed 1,080 units across 10 seeds, 9 variants, 4 world counts, and 3 route lengths. Validation passed with 42 PASS, 0 WARN, and 0 FAIL. The run produced 5,400 seed metric rows and 1,080 runtime rows. All runtime rows report CUDA execution on an NVIDIA TITAN X (Pascal), with total runtime approximately 4.75 hours.

The hard-slice results support four conservative conclusions.

First, endpoint neural sequence models can memorize seen supplied-context routes without learning reliable reusable transition structure. The context GRU endpoint model reaches approximately 0.9990 seen-route composition but only 0.4040 suffix-route composition and 0.0232 transition accuracy. The Transformer endpoint model is weaker but shows the same qualitative split.

Second, explicitly context-conditioned transition learning can solve the clean symbolic benchmark. The context transition MLP and world-head transition MLP reach 1.0000 on all reported hard-slice metrics. This weakens any broad claim that ordinary neural models cannot solve the task. The manuscript should therefore emphasize mechanism decomposition and interpretability, not neural-model superiority.

Third, no-context neural variants fail conflict-sensitive first-step probes. This supports context necessity for deliberately incompatible local mappings. However, the no-context transition MLP solves suffix composition, demonstrating that suffix-route success is not always context-sensitive when suffixes bypass the conflicting first step.

Fourth, the GRU rollout context model partially learns context-sensitive transition behavior but fails long multi-step execution in the fixed profile. It reaches approximately 0.8794 first-step conflict accuracy and 0.5122 transition accuracy, but only 0.0448 seen-route composition, 0.0777 suffix composition, and 0.0612 retention. This suggests compounding rollout error, insufficient transition learning, or profile limitations, but should not be generalized to all GRUs.

The replay variant should not be interpreted scientifically yet. Its near-zero hard-slice performance may reflect a bug, an insufficient replay buffer, undertraining, or a real sequential-interference failure. The repo docs explicitly require audit before citation as a replay result.

Exp15 also has a provenance caveat. The CSV artifacts are treated as authoritative, but `run_manifest.json` was reconstructed after a final SQLite manifest-write failure, and the SQLite `run_manifest` table may be empty. This should be disclosed if Exp15 becomes a central manuscript table.

### 6.8 Supplementary or negative results

Several results should remain supplementary, historical, or limitations in the first manuscript.

Consolidation (C8) should be framed as a stability-plasticity bias rather than an accuracy-rescue mechanism. Easy regimes do not require consolidation, and Exp13.1 did not show that consolidation strength materially rescues constrained-budget accuracy.

Seen-versus-unseen primitive transition claims (C9) require metric cleanup. Existing evidence suggests the model composes over stored primitives and does not infer unseen primitive transitions, but route-table accuracy requires seen/unseen/all split metrics before this becomes a central claim.

Context corruption (C10) should be framed as wrong-world or symbolic cue-evidence sensitivity, not generic stochastic robustness. Exp13/Exp13.1 wrong-world injection and Exp14 cue corruption identify context-selection failure boundaries, but they do not establish broad robustness to realistic noise.

The continuous/noisy bridge (C11) remains preliminary. It tests whether a decoded noisy symbolic input can feed route memory. It is not end-to-end perception or learned visual representation.

Exp13.1 lesion diagnostics should not be cited as positive mechanism evidence. The targeted lesion sensitivity result was less damaging than random count-matched lesion sensitivity, so it is either a diagnostic failure, a definition problem, or a negative result requiring audit/rerun before use.

Exp15 replay collapse should not be cited as evidence that replay fails until the implementation and training regime are audited.

---

## 7. Discussion

The results support a narrow mechanistic interpretation. In a controlled symbolic route-memory benchmark, structural storage, context indexing, recurrent execution, and context selection play distinct roles. Structural route storage supports formation of one-step transition entries. Context/world indexing separates incompatible local transition systems. Recurrence turns stored one-step transitions into executable multi-step routes. Symbolic transition cues can select an active world before execution.

The strongest conceptual point is the separation between route storage and route execution. A system can store local transitions but fail to execute multi-step routes. A system can memorize endpoints but fail suffix composition. A system can solve clean supplied-context route memory with an oracle context-gated table, but fail when context must be selected or when conflict-sensitive first-step probes are tested.

Experiment 13.2 prevents overclaiming. The oracle context-gated transition table matches CIRM under clean supplied context, showing that clean accuracy with supplied labels is not enough. Shared no-context lookup fails conflict-sensitive probes, showing that context separation matters where local transitions conflict. Endpoint memorization fails suffix composition, showing that full-route recall is not equivalent to compositional route execution.

Experiment 14 changes the manuscript from a purely oracle-context story to a partially cue-selected context story. The active symbolic world can be selected from transition cues before recurrent execution. Multiple cues improve selection under corruption. However, the result remains symbolic and controlled. It does not establish perception, open-ended latent-cause discovery, or a general inference algorithm.

Experiment 15 changes the manuscript’s neural baseline posture. Minimal neural comparator coverage is now present. The result is not “CIRM beats neural networks.” In fact, the context-conditioned transition MLP solves the clean hard slice. Instead, Exp15 shows that different neural contracts produce different behavior: endpoint models can memorize seen endpoints without transition structure; rollout models may learn partial transitions without robust long-route composition; no-context models fail conflict-sensitive disambiguation; and supplied-context transition learners can solve the clean transition-composition problem.

This makes the manuscript more scientifically honest and, arguably, stronger. The paper no longer depends on neural baselines failing. It instead argues that the benchmark decomposes memory behavior into interpretable components and exposes where each model class succeeds or fails.

The relationship to continual learning should remain careful. The benchmark shares the stability-plasticity and interference concerns of continual learning, but it is not a class-incremental or domain-incremental neural benchmark. It is closer to a controlled task/context-memory benchmark with explicit or symbolically selected context. It may be useful for future memory architectures because it exposes which metrics separate storage, routing, execution, and endpoint recall. It does not replace standard continual-learning evaluation.

The biological interpretation should remain bounded. Hippocampal indexing, cognitive maps, pattern separation/completion, recurrence, and structural plasticity motivate the work, but the experiments are synthetic and symbolic. The manuscript can say the mechanism is computationally inspired by these ideas. It should not claim the brain uses this exact mechanism or that the benchmark validates a biological theory.

### 7.1 Why the work is still not submission-ready

The repository is ready for claim hardening and final figure/table planning, but not submission-ready. Remaining blockers include:

* retained-main-claim decision after post-Exp15 narrowing;
* human-review Exp15 Table 4 and final placement;
* seed-level confidence intervals and effect-size review for retained claims;
* final figure caption and panel review;
* prior-art/novelty import as a local artifact;
* final BibTeX and DOI verification;
* optional memory-augmented/key-value neural baseline decision;
* replay audit if replay is mentioned beyond a caveat;
* fresh checkout command verification;
* license and `CITATION.cff`.

### 7.2 Target venue posture

For a controlled symbolic/mechanistic benchmark paper, the current evidence can support a cautious manuscript after statistical and documentation hardening. For a stronger ML venue, reviewers may still expect broader neural baselines, especially memory-augmented or key-value neural lookup models. Exp15 helps, but it is fixed-profile and non-exhaustive.

The safest target-venue framing is:

This paper introduces a controlled route-memory benchmark and mechanism decomposition, supported by symbolic/algorithmic baselines and a minimal neural comparator. It does not claim exhaustive neural benchmarking.

---

## 8. Limitations

1. **Synthetic symbolic tasks.** The benchmark uses symbolic states, worlds, routes, and transition cues. This supports controlled mechanistic analysis but limits claims about natural data.

2. **Limited perceptual grounding.** The manuscript-relevant experiments do not learn from raw sensory input. Exp13’s continuous/noisy bridge is a decoded symbolic front end, not end-to-end perception.

3. **Oracle context assumptions.** Many experiments supply the world/context label directly. Exp14 reduces this limitation using symbolic transition cues, but does not eliminate it.

4. **Symbolic latent context selection.** Exp14 cues are symbolic transition evidence. Cue corruption is synthetic. The result does not establish general latent-cause inference or raw sensory world discovery.

5. **Minimal neural comparator only.** Exp15 supplies a completed fixed-profile neural comparator, but it is not exhaustive. It uses small fixed models/hyperparameters, omits memory-augmented/key-value neural baselines, and does not include route length 16 in the default full profile.

6. **Neural superiority is not supported.** Exp15 shows that context-conditioned transition MLPs solve the clean hard slice. The manuscript must avoid broad CIRM-over-neural-model claims.

7. **Replay variant requires audit.** Exp15 replay collapse should not be cited as scientific evidence against replay until implementation and training-regime audit is complete.

8. **Exp15 provenance caveat.** `run_manifest.json` was reconstructed after a final SQLite manifest-write failure, and the SQLite `run_manifest` table may be empty. CSV artifacts are treated as authoritative unless a later audit changes that.

9. **Prior-art/novelty import incomplete.** The repository still lacks a local prior-art/novelty assessment artifact. Citation verification and recent literature positioning remain required before submission.

10. **Metric cleanup remains.** Seen-versus-unseen primitive transition claims require cleaned route-table and composition splits. Suffix metrics can be misleading when they bypass first-step context conflicts.

11. **Uncertainty and effect-size review.** Candidate statistical tables exist, but effect-size groupings and confidence intervals require human review before exact manuscript citation.

12. **Generated figures are candidates.** Figures 1-5 have been generated by a reproducible asset pipeline, but they are not final journal figures. Captions, panel choices, and main-versus-supplement placement require review.

13. **Capacity law not established.** Finite-budget results show observed degradation curves. No fitted capacity law is claimed.

14. **Consolidation claim is preliminary.** Current evidence supports at most a stability-plasticity bias, not necessity or robust accuracy rescue.

15. **Lesion diagnostic failure.** Exp13.1 targeted lesion results should not be cited positively without audit/rerun.

16. **Biological interpretability is limited.** The work is biologically inspired, but the evidence is not biological.

17. **Reproducibility metadata gaps.** Older Exp11/Exp12 layouts lack validation JSON and SQLite manifests. Fresh command verification and hardware/runtime logs are still required before submission.

18. **License/citation metadata missing.** A human-selected license and `CITATION.cff` remain needed before formal public release or submission.

---

## 9. Conclusion

This manuscript establishes a cautious first result from the context-indexed route-memory research program. In a controlled symbolic benchmark, context-indexed structural storage can preserve incompatible local transition systems, recurrent execution is required to compose stored one-step transitions into multi-step routes, and route-table storage can dissociate from executable composition. Clean supplied-context scaling reaches ceiling through tested world counts, while finite structural budget produces an observed degradation curve.

Symbolic transition-cue selection can choose the active world before route execution, reducing the oracle-context limitation within the benchmark. A minimal neural comparator further sharpens the claim boundary: endpoint neural models can memorize seen routes without robust reusable transition structure, no-context models fail conflict-sensitive disambiguation, and context-conditioned transition MLPs solve the clean hard slice.

The work should therefore be read as a mechanism-focused benchmark and evidence map, not as a complete continual-learning solution, biological theory, perceptual latent-world model, or broad neural benchmark. Its immediate value is to make failure modes visible: no structural route storage, no context separation, no recurrence, endpoint memorization, finite capacity, corrupted symbolic context evidence, and insufficient neural comparator contracts fail in different ways.

The next step is not to broaden the claim, but to harden it: freeze the retained post-Exp15 claim set, review the source-data-backed Exp15 table, finalize figures and statistics, verify citations, decide target venue, and add broader neural baselines only if the venue or reviewers require them.

---

## 10. Methods

### 10.1 Route-memory task generation

The benchmark generates symbolic worlds containing transition systems over shared state symbols. Routes are generated by applying world-specific one-step transitions over a fixed route length. Context conflict arises when the same local cue has different successors in different worlds.

Key manipulated variables across experiments include:

* world count;
* route length;
* structural budget;
* local versus global budget pressure;
* cue count;
* cue corruption;
* supplied versus selected context;
* endpoint versus transition training objective;
* context-present versus no-context neural inputs;
* joint versus sequential-world training regimes.

[Draft note: Fill exact task-generation parameters and pseudocode from implementation files.]

### 10.2 Model variants and controls

The full mechanism uses context-indexed structural route memory with recurrent route execution.

Manuscript-relevant controls include:

* no structural plasticity;
* no context binding or shared no-context lookup;
* no recurrence at evaluation;
* oracle context-gated transition table;
* endpoint memorizer;
* recurrent non-plastic rules;
* bounded LRU/replay variants;
* parameter-isolation controls;
* superposition/hash-slot symbolic controls;
* random and recency selectors in Exp14;
* compact hash-slot selectors in Exp14;
* neural endpoint GRU;
* neural rollout GRU;
* neural Transformer endpoint model;
* context-conditioned transition MLP;
* no-context transition MLP;
* replay transition MLP;
* world-head transition MLP.

The oracle context-gated table is an upper-bound supplied-context control, not a defeated competitor. The context-conditioned neural transition MLP is a conventional neural transition learner, not a CIRM variant.

### 10.3 Metrics

Primary metrics include:

* `route_table_accuracy`: accuracy of one-step transition storage/retrieval.
* `composition_accuracy`: accuracy of multi-step route execution.
* `seen_route_composition_accuracy`: composition on seen full-route probes.
* `suffix_route_composition_accuracy`: composition on route suffixes to test primitive reuse rather than endpoint memorization.
* `first_step_context_conflict_accuracy`: correctness of conflict-sensitive first-step transitions.
* `transition_accuracy`: one-step transition accuracy in Exp15 neural comparators.
* `retention_after_sequential_worlds`: retention under sequential-world conditions.
* `world_selection_accuracy_seen_route`: Exp14 world/context selection from symbolic transition cues.
* capacity/budget metrics: composition accuracy across global and local budget ratios.
* validation integrity: pass/warn/fail counts, metrics rows, summary rows, effect-size rows, plot counts, manifest/database presence.

[VERIFY: Metric names should be made exact against CSV headers before submission.]

### 10.4 Experimental profiles and seeds

The run-integrity table should report:

* Exp11: historical full run; older layout lacks current validation JSON.
* Exp12: historical full run; older layout lacks current validation JSON.
* Exp13: finite-budget source; validation PASS with caveats.
* Exp13.1: publication-hardening full run with validation PASS.
* Exp13.2: symbolic/algorithmic baseline suite with validation PASS.
* Exp14: symbolic context-selection full run with validation PASS.
* Exp15: minimal neural comparator full run `exp15_full_20260508_092811`, validation PASS with 42 PASS, 0 WARN, 0 FAIL; 10 seeds; 9 variants; 5,400 seed metric rows; 1,080 runtime rows; CUDA on NVIDIA TITAN X (Pascal); reconstructed-manifest caveat.

Source: `docs/manuscript/tables/table_02_run_integrity.md` for Exp11-Exp14, plus `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`, `docs/threads/experiment15_analysis_digest.md`, and Table 4 for Exp15 until the run-integrity table is regenerated.

### 10.5 Validation and artifact generation

Validation reports are available for Exp13, Exp13.1, Exp13.2, Exp14, and Exp15. Older Exp11/Exp12 layouts lack validation JSON and SQLite manifests, so they should be cited with provenance caveats.

The manuscript asset pipeline was generated with:

`python scripts/manuscript_assets/build_manuscript_assets.py`

This produced candidate figures, source-data CSVs, manuscript tables, `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`, and `docs/repo_audit/MANUSCRIPT_ASSET_GENERATION_REPORT.md`.

Exp15 now has a source-data-backed Table 4 artifact for V2; it still requires human review, final caption approval, and a main-text-versus-supplement decision for the target venue.

### 10.6 Figure and table plan

Generated candidate figures:

* Figure 1: conceptual route-memory schematic.
* Figure 2: structural plasticity and recurrence ablation.
* Figure 3: clean capacity scaling.
* Figure 4: finite structural budget/local-global pressure.
* Figure 5: symbolic context selection.

Generated manuscript tables:

* Table 1: claim evidence.
* Table 2: run integrity.
* Table 3: statistical summary.

Existing V2 table:

* Table 4: Exp15 minimal neural comparator hard-slice summary (`docs/manuscript/tables/table_04_exp15_neural_comparator.md`).

Recommended placement:

* Figure 1: main text.
* Figure 2: main text.
* Figure 3: main text.
* Figure 4: main text only if C6/C7 remain central; otherwise supplement.
* Figure 5: main-narrow or high-priority supplement; recommended main-narrow because it addresses the oracle-context critique.
* Table 4: compact main-text table in V2; full Exp15 plots and variant details in supplement unless venue constraints require moving the table itself.

---

## 11. Remaining work before submission

The V2 draft is now captured in the repository branch and should be treated as the manuscript base for the next hardening pass. The next steps are not to broaden the scientific claim, but to harden the retained claim set.

Immediate next actions:

1. Decide the retained main claim set after post-Exp15 narrowing.
2. Decide Exp14 placement: main-narrow Figure 5 versus supplement.
3. Human-review Exp15 Table 4 and decide whether it remains compact main text or moves to supplement for the target venue.
4. Generate or review seed-level confidence intervals and effect sizes for retained claims.
5. Review Table 3 effect-size groupings before exact manuscript citation.
6. Review figure captions and panel choices for Figures 1-5.
7. Import prior-art/novelty evidence as a local repository artifact.
8. Verify citation metadata, BibTeX entries, DOIs, and venues.
9. Audit Exp15 replay only if it will be interpreted beyond a caveat.
10. Decide whether a memory-augmented/key-value neural baseline is required by the target venue.
11. Run fresh checkout/path verification before submission handoff.
12. Add a human-selected `LICENSE` and `CITATION.cff`.

Keep out of main claims unless future work changes the evidence base:

- Exp15 replay collapse as a general replay result.
- Broad CIRM-over-neural-model superiority.
- Broad biological mechanism claims.
- Raw sensory latent-world discovery.
- End-to-end perception.
- Unseen primitive transition inference.
- Positive Exp13.1 lesion evidence.
- Fitted capacity-law language.
