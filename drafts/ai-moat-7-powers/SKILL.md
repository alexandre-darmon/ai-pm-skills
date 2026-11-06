---
name: ai-moat-7-powers
description: 'Scan where an AI product has a defensible advantage with Helmer''s 7 Powers when the model is a commodity. Use for "what''s our moat?", an investment committee or a similar competitor launch.'
stage: strategy
version: 0.2.0
depends_on: [ai-opportunity-assessment]
feeds: [ai-initiative-pitch]
autonomy_relevant: false
sources: [helmer-7-powers, own-moat-thesis, repo-lenny]
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
1. Check the two usual AI sources first: a workflow position that is costly to leave, and proprietary data. When data is claimed, ask three separate questions: do we hold the rights to use it this way, does use of the product generate better data, and does that better data measurably improve outcomes? Exclusive data that stays static supports cornered resource, not a flywheel. A question the brief cannot answer goes to the next action; it does not lower a rating the stated facts support.
2. Rate each of the seven powers as present, buildable or absent, with one fact as evidence: scale economies, network economies, counter-positioning, switching costs, branding, cornered resource, process power. For counter-positioning the fact is what an incumbent would give up by copying (it won't); for cornered resource, why a rival cannot obtain the asset (it can't). "Hard to copy" is not evidence.
3. State what the model does not protect: anything a rival can buy from the same API is not an advantage.
4. Apply the copy test: what could a funded rival rebuild in six months? Then the model-progress test: what would the next model or a platform release absorb? State it as a shipped example, or as an assumption with a date to recheck it. A forecast is not a fact, so on its own it does not change a rating.
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
- repo-lenny: ideas only, no quotes: model progress as a threat, data rights and flywheel as separate questions, can't versus won't.
