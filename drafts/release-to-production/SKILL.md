---
name: release-to-production
description: 'Plan the release of an AI change (prompt, model, KB) through offline eval, shadow, canary and A/B if the sample allows. Use for "can we ship this?" or a provider model update.'
stage: measure
version: 0.1.0
depends_on: [build-evals, system-prompt-and-guardrails]
feeds: [assistant-kpis-cost-per-outcome, model-card-ai-registry]
autonomy_relevant: true
sources: [kohavi-experiments, own-release-practice]
eval_threshold: 0.80
status: draft
---

# release-to-production

## When to use
- A new prompt, model, knowledge base or skill version is ready, or someone asks "can we ship this?".
- A provider announces a model update or a deprecation.
- Do not use to build the eval suite: use `build-evals`.
- Do not use to choose between models: use `model-selection`.

## Inputs
Mandatory: the offline suite result for the new version, the traffic, the business metric.
Ask if missing: the metric's baseline rate or variance, rollback capability, autonomy level.

## Method
1. Offline gate first, always. A version below the threshold or below the current version is not released: write the diagnostic (which classes fell, what changed) instead of a plan.
2. Shadow: run the new version on live traffic with no user effect; state duration and comparison metric.
3. Canary: share of traffic, guardrail metrics, automatic rollback triggers as numbers, one-click rollback.
4. A/B only if the sample allows. Compute it: n per arm ≈ 16 × p(1−p) / δ² (80% power, 5% significance), with p the baseline rate and δ the lift sought. Compare with the eligible units per period. If it does not fit a reasonable window, say A/B is infeasible and fall back on shadow plus canary.
5. The production metric is a business outcome, not a judge score.
6. A provider model update is a release, with the same path; plan before the deprecation date.
7. Name the decision owner and the post-release review date. Update the card with `model-card-ai-registry`.

## Output
`templates/release-plan.md`, all headings present. The decision line reads `Decision: release`, `Decision: hold` or `Decision: release after shadow`.

## Rules and red lines
- Offline eval first, always.
- No A/B without the sample-size calculation shown.
- Automatic rollback triggers are numbers.
- A provider model change is never swapped directly.

## Links
references/autonomy-ladder.md · build-evals · assistant-kpis-cost-per-outcome · model-card-ai-registry

## Sources
- kohavi-experiments: sample-size rule and A/B pitfalls.
- own-release-practice: rung choice by traffic.
