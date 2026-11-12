**No, I wouldn't attach it as the validation pack or cite 92.5% as the system's accuracy.** Model risk would likely catch these problems, and the paragraph is stronger if it names them first.

- **The interval is wide.** 37/40 has a Wilson 95% interval of roughly 80% to 97%. The point estimate clears your 90% bar, but the lower bound doesn't. The honest reading is "promising, not demonstrated."
- **The cases are synthetic.** Your team wrote them, so they weren't sampled from real complaint traffic. They probably under-represent messy, ambiguous, multi-issue complaints.
- **The definition of "correct" moved twice after you saw outputs.** The 92.5% is therefore a description of the results, not an independent test. Changing the definition is normal in a spike, but the changes need a dated log and a final re-grade of every case. That is only valid if the 90% bar was fixed beforehand.
- **There is no per-class result.** 40 cases across 6 categories is about 7 each, so you can't say anything about the costly categories. Pooling can hide a weak one.
- **The go-live design depends on accuracy.** The model classifies every complaint, and a reviewer sees only exceptions and a sample. Misclassifications the model is confident about can pass through unseen, so a pooled spike number isn't enough.

**Draft paragraph:**

> Subject: Complaint classification – feasibility evidence and proposed validation plan
>
> Attached is the report from our feasibility spike on classifying customer complaints into the six regulatory categories. We are submitting it as **feasibility evidence, not as validation of the production system.** The model classified 37 of 40 synthetic complaints correctly (92.5%; 95% Wilson interval approximately 80%–97%) against a pre-set bar of 90%. Because the lower bound is below the bar, we regard the result as promising but not demonstrated. The cases were written by the team rather than sampled from live complaints, the definition of a correct answer was refined twice after reviewing initial outputs (revisions and dates are logged in the report, and all cases were re-scored under the final definition), and the sample is too small to report results by category. We therefore do not cite 92.5% as the expected production accuracy. Ahead of the March go-live, we propose to validate on a labelled sample drawn from historical complaints, with the correctness criteria frozen before the run. We will report results per category with confidence intervals and size each category to show the agreed threshold. We will also confirm that the reviewer checks (exceptions and sampling) are set so that confident misclassifications in the highest-risk categories are detected. We would welcome your view on the thresholds and sample sizes before we run it, and we will share results before go-live.

**Before you send it**, please check or fill in three things:

1. Confirm the 90% bar was written down before the first run. If it wasn't, say so in the paragraph.
2. Agree the per-category thresholds with model risk, especially for the category where an error is most costly.
3. Check the timeline. March is tight for assembling and labelling a real sample, so start now. About 70 or more cases per category is typical to show a 90% bar at an expected rate near 95%, and more if the expected rate is closer to the bar.

If you'd like, I can help draft the validation plan or size the sample per category.