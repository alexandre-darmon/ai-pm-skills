# KPI spec and monthly review: employee assistant

## 1. Source inventory

| Field | Status |
|---|---|
| Conversations per month (9,000) | Known. I need the trace id, timestamp, KB and country on each one. |
| Use-case or KB classification per conversation | **Not confirmed.** Without it, volume per KB is not computable. Add a classifier or the retrieval metadata (which KB the cited documents came from). |
| User population (3 countries) | **Not confirmed.** Needed for adoption per country. |
| Active users (distinct employees) | **Not confirmed.** I can't compute adoption without it. |
| Run cost (1,900 EUR/month) | Known as a total. Split it into tokens, infrastructure and licences. |
| Quality | One review of 200 answers, 84% overall, **no breakdown per KB**. Treat it as a single blended data point. |
| Document review date and version per KB document | HR is known (<3 months). IT is 14 months old. T&E is mixed. A per-document date and "superseded by" field must exist. |
| Outcomes (accepted, escalated, abandoned) | Not logged. Quality stays **interim**, from sampled review. |

**What the numbers say so far**
- Run cost per conversation is 1,900 ÷ 9,000 = **0.21 EUR**.
- Cost per correct outcome, using the blended 84%, is 1,900 ÷ (9,000 × 0.84) = **0.25 EUR**. This is indicative only.
- With n = 200, the 84% has a margin of about ±5 points. The blended figure can hide a failing KB. HR (240 documents, all recent) likely carries the average, while IT and T&E are the likely weak spots.

## 2. Outcome event (added to each trace)
`outcome_id, trace_id, use_case, kb, country, result (success | failure | escalated | abandoned), value_eur (empty until a unit value is sourced), source (user | system | reviewer), timestamp`. Model and token fields follow the OpenTelemetry `gen_ai.*` conventions.

Until outcomes are logged, use the sampled review below. Label it interim.

## 3. KPI table

| Family | Definition and formula | Source | Grain | Refresh | Owner | Status |
|---|---|---|---|---|---|---|
| **Volume** | Conversations per use case, by KB and country | Traces and classification | KB × country | Weekly | Assistant product owner | Needs classification |
| **Quality** | Correct sampled answers ÷ sampled answers, with n | Reviewer grading against a written rubric | **One line per KB** (HR, IT, T&E), T&E also by country | Monthly, with a weekly sample | One domain reviewer per KB | Interim, **to start** |
| **Adoption** | Active users ÷ eligible users, plus the share returning within 4 weeks | Traces (distinct user) and HR headcount | Country (3,500 eligible in total) | Weekly | Product owner | Not computable yet (no user id or per-country headcount) |
| **Cost per correct outcome** | Run cost ÷ (volume × quality). The numerator is run cost only. Review time is reported separately as change cost. | Finance and traces | KB, then total | Monthly | Product owner and finance | Computable at total level only |
| **Stale-answer rate** | Sampled answers that rely on a document past its review date or superseded ÷ sampled answers. Also report the age of the oldest active document per KB. | Review sample, plus the document register | KB | Monthly | KB owner | To start |

Every usage KPI (volume, adoption) is shown next to the quality line for the same KB or country.

## 4. Monthly sample
Each KB needs at least 30 graded answers to be more than indicative. The sample is oversized where the risk is highest:

| KB | Answers per month | Why |
|---|---|---|
| HR | 60 | Recently reviewed. A lower-risk baseline. |
| IT | 80 | Last full review was 14 months ago, and the ticketing tool changed in spring. Old procedures probably still describe the previous tool. |
| Travel and expenses | 80, split across the 3 countries | The September policy change was only half applied, so old and new documents may contradict each other. |

That is 220 answers a month. I'd have reviewers grade about 55 a week. Any cell under 30 is flagged "indicative".

## 5. Dashboard (one page)
1. Volume by KB and country, with the quality value beside it.
2. Quality by KB (three lines), with n and a threshold.
3. Adoption curve by country, with the 4-week return rate.
4. Cost per correct outcome: total, and per KB once volumes are classified.
5. Stale-answer rate by KB, with the age of the oldest active document.

Thresholds are for you to set. As a starting proposal, quality ≥ 90% per KB and stale-answer rate ≤ 5%. Today's 84% would be below that bar overall.

## 6. Monthly review template
For each KPI, record this month, last month, target and the decision taken. Attach an owner and a date to every action.

1. Quality per KB against target, with n. Name the worst failure types.
2. Stale-answer rate per KB. List the documents that caused stale answers.
3. Adoption per country, and whether the low-quality KBs are driving people away.
4. Cost per correct outcome, and the cost lines included.
5. Actions, one per owner. Examples are listed below.
6. Autonomy gate: state which steps the quality KPI supports and since when it has held, with n. Don't claim stability before about three monthly readings.

**First actions I'd propose**
- **T&E owner:** finish updating the other ~30 documents to the September policy, or withdraw the old ones from the index. This is likely the biggest source of wrong answers.
- **IT owner:** run a full review of the 180 documents. Start with those mentioning the old ticketing tool.
- **Product owner:** add the KB, country and user id to the traces, and log outcome events.
- **Reviewers:** run the first stratified sample to get a real per-KB baseline before setting targets.

## 7. ROI
I don't state any gain figure. A gain needs volume × quality × unit value − run cost − change cost, and no unit value is sourced yet (for example, minutes saved per HR or IT question). Once volume and quality are available per use case, these feed the ROI quantification.

## What I need from you
- Does the 200-answer review have a per-KB split?
- Are user ids and the KB used available in the traces?
- Who owns each KB?