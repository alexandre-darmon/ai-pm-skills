I'd keep your manager's pipeline but change its order. The LLM labeller can run at scale, but the categories need to come from someone reading real conversations first. Otherwise the dashboard will show the share of "hallucination", "incomplete", "tone" and "off-topic". Those are generic guesses, and they probably won't point at what the prompt change broke. It also won't show whether the labeller is right.

The cost is about half a day of one person's time, not days of hand review.

## Plan: Tuesday to Friday

**Tuesday: mask and sample**
- Mask personal data (names, card and account numbers, IBANs) before anyone reads a conversation or sends one to a model.
- Draw two samples:
  - About 100 random conversations from last month. This is the only sample that gives you rates.
  - About 50 targeted ones: complaints, escalations, thumbs-down, abandoned or very long conversations. They help you find failure types, but you can't use them for rates.
- If you have logs from before the prompt change, pull about 50 random ones for comparison.

**Wednesday: expert reading**
- The person who owns card, fee and transfer quality (not the build team) reads each conversation. For each one they write a specific note, such as "quoted the old transfer fee" or "didn't say the card block takes 24h", or "pass".
- When a conversation has a chain of errors, note the first one.
- Stop when about 20 conversations in a row show nothing new. This usually takes 50 to 100, or roughly 3 to 4 hours.
- Group the notes into failure modes. An LLM can propose groupings, but the expert decides. Give each mode a pass/fail definition with one example of each.
- My guess is that many failures will be gaps in the prompt, such as a missing instruction, a lost fee table or a dropped escalation rule. Those get fixed in the prompt directly. They don't need a judge.

**Thursday: label at scale and check the labeller**
- Run the labelling prompt below over all 5,000 conversations, one mode per call.
- Have the expert label 50 to 60 fresh random conversations they haven't read yet. Compare their labels with the LLM's for each mode, looking at true-positive and true-negative rates, not overall agreement. A labeller that passes everything can still show high agreement.
- If a mode's labeller is poor, rewrite its definition and re-run. If it's still poor, drop that mode from the dashboard.

**Friday: dashboard**
- For each mode, show the share with a confidence interval. For example, 6 of 60 is 10%, with an interval of about 5% to 20%.
- Show before vs. after the prompt change, if you have the old logs.
- Rank modes by monthly volume × share × cost per occurrence. Use a cost only if someone can source it. Otherwise write "to source" with an owner.
- Label it "taxonomy v0.1, provisional" if you didn't reach saturation.
- Footnote the labeller's validation: "LLM-labelled, checked against N expert labels, TPR x / TNR y."

## Labelling prompt

Use one call per failure mode, not one call with all four categories. Fill in the bracketed parts from Wednesday's definitions. Until then, the four original categories are only hypotheses.

```
You are reviewing a conversation between a customer and a retail bank's
virtual assistant (topics: cards, fees, transfers). Personal data has been
masked.

Decide whether the assistant's replies exhibit ONE specific failure mode.

FAILURE MODE: [name]
DEFINITION: [binary definition written by the domain expert, e.g. "The
assistant states a fee, limit, delay or eligibility rule that differs from
the reference information below."]
DOES NOT COUNT: [edge cases the expert ruled out]

EXAMPLE THAT FAILS: [real, masked excerpt + why it fails]
EXAMPLE THAT PASSES: [real, masked excerpt + why it passes]

REFERENCE INFORMATION (current fee schedule, card terms, transfer rules):
[paste or retrieve; required for any factual-accuracy mode]

CONVERSATION:
<conversation>
{conversation}
</conversation>

Instructions:
- Judge only this failure mode. Ignore other problems.
- Base your decision only on the conversation and the reference
  information. Do not use outside knowledge about banking.
- If the evidence is ambiguous, answer "unclear" rather than guessing.
- Quote the exact assistant sentence that supports your decision.

Respond in JSON only:
{"evidence": "<quote or null>", "reasoning": "<one or two sentences>",
 "verdict": "fail" | "pass" | "unclear"}
```

Why it's built this way:
- **Binary verdict:** a pass/fail answer is easier to validate than a score.
- **Evidence quote:** it lets you spot-check quickly.
- **"Unclear" option:** report the share of "unclear" answers on the dashboard. Don't hide it.
- **Reference information:** the labeller can't judge accuracy about fees without it, and without it it will confidently invent answers.

## What to tell your manager

- The plan stays the same: an LLM labels 5,000 conversations and you chart the shares.
- Two additions make the chart defensible to the executive committee. The categories come from about 100 real conversations, and the labeller is checked against an expert's labels.
- Without those, the likely outcome is a confident chart that nobody can explain when someone asks "how do you know the labels are right?"

If you can tell me what's available (log format, whether pre-change logs exist, who the domain expert is), I can write the masking and sampling script and the batch labelling runner.