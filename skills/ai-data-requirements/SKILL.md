---
name: ai-data-requirements
description: 'Specify what an AI feature reads and writes. Use on "what data do we need", a DPO asking what is processed, or to set up or review a RAG store: stale answers, mixed sensitivity, unowned docs.'
license: CC-BY-4.0
metadata:
  stage: "specify"
  version: "0.3.0"
  status: "tested"
  eval_threshold: "0.80"
  autonomy_relevant: "false"
  depends_on: "llm-feature-prd"
  feeds: "synthetic-eval-data, build-evals, retrieval-evaluation, production-evals-monitoring, assistant-kpis-cost-per-outcome, process-ai-redesign"
  sources: "dama-dmbok, gdpr, own-data-platform, own-assistant-mission, own-rag-practice, repo-vishalhabib, repo-product-on-purpose, repo-chanmeng"
---

# ai-data-requirements

## When to use
- A PRD is done and the data for the AI feature must be specified: "what data do we need?", a data team asks for a spec.
- A DPO or privacy office asks what the feature processes and where each field ends up (prompt, logs, eval set, vendor, training).
- A team sets up retrieval (RAG, vector store) for an assistant and must pick the documents, or a new domain or user population is added.
- Answers are stale or contradict each other, nobody knows who maintains the knowledge base, or one index mixes public and restricted documents.
- Do not use to measure retrieval quality (recall, wrong document cited, a re-index or new embedding model): use `retrieval-evaluation`.
- Do not use to define business metrics (MRR, churn) or assistant KPIs: metric definitions are out of scope, and assistant KPIs belong to `assistant-kpis-cost-per-outcome`.

## Inputs
Mandatory: the PRD or feature description; the candidate tables and fields, and/or the candidate documents (docs, wikis, procedures, tickets); who the users are.
Ask if missing: owner per source, access constraints, retention rules, how often each source changes, sensitivity per source, the question inventory for a retrieval feature, volumes and model calls per day.

## Method
The skill owns everything the feature reads or writes. Part A covers structured fields and their flows; Part B covers the documents an assistant retrieves from. Run Part A always (retrieved chunks are fields too: they reach the prompt, the logs and the vendor), Part B when the feature retrieves documents. Steps 1 and 2 apply to both.

**Common to every source**

1. **One owner per source, or it is out.** A table or document with no named owner (person or team) is a blocker: it is excluded or escalated to the sponsor, never used or indexed by default "because a script updates it" or "because more content helps". Count the excluded sources and say what the feature loses without them.
2. **Measure, don't assume.** Every threshold is a number with the value measured today beside it, on a real, unfiltered sample: a curated sample overstates what the model will meet. No access to the data: write "not measured" and make the measurement an open action, never an estimate.

**Part A: fields and flows**

3. List sources and fields per step of the feature; drop any field no step needs. Give the volume per source and the model calls per day: they set token cost and the volume term `ai-roi-quantification` checks. If the brief has none, list it as open; never invent it.
4. Quality thresholds per source: completeness, freshness as a maximum age in minutes, hours or days, duplication, and for training or eval data, label quality (who labels and how: `build-evals`). Below the bar is a blocker.
5. Flag personal data per field, then state in one sentence per source whether it holds any. Each flagged field gets a lawful basis (GDPR art. 6) for the DPO to confirm, or is dropped; never "TBD". Special categories (art. 9) go to the DPO with a question on an impact assessment (art. 35).
6. Map where each field flows: prompt, retrieved context, logs and traces, eval set, vendor, training. Per destination: masked or clear, and retention as a number. A personal-data field reaching the eval set or training is a further purpose: it needs its own basis or a compatibility assessment (art. 6(4)) for the DPO, or it stays out. This table is the single record of AI data flows; `production-evals-monitoring` reads it before any trace reaches a judge.
7. Pseudonymisation plan by destination (what is masked or tokenised before the model, the logs and the vendor see it, where the key lives), then lineage, refresh cadence and retention per source, as numbers.

**Part B: documents the assistant retrieves**

8. **Source register**: source, owner, refresh cadence, expiry, effective dates, sensitivity, format, users allowed. Expiry is a number of days or months set from how often the source really changes (a policy revised yearly does not expire like a weekly spec); past expiry the owner re-certifies or the source leaves the index.
9. **Dated versions, not deletion.** A replaced version of a time-bound source (policy, rate, contract terms) keeps effective-from and effective-to dates and stays retrievable for questions about its period; questions about today are filtered to the version in force. Deleting it destroys the answer to "what applied when this was filed?". A source whose past versions answer nothing (an FAQ page) is simply replaced. Detail: references/knowledge-sources.md §1.
10. **Segregate by sensitivity and audience**: separate indexes or collections with access control at retrieval, from the user's own permissions, so nobody retrieves what they could not open. Mixed sensitivity in one index without that filter is a blocker; restricted personal data (salary grids, health) also goes through step 5.
11. **Chunk metadata and no-source behaviour.** Every chunk carries owner, version, effective dates and expiry. When retrieval is empty, weak or conflicting, the assistant does not answer from the closest document: it says it has no basis, names what is missing and routes to the source owner. Every excluded source makes this path more frequent, so it is set before launch.
12. **Hand-offs.** From the question inventory, write labelled queries (question, source that should be found) and hand them to `retrieval-evaluation` via `build-evals`. Define the stale-answer KPI and the untraceable-claim KPI on a sample and hand them to `assistant-kpis-cost-per-outcome`. Set the retirement path and the monthly review (references/knowledge-sources.md §2–3).

## Output
`templates/data-requirements.md`, all Part A headings present and one row per field; Part B headings present when the feature retrieves documents. Blockers come first in the reply, before the tables.

## Rules and red lines
- One owner per source, table or document, or it is out; never "index everything" or "use it as it is".
- Every personal-data field has a lawful basis or is dropped; never "to be defined".
- Freshness and expiry are numbers, never "regularly" or "as needed".
- A field with a blank flow destination is unspecified: say no, or say where and for how long.
- Never clean the sample before measuring: its messy records are what the model will meet.
- Restricted documents never share an index with open ones without access control at retrieval.
- A replaced version that still answers questions about its period is dated, not deleted.
- Empty, weak or conflicting retrieval never produces an answer from the closest document.

## Links
llm-feature-prd · build-evals · retrieval-evaluation · synthetic-eval-data · production-evals-monitoring · assistant-kpis-cost-per-outcome · ai-roi-quantification

## Sources
- dama-dmbok: data-quality dimensions.
- gdpr: minimisation and lawful basis (art. 5, 6), further purposes (art. 6(4)), impact assessment (art. 35).
- own-data-platform: owner-or-out rule, field-level sheet.
- own-assistant-mission: owner-and-expiry register and the monthly review, method only.
- own-rag-practice: metadata on every chunk, segregation by audience, stale-answer sampling.
- repo-vishalhabib: framing data handling by where sensitive data ends up (logs, prompts, third parties).
- repo-product-on-purpose: trace capture, redaction and retention as a privacy concern.
- repo-chanmeng: dirty data as the test; effective-date ranges and refusal on a retrieval miss; untraceable claims. Ideas only, own words.
