---
name: llm-feature-prd
description: Write the PRD for an LLM feature with autonomy level per step, failure paths, eval plan and guardrails. Use when asked for the PRD of anything that generates, extracts, classifies or acts.
license: CC-BY-4.0
metadata:
  stage: "specify"
  version: "0.3.0"
  status: "tested"
  eval_threshold: "0.80"
  autonomy_relevant: "true"
  depends_on: "ai-opportunity-assessment, ai-feasibility-spike"
  feeds: "build-evals, error-analysis, system-prompt-and-guardrails, ai-data-requirements, ai-act-classification"
  sources: "cagan-inspired, torres-continuous-discovery, own-prds, repo-chanmeng, spec-kit"
---

# llm-feature-prd

## When to use
- A go from `ai-opportunity-assessment`, or a sponsor asks for "the PRD".
- The feature generates, extracts, classifies, retrieves or acts with an LLM.
- An engineering lead needs a spec they can build and an evaluator can test.
- Do not use for a non-AI feature: a generic PRD template is enough.
- Do not use before the problem is validated: run `ai-opportunity-assessment` first.

## Inputs
Mandatory: problem statement, target users, success metric (an outcome, not usage), constraints (latency, cost per call, sovereignty, languages).
Ask if missing: data sources, current process and its cost, risk context (personal data, regulated domain).
Optional: the spike report from `ai-feasibility-spike` (n of N per class, cost per correct answer, failure classes). It seeds the eval stub and the open questions; its numbers are never release evidence.
A usage metric (questions answered, sessions, active users) is not an outcome: treat it as missing.
If the outcome metric is missing, ask for it and stop, even when asked to skip questions or to add metrics later. Do not write the PRD around a placeholder; offer instead the problem statement and the list of what is missing.

## Method
1. Restate the problem and the outcome metric in one sentence each. Refuse to continue without an outcome metric.
2. List the steps the feature performs. Assign an autonomy level L0–L5 per step, as defined in references/autonomy-ladder.md (read it first: levels, gates, rules). Say why each step is not at L+1. Give each step its launch level and its path, one level at a time with the gate for each move (e.g. L2 → L3 → L4). Say whether each step's effect can be undone, and by whom: an LLM error on a step that cannot be undone has no second chance.
3. Write the happy path, then the four failure paths: wrong answer, no answer, out-of-scope request, prompt injection (instructions hidden in the input or a retrieved document). Say what the user sees and what the system does in each.
4. Write the eval stub: what "correct" means per step, how cases are sampled, who labels, the threshold to beat. For generated text (summaries, drafts, answers), name the reference outputs written by domain experts and the grading rubric a judge or reviewer applies. Write each criterion and gate as one testable line (step, metric, threshold, sample size), so a spec-driven coding workflow such as a Spec Kit constitution can import them unchanged. Hand over to `build-evals`.
5. List guardrail requirements per layer: input, output, action. Any step at L3 needs tested output guardrails; any step at L4 needs action guardrails (scope, caps, approvals). Add one Never line under Non-goals: the actions the feature must be unable to take, stated as absent from its tools and credentials, because a prompt instruction can fail. Hand over to `system-prompt-and-guardrails`, which owns enforcement.
6. Point to data requirements and compliance flags: personal data, high-risk domain, employee impact. Hand over to `ai-data-requirements` and `ai-act-classification`.
7. Define KPIs as outcomes, each with a quality KPI beside any usage KPI. Define the rollout path: shadow, then canary, then general availability, with the gate for each.
8. Carry over the stop conditions from `ai-opportunity-assessment`, or write them if there were none: a model can sit just under its threshold for months with nobody empowered to end the project. Each names a metric, a threshold, where and when it is read, and the action. Also state what moves the feature to the next stage: date, metric, value, sample size. These end the project; rollback of a bad canary belongs to `release-to-production`.
9. List open questions with an owner each.

## Output
A PRD following `templates/prd.md`: all headings present, no empty section. Sections that cannot be filled yet say what is missing and who provides it.

## Rules and red lines
- No PRD without an eval section.
- No step without an autonomy level.
- No usage KPI without an outcome KPI beside it.
- No gain stated without volume × quality × unit value behind it (references/roi-model.md); remove or rewrite free-floating percentages.
- Never skip a level in production: a step moves one level at a time (L2 → L3 → L4), each move behind its own gate. A step that issues payments, refunds or other irreversible actions launches at L2 at most.

## Links
references/autonomy-ladder.md · references/roi-model.md · ai-feasibility-spike · build-evals · system-prompt-and-guardrails · ai-data-requirements · ai-act-classification

## Sources
- cagan-inspired: product risks (value, usability, feasibility, viability) frame the failure paths.
- torres-continuous-discovery: outcome over output for the KPI section.
- own-prds: section structure and the eval-stub practice.
- spec-kit: eval criteria and gates written so a project constitution can import them.
- repo-chanmeng: stop conditions with metric, threshold, observation point and action; reversibility per action; a never list.
