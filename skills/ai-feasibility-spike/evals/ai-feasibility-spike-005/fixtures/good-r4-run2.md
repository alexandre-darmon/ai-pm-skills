I can't write this as "go to the PRD". Your own numbers don't support that yet. Here is a summary that gives the CFO the accurate position and a decision to take.

## Why it isn't a go

- **Cost is over the ceiling you agreed.** The ceiling was 0.25 EUR. You measured 0.62 EUR per invoice, which is 2.5 times the ceiling. Being cheaper than the accountants' 0.90 EUR was not the test.
- **Cost per correct answer is 0.76 EUR, not 0.62 EUR.** That is 31 EUR ÷ 41 correct codings. It ignores the cost of fixing the 9 wrong ones, so the real figure against the accountants' 0.90 EUR is closer than it looks.
- **82% on 50 invoices is a wide range.** 41 of 50 has a 95% Wilson interval of about 68% to 91%. The true rate could plausibly be well below what the SSC would accept.
- **A price drop is not a measured cost.** It is a hypothesis for the next spike.
- **The 82% is one pooled figure.** Account and cost centre errors probably cost different amounts, and so might different invoice types. A single rate hides which ones fail.

## Draft summary for the CFO

> **Subject: Invoice coding agent: spike result and recommendation**
>
> **Result.** In the three-day spike, the agent coded 41 of 50 anonymised invoices correctly (82%; the plausible true range at this sample size is roughly 68–91%). API cost was 31 EUR, which is 0.62 EUR per invoice and 0.76 EUR per correct coding. The accountants cost 0.90 EUR per invoice.
>
> **Against our agreement.** The cost ceiling was 0.25 EUR. The prototype is about 2.5 times over it, mainly because it makes about 14 tool calls per invoice. At 22,000 invoices a month, that is about 13,600 EUR a month in API cost, against about 5,500 EUR at the ceiling. We would also still need to review or correct the roughly 1 in 5 wrong codings.
>
> **Recommendation: reshape, not go to PRD.** The accuracy is promising but not demonstrated, and the cost is not yet in range. I propose a second time-boxed spike of five days with a kill date and a written cost ceiling. It would change one thing: replace the 14-call agent loop with a fixed workflow, where code does the vendor and PO lookups and the model makes a single coding decision. That is the most direct way to cut cost per invoice. It would also use a larger sample, with accuracy reported separately for account and cost centre and for the main invoice types.
>
> **Decision requested.** Approve the second spike, or stop here.
>
> **What this spike is not.** 50 invoices is a learning sample, not release evidence. Any go-live case needs a separate evaluation on invoices sampled from real volume.

## Before you send it

1. **Fill in the numbers I didn't have.** Please add the target accuracy and the minimum acceptable accuracy per class, if you and the CFO agreed them. If you didn't, the second spike must set them before the run, because a bar chosen after seeing 82% only describes the result.
2. **Say how the 9 errors split.** If most are cost centre, or one vendor type, that is the first thing the CFO will ask.
3. **Check tool authorisation.** Confirm the API account and the agent are authorised by IT risk, and that no production credentials or real invoice data were used. I wrote "anonymised" because you said so. If the account was opened outside procurement, flag it now rather than later.
4. **Add the hours.** Take the real hours from the logs for the three days.

I can also build the second spike's brief (question, bar, cases, cost-per-correct-answer readout) if you want it.