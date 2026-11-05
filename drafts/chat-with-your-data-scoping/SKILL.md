---
name: chat-with-your-data-scoping
description: 'Scope a chat-with-your-data or text-to-SQL product: allowed question classes, golden set, accuracy per class, answer format. Use when users want to ask the data in natural language.'
stage: specify
version: 0.1.0
depends_on: [llm-feature-prd, semantic-layer-design]
feeds: [build-evals, system-prompt-and-guardrails]
autonomy_relevant: true
sources: [text-to-sql-benchmarks, own-semantic-layer]
eval_threshold: 0.80
status: draft
---

# chat-with-your-data-scoping

## When to use
- Someone wants users to ask questions to their data in natural language.
- A BI team or a vendor proposes text-to-SQL.
- Do not use to define the metrics themselves: use `semantic-layer-design`.
- Do not use for questions over documents: use `agent-knowledge-base`.

## Inputs
Mandatory: the question inventory (the questions users really ask), the state of the metric definitions, data sensitivity, the user population.
If there is no inventory, collect one first. Ask for at least 50 real questions from tickets, analysts or BI logs.

## Method
1. Sort the inventory into question classes: lookup, aggregate on a defined metric, comparison, ambiguous, forbidden.
2. Map every metric to its definition in the semantic layer. A question on an undefined or disputed metric is blocked until the metric is defined; hand over to `semantic-layer-design`.
3. Write allowed and forbidden classes. Sensitive data (salaries, health, individual performance) is forbidden in free-form questions.
4. Fix the answer format: number + SQL + source + freshness. No answer without its SQL.
5. Build the golden set from the inventory: at least 50 question → expected answer pairs, across classes. Hand over to `build-evals`.
6. Set an accuracy target per class, measured per class and never as one global figure.
7. Define refusal for out-of-scope questions and the escalation path to an analyst. Set the autonomy level from references/autonomy-ladder.md, almost always L1 or L2.

## Output
`templates/scoping.md`, all headings present. The level line reads `Autonomy level: L<n>`.

## Rules and red lines
- No production without defined metrics for what is in scope.
- Every answer shows its SQL and source.
- Accuracy per class, never global.
- A question outside scope gets a refusal, not a guess.

## Links
references/autonomy-ladder.md · semantic-layer-design · build-evals · system-prompt-and-guardrails

## Sources
- text-to-sql-benchmarks: eval method only, never their scores.
- own-semantic-layer: blocked-until-defined rule, answer format.
