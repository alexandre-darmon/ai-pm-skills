---
name: system-prompt-and-guardrails
description: 'Write an LLM feature''s system prompt and its input, output and action guardrails with budgets and a redteam set. Use for a first prompt, a jailbreak found, or an agent given tools.'
stage: build
version: 0.1.0
depends_on: [llm-feature-prd, agent-design-and-tooling]
feeds: [build-evals, release-to-production, ai-act-classification]
autonomy_relevant: true
sources: [owasp-llm-top10, eu-ai-act, own-guardrails]
eval_threshold: 0.80
status: draft
---

# system-prompt-and-guardrails

## When to use
- A first system prompt is drafted for an LLM feature or an agent.
- A jailbreak or an injection was found, or the false-positive rate of a guardrail is disputed.
- An agent gets tools, or a step moves up the autonomy ladder.
- Do not use to write the PRD itself: use `llm-feature-prd`.
- Do not use for a legal classification: use `ai-act-classification`.

## Inputs
Mandatory: the PRD or feature description, the autonomy level per step, the tools the agent can call.
Ask if missing: sensitive data classes, latency and cost budget per call, current redteam results.

## Method
1. Write the system prompt: role, scope (what it does and does not do), refusal policy with the wording for out-of-scope requests, output format. "Be helpful" is not a scope.
2. Specify the three guardrail layers. Input: injection and out-of-scope detection. Output: format, grounding, sensitive data. Action: scope of each tool, caps (amount, count, rate), approvals. For each guardrail give the mechanism, latency budget, cost per call and the failure action. Cheap checks first (rules, small classifiers), a frontier judge last.
3. Tie layers to the ladder in references/autonomy-ladder.md. No step at L3 without tested output guardrails. No step at L4 without tested action guardrails; until they pass in redteam, the step stays at L3 or below.
4. Build the redteam set as eval cases tagged `redteam`: at least 20 injections, 10 out-of-scope requests, 5 action-limit attempts. Hand over to `build-evals`.
5. Set the false-positive budget (share of legitimate requests blocked) next to the pass rate. A run above budget gets a tuning plan: thresholds, rules, examples, then a re-run. It is not accepted as is.
6. Record human oversight (AI Act art. 14 where it applies): who can stop the system and how.

## Output
`templates/guardrail-spec.md`, all headings present.

## Rules and red lines
- No L3 without tested output guardrails; no L4 without tested action guardrails (scope, caps, approvals).
- Every guardrail has a latency and a cost line.
- Guardrails are defence in depth, never a guarantee: never call the system safe or jailbreak-proof.
- A false-positive rate above budget is tuned, not accepted.

## Links
references/autonomy-ladder.md · llm-feature-prd · build-evals · agent-design-and-tooling · release-to-production

## Sources
- owasp-llm-top10: threat classes for the input and output layers.
- eu-ai-act: human oversight (art. 14) for the stop and override design.
- own-guardrails: cheap-first layering, budgets per guardrail, false-positive budget.
