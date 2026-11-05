# Dashboard spec: Customer-service assistant (claims and contracts)

The 0.08 EUR figure checks out: 4,160 EUR ÷ 52,000 sessions = 0.08 EUR. One caveat: it's cost per *session*, so the dashboard has to treat "conversation" and "session" as the same thing (see Definitions).

## Metrics

| # | Metric | Definition | Granularity | Last month |
|---|---|---|---|---|
| 1 | Daily sessions | Count of sessions started per calendar day | Daily | 52,000 total (about 1,730/day) |
| 2 | Monthly active users | Distinct policyholders with at least 1 session in the calendar month | Monthly | Not provided |
| 3 | Avg messages per session | Total messages (user + assistant, or user only; pick one) ÷ sessions | Daily and monthly | Not provided |
| 4 | Avg session length | Mean minutes from first to last message, with an inactivity timeout (e.g. 30 min) | Daily and monthly | Not provided |
| 5 | Thumbs-up rate | Thumbs-up ÷ rated sessions | Daily and monthly | 74% |
| 6 | **Cost per conversation** (new) | Total cost ÷ sessions (tokens + hosting + licences) | Monthly | **0.08 EUR** (4,160 ÷ 52,000) |

## Definitions to confirm before the committee meeting

1. **Conversation = session.** If a conversation can span several sessions, or a session can hold several topics, the 0.08 EUR changes. State the equivalence on the dashboard.
2. **Thumbs-up denominator.** Is 74% of rated sessions or of all sessions? Feedback is usually given in a small share of sessions, so also show the **feedback response rate** next to it. Otherwise 74% can mislead.
3. **Cost scope.** Cost includes tokens, hosting and licences. Say whether it includes fixed costs such as licences. If it does, cost per conversation will fall as volume grows, and the committee shouldn't read that as a per-token efficiency gain. Consider showing the variable (token) cost separately.
4. **Message count and session timeout** (items 3 and 4) need one agreed rule each. Otherwise the numbers will shift between reports.
5. **MAU identity.** Say how users are identified (policyholder ID or device/cookie). Anonymous users will inflate MAU.

## Gaps worth a committee decision

The five metrics measure usage and sentiment. They don't show whether the assistant resolves claims and contract questions. I'd suggest adding these, or at least discussing them:

- **Escalation or hand-off rate to a human agent**
- **Resolution (containment) rate**
- **Cost per resolved conversation**, which is more meaningful than cost per session if many sessions end in escalation

## Display notes

- Put cost per conversation and thumbs-up rate in the top KPI row, with month-over-month change.
- Trend lines for daily sessions and MAU. Show averages (messages, length) as single values with a trend.
- Label every tile with its definition on hover, since finance and operations will read these differently.

The spec gives no figures for MAU, messages per session or session length, so those cells are blank. Send me those numbers, or confirm the definitions above, and I can fill them in.