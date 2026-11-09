Don't switch models yet: 84% end to end says something fails, not which step.

1. **Keep the end-to-end score as the release gate.** It is what accounts payable lives with, per invoice type, with its interval (120 invoices: roughly 76% to 89%).
2. **Add an eval per step.** Label 30 to 50 invoices at each step: OCR text against the PDF, each extracted field against the true value, each validation-rule verdict, each ERP posting. Score the unit the business pays for: an invoice fully right, not a field.
3. **Label the first failing step** on the 19 failed invoices. If most first go wrong at OCR (rotated scans, stamps over the amount), a new LLM will not help.
4. **Score extraction on frozen OCR output**, stored once, so a change in OCR does not move the extraction score at the same time.
5. **Before any swap, run old and new extraction on the same invoices** and compare paired: a gap under 2√d / n, with d the invoices where only one model is right, is a tie, and a tie goes to the cheaper model.
6. Then re-run end to end before release.
