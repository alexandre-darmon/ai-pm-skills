I'd change the plan before writing the prompt. A prompt that labels 5,000 conversations with those four categories would produce a chart on Friday, but it probably wouldn't tell the committee why complaints doubled.

## Problems with the plan as stated

- **The categories are guesses.** "Hallucination / incomplete / tone / off-topic" are generic. The real failure might be specific, such as a wrong fee after the prompt change, a refusal to explain card blocking, or a missing escalation to a human. Those would be spread across your four buckets and lost.
- **Nobody has checked the LLM's labels.** If it labels 5,000 conversations and calls 18% "hallucination", you can't tell whether that's true. Without a sample checked by a banking expert, the chart is an opinion.
- **No before/after comparison.** The question is what the prompt change broke. A single month of shares can't answer that.
- **Customer data.** Mask names, card numbers and IBANs before anyone, or any model, reads the conversations.

## Plan to Friday

The reading step needs one domain expert for about a day, not the whole team.

**Mon: setup (about 2 hours)**
1. Pull the 5,000 conversations plus the previous month's, from before the prompt change. Pull the old and new prompts.
2. Mask personal data.
3. Draw about 100 conversations for reading:
   - About 60 at random, which is the only sample that gives real rates.
   - About 40 targeted: complaints, escalations, and abandoned or very long conversations. These find failure types but say nothing about how common they are.

**Tue–Wed: expert reading (about 1 day)**
4. A card/fees/transfers expert reads each sampled conversation and writes one specific note, or "pass". For example: "quoted the €2 withdrawal fee for a Gold card, which is free". A vague note like "inaccurate" doesn't help. When several things go wrong, note the first one.
5. Stop when about 20 conversations in a row show nothing new. Then group the notes into 5–8 failure modes. An LLM can propose groupings from the expert's notes, and the expert accepts or rewrites each one. Each mode gets a yes/no definition plus one pass example and one fail example.
6. Diff the old and new prompts against the modes. Many will trace straight to a specific line, and those are fixes rather than metrics.

**Wed–Thu: scale with an LLM**
7. Run one yes/no judge per mode over all 5,000 conversations, using the prompt below.
8. Check each judge on 30–50 conversations the expert has already labelled. Look at how many true failures it catches and how many good answers it wrongly flags, not just overall agreement. If a judge misses failures or over-flags, fix its definition before charting it.

**Thu–Fri: dashboard**
9. Chart each mode's share with a confidence interval, before versus after the prompt change, with the mode that grew most at the top. Add the expert's fail examples and the prompt-line diff. Put the sample size and "taxonomy v0.1, provisional" on the chart.
10. For each mode, record whether to fix it now, build a recurring evaluation, or accept it. For anything with legal or financial effect, such as wrong fees or fraud handling, list it as a question for compliance rather than a number.

If the expert is only free for half a day, read 50 conversations and label the taxonomy provisional. That is still better than the four generic buckets.

## Prompt for the labelling LLM (step 7)

Use one copy per failure mode, after the expert has defined the modes. Fill in the placeholders from step 5.

```
You are reviewing one conversation between a retail bank's customer
assistant and a customer. Personal data has been masked.

Decide whether the assistant's answers show this specific failure:

FAILURE MODE: {mode_name}
DEFINITION: {binary definition written by the domain expert}
FAIL EXAMPLE: {real masked example}
PASS EXAMPLE: {real masked example}

Reference material (the only source of truth for fees, limits and policy):
{current fee schedule / policy excerpts}

Rules:
- Judge only this failure mode. Ignore any other problems.
- Base your decision only on the conversation and the reference
  material. If the reference does not cover the claim, answer
  "unclear", not "fail".
- Quote the exact assistant sentence that supports your decision.

Return JSON only:
{"verdict": "fail" | "pass" | "unclear",
 "evidence": "<exact quote or empty>",
 "reason": "<one sentence>"}

CONVERSATION:
{conversation}
```

Send "unclear" verdicts to the expert, and re-check a random sample of "pass" verdicts as well.

## What I need from you

- Is there a prior month of conversations from before the change, and does the log record the prompt version?
- Who is the banking expert who can read for a day?
- Do you have a feedback signal such as thumbs, escalations or complaint tags? It would make the targeted sample much better.

If you give me a masked export, I can draft the reading sheet and write the script that computes shares and intervals.