**Don't roll back today.** Last week's 86% is a worrying point, but it doesn't yet show a real change. A rollback also wouldn't address the likeliest causes.

**The numbers**
- The ten-week centre is 91.0%. With 100 conversations a week, sampling noise alone is about ±2.9 points (1σ).
- The 3σ control limits are about 82.4% to 99.6%. 86% is inside them, at roughly 1.75σ below centre.
- At n=100 the judge can't reliably detect a 5-point drop. You'd need about 324 conversations a week for that. A single week at this sample size can't separate a dip from a real shift.

**Why I'm not calling it noise**
- Your ten earlier weeks varied far less than sampling alone predicts (spread of about 1.5 points against an expected 2.9). 86% is also 3 points below your previous worst week.
- Both observations could still be luck, but they justify investigating today rather than waiting.

**Why rollback is the wrong first move**
- Nothing was deployed for a month, so the August version isn't the thing that changed.
- The more likely causes are outside your code:
  - a silent provider model update (check whether the model that answered changed);
  - changed knowledge base or policy documents;
  - a shift in the mix of questions, for example winter claims;
  - the judge drifting.
- A rollback is itself a release, and it would muddy the diagnosis.

**What to do today**
1. Score another 300 or more conversations from last week with the same judge. At n≈400 the noise is about ±1.4 points, so a real drop to 86% would stand out clearly.
2. Break the result down by question class (claims, coverage, payments). One failing class can hide inside a stable overall number.
3. Have an expert re-check the judge on the failing traces, since the judge can drift too.
4. Diff what changed: the model that answered, the prompt, the knowledge base, the judge version, and the class and language mix.
5. Check any deterministic red-line hits (data leaks, forbidden actions, wrong hand-overs). A single confirmed one would justify acting immediately.

**What would trigger a rollback**
- The larger re-score confirms a drop of about 5 points or more, and the cause is plausibly in your own stack.
- This week's rate falls below about 82%, or eight weeks in a row land below 91%.
- One class is confirmed failing, with the cause traced to something a rollback would revert.
- The investigation finds a silent model change. In that case the fix is to pin the model version and re-run your offline test set, not to restore August by default.

**For your manager**
- Today's answer is: we're investigating, and we'll have a verdict within a day, once the larger sample is scored.
- If the verdict is "real", you act with the evidence in hand.
- Longer term, move to per-class sampling of about 300 conversations a week, or chart over two weeks. That way a 5-point drop shows up in one period.