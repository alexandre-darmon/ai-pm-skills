---
name: ai-opportunity-assessment
description: 'Decide in one page if an AI idea deserves a PRD, in which form, and what to ask the sponsor: a dated pilot, stop conditions, an evidence plan. Use for "should we do this with AI?" or an AI pitch.'
license: CC-BY-4.0
metadata:
  stage: "specify"
  version: "0.4.0"
  status: "tested"
  eval_threshold: "0.80"
  autonomy_relevant: "true"
  depends_on: ""
  feeds: "llm-feature-prd, ai-feasibility-spike, build-evals, ai-act-classification, ai-roi-quantification"
  sources: "cagan-inspired, fitzpatrick-mom-test, miller-error-bars, own-enterprise-checklist, repo-chanmeng, repo-vishalhabib, repo-yoseph"
---

# ai-opportunity-assessment

## When to use
- A sponsor or business team pitches a use case "with AI", or a vendor demo lands and someone asks whether to buy it.
- A team asks whether a problem needs an LLM, classic ML, an agent or nothing.
- An AI initiative needs a sponsor's money or a comex slot: the one-pager, the pitch, the ask.
- A draft pitch or business case for an AI project carries a gain nobody can trace.
- Do not use once the go is decided and the pilot funded: write the PRD with `llm-feature-prd`.
- Do not use to compute the return of a system already live: that is `ai-roi-quantification`.
- Do not use to build or run the prototype itself on the model: that is `ai-feasibility-spike`.

## Inputs
Mandatory: the problem in the business's words, who suffers it and how often, the current process and its cost.
Ask if missing: data available (source, volume, quality, access), constraints (sovereignty, latency, languages), risk context (personal data, regulated domain), any quality already measured (on how many cases, chosen how), and, when money is asked, the audience and the date of the decision.
If the data situation is unknown, score readiness as unknown and the decision can only be explore. If volume, quality or unit value is unknown, the gain is not computable yet: measuring it becomes the evidence plan.

## Method
1. Restate the problem in one sentence and the evidence that it is real: frequency, cost, who complained. A problem stated only as "use AI for X" is not yet a problem; ask what hurts.
2. Name the non-AI alternative first: a rule, a SQL query, a form, a process change. State how far the rule goes: n of N cases and how those cases were chosen (for instance the last 200 in the queue), or write `unmeasured` and what the claim rests on (the team's stated criteria, a past attempt). An unmeasured claim does not block the decision; the next step then measures it. If a deterministic rule covers about 80% of cases, the decision is no-go on AI and the rule is the recommendation.
3. Score data readiness 0–5 on five axes: availability, volume, quality, access rights, labels or ground truth. Give the mean as `x/5`. Below 2/5 the decision cannot be go: it is explore (a data task first) or no-go.
4. Compare feasibility by approach, simplest first: rule, workflow with an AI step (fixed path, the model judges at one node), single LLM call, RAG (the answer sits in documents), classic ML, agent. Pick the simplest that meets the need and say why the simpler ones fall short. An agent needs three things at once, each shown from the brief: no fixed path exists, its next step depends on what it observes, and its actions change a system. If the steps can be drawn in advance, it is a workflow: call it that.
5. Recommend build, buy or API with the reason (data sensitivity, differentiation, time to value, run cost).
6. State the cost of a wrong answer: what breaks, who catches it and how long it stays uncaught. Then give the target autonomy level for the use case as a whole, as defined in references/autonomy-ladder.md (read it first). That cost caps the level: if a wrong output can reach a customer or become irreversible before anyone sees it, L3 and above are out, whatever accuracy is hoped for. A low tolerance for error changes the design (cited sources, human confirmation), not by itself the decision. Start low: a new use case rarely launches above L2.
7. Flag first risks: personal data, employees affected, a possible AI Act high-risk domain. Name them on the page before any ask: a sponsor who learns them later withdraws. Each goes to its owner with the question to settle before money is spent: `ai-act-classification` and counsel for the classification, the DPO for personal data.
8. Decide: go, no-go or explore, with the next step and its owner. On explore, when the open question is whether the model can do the task well enough and at what cost, the next step is a time-boxed spike with `ai-feasibility-spike`; when it is a data gap, it is the data task from step 3.
9. Anchor every number. A gain is volume × quality × unit value − run cost − change cost (references/roi-model.md). Before deployment it is a projection: label it and give a low and a high value for its weakest line. When that line is a measured rate, take the bounds of its 95% interval (references/eval-statistics.md): 82% on 200 test cases reads 76% to 87%. A percentage with no lines behind it is rewritten from the lines or removed, and the page says which. Testers liking a prototype is not quality: quality is the share of sampled outputs judged correct. Hours freed are capacity, not cash, until someone removes a cost. Show what the sponsor is choosing between: the ask, doing nothing, the non-AI alternative, with figures where known and "not costed" elsewhere.
10. On go or explore, write the evidence plan that will decide go or stop:
    - the deciding metric per question class: quality on the classes that carry the cost of a wrong answer (step 6), plus the baseline lines still unknown (volume today, time per case, current error rate);
    - the number of cases per class, sized for the decision (references/eval-statistics.md): about 60 read a rate near 80% within ±10 points, about 35 a rate near 90%. Where a false pass is costly, the go reads the lower bound of the interval, not the point estimate;
    - where the cases come from (real, sampled how), who labels them, by which date, who reads the result.
    Thresholds are written and signed before the run. Hand the plan to `build-evals` for the set, graders and baseline. If the traffic cannot fill the cases by the date, say so and move the date, never the bar.
11. Write one dated ask: what, how much, for how long, decided by whom, by which date. While the gain is a projection or unmeasured, the ask is a measurement pilot or the data task from step 3, never a rollout or a programme; the rollout is the next ask, made on the pilot's evidence.
12. Write the stop conditions with the ask, before any money is spent. Each names a metric, a threshold, where and when it is read (which set or sample, which date) and the action if it fails: stop, shrink, or back to explore. It reads yes or no. Without a baseline, the threshold may stay a bracket to settle before funding; the metric, the date and the action may not. A success criterion with no stop leaves a pilot with no end. `llm-feature-prd` step 8 carries the stop conditions over as written; `ai-roi-quantification` checks them later.
13. Answer the AI-specific objections a sponsor will raise (wrong answers, a vendor's demo score, staff replaced, data leaving the company) with a fact from the page or the evidence-plan item that will produce it. A vendor's score counts only on your cases, with their number.

## Output
`templates/assessment.md`, all headings present; one page, two with an ask. The decision line reads `Decision: go`, `Decision: no-go` or `Decision: explore`. With an ask, it reads `Ask: <pilot or data task>, <amount>, <duration>, decided by <who> on <date>.` and each stop condition `Stop if <metric> <threshold> on <set or sample> at <date>: <action>.`

## Rules and red lines
- No go when a deterministic rule solves about 80% of the cases.
- No go when data readiness is below 2/5.
- Always name the non-AI alternative, even on a go.
- No claim of rule coverage or of quality without n of N, or the word unmeasured.
- No target level without the cost of a wrong answer and who catches it.
- No gain without its five lines; no free-floating percentage; before deployment, a gain is a projection with a low and a high value.
- One dated ask. While the gain is unmeasured it is a pilot or a data task, never a rollout.
- No pilot without a stop condition: metric, threshold, where and when read, action.
- No pass rate in the evidence plan without its number of cases.
- Never call the initiative compliant: risk flags go to `ai-act-classification`, counsel and the DPO.

## Links
references/autonomy-ladder.md · references/roi-model.md · references/eval-statistics.md · llm-feature-prd · ai-feasibility-spike · build-evals · ai-act-classification · ai-roi-quantification

## Sources
- cagan-inspired: value and feasibility risks structure the assessment.
- fitzpatrick-mom-test: evidence that the problem is real comes from past behaviour, not opinions.
- miller-error-bars: sizing the evidence before the run; a measured quality carries its interval.
- own-enterprise-checklist: the five readiness axes, the rule-first test and the single dated ask, from assessments run with business sponsors.
- repo-chanmeng: approaches chosen from the most certain side, agent conditions, error tolerance changing the design, stop conditions written before funding, the ask compared with its alternatives (ideas only).
- repo-vishalhabib: stating the sample behind a claim before relying on it (idea adapted).
- repo-yoseph: low and high values on a business case's weak drivers.
