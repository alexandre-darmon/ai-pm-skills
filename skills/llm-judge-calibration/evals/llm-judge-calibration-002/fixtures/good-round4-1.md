Yes. Don't put the number in the steering pack yet, because the 94% doesn't tell you how well the judge works on new summaries.

**Why 94% can't be trusted**
- **It was measured on tuning data.** You iterated seven prompt versions on those 60 summaries and pasted four of them in as examples. That score describes how well the prompt was fitted to those 60, not how it will do on next week's claims.
- **Agreement hides the failure you care about.** 51 of the 60 are fine, so a judge that passes everything would agree 85% of the time. Your 94% is 4 errors, and we don't know which kind. If all 4 were missed exclusions, the judge catches only 5 of 9 (56%). With only 9 fails, even a perfect-looking 8 of 9 has a 95% interval of roughly 52–98%.
- **A missed exclusion is the costly error.** The judge exists to catch summaries that leave one out. If it lets those through, the weekly pass rate will look better than reality.

**What to do before Monday**
1. **Get fresh labels.** Ask your senior handler to label new summaries that the judge and the prompt have never seen, and have them labelled without seeing the judge's verdicts. Aim for 100 or more, enriched so there are at least 30 to 40 with a missed exclusion. The precision on catching exclusions depends on the number of fails, not the total. Enrichment doesn't bias the rates, because they are measured within each class.
2. **Set targets first, in writing.** The decision owner should write down dated minimums for two rates: the share of good summaries the judge passes, and the share of bad ones it fails. A sensible default is 80% each, stricter on the second because a false pass is the costly error. Do this before scoring the fresh set.
3. **Score the fresh set once.** Report both rates with 95% intervals, not raw agreement. If both targets are met, the judge can run at scale. If either is missed, it isn't ready, whatever the date. Read the disagreements, revise the prompt, and re-test on yet another fresh set, because the one you used to revise has become tuning data.
4. **Correct the weekly rate.** The judge's raw pass rate mixes good summaries it passes with bad ones it lets through. Use the two measured rates to correct it and report the result with an interval, for example "88% ± 5". Don't report the raw rate. If the two rates are so weak that the correction is unstable, don't report a rate from this judge at all.
5. **Check the biases.**
   - Pin the judge model version, since an alias that moves is a new judge.
   - If the judge and the summarising assistant are the same model family, re-judge a sample with a different family.
   - Re-run the fresh set with a paraphrased instruction to see whether verdicts hold.
6. **Plan re-validation.** Re-test on fresh labels after any change to the judge model, prompt or criterion. Also have the handler label about 50 production summaries a month, with fails included, to catch drift.

**If Monday can't move**
You can switch the judge on, but treat it as a screening tool rather than a measurement. Have a human review a sample of what it passes. In the pack, don't report a pass rate yet. Say that a validated measure is coming once the fresh labels are scored.

I can compute the intervals and the corrected rate once you have the fresh labels as a CSV with `human` and `judge` columns. The calibration report can follow the template too.