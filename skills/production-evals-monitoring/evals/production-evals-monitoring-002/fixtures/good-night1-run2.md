**No, don't roll back today. The 86% is inside normal variation, but don't dismiss it either.**

**Why it isn't a rollback trigger**
- The ten-week average is 91%. With 100 conversations a week, sampling noise alone is about ±2.9 points (one standard deviation). The 3σ control limits are roughly 82.4% to 99.6%.
- 86% is about 1.7σ below the average. A fair week at a true 91% would score 86% or lower roughly 6% of the time. With a weekly chart that's a dip worth a look, not a shift.
- One point inside the limits is noise until a run rule or a larger sample says otherwise. Eight weeks in a row on the same side of the average would be a run-rule trigger.

**Two caveats**
- Your ten weeks vary less than sampling should produce. They have a standard deviation of about 1.5 points against the expected 2.9. That may be luck or rounding, or the sample may not be purely random. If the true week-to-week spread really is that tight, 86% looks much more unusual. Check how the 100 are drawn.
- "Nothing deployed on our side" doesn't rule out a change. Check whether the provider's model changed silently. Look at the model that actually answered in your traces, not the one you requested. Also check whether the knowledge base or policy documents were updated, whether the mix of questions shifted, and whether the judge model or rubric changed. A rollback to your August version would only help if the cause is in your own bundle. A provider model change would survive it.

**What to do today (cheap, same-day)**
1. Re-score last week with the same judge and a bigger sample. About 400 conversations gives a margin of about ±3 points, which is enough to tell 86% from 91%.
2. Break the result down by question class. Look especially at your costliest class, such as claims decisions or coverage. A drop concentrated in one class matters more than the same overall number.
3. Have an expert read the judge's failures. That confirms real failures and checks the judge itself.
4. Check the deterministic red lines: wrong-policy answers, personal data in answers, missing hand-overs. A single hit acts immediately, whatever the pass rate.
5. Diff the model that answered, the prompt version, the knowledge base and the judge version for the week.

**Pre-agree the next step with your manager**
- If the larger sample confirms a drop (roughly 84% or lower, with failures an expert confirms, concentrated in one class or tied to a specific change), roll back or fix that change.
- If it comes back near 90%, treat it as noise. Keep watching, and set up per-class control charts and the run rule.

For your manager: a rollback has its own risk and cost. It undoes a month of fixes, and it may not touch the real cause. One in-limits week doesn't justify it, but a day of checks will settle the question.