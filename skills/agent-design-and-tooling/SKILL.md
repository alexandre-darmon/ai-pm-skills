---
name: agent-design-and-tooling
description: 'Design an agent''s loop, tools, permissions, stop conditions and traces from its autonomy levels, before any framework. Use for "make it an agent", a new tool or permission, or a framework debate.'
license: CC-BY-4.0
metadata:
  stage: "build"
  version: "0.4.5"
  status: "tested"
  eval_threshold: "0.80"
  autonomy_relevant: "true"
  depends_on: "llm-feature-prd, process-ai-redesign"
  feeds: "system-prompt-and-guardrails, assistant-kpis-cost-per-outcome"
  sources: "anthropic-agents, anthropic-agent-tools, mcp-spec, own-nanoagent, repo-chanmeng"
---

# agent-design-and-tooling

## When to use
- Someone asks to "make it an agent", or a workflow has branches and tools.
- A framework debate starts before the design exists.
- An agent gets a new tool, a higher cap or a new permission, and its matrix must change.
- Do not use for the prompt and guardrail wording: use `system-prompt-and-guardrails`.
- Do not use when one model call answers the need: say so and stop.
- Do not use to test the agent: that is `agent-evals`.

## Inputs
Mandatory: the process steps with their L-levels, the candidate tools.
Ask if missing: failure modes, latency and cost constraints.

## Method
1. Set the trigger (request, batch, event, schedule) and define done as a state of the world (a record written, a case ready for the adjuster), not a sentence in the transcript. Name the exits and what follows each: success, error, escalation, paused for approval, policy denied, budget exhausted. A trigger other than on-request also needs dedup of repeated signals.
2. Pick the loop type: single step, plan-execute, multi-agent. Start with a raw loop. Multi-agent needs a written justification naming what a single loop cannot do. Steps that always run in the same order are a workflow in code, not agents, still bounded by step 6's stop conditions. Least privilege is not such a reason: one loop gets it from tools scoped and gated in code (step 3). Do not overclaim injection containment: a model without tools can still be steered into a misleading draft, so the human review stays the control for what code cannot check.
3. List tools with schemas, side effects and whether they can be undone. For each, write the contract the model reads: when to use it over its nearest neighbour, named parameters over a generic tool, and an empty result kept distinct from a failed call. Rate the risk by effect, not by name: a read that discloses data cannot be undone either. Scope every data tool by the identity and authorization of the trusted session or case record, enforced inside the tool. An ID the model extracted from text only selects within that scope; otherwise one crafted message can read another customer's data. Detail in references/tool-contracts.md.
4. Build the permission matrix: tool × level × approval, following references/autonomy-ladder.md. Name the target level and the gate to reach it in one line, its figures written as proposals (the ladder's durations are defaults, not policy the reader has adopted); the rollout path belongs to `release-to-production`. A tool that moves money or changes records carries a cap and an approval rule naming the role who approves (at L4, the calls above the cap), plus its eligibility rule: when the action is justified and how the amount or change is set, so the cap bounds a decision rather than replacing it. A value the brief does not give is not left blank: propose one concrete starting value, sized from what the brief gives (typical amount, volume, unit value) or the smallest that serves the use, written as "proposed, to be confirmed by <role>", never "confirmed by": no one has confirmed it yet, and a reader would trust it. A cap carries its unit (currency, per action or rolling over a period); a per-action cap and a rolling cap are separate lines, each saying what happens when it is crossed. A cap has one meaning: above it, the call waits for approval. Keep "policy denied" for what no approval lifts (wrong scope, a second payment for the same case), so a cap breach is never both. State the one rule that holds until then (every call approved, or the tool off), and the rule once confirmed: calls within the cap run at the target level, calls above it need approval.
5. Write the protocol for each write tool at L3 and above: prepare is separate from commit; where the matrix requires approval, it is bound to the exact action, target and payload, and it expires; the cap is checked on the resulting state in the system of record, where other sessions and channels count too, in the same transaction as the commit so two parallel runs cannot both pass it; every write has an idempotency key taken from the business action it settles (the case or request), not from the payload, so a changed amount cannot pay twice, and is never retried blindly; a write that times out has an unknown result, so reconcile before any retry. When one write succeeds and a later one fails, the run records the first as done and handles only the failed step, never reporting the whole run as nothing done. Text the agent sends or saves for a customer is checked in code where code can check it (amounts, dates, IDs stated as facts, against what the tools returned) before it leaves the run. Text that quotes what a user asserted is marked as their claim, not checked as a fact. What code cannot check, such as a promise or a conclusion, stays with the human reviewer, and the design says so rather than claiming a check it lacks. A write that overwrites human-editable content carries a version check. Where the brief does not show the tool or its backend can do this (atomic cap check, idempotency, reconciliation, version check), write it as a requirement for the tool owner to confirm, not as a given. How the gate is enforced and attacked belongs to `system-prompt-and-guardrails`.
6. Write stop conditions for the run. A run ends on a checkable done state or the API's stop signal, never on the model's prose or self-reported confidence. Maximum steps (model and tool calls together, so retries and fallbacks count), budget per run and timeout are the safety net, each written as a number in the design ("max steps: <n>, proposed, to be confirmed by <role>"), never a promise to set one later: a limit with no value cannot be enforced. Take it from the brief, or propose a starting figure labelled as an assumption, to be replaced by what the prototype's traces measure (step 9), without an invented derivation from call counts or prices you have not seen. State the budget as a token figure, counted in code from the usage each call reports, plus a cap on calls to any metered tool API, since tokens do not bound those; add a money figure when the brief gives prices: a money figure built on a guessed price per call is not enforceable. Each one, budget included, is a stop condition: a hit is an alert with its own exit (hand off to a human, never silent). Stop conditions for the initiative itself start in `ai-opportunity-assessment`; how the agent is tested over repeated trials is `agent-evals`.
7. Set the memory policy: what persists, for how long, and personal-data limits.
8. Define the trace schema: every tool call logged with input, output and cost (personal data redacted or kept as record IDs, access restricted), and an outcome field set from the exit, usable by `assistant-kpis-cost-per-outcome`.
9. Before handing the design to engineering, prototype the tool set on a local MCP server (synthetic or anonymised data, no production credentials: references/build-to-learn.md) and run about 10 representative tasks. Read the traces from step 8: which tools the agent called, in which order, where it looped or picked the wrong neighbour. Fix tool names, descriptions and response sizes before touching the prompt. The prototype is evidence for the design, not the build; record it in the Prototype check section, or "not yet run".
10. Map frameworks last: each candidate against a named need the raw loop cannot meet (such as durable state, pausing for a human across sessions, replay for audit, the team's hosting and skills), or none. Say which needs the brief establishes and which are still open.

## Output
`templates/agent-design.md`, all headings present. The loop line reads `Loop type: <type>`.
When the brief asks which framework to take, the answer opens with what the design lacks, says the choice waits for it, and keeps candidates for the closing section, because readers stop at the first name they see. No conditional pick up front ("X, if you adopt one"). The closing section still decides, in one line: the raw loop for now, or a candidate tied to the need it meets ("raw loop now; X only if <need> is confirmed"), and what would change that. Then one line per candidate the brief names: the need it would serve, and whether this design has it, lacks it, or does not know yet. Describe what each candidate is built for rather than asserting weaknesses you cannot show: frameworks change fast, so compare on the needs, not on a mode you assume one lacks.
When the brief asks what is missing, rank the gaps by the harm they would cause for this agent and give the top ones in detail; the reader wants priorities, not every template section.
Each limit and exit is stated once and the other sections point to it, so the design never gives two values for one cap or a path that bypasses an exit.

## Rules and red lines
- Permissions follow the ladder; no write tool without a line in the matrix.
- Data scope comes from the trusted session or case, never from model output.
- No write tool at L3 or above without its protocol line.
- No agent without stop conditions and named exits.
- Multi-agent needs a written justification.
- The framework comes last, in the answer as much as in the method, and never as an unconditional pick: the raw loop stays the default until a named need requires more.

## Links
references/autonomy-ladder.md · references/tool-contracts.md · references/build-to-learn.md · system-prompt-and-guardrails · agent-evals · assistant-kpis-cost-per-outcome · process-ai-redesign

## Sources
- anthropic-agents: simple loops first, frameworks last.
- anthropic-agent-tools: prototype a few tools, run realistic tasks, read the transcripts, then refine.
- mcp-spec: tools exposed by a server to the model, which a local prototype server reuses.
- own-nanoagent: raw loop reference, trace with an outcome field.
- repo-chanmeng: ideas for tool contracts, the write protocol, trigger and exits, rewritten in our own words.
