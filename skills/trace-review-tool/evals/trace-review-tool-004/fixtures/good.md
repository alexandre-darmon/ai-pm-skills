## What to change before the agent builds it

1. **Sampling leaves the app.** A separate sampling script with a fixed seed writes the list: 160 random letters and 80 targeted (thumbs-down, large settlements), with a `stream` column. The quality rate comes from the random stream only, with its Wilson interval. Loading the thumbs-down letters first over-represents failures: a rate computed on that mix is biased and is not the rate of the 12,000 letters.
2. **Pass or fail, not 1–5.** An average of 3.6 tells nobody what to fix. Each letter gets a binary label and a critique on fails, plus a "not sure" flag that never counts as pass.
3. **No GPT pre-fill.** A suggested score anchors the handler, who then mostly confirms. The handler reads first; a model judge comes later, calibrated against these labels, so the script also assigns a dev or test split now and the test labels never reach whoever writes the judge prompt.
4. **Audit fields.** Each label carries the handler's reviewer id from the company login and a timestamp, append-only, in approved storage.

## Cost

- Review: 240 letters × 3 min = 720 min = 12 hours × 70 EUR = 840 EUR.
- One run of the assistant: 9,000 tokens × 0.004 EUR per thousand = 0.036 EUR, about 432 EUR a month. Log tokens per call so this comes from the traces, not the contract. The number the committee needs is the cost per correct letter: 0.036 EUR divided by the random-stream pass rate.
