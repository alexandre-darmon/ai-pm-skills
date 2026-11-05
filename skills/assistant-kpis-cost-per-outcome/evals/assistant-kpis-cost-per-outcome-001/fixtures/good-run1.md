# KPI spec: IT helpdesk assistant

## Bottom line for the CIO

**"Cost per resolved request" can't be computed from the current logs.** Nothing in them records whether a request was resolved. The only outcome-like field is the thumbs, and it can't stand in for one (see below).

In two weeks you can show a measured cost per conversation and an interim cost per resolved request. The interim figure comes from a sampled review and must be labelled as interim, with its sample size and confidence interval.

## 1. Source inventory

| Field | Available | Use |
|---|---|---|
| conversation id, timestamp | yes | volume, trend |
| department | yes | adoption and volume by population |
| number of messages | yes | effort proxy only |
| tokens in/out | yes | cost attribution per conversation |
| thumbs up/down | 6% of conversations, 81% up | signal only, not quality |
| monthly cost: 2,600 EUR | yes (aggregate) | numerator |
| use case / topic | **missing** | volume and quality by use case |
| KB / document used | **missing** | quality and stale-answer rate by KB |
| outcome (resolved, escalated, abandoned) | **missing** | the KPI itself |
| ticket opened, with link to conversation id | **missing** | proxy for escalation |
| eligible headcount per department | missing, but HR has it | adoption rate |
| KB owner and review date | missing | stale-answer rate |

**Why the thumbs can't be the outcome:**
- Only 6% of conversations are rated, and people who choose to rate differ from those who don't.
- 81% up among the 6% doesn't mean 81% of all requests were resolved.
- Extrapolating it would present an estimate as a measurement.
- Use it only as a secondary signal, for example to prioritise which down-voted conversations to review first.

## 2. Outcome definition and instrumentation

A request is **resolved** when the employee's problem was solved without human intervention. That means the answer was correct and either the user did not need a human or the assistant's ticket was closed successfully.

Add an outcome event per conversation:

`outcome_id, conversation_id, use_case, kb_id, result (resolved | escalated_ticket | failed | abandoned), source (reviewer | system | user), timestamp`

**Quick wins before the committee:**
- Log whether the assistant opened a ticket. It's one field and it gives you the escalation rate.
- Add a "was the problem solved?" prompt at the end of the conversation. Don't rely on the optional thumbs for this.
- Join to the ticketing system: a new ticket from the same employee within 48 hours on the same topic means the request was likely not resolved.

**Interim quality (labelled interim):**
- Sample about 100 conversations, stratified by department and by length.
- IT agents grade each against a written rubric: correct and resolved, partly, wrong, or escalated.
- A sample of 100 gives roughly ±10 points of uncertainty, so show the interval.

## 3. KPI table

| # | KPI | Formula | Source | Grain | Refresh | Owner | Status |
|---|---|---|---|---|---|---|---|
| 1 | Volume | conversations, classified by use case | logs plus classification | use case, department | weekly | product owner | total computable now; by use case needs classification of a sample |
| 2 | Quality | correct and resolved answers ÷ sampled conversations, with n | reviewed sample | one line per KB or use case, never blended | weekly sample, monthly report | IT service lead | not computable yet (interim review) |
| 3 | Adoption | active users ÷ eligible users, plus 4-week return rate | logs plus HR headcount | department, weekly | weekly | product owner | needs headcount (distinct user id is also not in the logs, so confirm it) |
| 4 | **Cost per resolved request** | run cost ÷ (volume × resolution rate) | cost lines plus KPIs 1 and 2 | monthly, by use case once possible | monthly | product owner with finance | interim from sample |
| 5 | Stale-answer rate | sampled answers relying on an out-of-date or superseded document ÷ sample, plus the age of the oldest active document | reviewed sample plus KB metadata | per KB | monthly | each KB owner | not computable yet |

**KPI 4 in detail:**
- **Numerator:** the 2,600 EUR/month run cost (tokens and hosting). State that it excludes staff time for review, KB maintenance and the project build. Counting those is change cost, which you can show on a separate line.
- **Denominator:** resolved requests, never all conversations.
- **Illustration with made-up numbers:** if there were 3,000 conversations and 60% were resolved, the cost per resolved request would be 2,600 ÷ 1,800 ≈ 1.44 EUR. The cost per conversation would be 0.87 EUR, and using it would understate the real cost.
- **Report both:** cost per conversation (measured now) and cost per resolved request (interim).
- **Add a companion figure:** the cost of a human-handled ticket, from the service desk. Without it, the CIO can't tell whether 1.44 EUR is good.
- **Avoiding double counting:** an escalated conversation is not a success, and its ticket still costs human time. Don't count it as savings.

## 4. Rules for the committee

- Every usage KPI (volume, adoption) sits beside its quality KPI.
- Every sample under 30 is flagged "indicative".
- No savings or ROI figure unless it shows volume × quality × unit value − run cost − change cost. The unit value (minutes saved per resolved request × loaded hourly cost) must be sourced from the service desk, not guessed.
- Don't present thumbs-up as satisfaction.

## 5. Plan for the next two weeks

1. **Days 1–2:** extract the 3 months of conversations, compute cost per conversation, and get headcount per department from HR.
2. **Days 2–5:** add ticket-creation logging, and join the logs to the ticketing system.
3. **Days 3–8:** agents review a stratified sample of about 100 conversations against the rubric. This gives the interim resolution rate, plus the first look at quality by topic.
4. **Days 8–10:** compute the interim cost per resolved request with its interval. Get the cost of a human ticket from the service desk.
5. **Days 10–14:** build the one-page dashboard: volume, quality, adoption, cost per resolved request, stale-answer rate. Everything not yet measurable is marked "not computable yet", with what it needs and who provides it.
6. **In parallel:** switch on the end-of-conversation "solved?" prompt so the real KPI exists from the next month.

## 6. Monthly review template

For each KPI: this month, last month, target, decision taken, owner. Include the sample sizes and the date the outcome logging started. If quality stays stable and above target across several months, you can use it as evidence for expanding what the assistant is allowed to do, such as opening tickets or acting on accounts without human review.

## Questions for you

- Does the ticketing system expose a link or a requester and topic I can join on?
- Is there a user identifier in the logs, or only the conversation id? Adoption needs a user identifier.
- Do you know the service desk's cost per ticket?