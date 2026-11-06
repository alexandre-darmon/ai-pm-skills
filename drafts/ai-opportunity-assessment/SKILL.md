---
name: ai-opportunity-assessment
description: 'Decide in one page whether an AI idea deserves a PRD and in which form (rule, workflow, LLM, ML, agent; build, buy, API). Use when someone asks "should we do this with AI?" or a use case is pitched.'
stage: strategy
version: 0.2.0
depends_on: []
feeds: [ai-moat-7-powers, llm-feature-prd, ai-act-classification]
autonomy_relevant: true
sources: [cagan-inspired, fitzpatrick-mom-test, own-enterprise-checklist, repo-chanmeng, repo-vishalhabib]
eval_threshold: 0.80
status: draft
---

# ai-opportunity-assessment

## When to use
- A sponsor or business team pitches a use case "with AI".
- A vendor demo lands and someone asks whether to buy it.
- A team asks whether a problem needs an LLM, classic ML, an agent or nothing.
- Do not use once the go is decided: write the PRD with `llm-feature-prd`.
- Do not use for a feature with no AI component: a standard business case is enough.

## Inputs
Mandatory: the problem in the business's words, who suffers it and how often, the current process and its cost.
Ask if missing: data available (source, volume, quality, access), constraints (sovereignty, latency, languages), risk context (personal data, regulated domain).
If the data situation is unknown, score readiness as unknown and the decision can only be explore.

## Method
1. Restate the problem in one sentence and the evidence that it is real: frequency, cost, who complained. A problem stated only as "use AI for X" is not yet a problem; ask what hurts.
2. Name the non-AI alternative first: a rule, a SQL query, a form, a process change. State how far the rule goes: n of N cases and how those cases were chosen (for instance the last 200 in the queue), or write `unmeasured` and what the claim rests on (the team's stated criteria, a past attempt). An unmeasured claim does not block the decision; the next step then measures it. If a deterministic rule covers about 80% of cases, the decision is no-go on AI and the rule is the recommendation.
3. Score data readiness 0–5 on five axes: availability, volume, quality, access rights, labels or ground truth. Give the mean as `x/5`. Below 2/5 the decision cannot be go: it is explore (a data task first) or no-go.
4. Compare feasibility by approach, simplest first: rule, workflow with an AI step (fixed path, the model judges at one node), single LLM call, RAG (the answer sits in documents), classic ML, agent. Pick the simplest that meets the need and say why the simpler ones fall short. An agent needs three things at once, each shown from the brief: no fixed path exists, its next step depends on what it observes, and its actions change a system. If the steps can be drawn in advance, it is a workflow: call it that.
5. Recommend build, buy or API with the reason (data sensitivity, differentiation, time to value, run cost).
6. State the cost of a wrong answer: what breaks, who catches it and how long it stays uncaught. Then give the target autonomy level for the use case as a whole, as defined in references/autonomy-ladder.md (read it first). That cost caps the level: if a wrong output can reach a customer or become irreversible before anyone sees it, L3 and above are out, whatever accuracy is hoped for. A low tolerance for error changes the design (cited sources, human confirmation), not by itself the decision. Start low: a new use case rarely launches above L2.
7. Flag first risks: personal data, employees affected, a possible AI Act high-risk domain. Hand over to `ai-act-classification` when one is flagged.
8. Decide: go, no-go or explore, with the next step and its owner. Any gain mentioned follows references/roi-model.md (volume × quality × unit value − run cost − change cost) or is left out.

## Output
`templates/assessment.md`, one page, all headings present. The decision line reads `Decision: go`, `Decision: no-go` or `Decision: explore`.

## Rules and red lines
- No go when a deterministic rule solves about 80% of the cases.
- No go when data readiness is below 2/5.
- Always name the non-AI alternative, even on a go.
- No claim of rule coverage without n of N or the word unmeasured.
- No target level without the cost of a wrong answer and who catches it.
- No gain without its ROI lines; no free-floating percentage.

## Links
references/autonomy-ladder.md · references/roi-model.md · llm-feature-prd · ai-act-classification · ai-moat-7-powers

## Sources
- cagan-inspired: value and feasibility risks structure the assessment.
- fitzpatrick-mom-test: evidence that the problem is real comes from past behaviour, not opinions.
- own-enterprise-checklist: the five readiness axes and the rule-first test.
- repo-chanmeng: approaches chosen from the most certain side, agent conditions, error tolerance changing the design (ideas only).
- repo-vishalhabib: stating the sample behind a claim before relying on it (idea adapted).
