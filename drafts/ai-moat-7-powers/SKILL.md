---
name: ai-moat-7-powers
description: 'Scan where an AI product has a defensible advantage with Helmer''s 7 Powers when the model is a commodity. Use for "what''s our moat?", an investment committee or a similar competitor launch.'
stage: strategy
version: 0.1.0
depends_on: [ai-opportunity-assessment]
feeds: [ai-initiative-pitch]
autonomy_relevant: false
sources: [helmer-7-powers, own-moat-thesis]
eval_threshold: 0.80
status: draft
---

# ai-moat-7-powers

## When to use
- Someone asks what the moat of an AI product is, or an investment committee asks about defensibility.
- A competitor launches a similar assistant.
- Do not use to decide if the idea deserves a PRD: use `ai-opportunity-assessment`.
- Do not use for a non-AI product: a standard strategy review applies.

## Inputs
Mandatory: product description, data owned, position in the workflow, competitors.
Ask if missing: customers, contracts, what a rival would need to copy it.

## Method
1. Check the two usual AI sources first: proprietary data no rival can obtain, and a workflow position that is costly to leave.
2. Rate each of the seven powers as present, buildable or absent, with one fact as evidence: scale economies, network economies, counter-positioning, switching costs, branding, cornered resource, process power.
3. State what the model does not protect: anything a rival can buy from the same API is not an advantage.
4. Apply the copy test: what could a funded rival rebuild in six months?
5. Pick the one or two powers to invest in, with the next action. If all seven are absent, say so and recommend competing on delivery or stopping the moat argument.

## Output
`templates/moat-scan.md`, all headings present, seven rated rows.

## Rules and red lines
- A conversational interface alone is never a moat.
- Better prompts are never a moat.
- Each rating has a fact as evidence.

## Links
ai-opportunity-assessment · ai-initiative-pitch

## Sources
- helmer-7-powers: the seven powers.
- own-moat-thesis: data and distribution checked first.
