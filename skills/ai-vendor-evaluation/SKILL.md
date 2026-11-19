---
name: ai-vendor-evaluation
description: 'Choose or renew a bought AI product or vendor (copilot, chatbot, document AI) on your own bake-off, cost per correct outcome and contract terms. Use for an RFP, a vendor demo or claim, a renewal.'
license: CC-BY-4.0
metadata:
  stage: "evaluate"
  version: "0.2.4"
  status: "tested"
  eval_threshold: "0.90"
  legal: "true"
  last_verified: "2026-11-09"
  autonomy_relevant: "true"
  depends_on: "build-evals"
  feeds: "ai-act-classification, production-evals-monitoring, model-card-ai-registry"
  sources: "dora, gdpr, eu-ai-act, eu-digital-omnibus-ai, miller-error-bars, wilson-interval, zhu-agentic-benchmarks, zhang-gsm1k, repo-yoseph, own-vendor-selection"
---

# ai-vendor-evaluation

## When to use
- An RFP or a shortlist for an AI product: a copilot, a chatbot platform, a document-AI product, a model API bought under a vendor contract.
- A vendor demo, a reference customer or a claim such as "97% accuracy" is on the table, and someone wants to decide on it.
- A renewal, a price change, or a new model under a product you use.
- Not to pick a foundation model for a system your team builds and tests itself (`model-selection`), nor to classify the product under the AI Act (`ai-act-classification`).

## Inputs
Mandatory: the use case and the outcome the business pays for (a claim file keyed without correction, an answer accepted); the candidates, with the current process or product as the line to beat; the eval cases and per-class thresholds from `build-evals`; whether the buyer is a financial entity under DORA (bank, insurer, investment firm, payment institution); what data the product will see (personal, health or other special-category, confidential).
Ask if missing: volume; prices; review and correction times; the autonomy level (references/autonomy-ladder.md); the draft contract and data-processing terms; the renewal date.
No eval cases yet: build them first (`build-evals`); a bake-off on the vendor's samples, or on cases written after seeing outputs, proves nothing.

## Method
Clause details and articles: references/vendor-checks.md. Statistics: references/eval-statistics.md. Evidence rules: references/evals-as-evidence.md.

1. **Fix the evidence rule before any demo.** A vendor's benchmark, demo, reference customers and declared accuracy are claims measured on someone else's data. Record each with its source as *claimed*; it stays claimed until your bake-off measures it. Before a benchmark score gets any weight, audit it (references/vendor-checks.md, Benchmark audit). Write the per-class thresholds, the primary metric, the scorecard weights and the decision rule, dated, before the first vendor run.
2. **Clear the data path before any upload.** No personal or confidential data reaches a trial, a sandbox or a vendor portal until: a processing agreement under GDPR art. 28 is signed, or the trial set is anonymised and the anonymisation checked on a sample (pseudonymised data are still personal data); hosting and processing locations are known (EU, or a transfer basis under GDPR Chapter V); sub-processors are listed, including the model provider behind the product; and the trial terms exclude training on your data. Health data in claims or HR files are special-category data (art. 9): the bar is higher. State the gate as one sentence procurement can forward ("no document reaches the trial until ...").
3. **Design a blind bake-off on your own cases.** Same cases, inputs, configuration time and instructions for every vendor, and the current process scored on the same cases as the baseline. Vendors never see the expected outputs. Allow the same small tuning slice for all; score only unseen cases, and keep a private holdout for the renewal re-test. Run a generative product at least twice per case. Record product version, model version and run date, or the score cannot be compared later.
4. **Score the unit the business pays for, per class, with intervals.** A field-level rate is not the outcome: 12 fields at 97% each give a fully right document about 69% of the time if errors are independent (0.97^12). Score per document (every critical field right) and per document type, never one global rate; the document, not the field, is the unit of the interval (references/eval-statistics.md §1). Give each class its Wilson 95% interval; mark classes under about 30 cases as indicative; for a costly class (an IBAN that pays the wrong account), gate on the lower bound.
5. **Compare vendors on the same cases.** Count d, the cases where exactly one vendor is right. A gap smaller than 2√d / n is a tie; state both in points (d = 9 on n = 60 gives 10 points). A tie is decided on cost per correct outcome and the data, contract and exit criteria, never on the higher point estimate. The noise is not a cap on the true gap, which can lie anywhere from about gap − noise to gap + noise: check the cost decision across that whole range and say where it would flip. Results not split by class: ask for the split and make the decision conditional on it. Put each vendor's declared accuracy next to your interval for the same class: a claim above the interval is recorded as *not reproduced*.
6. **Compute the total cost and the cost per correct outcome** (references/roi-model.md): licences, usage at your volume, integration spread over the contract term, and human time: review of each output at the product's autonomy level plus correction of each error. Leaving review out because nobody gave a figure understates every vendor; when times or the autonomy level are missing, use a labelled assumption the reader can replace, and claim no line dominates until real figures exist. Cost per correct outcome = total cost ÷ (volume × share the product got right before any human correction), never ÷ documents processed; say so in one line, since after correction every unit is right. Give the break-even quality gap on the metric that decides: the gap that equalises cost per correct outcome is smaller than the one that equalises total cost. Recompute at every price change.
7. **Collect the AI Act documents; do not judge them.** The vendor is usually the provider, you the deployer. Most duties attach only to a high-risk system and the classification is not made yet, so write each as conditional ("if classified high-risk"); stating it as applying overstates the law. Ask in any case for the instructions for use with the declared accuracy and metrics (arts. 13(3)(b)(ii), 15(3)) and the pre-determined changes (art. 13(3)(c)): they are the vendor's own statement of what the product does. If high-risk: the declaration of conformity (art. 47), the registration (art. 49), and your deployer duties (art. 26, logs kept at least six months), one more reason the contract must give you the logs. Give the Annex III date (2 December 2027, Regulation (EU) 2026/1744) only where the product may be high-risk. Record each document as *on file* (link), *claimed*, *requested* (not yet seen) or *not due yet*; *missing* only once the vendor says it does not exist.
8. **For a financial entity, run the DORA checks** (Regulation (EU) 2022/2554): an entry in the register of information (art. 28(3)); whether the service supports a critical or important function, your entity's call (art. 28(4)(a)); concentration and subcontracting risk, the model provider and third-country law included (art. 29); the clauses of art. 30(2) and, for a critical or important function only, art. 30(3) (quantitative service levels, notice of developments, audit, exit with a transition period); termination rights (art. 28(7)); a tested exit strategy (art. 28(8)). Record each clause as present or missing; whether the whole is enough is counsel's call.
9. **Write the clauses that keep the evidence alive after signature.** Must-have, blocking if absent:
   - no training, fine-tuning or improvement of any model on your inputs, outputs, feedback or eval set, written in the contract and binding sub-processors;
   - written notice before any change of model, model version or component that can change outputs, the right to re-run your eval set on the new version before the switch, to stay on the tested version meanwhile, and to exit without penalty if it misses your thresholds;
   - access to logs and per-request traces (input, output, model version, timestamp) for your monitoring and deployer duties;
   - the processing agreement, named processing locations, sub-processor list with notice and a right to object;
   - exit: your data, configurations and eval results returned usable, deletion certified, a transition period.

   Always propose, even where negotiable (DORA art. 30(3) makes it mandatory for a critical or important function): a quality service level on your metric measured on your eval set (per class, quarterly sample) with credits and a termination right; without it the eval set binds no one after signature. Negotiable: running your eval set at any time at no cost; incident notice times; price protection on a model change.
   A contract that allows silent model changes or training on your data is not signed as drafted: mark it *blocking*, name the clause to add and who negotiates it. A go-ahead under deadline pressure carries its condition in the same sentence ("sign only once <blocking clause> is replaced"); a blocking item is never traded for an exit right. A go-ahead needs your own scored results against thresholds, or a contract term that makes the commitment depend on them. Say what can be sent by the deadline, not that the negotiation will end by it.
10. **Score and record the decision.** Blocking items are gates, not points; the weighted criteria come after. The decision record holds the date, the cases version, the vendors with their versions, results per class with intervals, the paired gap against its noise, cost per correct outcome, open blocking items, the decision line, a re-evaluation date and its triggers (a new model or version, an incident, a price change, a drop in production quality). Use only dates the user gave, or a placeholder (an invented "today" reads as fact); set the re-evaluation relative to signature or the renewal notice. Hand over monitoring, classification and inventory (Links).

## Output
`templates/vendor-evaluation.md`, all headings present. The decision line reads `Selected vendor: <name>`, `Selected vendor: pending bake-off` or `Selected vendor: none (blocking: <item>)`. The document ends with: "This evaluation is a checklist for counsel and procurement, not a compliance assessment."
In a chat answer, the reader has none of this skill's files, scripts or skill names: show the computed numbers and say each step in plain words, a line or two per item. Cover what the decision still needs. A check the user says is done (data path, contract terms) with nothing shown is recorded as *claimed* ("stated by you, document to file") in one line, without re-listing the whole gate; the decision record names the signed processing agreement and contract clauses by reference. A chat answer that skips the template still gives: the decision line in those words; each claim's status; the data gate and the blocking clauses (one line each when stated as done); the quality service level; the AI Act and DORA documents to request; a re-evaluation point with its triggers; a short list headed "Questions for counsel"; and the closing line.

## Rules and red lines
- Never select or rank a vendor on its own benchmark, demo, reference customers or declared accuracy.
- Never send personal or confidential data to a trial before a processing agreement and a hosting check, or before anonymising it.
- Never recommend signing a contract that allows silent model changes or training on customer data without flagging it as blocking.
- A gap under 2√d / n is a tie, never a win, and never justifies the costlier vendor.
- Never state that a vendor, a product or a contract is "AI Act compliant", "DORA compliant" or "GDPR compliant": that is counsel's finding, not the buyer's. Record documents and clauses by status, and word questions for counsel as "whether ..." so none reads as a finding.
- Cost per correct outcome divides by correct business outcomes, never by documents or calls processed: dividing by volume hides the errors.
- Every decision record has a date, versions, a re-evaluation date and its triggers: a vendor's model changes after signature.

## Links
references/vendor-checks.md · references/eval-statistics.md · references/evals-as-evidence.md · references/roi-model.md · references/autonomy-ladder.md · scripts/bakeoff.py · build-evals · model-selection · ai-act-classification · production-evals-monitoring · model-card-ai-registry

## Sources
- dora: arts. 28–30, register, concentration, clauses, exit.
- gdpr: art. 28 and 28(10), art. 9, Chapter V.
- eu-ai-act: arts. 13, 15, 26, 47, 49.
- eu-digital-omnibus-ai: the amended Annex III date.
- miller-error-bars: paired differences; clustering.
- wilson-interval: per-class intervals with few cases.
- zhu-agentic-benchmarks, zhang-gsm1k: benchmark audit (references/vendor-checks.md).
- repo-yoseph: vendor oversight after purchase.
- own-vendor-selection: bake-offs, cost per correct outcome, evidence-keeping clauses at banks and insurers.
