# Tracker Update — Experiment 11

## Experiment

Experiment 11 — Context-Separated Memory and Non-Destructive Rebinding

## Question

Can higher-order world context separate multiple route systems over the same symbolic substrate so that new rule worlds can be learned without destroying old ones?

## Prior result motivating this

Experiment 10 demonstrated adaptive route reversal and a clear stability-plasticity tradeoff. However, ordinary same-context reversal mostly overwrote old rules. The dual-context result hinted that both A and B could coexist after switchback, but the protocol did not cleanly test non-destructive retention during initial B acquisition.

## Design

Phases:

1. Sequential A then B training, evaluating A and B throughout B acquisition.
2. Alternating A/B training.
3. Multi-world scaling with A/B/C/D.
4. Context retrieval robustness under world-context bleed/dropout.

Key variants:

- full context-separated memory
- world-gated plasticity
- no world context
- no context binding
- no inhibition
- no structural plasticity
- no consolidation
- strong consolidation
- shared edges only

## Expected belief update

A positive result would move the project from adaptive route overwrite toward context-separated adaptive memory.

A negative result would suggest the architecture can learn and adapt route fields, but cannot yet preserve multiple rule systems without manual substrate isolation or rehearsal.
