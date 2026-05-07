# Experiment 14 Validation Report

- Analysis directory: `analysis\exp14_full_20260507_210712`
- Status: **PASS**
- PASS: 27
- WARN: 0
- FAIL: 0

## Checks

| Status | Check | Detail |
|---|---|---|
| PASS | file exists: exp14_metrics.csv | analysis\exp14_full_20260507_210712\exp14_metrics.csv |
| PASS | file exists: metrics.csv | analysis\exp14_full_20260507_210712\metrics.csv |
| PASS | file exists: exp14_summary.csv | analysis\exp14_full_20260507_210712\exp14_summary.csv |
| PASS | file exists: exp14_effect_sizes.csv | analysis\exp14_full_20260507_210712\exp14_effect_sizes.csv |
| PASS | file exists: run_manifest.json | analysis\exp14_full_20260507_210712\run_manifest.json |
| PASS | file exists: progress.jsonl | analysis\exp14_full_20260507_210712\progress.jsonl |
| PASS | file exists: experiment_report.md | analysis\exp14_full_20260507_210712\experiment_report.md |
| PASS | metrics row count | 46080 rows |
| PASS | summary row count | 2304 rows |
| PASS | effect sizes row count | 12288 rows |
| PASS | required metric columns | missing=[] |
| PASS | required phases present | missing=[] |
| PASS | required variants present | missing=[]; hash_variants=['baseline_hash_slot_selector_div2', 'baseline_hash_slot_selector_div4', 'baseline_hash_slot_selector_div8'] |
| PASS | seed count nonzero | seed_count=20 |
| PASS | manifest experiment name | exp14_latent_context_inference |
| PASS | device metadata present | {"cpu_count": 12, "gpu_note": "This experiment is symbolic/table-based and runs on CPU; no GPU is required.", "gpu_used": false, "machine": "AMD64", "matplotlib_version": "3.10.9", "numpy_version": "2.4.4", "pandas_version": "3.0.2", "platform": "Windows-10-10.0.19045-SP0", "processor": "Intel64 Family 6 Model 63 Stepping 2, GenuineIntel", "python_version": "3.12.10 (tags/v3.12.10:0cc8128, Apr  8  |
| PASS | sqlite db exists | runs\exp14_full_20260507_210712.sqlite3 |
| PASS | sqlite tables | ["effect_sizes", "manifest", "metrics", "summary"] |
| PASS | oracle context upper bound solves clean seen routes | mean=1.0000 |
| PASS | CIRM latent selector identifies clean context | mean=1.0000 |
| PASS | CIRM latent selector composes clean seen routes | mean=1.0000 |
| PASS | shared no-context table underperforms clean seen routes | mean=0.0312 |
| PASS | endpoint memorizer fails suffix routes | mean=0.0000 |
| PASS | random selector below useful context selection | mean=0.0307 |
| PASS | corruption reduces or challenges CIRM context selection | clean=1.0000; max_corruption=0.5; corrupted=0.9416 |
| PASS | plots generated | 6 png files |
| PASS | progress has run_complete | events=46083 |
