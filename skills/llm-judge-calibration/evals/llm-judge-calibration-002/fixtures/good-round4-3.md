Yes. Don't put the weekly pass rate in the steering-committee pack on Monday, because the 94% doesn't yet tell you how good the judge is.

## Why 94% isn't usable yet

1. **All 60 labels were used to build the judge.** You iterated seven versions against them and pasted four into the prompt. That makes 94% a score on the tuning data, not on summaries the judge hasn't seen. Seven rounds of fixing disagreements will push it up whether or not the judge generalises. Four of the 60 are also the judge's own examples.
2. **Agreement hides the failure you care about.** A judge that passes every summary would agree with her on 51 of 60, which is 85%. Your 94% is only 9 points above that. The four disagreements could all be missed exclusions, which would give a true-fail rate (TNR) of 5/9 = 56%. They could also all be false alarms. I can't tell which without the confusion counts, so please send them.
3. **The error that matters is the one hidden.** A summary that misses an exclusion and gets a pass is the costly mistake, because the handler relies on the summary. TNR is the number that measures it, and it rests on only 9 fails. Even a perfect 9/9 would only show TNR above about 70%, at 95% confidence.
4. **The pass rate would be biased.** The judge's raw rate mixes good summaries it passes with bad ones it lets through. If TNR is weak, the raw rate overstates quality, and it would be reported as fact. At about 2,500 a week, a figure that leans in a flattering direction will be quoted.

## What to do before switching on

1. **Get fresh labels.** Have the handler label summaries the prompt has never seen, without showing her the judge's verdicts. Fails are about 15% of your sample, so a random sample would be wasteful. Enrich it with likely fails, such as claim types where exclusions are common. TPR and TNR are measured within each class, so enrichment doesn't bias them. Aim for 100+ labels with at least 30–40 expert fails.
2. **Write the targets before scoring.** Have whoever owns the decision write down, date and sign TPR and TNR targets. I'd suggest at least 0.80 for both, and a stricter TNR gated on the lower bound of its interval, since a missed exclusion is the costly error.
3. **Score the new set once.** Report TPR and TNR with Wilson 95% intervals, not raw agreement. `scripts/judge_metrics.py` does this. If a target is missed, read the disagreements, revise the prompt, and re-test on yet another fresh set. Once you've read the disagreements on a set, it counts as tuning data.
4. **Run the bias checks that apply.**
   - If the judge and the summariser are the same model family, re-judge a sample with a different family (self-preference).
   - Re-run with a paraphrased instruction to check prompt sensitivity.
   - Pin the judge model version, because a moving alias is a new judge.
5. **Report a corrected rate with an interval.** Use observed = true × TPR + (1 − true) × (1 − TNR), solved for the true rate (Rogan–Gladen), with an interval that includes the uncertainty in TPR and TNR. Take any threshold in the pack against that interval, not the raw rate. If TPR + TNR − 1 comes out below 0.5, the correction is unstable and the judge shouldn't be used to report a rate.
6. **Plan for drift.** Re-test after any change of judge model, prompt or criterion. Also have the handler label about 50 production summaries a month, including fails, to catch drift.

## What you can do on Monday

You can start the judge in **shadow mode**. It scores all summaries, but a human reviews what it flags and what it passes, and nothing is reported as the quality figure. That also gives you production data for the drift check and a real cost per month. If the steering committee needs something, tell them the metric is in validation and give the date the validated figure will arrive. That date depends on the handler's labelling time, so ask her how long about 100–150 labels would take.

If you send the 2×2 counts for the 60 (expert pass/fail against judge pass/fail), I can tell you what the 4 disagreements say about TNR, and I can draft the calibration report from the template.