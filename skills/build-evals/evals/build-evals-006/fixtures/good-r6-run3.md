**Not on chargeback eligibility, no. The other four classes can ship Monday on their own results.**

**Why 58/60 doesn't clear 95%.** The point score is 96.7%, but 60 cases is too few to separate that from a true rate below the bar. The 95% Wilson interval is about **88.6% to 99.1%**. The lower bound is well under 95%, so the result is "not demonstrated", not "passes". Two misses either way would swing the score several points. For a class where a wrong answer costs us the disputed amount, the gate should pass only when the lower bound clears the threshold.

**What I'd tell Product**
- **Ship** the four other classes, each on its own signed bar.
- **Chargeback eligibility** either goes behind human review (the assistant drafts and an agent confirms) or is held out of the release. It shouldn't go live autonomously.
- **More cases before Monday won't fix this.** If the true rate is about 97%, the lower bound only clears 95% at roughly 450 cases. At 98% it takes about 200, and at 96% about 1,800. So the realistic options are a human-reviewed launch now and a larger set later.
- **The only exception** is the person who signed the threshold. They can accept the residual risk in writing, with their name and a date. Product can't make that call by reading the point score.

**Checks before the decision is final**
1. **Signed reading.** If the signed threshold explicitly said "point score ≥ 95%", then it passes as written. Even so, I'd flag the 88.6% lower bound to the signer before they rely on it.
2. **The two misses.** Were they confident wrong answers, or hand-offs graded as wrong? If wrong answers cost more than hand-offs, score correct, abstained and wrong separately, and report coverage next to the error rate.
3. **Set quality.** Check that the 60 cases are mostly real, sampled by risk, and not used to tune the prompt. Also check that the two failures share a pattern, since a single failure mode is cheap to fix.
4. **Baseline.** Compare against the previous version on the same 60 cases, paired. If the new version isn't clearly better, the case for shipping weakens.

Next steps: I can draft the eval plan, covering the per-class table with intervals, the case count needed for chargeback eligibility, and the written sign-off wording. Or I can write a short note for Product. Tell me which you want.