Yes. Don't put the number in the steering pack on Monday. The 94% doesn't tell you how well the judge works.

**Why the 94% doesn't count**
- **Tuned data.** You iterated seven prompt versions against those 60 labels, and four of them are now examples inside the prompt. That figure measures how well the judge was fitted to those summaries, not how it will do on new ones.
- **Raw agreement is the wrong measure.** 51 of the 60 are fine, so a judge that passes everything would score 85%. Your 94% is only 9 points above that.
- **The 4 errors matter more than the 94%.** You haven't said where they fall. If all 4 are among the 9 missed exclusions, the judge catches only 5 of 9, which is about 56%, and it is missing exactly what you built it to find. Even in the best case, 9 fails is too few to pin down the catch rate. The interval is very wide.
- **The weekly rate would be biased.** A judge that lets some bad summaries through inflates the pass rate. The raw rate needs a correction and an interval before anyone reads it as quality.

**What to do before Monday, or before the figure goes in the pack**
1. **Write the targets first.** The decision owner dates and signs a catch-rate target (judge fails the summaries that miss an exclusion) and a pass-rate target (judge passes the good ones). Both are written before anything is scored. The default is at least 80% each, and stricter on the catch rate, since a missed exclusion is the costly error. Decide who owns that.
2. **Get fresh labels.** Your senior handler labels new summaries the judge has never seen and that weren't used for any prompt edit. Enrich the sample with likely misses so you get about 30–60 real fails, because the precision of the catch rate depends on the number of fails. Label them without showing her the judge's verdicts. Aim for 100 or more in total.
3. **Score them once.** Report the catch rate and the pass rate, each with a 95% interval, plus the agreement a pass-everything judge would get on that set. Don't read the disagreements and then re-tune on the same set. If you do, it becomes dev data and you need another fresh set.
4. **Check bias.**
   - If the judge and the summarising model are from the same family, re-judge a sample with a different family.
   - Re-run with a paraphrased instruction to see how much the verdicts move.
   - Pin the judge model version.
5. **Correct the weekly rate.** Use corrected = (observed + catch rate − 1) ÷ (catch rate + pass rate − 1), with an interval that carries the uncertainty in both rates. If catch rate plus pass rate minus 1 is below 0.5, don't use this judge for a rate at all. Compare any committee threshold with the interval, not the raw rate.
6. **If it misses a target, it isn't a gate yet.** Read the disagreements, add a pass example and a fail example for the cases it got wrong, and re-test on new labels. A handler reviews a sample of summaries in the meantime.

**What you can do on Monday.** You can run the judge in shadow mode and have a handler spot-check a sample each week, with a few of the judge's fails and a few of its passes. Label it "unvalidated" internally. Don't publish a pass rate.

**Once it's live.** Re-validate whenever the judge model, prompt or criterion changes. Also have the handler label about 50 production summaries a month, fails included, to catch drift. At 2,500 a week, if your sample is representative, roughly 15% of summaries (about 375 a week) could be missing an exclusion, so the correction matters.

If you share the judge's verdicts on the 60 (which 4 it got wrong), I can compute the interval you actually have now, and I can run the metrics script once the fresh set is labelled.