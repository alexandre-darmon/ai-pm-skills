---
name: assistant-kpis-cost-per-outcome
description: Define an AI assistant's or agent's KPIs (quality by domain, adoption, cost per correct outcome). Use when asked for its dashboard or ROI, or when usage grows and nobody knows if it helps.
stage: measure
version: 0.1.0
depends_on: [build-evals, conversation-analysis, agent-knowledge-base]
feeds: [ai-roi-quantification, ai-initiative-pitch, ai-adoption-plan]
autonomy_relevant: true
sources: [otel-genai, own-assistant-dashboards]
eval_threshold: 0.80
status: tested
---

# assistant-kpis-cost-per-outcome

## When to use
- A sponsor asks for "the dashboard" of an assistant or agent in production, or for its ROI.
- Usage is up (sessions, messages, active users) but nobody knows if the answers are right or if it helps.
- Traces or logs exist but no outcome is recorded: you can count conversations, not results.
- Quality differs by domain, or a knowledge base (KB) seems out of date.
- Do not use to build the eval set, graders or judge: that is `build-evals`.
- Do not use for a product with no model in it (web funnel, app retention, BI on sales): a generic analytics method is enough.

## Inputs
Mandatory: what the assistant does (use cases, the KBs or domains it answers from), the fields its traces or logs actually contain, the run costs (tokens, infra, licences) for a period.
Ask if missing: conversation classification by use case (`conversation-analysis`), sampled quality scores (`build-evals` graders or a reviewed sample), headcount per population (eligible users), each KB's owner and last review date, unit values per use case.
A thumbs-up rate is not a quality source: treat quality as missing and plan a sampled review.

## Method
1. **Inventory the sources.** List the fields the traces have (trace id, timestamp, use case, KB, user population, tokens, cost) and the ones missing. Any KPI whose source does not exist is marked "not computable yet", with the instrumentation it needs. Never fill a gap with an estimate shown as a measure.
2. **Define the outcome per use case** in business terms: answer accepted, request closed without escalation, form submitted. Add an outcome event attached to the trace: `outcome_id`, `trace_id`, `use_case`, `result` (success, failure, escalated, abandoned), `value_eur` (empty until a unit value is sourced), `source` (user, system, reviewer), `timestamp`. Model and token fields follow the OpenTelemetry GenAI semantic conventions (`gen_ai.*` attributes). Until outcomes are logged, quality comes from a sampled review, labelled **interim**: a fixed number of conversations per use case and per KB each week, graded by domain reviewers against a written rubric.
3. **Specify the five KPI families.** Each KPI gets a definition, a formula, a source, a grain, a refresh rate and an owner:
   - **Volume** by use case, from traces and classification, never from declared usage.
   - **Quality** by KB or domain: share of sampled answers judged correct, with the sample size. One line per KB, never one blended score: a large easy KB hides a failing small one.
   - **Adoption** by population: active users ÷ eligible users per population, as a weekly curve, plus the share who come back within four weeks.
   - **Cost per correct outcome** = cost ÷ (volume × quality), i.e. divided by successes, never by all conversations (references/roi-model.md). State which cost lines the numerator includes: run cost (tokens, infra, licences) and, if counted, review time, which is change cost.
   - **Stale-answer rate** by KB: share of sampled answers that rely on a document past its review date or superseded by a newer version, next to the age of each KB's oldest active document.
4. **Pair every usage KPI with a quality KPI** at the same grain. Sessions, messages or active users never appear alone.
5. **Lay out the dashboard** on one page: volume by use case, quality by KB, adoption curve by population, cost per correct outcome, stale-answer rate by KB. Each line shows its threshold and its sample size; a sample under 30 is flagged as indicative.
6. **Write the monthly review**: each KPI against last month and its target, the decision taken, the owner of each KB action. A stable quality KPI is the evidence this skill gives for a step's L2 gate (references/autonomy-ladder.md); the gate's other facts come from the release plan. Say which steps it gates and since when the KPI has held, with sample sizes.
7. **Hand over the economics.** Volume and quality per use case feed `ai-roi-quantification`. Any gain stated here shows the five lines of references/roi-model.md, or it is not stated.

## Output
A KPI spec following `templates/kpi-spec.md`: source inventory, outcome-event convention, KPI table (five families, each with definition, formula, source, grain, refresh, owner, status), dashboard layout and monthly review template. A KPI that cannot be computed yet says what is missing and who provides it.

## Rules and red lines
- No KPI without a definition, a formula and a source. A missing source is stated, not invented.
- No usage KPI without a quality KPI beside it.
- Cost per correct outcome divides by successes (volume × quality), never by all conversations, messages or sessions.
- Every KB has its own quality line and stale-answer rate.
- Quality comes from sampled review or graders, never from thumbs-up alone.
- No gain or ROI figure without volume × quality × unit value − run cost − change cost (references/roi-model.md).

## Links
references/roi-model.md · references/autonomy-ladder.md · build-evals · conversation-analysis · agent-knowledge-base · ai-roi-quantification

## Sources
- otel-genai: trace fields for model and token usage; the outcome event extends them.
- own-assistant-dashboards: the five KPI families, the outcome event and the per-KB quality line, from dashboards of internal assistants in production (method only).
