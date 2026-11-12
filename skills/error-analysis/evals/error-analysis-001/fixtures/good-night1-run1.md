**No, not as a primary measure. A 1–5 judge on helpfulness, accuracy and tone, averaged weekly, would be a poor way to measure quality here.** Before rollout, read the pilot conversations and let what you find decide the metrics.

## Why the plan doesn't fit

- **The scores are chosen before anyone has read the failures.** A weekly average of 3.8 doesn't tell you whether the deductible logic or the exclusion retrieval needs fixing. Averages also hide rare, expensive errors. A wrong deductible is one conversation in a hundred, and a mean barely moves for it.
- **The costs are very different, and the scores ignore that.** Using your figures:
  - A wrong answer the handler catches costs 10 min × 54 EUR/h = **9 EUR**.
  - A wrong deductible or missed exclusion that reaches a claimant costs **150 EUR**, about 17 times more.
  - At 9,000 conversations a month, each 1 percentage point of answers that are wrong and *escape* costs about 90 × 150 = **13,500 EUR/month**. The same point of errors the handler catches costs about 810 EUR/month.
  - So the metric that matters is wrong answers that go unnoticed. A helpfulness or tone score doesn't capture that.
- **The judge is unvalidated.** No one has checked that it agrees with a claims expert. It can't know the correct deductible unless it sees the policy and claim data. LLM judges also tend to reward fluent, confident text, which is the kind of wrong answer that gets past a handler.
- **Thumbs and escalations are biased.** A thumbs-down only shows errors the handler noticed, and those are the cheap ones. A handler who trusts a wrong answer gives a thumbs-up. The pilot handlers were also 40 volunteers, who may not resemble 350 handlers.
- **Personal data.** The logs contain claimant names, policy numbers and injury details, which are health data under GDPR. Mask them before anyone reads the logs and before any are sent to a judge model.

## What to do before rollout

1. **Mask the 1,200 conversations.** Keep the raw text only in its source system.
2. **Sample about 100 conversations in two streams.**
   - Draw a random sample, proportional to question class (coverage, deductible, documents, next steps; motor vs. home). Only this sample can tell you how often each failure occurs.
   - Draw a targeted sample: thumbs-downs, escalations, and extra conversations on deductibles and exclusions. This finds failure types but says nothing about their frequency.
3. **Have one accountable claims expert read each conversation in full.**
   - The claims quality lead or a senior handler should do this, not the build team.
   - They write a free-text note on what went wrong, or "pass". An example is "quoted the base deductible and ignored the glass-cover endorsement".
   - When a wrong retrieval leads to a wrong answer, record the retrieval as the failure.
   - Don't let an LLM do the first read. Keep reading until about 20 conversations in a row show nothing new.
4. **Group the notes into failure modes.**
   - Each mode gets a yes/no definition plus one passing and one failing example.
   - An LLM can help propose groupings here, and the expert approves them.
5. **Count and price each mode.**
   - Share = occurrences in the random sample ÷ size of the random sample, with a confidence interval.
   - Expected monthly cost = 9,000 × share × cost per occurrence.
   - Split each mode into "caught by the handler" (9 EUR) and "reached the claimant" (150 EUR).
   - Source the 150 EUR figure properly with the quality lead. It's currently an estimate.
   - Don't put a euro figure on legal or regulatory exposure, such as a wrongly denied claim. Raise it with compliance or counsel as a question.
6. **Decide what to do about each mode.**
   - **Specification failures**, where the prompt, the retrieved clauses or the claim data never gave the model what it needed (for example a missing endorsement or an outdated wording in the knowledge base): fix them now and keep the failing conversations as regression tests. Don't build an evaluator for them.
   - **Cases where the inputs were right and the model still erred:** use the cheapest check that works.
     - **Code checks first.** Compare any quoted deductible or amount against the policy system, and check that required documents are listed.
     - **A yes/no LLM judge** only for things code can't decide, such as a missed exclusion or an unsupported claim. Build one judge per failure mode, not one overall judge.
     - **Validate every judge** against the expert's labels before you trust it.
   - **Low-cost modes with no legal or privacy effect:** accept them, with a written reason, an owner and a re-check date.
7. **Monitor what matters after launch.**
   - Track the rate of each costly failure mode, from code checks and validated judges.
   - Sample a few dozen conversations each week for expert review. This is the only way to catch errors the handler didn't.
   - Keep tone as a minor check, if at all.
   - Re-run this analysis after any change to the model, prompt or policy wordings, and after any complaint spike.

## Open questions

- Who is the accountable expert, and do they have the time to read about 100 conversations?
- Where does the 150 EUR figure come from?
- Does the system have an authoritative source for deductibles and endorsements that code checks can call?
- Does the planned rollout have handlers validate every answer, or will some answers go to claimants unchecked? That decides how much weight the 150 EUR cost carries.

I can set up the failure-mode log and cost template next. I'd need the masked conversations and the expert's notes to fill it in.