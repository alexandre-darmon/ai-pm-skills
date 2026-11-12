I'd build an evaluation, not an agent. The COO's question is whether AI can route emails accurately enough, safely enough and cheaply enough. A demo agent that handles a few emails well won't answer that. Measured results on your own historical emails will.

Routing is also a classification and extraction step in a fixed workflow, not an open-ended agent task. A single model call per email with structured output is simpler, cheaper and easier to audit than an agent.

## The stakes

6,000 emails at 4 minutes is about 400 hours a month, or roughly 2.5 FTE. That's a real but modest saving. So the decision hinges on how much can be automated safely, and what a bodily injury (BI) misroute costs, rather than on whether the AI can do it at all.

## Plan for the next few weeks

**Week 1: data and approvals**
- Pull 500–1,000 past emails with the category the handler actually routed them to and the policy number they keyed in. Oversample BI, because you need enough BI cases to measure it.
- Check with infosec and data protection that claims emails (which include health information) can go through the approved gateway. Settle this before anything else, since it can block the whole project.
- Have two senior handlers independently relabel about 200 emails. This gives you the human error rate, which is the fair benchmark. Handlers misroute too, and the AI only has to match or beat them.

**Week 2: prototype**
- One prompt per email returns category, policy number, confidence and a short reason.
- Include an "unsure / needs human" outcome.
- Validate extracted policy numbers against your policy system or at least a format check. Wrong numbers are worse than missing ones.
- Treat email content as untrusted input. Senders can try prompt injection, so the model should only output labels and never take actions.

**Week 3: measure**
- **BI recall** is the headline number: what share of true BI emails get flagged as BI. Everything else is secondary.
- Per-category precision and recall, plus a confusion matrix.
- Policy number exact-match rate.
- Accuracy at different confidence thresholds. This tells you what share of emails could be auto-routed at, say, 99% accuracy, with the rest going to a human.
- Cost per email.
- Read every failure and group them. Likely causes are multi-topic emails, a motor accident with an injury (should go to BI), forwarded chains, attachment-only emails and non-claims.

**Week 4: shadow mode, if you can get access**
- Run on live emails alongside handlers without acting. Compare the two over a couple of weeks.

## What to show the COO

1. Accuracy against the human baseline, with BI recall first.
2. A table of automation scenarios. For example: "At confidence ≥X, we auto-route Y% of emails at Z% accuracy. The rest go to a human."
3. Hours saved and cost per email under each scenario, set against the current 400 hours a month.
4. The remaining risks, including the failure types, data protection, and who owns a misrouted BI email.
5. A recommended operating model. The safest first version is probably AI-suggested routing with one-click handler confirmation, and auto-routing only for high-confidence non-BI emails. BI stays human-confirmed, or auto-routed only if the numbers clearly support it.

## Things to decide early

- Does a BI misroute from the AI have to be rarer than the handlers' current rate, or equal to it? Get the COO or compliance to set that bar before you see results, so you aren't rationalising afterward.
- Who owns the labels and the data access?
- Are any emails in languages other than English, or mostly attachments? Both change the scope.

I can help build the evaluation harness, with the labeled-data loader, the classifier prompt with structured output, and the metrics and confusion-matrix report. If you can share a sample of anonymised emails, I'd start there.