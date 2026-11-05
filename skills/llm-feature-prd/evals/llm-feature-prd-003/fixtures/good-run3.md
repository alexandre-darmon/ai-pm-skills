I haven't written the PRD. The one metric you gave is a usage metric, and the PRD method I'm using requires an outcome metric first. It says to stop and ask even when told to skip questions or add metrics later. A PRD built around a placeholder would fail the committee's first question, "how will we know it worked?"

**"2,000 questions answered per month" is usage.** It counts activity, not whether employees got correct answers or whether HR's workload fell. It's also low for 3,000 employees. That's under one question per employee per month, so it may not be the right target.

**"30% productivity for HR" has no basis yet.** The PRD rules say a gain needs volume × quality × unit value behind it. To support it, we need:
- how many policy questions HR handles today per month
- the share of those a bot could answer correctly
- the minutes HR spends per question

## Problem statement (ready to reuse)
About 3,000 employees ask HR repeated questions on leave, expenses and remote work. The answers already exist in policy documents, but they're hard to find, so HR answers them by hand. We want an assistant, hosted in the EU and working in French, that answers from those documents so HR spends less time on routine questions.

## Outcome metric (to confirm)
Pick one, or propose your own:
- **Deflection:** the share of policy questions resolved without an HR ticket, for example from X to Y.
- **HR time:** hours per month HR spends on policy questions, from X to Y.
- **Answer quality:** the share of answers that are correct and cite the right source, as judged by HR on a sample.

Keep 2,000 questions per month as a usage KPI, paired with whichever quality KPI you pick.

## What I need from you
| Missing | Who provides it |
|---|---|
| Outcome metric and target | Sponsor and HR lead |
| Current HR volume of policy questions per month and minutes per question | HR operations |
| Basis for the 30% figure | Sponsor |
| Policy documents: format, owner, how often they change, whether any are out of date | HR |
| Whether the assistant answers only or also acts, such as submitting a leave request | Product owner |
| Personal data in scope, for example questions about an individual's leave balance | DPO |
| Latency and cost-per-question limits | Engineering |

## For tomorrow
If you send the HR volume and the metric choice, I can write the full PRD straight away. It would cover the autonomy level per step, failure paths, eval plan, guardrails, compliance flags, and the shadow → canary → general availability rollout.

If you have no baseline numbers by the committee, you could ask the committee to approve a **4-week shadow phase** that measures them. I can draft that one-pager now. It's a more defensible ask than a 30% promise.