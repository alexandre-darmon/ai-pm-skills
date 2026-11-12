**No, a 1–5 judge on helpfulness, accuracy and tone is not the right way to measure quality, at least not as the first or only measure.** Do error analysis first and build the monitoring from its results.

## Why the current plan falls short

- **The scores come from a template, not from your failures.** An average of 3.9 doesn't tell you whether the assistant quotes a deductible from the wrong policy year or misses a flood exclusion. Those are the errors that cost money, and a fluent, polite answer with the wrong deductible can still score 4–5 on helpfulness and tone.
- **Nobody has checked the judge against your experts.** An uncalibrated LLM judge tends to pass nearly everything. A flat weekly average could mean stable quality or a judge that can't see the errors.
- **The costs are very uneven.** A wrong answer the handler catches costs about 9 EUR (10 min × 54 EUR/h). One that reaches a claimant costs about 150 EUR, roughly 17 times more. Equal-weight averages hide this. What matters is how often each failure type occurs and whether it gets caught.
- **Averaged scores are noisy.** At 9,000 conversations a month, a small weekly change in the average can't be told apart from noise.

## What to do before rollout

1. **Mask the personal data first.** Claimant names, policy numbers and injury details should be masked before anyone reads a conversation or sends one to a model. Injury details are health data, so ask your DPO or counsel about this, and about the judge's data flows in production.
2. **Draw two samples from the 1,200 conversations, about 100 in total.**
   - A random sample, split by motor and home and by question type. This is the only sample that tells you how often a failure happens.
   - A targeted sample: thumbs-down, escalations, and rare question types with big financial consequences. This finds failure types but says nothing about their rate.
3. **Have one senior claims expert read each conversation and write a free-text note.** The note should be specific, for example "used the 2024 deductible table on a 2026 policy", and not just "inaccurate". Don't let an LLM do the first read. Where a conversation has several errors, note the first upstream one. A wrong retrieved clause that leads to a wrong answer counts as one retrieval failure. Keep reading until about 20 conversations in a row show nothing new. Until then, call your list of failure types provisional.
4. **Group the notes into failure types, each defined as pass or fail.** An LLM can suggest groupings once the expert's notes exist, and the expert accepts or rewrites them. Likely candidates are a wrong deductible or limit, a missed exclusion, an outdated or wrong-product clause, a missing required document, a wrong next step, and an answer that ignores the claim file. Treat these as guesses until you've read the conversations.
5. **Count and price each failure type.**
   - Take the share from the random sample only, with a confidence interval. For example, 6 of 60 is 10%, with an interval of about 5–20%. A type never seen in 60 random conversations can still affect up to about 5% of traffic.
   - Expected monthly cost = 9,000 × share × cost per occurrence. For cost per occurrence, use the 9 EUR catch cost, and add the 150 EUR for the fraction that reaches a claimant. That fraction is unknown. Your thumbs-up/down and escalation data show what handlers catch, but not what they miss. Have the quality lead or a second reviewer re-check a sample of answers the handler accepted without escalating.
   - Rank failure types by expected cost. Anything with legal, privacy or injury implications goes to counsel as a question, not into a euro figure.
6. **Decide what to do with each failure type: fix, evaluate or accept.**
   - If the KB, prompt or inputs never gave the model what it needed (a policy version missing from the KB, no instruction to check the policy year), fix that directly. Keep the failing conversations as regression cases.
   - If the model had the information and still got it wrong, add an automated check. Use code where possible, for example comparing the quoted deductible against the policy system of record, or checking that the cited clause exists and matches the product and year. Use an LLM judge only where code can't decide, such as an unsupported claim. Use one pass/fail judge per failure type, not one overall score.
   - Accept low-cost types with a written reason, an owner and a re-check date.
7. **Validate every judge before trusting it.** Compare it with the expert's labels and report true-positive and true-negative rates, not raw agreement. Check this on conversations the judge hasn't seen.
8. **Design the monitoring around the failure types.**
   - Track the rate of each failure type, the share of conversations flagged by the code checks, and escalations and thumbs-down by question type.
   - Have an expert read a fresh random sample every week, say 50 conversations. This keeps the judge honest and catches new failure types.
   - Re-run the error analysis after any change to the model, prompt or KB, and after any complaint spike.
9. **Plan for the rollout itself.** Going from 40 to 350 handlers brings less experienced users, and handler catch rates may differ from the pilot. Consider a staged rollout, and don't assume the pilot's catch rate holds.

## Caveats

- The pilot thumbs-up rate is a weak signal. Handlers who accept a plausible but wrong answer will give it a thumbs-up, and those are the errors that reach claimants.
- The cost figures are only as good as the 150 EUR estimate and the 10-minute catch time. Ask the quality lead where those numbers come from, so the ranking in step 5 holds up.
- I haven't seen the conversations, so the failure types and shares above are hypotheses, not findings.

If you export the logs with the personal data masked, I can help set up the sampling and the reading log. I can also help compute the counts and costs once the expert has labelled the sample.