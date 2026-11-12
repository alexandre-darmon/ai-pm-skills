Before switching models, measure where the 16% of failures actually occur. With 120 invoices that's about 19 failures, so you can inspect every one by hand.

**1. Per-stage error attribution (the key step)**

For each failed invoice, find the first stage where the output diverges from ground truth:

- **OCR**: Is the text missing, garbled or misordered? Are digits wrong (0/O, 1/l, decimal and thousand separators)? Are tables or multi-column layouts broken?
- **LLM extraction**: Was the OCR text correct but the field wrong or missing? Was a value hallucinated? Was the wrong amount picked (subtotal vs. total, or a credit note)?
- **Business rules**: Was the extraction correct but the rule rejected it wrongly? This could be a too-strict tolerance, a VAT rounding mismatch, an unknown date format, or a supplier-name match that is too exact.
- **ERP posting**: Was the validated data correct but the post failed? Look at API errors, missing supplier master data, duplicate detection, or period locks.

Also check whether the ground-truth labels are themselves wrong. That happens often in small test sets.

**2. Field-level accuracy for the LLM step in isolation**

Feed the LLM hand-corrected OCR text, so OCR errors can't affect the result. Score supplier, amount, VAT and due date separately, using exact match after normalization. This gives the LLM's real ceiling. Then compare with accuracy on real OCR output. The gap is the damage OCR does.

**3. Rules and ERP isolation**

Run the rules on gold-standard extractions. Any failure there is a rules or ERP bug that no model swap will fix.

**4. Failure type and cost**

- Split failures into silent wrong posts (bad data in the ERP) and loud rejections (routed to a human). Silent errors are far more costly, so they matter more than the raw percentage.
- Break results down by supplier, layout, language, scan quality and invoice type. Failures often cluster in a few suppliers or formats.

**5. Evidence for the model decision**

If the LLM turns out to cause a meaningful share of failures:

- Run the candidate model on the same 120 invoices, same prompt, same OCR text.
- Compare field-level results, and look at which invoices flip in each direction.
- Also measure cost, latency, and output stability across repeated runs.

**Caveats on the numbers**

- With n=120, 84% has a 95% confidence interval of roughly ±7 points (about 76–90%). A difference of a few points between models is within noise. Compare on the same invoices as a paired test, and consider enlarging the set.
- Check that the test set resembles production (supplier mix, scan quality, edge cases), and that you haven't tuned prompts on it.

**How to read the outcome**

- If most failures are in OCR, rules or the ERP, a new LLM won't help much. Spend the sprint on those stages.
- If most failures are in extraction, the model switch is justified. First check whether a prompt fix, a structured-output schema or a few-shot example would get the same gain more cheaply.

The attribution in step 1 takes a day or two by hand, and it keeps the sprint from going to the wrong stage.