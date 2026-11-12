---
name: release-to-production
description: 'Plan the release of an AI change (prompt, model, KB) through offline eval, shadow, canary and A/B if the sample allows. Use for "can we ship this?" or a provider model update.'
license: CC-BY-4.0
metadata:
  stage: "evaluate"
  version: "0.2.0"
  status: "tested"
  eval_threshold: "0.80"
  autonomy_relevant: "true"
  depends_on: "build-evals, system-prompt-and-guardrails"
  feeds: "assistant-kpis-cost-per-outcome, model-card-ai-registry"
  sources: "kohavi-experiments, own-release-practice, repo-chanmeng"
---

# release-to-production

## When to use
- A new prompt, model, knowledge base or skill version is ready, or someone asks "can we ship this?".
- A provider announces a model update or a deprecation.
- Do not use to build the eval suite: use `build-evals`.
- Do not use to choose between models: use `model-selection`.

## Inputs
Mandatory: the offline suite result for the new version, the traffic, the business metric.
Ask if missing: the metric's baseline rate or variance, rollback capability and its last rehearsal, autonomy level.

## Method
1. Offline gate first, always. A version below the threshold or below the current version is not released: write the diagnostic (which classes fell, what changed) instead of a plan.
2. Version bundle: a version is one pinned set of prompt, dated model snapshot (never a `latest` alias), parameters, tool definitions and KB snapshot. Open the plan with which parts differ from production, because the risk is one part moving silently.
3. Autonomy level: state the level of each step the release touches (`references/autonomy-ladder.md`), or ask for it. If the release raises a step's level or touches a step above L2, list that level's gate facts from the ladder with their measured values. A missing fact blocks the level change: ship at the current level or hold.
4. Shadow: run the new version on live traffic with no user effect; state duration and comparison metric.
5. Canary: share of traffic, guardrail metrics, automatic rollback triggers as numbers.
6. Rollback: answer to which bundle, how long, who, what happens to data and actions written meanwhile, and when it was last rehearsed and how long that took. With pinned bundles it is a pointer change; because outputs vary, verify it on a sample of the eval set, not one query. Name the agent writes that cannot be undone. A retired provider model stops being a target, so give the date rollback ends. Never rehearsed: rehearse before canary.
7. A/B only if the sample allows. Compute it: n per arm ≈ 16 × p(1−p) / δ² (80% power, 5% significance), with p the baseline rate and δ the lift sought. Compare with the eligible units per period. If it does not fit a reasonable window, say A/B is infeasible and fall back on shadow plus canary.
8. The production metric is a business outcome, not a judge score.
9. A provider model update is a release, with the same path; plan before the deprecation date.
10. Name the decision owner and the post-release review date. Update the card with `model-card-ai-registry`.

## Output
`templates/release-plan.md`, all headings present for a release. The decision line reads `Decision: release`, `Decision: hold` or `Decision: release after shadow`. A hold carries the offline result, the diagnostic and the decision only.

## Rules and red lines
- Offline eval first, always.
- No A/B without the sample-size calculation shown.
- Automatic rollback triggers are numbers.
- A provider model change is never swapped directly.
- An unrehearsed rollback does not count as rollback capability.
- L5 bandit switching only when L4 is stable and documented.

## Links
references/autonomy-ladder.md · build-evals · assistant-kpis-cost-per-outcome · model-card-ai-registry

## Sources
- kohavi-experiments: sample-size rule and A/B pitfalls.
- own-release-practice: rung choice by traffic.
- repo-chanmeng: version bundle and rollback questions.
