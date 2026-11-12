# Interaction spec: "Send to CRM" on AI-drafted client meeting notes

**Core decision:** At L1, a Send to CRM button directly on the raw answer is the one-click path the pattern forbids. The button can still be there, and it can still save time. It has to live in the editor, and it has to stay disabled until the flagged items are resolved. What gets sent is the adviser's version, not the AI's.

## Level and pattern per step
| Step | Level | Who reads the output | Pattern | Gate to next level |
| --- | --- | --- | --- | --- |
| Draft meeting notes | L1 | Adviser (staff) | Editable draft. The adviser saves their own version to the CRM. | Not applicable. Moving to L2 needs the ladder's gate. Acceptance rate and speed don't count. |
| Save to CRM | L1 | Adviser, then the CRM record | The button sits in the editor toolbar. It is not on the answer card. | Same as above. |

## Interaction, step by step
1. **Draft arrives** in an editable editor, streamed progressively. The header reads "AI draft, not yet reviewed". **Send to CRM** is visible but disabled until generation completes. Its tooltip says "Resolve N flagged items to enable".
2. **Flagged items** are highlighted inline, with a counter ("3 to check"). Next/previous keys step through them.
3. **Each flagged item needs its own action:** confirm as-is, edit, or delete. Confirming one item is a single click on that item. There is no "confirm all".
4. **Button enables** when every flag is resolved. Edits made after that don't re-lock it unless they add new flagged content, such as a new amount.
5. **Click opens a preview.** It shows the final text, the target client and the record it will be written to, and a diff against the AI draft. It is not a "I have reviewed this" dialog. It is the destination check, and it has a single **Save to CRM** action and a Cancel.
6. **After saving,** a toast offers "View in CRM" and "Undo" (a placeholder 10-minute window, or whatever the CRM allows). The record is labelled "Drafted by AI, edited and saved by [adviser], [timestamp]".
7. **Failure** (CRM down, client not matched): the draft stays in the editor, the error names the cause, and a retry is offered. Nothing is lost.

## Review on the screen
- **Flagged for a look:**
  - Statements with no source in the transcript, labelled "not found in the transcript" and styled differently from sourced ones.
  - Amounts, dates and product names.
  - Client and third-party names.
  - Commitments and action items ("will send", "agreed to").
  - Suitability, risk or advice statements.
  - Mismatches with existing CRM fields, such as risk profile or holdings.
  - A client match with low certainty.
- **Action each needs:** confirm, edit or delete, one per item. No attestation checkbox and no confirm-everything dialog.

## Sources and confidence
- Every claim links to its transcript span, one click away, shown in a side panel.
- **No confidence score, percentage or badge.** There is no reliability table yet, so sources carry the trust.
- Once a table exists, it needs at least 100 labelled cases per bucket, with the Wilson interval. Any figure shown has to be the lower bound, in a neutral colour. Rebuild it after every model, prompt or retrieval change.

## Correction and feedback (what is logged)
- Editing inline is the correction, so no extra step is needed. An optional "why?" reason code is offered on deletes and on edits to flagged items.
- Logged: the original draft, the saved version, per-item actions, reason codes, who and when, and time in the editor.
- Corrections feed the eval set through `build-evals`. The UI says so: "Your edits help improve drafts."

## Refusal wording
- **Template:** "I can't draft notes for this meeting. [Reason: no transcript / transcript too short / client not identified]. You can [upload the transcript / pick the client / write notes manually]."
- If the draft is partial, say what is missing instead of filling it in.

## Escalation to a human
- **Conditions:** the adviser asks for support, the transcript is missing or corrupt, the client can't be matched, or the content touches a complaint or vulnerable-client marker (a policy question, see open questions).
- **Queue owner and SLA:** to be set, with placeholders for the owner (e.g. operations or compliance) and the response time.
- **When the SLA lapses:** the case goes to a fallback owner. The adviser reads "Still with [team]; escalated to [fallback]". The AI draft is never sent unreviewed.
- **Handoff summary:** adviser, client, request, what the AI found and tried, recommendation, and why it stopped.

## Decisions about people and transparency
- No decision about a person is made at this step, so the GDPR art. 22 questions don't apply at L1. If notes later drive suitability or eligibility outcomes, they go to the DPO first.
- This is a staff tool, so no AI disclosure to clients is needed in the UI. The CRM record carries the "drafted by AI, reviewed by whom" label. The provider/deployer role and any client-facing use go to `ai-act-classification` as questions.

## Latency and progressive display
- The draft streams in. A target for time to first output is a placeholder to set from your data.
- Send to CRM and the flag counter only become active when generation is complete.

## Trust signals
- **Measure:** acceptance and bypass (definitions from `assistant-kpis-cost-per-outcome`), the share of drafts edited before saving, and review time. Add the time from draft to save as the headline measure of time saved.
- **Read together:** high acceptance with short review time points to rubber-stamping. Routine bypass points to under-trust. Both are inferences to be tested.
- **Baseline and thresholds:** to be set from the team's current note-writing time, with placeholders for now.
- **Tests:**
  - Seeded errors in the live queue, withdrawn before saving, to measure the reviewers' catch rate.
  - A blind re-review of a random sample, to measure the AI's error rate in each direction.
  - Size by the rule of three: bounding a rate at 1% takes about 300 clean cases, per stratum for rare, costly categories.
- Answer over-trust on the screen, with flags, never with a badge.

## What to tell Product
- The button is possible and it saves time, but it goes in the editor and unlocks after flagged items are resolved. That keeps the time saved on typing and filing, not on checking.
- The adviser's saved version goes to the CRM, never the raw AI answer.
- A one-click send, or a "I have reviewed this" checkbox, is not an option at L1. Moving to a faster flow means moving up the ladder through its measured gate.

## Open questions (missing input, what it would change)
- **Error profile from evals:** this sets which categories get flagged, and whether any need a harder stop.
- **Reliability table:** without it, no score or badge. With it, a neutral measured-frequency line could be added.
- **Cost of an error in each direction:** a wrong fact in the CRM versus a missed one. This decides how aggressive the flagging is.
- **CRM capabilities:** whether it supports undo, and which fields or objects the notes write to.
- **Compliance rules on advice records:** whether certain notes need a second look or a retention rule, and who owns the escalation queue and its SLA.
- **Baseline for acceptance, edit share and review time:** needed before any threshold can be set.
- **Vulnerable-client or complaint markers:** whether they should block the button or route to a human.