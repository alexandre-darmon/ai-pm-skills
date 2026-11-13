---
name: agent-design-and-tooling
description: 'Design an agent''s loop, tools, permissions, stop conditions and traces from its autonomy levels, before any framework. Use for "make it an agent", a new tool or permission, or a framework debate.'
license: CC-BY-4.0
metadata:
  stage: "build"
  version: "0.4.0"
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
2. Pick the loop type: single step, plan-execute, multi-agent. Start with a raw loop. Multi-agent needs a written justification naming what a single loop cannot do. Steps that always run in the same order are a workflow in code, not agents. Least privilege and injection containment are not such a reason: one loop gets them from tools scoped and gated in code (step 3).
3. List tools with schemas, side effects and whether they can be undone. For each, write the contract the model reads: when to use it over its nearest neighbour, named parameters over a generic tool, and an empty result kept distinct from a failed call. Rate the risk by effect, not by name: a read that discloses data cannot be undone either. Scope every data tool by the identity and authorization of the trusted session or case record, enforced inside the tool. An ID the model extracted from text only selects within that scope; otherwise one crafted message can read another customer's data. Detail in references/tool-contracts.md.
4. Build the permission matrix: tool × level × approval, following references/autonomy-ladder.md. A tool that moves money or changes records carries a cap and an approval rule naming the role who approves (at L4, the calls above the cap). A value the brief does not give is not left blank: propose one concrete starting value, sized from what the brief gives (typical amount, volume, unit value) or the smallest that serves the use, marked as an assumption its named owner confirms. State the one rule that holds until then (every call approved, or the tool off), and the rule once confirmed: calls within the cap run at the target level, calls above it need approval.
5. Write the protocol for each write tool at L3 and above: prepare is separate from commit; where the matrix requires approval, it is bound to the exact action, target and payload, and it expires; the cap is checked on the resulting state in the system of record, where other sessions and channels count too; every write has an idempotency key and is never retried blindly; a write that times out has an unknown result, so reconcile before any retry. Text the agent sends or saves for a customer is checked in code against the facts its tools returned (amounts, dates, commitments) before it leaves the run. How the gate is enforced and attacked belongs to `system-prompt-and-guardrails`.
6. Write stop conditions for the run. A run ends on a checkable done state or the API's stop signal, never on the model's prose or self-reported confidence. Maximum steps, budget per run and timeout are the safety net, each with a number, never a placeholder: from the brief, or sized from a normal run (its tool calls plus a margin; budget = maximum steps × cost per call), marked as an assumption with the owner who confirms it. Each one, budget included, is a stop condition: a hit is an alert with its own exit (hand off to a human, never silent). Stop conditions for the initiative itself start in `ai-opportunity-assessment`; how the agent is tested over repeated trials is `agent-evals`.
7. Set the memory policy: what persists, for how long, and personal-data limits.
8. Define the trace schema: every tool call logged with input, output and cost (personal data redacted or kept as record IDs, access restricted), and an outcome field set from the exit, usable by `assistant-kpis-cost-per-outcome`.
9. Before handing the design to engineering, prototype the tool set on a local MCP server (synthetic or anonymised data, no production credentials: references/build-to-learn.md) and run about 10 representative tasks. Read the traces from step 8: which tools the agent called, in which order, where it looped or picked the wrong neighbour. Fix tool names, descriptions and response sizes before touching the prompt. The prototype is evidence for the design, not the build; record it in the Prototype check section, or "not yet run".
10. Map frameworks last: each candidate against a named need the raw loop cannot meet, or none.

## Output
`templates/agent-design.md`, all headings present. The loop line reads `Loop type: <type>`.
When the brief asks which framework to take, the answer still opens with what the design lacks, says the choice waits for it, and keeps candidates for the closing section. No conditional pick up front ("X, if you adopt one"): readers stop at the name. The closing section still decides, in one line: the raw loop for now, or a candidate tied to the need it meets ("X only if <need>"), and what would change that. Then one line per candidate the brief names: the need it would serve and whether this design has that need now.

## Rules and red lines
- Permissions follow the ladder; no write tool without a line in the matrix.
- Data scope comes from the trusted session or case, never from model output.
- No write tool at L3 or above without its protocol line.
- No agent without stop conditions and named exits.
- Multi-agent needs a written justification.
- The framework comes last, in the answer as much as in the method.

## Links
references/autonomy-ladder.md · references/tool-contracts.md · references/build-to-learn.md · system-prompt-and-guardrails · agent-evals · assistant-kpis-cost-per-outcome · process-ai-redesign

## Sources
- anthropic-agents: simple loops first, frameworks last.
- anthropic-agent-tools: prototype a few tools, run realistic tasks, read the transcripts, then refine.
- mcp-spec: tools exposed by a server to the model, which a local prototype server reuses.
- own-nanoagent: raw loop reference, trace with an outcome field.
- repo-chanmeng: ideas for tool contracts, the write protocol, trigger and exits, rewritten in our own words.
