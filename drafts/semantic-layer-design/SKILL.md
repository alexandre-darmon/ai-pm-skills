---
name: semantic-layer-design
description: 'Define the metrics an AI or a human may use: one definition, owner and test each, conflict register, Apache Ossie export. Use for metric disputes, before chat-with-data, or a BI migration.'
stage: data
version: 0.2.0
depends_on: [ai-data-requirements]
feeds: [chat-with-your-data-scoping, assistant-kpis-cost-per-outcome]
autonomy_relevant: false
sources: [apache-ossie, dbt-semantic-layer, own-data-platform, repo-anthropic-kwp, repo-chanmeng]
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
1. Pin down the words under the metrics first. For each business word people use loosely (customer, active, amount): one meaning, the entity it counts and that entity's key, what breaks if it differs. Two metrics can have clean formulas and still count different entities, and an AI writing SQL will not notice. A word with two live meanings goes to the conflict register.
2. List each metric with name, business definition, formula, grain, allowed dimensions, source tables, owner. Name the joins too: which table is the many side and which the one side, on which keys. Collect the terms users really say, from the question inventory.
3. For each metric, write what an analyst applies by habit and an agent drops silently. Standing filters: test, internal or fraud rows, cancelled records. Traps: timezone, nulls, historical versus current table, source refresh lag. Put a filter in the formula when you can; otherwise it travels as an instruction to the AI. If nobody has named any, write `none known` and ask the owner: this alone does not change the status.
4. One definition per name. Two definitions for one name go to the conflict register with both versions, the difference in numbers and who decides. Both stay draft until the decision; the skill does not arbitrate.
5. Set a status: certified, draft or deprecated. A metric without a test is draft. Generate a test stub per metric: a known value, a row-count or reconciliation check.
6. Only certified metrics are readable by an AI.
7. Make the spec portable. Express it in Apache Ossie, the vendor-neutral format, as mapped in references/ossie-mapping.md: datasets, fields, relationships, metrics scoped to a dataset or to the model, and `ai_context` for synonyms and sample questions. Ossie has no field for owner, status, test or grain: carry them in `custom_extensions`, and keep this spec as the governance source. Export certified metrics only. Name the Ossie version used: the current spec is a draft that can still break, so check what the target tool reads and prefer an existing converter over a hand-written file.
8. For a migration, order the work: metrics already agreed and tested first, disputed ones after their decision. Deprecated metrics keep an alias for 90 days.

## Output
`templates/semantic-spec.md`, all headings present, one row per metric.

## Rules and red lines
- One definition per metric name.
- No blank filters cell on a certified metric: filters and traps listed, or `none known`.
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
- repo-anthropic-kwp: asking what a business word means and which IDs link entities; standing filters and analyst mistakes as things to capture.
- repo-chanmeng: stating what breaks when a shared term differs across components.
