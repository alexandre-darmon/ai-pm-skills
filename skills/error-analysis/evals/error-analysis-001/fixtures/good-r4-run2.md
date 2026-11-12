**No, the 1-5 judge averages aren't the right way to measure quality.** I'd change the approach before rollout.

## Why the current plan falls short

- **Generic scores don't match your costs.** A weekly "accuracy 4.1" can't distinguish a wrong deductible (150 EUR if it reaches a claimant) from a slightly clumsy sentence. It also doesn't tell anyone what to fix. A judge scoring helpfulness, accuracy and tone measures what a template expects, not what this assistant gets wrong.
- **The two costs differ a lot.** A caught error costs 10 min × 54 EUR/h = **9 EUR**. An uncaught one costs **150 EUR**, about 17 times more. Nearly all the money is in the errors handlers miss.
- **Thumbs are blind to the costly errors.** A handler who doesn't notice a missed exclusion gives a thumbs up. Thumbs-down and escalation mostly capture errors that get caught, which are the cheap ones.
- **Illustrative exposure.** At 9,000 conversations a month, each 1% of wrong answers is 90 answers. If 20% of those slip through, that is 18 × 150 + 72 × 9 ≈ **3,350 EUR a month**. The 1% and the 20% are placeholders, not measurements, and the handler catch rate is the most important number you don't have yet.
- **Data protection.** Sending every answer to a judge means claimant names, policy numbers and injury details go to a model. That needs masking first. Injury details are health data, so involve your DPO.

## What to do before rollout

1. **Mask the 1,200 logs.** Do this before anyone reads them or any model sees them.
2. **Sample about 100 conversations in two streams.**
   - A random draw, weighted by motor and home volume. Only this gives failure rates.
   - A targeted draw of thumbs-downs, escalations, and conversations on exclusions, injury and other rare, high-impact question types. This finds failure modes but says nothing about how often they occur.
3. **Have your claims quality lead or a senior handler read each one.** They write a free-text note on what went wrong, or "pass", and keep reading until about 20 consecutive conversations show nothing new. Don't let an LLM do the first pass. Note the first upstream failure. For example, a wrong clause retrieved that then produces a wrong answer is one retrieval failure, not two.
4. **Group the notes into binary failure modes.** Each mode is pass or fail, with a written definition and an example of each. My guesses for what you'll find, to check while reading and not to adopt as metrics:
   - wrong deductible
   - missed exclusion
   - outdated policy version
   - missing required document
   - unsupported next step
5. **Count and price each mode.** Use the share from the random stream with its confidence interval, then multiply by 9,000 × cost per occurrence. Rank by expected monthly cost. A mode with legal or regulatory exposure, such as a wrong coverage statement to a claimant, goes to counsel as a question and not into a euro figure.
6. **Decide for each mode whether to fix, evaluate or accept.**
   - *Spec or knowledge-base gaps*, such as a missing or outdated policy wording or no instruction to cite the exclusion: fix them now and keep the failing conversations as regression cases.
   - *Failures where the model had what it needed*: use code checks first, for example comparing the quoted deductible to the policy system of record or checking that the exclusion clause was retrieved. Use a binary LLM judge only where code can't decide.
   - *Any judge*: validate it against the expert's labels and report true-positive and true-negative rates. Raw agreement hides a judge that passes everything.
7. **Measure the handler catch rate.** Of the wrong answers, what share do handlers fix before it reaches the claimant? Check it in the random sample against the claim file outcomes. It is the biggest driver of cost and the most likely thing to change at 350 handlers. Your 40 pilot handlers may not be representative of the full group.

## Monitoring after rollout

- Track weekly **failure rates per mode and per claim type, with intervals**, instead of averages. Report high-severity modes separately and alert on any occurrence.
- Run the calibrated judges and code checks on all traffic. Add a weekly expert review of a random slice (for example 50-60 conversations) to catch drift and new modes. A sample that small only resolves rates to within about ±10 points, so don't read small week-to-week moves as trends.
- Re-run the error analysis after any change to the model, prompt or policy knowledge base, and after any complaint spike.
- Consider a staged rollout, with thresholds on the high-cost modes before each expansion.

## What I need from you

- Who is the accountable domain expert, and how much of their time do you have?
- Can you provide the masked logs (or the masking rules), and do you have any data on complaints or rework traced to assistant answers?
- Do handlers have to confirm or edit every answer, or can they pass it on as is?

Once I have the masked logs and the expert's notes, I can build the counted and priced failure-mode report.