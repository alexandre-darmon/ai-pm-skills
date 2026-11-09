**Don't choose on the 97%. Choose on a blind bake-off of both vendors on your 300 documents, and don't accept Vendor A's portal offer as it stands.** The decision today is "pending bake-off".

## Why the 97% doesn't carry the decision
- **It's a claim.** It was measured on Vendor A's own documents, so it says little about your invoices and medical reports. It stays "claimed" until your data reproduces it.
- **It's per field, but you pay per document.** At 97% per field and 12 fields, a document comes out fully right only about 69% of the time (0.97¹²), assuming independent errors. That leaves roughly 3 documents in 10 needing a human fix.
- **A global rate hides the weak spots.** Invoices, medical reports, accident reports and bank forms behave differently. A wrong IBAN costs far more than a wrong date.
- **Vendor B's silence isn't a weakness.** Having no published figure means B is unmeasured, not worse.

## The portal offer
- **Data.** Your set contains health data (medical reports, GDPR art. 9) and bank details. Nothing goes to any vendor until three things are in place:
  - a signed art. 28 processing agreement, or an anonymised set with the anonymisation checked on a sample;
  - known hosting locations and sub-processors, including the model provider behind the product;
  - trial terms that exclude training on your data.
- **Method.** A vendor-run portal isn't a fair test. Both vendors need the same cases, the same instructions and the same configuration time, and neither may see your keyed values. Offer B the identical test.
- **Counter-offer to A.** Say yes, once the data conditions are met, to a test where you control the scoring.

## How to run it
1. **Write the rules first, dated.** Fix the thresholds per document type, the main metric (every critical field right per document), and the decision rule before any vendor run.
2. **Check your ground truth.** Handler keying has errors too. Re-check a sample of disagreements between the vendors and the handlers' values. Score the handlers on the same cases as your baseline.
3. **Use a small tuning slice and a hidden holdout.** Give both vendors the same tuning slice, score only unseen cases, and keep a private holdout for the renewal re-test.
4. **Score per document and per field class, per document type, with Wilson 95% intervals.**
   - Bank forms (40) and accident reports (50) will have wide intervals, so treat them as indicative.
   - Gate the IBAN and other costly fields on the interval's lower bound, not the point estimate.
5. **Compare on the same cases.** Count d, the cases where exactly one vendor is right. A gap below 2√d / n is a tie. With d = 30 on 300 cases, that's about 3.7 points. A tie is settled on cost, data terms and exit rights, never on the higher point estimate.
6. **Record versions and dates.** Note each vendor's product and model version and the run date.

## Cost
I don't have your handler cost, so I've used licence and integration only.

| | A | B |
|---|---|---|
| Licence at 85,000 docs/yr | 38,250 € | 25,500 € |
| 3-year total with integration | about 174,750 € | about 151,500 € |

B is about 23,000 € cheaper over three years, and its higher integration cost is recovered in about 14 months. That is before human time, which is the larger term.

- **Today's baseline:** 85,000 × 4 min is about 5,700 handler-hours a year.
- **Human time scales with quality.** If the product runs with every output reviewed, review and correction time depend on the error rate. The 0.15 € price gap is only a few seconds of handler time per document. A few points of document-level accuracy outweigh it.
- **The figure to compare** is cost per correct document: total cost, including review and correction, divided by documents × measured fully-correct rate. Never divide by documents processed.

## Contract and compliance (record as present, claimed or missing)
- **Blocking if absent:**
  - no training on your data, binding sub-processors too;
  - written notice before any model change, with the right to re-run your eval set and to exit without penalty;
  - access to logs and per-request traces;
  - the processing agreement, named processing locations and a sub-processor list;
  - exit terms: data returned, deletion certified, a transition period.
- **DORA:** as an insurer you're a financial entity. Check the register-of-information entry, whether this supports a critical or important function, concentration and subcontracting risk, the art. 30 clauses, termination rights and a tested exit plan.
- **AI Act:** ask each vendor for its instructions for use with declared accuracy levels, and for its conformity documents if the system is high-risk. Pass the classification question to counsel.
- **Negotiable:** a quality service level measured on your eval set, with credits and a termination right.

## Next steps
1. Tell procurement the 97% is a claim and the decision waits for the bake-off.
2. Get the DPA, hosting and sub-processor answers from both vendors, or anonymise the 300 documents.
3. Write the thresholds and decision rule, then run both vendors blind.
4. Send me the per-case results as a CSV with columns `case_id,class,A,B,handlers` (1 or 0). I'll compute the intervals, the paired gap and the cost per correct document.
5. Give me your loaded handler cost per hour and your review model (every output checked, or only flagged ones). Then I can complete the cost comparison.

This evaluation is a checklist for counsel and procurement, not a compliance assessment.