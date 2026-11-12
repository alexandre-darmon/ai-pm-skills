# Short answer

Not as the primary measure. A weekly mean of 1-5 judge scores is a fine dashboard line, but it doesn't measure the risk that costs you money. The judge also hasn't been checked against anyone who knows claims.

## Why the current plan falls short

**1. The cost is in the tail, and averages hide the tail.**
- A handler-caught error costs about 10 min × 54 EUR/h = **9 EUR**.
- An error that reaches a claimant costs about **150 EUR**, roughly 17 times more.
- Illustration with made-up rates: at 9,000 conversations a month, a 5% wrong-answer rate and handlers catching 80%, you get 360 caught errors (about 3,200 EUR) and 90 uncaught ones (about 13,500 EUR).
- The uncaught errors are about 80% of the cost, but they are a 1% event. A weekly average moving from 4.3 to 4.2 won't show them. Treat all of these rates as placeholders until you measure them.

**2. The errors that matter are the ones nobody sees.** A wrong deductible or a missed exclusion looks plausible, so the handler gives it a thumbs-up. That means the pilot's thumbs-up and escalation data is biased against the costly failures. A judge that sees only the question, the retrieved clauses and the answer also can't spot a missed exclusion, because the missing clause was never retrieved.

**3. A 1-5 helpfulness/accuracy/tone score is the wrong target.**
- Helpfulness and tone are fluent-sounding qualities that LLM judges rate generously.
- Accuracy here is binary and specific: did the answer state the right figure and the right exclusion?
- Judges tend to compress scores around 4, favour long answers, and favour output from their own model family.

**4. The judge is unvalidated.** Until you know how often it flags a wrong answer that experts also call wrong, and how often it passes one, its scores don't mean anything.

## What to do before Q1

1. **Build an expert-labelled gold set from the 1,200 logs.**
   - Have claims specialists label each answer as correct or incorrect, with the error type (wrong amount, missed exclusion, wrong document list, wrong next step) and severity.
   - Label all thumbs-down and escalated conversations.
   - Label a random sample of at least 300-400 thumbs-up conversations, stratified by motor/home and question type.
   - The thumbs-up sample gives you the **uncaught error rate**, which is the number that drives cost.

2. **Estimate the handler catch rate.** Compare handler feedback to the expert labels. Report it with confidence intervals. With few errors, the intervals will be wide, and you should say so.

3. **Replace the 1-5 scores with targeted checks.**
   - Use deterministic checks where you can, for example comparing the stated deductible or amount to the policy data.
   - Use binary judge questions for the rest: "Does the answer state the deductible, and does it match clause X?" and "Is there an exclusion in the full wording that applies and isn't mentioned?"
   - Give the judge the full policy wording and the claim file, not only the retrieved clauses.
   - Use a different model family from the assistant.
   - Keep tone as a minor secondary metric.

4. **Validate the judge on the gold set.** Report its recall on real errors, especially high-severity ones, and its precision, with intervals. Set a minimum recall as a launch criterion. If recall on costly errors is low, use the judge only to prioritise human review and not as a measurement.

5. **Measure retrieval separately.** Check whether the right clauses, including exclusions, were retrieved. Most missed-exclusion errors will start there.

6. **Design the ongoing monitoring around cost.**
   - Track severity-weighted error rate and counts of high-severity errors, not means.
   - Add a weekly stratified expert audit of about 100-150 answers, with the judge flagging the riskiest ones.
   - Alert on error counts or rates with confidence intervals.
   - Add reason codes to the handler feedback.
   - Use the 9 EUR and 150 EUR figures to decide how much review effort is worth paying for.

7. **Don't assume the pilot transfers to 350 handlers.**
   - The 40 pilot handlers may have been experienced or enthusiastic, and less experienced handlers may catch fewer errors.
   - Roll out in waves.
   - Consider product changes for high-risk question types, such as showing the source clause next to deductible and exclusion answers.
   - Re-test whenever the policy wordings change.

8. **Sort out data protection before anyone labels or judges the logs.** They contain claimant names, policy numbers and injury details, which is health data under GDPR. Pseudonymise them before they go to an external judge model or outside labellers. Confirm the data processing agreement, retention and access controls with your DPO.

If you want, I can draft the sampling plan with sample sizes, or a labelling guide for the claims experts.