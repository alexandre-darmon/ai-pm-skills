My call: don't ship "92% sure" yet.

**Why**
- The score has never been compared with real outcomes, so "92%" is a number, not a probability. Nobody knows whether answers scored 0.92 are right 92% of the time. They could be right 70% of the time, or 98%.
- A precise percentage reads as a measured fact. If it's miscalibrated, users will over-trust the wrong answers. Once they notice it's off, they'll stop trusting the product's other signals too.
- Model scores usually cluster high and don't track how hard a case is. Showing it on every answer would mostly display noise that looks like reassurance.

**What designers can have now**
1. **Show sources next to each answer.** Users can check the answer themselves. This builds trust that has a basis.
2. **Make every answer correctable in one action**, and log the corrections. This also gives you outcome data.
3. **Hide the score for now.** Don't use it for escalation or routing either, until it's calibrated.

**How to get to showing it**
1. Collect outcomes. Use a labelled sample, plus the corrections and acceptance data from step 2.
2. Build a calibration check. Bucket answers by score and compare each bucket's score with its actual accuracy. A reliability curve shows this.
3. If it's off, recalibrate (Platt or isotonic) and re-check on held-out data.
4. Choose the display from what the data supports:
   - If it's well calibrated, show a coarse label such as "High / Medium / Low confidence" tied to measured accuracy, rather than "92%". Only show exact percentages if the bucket-level accuracy supports that precision.
   - If it's well calibrated only at the extremes, show a flag only on low-confidence answers ("check this one").
   - If it doesn't separate right from wrong, never show it.
5. After launch, monitor acceptance together with review time. Very high acceptance with short review time suggests rubber-stamping, not trust. Set thresholds from your own baseline.

**What to tell the designers**
Design the confidence slot now, so the layout is ready, but ship it empty or with sources only. The calibration work is likely days to a few weeks, not months, and it turns "92% sure" from a claim you can't back into one you can.

If you want, I can sketch the calibration check or draft the interaction spec.