---
name: model-card-ai-registry
description: 'Document an AI system as a model card and registry entry: purpose, version, evals, limits, failure modes, oversight, owners, review date. Use at go-live, a new version, an audit or a registry request.'
stage: govern
version: 0.2.0
last_verified: 2026-11-05
depends_on: [build-evals, model-selection, system-prompt-and-guardrails, ai-act-classification]
feeds: [release-to-production, ai-incident-playbook]
autonomy_relevant: true
sources: [mitchell-model-cards, eu-ai-act, own-registry, repo-chanmeng, repo-yoseph]
eval_threshold: 0.90
status: draft
---

# model-card-ai-registry

## When to use
- An AI system goes live, ships a new version, is being retired, or faces an audit.
- Compliance asks for a registry entry.
- Do not use to classify the system: use `ai-act-classification` and carry its result over.
- Do not use for a non-AI application: the normal application inventory is enough.

## Inputs
Mandatory: purpose, model and version, owners.
Ask if missing: the decision record from `model-selection`, the version bundle from `release-to-production`, per-class eval results from `build-evals`, the guardrail spec, the classification.

## Method
1. Fill the card: purpose and out-of-scope uses, version bundle, data, eval results and suite version, limits, known failure modes, guardrails, autonomy level per step from references/autonomy-ladder.md, oversight, owners, status and end of life, review date.
2. Record the version bundle as `release-to-production` defines it, part by part: system prompt version, dated model snapshot, parameters, tool definitions, knowledge base snapshot. A vendor's model name and number is one part and may still move under you; an alias such as `latest` tells an auditor nothing about what ran. Any part unknown makes the card incomplete. Rollback stays with `release-to-production`.
3. Carry over the scores per question class from `build-evals`, each with its threshold and the suite version, and name the worst class next to the overall figure. An overall score alone is incomplete, because a strong average hides the class that causes complaints: say so and name who provides the breakdown.
4. Refuse a card with no limits or failure modes: it is incomplete. List what is missing and who provides it, rather than inventing it.
5. For L3 and above, fill the guardrails and human oversight sections: who sees exceptions, who can stop the system, how. The AI Act classification comes from `ai-act-classification`, stated as its result, never as a conformity statement.
6. Plan the end of life: status (pilot, live, retiring, retired), what would retire the system, the provider's announced deprecation date for the model, what happens to dependent systems and logs. The provider sets that date, not you, so the review date falls before it. How long logs stay after retirement is a question for counsel. A retired system keeps its entry, marked retired.
7. Write the registry entry in the company's format; if none, use the template's fields.
8. Keep a changelog per version: what changed in the bundle, eval delta, who approved. A provider's model update counts as a version. Generate the changelog from the diff when it is missing. `release-to-production` updates the card at each release.

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
- repo-chanmeng: a vendor model update as a product change, tracking deprecations.
- repo-yoseph: per-slice results and retirement on the card.
