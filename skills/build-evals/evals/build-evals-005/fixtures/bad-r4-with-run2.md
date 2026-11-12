Before deciding, find out where the ~19 failures (16% of 120) actually occur. Right now the 84% doesn't say which step is responsible.

**1. Attribute each failure to a step**

Hand-label the correct supplier, amount, VAT and due date for each failing invoice, then check:
- **OCR:** is the correct value present and legible in the OCR text? If not, it's an OCR failure, and no LLM will fix it.
- **LLM:** the value was in the OCR text but the extraction is wrong, missing or malformed.
- **Rules:** the extraction was correct but the invoice was rejected (false reject), or the extraction was wrong and the rules passed it (false accept).
- **ERP posting:** the fields were correct and valid but posting failed. Examples are supplier matching, date format, and rounding or currency.

The result is a count per step, such as "OCR 7, LLM 5, rules 4, ERP 3". Only the LLM bucket is something a model swap can fix. If it's a minority, the team's hypothesis is wrong.

**2. Measure the LLM in isolation**

- Run field-level accuracy (supplier, amount, VAT, due date) on all 120 invoices. Feed it the OCR text for the real-world number. Also run it on the PDF or image directly, to see how much OCR is costing.
- Run the same input several times to measure run-to-run variance. If the model flips between runs, a single comparison between models will be misleading.

**3. Check the downstream steps independently**

- Feed gold-labeled fields into the rules and ERP steps. Any failures there are not LLM-related.
- Check whether the rules are too strict, for example rejecting valid but unusual VAT formats or date styles.

**4. Look at the failure pattern**

Break failures down by supplier, layout, scan quality, language and currency. Failures concentrated in a few suppliers or formats usually point to OCR, rules or mapping problems, not model quality.

**5. Separate silent errors from caught errors**

An invoice rejected to human review costs minutes. A wrong amount posted without anyone noticing costs much more. Count each kind separately, because a model that is slightly more accurate but fails silently may be worse.

**6. Make the comparison trustworthy if you do test a new model**

- Use the same 120 invoices and the same OCR output, and compare per invoice (a paired test such as McNemar's).
- Be careful with small samples. 84% on 120 invoices has a 95% interval of roughly ±7 points. A swing of 3–4 invoices is noise. If the LLM bucket from step 1 is around 5 invoices, 120 invoices can't tell you much. You'd need more labeled data, especially more cases from the failure categories.
- Include cost and latency alongside accuracy.

**Recommendation:** spend a day or two on steps 1 and 2 before the sprint plan is set. If most failures are in the LLM bucket, switch and use the paired comparison to confirm the gain. If not, put the sprint effort into the step that is actually failing. A model swap costs very little to trial once you have the attribution and labeled set, so it can still be tested cheaply afterwards.

If you'd like, I can help build the per-step failure attribution sheet or the eval harness.