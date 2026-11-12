**Change the slide: 0 of 200 is a measure of fit, not of robustness.** The prompt and filter were iterated until those 200 failed, so the 0% holds by construction. Model risk needs a rate on attacks the defence has never seen.

What to show instead:
1. **A sealed held-out set.** Fresh attacks written by testers independent of the build team (the security team or second line), sealed and hashed before they see version 1.4, never shown to the prompt engineer.
2. **Size it for the bar.** Zero successes in 200 fresh attacks would still allow up to about 1.5% (rule of three, 3/200; Wilson upper bound 1.9%). Set the tolerance per attack class before running, for example 1% for leaking an applicant's data, which needs about 381 fresh attacks to read under it on the Wilson bound.
3. **Compare the two sets.** Report the gap between the tuned set (0/200) and the fresh set: a large gap means the filter learned these attacks, not the class.
4. **Keep the 200.** They move to the regression suite and run on every prompt or filter change.
5. **List what was not tested** (indirect injection through uploaded payslips, other applicants' data) in the residual-risk record.

Suggested slide: "Tuning set: 0/200 (used to build v1.4, not evidence). Held-out set by <team>: k/n per class, 95% interval, tolerance signed <date>. Untested: …"
