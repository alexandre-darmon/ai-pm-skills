Your manager's plan is fast, but it has gaps that could make the dashboard misleading in front of the executive committee. All of them can be fixed in about the same time budget.

## Problems to fix first

1. **Nobody checks the labels.** An LLM labelling at scale is useful, but you don't know how accurate it is until you compare it to humans. Spend about 2 hours on 150 conversations, labelled by two people (or one person plus a domain expert). If the LLM agrees with them about 80% of the time or more, the chart is defensible. If it doesn't, you'll find out before Friday and not in the meeting.
2. **"Hallucination" can't be judged from the transcript alone.** The labelling LLM doesn't know your real fees, limits or transfer rules. Give it the current fee schedule and product policy text, or have it label "unverifiable claim" separately. Otherwise it will rate a confident wrong answer as fine.
3. **There's no before/after comparison.** The question is what changed with the prompt. A share-of-categories chart for last month alone doesn't answer it. Also label a similar sample from the month before the prompt change (about 5,000 more, or 1,000 if cost matters), then chart the difference.
4. **Complaints aren't connected to the labels.** Flag which conversations led to a complaint and show the label rate for complained versus not complained. That tells you which failure is driving the complaints. It may be none of your four categories.
5. **The categories should be multi-label and include "ok".** One conversation can be both incomplete and off-tone. Forcing one label distorts the shares. Add "none" and "other" so the model isn't pushed to invent a problem.
6. **Compliance.** These are banking conversations. Confirm that sending them to the LLM is approved, and redact names, account numbers and card numbers first.

## Labelling prompt

```
You are a quality reviewer for a retail bank's customer-facing assistant, which answers questions about cards, fees and transfers. You will be given one conversation and the bank's current reference material. Judge only the assistant's messages.

<reference_material>
{fee schedule, card terms, transfer rules, current as of the review period}
</reference_material>

<conversation>
{redacted transcript, with turns numbered}
</conversation>

Assign every label that applies. A conversation can have several labels, or "none".

Labels:
- hallucination: The assistant states a fact (a fee, limit, deadline, eligibility rule, process step) that contradicts the reference material, or states a specific fact that the reference material does not support. If a claim is plausible but you cannot verify it from the reference material, use "unverifiable" instead.
- incomplete: The customer's question was not fully answered, a required caveat or next step was missing, or the assistant stopped before resolving the request.
- tone: The assistant was curt, condescending, overly casual, dismissive, or ignored visible customer frustration. Do not use this for correct but unwelcome answers.
- off_topic: The assistant answered something other than what was asked, or engaged with topics outside cards, fees and transfers when it should have redirected.
- unverifiable: See above. Use sparingly.
- other_issue: A real problem that fits none of the labels (describe it).
- none: No problems found.

Rules:
- Base every label on specific evidence. Quote the assistant's exact words and give the turn number.
- Do not penalise the assistant for refusing to do something it is not allowed to do, if it explained clearly.
- If unsure between a label and "none", choose "none" and set confidence to "low".
- Do not infer what the customer felt after the conversation ended.

Return only JSON:
{
  "labels": ["..."],
  "evidence": [{"label": "...", "turn": 0, "quote": "...", "reason": "..."}],
  "confidence": "high|medium|low",
  "customer_issue_resolved": true|false|null
}
```

Run it at temperature 0. Run it twice on a subset to check that it gives the same answer.

## Plan to Friday

**Tuesday (today is 10 Nov)**
- Get approval and set up redaction.
- Pull last month's 5,000 conversations and about 5,000 from before the prompt change. Add complaint flags and the date of the prompt change.
- Collect the reference material (fee schedule and so on).

**Wednesday**
- Randomly sample 150 conversations, with extra from complained-about ones. Two people label them using the same definitions. Use the first 20 to tune the definitions.
- Run the LLM on the same 150. Calculate agreement per category, and look at the disagreements.
- Run the LLM on all 5,000 conversations, then have an expert spot-check 50 labels; tune the LLM prompt from the expert's notes.
- The LLM labelling comes after masking: strip card numbers and IBANs, then run it on all 5,000 conversations.
- Label all 5,000 with the LLM tonight. Then have a human reading the low-confidence labels first, then publish.

**Thursday**
- Run the full set (both periods) in batch. Spot-check 20 outputs for malformed JSON or missing evidence.
- Build the charts: label rate before vs. after, label rate for complained vs. not complained, and the top 10 example conversations (with quotes) for each category.
- Check whether the shift lines up with the complaint increase.

**Friday**
- Show the numbers together with the measured accuracy of the labels. For example: "LLM agreed with human reviewers 84% of the time on hallucination, 71% on tone." The committee can then judge how much weight to give each chart.
- Label tone with extra care. It's usually the least reliable category.

## Caveats for the dashboard

- Present rates as estimates, and if any category has low agreement, say so on its chart.
- If the labels show no clear change before vs. after, report that. The complaint cause may be somewhere else, such as a new policy or a product change at the same time.

I can also write the script that sends the batch to the API and calculates agreement, or the dashboard itself. Tell me where the conversation data lives and what format it's in.