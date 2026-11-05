# KPI spec and monthly review: employee assistant

## 1. Source inventory

| Item | Status |
|---|---|
| Run cost | **Known:** 1,900 EUR/month. I don't know which lines it includes (tokens, infra, licences), so I need that breakdown. |
| Conversation volume | **Known:** about 9,000/month. |
| Eligible users | **Known:** 3,500 across 3 countries. I need the split by country. |
| Quality | **Partial:** 84% correct on 200 answers last quarter, blended. I don't know the split by KB, the rubric, or who graded. |
| Volume by KB and use case | **Not computable yet.** I need each trace tagged with the KB(s) used and a use case. |
| Active users | **Not computable yet.** I need a pseudonymous user ID and country on each trace. |
| Document age and version | **Not computable yet.** I need the cited document ID, version and last-review date logged per answer. |
| Outcome (accepted, escalated, abandoned) | **Not logged.** |

**Reading the 84%:** with 200 answers the 95% margin is about ±5 points, so last quarter's true figure is somewhere between about 79% and 89%. The blend also hides the problem. HR is the largest KB and the freshest, so it likely pulls the average up. IT and Travel are my main suspects for the failures, but that's a hypothesis until each KB has its own line.

**Fields to add to traces** (using `gen_ai.*` for model and tokens):
- `trace_id`
- `timestamp`
- `use_case`
- `kb_id`
- `doc_id`, `doc_version`, `doc_last_reviewed`
- `user_pseudo_id`
- `country`
- token counts and cost

**Outcome event:** `outcome_id`, `trace_id`, `use_case`, `result` (success, failure, escalated, abandoned), `value_eur` (empty until someone sources a unit value), `source` (user, system, reviewer), `timestamp`. For IT, a ticket opened right after an answer counts as `escalated`. For Travel, an expense claim rejected for a policy reason counts as `failure`.

## 2. KPI table

| KPI | Formula | Grain | Refresh | Owner | Status |
|---|---|---|---|---|---|
| **Volume** | Count of classified conversations | Use case × KB × country | Weekly | Assistant product owner | Total known (9,000). The split needs tagging. |
| **Quality** | Correct answers ÷ reviewed answers, with n | One line per KB (HR, IT, Travel). Travel is also split into docs updated vs. not updated since September. | Monthly | Domain owners (HR, IT, Finance/Travel) | Interim, from the sampled review. |
| **Adoption** | Active users ÷ eligible users, plus the share returning within 4 weeks | Country, weekly curve | Weekly | Product owner | Not computable yet. It needs user ID and country. |
| **Cost per correct outcome** | Run cost ÷ (volume × quality) | Overall, then per KB once volumes are tagged | Monthly | Product owner with Finance | Overall figure computable now. |
| **Stale-answer rate** | Reviewed answers relying on a document past its review date or superseded ÷ reviewed answers, plus the age of each KB's oldest active document | KB | Monthly | KB owners | Reviewer-flagged now, automated once `doc_id` is logged. |

Rules for the table:
- Every volume or adoption number is shown beside the quality line at the same grain.
- Cost is run cost only. Reviewer time is change cost and is reported on its own line.

**Baseline for cost per correct outcome:**
- 1,900 ÷ 9,000 = **0.21 EUR per conversation**.
- 1,900 ÷ (9,000 × 0.84) = **about 0.25 EUR per correct outcome**.
- Treat 0.25 as indicative because of the ±5-point margin on the 84%.
- Every 10 points of quality lost raises the figure by about 0.03 EUR. At this scale, cost is not the risk. Wrong answers are.

I won't state any gain or ROI figure yet. It needs unit values per use case and the change cost, and it goes to `ai-roi-quantification`.

## 3. Monthly review sample

- **Size:** 60 conversations per KB per month, 180 in total. Draw them at random, stratified by country. Drawing evenly per KB matters here: Travel is only 60 documents and would otherwise end up under 30, which is indicative only.
- **Travel:** within the 60, make sure both groups are represented, the documents updated in September and the ones not updated. This tells you whether the half-updated state is causing the errors.
- **Rubric (written once, then frozen):**
  - Correct, partially correct, or incorrect.
  - Cites a current document, yes or no.
  - Right country policy, yes or no.
  - Should have escalated or refused, yes or no.
- **Reviewers:** one domain reviewer per KB, plus a second reviewer on 10 conversations per KB to check agreement.
- **Reading:** a result of 54/60 is 90% with a margin of about ±8 points. Compare months with that margin in mind, and don't react to a 3-point move.
- **Review cost:** log reviewer hours each month as change cost.

## 4. One-page dashboard

1. Volume by use case and KB (the table in section 2).
2. Quality by KB, three lines, each with its threshold and n. Flag n < 30 as indicative.
3. Adoption curve by country.
4. Cost per correct outcome, with the cost lines stated.
5. Stale-answer rate by KB, next to the age of each KB's oldest active document.

**Proposed thresholds** (these are starting points for the owners to agree):

| KPI | Proposed threshold |
|---|---|
| Quality, HR | ≥ 90% |
| Quality, IT | ≥ 85% |
| Quality, Travel | ≥ 85% |
| Stale-answer rate | < 5% per KB |
| Oldest active document | < 12 months |

## 5. Monthly review template

Attendees: the product owner and the three KB owners. The agenda takes about 45 minutes.

| KPI | Last month | This month (n) | Target | Decision | Owner and date |
|---|---|---|---|---|---|

Fixed agenda:
1. Quality by KB against target, then the top 5 failure patterns per KB.
2. Stale-answer rate, then the list of documents to retire or update.
3. Adoption by country, and whether a drop in a country coincides with a drop in quality.
4. Cost per correct outcome and the reviewer hours spent.
5. Actions, each with a named KB owner and a date. Check last month's actions first.

## 6. Priorities for the first review

1. **IT:** run a full review of the 180 documents, starting with everything that mentions the old ticketing tool. 14 months without a review plus a tool change means answers may point people to a system that no longer exists. Fix this before measuring anything else.
2. **Travel:** finish updating the other half of the documents to the September policy. In the meantime, check whether the assistant is mixing old and new rules. Use `doc_version` to see which one it cites.
3. **Instrumentation:** add the trace fields and the outcome event. Without them, volume by KB, adoption and automated staleness stay uncomputable.
4. **Baseline:** run the first sampled review within the next two weeks, so that the November review has real per-KB numbers instead of the blended 84%.

**What I need from you:**
- The cost breakdown.
- Eligible headcount per country.
- The owner of each KB.
- A decision on who does the reviews.

I can turn this into a spreadsheet or a dashboard mockup if you want one.