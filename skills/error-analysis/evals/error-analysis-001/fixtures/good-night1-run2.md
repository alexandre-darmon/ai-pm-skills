No, I wouldn't rely on this as the main way to measure quality. A weekly average of 1–5 scores for helpfulness, accuracy and tone can't tell you which failures to fix, and it is weakest on the failures that cost you the most.

## Why the proposed scheme falls short

- **The scores were chosen before anyone read the outputs.** An average of 3.8 on accuracy doesn't say whether the problem is stale deductible tables, missed exclusions or wrong retrieval. The measures should come from the failures you actually observe.
- **The costs are very uneven, and an average hides that.** A wrong answer the handler catches costs about 9 EUR (10 minutes × 54 EUR/h). A wrong deductible or missed exclusion that reaches a claimant costs about 150 EUR, roughly 17 times more. A judge that scores "accuracy" as 4 versus 5 doesn't separate these. A fluent, confident wrong deductible will probably score well on helpfulness and tone.
- **The judge hasn't been checked against anyone.** Nobody has shown that its scores agree with what your claims quality lead would say. A 1–5 scale also tends to bunch around 4, so the weekly trend will move very little.
- **Thumbs-down is a biased signal.** The costly errors are the ones the handler didn't notice, and those get a thumbs-up. Use thumbs and escalations to find failures to read. Don't use them to estimate how often failures happen.
- **Privacy.** Sending conversations with claimant names, policy numbers and injury details to a judge model needs masking first, or a data-processing basis. Check this with your DPO.

## What to do before rollout

1. **Mask the 1,200 conversations.** Remove names, policy numbers and injury details before anyone reads them or any model sees them. Keep the raw text in the source system.
2. **Draw about 100 conversations in two groups.**
   - A random sample, ideally proportional to the motor/home mix and the question types. This is the only group that tells you how often each failure occurs.
   - A targeted sample: thumbs-down, escalations, long conversations, and extra cases on exclusions and deductibles. This finds failure types but says nothing about their frequency.
3. **Have your claims quality lead (or a senior handler they nominate) read each one and write a free-text note** on what went wrong, or "pass".
   - Notes should be specific, for example "quoted the wrong deductible for a home policy with an add-on".
   - Note the first upstream failure. A wrong clause retrieved followed by a wrong answer counts as one retrieval failure.
   - An LLM shouldn't do this first reading. It can group the expert's notes afterwards.
4. **Keep reading until about 20 consecutive conversations show no new kind of failure.** This usually takes 50–100. Until then, call the failure list provisional.
5. **Group the notes into failure modes.** Each mode gets a pass/fail definition with one pass and one fail example. Typical candidates are wrong deductible, missed exclusion, outdated wording, wrong or missing required document, and answering when the claim file lacks the facts. Your own reading will decide the actual list.
6. **Count each mode in the random sample, with a confidence interval, and price it.** The expected monthly cost is 9,000 × share × cost per occurrence. For example, if 1% of answers are wrong, that is 90 a month. If 20% of those reach a claimant, that is about 72 × 9 + 18 × 150 ≈ 3,350 EUR a month. The 1% and the 20% are placeholders. The reading gives you the real shares, and the real share that reaches a claimant needs the quality lead's data. The 150 EUR figure needs a source, such as complaint-handling records.

   A mode with regulatory or privacy effects should go to compliance as a question. Don't just put a euro figure on it.
7. **Decide what to do with each mode.**
   - If the prompt, the retrieval or the knowledge base never gave the model what it needed (for example an outdated wording), fix it now. Don't build a judge for it.
   - If the model has the information and still gets it wrong sometimes, build a check. Prefer code checks, such as comparing the quoted deductible with the policy system or confirming a required document list is present. Use an LLM judge only where code can't decide. Each judge should be one pass/fail question per failure mode.
   - Accept low-cost modes in writing, with an owner and a re-check date.
8. **Validate every judge against the expert's labels before using it,** using enough labelled cases per mode. Report agreement per mode, not overall. If you can't validate a judge, don't use it to gate anything.

## What to monitor after rollout

- A weekly random sample of masked conversations, reviewed by a handler or the quality lead, with the failure rate per mode and its interval.
- Automated checks on every conversation for the modes you can check in code. Use calibrated judges for the rest.
- A guard for the 150 EUR failures specifically. For example, flag any answer that states a deductible or exclusion that doesn't match the retrieved clause, and send it for review.
- Thumbs and escalation rates as signals for which conversations to read, not as quality scores.
- A fresh round of error analysis after any change to the model, prompt or policy wordings, and again once the first month of production traces is in.

The pilot ran with 40 handlers over six weeks, so the mix of questions across 350 handlers may differ. Check the reading against the production mix once rollout starts.

If you can share a masked export, I can help set up the reading log and compute the counts, shares and monthly cost per failure mode. The conversations aren't in this working directory, so I haven't looked at any of them.