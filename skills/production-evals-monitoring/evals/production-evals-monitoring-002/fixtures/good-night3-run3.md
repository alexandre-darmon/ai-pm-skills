**No, not on this evidence. But don't do nothing today. Spend today finding out whether the drop is real.**

**Why 86% isn't enough to roll back**
- The ten-week average is 91%. With 100 conversations a week, ordinary sampling noise is about ±2.9 points for one standard deviation. The 3σ control limits are about **82.4% to 99.6%**, and 86% is inside them.
- 86% on 100 conversations has a 95% interval of roughly 79–92%, which includes your normal level.
- It's one week. The usual run rule needs 8 weeks in a row on the same side of the centre line, and you have one.

**Why you shouldn't dismiss it either**
- Your ten historical weeks vary less than chance predicts. Their standard deviation is about 1.5 points, against about 2.9 expected from sampling alone. By that tighter yardstick, 86% would be a genuine outlier (about 3.4σ).
- That tight spread could be luck. It could also mean the sampling isn't as random or independent as you think. Either way, I wouldn't call this noise.
- So it's ambiguous, and you can resolve it cheaply.

**Why a rollback may not help**
- "Nothing deployed on our side" doesn't rule out a cause outside your control. Check the following:
  - A silent provider model update. Look at which model actually answered (`gen_ai.response.model`) over the past few weeks.
  - Knowledge base or policy document changes.
  - A shift in the mix of questions, such as winter claims, renewals, or a new kind of query.
  - A change in the judge.
- If the cause is one of these, going back to the August version won't fix it. You'd also lose a month of other changes.

**What to do today (a few hours of work)**
1. Break the 86% down by question class (claims, coverage, payments). Find out whether one class, especially a costly one, is carrying the drop.
2. Re-judge a larger sample from last week's 9,000 conversations. About 300–400 gives you enough resolution to tell 86% from 91%.
3. Have an expert read the failing traces. Look for a common pattern, and check whether the judge is wrong on them.
4. Compare the model that answered, the prompt, the knowledge base, and the judge across the last few weeks.
5. Run any deterministic red-line checks, such as wrong refusals, personal data in answers, and forbidden actions, across 100% of traffic.

**What would justify a rollback**
- The larger sample confirms a real drop, meaning an interval that clearly excludes 91%.
- The failures trace to something the August bundle doesn't have.
- Or a red-line hit. A single one is enough to act on.
- Or next week also falls below the usual range. Two low weeks in a row plus a plausible cause is a strong case.

If one risky class does look bad, you can move that step down a level right away, for example by routing it to human hand-over. That is cheap, reversible, and needs no approval. It protects customers while you investigate.

**What to tell your manager**
"The drop is within normal weekly variation but I can't rule out a real change. I'll have a per-class breakdown and a larger-sample answer today. If it's confirmed and tied to something the August version avoids, we roll back. If not, a rollback risks losing a month of improvements without fixing anything."

One longer-term fix: 100 conversations a week is thin. Sample per class and size each class so it can detect a drop of about 5 points, which is roughly 300 or more per class per period. Otherwise you'll keep facing this same question every time a week looks low.