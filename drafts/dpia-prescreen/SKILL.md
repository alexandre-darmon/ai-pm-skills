---
name: dpia-prescreen
description: 'Pre-screen whether an AI use case needs a DPIA against the nine EDPB criteria and the CNIL list, and pre-fill it for the DPO. Use when personal data, profiling or a new data source is in scope.'
stage: govern
version: 0.1.0
last_verified: 2026-11-05
depends_on: [ai-data-requirements, ai-act-classification]
feeds: [model-card-ai-registry]
autonomy_relevant: true
sources: [gdpr, edpb-wp248, cnil-dpia]
eval_threshold: 0.90
status: draft
---

# dpia-prescreen

## When to use
- An AI feature processes personal data, profiles people or makes automated decisions.
- The DPO asks for a pre-screen, or a new data source joins an existing system.
- Do not use for the AI Act classification: use `ai-act-classification`.
- Do not use when no personal data is involved in any form: say so in one line.

## Inputs
Mandatory: purpose, populations, data categories.
Ask if missing: automated decision flags, vendors and hosting, retention.

## Method
1. Score the nine EDPB criteria (WP248 rev.01), each yes or no with a reason: evaluation or scoring; automated decision with legal or similar effect; systematic monitoring; sensitive or highly personal data; large scale; matching or combining datasets; vulnerable people (employees count); innovative use of technology; preventing the use of a right or service.
2. Check the French CNIL list: constant monitoring of employees' activity and HR profiling are on it.
3. Recommend: two or more criteria, or a CNIL-list match, gives `DPIA recommended` (the guidelines say likely needed). Fewer gives `DPIA not needed`, with reasons kept on file. The DPO decides; the skill prepares.
4. Pre-fill the product sections: purpose, data, flows, recipients, retention, risks, measures.
5. Flag transfers: any hosting, vendor or support access outside the EU is flagged for the DPO, with vendor and country. It is flagged, not assessed.
6. Write the questions for the DPO.

## Output
`templates/prescreen.md`, all headings present. The recommendation line reads `Recommendation: DPIA recommended` or `Recommendation: DPIA not needed`, followed by "DPO decides".

## Rules and red lines
- Checklist, not verdict: the DPO decides.
- The count rule is applied and shown.
- Transfers are flagged, never declared lawful.

## Links
ai-data-requirements · ai-act-classification · model-card-ai-registry · cse-consultation

## Sources
- gdpr: art. 35.
- edpb-wp248: the nine criteria and the two-criteria rule.
- cnil-dpia: the French list and PIA sections.
