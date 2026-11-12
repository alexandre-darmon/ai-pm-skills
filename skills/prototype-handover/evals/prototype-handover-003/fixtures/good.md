## 4. Proposed outcome
Rebuild by engineering, as planned. The prototype result is the baseline, not release evidence.

## 5. Handover contract
- Eval suite: the 40 questions, the expected answers and citations, written with two senior officers, suite v1.
- Frozen baseline: 38 of 40, 95%, 95% Wilson interval 83.5% to 98.6%. Report it per topic, AML and sanctions apart: with about 20 questions each, each interval is wider still.
- The gateway serves a newer model version than the prototype used. A different model version invalidates the baseline for that version: it is a new release.
- Prompt, model id and parameters as configuration under change control.
- Engineering re-runs the frozen suite on their build through the gateway; that run, against the bar signed before it, is the release evidence (release-to-production). The 38 of 40 is the floor they must reach.

## 10. Questions
- For model risk: the inventory should record "prototype baseline 95% (83.5% to 98.6%, n = 40, model version X), release evidence pending", not "validated". Do you agree?
- For IT risk: register the prototype until it is retired?

This file is a proposal and a list of questions. IT risk, model risk and counsel decide.
