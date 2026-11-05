---
name: ai-data-requirements
description: 'Specify the data an AI feature needs: fields, quality thresholds, legal basis, owner, refresh. Use after the PRD, when asked "what data do we need" or when a DPO asks what is processed.'
stage: specify
version: 0.1.0
depends_on: [llm-feature-prd]
feeds: [semantic-layer-design, agent-knowledge-base, dpia-prescreen]
autonomy_relevant: false
sources: [dama-dmbok, gdpr, own-data-platform]
eval_threshold: 0.80
status: draft
---

# ai-data-requirements

## When to use
- A PRD is done and the data for the AI feature must be specified.
- A data team asks for a spec, or a DPO asks what the feature processes.
- Do not use for metric definitions: use `semantic-layer-design`.
- Do not use for documents an assistant retrieves: use `agent-knowledge-base`.

## Inputs
Mandatory: the PRD or feature description, the candidate sources or tables.
Ask if missing: access constraints, retention rules, who owns each source.

## Method
1. List sources and fields needed per step of the feature. A field no step needs is dropped.
2. Set quality thresholds as numbers per source: completeness, freshness (a maximum age in hours or days), duplication, and for training or eval data, label quality.
3. Flag personal data per field. Give each flagged field a lawful basis (GDPR art. 6) to be confirmed by the DPO, or drop it. Special categories (art. 9) go to `dpia-prescreen`.
4. Write the pseudonymisation plan: what is masked or tokenised before the model sees it, and where the key lives.
5. Name one owner per source. A source with no owner is a blocker: it is out until a sponsor names one.
6. Sketch the lineage and the refresh cadence, and retention per source.

## Output
`templates/data-requirements.md`, all headings present, one row per field.

## Rules and red lines
- Every personal-data field has a lawful basis or is dropped; never "to be defined".
- Freshness is a number, never "regular".
- One owner per source, or the source is out.

## Links
llm-feature-prd · dpia-prescreen · semantic-layer-design · agent-knowledge-base

## Sources
- dama-dmbok: data-quality dimensions.
- gdpr: minimisation and lawful basis (art. 5, 6).
- own-data-platform: owner-or-out rule, field-level sheet.
