---
name: semantic-layer-design
description: 'Define the metrics an AI or a human may use: one definition, owner and test each, conflict register, Apache Ossie export. Use for metric disputes, before chat-with-data, or a BI migration.'
stage: data
version: 0.1.0
depends_on: [ai-data-requirements]
feeds: [chat-with-your-data-scoping, assistant-kpis-cost-per-outcome]
autonomy_relevant: false
sources: [apache-ossie, dbt-semantic-layer, own-data-platform]
eval_threshold: 0.80
status: draft
---

# semantic-layer-design

## When to use
- Teams disagree on a metric, or the same name gives two numbers.
- Before any chat-with-your-data product.
- A BI or dashboard migration starts.
- Do not use for documents an assistant retrieves: use `agent-knowledge-base`.
- Do not use for non-metric data specs: use `ai-data-requirements`.

## Inputs
Mandatory: the metrics in use, their current SQL or BI definitions.
Ask if missing: owners, known conflicts, the tool in place.

## Method
1. List each metric with name, business definition, formula, grain, allowed dimensions, source tables, owner. Name the joins too: which table is the many side and which the one side, on which keys. Collect the terms users really say, from the question inventory.
2. One definition per name. Two definitions for one name go to the conflict register with both versions, the difference in numbers and who decides. Both stay draft until the decision; the skill does not arbitrate.
3. Set a status: certified, draft or deprecated. A metric without a test is draft. Generate a test stub per metric: a known value, a row-count or reconciliation check.
4. Only certified metrics are readable by an AI.
5. Make the spec portable. Express it in Apache Ossie, the vendor-neutral format, as mapped in references/ossie-mapping.md: datasets, fields, relationships, metrics scoped to a dataset or to the model, and `ai_context` for synonyms and sample questions. Ossie has no field for owner, status, test or grain: carry them in `custom_extensions`, and keep this spec as the governance source. Export certified metrics only. Name the Ossie version used: the current spec is a draft that can still break, so check what the target tool reads and prefer an existing converter over a hand-written file.
6. For a migration, order the work: metrics already agreed and tested first, disputed ones after their decision. Deprecated metrics keep an alias for 90 days.

## Output
`templates/semantic-spec.md`, all headings present, one row per metric.

## Rules and red lines
- One definition per metric name.
- A metric without a test is draft, never certified.
- A disputed metric is not certified by the skill: the named owner decides.
- The AI reads certified metrics only: a draft metric never enters an export for an agent.
- Ossie is the exchange format, not the governance: being in a valid file does not certify a metric.

## Links
references/ossie-mapping.md · chat-with-your-data-scoping · assistant-kpis-cost-per-outcome · ai-data-requirements

## Sources
- apache-ossie: the exchange format for datasets, fields, relationships, metrics and AI context.
- dbt-semantic-layer: metric, grain and dimension vocabulary.
- own-data-platform: conflict register, certified-first migration, 90-day alias.
