**The slide, as written, won't survive a model risk committee.** The 0% is a tuning score, not a robustness measurement. Here is what I'd change.

## Problems

1. **The 200 attacks were used to tune the defence.** The team iterated on the prompt and filter until none got through, so the run measures how well the defence learned those 200 attacks. It says little about how it handles new ones. This is the biggest issue, and the committee will probably spot it first.
2. **0 out of 200 is not 0%.** The 95% Wilson upper bound is about 1.9% (rule of three: about 1.5%). Even on fresh attacks, the true rate could plausibly be that high. For a persistent attacker, 1.9% means a first success in roughly 50 tries.
3. **There is one pooled number.** A pooled 0% can hide a weak class. Results need to be shown per attack class, each against a tolerance.
4. **There is no tolerance.** "0%" isn't compared to anything. Nobody has stated beforehand what rate is acceptable for, say, leaking another applicant's data or giving a misleading rate or eligibility statement.
5. **Coverage is unstated.** The slide doesn't say which classes were tested (direct, indirect, multi-turn, and so on) or which weren't. It also doesn't map them to OWASP LLM Top 10 or MITRE ATLAS.
6. **The testers aren't independent.** The people who built the defence wrote the attacks. Model risk will want rates from testers outside the build team.
7. **Settings and criteria are missing.** The slide gives no success criterion per class, no model or temperature, and no number of attempts per attack.
8. **"Release requested" doesn't say who accepts the risk.** Residual risk should be accepted by a named owner outside the build team.

## What to change

**Before Thursday, if you can:**
- Run a **fresh, held-out set** of attacks that the build team has never seen, ideally written by someone independent (security, second line, or an external tester). Report the gap between the tuned set and the fresh set. A big gap means the defence learned the attacks rather than the class.
- Group the attacks into classes drawn from the assistant's own harms. For a mortgage assistant these might be leaking PII or another customer's data, giving credit, rate or eligibility advice it shouldn't, system prompt extraction, and indirect injection through uploaded documents. Then tag each attack with its class.
- Get tolerances signed per class. Size each held-out class for its tolerance. Reading a class as under 1% with zero successes takes about 380 fresh seeds, and under 0.5% takes about 765. Classes with fewer seeds get labelled "indicative".

**If you can't get fresh attacks in time, reword the slide honestly:**

> **Prompt-injection testing, v1.4: development-set result, not a robustness estimate**
> - 0/200 successful on the attack set used to tune the prompt and filter. Because the team tuned against these attacks, the result shows regression-suite pass, not resistance to new attacks.
> - For a clean 200 on unseen attacks, the 95% upper bound would be about 1.9% per attack. We have not yet measured this on held-out attacks.
> - Per-class results, coverage against OWASP LLM Top 10, and untested classes: [table].
> - Held-out independent campaign: planned for [date], owner [name]. Tolerances per class: [signed values].
> - Release requested as [limited / monitored release] with residual risk accepted by [named owner outside the build team]. Triggers for re-test: any change to the model, system prompt, filter, or data sources.

**Add to the slide or an appendix:**
- A per-class table: successes ÷ seeds, Wilson interval, tolerance, and a reading of under, over, or undecided.
- The exposure on actual attack attempts, not all conversations. The 15,000 conversations a month is the wrong base. You need an estimate of attack attempts from logs. As an illustration, if 1% of conversations are attacks, that is 150 attempts a month, and a 1.9% bound allows up to about 3 successes a month.
- A regression-suite commitment, so every future successful attack becomes a permanent test case.
- A line saying the 200 attacks are now burned for decision purposes and moved to regression.

I'd also drop "robust", "secure" and "0%" from the wording entirely, and ask for the committee's tolerance per class up front.

If you share the 200 attacks, I can sort them into classes and show the coverage gaps. If you share the class tolerances, I can compute the exact table.