**No, not on this evidence. But don't do nothing today: run a same-day investigation, and set the trigger that would justify a rollback.**

**Why 86% isn't enough**

- Your ten-week baseline averages 91.0%. With 100 conversations a week, sampling noise alone is about ±2.9 points (one standard deviation), so the 3σ control limits are roughly 82.4% to 99.6%.
- 86% is about 1.75σ below the centre, well inside those limits. A week that low would turn up by chance roughly 1 time in 25 or 30, and you've had about 10 weeks to produce one.
- A 100-conversation sample can't reliably show a 5-point drop. You'd need about 320 per period for that.
- Your ten past weeks vary less than pure sampling noise would predict (a standard deviation of about 1.5 points, against 2.9 expected). That could be luck, or it could mean the limits are looser than they should be. Even if the true noise is smaller, one point is still one point, and it needs confirming.

**What to do today (a few hours, not a release)**

1. **Re-score a bigger sample.** Draw 300 more conversations from the same week and run them through the same judge, so you have about 400 in total. If the rate comes back around 90%, it was noise. If it comes back around 86% or lower, the drop is real.
2. **Break it down by question class** (claims, coverage, payments). A fall concentrated in one class matters more than a small overall dip. It also tells you where to look.
3. **Check for silent changes.** "Nothing deployed on our side" doesn't rule out the following:
   - The LLM provider updating the model behind the assistant. Compare the model ID that actually answered last week against earlier weeks.
   - Changes to the judge model or rubric.
   - Knowledge-base or policy-document edits.
4. **Check for input shift.** Look at the class mix, the share of unclassified requests, and anything seasonal such as storm or winter claims, or renewals.
5. **Look for red-line hits.** If any deterministic check fired (a data leak, a forbidden action, a missing hand-over), that justifies acting on a single occurrence.
6. **Read the failing traces.** Have an expert look at 15 to 20 of the judge's failures, and confirm the judge agrees with them. That also tests whether the judge itself has drifted.

**Why a rollback isn't the safe default**

Going back to August's version is a release in its own right. It hasn't been tested against today's knowledge base or policies. If the cause is a provider change, a knowledge-base change or a shift in what customers ask, the rollback won't fix it. It would also muddy the evidence, because you couldn't tell afterwards whether the pass rate changed because of the rollback or because of something else.

**Triggers for rolling back**

- The larger sample (400 or more) confirms a rate clearly below the baseline, and the investigation points to a model, prompt or version change that the August bundle predates.
- Or a second week falls below the baseline, or several weeks in a row sit below the centre line.
- Or a red-line check fires. In that case suspend or step the assistant down a level immediately, which doesn't need approval.

**What to tell your manager**

"Last week's score is within normal week-to-week variation, so it isn't enough to justify a rollback. We're re-scoring a larger sample and checking per class and for silent model changes today. We'll have a decision by end of day, and we'll roll back if the bigger sample confirms a real drop."

Longer term, 100 conversations a week is too few to detect a 5-point change. Consider about 300 a week, or a sample split by class, plus an alert on the model ID changing.