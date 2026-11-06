---
name: agent-knowledge-base
description: 'Plan the knowledge an assistant or agent retrieves from: source register, owners, expiry, sensitivity, review ritual. Use for "set up the RAG", stale answers, or a KB nobody maintains.'
stage: data
version: 0.1.0
depends_on: [ai-data-requirements]
feeds: [assistant-kpis-cost-per-outcome, conversation-analysis, process-ai-redesign]
autonomy_relevant: false
sources: [own-assistant-mission, own-rag-practice]
eval_threshold: 0.80
status: draft
---

# agent-knowledge-base

## When to use
- A team sets up retrieval (RAG) for an assistant or agent and must pick sources.
- Answers are outdated, contradict each other, or nobody knows who maintains the knowledge base.
- A new domain or a new population of users is added to an existing assistant.
- Do not use to define the assistant's KPIs: use `assistant-kpis-cost-per-outcome`.
- Do not use for structured metrics and tables: use `semantic-layer-design`.

## Inputs
Mandatory: the candidate sources (docs, wikis, tickets, policies) with their owners if known, and who the users are.
Ask if missing: how often each source changes, its sensitivity (public, internal, restricted, personal data), the question inventory.

## Method
1. Build the source register: source, owner (a named person or team), refresh cadence, sensitivity, format, users allowed. A source without an owner is excluded or escalated to a sponsor; it is never indexed by default. Count them.
2. Set an expiry per source type as a number of days or months, from how often the source really changes: a policy revised yearly does not expire like a weekly product spec. Past expiry, the owner re-certifies or the source leaves the index.
3. Write inclusion and exclusion rules: drafts, duplicates, superseded versions, personal data that the use case does not need.
4. Segregate by sensitivity and audience: separate indexes or collections with access control at retrieval, so a user never retrieves what they could not open. Mixed sensitivity in one index without access filtering is a blocker.
5. Give chunking and metadata guidance: owner, version, effective date and expiry carried on every chunk, so answers can cite and age-check their source.
6. Define the retirement path for a source and the monthly review ritual: expired sources, owner changes, questions with no good source.
7. Define the stale-answer KPI (share of sampled answers citing an expired or superseded source) and hand it to `assistant-kpis-cost-per-outcome`. Quality of the knowledge base is measured on a sample, not assumed.

## Output
`templates/kb-plan.md`, all headings present.

## Rules and red lines
- No source without an owner.
- Every source has an expiry stated as a number, never "regularly".
- Restricted sources never share an index with open ones without access control at retrieval.
- Every source has a retirement path.

## Links
assistant-kpis-cost-per-outcome · conversation-analysis · ai-data-requirements · semantic-layer-design

## Sources
- own-assistant-mission: owner-and-expiry register and the monthly review, method only.
- own-rag-practice: metadata on every chunk, segregation by audience, stale-answer sampling.
