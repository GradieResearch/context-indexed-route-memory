# Biological Neural Nets — Theory, Results, and Experimental Roadmap

## Purpose of this document

This document preserves the current research context so the project can continue in a new thread without losing the conceptual trajectory, experimental history, or design decisions.

The project is exploring whether a fundamentally different style of learning machine can be built by moving away from the dominant paradigm of dense, static parameter matrices and toward a persistent, sparse, adaptive graph of neuron-like units whose connections, internal states, and traversal probabilities change through interaction.

The working thesis is not that we should literally simulate biology in every biochemical detail. The thesis is that modern neural networks may be missing a core property of biological intelligence: **the computational substrate itself changes over time through gated plasticity, sparse activation, recurrent traversal, structural adaptation, and consolidation.**

---

# 1. Core thesis

Modern neural networks, including transformers, are mostly **frozen learned functions**. They learn by converging on parameters during training, then use those largely fixed parameters during inference.

A simplified contemporary pattern is:

```text
training data -> optimize parameters -> frozen model -> inference via context
```

By contrast, biological intelligence appears closer to:

```text
experience -> activation -> internal state change -> synaptic modulation -> structural adaptation -> future behavior changes
```

So the key distinction is:

```text
Current LLMs remember by being reminded through context.
Biological systems remember because the system itself has changed.
```

This leads to the central architectural claim:

> The next generation of learning systems should move from static parameter fields toward persistent adaptive substrates: sparsely activated graph-structured systems whose units have internal state, whose edges carry plastic potential, and whose topology can evolve through experience-driven updates.

A more concise slogan emerged:

> **Memory can fade, but reasoning should strengthen.**

Meaning:

- Episodic details should decay unless reinforced.
- Useful reasoning pathways should consolidate through repeated successful use.
- The system should not merely store facts; it should become better at traversing useful paths.

---

# 2. Why long-context prompting is not enough

The initial conceptual problem was framed as a “multipath manifold.” A conversation creates many possible latent trajectories. When the entire history is passed into a model, the model attempts to infer the correct path through that manifold.

But very long context can become harmful. It may include active goals, stale goals, abandoned branches, false starts, outdated assumptions, emotional residue, and irrelevant but semantically nearby information.

The problem is not only forgetting. It is **remembering too indiscriminately**.

A better context-management principle was proposed:

```text
keep_score = utility + persistence - interference
```

The strongest theoretical formulation was:

```text
Query-conditioned information bottleneck pruning
+ belief-state tracking
+ contrastive context routing
+ interference-aware suppression
```

The long-term implication for this project is that a model should not require all prior history to reconstruct the correct state. Instead, the substrate should adapt, and only the relevant state should be activated.

---

# 3. Biological inspiration, without literal biological simulation

We discussed that the brain has roughly 86 billion neurons, but that literal scale is not the point. The brain’s efficiency comes from sparse activation, local interaction, recurrent pathways, physical locality, low precision/noisy computation, local plasticity, modulatory learning signals, homeostasis, pruning, consolidation, and the fact that not every neuron is active at once.

The proposed artificial analogue is not “simulate every molecule.” Instead, abstract the right computational principles:

```text
persistent units
sparse edges
local state
activation traces
reward/error modulation
structural plasticity
homeostatic stabilization
recurrent traversal
consolidation and decay
```

---

# 4. Neuron and synapse as persistent adaptive objects

The project rejects the idea that an artificial neuron should only be:

```text
output = activation(weighted_sum(inputs))
```

Instead, a neuron-like unit should be conceptually closer to:

```text
Neuron {
    identity
    internal state
    activation dynamics
    memory trace
    input synapses
    output synapses
    plasticity rule
    excitability
    threshold
    stability
    energy budget
    growth/pruning policy
}
```

A synapse-like edge should be closer to:

```text
Synapse {
    source
    target
    weight
    eligibility trace
    plasticity rate
    confidence
    decay
    last activation
    inhibitory/excitatory type
}
```

The model at time `t` can be described as:

```text
M_t = (V_t, E_t, H_t, W_t, P_t)
```

Where:

- `V_t` = neuron-like units,
- `E_t` = connections,
- `H_t` = internal states,
- `W_t` = synaptic states/weights,
- `P_t` = plasticity policies.

Given an input:

```text
y_t, M_{t+1} = F(M_t, x_t, feedback_t)
```

The key is that:

```text
M_{t+1} ≠ M_t
```

The system changes over time.

---

# 5. Practical representation: conceptually object-like, physically array-backed

We discussed whether neurons could be literal objects stored in memory or graph database rows.

The conclusion:

> Conceptually, yes. Physically, not in the hot loop.

A naïve object-per-neuron and object-per-synapse representation would be too memory-heavy and inefficient due to object overhead, pointers, cache misses, garbage collection, and irregular access patterns.

The practical design should be:

```text
Graph/database layer:
    durable topology, metadata, checkpoints, experiment history

Array-backed runtime layer:
    compact contiguous arrays for neuron and synapse state

Sparse active computation layer:
    only active subgraphs are traversed

Commit/consolidation layer:
    important changes are persisted back
```

Implementation should favor structure-of-arrays:

```text
activation[unit_id]
threshold[unit_id]
trace[unit_id]
excitability[unit_id]

source[synapse_id]
target[synapse_id]
weight[synapse_id]
trace[synapse_id]
stability[synapse_id]
```

Not heavyweight objects in the runtime path.

---

# 6. Scale estimates

A full 86B-neuron model with biological-ish connectivity is likely hundreds of terabytes to multiple petabytes if synapses are represented explicitly.

But a smaller biologically inspired system is feasible.

Approximate scale tiers:

```text
Laptop prototype:
    1M–5M units
    32–128 edges/unit
    ~1–10 GB

Workstation prototype:
    10M–50M units
    64–256 edges/unit
    ~20–300 GB

Server prototype:
    100M–250M units
    100–1,000 edges/unit
    ~100 GB–8 TB

Fruit-fly-scale prototype:
    ~140k units
    ~50M edges
    ~1–8 GB depending representation
```

We concluded that a fruit-fly-scale system does **not** undermine the thesis. It makes the idea testable.

---

# 7. Core architectural principles

## 7.1 Sparse activation

Only a small subset of the network should be active during a task.

```text
cost ≈ active units + active edges
not total parameters
```

## 7.2 Recurrent traversal

The model should not merely classify from a fixed hidden representation. It should traverse learned paths.

```text
input activation -> active assembly -> recurrent transition -> next assembly -> output
```

## 7.3 Eligibility traces

During traversal, active pathways should leave temporary traces.

```text
if path participates:
    eligibility_trace += contribution
```

Later feedback determines whether those traces become durable learning.

## 7.4 Reward/error modulation

Learning should be modulated by feedback:

```text
weight_update = learning_rate × reward/error_signal × eligibility_trace
```

But our experiments so far show that the current reward gate is not yet strongly useful. It needs a task with noisy, delayed, ambiguous, or conflicting feedback.

## 7.5 Structural plasticity

The graph must be able to form, reinforce, weaken, and prune connections.

```text
successful path -> strengthen/stabilize
unused path -> decay
harmful path -> suppress/prune
co-active useful units -> possible new edge
```

## 7.6 Homeostasis

Recurrent systems can explode. Biological systems need threshold regulation, inhibition, refractory behavior, and gain control.

Our MNIST recurrent suite showed that removing homeostasis caused recurrent drive explosion and performance collapse.

## 7.7 Consolidation and decay

The model should distinguish temporary activation, short-term traces, medium-term memory, durable reasoning pathways, and stable identity/priors.

Episodic memory should fade. Useful reasoning should strengthen.

---

# 8. Experimental history and conclusions

## Experiment 1/2: Initial sparse plastic MNIST prototype

A structured Python prototype was created with sparse input-to-hidden connectivity, top-k hidden activation, hidden traces, threshold homeostasis, reward/novelty/confidence modulation, local plastic updates, SQLite/SQLAlchemy persistence, and MNIST data.

Result summary:

```text
Best test accuracy: ~92.25%
Latest test accuracy: ~91.90%
Train/window accuracy: ~98.20%
```

Interpretation:

- The model learned a real task.
- Confidence rose with accuracy.
- It was stable.
- But it likely behaved mostly like a sparse random-feature classifier with online plastic readout.
- It was not yet proof of recurrent graph reasoning.

Conclusion:

> Promising proof-of-life, but not yet fundamentally different enough from conventional shallow models.

---

## Experiment 3: Recurrent MNIST suite with ablations

Additions:

- hidden-to-hidden recurrent sparse edges,
- short multi-step traversal,
- recurrent plastic updates,
- ablation suite:
  - full recurrent plastic graph,
  - no recurrence,
  - frozen input projection,
  - no homeostasis,
  - no reward modulation.

Key results:

```text
no_reward_modulation: best test accuracy ~0.9285
no_recurrence_sparse_plastic_readout: ~0.9255
full_recurrent_plastic_graph: ~0.9230
frozen_input_projection: ~0.9225
no_homeostasis: collapsed to ~0.75 latest accuracy
```

Interpretation:

- Recurrence was present but weak.
- No-recurrence slightly beat the full recurrent model.
- Input-side plasticity was not strongly load-bearing.
- Reward modulation did not help.
- Homeostasis was strongly load-bearing for stability: without it, recurrent drive exploded.

Conclusion:

> MNIST does not strongly require recurrent traversal. The recurrent graph was not yet useful for the task, but homeostasis clearly matters once recurrence is introduced.

---

## Experiment 4: Successor traversal

This was the first task designed to actually require recurrence.

Training:

```text
learn local successor transitions:
0 -> 1
1 -> 2
2 -> 3
...
```

Testing:

```text
compose transitions to solve addition-like tasks:
2 + 3 = traverse successor 3 times -> 5
```

Variants:

- full traversal,
- no recurrence,
- no structural plasticity,
- no homeostasis,
- no reward gate.

Key results:

```text
exp4_full_traversal:
    transition accuracy: 1.0
    addition accuracy:   1.0

exp4_no_reward_gate:
    transition accuracy: 1.0
    addition accuracy:   1.0

exp4_no_homeostasis:
    transition accuracy: 1.0
    addition accuracy:   1.0

exp4_no_structural_plasticity:
    transition accuracy: ~0.0417
    addition accuracy:   ~0.0349

exp4_no_recurrence:
    transition accuracy: 0.0
    addition accuracy:   0.0
```

Interpretation:

- Recurrence became load-bearing.
- Structural plasticity became load-bearing.
- Recurrent drive was high in successful variants.
- Unique active units increased substantially during traversal.
- No-recurrence failed completely.
- No-structural-plasticity failed despite recurrent activity.

Conclusion:

> Experiment 4 is the first strong evidence for the core thesis: recurrent structural plasticity can create reusable paths that support composition.

Caveat:

- The task may be too easy.
- Reward gating was not proven useful.
- Homeostasis was not required in this clean symbolic task.

---

# 9. Current interpretation

The project has shown a progression:

```text
MNIST baseline:
    sparse plastic system can learn.

Recurrent MNIST:
    recurrence alone does not help on a task that does not need traversal;
    homeostasis prevents recurrent collapse.

Successor traversal:
    recurrence and structural plasticity are necessary when the task requires composition.
```

The most honest current conclusion:

> The architecture is not yet a general biological neural network, but it has now demonstrated a meaningful computational distinction: learned recurrent traversal over a structurally plastic graph can solve a compositional task that non-recurrent and non-structurally-plastic controls fail.

The core thesis remains viable.

---

# 10. What has not yet been proven

The following are still unproven:

- reward gating helps under realistic conditions,
- homeostasis helps in symbolic recurrent tasks under stress,
- the model can handle ambiguous contexts,
- the model can handle noisy or misleading feedback,
- the model can adapt after rule reversal,
- the model can bind concepts across modalities,
- the model can scale to more naturalistic datasets,
- the graph forms inspectable reusable abstractions rather than task-specific chains,
- the system can generalize beyond carefully constructed symbolic worlds.

---

# 11. Proposed next experimental roadmap

## Experiment 5: Contextual successor world

Purpose:

> Test whether the recurrent plastic graph can choose among multiple transition systems based on context.

Instead of one universal successor chain, introduce modes:

```text
Mode A: +1 successor
0 -> 1 -> 2 -> 3

Mode B: +2 successor
0 -> 2 -> 4 -> 6

Mode C: -1 predecessor
5 -> 4 -> 3 -> 2

Mode D: alternate/special route
custom transition table
```

Examples:

```text
mode=A, start=4, steps=3 -> 7
mode=B, start=4, steps=3 -> 10
mode=C, start=4, steps=3 -> 1
```

Why this matters:

- Same number can have different next states depending on context.
- The model must route, not merely build one chain.
- Inhibition and context selection become important.

Variants:

```text
full model
no recurrence
no structural plasticity
no reward gate
no homeostasis
no inhibition / no competition
no context routing
```

Metrics:

```text
accuracy by mode
accuracy by path length
wrong-route activation
path entropy
context confusion matrix
recurrent drive
unique active units
transition accuracy
composition accuracy
```

Expected result if thesis is supported:

```text
full model > no recurrence
full model > no structural plasticity
full model > no context routing
```

Reward gating may still not matter unless feedback is noisy or delayed.

---

## Experiment 5B: Noisy and delayed feedback

Purpose:

> Force reward modulation and eligibility traces to matter.

Add:

```text
90% correct feedback
10% misleading feedback
```

And/or delayed reward:

```text
no reward after intermediate steps
only reward after final answer
```

This tests whether the system can assign credit to the active path rather than blindly reinforce immediate associations.

Metrics:

```text
performance under noise
confidence calibration
recovery from misleading feedback
path stability
wrong-edge reinforcement rate
```

Expected result if reward gating is useful:

```text
full reward-gated model > no_reward_gate
```

---

## Experiment 5C: Rule reversal / adaptation

Purpose:

> Test plasticity without catastrophic destruction.

Phase 1:

```text
learn +1 successor
```

Phase 2:

```text
environment changes to +2 successor or reversed successor
```

Measure:

```text
adaptation speed
old-path decay
new-path formation
catastrophic interference
ability to preserve old mode if context-tagged
```

This directly tests:

> Memory can fade, but reasoning strengthens.

---

## Experiment 6: Multimodal number grounding

This is the proposed structured moonshot.

Purpose:

> Test whether the graph can bind the same latent concept across multiple modalities and then use recurrent traversal for operations.

Inputs:

```text
MNIST digit image
Arabic digit token: "3"
number word: "three"
dot pattern: •••
operator token: +, -, next, previous
```

Examples:

```text
MNIST(3) + text("four") -> 7
dots(••) + Arabic("5") -> 7
text("six") previous -> 5
MNIST(8) - dots(•••) -> 5
```

What this tests:

- cross-modal concept binding,
- shared number assemblies,
- recurrent operation traversal,
- compositional reasoning,
- generalization to held-out modality combinations.

Important train/test split:

```text
Train on some modality pairings:
    image + token
    word + dot

Test on held-out pairings:
    dot + image
    word + image
```

Expected result if thesis is supported:

> The system should activate shared number assemblies regardless of input modality, then perform the same recurrent traversal operation.

This is more meaningful than randomly mixing datasets because all modalities share a latent concept space.

---

## Experiment 7: Gridworld / embodied reward environment

Purpose:

> Test online learning, delayed reward, planning, state, and adaptation.

Environment ideas:

```text
MiniGrid-like world
symbolic maze
reward location changes
keys/doors
contextual rules
```

This is where the reward-center analogy becomes more real.

Metrics:

```text
episodes to solve
adaptation after reward relocation
path reuse
exploration/exploitation
catastrophic forgetting
recurrent planning traces
```

---

# 12. When to move to larger datasets

Do not scale just for scale.

Bad scaling path:

```text
MNIST -> CIFAR -> ImageNet
```

This mostly tests visual representation horsepower.

Better scaling path:

```text
single transition
-> compositional traversal
-> context-sensitive traversal
-> noisy feedback
-> delayed reward
-> multimodal concept binding
-> embodied action/reward environment
```

We should move to a larger dataset when at least three of these are true:

```text
1. Recurrence beats no-recurrence on composition.
2. Structural plasticity beats no-structural-plasticity.
3. Reward gating helps under noisy/delayed feedback.
4. Homeostasis prevents collapse under recurrent activity.
5. The model generalizes to held-out combinations.
6. We can inspect pathways and explain what changed.
```

Currently:

```text
1: yes, in Experiment 4
2: yes, in Experiment 4
3: not yet
4: yes, in MNIST recurrent suite; not needed in Experiment 4
5: partially, but only in synthetic successor composition
6: not sufficiently yet
```

Therefore:

> Run Experiment 5 before the larger multimodal moonshot, then proceed to Experiment 6.

---

# 13. Analytical framework going forward

For every experiment, compare against ablations:

```text
full model
no recurrence
no structural plasticity
no reward gate
no homeostasis
frozen input projection
no traces / no eligibility
no inhibition / no competition
```

Key metric categories:

## Performance

```text
accuracy
accuracy by path length
accuracy by context/mode
accuracy on held-out combinations
learning speed
adaptation speed
```

## Graph dynamics

```text
average recurrent drive
average unique active units
path entropy
edge utilization histogram
active unit diversity
recurrent edge concentration
class/concept-specific pathway overlap
```

## Plasticity

```text
edge growth rate
edge pruning rate
weight-change concentration
stability of reinforced paths
decay of unused paths
wrong-edge reinforcement rate
```

## Stability

```text
runaway recurrent drive
activation collapse
overconfidence
confidence calibration
train/test gap
performance after noisy feedback
```

## Interpretability

```text
Can we visualize learned chains?
Can we inspect paths used for a prediction?
Do correct paths become shorter/easier/lower energy?
Do wrong paths get suppressed?
Do modalities converge onto shared assemblies?
```

---

# 14. Current best project description

A concise description for future threads:

> We are developing a biologically inspired learning architecture based on a persistent sparse plastic graph. Instead of treating a model as a static field of learned matrices, we represent computation as traversal through adaptive neuron-like units and synapse-like edges. Units have state, traces, thresholds, and excitability. Edges have weights, traces, and plasticity. Learning occurs through recurrent traversal, eligibility traces, structural reinforcement, decay, and modulatory feedback. The goal is to test whether reasoning pathways can strengthen over time while episodic details fade.

Current results:

> MNIST experiments showed that sparse online plastic learning can reach ~92% test accuracy, but recurrence was not useful for that perceptual task. Ablations showed homeostasis prevents recurrent collapse. A successor traversal experiment then showed strong evidence for the core mechanism: full recurrent structural plasticity reached perfect compositional addition accuracy, while no-recurrence and no-structural-plasticity controls failed. This suggests recurrence and structural plasticity can be load-bearing when the task requires traversal.

Next step:

> Experiment 5 should introduce contextual successor systems, noisy/delayed feedback, and rule reversal to test reward gating, context-sensitive routing, inhibition, adaptation, and anti-forgetting. After that, Experiment 6 should attempt a structured multimodal number-grounding task using MNIST images, digit tokens, number words, dot patterns, and arithmetic operators.

---

# 15. Prompt to continue in a new thread

Use this prompt to restart the project elsewhere:

```text
We are continuing a project called Biological Neural Nets. The core thesis is that modern neural networks are mostly static parameter fields, while biological intelligence is a persistent adaptive substrate. We are building and testing a sparse plastic graph architecture where neuron-like units have internal state, thresholds, traces, and excitability, and synapse-like edges have weights, traces, and plasticity. The system learns through recurrent traversal, structural plasticity, reward/error modulation, homeostasis, consolidation, and decay.

Important principle: memory can fade, but reasoning should strengthen. Episodic traces should decay unless reinforced, while useful reasoning pathways should consolidate.

Experiments so far:

1. Sparse plastic MNIST prototype reached about 92% test accuracy. It proved the framework can learn online, but likely behaved mostly like a sparse random-feature classifier with plastic readout.

2. Recurrent MNIST suite added hidden-to-hidden recurrent edges and ablations. Recurrence did not improve MNIST, but no-homeostasis collapsed, showing homeostatic stabilization matters when recurrence is present.

3. Experiment 4 successor traversal trained local transitions like 0->1, 1->2, then tested compositional addition by repeated traversal. Full traversal, no-reward-gate, and no-homeostasis reached perfect transition and addition accuracy. No-recurrence got 0.0. No-structural-plasticity got about 0.035 addition accuracy. Conclusion: recurrence and structural plasticity are load-bearing when the task requires traversal. Reward gating and homeostasis are still not proven in this clean symbolic task.

Next planned phase:

Experiment 5: Contextual successor world. Create multiple transition systems selected by context/mode, e.g. mode A = +1, mode B = +2, mode C = -1. The same start number and step count should produce different answers depending on context. Add ablations: no recurrence, no structural plasticity, no reward gate, no homeostasis, no inhibition/context routing. Then extend with noisy feedback, delayed reward, and rule reversal to test reward gating, eligibility traces, adaptation, and anti-forgetting.

After Experiment 5:

Experiment 6: Structured multimodal number grounding. Inputs include MNIST images, digit tokens, number words, dot patterns, and arithmetic operator tokens. The goal is to bind different modalities to shared number assemblies, then perform recurrent traversal for operations. Train on some modality pairings and test on held-out modality combinations.

Please help continue from this point by designing and implementing Experiment 5 in clean Python with composable classes, SQLite/SQLAlchemy persistence, clear logging, ablation suite, analysis scripts, and README diagrams.
```

---

# 16. Immediate next implementation target

The next concrete deliverable should be:

```text
Experiment 5 package:
    contextual successor world
    noisy feedback option
    delayed reward option
    rule reversal option
    ablation suite
    analysis report
    diagrams
```

Suggested files:

```text
EXPERIMENT_5_CONTEXTUAL_SUCCESSOR.md
run_exp5_contextual_successor.py
run_exp5_suite.py
analyze_exp5_suite.py

plastic_graph_mnist/contextual_successor_task.py
plastic_graph_mnist/contextual_successor_graph.py
plastic_graph_mnist/contextual_successor_trainer.py
plastic_graph_mnist/inhibition.py
plastic_graph_mnist/context_router.py
```

Key outputs:

```text
exp5_report.md
exp5_comparison.csv
exp5_accuracy_by_mode.png
exp5_accuracy_by_path_length.png
exp5_context_confusion.png
exp5_recurrent_drive.png
exp5_wrong_route_activation.png
exp5_adaptation_curve.png
```

Primary hypothesis:

```text
The full recurrent structurally plastic graph should outperform no-recurrence and no-structural-plasticity variants on context-sensitive composition. Reward gating should begin to outperform no-reward-gate under noisy or delayed feedback. Homeostasis/inhibition should prevent recurrent route explosion when multiple paths compete.
```
