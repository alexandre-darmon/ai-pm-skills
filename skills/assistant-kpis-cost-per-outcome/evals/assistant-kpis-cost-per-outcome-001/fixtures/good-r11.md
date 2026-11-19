# KPI spec: IT helpdesk assistant

## 1. What the logs support today

| Field | Available | Limit |
|---|---|---|
| Conversation id, timestamp, department, messages, tokens in/out | Yes | Gives volume and token cost only. |
| Thumbs up/down | On ~6% of conversations (81% up) | Not a quality source. Raters are self-selected, and 94% of conversations are unrated. "81% satisfied" can't be extended to the rest. |
| Use case (password reset, VPN, etc.) | No | Needs classification of conversations. |
| Knowledge base (KB) or document used | No | Needed for per-KB quality and stale answers. |
| Outcome (resolved, escalated, abandoned, redone) | No | This is the gap. Today you can count conversations, not resolutions. |
| Link to the ticket tool | No | Needed for the redo rate and for escalations. |
| Eligible users and the old channel (phone, portal) | Headcount (4,000) only | Bypass rate can't be computed without old-channel volumes. |

Not computable today: resolved-request cost, quality, redo rate, bypass rate and stale-answer rate. The only exact figure is cost per conversation, which is 2,600 EUR ÷ the number of conversations in the month. It is not a cost per resolved request, and it shouldn't be presented as one.

## 2. Headline KPI: cost per correct outcome

**Cost per resolved request = monthly run cost ÷ (conversations × verified resolution rate)**

- **Numerator:** 2,600 EUR (tokens and hosting). Show review time separately as change cost, not in the headline.
- **Denominator:** only successes. A conversation counts as resolved if the employee's need was met and the employee did not come back for the same issue within the redo window. The window is 7 days, to be confirmed with the helpdesk.
- **Escalated, abandoned or redone** conversations are failures. A ticket opened by the assistant is an escalation, not a resolution. Report "ticket opened" as its own outcome. It still has value (a well-qualified ticket), but it isn't a resolved request.
- **Grain:** per month, then per use case, once classification exists.
- **Owner:** the product owner of the assistant. Finance validates the numerator.

For the steering committee, show it as a **range with sample size**, labelled **interim** (from sampled review), for example "X–Y EUR per resolved request, n=300". Don't show a single point figure. Sampling error at n=300 is about ±5 points on the resolution rate.

## 3. Outcome event (new instrumentation)

One event per conversation: `outcome_id`, `conversation_id`, `use_case`, `result` (success, failure, escalated, abandoned, redone), `source` (user, system, reviewer), `value_eur` (left empty until the helpdesk supplies a unit value), `timestamp`.

- **Latest event wins.** If the same employee opens a ticket or contacts the helpdesk on the same topic within 7 days of a "success", add a `redone` event and the conversation stops counting as a success.
- **System signals:** ticket created by the assistant, a ticket opened afterwards by the same employee on the same topic, and a conversation ending with no follow-up.
- **Token fields:** follow the OpenTelemetry `gen_ai.*` conventions.

## 4. KPI table

| Family | KPI | Formula | Source | Grain / refresh | Status |
|---|---|---|---|---|---|
| Volume | Conversations by use case | Count, classified | Logs plus a classifier or manual labelling | Use case, weekly | Total computable now. By use case, needs classification. |
| Quality | Verified resolution rate | Reviewed answers judged correct and resolving ÷ reviewed answers | Sampled review by helpdesk agents with a written rubric | Per KB and use case, weekly. Interim: 75 conversations per week, spread across use cases. | Not computable. Review starts this week. |
| Quality | Redo rate | Successes later redone ÷ logged successes | Ticket-tool link by employee id and topic within 7 days | Use case, weekly | Not computable until the link exists. Never shown as 0. |
| Quality | Escalation rate | Conversations ending in a ticket or human handoff ÷ conversations | Ticket creation events | Use case, weekly | Computable once tickets are linked to conversations. |
| Adoption | Active users ÷ eligible users | Distinct employees ÷ headcount | Logs (needs an employee id, see §6) | Department, weekly curve, plus the share returning within 4 weeks | Partly. Department is available, the employee id is to be confirmed. |
| Adoption | Bypass rate | In-scope requests reaching the phone or portal without the assistant ÷ all in-scope requests | Old-channel ticket volumes by category | Use case, monthly | Not computable until the helpdesk provides old-channel volumes. |
| Cost | Cost per correct outcome | §2 | Finance plus the above | Monthly | Interim only. |
| Cost | Cost per conversation | 2,600 EUR ÷ conversations | Logs and finance | Monthly | Computable now. Show it as context, never as the headline. |
| Stale answers | Stale-answer rate | Reviewed answers relying on an out-of-date or superseded document ÷ reviewed answers | Review sample plus KB review dates | Per KB, monthly. Also the age of the oldest active document per KB. | Not computable. Needs a list of KBs with owners and review dates. |

**Pairing rule:** conversations, messages and active users never appear without the resolution rate at the same grain. Quality is reported per KB, not as one blended score, because a large easy KB (passwords) can hide a failing small one (VPN, mobile devices). A sample under 30 is flagged "indicative".

**Thumbs:** keep collecting them, but show only as "rated conversations (6%): 81% positive". They are useful for spotting bad conversations to review. Don't use them as the quality KPI.

## 5. Dashboard (one page)

1. Conversations by use case, with the resolution rate beside each.
2. Resolution rate by KB, with n and the target.
3. Adoption curve by department.
4. Cost per correct outcome (range, labelled interim), with cost per conversation beside it.
5. Stale-answer rate by KB, and the age of each KB's oldest document.
6. Redo rate and escalation rate by use case.

Each line shows its threshold, its sample size and an "interim" or "measured" label.

## 6. Plan for the committee in two weeks

| When | Action | Owner |
|---|---|---|
| Days 1–2 | Confirm the log fields (an employee id, the conversation-to-ticket link). Get monthly conversation counts. Define the 7-day redo window with the helpdesk. | Product owner, IT data |
| Days 2–5 | Classify a sample into use cases. Write the review rubric (resolved, partially resolved, wrong, outdated). | Helpdesk lead |
| Days 3–10 | Review about 300 conversations (stratified by use case and department), preferably double-reviewing 10% to check agreement. | Helpdesk agents |
| Days 8–11 | Compute the interim cost per resolved request as a range. Link tickets to conversations retroactively where the data allows. | Data analyst |
| Days 11–14 | Build the one-page dashboard. Prepare the narrative on what is measured and what is interim. | Product owner |

## 7. Caveats for the CIO

- **No gain or ROI figure yet.** A saving needs volume × quality × a unit value per request (for example, the helpdesk's cost of handling an equivalent ticket) minus run cost and change cost. No unit value has been sourced, so don't state one.
- **Cost per resolved request will be higher than cost per conversation.** Dividing by successes instead of all conversations is the correct way, and the committee should hear that before seeing the number.
- **The review sample is change cost.** Report its time separately, and plan to replace it with the outcome events once they are logged.

If you can share the monthly conversation count and the fields in your ticket tool, I can fill in the cost per conversation and draft the review rubric.