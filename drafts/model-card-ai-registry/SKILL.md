---
name: model-card-ai-registry
description: 'Document an AI system as a model card and registry entry: purpose, version, evals, limits, failure modes, oversight, owners, review date. Use at go-live, a new version, an audit or a registry request.'
stage: govern
version: 0.1.0
last_verified: 2026-11-05
depends_on: [build-evals, model-selection, system-prompt-and-guardrails, ai-act-classification]
feeds: [release-to-production, ai-incident-playbook]
autonomy_relevant: true
sources: [mitchell-model-cards, eu-ai-act, own-registry]
eval_threshold: 0.90
status: draft
---

# model-card-ai-registry

## When to use
- An AI system goes live, ships a new version, or faces an audit.
- Compliance asks for a registry entry.
- Do not use to classify the system: use `ai-act-classification` and carry its result over.
- Do not use for a non-AI application: the normal application inventory is enough.

## Inputs
Mandatory: purpose, model and version, owners.
Ask if missing: the decision record from `model-selection`, eval results from `build-evals`, the guardrail spec, the classification.

## Method
1. Fill the card: purpose and out-of-scope uses, model and version, data, eval results and suite version, limits, known failure modes, guardrails, autonomy level per step from references/autonomy-ladder.md, oversight, owners, review date.
2. Refuse a card with no limits or failure modes: it is incomplete. List what is missing and who provides it, rather than inventing it.
3. For L3 and above, fill the guardrails and human oversight sections: who sees exceptions, who can stop the system, how. The AI Act classification comes from `ai-act-classification`, stated as its result, never as a conformity statement.
4. Write the registry entry in the company's format; if none, use the template's fields.
5. Keep a changelog per version: what changed, eval delta, who approved. Generate it from the diff when it is missing. `release-to-production` updates the card at each release.

## Output
`templates/model-card.md`, all headings present.

## Rules and red lines
- Every card has a review date.
- Limits and failure modes are mandatory.
- Checklist, not verdict: a card never says the system is compliant.

## Links
references/autonomy-ladder.md · ai-act-classification · build-evals · release-to-production · ai-incident-playbook

## Sources
- mitchell-model-cards: card structure.
- eu-ai-act: record-keeping and oversight as inputs to counsel.
- own-registry: changelog convention.
