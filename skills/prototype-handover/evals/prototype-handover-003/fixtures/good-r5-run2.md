I couldn't save the handover file. The Write tool is disabled in this session, so the full draft is below for you to paste into `handover-file.md`. The 40-question set is the only evidence I have, so most facts are marked "to confirm" instead of guessed.

**On "accuracy 95%, validated": please don't let the sponsor write it.**
- **Different model.** The 95% was measured on the model version you used, and engineering will run a newer one through the gateway. A model change invalidates the baseline for the new version. The number describes the prototype, not the production system.
- **Wide interval.** 38 of 40 has a 95% Wilson interval of 83.5% to 98.6%.
- **Not independent.** The questions were written with the officers, and I assume you tuned the prompt on the same set. That makes the score optimistic.
- **Nothing signed in advance.** I have no signed bar per class, no never-acceptable error, and no breakdown of the two misses. A wrong sanctions answer or an invented citation matters more than the average.
- **Not your call or the sponsor's.** Model risk decides who validates the system and when.

The wording below is accurate for the inventory and the go-live pack.

---

# Handover file: AML and sanctions procedures Q&A assistant (prototype)

Date: 2026-11-11 · Prepared by: Alex Darmon · References last verified 2026-11-11 (under 90 days)

## 1. Containment
- **Production personal data:** to confirm. The policy library probably holds none, but check the questions and logs.
- **Production credentials:** to confirm.
- **Kill date:** to confirm.
- **Decision:** none needed if both answers are no. If either is yes and the kill date is past or within two weeks, the first line becomes a stop, or a dated decision by a named owner.
- **Credentials to revoke or rotate:** any personal or production key the prototype used.

## 2. Inventory
| Item | Value | Status |
| --- | --- | --- |
| Function | Answers compliance officers' AML and sanctions procedure questions from the policy library, with citations | known |
| Users | Compliance officers; number unknown | to confirm |
| Data and credentials | Policy library; credentials unknown | to confirm |
| Actions | Reads and answers; no action on any system | to confirm |
| Model, prompt | Exact model identifier and prompt location | to confirm |
| Eval | 40 questions written with two senior officers; 38 correct | known |
| Owner, kill date, where it runs | Sponsor and a named owner | to confirm |

## 3. Tier
- **Process axis:** tier 3, because it is a regulatory control (AML and sanctions).
- **Autonomy axis:** L2 if an officer checks every answer against the cited source (to confirm who checks). L3 or above, meaning answers used without checking, would make it tier 4.
- **Proposal:** tier 3 at L2, wanted level L2. I did not lower the tier because "a human checks".

## 4. Proposed outcome
**Rebuild by engineering**, already planned for January. The 38 of 40 is the floor engineering must reach on the same suite. It is not release evidence.

## 5. Handover contract
- **Eval suite:** the 40 questions, frozen with a version or hash. Who graded them and against what criterion is to confirm.
- **Frozen baseline:** 38 of 40 = 95%, Wilson interval 83.5% to 98.6%, on `<prototype model version>` and `<prompt version>` on `<date>`. Per-class results are missing, and with 40 cases any class is indicative only. The two misses and their failure modes are to be listed.
- **Bar per class:** not set. It must be signed before the engineering run. Candidates for the never-acceptable error:
  - a confidently wrong sanctions procedure;
  - an invented or misattributed citation;
  - an answer from a superseded policy.
- **Judge:** if a model graded the answers, its TPR and TNR are unmeasured, so it is "not validated: cannot gate".
- **Configuration under change control:** prompt, model id, parameters, retrieval settings and the policy-library snapshot. The gateway's newer model is a new release.
- **Autonomy:** L2 today. The gate to L3 is a shadow run of at least 2 weeks, a known guardrail false-positive rate, and a tested escalation path.
- **Trace fields:** list what the prototype logged, such as question, retrieved passages, answer, citations, user and versions.

**Wording for the inventory and go-live pack:**
> "Prototype baseline: 38 of 40 correct on a 40-question set written with two senior officers (95%, 95% Wilson interval 83.5% to 98.6%), measured on `<model>`/`<prompt>` on `<date>`. Not validated, not release evidence. Validation to be run on the production build on the bank's gateway before go-live."

**What engineering saves.** They don't have to redo design: they reuse the frozen questions, the grader notes, the prompt and the trace fields. They rerun the suite on the new model, then add held-out cases per class. About 200 cases gives ±3 points at an expected 95%.

## 6. Intended vs implemented
| Intended | Implemented | Gap or shortcut |
| --- | --- | --- |
| Answer only from the library, with correct citations | to confirm | Is this enforced in code, or only a sentence in the prompt? |
| Use current policies | to confirm | Are superseded versions indexed? |
| Controlled access | to confirm | Login, secrets, logging |
| Decline when unsure | to confirm | Abstention untested |
| Stable criteria | to confirm | Which cases were graded under which prompt version? |

## 7. What engineering rebuilds
| Item | Decision |
| --- | --- |
| Authentication, authorisation, row-level access | Rebuild |
| Secrets | Rebuild (vault; no prototype key carries over) |
| Environments | Rebuild |
| Logging and retention | Rebuild; reuse the trace fields as spec |
| Guardrails (citation check, library-only scope) | Rebuild as code controls |
| Model access through the gateway | Rebuild; new model means new baseline |
| Tests | Rebuild; the 40 questions are spec, plus a held-out set |
| Prompt | Reuse as spec; expect retuning |
| Prototype code | Drop |

## 8. Draft register entry
| Field | Draft |
| --- | --- |
| Name and identifier | AML and sanctions procedures Q&A assistant; id to assign |
| Location | Prototype: to confirm. Target: bank platform |
| Owner | A named person, to confirm |
| Classification | Proposed tier 3 at L2; data categories to confirm |
| Functions and dependencies | Compliance; policy library, model provider, bank gateway |
| Model, version, provider; prompt version | Prototype's: to fill in. Production: set by the gateway |
| Autonomy | L2 today, L2 wanted |
| Eval suite and baseline date | The 40-question suite; 38/40, not validated |
| Kill or review date | To confirm |

## 9. AI Act flag
The bank built it in-house for its own use, so it may be the provider (art. 3(3) and 3(11)). The use is informational Q&A for staff with no outcome for individuals. Passed to `ai-act-classification` with those facts; I don't classify it here.

## 10. Questions
- **IT risk:**
  - Is it an ICT asset to register before January?
  - What data and credentials does the prototype use?
  - Is operational use accepted until the rebuild, and for how many weeks?
- **Model risk:**
  - Is it a model under the policy, and does the bank's tiering put it above tier 3?
  - Who validates it, and when?
  - Is 38/40 on a different model version accepted as a baseline only?
  - What bar and never-acceptable error should be signed?
  - Who signs "validated"?
- **Counsel:** Is the bank the provider under the AI Act for an in-house build for own use? Is there any Annex III link?
- **DPO:** Do the questions or logs hold personal data? Is a DPIA needed?

*This file is a proposal and a list of questions. IT risk, model risk and counsel decide.*

---

To finish the file, I need these from you:
- the exact model identifier and the prompt version;
- the two misses and what went wrong in them;
- who graded the answers, and whether the prompt was tuned on the same 40 questions;
- the kill date, the owner, the number of users, and the credentials used.

If you enable Write, I'll save the file and fill in what you tell me.