---
name: agent-design-and-tooling
description: 'Design an agent''s loop, tools, permissions, stop conditions and traces from its autonomy levels, before any framework. Use for "make it an agent" or a framework debate.'
stage: build
version: 0.1.0
depends_on: [llm-feature-prd, process-ai-redesign]
feeds: [system-prompt-and-guardrails, assistant-kpis-cost-per-outcome]
autonomy_relevant: true
sources: [anthropic-agents, own-nanoagent]
eval_threshold: 0.80
status: draft
---

# agent-design-and-tooling

## When to use
- Someone asks to "make it an agent", or a workflow has branches and tools.
- A framework debate starts before the design exists.
- Do not use for the prompt and guardrail wording: use `system-prompt-and-guardrails`.
- Do not use when one model call answers the need: say so and stop.

## Inputs
Mandatory: the process steps with their L-levels, the candidate tools.
Ask if missing: failure modes, latency and cost constraints.

## Method
1. Pick the loop type: single step, plan-execute, multi-agent. Start with a raw loop. Multi-agent needs a written justification naming what a single loop cannot do.
2. List tools with schemas, side effects and whether they can be undone.
3. Build the permission matrix: tool × level × approval, following references/autonomy-ladder.md. A tool that moves money or changes records carries a cap and an approval rule.
4. Write stop conditions: maximum steps, budget per run, timeout, and what happens on stop (hand off to a human, never silent).
5. Set the memory policy: what persists, for how long, and personal-data limits.
6. Define the trace schema: every tool call logged with input, output, cost and an outcome field, usable by `assistant-kpis-cost-per-outcome`.
7. Recommend a framework last, and only for a named need.

## Output
`templates/agent-design.md`, all headings present. The loop line reads `Loop type: <type>`.

## Rules and red lines
- Permissions follow the ladder; no write tool without a line in the matrix.
- No agent without stop conditions.
- Multi-agent needs a written justification.
- The framework comes last.

## Links
references/autonomy-ladder.md · system-prompt-and-guardrails · assistant-kpis-cost-per-outcome · process-ai-redesign

## Sources
- anthropic-agents: simple loops first, frameworks last.
- own-nanoagent: raw loop reference, trace with an outcome field.
