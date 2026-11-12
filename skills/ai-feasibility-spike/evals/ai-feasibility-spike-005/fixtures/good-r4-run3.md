I can't write "we go to the PRD". By the rules you and the CFO set, this spike reads as **reshape**. Here is why, followed by a summary you can send.

**Why it isn't a go**
- **Cost misses the ceiling.** The ceiling was 0.25 EUR, and cost per correct answer is 31 EUR ÷ 41 = **0.76 EUR**, about 3× over. Even per invoice, 0.62 EUR is 2.5× over. Beating the accountants' 0.90 EUR was not the test you agreed on.
- **The 0.90 comparison is also too generous to the agent.** 9 of 50 answers (18%) are wrong and someone has to catch and fix them. If an accountant reworks each one at 0.90 EUR, the real cost is about 0.62 + 0.18 × 0.90 ≈ **0.78 EUR per invoice**. That is only slightly cheaper than 0.90 EUR, and it assumes the errors get caught.
- **Price drops are a hypothesis, not a result.** Future model pricing can't be counted as measured cost.
- **Accuracy is not demonstrated.** 41/50 is 82%, but with 50 cases the 95% interval is about 68–91%. That interval is wide, and I can't judge it against a bar because I don't know whether you wrote one down before the run. If you didn't, the 82% describes the result and doesn't pass or fail anything. A single pooled rate also hides the classes. Wrong cost centres and wrong GL accounts probably have different consequences.

**Draft summary for the CFO**

> **Subject: Invoice coding agent: result of the 5-day spike and recommendation**
>
> **Question.** Can an AI agent propose the GL account and cost centre for supplier invoices at under 0.25 EUR per correct answer?
>
> **Result (50 anonymised invoices).** The agent coded 41 correctly (82%; the plausible range on a sample this size is about 68–91%). The API cost was 31 EUR, which is 0.62 EUR per invoice and **0.76 EUR per correct invoice**. The agent makes about 14 tool calls per invoice.
>
> **Against our ceiling.** The cost is about 3× above the 0.25 EUR ceiling we agreed. It is below the accountants' 0.90 EUR per invoice, but that is not the agreed test. The 18% of wrong answers would still need human correction, so the net saving is small.
>
> **Recommendation: reshape, not PRD yet.** The prototype shows the model can do the task, but at this cost the business case doesn't hold. I propose a second time-boxed spike that changes one thing: replace the agent loop with a fixed workflow. Code does the vendor-master and PO lookups, and the model makes a single judgment call. That should cut tool calls and tokens sharply. We would not count on future price cuts.
>
> **Second spike.** The time box is [X] days and the kill date is [date]. The cost ceiling stays at 0.25 EUR per correct answer. Accuracy bars per class (GL account, cost centre) and a stop line are written down before the run. The sample is sized for those bars (about 25–35 cases per class as a minimum, more for the costly class). Cases remain anonymised.
>
> **Decision rule.** If the cost is within the ceiling and no class the product can't drop falls under its stop line, we go to the PRD. If not, we stop. Neither outcome needs a further extension.
>
> **Not claimed.** These numbers are spike results. They are not evidence of production accuracy, which will need a proper evaluation on real invoice traffic before any release.

**Before you send it, please check:**
1. Did you write accuracy bars or a stop line before the run? If not, the second spike must set them, signed by the CFO.
2. Were the 50 invoices spread across GL accounts and cost centres, and what is the error split? I'd add a per-class table.
3. Take hours and spend from the logs, not from memory.
4. Was the model account and tool authorised through IT risk and procurement, and does the agent only propose codes without writing to the ledger? That decides whether the safety check on private data, untrusted invoice text and an outbound channel is clear.
5. Is the model and hosting route the one production would use? If not, the cost doesn't transfer.

If you give me the per-class results and the dates, I can fill in the placeholders and add the table.