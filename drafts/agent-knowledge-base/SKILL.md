---
name: agent-knowledge-base
description: 'Plan the knowledge an assistant or agent retrieves from: source register, owners, expiry, sensitivity, review ritual. Use for "set up the RAG", stale answers, or a KB nobody maintains.'
stage: specify
version: 0.2.0
depends_on: [ai-data-requirements]
feeds: [assistant-kpis-cost-per-outcome, build-evals, conversation-analysis, process-ai-redesign]
autonomy_relevant: false
sources: [own-assistant-mission, own-rag-practice, repo-chanmeng]
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
2. Set an expiry per source type as a number of days or months, from how often the source really changes: a policy revised yearly does not expire like a weekly product spec. Past expiry, the owner re-certifies or the source leaves the index. A replaced version is not expired: its content no longer changes, and step 3 governs it.
3. Write inclusion and exclusion rules: drafts, duplicates, personal data that the use case does not need. Do not exclude a replaced version of a time-bound source (policy, rate, contract terms). It carries effective-from and effective-to dates and stays retrievable for questions about its period; questions about today are filtered to the version in force. Removing it looks like hygiene and destroys the answer to "what applied when this was filed?". A source whose past versions answer no question (an FAQ page) is simply replaced.
4. Segregate by sensitivity and audience: separate indexes or collections with access control at retrieval, so a user never retrieves what they could not open. Mixed sensitivity in one index without access filtering is a blocker.
5. Chunk along the document's structure, and let the retrieval test in step 7 validate it. Carry owner, version, effective dates and expiry on every chunk, so answers can cite and age-check their source.
6. Define the no-source behaviour: when retrieval is empty, weak or conflicting, the assistant does not answer from the closest document. It says it has no basis, names what is missing (a period, an entity, a document) and routes the person to the source owner. List the question classes the knowledge base does not cover. Every source left out makes this path more frequent, so it is set before launch.
7. From the question inventory, write labelled queries (question, source that should be found) and hand them to `build-evals`, which owns the retrieval test, before launch and after each source change.
8. Define the retirement path for a source and the monthly review ritual: expired sources, owner changes, questions with no good source. A dated version retires when no question can still reach its period, subject to legal retention.
9. Define the stale-answer KPI (share of sampled answers citing an expired source, or a version outside its effective period for the question asked) and the untraceable-claim KPI (share of sampled answers with a factual claim no cited source supports), and hand both to `assistant-kpis-cost-per-outcome`. Quality of the knowledge base is measured on a sample, not assumed.

## Output
`templates/kb-plan.md`, all headings present.

## Rules and red lines
- No source without an owner.
- Every source has an expiry stated as a number, never "regularly".
- Restricted sources never share an index with open ones without access control at retrieval.
- Every source has a retirement path.
- A replaced version that still answers questions about its period is dated, not deleted.
- Empty, weak or conflicting retrieval never produces an answer from the closest document.

## Links
assistant-kpis-cost-per-outcome · build-evals · conversation-analysis · ai-data-requirements · semantic-layer-design

## Sources
- own-assistant-mission: owner-and-expiry register and the monthly review, method only.
- own-rag-practice: metadata on every chunk, segregation by audience, stale-answer sampling.
- repo-chanmeng: effective-date ranges and the refusal rule on a retrieval miss (production-readiness section 9), untraceable claims and retrieval judged before generation (evaluation). Ideas only, own words.
