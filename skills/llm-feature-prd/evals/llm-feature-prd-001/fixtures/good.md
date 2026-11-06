# PRD: claim thread summaries

Problem: handlers read long email threads before deciding a claim. Outcome metric: average handling time per claim, from 18 to 14 minutes.

## Steps and autonomy
- Summarise the thread into 5 bullets: L1, the handler decides and the full thread stays one click away. Not L2: no action is taken on the summary. Reversible: yes, the handler discards a summary and reads the thread; a claim decided on a wrong summary is not, so the thread stays the source.

## Failure paths
- Wrong summary (a fact missed or invented): the handler flags it in one click, and flagged threads feed the eval set.
- No summary (over 5 seconds): the tool shows the thread as today.
- Prompt injection in a customer email: email text is treated as data, never as instructions.

## Eval plan
Reference summaries written by senior handlers for 60 threads, and a grading rubric (facts covered, nothing invented, decision-relevant facts first) applied by a calibrated judge.

## KPIs
Outcome: handling time per claim. Quality KPI: factual error rate in summaries, from a weekly review of 30 threads.

## Rollout
Shadow mode for two weeks, then a canary with 10 handlers, then general availability.

## Stop conditions
If handling time has not fallen below 16 minutes after 12 weeks of general availability, read from the claims tool logs, we stop the project and remove the feature. Next stage: L2 only if the factual error rate is under 2% on 300 reviewed threads by the end of the quarter.
