**Short answer:** before switching models, find out which step fails. The 84% is an end-to-end number, and it can't tell you the LLM is the weak point.

## 1. Attribute each failure to a step
This is the most important measurement.

- You have about 19 failed invoices (16% of 120). For each one, label the **first step that went wrong**: OCR, LLM extraction, business rules, or ERP posting.
- To do that, compare each step's output against a hand-labelled truth for that invoice: the correct text, the correct fields, and the correct validation verdict.
- The counts per step tell you where to work. If 3 of 19 failures are LLM extraction errors, a better model can recover at most 3 invoices (about 2.5 points). The ceiling is the same whatever model you pick.

Look for failures that the LLM only appears to cause:
- **OCR errors:** a garbled amount or a missed line on a scan gets "extracted" wrongly, and a better model can't fix it.
- **Over-strict rules:** rules that reject correct extractions, for example rounding, VAT formats, date formats, or unknown-supplier matching.
- **ERP problems:** posting rejections caused by master data, duplicate detection, or period locks.

## 2. Per-field accuracy on the LLM step
Run the LLM step on frozen OCR output stored once, so nothing upstream moves. Score supplier, amount, VAT and due date separately. Compare to the labelled truth with exact checks (field equality), not an LLM judge. Aim for 30 to 50 cases with that step labelled. A field-level breakdown shows whether the problem is, for example, only due dates or only multi-VAT-rate invoices.

## 3. Failures by invoice type
Report end-to-end results per class, not as one global number: clean digital PDFs, scans, multi-page, multiple VAT rates, foreign currency and credit notes. 120 invoices split across classes leaves few cases per class, so give the count and a 95% interval for each. For example, 5 failures out of 12 is a wide interval. The costliest error is probably a wrong amount posted as correct, not an invoice rejected for review. Treat that class separately and with a stricter bar.

## 4. Silent errors versus caught errors
The 84% mixes two very different outcomes:
- An invoice that was **rejected or sent to review** because the rules caught a bad extraction. This costs some manual time.
- An invoice that was **posted with a wrong value**. This costs money and is hard to reverse.

Count them separately. If a newer model reduces the first kind but not the second, you gain little.

## 5. Baseline and decision rule
- Freeze a baseline now. Record the model name and version, the date, and the set version.
- Write down the pass rule **before** running a candidate model, for example "end-to-end must improve by X points on the same 120, paired, with no regression on the amount-error class".
- Compare old and new **on the same invoices, paired**. With 120 cases, a difference of a few points is inside the noise.
- A component improvement doesn't ship by itself. The end-to-end score per class gates the swap.
- Keep a private holdout of about 20% so you aren't tuning to the test set.

## 6. Cost per correct posting
Compute total cost (model, review time, rework) divided by the number of invoices posted correctly. A newer model that costs more per call may still win or lose on this number.

## Practical sequence for this week
1. Hand-label ground truth for all 120 invoices: OCR text, the four fields and the expected posting.
2. Tag the first failing step on each failure.
3. Score LLM fields per field on frozen OCR output.
4. Decide from the counts. If the LLM accounts for most failures, a model trial is justified, with the rule above. If not, put the sprint into OCR, rules or ERP handling.

I can turn this into a written eval plan with the labelling template and the per-step tally sheet if you'd like.