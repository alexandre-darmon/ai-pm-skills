I'd change the plan. Don't build an agent over the live inbox for a few weeks. Run a one-week spike that answers one yes/no question, and give the COO that answer with its limits stated.

## 1. The one question
> Can our approved model, working as a suggestion that a handler confirms, sort claims emails into motor, home, liability and bodily injury, and extract the policy number, well enough and at a low enough cost per correct answer to justify a real project?

Routing is a fixed workflow, so start with one model call per email. Code can do the policy-number lookup, and the model handles the judgment. Only move to an agent loop if that fails on specific cases that need one, and name those cases. Use the same model and gateway route production would use, or neither the quality nor the cost will transfer.

## 2. Fix these before building, dated and signed by whoever owns the risk
- **Appetite:** 5 working days, with a kill date. Past it, the spike stops. Extending means a new decision with a new budget.
- **Cost ceiling per correct answer.** Derive it from what a correct answer is worth, not from what the build costs. Today that is 4 minutes of handler time × 6,000 emails, about 400 hours a month. I need your loaded handler cost per hour to turn that into a number.
- **Bar per class, with a stop line** (the rate below which the idea is dead). Bodily injury gets the strictest bar, because a misroute delays a statutory letter. Treat it as a class the product can't drop. Policy-number extraction is its own scored field (exact match).
- **The decision this feeds and who takes it.** The COO's choices are go, reshape or stop.

Write these down before you see any results. A bar set afterwards only describes the results.

## 3. Data and tooling (do this first, it can block you)
- **No production emails or credentials in the spike.** Claims emails carry personal and health data. Use synthetic or properly anonymised cases. Real data needs an approved, time-limited testing exception from your DPO and IT risk.
- Check that the gateway route is approved for this use. Ask IT risk and the DPO in parallel. Synthetic cases don't need to wait for them.
- **Case count per class.** The stop line decides how many cases you need. At a 75% stop line you need about 19 per class, at 85% about 34, and at 90% about 53. With only 10 cases, even 10 of 10 can't show 75% with confidence. Expect 40–120 cases in total, with extra bodily injury cases. State how much of the set is synthetic.
- Your handlers' past routing decisions are a good source of labels, but only once anonymised or approved.

## 4. Safety design
Inbound emails are untrusted text, they contain private data, and a router could forward them. Those three together are a prompt-injection risk. Remove one of them in code, not in the prompt. The prototype should write a label and a policy number to a file or table and have no send or forward tool. A human does any forwarding. This also matches the autonomy level you are testing: suggest, then a handler confirms.

## 5. How to read the results
- Read the first 10–15 outputs by hand before scoring. Your definition of "correct" will sharpen. You may revise the criteria, but log each revision and re-grade everything. The bar and appetite never move.
- Report each class as n correct of N with a Wilson confidence interval, never one blended accuracy. A class clears the bar only when the interval's lower bound is above it. For example, 9 of 10 is not demonstrated.
- Cost per correct answer is model spend divided by correct answers, plus the handler time spent fixing wrong ones.
- Take hours spent from logs, not from impressions.
- The result is one of three outcomes:
  - **Go to PRD:** every must-keep class is promising or clears, and cost is within the ceiling.
  - **Reshape:** change one thing, such as narrower scope or a lower autonomy level, and run a new spike.
  - **Stop:** bodily injury is dead, or the kill date passes without an answer.

## 6. What to tell the COO
A spike number is evidence about feasibility, not accuracy for release. A few dozen hand-built cases, criteria refined along the way and a throwaway harness can't support a go-live claim. If the answer is go, the next phase builds a proper evaluation set sampled from real traffic, with frozen criteria, a holdout, and thresholds signed in advance. That set also needs sizing: showing a 90% bar when you expect 92.5% takes roughly 430 cases per class.

## What I need from you
1. Who signs for the business risk, and who is the COO's decision-maker for this?
2. Loaded handler cost per hour (to set the cost ceiling).
3. Whether you can get anonymised historical emails with the handler's routing, or whether you'll start synthetic.
4. Whether you're an EU-regulated entity. That determines how strict the tooling and data rules are.

Once I have those, I can draft the one-page signed plan and the acceptance brief. I can then build the harness here: the case files, one command that prints n of N per class with intervals, and cost per correct answer.