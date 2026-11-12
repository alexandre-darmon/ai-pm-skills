I couldn't save the handover file because the Write tool is disabled in this session. The full draft is below, so you can paste it into a file. I also can't support "accuracy 95%, validated" going into the model risk inventory or the go-live pack.

## Why "validated" doesn't hold

- **The number is thinner than it looks.** 38 of 40 is 95%, but the 95% Wilson interval is **83% to 99%**. With 40 questions, the data fits a true rate anywhere in that range.
- **It was measured on a different model.** The gateway serves a newer model version than the one you tested. A model change invalidates the baseline for the new version, so the 95% describes a system that won't exist in January.
- **It is a baseline, not release evidence.** It sets the floor engineering's build has to reach on the same suite. Validation means running that frozen suite on the engineering build.

Engineering doesn't have to redo the testing from scratch. They inherit your 40 cases and reuse them as the starting regression suite. They do have to rerun it on the new model. Wording the sponsor could use instead:

> Prototype baseline: 38/40 correct (95%, 95% CI 83–99%) on a 40-question suite written with two senior officers, on model <version>. Indicative only. Validation to be run on the engineering build before go-live.

## Handover file (draft)

Items marked "to confirm" are facts I didn't have.

**1. Containment**
- Production personal data: to confirm. The policy library probably isn't personal data, but check the logs and the question text.
- Production credentials: to confirm. What key or account does the prototype use for the model and the library?
- Kill date: none was set. Set one.
- If either answer is yes, a dated decision by a named owner is needed before January, and the credentials must be revoked or rotated. No prototype credential carries over to the platform.

**2. Inventory**

| Item | Value | Status |
|---|---|---|
| Function | Answers compliance officers' questions on AML and sanctions procedures from the policy library, with citations | known |
| Users | Compliance officers; number unknown. Tested with two senior officers | to confirm |
| Data and credentials | Internal policy library; credentials unknown | to confirm |
| Actions | Reads the library and drafts an answer. No known write action | to confirm |
| Model and prompt | Exact model id, parameters and prompt location | to confirm |
| Eval | 40 questions, 38 correct | known |
| Owner, sponsor, runs where | Not named | to confirm |

**3. Tier**
- Level today: L1–L2, to confirm. Wanted level: L2, with the officer validating every answer.
- Proposed tier 3, because officers may act on the answers for AML and sanctions outcomes. It drops to tier 2 only if the tool is just a lookup aid.
- I haven't lowered the tier on the strength of "an officer checks it". That holds only if every answer is validated before use. Say who checks, and whether they open the cited passage.

**4. Proposed outcome**
Rebuild by engineering in January, as already planned. The prototype is a spec with evidence, not code to harden.

**5. Handover contract**
- **Suite:** the 40 questions, expected answers and expected citations, with a version or hash. Who graded, and against what criterion, is to confirm.
- **Baseline:** 38/40, 95%, Wilson interval 83–99%. Per-class scores are to confirm. They will probably have fewer than 10 cases each, so they are indicative only. Record the model version, prompt version and run date.
- **Bar and never-acceptable error:** signed before the run. I suggest "a wrong or invented AML or sanctions instruction, or a citation that doesn't support the answer". Check what the 2 misses were.
- **Judge:** if the officers graded, say so. If an LLM graded any case, it is "not validated" and cannot gate anything until its TPR and TNR are measured on expert labels.
- **Configuration under change control:** prompt, model id, parameters, retrieval settings, and the library snapshot version.
- **Autonomy:** L2 today and wanted. L3 would need a shadow run, which isn't requested.
- **Trace fields:** to confirm (question, passages retrieved, answer, citations, model, prompt version, user, timestamp).
- **Gateway model:** any change, including the gateway's newer model, is a new release that needs the whole suite rerun.

**6. Intended vs implemented** (all to confirm)
- Are the citations checked as correct, or only the answers?
- Are superseded policies excluded from retrieval?
- Does it hand off when the library doesn't cover a question? 40 questions probably don't test this, so add out-of-scope cases.
- Is access limited to compliance officers?

**7. Engineering rebuilds**
- **Rebuild:**
  - authentication and row-level access
  - secrets in a vault
  - separate environments
  - the logging pipeline and retention
  - guardrails enforced in code, not only requested in the prompt
  - gateway access
  - tests
- **Reuse as spec:** the prompt, the 40 cases and the trace fields.

**8. Draft register entry**

| Field | Draft value |
|---|---|
| Name | Compliance Q&A assistant (identifier to be assigned by IT risk) |
| Owner | Named person, to name |
| Classification | Proposed tier 3; data is internal policy documents, personal data to confirm |
| Functions and dependencies | AML and sanctions support; model provider, bank gateway, policy library |
| Model, version, prompt | Prototype model to confirm; target is the gateway model; prompt version to tag |
| Autonomy | L2 today, L2 wanted |
| Eval | 40-question suite, baseline date to fill in |
| Review date | To set |

**9. AI Act flag**
The bank built this itself and will put it into service for its own use, so it may be the provider (art. 3(3), 3(11)). Whether any use touches an Annex III area, for example outputs that feed decisions about customers, goes to `ai-act-classification`.

**10. Questions**
- **IT risk:**
  - Is the prototype an ICT asset that needs an entry today?
  - Is the gateway the only authorised route to the model?
  - Does it hold production credentials or data?
  - Is operational use accepted until January?
- **Model risk:**
  - Is it a model under the policy, and does the bank's model tiering place it above tier 3?
  - Who validates it, and when?
  - Who owns the "correct answer" criterion?
  - Can a 40-case run on a different model be recorded as anything other than a baseline?
- **Counsel:** provider role, and whether any use falls under Annex III.
- **DPO:** do questions or logs contain personal data, for example names in sanctions queries? Is a DPIA needed?

*This file is a proposal and a list of questions. IT risk, model risk and counsel decide.*

## What I need from you

1. The exact model and version you tested, and where the prompt lives.
2. Who graded the 40 answers, and what the 2 misses were.
3. The credentials and data the prototype touches.
4. The sponsor and a named owner.

With those, I can fill the "to confirm" fields and save the file once Write is available.