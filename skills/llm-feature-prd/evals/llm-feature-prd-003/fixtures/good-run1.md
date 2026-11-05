I haven't written the PRD, because it has no outcome metric yet. "2,000 questions answered per month" measures usage, not outcome. The skill I'm following for this PRD says to stop here even when you ask me to skip questions or add metrics later. A PRD built around a placeholder would also be weak in front of the committee: the eval thresholds, the rollout gates and the ROI all hang on that metric. What I can give you now is the problem statement and a list of what's missing.

**Problem statement (draft)**
About 3,000 employees ask HR repeat questions on leave, expenses and remote work. Answering them takes HR time. We want an assistant that answers in French from the internal policy documents, hosted in the EU, and takes that load off the HR team.

**Outcome metric: what I need from you**
Pick one or two of these, each with a baseline and a target:
- **Deflection:** the share of policy questions resolved without an HR ticket or email. For example, from X% today to Y%.
- **HR time:** hours per month HR spends on policy questions, today versus target.
- **Answer quality:** the share of answers that are correct and cited, as rated by HR on a sample. This sits beside any usage number.
- **Time to answer:** the median wait for an employee, today versus target.

The 2,000 questions per month can stay as a usage KPI, but only next to one of these.

**Other gaps**
1. **The 30% productivity claim.** It needs volume × quality × unit value behind it. That means how many HR questions arrive per month, how many HR minutes each takes, and what share the assistant can safely handle. Without those, I would have to remove the figure from the PRD. *Owner: HR operations.*
2. **Policy documents.** I need the list, format, owner, last-updated dates, and whether any of them are out of date or contradict each other. *Owner: HR.*
3. **Risk context.**
   - Will employees ask questions that include personal data, such as their own leave balance or a case?
   - Is it policy answers only, or does it also look up individual records?
   - Is a works council or CSE consultation required in France?
   - Does the AI Act classification apply? *Owner: DPO/legal.*
4. **Hosting and model.** I need to know which EU provider or cloud is approved, the latency expectation, and the cost ceiling per question. *Owner: IT.*
5. **Escalation.** Where does a question go when the assistant can't answer, and who staffs that? *Owner: HR.*

**For tomorrow**
Reply with a metric, a baseline and a target, even rough ones. If the baseline is unknown, I'll write the PRD with a measurement task for the pilot phase. The PRD will then cover autonomy levels per step, failure paths, the eval plan, guardrails, compliance flags, the rollout gates (shadow, then canary, then general availability) and open questions with owners.