---
name: ai-vendor-evaluation
description: 'Choose or renew a bought AI product or vendor (copilot, chatbot, document AI) on your own bake-off, cost per correct outcome and contract terms. Use for an RFP, a vendor demo or claim, a renewal.'
license: CC-BY-4.0
metadata:
  stage: "evaluate"
  version: "0.2.0"
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
- A renewal is due, or the vendor changes its price.
- A vendor announces a new model or version under a product you already use.
- Procurement wants to sign an AI contract and asks what to check first.
- Do not use to pick a foundation model for a system your own team builds and tests on its own suite: that is `model-selection`.
- Do not use to classify the product under the AI Act: that is `ai-act-classification`; this skill only collects the vendor's documents.

## Inputs
Mandatory: the use case and the outcome the business pays for (a claim file keyed without correction, an answer accepted); the candidates, with the current process or product as the line to beat; the eval cases and per-class thresholds from `build-evals`; whether the buyer is a financial entity under DORA (bank, insurer, investment firm, payment institution); what data the product will see (personal, health or other special-category, confidential).
Ask if missing: volume per year; prices (licence, usage, integration); review time per output and correction time per error; the autonomy level the product will run at (references/autonomy-ladder.md); the draft contract and the vendor's data-processing terms; the renewal date.
No eval cases yet: build them with `build-evals` before any vendor run. A bake-off on the vendor's sample documents, or on cases written after seeing the vendors' outputs, proves nothing.

## Method
Clause details and articles: references/vendor-checks.md. Statistics: references/eval-statistics.md. Evidence rules: references/evals-as-evidence.md.

1. **Fix the evidence rule before any demo.** A vendor's benchmark, demo, reference customers and declared accuracy are claims measured on someone else's data. Record each with its source as *claimed*; it stays claimed until your bake-off measures it. Before a vendor's or a public benchmark score gets any weight, audit it (references/vendor-checks.md, Benchmark audit): a do-nothing answer and a known-wrong answer run through its grader must both fail, or the score measures the grader; contamination is the gap between the public set and a fresh matched set of your own. Write the per-class thresholds, the primary metric, the scorecard weights and the decision rule, dated, before the first vendor run.
2. **Clear the data path before any upload.** No personal or confidential data reaches a trial, a sandbox or a vendor portal until: a processing agreement under GDPR art. 28 is signed, or the trial set is anonymised and the anonymisation checked on a sample (pseudonymised data are still personal data); hosting and processing locations are known (EU, or a transfer basis under GDPR Chapter V); sub-processors are listed, including the model provider behind the product; and the trial terms exclude training on your data. Health data in claims or HR files are special-category data (art. 9): the bar is higher. Until then the bake-off waits or runs on anonymised cases.
3. **Design a blind bake-off on your own cases.** Same cases, same inputs, same configuration time and the same instructions for every vendor, and the current process scored on the same cases as the baseline. Vendors never see the expected outputs. Allow configuration on a small tuning slice, the same for all; score only cases they have not seen, and keep a private holdout for the renewal re-test (a regression suite, references/eval-statistics.md §14). For a generative product, run each case at least twice: outputs vary. Record each vendor's product version, model version and run date: a score without them cannot be compared later.
4. **Score the unit the business pays for, per class, with intervals.** A field-level rate is not the outcome: a document of 12 fields at 97% per field is fully right only about 69% of the time if errors are independent (0.97^12). Score per document (every critical field right) and per field class, per document type, never as one global rate. The document is the unit of the interval, not the field: fields of one document share its scan and layout (references/eval-statistics.md §1). Give each class its Wilson 95% interval; mark classes under about 30 cases as indicative; for a costly class (an IBAN that pays the wrong account), gate on the lower bound.
5. **Compare vendors on the same cases.** Count d, the cases where exactly one vendor is right. A gap smaller than 2√d / n is a tie; state both in points (d = 9 on n = 60 gives 10 points). A tie is decided on cost per correct outcome and the data, contract and exit criteria, never on the higher point estimate; if the decision needs a finer comparison, add cases first. Put each vendor's declared accuracy next to your interval for the same class: a claim above the interval is recorded as *not reproduced*.
6. **Compute the total cost and the cost per correct outcome** (references/roi-model.md): licences, usage at your volume, integration spread over the contract term, and human time, meaning review of each output at the product's autonomy level (at L2 every output is reviewed) plus correction of each error. Cost per correct outcome = total cost ÷ (volume × measured quality of the business unit from step 4), never ÷ documents or calls processed. Write the price assumptions next to the figure; recompute at every price change.
7. **Collect the AI Act documents; do not judge them.** The vendor is usually the provider, you the deployer; hand the classification to `ai-act-classification`. Ask for, and record as *on file* (link), *claimed* or *missing*: the instructions for use with the declared accuracy levels and metrics (arts. 13(3)(b)(ii), 15(3)) and the pre-determined changes (art. 13(3)(c)); for a high-risk system, the EU declaration of conformity (art. 47) and the registration (art. 49). Annex III provider duties apply from 2 December 2027: ask what exists today. Your deployer duties stay yours whatever the vendor says (art. 26: use per the instructions, oversight, monitoring, logs kept at least six months under 26(6)), so the contract must give you the logs.
8. **For a financial entity, run the DORA checks** (Regulation (EU) 2022/2554): an entry in the register of information (art. 28(3)); whether the service supports a critical or important function, which is your entity's call (art. 28(4)(a)); concentration and subcontracting risk, the model provider behind the product and third-country law included (art. 29); the mandatory clauses of art. 30(2) and, for a critical or important function, art. 30(3) (precise quantitative service levels, notice of developments that affect the service, unrestricted access, inspection and audit, exit with a transition period); termination rights (art. 28(7)); a documented, tested exit strategy (art. 28(8)). Record each clause as present or missing in the draft; whether the whole is enough is for counsel and the risk function.
9. **Write the clauses that keep the evidence alive after signature.** Must-have, blocking if absent:
   - no training, fine-tuning or improvement of any model on your inputs, outputs, feedback or eval set, written in the contract and binding sub-processors;
   - written notice before any change of model, model version or component that can change outputs, the right to re-run your eval set on the new version before the switch, to stay on the tested version meanwhile, and to exit without penalty if it misses your thresholds;
   - access to logs and per-request traces (input, output, model version, timestamp) for your monitoring and deployer duties;
   - the processing agreement, named processing locations, sub-processor list with notice and a right to object;
   - exit: your data, configurations and eval results returned in a usable format, deletion certified, a transition period.

   Always propose, even where negotiable (DORA art. 30(3) makes it mandatory for a critical or important function): a quality service level on your metric measured on your eval set (per class, quarterly sample) with credits and a termination right; without it the eval set binds no one after signature. Negotiable: the right to run your eval set at any time at no extra cost; incident notice times; price protection on a model change.
   A contract that allows silent model changes or training on your data is not signed as drafted: mark it *blocking*, name the clause to add and who negotiates it.
10. **Score and record the decision.** Blocking items are gates, not points; the weighted criteria come after. The decision record holds the date, the cases version, the vendors with their versions, results per class with intervals, the paired gap against its noise, cost per correct outcome, open blocking items, the decision line, a re-evaluation date and its triggers (a new model or version, an incident, a price change, a drop in production quality). Hand over: monitoring after purchase to `production-evals-monitoring`, the classification to `ai-act-classification`, the inventory entry to `model-card-ai-registry`.

With per-case results in a CSV (`case_id,class,<vendor>...`, values 1 or 0), `python3 scripts/bakeoff.py results.csv --volume 25000 --cost A=150000 --cost B=90000` prints per-class Wilson intervals, each pair's gap against 2√d / n, and cost per correct outcome.

## Output
`templates/vendor-evaluation.md`, all headings present. The decision line reads `Selected vendor: <name>`, `Selected vendor: pending bake-off` or `Selected vendor: none (blocking: <item>)`. The document ends with: "This evaluation is a checklist for counsel and procurement, not a compliance assessment."
A chat answer that skips the template still gives: the decision line in those words; each claim's status; the data gate; the blocking clauses and the quality service level; the AI Act and DORA documents to request; a short list headed "Questions for counsel"; and the closing line.

## Rules and red lines
- Never select or rank a vendor on its own benchmark, demo, reference customers or declared accuracy.
- Never send personal or confidential data to a trial before a processing agreement and a hosting check, or before anonymising it.
- Never recommend signing a contract that allows silent model changes or training on customer data without flagging it as blocking.
- A gap under 2√d / n is a tie, never a win, and never justifies the costlier vendor.
- Never state that a vendor, a product or a contract is "AI Act compliant", "DORA compliant" or "GDPR compliant": record documents and clauses as on file, claimed or missing, and list questions for counsel.
- Cost per correct outcome divides by correct business outcomes, never by documents or calls processed.
- Every decision record has a date, versions, a re-evaluation date and its triggers.

## Links
references/vendor-checks.md · references/eval-statistics.md · references/evals-as-evidence.md · references/roi-model.md · references/autonomy-ladder.md · scripts/bakeoff.py · build-evals · model-selection · ai-act-classification · production-evals-monitoring · model-card-ai-registry

## Sources
- dora: arts. 28–30, register of information, pre-contract assessment, concentration and subcontracting risk, mandatory clauses, termination and exit.
- gdpr: art. 28 processing agreement and sub-processors, art. 28(10) a processor that sets its own purposes, art. 9 special categories, Chapter V transfers.
- eu-ai-act: what a deployer can ask the provider for (arts. 13, 15, 47, 49), deployer duties (art. 26), substantial modification (art. 43(4)).
- eu-digital-omnibus-ai: the amended application date of the Annex III duties.
- miller-error-bars: paired differences between two systems on the same cases; clustering when cases share a source.
- wilson-interval: an interval per class that holds with few cases.
- zhu-agentic-benchmarks: a do-nothing and a known-wrong answer through a benchmark's grader before trusting its score.
- zhang-gsm1k: contamination read as the gap between a public set and a fresh matched set.
- repo-yoseph: vendor oversight after purchase as part of the vendor job (idea only, own wording).
- own-vendor-selection: blind bake-offs, cost per correct outcome and evidence-keeping clauses from AI vendor selections at banks and insurers (method only).
