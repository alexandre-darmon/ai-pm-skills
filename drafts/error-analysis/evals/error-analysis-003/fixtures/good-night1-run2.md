I'd change the plan in one place. The LLM-labelling idea is fine, but the four categories are a guess made before anyone has read a conversation. A chart of "hallucination 18%, tone 12%…" would go to the executive committee and might not explain the complaints. It could also send you to fix the wrong thing.

**What to change:** one person reads about 100 conversations first, and the LLM then labels all 5,000 using the categories that reading produces. That is roughly one day of one person's time, not a week of the team's.

## Plan to Friday

**Mon: sample and mask**
- Mask personal data (names, card and account numbers, IBANs, addresses) before anyone reads a conversation or sends one to a model. Keep the raw text in its source system.
- Draw two samples from last month:
  - **Random, about 60 conversations.** This is the only sample that gives you a rate.
  - **Targeted, about 40 conversations.** Take complaints, escalations, thumbs-down and abandoned conversations. Add a few on fees and disputed transfers, where a wrong answer has financial or regulatory consequences. This sample finds failure types but cannot give a rate.
- Pull about 30 conversations from before the prompt change. Without a baseline, the dashboard can't show that things got worse.
- Get the prompt diff. Complaints doubling right after a prompt change often mean an instruction was dropped or added, for example a fee-disclosure rule or a "don't say you can't help" line. That is a fix, not a metric.

**Tue: expert reads**
- Name one domain expert, for example a card or fees product owner or a senior advisor, and not an engineer.
- For each conversation they write a free-text note on what went wrong, or "pass". Notes should be specific, such as "quoted the old €2 ATM fee" and not "inaccurate".
- If the failure started upstream (wrong retrieval, then a wrong answer), note only the first failure.
- Stop when about 20 conversations in a row show nothing new. If you haven't reached that point, label the taxonomy "provisional" on the dashboard.

**Wed: build the taxonomy and fix the obvious**
- Group the notes into failure modes. An LLM can propose the groupings, but the expert accepts or rewrites each one.
- Give each mode a yes/no definition plus one pass example and one fail example.
- Count each mode in the random sample, with a confidence interval. For example, 6 of 60 is 10% (5–20%). Don't use the targeted sample for rates.
- If a mode comes from a missing instruction, missing data or a gap in the knowledge base, fix it now and re-run those conversations. Don't build a measurement for it.

**Thu: label all 5,000 with the LLM, then check it**
- Run the prompt below, one yes/no question per mode.
- Have the expert label about 50 conversations blind, then compare. If agreement on a mode is poor, fix its definition before charting it.

**Fri: dashboard**
- Show the share of conversations per failure mode, with intervals, for last month against the pre-change baseline.
- Rank the modes by expected cost (volume × share × cost per occurrence). Mark any cost without a source as "to source" and name an owner. Send fee-misstatement and dispute-advice issues to compliance as questions, not as euro figures.
- Add the fixes already shipped, a "provisional" label if it applies, and the open questions.

## Labelling prompt (use after Wednesday)

```
You are reviewing a conversation between a customer and a retail banking
assistant. The assistant answers questions about cards, fees and transfers.
Personal data has been masked.

Decide, for each failure mode below, whether the conversation FAILS it.
Judge only what the assistant said, using the reference material provided.
A mode is a fail only if the definition clearly applies. If unsure, answer
"unclear" and explain.

Failure modes (version {{taxonomy_version}}):
{{for each mode:
 - id: {{id}}
   definition: {{binary definition written by the expert}}
   fail example: {{example}}
   pass example: {{example}}
}}

Reference material (current fee schedule and policies):
{{fee_schedule_and_policy_excerpts}}

Conversation:
{{masked_conversation}}

Rules:
- Evaluate each mode independently. Do not give an overall score.
- If several failures occur, mark the first one in the conversation as
  "root_cause": true, since later errors are often consequences of it.
- Quote the exact assistant sentence that supports each fail.
- Do not invent facts. If the reference material does not cover the
  claim, answer "unclear" and not "fail".
- If the conversation shows none of the modes, set "any_failure": false.

Return JSON only:
{
  "any_failure": bool,
  "modes": [
    {"id": "...", "result": "pass|fail|unclear",
     "root_cause": bool, "evidence_quote": "...", "reason": "one sentence"}
  ]
}
```

Your manager's four labels can go in as hypotheses to check while the expert reads. They shouldn't be the final categories unless the reading confirms them. "Hallucination" in particular is usually several different things in banking, such as a wrong fee, an invented policy or a wrong transfer limit. Each has a different fix and a different risk.

## What you need from the team

- One expert for about a day, plus the prompt diff and the pre-change conversations.
- A decision on how personal data is masked, and sign-off from your data protection contact before any conversation goes to an external model.
- A source for the cost of one wrong answer, such as a complaint handling cost or the cost of a refund. If you don't have one by Friday, show shares and leave the euro column as "to source".

If it helps, I can write a script that masks the conversations, draws the two samples and computes counts, shares and intervals from the expert's reading log. I'd need a sample of the export format, with the fields masked.