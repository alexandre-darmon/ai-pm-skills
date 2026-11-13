---
name: system-prompt-and-guardrails
description: 'Write or tune an LLM feature''s system prompt and guardrails. Use for a first prompt, a jailbreak, injection or leak, a guardrail refusing too much (false positives), or a redteam result to judge.'
license: CC-BY-4.0
metadata:
  stage: "build"
  version: "0.3.0"
  status: "tested"
  eval_threshold: "0.80"
  autonomy_relevant: "true"
  depends_on: "llm-feature-prd, agent-design-and-tooling"
  feeds: "build-evals, release-to-production, ai-act-classification"
  sources: "owasp-llm-top10, eu-ai-act, own-guardrails, repo-chanmeng"
---

# system-prompt-and-guardrails

## When to use
- A first system prompt is drafted for an LLM feature or an agent.
- Someone got the assistant to break its rules or leak what it should keep (jailbreak, injection), a redteam run must be judged before a guardrail goes live, or a guardrail refuses too many normal requests and its false-positive rate is disputed.
- The action guardrails an agent's design calls for (scope, caps, approvals) must be written and enforced.
- Do not use to write the PRD itself: use `llm-feature-prd`.
- Do not use for a legal classification: use `ai-act-classification`.
- Do not use to design an agent's loop, tools or permission matrix: that is `agent-design-and-tooling`.

## Inputs
Mandatory, except for a go-live call on one run (step 7): the PRD or feature description, the autonomy level per step, the tools the agent can call.
Ask if missing: sensitive data classes, the business rules the agent applies (eligibility, limits), latency and cost budget per call, current redteam results. A figure or rule not given (cap, threshold, budget, latency, cost, eligibility) is written as an assumption with the owner who confirms it, never as fact.

## Method
1. Write the system prompt: role, scope (what it does and does not do), refusal policy with the wording for out-of-scope requests, output format. "Be helpful" is not a scope.
2. Specify the three guardrail layers. Input: out-of-scope detection and injection, both direct (the user's message) and indirect (instructions planted in retrieved documents, tool results or uploads, which the prompt and the pipeline handle as data, never as commands). Output: format, grounding, sensitive data. Action: scope of each tool, caps (amount, count, rate), approvals. For each guardrail give the mechanism, latency and cost per call (given, measured, or an estimate marked to measure) and the failure action. Cheap checks first (rules, small classifiers), a frontier judge last.
3. Give each action guardrail its enforcement point: tool absent, permission, code check or approval step. The prompt can ask, only these can stop, so a prompt sentence never counts. Action gates fail closed: if the check itself breaks or cannot answer, the action does not go through, and an attempt at a forbidden action alerts a named owner. The tool list and permission matrix come from `agent-design-and-tooling`; this skill says how they are enforced, attacked and costed.
4. For an agent with tools, run the three-leg check: does it reach private data, read untrusted content, and have a way to send or move something outside (email, webhook, payment)? Together they let a planted instruction exfiltrate data or move money. If all three are present, name the leg you break or lower the level. Record the answer per leg.
5. Tie layers to the ladder in references/autonomy-ladder.md. No step at L3 without tested output guardrails. No step at L4 without tested action guardrails; until they pass in redteam, the step stays at L3 or below. No fallback: a capped L4 or a date-based release is still L4 before the tests pass.
6. Build the redteam set as eval cases tagged `redteam`: at least 20 injections, 10 out-of-scope requests, 5 action-limit attempts, or the previous set's size if larger: a re-run never shrinks the set. Keep a held-out part unseen during tuning, and write the pass criteria (attack pass rate, false-positive budget, outcomes that must never occur) before the run. If the feature reads documents, tool results or uploads, at least 5 of the injections are indirect, planted in those sources: a set of typed attacks can pass while the agent stays exposed through what it reads. Hand over to `build-evals`.
7. Set the false-positive budget (share of legitimate requests blocked) next to the pass rate, with the product owner, from the cost of a wrongly blocked user; a figure you propose is an assumption. A filter on sensitive topics routes or flags legitimate questions rather than blocking them. A run above budget gets a tuning plan: thresholds, rules, examples, then a re-run. It is not accepted as is. A go-live call on one run needs no full spec or PRD: give the call, this budget, the plan and the re-run. A shadow or log-only mode lets attacks through: offer it only where another enforced layer stops the harm, and name that layer.
8. Record human oversight (AI Act art. 14 where it applies): who can stop the system and how. Logs and human review of conversations hold personal data: state redaction, who can read them and retention.

## Output
`templates/guardrail-spec.md`, all headings present, except for a go-live call on one run (step 7).

## Rules and red lines
- No L3 without tested output guardrails; no L4 without tested action guardrails (scope, caps, approvals), and no capped or dated L4 in the meantime.
- Every guardrail has a latency and a cost line, measured or marked as an estimate; no unprovided policy, cap or threshold stated as fact.
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
