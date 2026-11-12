I wouldn't send the plan as written. An unvalidated LLM label can't be defended to an executive committee, and four predefined categories may not match what's going wrong. The problem is also narrower than "label everything": complaints doubled after one prompt change, so you probably have a few specific failures, not four broad ones. Finding them takes about 100 conversations read by one person, not 5,000 labelled by a model.

## Why the original plan is risky
- **The categories come from a template, not from your data.** A bank's real failures look like "quoted the old card fee", "said a transfer is instant when it isn't", or "refused to explain the dispute process". Those all land in "hallucination" or "incomplete", and the chart can't tell you what to fix.
- **Nobody has checked the labels.** If the LLM says 18% "hallucination", you can't say whether that's 8% or 30%. The first tough question on Friday ends the dashboard.
- **Some failures matter more than their share.** Wrong fee or transfer information is a regulatory and financial risk. Tone issues are not. A share-of-categories chart weights them equally.
- **Nothing in it tests the prompt change.** You need before and after, which means conversations from before the change.

## Plan for Friday (about 3 days of effort)

**Mon: set up**
1. **Mask personal data** (names, card numbers, IBANs, phone numbers, emails) before anyone reads a conversation or it goes to a model. Ask your DPO or compliance contact whether sending logs to an external LLM is allowed.
2. **Pull two samples**:
   - **Random**: about 60 conversations from last month, stratified by topic (cards, fees, transfers). This is the only sample you can use for rates.
   - **Targeted**: about 40 from complaints, escalations, thumbs-down, and abandoned or very long conversations. This sample finds failure types, but it can't give rates.
   - If you have pre-change conversations, add about 30 random ones for the comparison.

**Tue–Wed: one expert reads**
3. **One domain expert reads each conversation and writes a one-line note.** The expert should be someone who knows the fee and transfer policies, such as a product owner or an ops lead. They write what went wrong in their own words, or "pass". Be specific: "quoted €5 fee, current fee is €3". Where several things went wrong, note the first one, since later errors are often consequences of it.
4. **Keep reading until about 20 conversations in a row show nothing new.** This usually takes 50 to 100. It's roughly half a day to a day of one person's time.
5. **Group the notes into failure types.** Here an LLM can help: give it the expert's notes and ask it to propose groupings (prompt B below). The expert accepts or rewrites each one. Each type gets a yes/no definition plus one example that passes and one that fails.

**Wed–Thu: scale up and price it**
6. **Let the LLM label the full 5,000, one yes/no question per failure type** (prompt A below). First check it against the expert's labels on about 30 conversations the expert has already coded. Report agreement per failure type. If a type is below roughly 80% agreement, either fix its definition or leave it off the dashboard and show only its hand-counted rate.
7. **Count and rank.** For each type, take the share in the random sample with a confidence interval (6 of 60 is 10%, with a range of about 5–20%). Rank by expected cost, not count. Anything with regulatory or financial effects, such as wrong fees or wrong transfer terms, goes to compliance as a question regardless of how rare it is.
8. **Decide per type: fix, evaluate or accept.** If the prompt never told the model something it needed (for example, the current fee table), that's a prompt fix, not something to measure. Compare the before/after rates to see which prompt change caused it.

**Fri: dashboard**
- Shares per failure type with their ranges, the before/after comparison, 2–3 real anonymised examples per top type, and the fix for each.
- State plainly: "Based on N hand-read conversations; LLM labels checked at X% agreement." Mark the taxonomy as provisional if you didn't reach saturation.

## Prompts

**A. Labelling prompt (use only after step 5 gives you real failure types)**
```
You are reviewing one conversation between a retail-banking assistant and a customer.
The conversation is anonymised. Today's reference documents are provided below.

<reference_documents>
{current fee table, card terms, transfer rules}
</reference_documents>

<conversation>
{conversation}
</conversation>

Failure type: {NAME}
Definition: {binary definition written by the expert}
Fails example: {example}
Passes example: {example}

Does the assistant's behaviour in this conversation meet the failure definition?
Answer only with JSON:
{"fails": true|false, "evidence": "<exact quote from the assistant's reply>", "reason": "<one sentence>"}
If you cannot tell from the conversation and the references, use {"fails": false, "evidence": "", "reason": "unclear"}.
```
Run one call per failure type. Don't ask for a single overall label or a 1–5 score. Without the reference documents, the model can't tell a wrong fee from a right one.

**B. Grouping prompt (after the expert has written notes)**
```
Below are free-text notes an expert wrote about failures in a banking assistant.
Group notes that describe the same underlying failure. For each group give:
a short name, a yes/no definition, and the note numbers it contains.
Split a note that describes two different failures. Don't invent groups
the notes don't support, and put anything that doesn't fit under "unclear".

{notes, numbered}
```
The expert reviews and rewrites the output. The LLM doesn't do the first reading.

## What I need from you
- Who is the domain expert, and can they spare about a day this week?
- Do you have conversations from before the prompt change, and which data-protection rules apply to logs?
- Can you share a sample of masked conversations and the prompt diff? I can help draft the failure definitions and set up the counting.

If the expert has no time at all, I'd tell the committee on Friday that you have a preliminary view and will deliver a validated dashboard the following week. A confident chart built on unchecked labels is the worse outcome.