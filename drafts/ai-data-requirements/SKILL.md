---
name: ai-data-requirements
description: 'Specify the data an AI feature needs and where each field flows: prompt, logs, eval, vendor, training. Use after the PRD, on "what data do we need" or when a DPO asks what is processed.'
stage: specify
version: 0.2.0
depends_on: [llm-feature-prd]
feeds: [semantic-layer-design, agent-knowledge-base, synthetic-eval-data, build-evals]
autonomy_relevant: false
sources: [dama-dmbok, gdpr, own-data-platform, repo-vishalhabib, repo-product-on-purpose, repo-chanmeng]
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
1. List sources and fields needed per step of the feature. A field no step needs is dropped. Give the volume per source and the model calls per day: it sets token cost and is the volume term `ai-roi-quantification` checks. If the brief has none, ask and list it as open; never invent it.
2. Set quality thresholds as numbers per source: completeness, freshness (a maximum age in hours or days), duplication, and for training or eval data, label quality (who labels and how: `build-evals`). Beside each threshold, put the value measured today on a real, unfiltered sample, because a curated sample overstates what the model will meet in production. Below the bar is a blocker. No access to the data: write "not measured" and make the measurement an open action, not an estimate.
3. Flag personal data per field, then state in one sentence per source whether it holds any, so the DPO reads the scope without scanning cells. Give each flagged field a lawful basis (GDPR art. 6) to be confirmed by the DPO, or drop it. Special categories (art. 9) go to the DPO with a question on a data protection impact assessment (art. 35).
4. Map where each field flows: prompt, retrieved context, logs and traces, eval set, vendor, training. For each destination it reaches, state whether it arrives masked and how long it stays, as a number. A personal-data field reaching the eval set or training is a further purpose: it needs its own basis or a compatibility assessment (GDPR art. 6(4)), for the DPO to confirm, or it stays out. This table is the single record of AI data flows; the DPO reads it for the impact assessment, and `production-evals-monitoring` reads it before any trace reaches a judge.
5. Write the pseudonymisation plan by destination: what is masked or tokenised before the model, the logs and the vendor see it, and where the key lives.
6. Name one owner per source. A source with no owner is a blocker: it is out until a sponsor names one.
7. Sketch the lineage, the refresh cadence as a number, and retention per source.

## Output
`templates/data-requirements.md`, all headings present, one row per field.

## Rules and red lines
- Every personal-data field has a lawful basis or is dropped; never "to be defined".
- Freshness is a number, never "regular".
- One owner per source, or the source is out.
- A field with a blank flow destination is unspecified: say no, or say where and for how long.
- Never clean the sample before measuring: its messy records are what the model will meet.

## Links
llm-feature-prd · semantic-layer-design · agent-knowledge-base · synthetic-eval-data · production-evals-monitoring

## Sources
- dama-dmbok: data-quality dimensions.
- gdpr: minimisation and lawful basis (art. 5, 6).
- own-data-platform: owner-or-out rule, field-level sheet.
- repo-vishalhabib: framing data handling by where sensitive data ends up (logs, prompts, third parties).
- repo-product-on-purpose: trace capture, redaction and retention as a privacy concern (a planned spec item).
- repo-chanmeng: dirty data as the test, not something to clean for the demo.
