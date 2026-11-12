I'd change the plan in three ways: shrink "an agent over a few weeks" to a one-week feasibility spike, fix the pass/fail bars before building, and show the COO measured results per class instead of a demo. Her real question is whether the model sorts and extracts well enough, cheaply enough, on the class that hurts most. A working agent doesn't answer that, and a polished demo can hide the gaps.

## 1. Write one question and get it signed
"Can our approved model, suggesting a class and policy number for a human to confirm, sort claims emails into motor, home, liability and bodily injury accurately enough, for under X per correct email?"

Before any build, the person who owns the risk (you, or the claims head) signs and dates these:

- **Appetite:** 5 working days and a cost ceiling per correct answer. Derive the ceiling from what a correct email is worth. Today that is about 4 minutes of handler time, or about 400 hours a month across 6,000 emails. I need your loaded hourly handler cost to put a number on it.
- **Bar per class, with a stop line.** Bodily injury gets the strictest target because a misroute delays a statutory letter. Suggested starting point: 90% target and 85% stop line for bodily injury, lower for the others. Setting these is your and the COO's call.
- **Kill date:** the end of week one. Extending it is a new decision, not drift.
- **The decision this feeds and who takes it.** That is the COO's go, reshape or stop.

## 2. Check the tool and the data
- **Tool:** confirm with IT risk that using the approved model through the gateway for a prototype is covered, and whether a script you build counts as a registered tool. Ask early, because this is the likeliest cause of delay.
- **Data:** use synthetic or anonymised emails only, not live inbox content and no production credentials. Real emails need an approved, time-limited testing arrangement. Ask the DPO in parallel. A good source is old emails with names and policy numbers scrubbed or replaced, plus synthetic edge cases.
- **Size:** each class needs enough cases to prove its bar. With a 85% stop line you need about 34 cases per class, and about 53 for 90%. Over-represent bodily injury and the ambiguous cases, such as an accident with both vehicle damage and an injury. Expect 60–120 cases in total.

## 3. Build the smallest thing
- **One model call per email, not an agent.** It returns a class, a confidence level, an extracted policy number and a one-line reason. Code validates the policy number format and looks it up. The model does the judgment, and code does the lookups.
- **It suggests and a human confirms,** so a mistake never reaches a team on its own. Emails are untrusted content, so the prototype must have no outbound send tool. Read-only plus a human forwarding removes that risk in code.
- Read the first 10–15 outputs before grading anything, since your definition of "correct" will sharpen. Log any change to the criteria. The bar and stop lines don't move.

## 4. What the COO sees
A one-page report with:
- Results per class as n of N with a confidence interval, not one pooled accuracy.
- Each class labelled clears, promising, undecided, short or dead against its bar.
- Cost per correct answer, plus hours you actually spent, from logs.
- The recommendation: go to a real project, reshape (one change, and a new spike), or stop.
- A clear note that a spike number is not release evidence. A real project would need cases sampled from live traffic, frozen criteria and a held-out test set before anyone quotes an accuracy figure.

A short live demo can sit alongside the report, but the numbers carry the decision.

## What I need from you to start
1. Your loaded handler hourly cost, to set the cost ceiling.
2. Where the test emails can come from, and whether they can be anonymised.
3. The model and gateway details production would use. The spike should run on the same route, or neither quality nor cost will transfer.
4. Who signs the bars.

Once you have those, I can set up the harness: a case folder, an expected-answers file, and one command that prints n of N per class and cost per correct answer. I can also draft the spike report template and the one-page IT risk and DPO check message so those start today.