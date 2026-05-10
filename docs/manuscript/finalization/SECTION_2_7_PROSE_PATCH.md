# Section 2.7 Prose Patch

Date: 2026-05-10

Status: ready-to-apply manuscript patch.

Purpose: preserve the human decision to convert `docs/manuscript/closest_prior_art_table.md` into prose in Section 2.7, while retaining the table as a companion source artifact.

This patch exists because the manuscript file is large and should be edited carefully without replacing unrelated manuscript content. The prose below is derived from `docs/manuscript/closest_prior_art_table.md` and `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md`.

## Replace current Section 2.7 with this text

```markdown
### 2.7 Closest prior-art positioning and narrow contribution

The contribution is best described as a controlled route-memory decomposition, not as novelty of any single mechanism. Context gating, recurrence, modular routing, differentiable or external memory, fast weights, graph reasoning, and hippocampal indexing all have substantial prior art. The present benchmark deliberately puts these ideas into a narrow symbolic transition setting where each can be probed separately: one-step transition storage, recurrent route execution, supplied versus selected context, endpoint memorization, suffix-route composition, finite structural budget pressure, and minimal neural comparator behavior.

This framing is important after Exp13.2 and Exp15. Exp13.2 shows that an oracle context-gated transition table can match the full model in the clean supplied-context setting. Exp15 shows that a conventional context-conditioned neural transition learner and a world-head transition learner can solve the clean hard slice when context is supplied. Therefore, clean ceiling accuracy with supplied world labels is not the novelty claim.

The manuscript’s narrow contribution is the evidence map: it shows where different computational contracts diverge under controlled interference. Endpoint memorization, reusable one-step transition learning, recurrent rollout, no-context sharing, supplied context, selected symbolic context, finite structural budget, and parameter/world-head isolation produce different failure modes. The paper should therefore be read as a mechanism-sensitive benchmark and decomposition study rather than a claim that CIRM invents context gating, recurrence, neural memory, modular routing, graph reasoning, biological indexing, or general neural superiority.

The companion source artifact for this positioning is `docs/manuscript/closest_prior_art_table.md`. It should remain available for reviewer-facing traceability and possible later conversion into a venue-specific table or supplement.
```

## Removal target

Remove the old Section 2.7 TODO block, especially the text that says:

```markdown
[TODO: Before submission, add a “closest prior-art risk” table covering task-gated lookup, mixture-of-experts routing, fast weights/linear attention, differentiable external memory, neural algorithmic reasoning, hippocampal scaffold memory, symbolic graph/path algorithms, and memory-augmented neural baselines.]
```

## Guardrails

- Do not create a final bibliography file yet.
- Do not invent target-venue citation formatting.
- Do not broaden claims beyond the controlled benchmark/evidence-map posture.
- Preserve Exp13.2 and Exp15 caveats.
- Keep `docs/manuscript/closest_prior_art_table.md` as the companion artifact.
