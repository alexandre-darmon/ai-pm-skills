Before you decide, find out where the 16% of failures come from. That's about 19 of your 120 invoices, and right now nobody has shown which step caused them.

**1. Attribute each failure to the first step that went wrong**

Hand-label the correct supplier, amount, VAT and due date for all 120 invoices. Then, for each of the ~19 failures, check each step in order:
- **OCR:** is the correct value present in the OCR text? Look for dropped digits, swapped decimal and thousands separators, and mangled tables or multi-page layouts.
- **LLM:** if the value is in the OCR text, did the LLM extract it correctly?
- **Business rules:** were the extracted fields correct but the rules rejected them? Typical causes are VAT tolerance, date formats or duplicate checks.
- **ERP posting:** were the fields and validation fine but posting failed? Typical causes are supplier master-data mismatch, closed periods or missing GL mappings.

The LLM's share of those 19 is the most you can gain from swapping it. If it's 5 of 19, the ceiling is about 4 points of the 16 lost.

**2. Run the LLM in isolation**

- Score field-level accuracy per field (supplier, amount, VAT, due date), not just whole-invoice accuracy.
- Run it on clean text, such as the PDF's text layer or a human transcription, and on your real OCR output. The gap between the two is the OCR's contribution.

**3. Look at how the rules treat errors**

- When the LLM is wrong, do the rules catch it and route to manual review (a safe failure), or does the bad value get posted (a silent failure)? These have very different costs.
- Do the rules reject correct extractions (false rejections)?
- Check whether failures are "not posted" or "posted wrong". Count them separately and weight by business impact.

**4. Check that the test set and the comparison are sound**

- With 120 invoices, 84% has roughly a ±6.5-point confidence interval. A model that scores 88% on the same set may not be better.
- Compare the old and new models on the same invoices (paired). Count how many invoices each model gets right that the other gets wrong, and run each model a few times to measure run-to-run variance.
- Check whether the set covers your real mix: scanned vs digital PDFs, languages, layouts, credit notes, multi-currency, and your top suppliers by volume.
- Also compare cost and latency, since a newer model may differ on both.

**A cheap test you can run now**

Cache the existing OCR outputs, run the new model on them offline, and score field by field against your labels. That takes a day or two, not a sprint. If the new model fixes few of the LLM-attributed failures, you've saved the sprint. If it fixes most of them, you have evidence to switch.

I can help build the failure-attribution sheet or the offline comparison harness if you share the pipeline code or the results.