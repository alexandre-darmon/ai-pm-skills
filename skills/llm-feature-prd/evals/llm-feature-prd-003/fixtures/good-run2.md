I haven't written the PRD, because the success metric you gave is a usage metric. "2,000 questions answered per month" counts activity. It doesn't show that HR's workload fell or that employees got correct answers. A PRD built on it would pass the committee on volume and leave nobody able to say whether the assistant worked. The "30% productivity" figure has the same problem: no volume, quality or unit value stands behind it, so I can't put it in a PRD as a gain.

**Problem statement (ready to reuse)**
About 3,000 employees ask HR recurring questions on leave, expenses and remote work. Policy documents hold the answers, but the HR team answers them by hand. We want an assistant, hosted in the EU and working in French, that answers these questions from the policy documents and sends the rest to HR.

**What I need from you (one line each is enough)**
1. **An outcome metric.** Three candidates, so you can pick fast:
   - Share of policy questions resolved without an HR ticket, with a correctness rate checked by HR on a sample (for example, at least 95% correct).
   - HR hours per month spent on policy questions, today versus after launch.
   - Median time for an employee to get a correct answer.
2. **The baseline.** How many policy questions HR handles per month today, and roughly how long each takes. The 30% claim needs this: volume × share the assistant resolves correctly × minutes saved per question.
3. **Data sources.** Which policy documents exist, their format, who owns them, and whether they are current and in French.
4. **Risk context.** Whether questions will include personal situations (sick leave, a specific employee's balance). This decides the data and AI Act review.

If you send even rough answers to 1 and 2, I'll write the full PRD straight away. It will cover the autonomy level per step, the failure paths, the eval plan, the guardrails, the rollout and the open questions. If it helps for tomorrow, I can also draft a one-page committee brief with the problem, the EU and French constraints, and these open items, which you can present without a PRD.