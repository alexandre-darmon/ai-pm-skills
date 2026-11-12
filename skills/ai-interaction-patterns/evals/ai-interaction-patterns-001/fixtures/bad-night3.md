# Spec: "Send to CRM" on AI-drafted meeting notes

**Assumptions** (tell me if any are wrong):
- "L1" is the first-line surface where the draft appears.
- The CRM note becomes part of the client record, which is likely a regulated, auditable record.
- The adviser is the author of record, not the AI.

## Design principle
The button saves clicks, not review. A draft must not reach the CRM without the adviser having had a chance to read and edit it. The speed-up comes from removing navigation, copy/paste, and client-matching work.

## Placement
- A primary action in the footer of the draft card: **Send to CRM**. Next to it are **Copy** and **Edit**.
- The label stays the same in every state, and the state shows in the button's adjacent status text.
- The button is on the draft only. It doesn't appear on other AI answers.

## States

| State | Button | Notes |
|---|---|---|
| Draft generating | Hidden | Streaming is still in progress. |
| Draft ready, unedited | Enabled | See "Review gate" below. |
| Draft edited | Enabled | A small "Edited" tag shows. |
| Client not matched | Enabled, opens the picker | Opens the client picker before anything is sent. |
| Sending | Disabled, spinner, "Sending…" | Blocks double-submit. |
| Sent | Replaced by "Sent to CRM · [time] · View in CRM" | Link opens the CRM record. Offers "Send update" if the draft is edited afterward. |
| Failed | Enabled, inline error plus **Retry** | The draft is never lost. |
| No permission or no CRM link | Disabled with tooltip explaining why | Say who to contact. |

## Flow
1. **Click Send to CRM.** A confirmation sheet opens (a popover, not a full modal). It isn't skipped.
2. **The sheet shows:**
   - **Client:** pre-filled from the meeting or calendar match. Shows name plus an identifier (such as the last 4 digits of the account number) to prevent wrong-client errors. It's editable.
   - **Note type and date:** pre-filled (e.g. Meeting note, meeting date). Editable.
   - **Preview:** the exact text that will be saved, with an inline edit option.
   - **Attribution line:** "Drafted with AI, reviewed by [Adviser name]". This is written into the CRM record. Check whether compliance requires it. I'd assume yes.
   - **Checkbox:** "I have reviewed this note for accuracy". It's required, and unchecked by default.
3. **Click Confirm and send.** The button is disabled until the checkbox is ticked and the client is set.
4. **On success,** the sheet closes. The card shows the Sent state and a toast "Saved to [Client]'s record" with an **Undo** link for about 10 seconds. If the CRM API supports it, Undo deletes or voids the note. If it doesn't, drop Undo and don't promise it.
5. **On failure,** the sheet stays open and shows the error with Retry. Preserve all edits.

## Review gate
- If the draft contains items the AI is unsure of or that are high-risk (numbers, product recommendations, commitments, suitability statements), highlight them in the preview. The adviser doesn't have to resolve each one, but they should be visible.
- Don't allow a one-click send with no review step. If the team wants a faster path later, add a "Don't ask again for this client" option only after compliance signs off.

## Behaviors and edge cases
- **Idempotency:** each send carries a draft ID and version. A retry or double-click can't create duplicate notes.
- **Edit after send:** shows "Send update", which edits or appends to the existing CRM note. It doesn't create a second note. Show a diff-style summary in the confirmation.
- **Multiple matched clients** (joint meetings): the picker allows multi-select, with one note per client or one note linked to several, depending on what the CRM supports.
- **Sensitive content:** if the draft includes anything on a restricted category list (e.g. health or vulnerability notes), show a warning in the sheet. Do not auto-redact.
- **Session timeout or offline:** keep the draft locally and show "Not sent, reconnect to retry".
- **Keyboard and accessibility:** the sheet is focus-trapped, Esc cancels, Enter confirms only when the checkbox is focused or valid. Status changes are announced via `aria-live`.

## Audit and analytics
- **Log, for audit:** who, when, which client, draft version, final text, whether it was edited, and the AI model/version.
- **Track, for product:** send rate, edit-before-send rate, time from draft to send, failure rate, undo rate, and wrong-client corrections. The edit rate and undo rate tell you whether the draft quality and the review step are working.

## Open questions
1. Does the CRM API support updates, deletes and voids? This decides whether Undo and Send update are possible.
2. Does compliance require the AI attribution and the review checkbox? I've assumed yes.
3. Who owns client matching if the calendar match is wrong or missing?
4. Is there a retention rule on drafts that were never sent?

I can turn this into a Figma-ready screen list or user stories with acceptance criteria if you'd like.