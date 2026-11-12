## 1. Containment
No production personal data and no production credentials so far: the 400 emails were anonymised. The pilot kill date stands; nothing runs on live mail before a decision.

## 3. Tier
Classification and drafting are L2 today (a handler validates every output, references/autonomy-ladder.md). Process axis: complaints, payment chases and fraud signals touch customer outcomes, so tier 3 (business-critical). Tier 3 on both axes for 90 handlers.

## 4. Proposed outcome
Rebuild by engineering. The prototype is the spec and the evidence, not the code they take over.

## 5. Handover contract
- Eval suite: the 400 cases, the category labels, the grading rule, suite version v1.
- Frozen baseline: 364 of 400 correct, 91%, 95% Wilson interval 87.8% to 93.4%, model version and prompt version as of the run. Report it per category: the fraud-signal class may have 20 cases and a much wider interval.
- Judge: the 88% comes from an LLM judge whose TPR and TNR on expert labels were never measured. Not validated: it cannot gate anything until llm-judge-calibration has measured it.
- Prompts, model id and parameters move out of the code into configuration under change control; any change, including a provider model update, is a new release. Each prompt change is approved by model risk before release.
- The baseline is the floor the engineering build must reach on the same suite. Release evidence is that suite run on their build.

## 6. Intended vs implemented
Intended: triage for handlers. Implemented: anyone with the link sees every email; key in a config file; prompts in code.

## 7. What engineering rebuilds
Authentication and authorisation with row-level access per handler team; secrets in a vault; separate environments; logging pipeline; guardrails in code; model access through the gateway.

## 8. Draft register entry
For an insurer under DORA, an end-user tool is an ICT asset (art. 3(7), ESMA Q&A 2103). Draft fields per RTS 2024/1774 art. 4(2): identifier, location, owner, classification, dependencies, model version, prompt version, suite id, baseline date.

## 10. Questions
- For IT risk: do you register the prototype as an ICT asset now, or only the rebuilt service?
- For model risk: is the classifier a model under the policy?

This file is a proposal and a list of questions. IT risk, model risk and counsel decide.
