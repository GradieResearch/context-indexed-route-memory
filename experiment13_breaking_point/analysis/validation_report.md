# Experiment 13 Validation Report

## PASS: all phases executed

Found phases: ['capacity_pressure', 'context_corruption', 'continual_retention_pressure', 'continuous_frontend_bridge', 'local_capacity_pressure', 'true_holdout_generalization']

## PASS: full model succeeds at exact/surplus capacity

mean=1.0000

## PASS: finite memory pressure creates a breaking curve

low=0.3939, exact=1.0000

## PASS: no-recurrence separates one-step storage from composition

route_table=1.0000, multi_comp=0.0427

## PASS: no-world-context shows interference

no_world_context=0.0694, full=1.0000

## PASS: adversarial context corruption creates world-selection failure

low=1.0000, high=0.0000

## PASS: primitive holdout separates composition from unseen-transition inference

seen=0.8924, unseen=0.0747

## PASS: continuous front-end degrades under perceptual noise

low=1.0000, high=0.3841

## WARN: consolidation changes finite-pressure behavior

no_consolidation=0.7661, strong=0.7676, delta=0.0016

## Summary

- pass: 8
- warn: 1
- fail: 0