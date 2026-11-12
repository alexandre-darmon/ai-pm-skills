**No, not on this evidence. But don't do nothing today.**

**Why 86% isn't a signal yet**
- The ten-week baseline averages 91.0%. With 100 conversations a week, sampling noise alone is about ±2.9 points (1σ). The 3σ control limits are roughly 82.4% to 99.6%.
- 86% is about 1.75σ below the centre, so it falls inside the limits. A dip like that happens by chance fairly often, and nothing in a single week separates it from noise.
- It also isn't a run: it's one point, not eight in a row on one side of the centre line.
- A caveat in the other direction: your ten baseline weeks vary less (SD about 1.5 points) than pure sampling noise at n=100 would predict (about 2.9). That's a bit unusual and could just be luck. If your real week-to-week spread is that tight, 86% would look more serious. It's another reason to take a larger sample instead of arguing from one point.
- To detect a 5-point drop reliably, you need about 320 to 580 judged conversations per period, not 100.

**What to do today**
1. **Re-judge a bigger sample from last week.** Draw 300 to 400 more conversations at random, using the same judge version. If the pooled rate stays near 86%, the drop is real. If it returns to about 91%, it was noise.
2. **Break it down by question class.** Check claims, coverage and payments separately. A drop in one risky class, or a shift in the class mix, matters more than the headline number.
3. **Look for changes on the provider's side, even though you deployed nothing.**
   - Check whether the model that actually answered (`gen_ai.response.model`) changed, and whether the model behind the judge changed.
   - Check for knowledge-base or policy-document updates, such as new terms or rates.
   - Check for changes in input, such as seasonal claims, a storm, or a new product.
4. **Check the deterministic red lines** (data leaks, forbidden actions, missing hand-overs). One hit acts immediately, regardless of the pass rate.
5. **Have your experts read 20 to 30 of the failing conversations.** This confirms whether the judge is right and whether there is a new failure mode.

**When to roll back**
- The larger sample confirms a drop of about 5 points or more, or a second week falls outside the limits (or the weeks keep trending down).
- Or a red-line check fires.
- And the August bundle can fix it. If the provider silently changed the model, rolling back your prompt and knowledge base may not undo it. Pinned, dated model versions are what make a rollback meaningful.

**For your manager**
A rollback is itself a release. It has its own risk, and it throws away any improvements since August. Rolling back on a point inside the noise band could cost more than it saves, and you'd learn nothing about the cause. If today's checks come back clean, the decision can wait until next Monday's sample, and you'd be doing it with real evidence.

I can also write the weekly control chart and sample-size rules into a monitoring plan, so the next dip gets a decision rule before anyone is under pressure.