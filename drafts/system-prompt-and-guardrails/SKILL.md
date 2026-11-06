---
name: system-prompt-and-guardrails
description: 'Write or tune an LLM feature''s system prompt and guardrails, with budgets and a redteam set. Use for a first prompt, a jailbreak, a redteam result to judge, or an agent given tools.'
stage: build
version: 0.2.0
depends_on: [llm-feature-prd, agent-design-and-tooling]
feeds: [build-evals, release-to-production, ai-act-classification]
autonomy_relevant: true
sources: [owasp-llm-top10, eu-ai-act, own-guardrails, repo-chanmeng]
eval_threshold: 0.80
status: draft
---

# system-prompt-and-guardrails

## When to use
- A first system prompt is drafted for an LLM feature or an agent.
- A jailbreak or an injection was found, a redteam run must be judged before a guardrail goes live, or its false-positive rate is disputed.
- An agent gets tools, or a step moves up the autonomy ladder.
- Do not use to write the PRD itself: use `llm-feature-prd`.
- Do not use for a legal classification: use `ai-act-classification`.

## Inputs
Mandatory, except for a go-live call on one run (step 7): the PRD or feature description, the autonomy level per step, the tools the agent can call.
Ask if missing: sensitive data classes, latency and cost budget per call, current redteam results.

## Method
1. Write the system prompt: role, scope (what it does and does not do), refusal policy with the wording for out-of-scope requests, output format. "Be helpful" is not a scope.
2. Specify the three guardrail layers. Input: out-of-scope detection and injection, both direct (the user's message) and indirect (instructions planted in retrieved documents, tool results or uploads, which the prompt and the pipeline handle as data, never as commands). Output: format, grounding, sensitive data. Action: scope of each tool, caps (amount, count, rate), approvals. For each guardrail give the mechanism, latency budget, cost per call and the failure action. Cheap checks first (rules, small classifiers), a frontier judge last.
3. Give each action guardrail its enforcement point: tool absent, permission, code check or approval step. The prompt can ask, only these can stop, so a prompt sentence never counts. Gates fail closed: if the check itself breaks or cannot answer, the action does not go through, and an attempt at a forbidden action alerts a named owner. The tool list and permission matrix come from `agent-design-and-tooling`; this skill says how they are enforced, attacked and costed.
4. For an agent with tools, run the three-leg check: does it reach private data, read untrusted content, and have a way to send or move something outside (email, webhook, payment)? Together they let a planted instruction exfiltrate data or move money. If all three are present, name the leg you break or lower the level. Record the answer per leg.
5. Tie layers to the ladder in references/autonomy-ladder.md. No step at L3 without tested output guardrails. No step at L4 without tested action guardrails; until they pass in redteam, the step stays at L3 or below.
6. Build the redteam set as eval cases tagged `redteam`: at least 20 injections, 10 out-of-scope requests, 5 action-limit attempts. If the feature reads documents, tool results or uploads, at least 5 of the injections are indirect, planted in those sources: a set of typed attacks can pass while the agent stays exposed through what it reads. Hand over to `build-evals`.
7. Set the false-positive budget (share of legitimate requests blocked) next to the pass rate. A run above budget gets a tuning plan: thresholds, rules, examples, then a re-run. It is not accepted as is. A go-live call on one run needs no full spec or PRD: give the call, this budget, the plan and the re-run.
8. Record human oversight (AI Act art. 14 where it applies): who can stop the system and how.

## Output
`templates/guardrail-spec.md`, all headings present, except for a go-live call on one run (step 7).

## Rules and red lines
- No L3 without tested output guardrails; no L4 without tested action guardrails (scope, caps, approvals).
- Every guardrail has a latency and a cost line.
- A prompt sentence is never an action guardrail; every gate names its enforcement point and fails closed.
- Private data, untrusted content and an outbound path in one agent: a leg is broken or the level is lowered.
- Guardrails are defence in depth, never a guarantee: never call the system safe or jailbreak-proof.
- A false-positive rate above budget is tuned, not accepted.

## Links
references/autonomy-ladder.md · llm-feature-prd · build-evals · agent-design-and-tooling · release-to-production

## Sources
- owasp-llm-top10: threat classes for the input and output layers.
- eu-ai-act: human oversight (art. 14) for the stop and override design.
- own-guardrails: cheap-first layering, budgets per guardrail, false-positive budget.
- repo-chanmeng: enforcement points over prompt rules, gates that fail closed, indirect injection, and the three-leg check (the framing it credits to Simon Willison's "lethal trifecta").
