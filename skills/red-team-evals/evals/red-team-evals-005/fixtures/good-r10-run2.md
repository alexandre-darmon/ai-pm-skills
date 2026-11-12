**Short version:** the slide says more than the evidence supports. "0%" is the result on attacks the team tuned against, so it measures the tuning. It does not measure how robust the assistant is. Committee members will probably spot this, so fix it before Thursday.

## What's wrong

1. **The 200 attacks were used to build the defenses.** The team ran them after every change and iterated until none got through. Those attacks are burned, so 0/200 is a regression-test result. It says the known attacks are blocked. It doesn't say what a new attack would do. No fresh set is mentioned, so nobody can see the gap between the tuned set and a fresh one.
2. **0 out of 200 is not 0%.** With 200 independent seeds and no successes, the true rate could still be about 1.5% (rule of three). The Wilson 95% upper bound is about 1.9%. Across a year of real attack attempts, that is a lot more than zero.
3. **One pooled number hides the classes.** A pooled rate can look fine while one class fails badly. For a mortgage assistant the classes that matter are:
   - leaking another applicant's data or the system prompt
   - bypassing the policy lines (fair lending, no approval or rate commitments, no adverse-action advice)
   - indirect injection through uploaded pay stubs or documents, if uploads exist
   - multi-turn attacks
4. **The tester isn't independent.** The prompt engineer and ML engineers who built the defenses also wrote the attacks. Model risk will want rates from someone outside the build team. A builder also tends to write attacks the builder already knows how to defend.
5. **There is no success criterion, tolerance or settings.** The slide doesn't say what counts as "got through", what rate is acceptable, or which model, prompt, temperature and turn limits were used. Without a tolerance signed beforehand, "0%" has nothing to be compared against.
6. **There is no coverage or untested list.** The slide doesn't say which OWASP LLM Top 10 or NIST AI 100-2 categories were tested and which weren't.
7. **"Release requested" has no residual-risk owner.** The committee needs to see who outside the build team accepts the remaining risk, and what triggers the next campaign.

## What to put on the slide

- **A per-class table.** For each class: successful seeds ÷ held-out seeds, the rate with its Wilson 95% interval, the tolerance signed beforehand, and a reading of under tolerance, over, or undecided.
- **A wording change.** Replace the claim with something like: "0/200 on the development attack set (tuned against, version 1.4). Fresh held-out result: X/N, from tester Y (independent of the build team)."
- **Coverage.** Say how many of the relevant attack classes were tested, and list the untested ones.
- **Setup.** Give the success criteria, model and prompt versions, generation settings and dates.
- **Exposure.** Estimate how many attack attempts you see per month (from logs, not the 15,000 conversations) and multiply by the upper bound. Also say how many tries a persistent attacker needs for a first success (about 1/p).
- **Regression suite.** State that the 200 attacks, and every future success, run on every prompt, filter or model change.
- **Residual-risk record.** Name the owner outside the build team, say what triggers the next campaign, and tick off the checklist items for counsel.

## What to do before Thursday

If you can't finish a full campaign in time, there is still a lot you can do:

- **Get fresh attacks from someone independent.** Security, second line, or a domain expert such as a loan officer or fraud analyst should write them, and the build team shouldn't see them. Run them once on version 1.4 and report the gap against the 200.
- **Size each class for its tolerance.** To read a class as under 1% with no successes you need about 381 held-out seeds, and 765 for 0.5%. For the costly classes (another applicant's data, policy commitments), size for their own tolerance. If you fall short, label those classes "indicative" on the slide.
- **Change the ask if the fresh set isn't ready.** Request a conditional or staged release, with a named residual-risk owner and a date for the held-out campaign.

If you want, I can draft the revised slide and the per-class table. I'd need the attack classes you tested, the number of seeds per class, your tolerances, and a rough monthly count of attack attempts. I can also calculate the intervals once you have fresh results.