Replace the single 85% threshold with a threshold per question class: a global score hides failures in the small classes, and warranty claims are only about 12 of your 120 cases.

- Warranty claims have legal consequences: set a stricter bar, 95% or more, and route failures to a human.
- Order status and returns: 85% is fine.
- Product advice: 80%.

Re-sample the suite with stratified sampling so warranty claims and product advice get at least 30 cases each, instead of the 12 and 6 a random draw gives. Keep 20% of the cases as a private holdout that never enters a prompt or a repo.

Freeze the 88% run as the baseline, with the model and version, the judge model, the date and the set version.

Track cost per correct answer, not cost per answer: at 0.04 EUR per answer and 88% correct, that is about 0.045 EUR per correct answer.

Before adding graders, read 30 of the failed or borderline answers from the last run, note what went wrong in each, and cluster the notes into failure modes. Write graders for those.

Write the new thresholds down before the next run, dated, and signed by the support lead; only legal may relax the warranty bar.
