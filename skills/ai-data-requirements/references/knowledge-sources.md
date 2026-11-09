# Knowledge sources: versions, review and KPIs

Detail for Part B of `ai-data-requirements` (documents an assistant retrieves from).

## 1. Expiry versus dated versions

Two different things age in a knowledge base, and they get different rules.

| Situation | Rule |
|---|---|
| The current version of a source has not been checked for a while | Expiry: a number of days or months per source type, set from how often it really changes. Past expiry, the owner re-certifies or the source leaves the index. |
| A source was replaced by a newer version, and the old one still answers questions about its period (policy, rate, tariff, contract terms, procedure in force at a date) | Not expired: its content no longer changes. Keep it with effective-from and effective-to dates; questions about today are filtered to the version in force; questions about a past date (a claim filed last year, a loan signed in 2024) reach the version in force then. |
| A source was replaced and its past versions answer no question (FAQ page, contact list) | Replace it; the old version leaves the index. |

Setting expiry: start from the observed change frequency (a yearly policy revised in January: about 13 months, so the January revision lands before expiry; a spec engineering changes weekly: 7 to 14 days unless re-certified). State the number per source type in the register; "regularly" is not an expiry.

Removing old versions looks like hygiene. In a regulated business it destroys the answer to "what applied when this was filed?", which complaints, audits and claims ask every week.

## 2. Retirement path and monthly review

- A source retires when its owner withdraws it, when it fails re-certification, or, for a dated version, when no question can still reach its period, subject to legal retention.
- Monthly review, owned by the knowledge-base owner: sources past expiry, owner changes (a leaver makes a source ownerless: blocker again), questions with no good source (from the no-source path and from `conversation-analysis`), new sources requested.
- Each review is dated and its decisions logged in the register.

## 3. KPIs handed to assistant-kpis-cost-per-outcome

Both are measured on a sample of answers, never assumed from the register.

- **Stale-answer rate**: share of sampled answers citing an expired source, or a version outside its effective period for the question asked.
- **Untraceable-claim rate**: share of sampled answers with a factual claim no cited source supports.

This skill defines the KPI and its sampling unit (one answer); the sample size and interval are set where the KPI is measured.

## 4. Labelled queries for the retrieval test

From the question inventory, write pairs (question, source that should be found), per question class, including questions whose answer is in no source (expected: the no-source path). They go to `build-evals` and `retrieval-evaluation`, which own the test, its size and its thresholds. Rerun them before launch and after each source change.
