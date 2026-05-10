# Table 3. Compact final-safe descriptive statistical summary

Status: compact main-text candidate, final-safe for descriptive manuscript use under the caveats below.

This compact table intentionally does not replace the generated statistical map at `docs/manuscript/tables/table_03_statistical_summary.md`. The generated map remains a detailed candidate/supplementary artifact until final seed-level grouping and effect-size comparison families are approved. This table is the safer main-text Table 3 path for the current manuscript pass.

| Claim | Experiment / slice | Descriptive result | Manuscript use | Status | Required caveat |
|---|---|---|---|---|---|
| C1-C4 | Exp13.1 core symbolic ablation; `exp13_1_full_20260506_214756` | Full model reaches route-table and composition accuracy 1.000. No-context binding is 0.364 route-table / 0.0467 composition. No recurrence at eval is 1.000 route-table / 0.0401 composition. No structural plasticity is 0.0286 route-table / 0.0317 composition. | Main-text descriptive support for Figure 2 and C1-C4. | `final_safe_descriptive` | Benchmark/model-family-specific descriptive summary only. Do not present as final effect-size evidence or universal neural-architecture necessity. |
| C5 | Exp12 clean supplied-context scaling; world_count 2/4/8/16/32; route_length 1/2/4/8/12 | Route-table and composition accuracy are 1.000 across the mirrored clean supplied-context grid used for Figure 3. | Main-text descriptive support for Figure 3 and C5. | `final_safe_descriptive` | Ceiling-limited supplied-context result through the tested range only. No fitted capacity law or broad generalization claim. |
| C6 | Exp13 global finite structural budget; world_count=32; route_length=12; budget_ratio 0.25/0.50/0.75/1.00/1.25 | Composition accuracy rises from 0.276 at budget_ratio=0.25 to 0.517 at 0.50, 0.758 at 0.75, and 1.000 at exact/surplus budget levels. | Descriptive support for finite-budget degradation; Figure 4 remains supplement-default unless emphasized. | `final_safe_descriptive_supplement_default` | Observed finite-budget degradation only. No fitted capacity law. Local-vs-global C7 is not promoted without paired seed-level analysis. |
| C13 | Exp14 symbolic transition-cue selection; world_count=32; route_length=16; cue_count=8; corruption_rate 0.00/0.10/0.25/0.50 | CIRM latent selector reaches 1.000 world-selection/seen-composition accuracy at corruption 0.00 and 0.10, 0.999 at 0.25, and 0.942 at 0.50. Oracle context-gated lookup remains 1.000. Shared no-context lookup fails first-step/seen-route metrics near chance while suffix probes can remain misleadingly high. | Main-narrow descriptive support for Figure 5 and C13. | `final_safe_descriptive` | Symbolic transition-cue selection only, not raw sensory latent-world discovery. Oracle context-gated lookup remains an upper-bound control. |

Source data: `docs/manuscript/source_data/table_03_compact_final_safe.csv`.

Detailed candidate map retained: `docs/manuscript/tables/table_03_statistical_summary.md`; `docs/manuscript/tables/table_03_statistical_summary.csv`.
