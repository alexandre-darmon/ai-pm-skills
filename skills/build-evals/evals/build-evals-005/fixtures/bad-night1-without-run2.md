Before choosing a fix, find out where the 16% of failures actually occur. A model swap only helps if the LLM step is the main source.

**1. Label each failure by the first step that went wrong.**
For each of the ~19 failed invoices, work through the steps in order:
- **OCR:** Is the text wrong, missing or misordered? Common causes are bad scans, tables, multi-column layouts and stamps. Check this against the PDF itself, not just the extracted text.
- **LLM extraction:** Was the OCR text correct but the field wrong? Compare each field (supplier, amount, VAT, due date) to a hand-labeled ground truth.
- **Business rules:** Did the extraction match ground truth but get rejected anyway, or accepted when it should have been flagged? Examples are rounding tolerances, date formats, supplier-matching rules and VAT-rate checks.
- **ERP posting:** Was a correct, validated record rejected or posted to the wrong place? Examples are supplier ID mapping, duplicate detection, period locks and API errors.

Count failures per step. Don't attribute a failure to the LLM just because the final field was wrong, because OCR errors show up as LLM errors.

**2. Measure the LLM step in isolation.**
- Feed it ground-truth text (clean text, or OCR output that you've corrected by hand) and score field-level accuracy. This is the model's ceiling.
- Feed it the real OCR output and score again. The gap between the two numbers is the cost of OCR noise.
- Break results down by field. Amount and VAT errors, date-format confusion, and picking the wrong supplier (e.g. remit-to vs. bill-to) have different fixes.

**3. Check whether the failures are really failures.**
- Is "posted correctly" judged by a human or by the pipeline's own checks? Silent wrong postings are worse than rejections.
- Separate false rejections (a good invoice blocked) from wrong acceptances (a bad one posted). They have different costs.
- Check whether the ground truth is itself right. Labeling errors are common in small sets.

**4. Check the sample.**
- 120 invoices gives a wide margin: 84% is roughly ±7 points at 95% confidence. Differences of a few points between two models won't be distinguishable.
- Check whether the set matches production in supplier mix, languages, scan quality and invoice layout. Include the long tail.
- Check whether prompts were tuned on these same 120. If so, the 84% is optimistic.

**5. If the LLM does turn out to be the weak point, compare models fairly.**
- Run old and new models on the same invoices with the same prompt. Then try a prompt adapted to the new model.
- Use structured output or schema validation, and compare cost, latency and variance across repeated runs.
- Pre-register the decision threshold, e.g. "switch if field accuracy improves by X points or end-to-end by Y".

**What the results would tell you**
- If most failures are OCR, better OCR, higher-resolution rendering, or sending the PDF image directly to a vision-capable model, will help more than a new text model.
- If most are rule or ERP failures, fix those. They are deterministic and cheap to fix.
- If most are LLM failures even on clean text, the model switch is justified. Then check whether the errors are ambiguity (needing prompt or schema changes) or real capability gaps.

The failure-by-step table can be built in an afternoon by hand, which is cheap enough to do before committing a sprint to the model swap.