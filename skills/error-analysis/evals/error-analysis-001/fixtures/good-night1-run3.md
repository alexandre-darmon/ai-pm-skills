**No, I wouldn't roll out with that.** The weekly average of a 1–5 judge score on helpfulness, accuracy and tone tells you little about what you care about, and it hasn't been checked against anything. I haven't seen your logs yet, so the plan below is what I'd do with them.

## Problems with the current plan

1. **The metrics were picked before anyone read the outputs.** An average of 3.8 doesn't tell you whether the problem is a stale deductible table, a missed exclusion or bad retrieval. The failure modes should decide the metrics, not a generic template.
2. **A 1–5 scale hides the costly errors.** A wrong deductible stated in a friendly, helpful tone can score 4 on two of three dimensions. Scoring each failure as pass/fail would catch it.
3. **The judge hasn't been validated.** You don't know whether it agrees with your claims quality lead on what a wrong answer is. Until it does, the weekly trend could be noise or bias, for example favouring longer answers.
4. **Thumbs-up isn't evidence of accuracy.** The expensive error is the one the handler *doesn't* catch and that reaches the claimant. A handler can thumbs-up a wrong deductible. Thumbs-down and escalation are useful for finding failures, but they undercount the worst ones.
5. **Cost is asymmetric.** A caught error costs about 10 min × 54 EUR/h = **9 EUR**. One that reaches a claimant costs **150 EUR**, roughly 17 times as much. So what matters is the share of wrong answers that get past the handler, not just how many answers are wrong. For example, at 9,000 conversations a month, 5% wrong is 450 errors. If 10% of those slip through, that's about 45 × 150 + 405 × 9 ≈ 10,400 EUR a month. If 2% slip through, it's about 5,000 EUR. That is only an illustration, because you haven't measured either rate yet.
6. **Privacy.** Your logs contain claimant names, policy numbers and injury details. Injury details are health data under GDPR Art. 9. Mask the logs before anyone reads them or sends them to a judge model. Ask counsel whether sending unmasked text to an external LLM is allowed at all.

## What to do before rollout

1. **Mask the 1,200 conversations.** Strip names and policy numbers, and generalise the injury details. Keep the raw text in its source system.
2. **Draw two samples, about 100 conversations in total.**
   - **Random sample (~60), stratified by motor vs. home and by question type.** This is the only sample that tells you how often each failure happens.
   - **Targeted sample (~40):** thumbs-down, escalations, and questions about exclusions and deductibles. This finds failure types but says nothing about their rate.
3. **Have your claims quality lead (or a senior handler) read each one, not an LLM.** For each conversation they write a free-text note on what went wrong, or "pass". They should check the answer against the clause that was retrieved *and* the policy wording. Record the first upstream failure. A wrong retrieval followed by a wrong answer counts as one retrieval failure. Keep reading until about 20 conversations in a row show nothing new.
4. **Group the notes into failure modes.** Each mode needs a binary definition and one pass and one fail example. Likely candidates are wrong deductible or limit, missed exclusion, outdated or wrong policy version, wrong or missing required documents, and wrong next step. Let the data confirm or replace these.
5. **Count and price each mode.** Use the random sample only, with a confidence interval. For example, 6 of 60 is 10%, with an interval of roughly 5–20%. Then compute volume × share × cost per occurrence. For the cost of an error that reaches a claimant, use 150 EUR. Also record how often a handler actually catches each mode, which you can estimate from the handler's own behaviour, such as follow-up questions or escalations.
6. **Decide per mode whether to fix, evaluate or accept.**
   - **Fix first** if the cause is in the spec, such as a missing instruction, a stale policy in the knowledge base or poor retrieval. Re-run the failing conversations afterwards and keep them as regression tests.
   - **Evaluate** if the model fails despite having what it needs. Use code checks where you can, for example comparing the quoted deductible with the policy system. Use an LLM judge only for what code can't decide, one binary judge per mode.
   - **Accept** cheap, low-impact modes with a written reason, an owner and a re-check date.
7. **Validate every judge you keep** against the expert's labels, mode by mode. Check how often they agree, and especially how many real errors the judge misses. Don't put a judge into monitoring until it passes.
8. **Set rollout gates and monitoring from this.** Examples: the rate of deductible and exclusion errors stays below an agreed threshold, and a small random sample of production answers is expert-reviewed every week, which is about 50 a week at 9,000 a month. Add automatic checks on the numbers, and keep thumbs-down and escalation as triggers for review. Re-run the analysis after any change to the model, prompt or policy knowledge base, and after the first month at 350 handlers. That is a different population from the 40 pilot handlers.

## Open questions

- Who owns the quality decision? That should be the claims quality lead, not the build team.
- How often do handlers catch a wrong answer today? Nobody has measured this, and it drives most of the cost.
- Is the 150 EUR figure an average across error types? A missed injury exclusion may cost far more than a wrong deductible. Legal and financial exposure should go to counsel as a question, not be folded into an average.

If you share the masked logs, I can help build the sampling plan and, once the expert has read the sample, count and price the failure modes.