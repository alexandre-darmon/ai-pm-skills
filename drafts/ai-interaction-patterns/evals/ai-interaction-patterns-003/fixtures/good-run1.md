**My call: don't ship "92% sure" yet.** Ship sources next to each answer, and show the score only after it has been calibrated against real outcomes.

**Why**
- An uncalibrated score is not a probability. Nobody has checked whether the answers marked 92% are right 92% of the time. If they're right 75% of the time, the UI is making a false claim to every user.
- A number like that gets treated as precise. Users will stop checking the answers it flags as high-confidence, and those are the ones where a wrong answer costs the most.
- Model scores often don't track how hard a case is. They can be high on confidently wrong answers.
- Once users have been burned by a "92%" that was wrong, trust is hard to win back.

**What to do instead**
1. **Now:** show sources beside each answer so users can verify it. Make every answer correctable in one action, and log each correction.
2. **Calibration:** collect real outcomes, from corrections and from ground-truth labels on a sample. Then plot predicted score against observed accuracy in a reliability curve. This is usually a few weeks of work, not months.
3. **If it calibrates:** show the score, but as coarse bands such as "High / Medium / Check this" rather than a precise percentage. Set the band cutoffs from the observed accuracy.
4. **If it doesn't:** recalibrate (Platt scaling or isotonic regression), or keep the score hidden and rely on sources.
5. **After launch:** monitor calibration for drift. Read trust from behaviour, meaning acceptance rate together with review time and the share of outputs edited. Very high acceptance with very short review time suggests rubber-stamping, not trust.

**What to tell the designers**
Their goal is right: users should be able to tell when to rely on an answer. A number only does that if it's true. Give them a design slot for a confidence indicator now, with sources filling it for the time being. That way the calibrated version drops in later without a redesign.

If you can get even a few hundred labelled outcomes, I can help set up the calibration check.