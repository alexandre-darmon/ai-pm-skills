I've finalised the spec below, with one change to the cost line. The 0.08 EUR figure is correct arithmetic (4,160 ÷ 52,000), but it is cost per session. Divided by all sessions, it hides how many answers were wrong. Cost per correct outcome divides by successes, so I've made that the dashboard KPI and kept 0.08 EUR as a secondary line. The quality figure it needs doesn't exist yet.

# Dashboard spec: claims and contracts assistant (for steering committee)

## 1. Status of the requested KPIs

| KPI | Computable now? | Change |
|---|---|---|
| Daily sessions | Yes, from traces | Break down by use case (claims vs contracts) |
| Monthly active users | Yes | Show as a share of eligible policyholders, which needs the headcount from the business |
| Avg messages per session | Yes | Usage only, so it needs a quality KPI next to it |
| Avg session length | Yes | Same as above. Longer can mean engagement or failure. |
| Thumbs-up rate (74%) | Yes | **Not a quality measure.** Only some users vote, and a vote doesn't show whether the answer was correct. Keep it as a satisfaction signal only. |
| Cost per conversation (0.08 EUR) | Yes, as cost per session | Keep as a secondary line. The headline KPI is cost per correct outcome. |

## 2. Added KPIs

| KPI | Definition and formula | Source | Grain / refresh | Status |
|---|---|---|---|---|
| **Quality** | Share of sampled answers judged correct by domain reviewers against a written rubric, shown with the sample size | Weekly sampled review (labelled **interim**) | Per knowledge base (KB) and use case, weekly | **Not computable yet.** Needs a reviewer and a fixed weekly sample, for example 30 or more conversations per KB. |
| **Cost per correct outcome** | Run cost ÷ (sessions × quality). The numerator is tokens, hosting and licences. Review time is change cost and is shown separately. | Finance and traces, plus quality | Monthly | **Not computable yet.** It needs quality. |
| **Stale-answer rate** | Share of sampled answers that rely on a document past its review date or superseded by a newer one, plus the age of each KB's oldest active document | Sampled review and KB metadata | Per KB, monthly | **Not computable yet.** Needs each KB's owner and last review date. |
| **Outcome event** | Fields: `outcome_id`, `trace_id`, `use_case`, `result` (success, failure, escalated, abandoned), `value_eur`, `source`, `timestamp` | To instrument | Per trace | Not computable yet. |

## 3. What cost per correct outcome means for the 0.08 EUR

The figure is 0.08 EUR ÷ quality, so it is always higher than 0.08 EUR. Using 0.08 EUR for last month, it works out as follows. These are sensitivity values, not measurements:

| If sampled quality turns out to be | Cost per correct outcome |
|---|---|
| 90% | 0.089 EUR |
| 74% | 0.108 EUR |
| 60% | 0.133 EUR |

The 74% row is only an illustration of what the thumbs-up rate would imply if it were quality. It shouldn't be presented as a measured result.

## 4. One-page layout

1. Sessions per day by use case, next to quality for the same use case.
2. Quality per KB, with the sample size. Samples under 30 are flagged as indicative.
3. Monthly active users ÷ eligible policyholders, as a weekly curve plus the four-week return rate.
4. Cost per correct outcome (headline), with cost per session in smaller type.
5. Stale-answer rate per KB.
6. Messages per session, session length and thumbs-up rate sit in a "usage and satisfaction" strip. They carry no targets.

## 5. Monthly review

Each KPI is shown against last month and its target. The review records the decision taken and the owner of each KB action. Once quality has held steady, state which autonomy steps it supports and since when, with the sample sizes.

## 6. Decisions for the committee

1. Appoint a reviewer and approve the weekly sample, which is the only source of quality for now.
2. Have Finance break last month's 4,160 EUR into tokens, hosting and licences. Also confirm that "sessions" and "conversations" mean the same thing.
3. Provide eligible-policyholder counts and a KB owner and review date for each KB.
4. Approve adding the outcome event, for example claim filed or escalated to an agent, so the interim sampling can later be replaced by logged outcomes.

Until item 1 is in place, the dashboard should show cost per session (0.08 EUR). It should not show a "cost per outcome" figure.