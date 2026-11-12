I'd change the plan in one place: don't fix the four categories before anyone has read a conversation. "Hallucination / incomplete / tone / off-topic" is a generic list. It will tell the committee a percentage but not what the prompt change broke. Complaints doubling suggests one or two specific regressions, such as a dropped fee disclosure or a wrong transfer cutoff. Generic buckets will smear those across categories.

The LLM is still the right tool for labelling all 5,000. It just shouldn't be the first reader, and its labels need checking against a person's. That costs about half a day of one domain expert's time, not a week.

## Plan to Friday

Today is Tuesday, so this fits in three days.

**Tuesday: prepare the data**
1. Mask personal data (names, card and account numbers, IBANs, phone numbers, emails) before anyone reads a conversation or sends it to a model. This is a bank, so do this first. Check with your DPO that the LLM provider is approved for this data.
2. Draw about 100 conversations in two streams:
   - **Random (about 60):** a simple random draw from last month. Only this stream can estimate how often a problem occurs.
   - **Targeted (about 40):** conversations with complaints, escalations, thumbs-down, or abandonment, and any from the days right after the prompt change. These find problems but say nothing about rates.
3. Pull the same random sample from the month before the prompt change, if you have it. "Complaints doubled" is a before/after question, and a single month can't answer it.

**Tuesday afternoon to Wednesday morning: expert reading (about 3–4 hours)**
4. One person who owns quality for cards, fees and transfers (product, operations or compliance, not the build team) reads each conversation. For each one they write a specific free-text note, such as "quoted €2 ATM fee, current schedule says €3.50", or "pass". If a conversation has several errors, note the first one, because later errors are often consequences of it.
5. Keep reading until about 20 conversations in a row show nothing new. If you don't get there, label the taxonomy "provisional" on the dashboard.

**Wednesday midday: define the failure modes**
6. Group the notes into 4–8 modes. Each gets a yes/no definition, one pass example and one fail example. An LLM can suggest groupings, but the expert accepts or rewrites each one.
7. For each mode, decide whether it's a fix, an evaluation, or something to accept:
   - If the prompt change removed an instruction, fix the prompt now and keep the failing conversations as regression cases. Don't build a metric for something the prompt never asked for.
   - If the instruction was there and the model still fails, keep the mode for the automated labelling.

**Wednesday afternoon: validate the labeller**
8. Run the prompt below on the expert's ~100 conversations. Use about 30 as examples inside the prompt and hold out the rest. Measure true-positive and true-negative rate per mode, not overall agreement, because a labeller that passes everything still scores high on agreement. Rewrite any mode with weak rates. If a mode can't be fixed, report it from the expert sample only.

**Thursday: label and build the dashboard**
9. Run the labeller on all 5,000 and compute each mode's share with a confidence interval.
10. Dashboard contents:
    - Share of conversations per mode, with intervals, before vs. after the prompt change.
    - Two or three real example conversations per mode, masked.
    - A footer stating sample sizes, taxonomy version, and the labeller's measured accuracy.
    - Cost per mode only if finance gives you a sourced unit cost. Otherwise write "to source".

**Friday: present**
11. Lead with "the prompt change caused X and Y; here's the fix and how we'll confirm it." Anything unverified is marked provisional.

## Labelling prompt

Run it once per failure mode. One yes/no question per call is more reliable than one call that assigns a category. Fill the bracketed parts from Wednesday's taxonomy.

```
You are reviewing a conversation between a customer and a retail banking
assistant (cards, fees, transfers). Personal data has been masked.

Your task: decide whether this conversation FAILS the following criterion.

CRITERION: [mode name, e.g. "Wrong or unsupported fee/limit/deadline"]
DEFINITION: [one or two sentences written by the domain expert. State exactly
what counts as a failure and what does not.]
FAIL example: [real masked excerpt + why it fails]
PASS example: [real masked excerpt + why it passes]
[2–3 more borderline examples with the expert's verdict]

REFERENCE MATERIAL (the only source of truth for facts):
[current fee schedule / card terms / transfer cutoffs, or the retrieved
documents the assistant saw]

CONVERSATION:
<conversation>
{conversation}
</conversation>

Instructions:
- Judge only this criterion. Ignore any other problems you notice.
- Check factual claims against the reference material only, never against
  your own knowledge of banking. If the material doesn't cover a claim, answer
  "unclear" rather than guessing.
- Quote the exact assistant sentence(s) that justify your verdict.
- If the conversation has several failures of this kind, cite the first one.

Respond in JSON only:
{"evidence": "<quoted text>", "reasoning": "<2-3 sentences>",
 "verdict": "fail" | "pass" | "unclear"}
```

Two notes on the prompt:
- **The reference material is required for fact checks.** Without the actual fee schedule and terms, an LLM can't tell a hallucinated fee from a real one. It will just judge whether the answer sounds plausible.
- **Count "unclear" separately.** Send those to the expert instead of folding them into pass or fail.

## What I'd tell your manager
Their plan isn't wrong about the LLM doing the volume work. The addition is a few hours of expert reading before the labelling, which is what makes the dashboard explain the complaints. Without it, the committee gets a chart of generic categories that doesn't say what to change.

If it helps, I can draft the note-taking template for the expert, a script to compute shares with intervals from the labelled output, or the dashboard itself once you have the labels.