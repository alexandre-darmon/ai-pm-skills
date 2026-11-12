Your manager's plan can work, but one change is needed: a person has to read about 100 conversations first. Without that, the Friday chart will show shares nobody can defend, and it won't say what the prompt change broke.

**Problems with the plan as written**
- **The categories are guesses.** "Hallucination, incomplete, tone, off-topic" is a generic list. Complaints doubled after a prompt change, so the cause is probably specific. Examples would be fee answers that skip a condition, a card-block flow that no longer gives the phone number, or transfer limits quoted wrongly. A generic label like "incomplete" would bury that.
- **The LLM's labels are unchecked.** If it says 18% hallucination, you can't tell whether that's true. An executive committee will ask.
- **Nobody ever compares the labels with a person's judgment.** The chart would show what the LLM thinks, not what happened.
- **Personal data.** Mask names, IBANs, card numbers and the like before anyone reads a conversation or sends it to a model.

**Plan for Friday (today is Monday)**

| Day | Step | Owner |
|---|---|---|
| Mon | Mask personal data. Draw about 60 random conversations and about 40 targeted ones (complaints, escalations, long or abandoned chats). Pull the old and new prompt. | You, data team |
| Tue | The retail banking domain expert (the person who owns answer quality, not the builders) reads each conversation and writes a free-text note: what went wrong, or "pass". Aim for about 3 minutes each, so roughly half a day. Stop once about 20 in a row show nothing new. Don't use an LLM for this first reading. | Domain expert |
| Wed am | Group the notes into 4–8 failure modes. Each gets a yes/no definition, one pass example and one fail example. An LLM can suggest groupings, and the expert accepts or rewrites them. Note any mode that traces back to the prompt change. | Expert + PM |
| Wed pm | Run one yes/no judge per mode over the 5,000 conversations (prompt below). Check each judge against the expert's labels on the 100 conversations, and have the expert label about 30 more. Report agreement for each mode. Drop or caveat any judge that doesn't agree well. | PM, engineer |
| Thu | Build the dashboard. Reconcile the shares and fix anything the judges got wrong. | Engineer |
| Fri | Present. | PM |

**What the dashboard should show**
- Share per failure mode, with a confidence interval, and the judge's agreement with the expert next to each.
- Which modes started with the prompt change. If you have old-prompt conversations, compare the two periods. Otherwise cite the expert's notes.
- Expected monthly cost per mode (volume × share × cost per occurrence). Get the cost per occurrence from finance or support, and mark it "to source" if you don't have one. Don't guess it.
- Anything with legal or regulatory effect, such as wrong fee disclosures or mishandled fraud reports. Rank it high whatever its count, and raise it with compliance as a question, not a euro figure.
- A status line saying "taxonomy provisional" if you didn't reach saturation.
- Fixes: for modes caused by the prompt, revert or rewrite the prompt and re-run the failing conversations. Only build ongoing evaluators for modes the prompt doesn't explain.

**Prompt for the labelling LLM (Wednesday, one run per mode)**

Use this template after the expert has defined the modes. Don't ask the LLM for all categories at once.

```
You are reviewing one conversation between a customer and a retail
banking assistant. Personal data has been masked.

Question: does this conversation show the following failure?

FAILURE MODE: {mode_name}
DEFINITION: {binary definition written by the domain expert}
FAIL EXAMPLE: {real example, masked}
PASS EXAMPLE: {real example, masked}

Reference material (use only this to check facts):
{current fee schedule / card terms / transfer limits excerpt}

Conversation:
{conversation}

Rules:
- Judge only this failure mode. Ignore any other problems.
- If the reference material doesn't let you decide, answer "unclear".
- Quote the exact assistant sentence that supports your answer.

Reply in JSON only:
{"verdict": "fail" | "pass" | "unclear",
 "evidence": "<quote from the assistant, or empty>",
 "reason": "<one sentence>"}
```

The first reading of the conversations is the part to protect. If the LLM does it, it will bring its own idea of failure and miss the banking-specific errors that only your expert will catch.

**What I need from you to go further**
1. Who is the domain expert, and can they spare half a day on Tuesday?
2. Do you have conversations from before the prompt change, and the old and new prompts?
3. What are the feedback signals (complaint tags, escalations, thumbs-down)?
4. Is there a sourced cost for a wrong answer, such as handling time per complaint or a regulatory cost?

With the first three I can draft the sampling script, the masking checklist and the reading template, and turn the expert's notes into the failure-mode report.