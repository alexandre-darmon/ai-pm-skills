---
name: release-to-production
description: 'Plan the release of an AI change (prompt, model, KB) through offline eval, shadow, canary and A/B if the sample allows. Use for "can we ship this?" or a provider model update.'
license: CC-BY-4.0
metadata:
  stage: "evaluate"
  version: "0.3.2"
  status: "tested"
  eval_threshold: "0.80"
  autonomy_relevant: "true"
  depends_on: "build-evals, system-prompt-and-guardrails, prototype-handover"
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
For an engineering rebuild of a prototype: the handover file (frozen suite, baseline per class) and the PRD's scenarios.

## Method
1. Acceptance of the build, read-only. When engineering rebuilt a prototype, run the PRD's pre-declared scenarios and the frozen suite from the `prototype-handover` file on the engineering build, before any shadow or canary. Nobody edits a case, a grader or a bar during acceptance. Report per class against the handover baseline: this run is the release evidence, the prototype baseline only the floor it is read against. A failed scenario goes back to engineering with the failing cases.
2. Offline gate before any online step. A version below the threshold or below the current version is not released, and it gets no online step either: no partial rollout, no route for some classes until per-class evidence clears both bars. Write the diagnostic instead of a plan: which classes fell, weighted by the severity of their errors and not only by count, what changed in the bundle, and the way back (fix, rerun, clear both bars). Give the reason in the user's terms (users would get a worse version than today's), not as a rule of some process they never stated.
3. Version bundle: a version is one pinned set of prompt, dated model snapshot (never a `latest` alias), parameters, tool definitions and KB snapshot. Open the plan with which parts differ from production, because the risk is one part moving silently.
4. Autonomy level: state the level of each step the release touches (`references/autonomy-ladder.md`), or ask for it. If the release raises a step's level or touches a step above L2, list that level's gate facts from the ladder with their measured values. A missing fact blocks the level change: ship at the current level or hold.
5. Shadow: run the new version on live traffic with no user effect; state duration and comparison metric. Shadow shows output differences, guardrail hits, latency and cost; it cannot measure an outcome that needs the user to act on the answer, so say what it cannot prove. Copied live traffic is personal data: same retention, access and provider terms as production.
6. Canary: share of traffic, guardrail metrics, automatic rollback triggers as numbers. On a small population a canary only catches large harm: say roughly what drop it can see, and never present it as proof of a lift.
7. Rollback: answer to which bundle, how long, who, what happens to data and actions written meanwhile, and when it was last rehearsed and how long that took. With pinned bundles it is a pointer change; because outputs vary, verify it on a sample of the eval set, not one query. Name the agent writes that cannot be undone. A retired provider model stops being a target, so give the date rollback ends. Never rehearsed: rehearse before canary.
8. A/B only if the sample allows. Compute it: n per arm ≈ 16 × p(1−p) / δ² (80% power, 5% significance), with p the baseline rate and δ the lift sought. Count units at the randomisation level, usually the user. With returning users, waiting adds tasks but not new independent users: the population is the upper bound on units. Repeated tasks per user add power only as far as within-user correlation allows (design effect 1 + (m−1) × ICC, m tasks per user); state the ICC assumed. If it does not fit a reasonable window, decide: write that A/B is infeasible, fall back on shadow plus canary, and say the lift will not be proven. A verdict left conditional on figures nobody has leaves the reader with no plan.
9. The production metric is a business outcome, not a judge score.
10. A provider model update is a release, with the same path. Plan backward from the deprecation date (for example, shadow starts at least N weeks before it), and do not state today's date or the runway left unless the user gave them: a wrong calendar is worse than a relative one.
11. Name the decision owner, the sign-offs a regulated organisation usually needs before go-live (risk or compliance, data protection if the data use changes), and the post-release review date. Update the card with `model-card-ai-registry`.

## Output
`templates/release-plan.md`, all headings present for a release. The decision line reads `Decision: release`, `Decision: hold` or `Decision: release after shadow`. A hold carries the offline result, the diagnostic and the decision only. Every figure comes from the user or is labelled as an assumption; argue from reasons, never from "the skill" or a policy the user did not mention.

## Rules and red lines
- Offline eval before any online step; for a rebuilt prototype, read-only acceptance of the build before both.
- No A/B without the sample-size calculation shown.
- Automatic rollback triggers are numbers.
- A provider model change is never swapped directly.
- An unrehearsed rollback does not count as rollback capability.
- L5 bandit switching only when L4 is stable and documented.

## Links
references/autonomy-ladder.md · build-evals · prototype-handover · assistant-kpis-cost-per-outcome · model-card-ai-registry

## Sources
- kohavi-experiments: sample-size rule and A/B pitfalls.
- own-release-practice: rung choice by traffic.
- repo-chanmeng: version bundle and rollback questions.
