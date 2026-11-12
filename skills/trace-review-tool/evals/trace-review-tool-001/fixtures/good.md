# Review app brief: complaints-reply drafts

**Decision fed.** 300 drafts read by three senior officers, labels feed an error analysis before the card disputes extension. Owner: PM. Kill date: four weeks from today.

**Data in.** The app reads a JSONL file from the logging platform, never production. Customer names, account numbers, addresses and phone numbers are masked in the export step with typed, consistent placeholders (`<CUSTOMER_1>`, `<IBAN_1>`), so the app never holds raw personal data. Masked drafts are still personal data, so the app is entered as an ICT asset at its end-user computing tier before it loads them. Before the officers start, a second person reads all 300 masked traces, free text first, for residual leaks: zero leaks in 300 still allows up to about 1%.

**Sampling script, separate from the app.** A small script with a fixed seed draws the 300: 200 random, in proportion to complaint type, and 100 targeted (complaints reopened, drafts the officer rewrote heavily, the rare regulatory complaints). The rate of each failure comes from the random stream only, with its Wilson interval.

**Screen.** One complaint per screen: complaint text, the draft, the final letter sent, the prompt version. Pass or fail, with a free-text critique mandatory on a fail. No 1–5 score.

**Audit fields.** Every label row holds `trace_id, label, critique, reviewer_id` (from the company login, not a typed name), `labelled_at` timestamp in UTC, app version and sample version. Append-only: a change is a new row. The app refuses to save without a reviewer id.

**Storage.** Labels go to an approved internal database with an access list, not on a laptop or in browser storage.

**Officers' edits.** The diff between draft and final letter sent is a human override: capture it per trace, it is the cheapest signal of what the drafts get wrong.

**Exports.** `trace_id,stream,class,mode,critique,reviewer_id,labelled_at` for the error analysis; `trace_id,split,human` for a later judge calibration.

**Smoke test.** 10 known traces through load, label, save, export, re-import; a fresh session reviews the agent's code.

**Review cost.** 300 drafts × 2 min = 600 min = 10 hours of officer time × 85 EUR = 850 EUR, about 3.3 hours each over two weeks.

**For counsel and the DPO.** Retention of traces and labels; whether the app needs registering as an end-user tool.
