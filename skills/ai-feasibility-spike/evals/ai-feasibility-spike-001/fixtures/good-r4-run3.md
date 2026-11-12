Don't build "an agent that reads the inbox" over a few weeks. Run a five-day spike that answers one yes/no question, with the pass/fail bar written down before you start. That gives the COO something she can decide on. A demo that looks good doesn't.

## The one question
"Can our approved model, suggesting a class and policy number for a handler to confirm, sort claims emails into motor, home, liability and bodily injury well enough, and at an acceptable cost per correct answer?"

Keep the spike at suggest-only. A human still sends the email on. The COO's real decision is whether to fund a project, and a suggestion step is the cheapest place to test that.

## Fix these before building (dated, signed by whoever owns the risk)
- **Time box:** 5 working days, with a kill date. Extending means a new decision, not drift.
- **Cost ceiling:** a maximum cost per correct answer. Work it out from what one handled email is worth, not from the build cost. Your baseline is about 400 handler-hours a month (6,000 × 4 min). Multiply that by the loaded hourly cost to get the baseline.
- **Bar and stop line per class:** bodily injury gets the strictest target, because a misroute delays the statutory letter. Also say which classes the product can't drop. I'd treat bodily injury as non-droppable. You may also want "unsure, send to a human" as an allowed output.
- **The decision and who takes it:** for example, go to a proper project, reshape, or stop.

## Check these before any email goes in
- **Data:** use synthetic or anonymised emails only, not real inbox emails and not production credentials. Real claims emails contain personal data and often health data. Real data needs an approved, time-limited testing arrangement.
- **Tool:** confirm with IT risk and the DPO that your gateway route and the scripts you write are authorised for this use. Do that in parallel; synthetic cases don't need to wait.
- **Design:** if this ever reads real email, it would handle private data and untrusted content. It must not also have an outbound channel. The spike should have no send tool and no write access to claims systems.

## Build
- Use a single model call or a fixed chain, not an agent. Code does the policy-number lookup and validation, and the model does the classification.
- Move to an agent loop only if that fails on named cases.
- Use the same model and gateway route production would use, so cost and quality carry over.

## Test set
- **Size per class:** the number of cases needed depends on your stop line. A 80% stop line needs about 25 cases per class, 85% needs 34, and 90% needs 53. At 10 cases, even a perfect score can't show a rate above about 72% with confidence.
- **Total:** most spikes land at 40 to 120 cases. Over-represent bodily injury and the ambiguous ones: mixed motor and injury, wrong policy numbers, forwarded chains and attachments-only emails.
- **Labels:** have experienced handlers label them.
- **Read first:** read the first 10 to 15 outputs before scoring. You may refine what "correct" means, and you should log each change. The bar and the ceiling do not move.

## Report to the COO
- **Per class:** n correct of N with a confidence interval, not one overall accuracy. "9 of 10" is not "90%".
- **Cost:** model spend divided by correct answers, plus the cost of handlers fixing wrong ones, and the hours you actually spent from logs.
- **Verdict per class:** clears, promising, undecided, short or dead.
- **Decision:** go to a requirements document, reshape (one change, new spike), or stop.
- **What this isn't:** release evidence. Before go-live you would need cases sampled from real traffic, frozen criteria, a private holdout and thresholds signed in advance.

## What I need from you
1. What is a handler's loaded hourly cost, or what is one correct routing worth? That sets the cost ceiling.
2. Who owns the business risk and will sign the bar? Probably claims operations or compliance.
3. Where could anonymised or synthetic emails come from? Can anyone anonymise a sample, or do we generate them?
4. Is your gateway route and a laptop script already authorised, or does IT risk need to approve it?

When you have those, I can draft the spike plan and the acceptance brief for the test harness. The brief would include one command that prints per-class results and cost per correct answer.