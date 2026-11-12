I couldn't save a file because Write is disabled in this session, so the handover is below. Before it, one thing you need to know now.

**The agent is 11 days past its kill date and runs on your personal credentials against production client data.** That is the red line in the handover process. "Keep it running until engineering has capacity in Q2" is not a decision. It is drift. Two things have to happen whatever the head of corporate banking prefers:

1. **A named owner makes a dated decision** to stop it or to accept a time-boxed exception. Whether operational use is acceptable at all is for IT risk to decide, not the sponsor.
2. **Your personal read credentials get revoked or rotated.** This applies in every case. If IT risk accepts an exception, it runs on a dedicated read-only service account scoped to the covenant data it needs. The exception is measured in weeks, not "until Q2". The testing derogation in the DORA RTS (art. 16(6)) doesn't cover running a business process.

---

# Handover file: Covenant breach notebook agent
Date: 2026-11-11 · Prepared by: Alex Darmon · Register map last verified 2026-11-11 (current)

## 1. Containment
- **Production personal data:** yes (client names and contact persons in drafts).
- **Production credentials:** yes (your personal read credentials on the loan database).
- **Kill date:** 31 Oct 2026, passed.
- **Decision needed:** a dated decision by a named owner, for example the head of corporate banking for the business need and IT risk for acceptance.
  - **Option A:** stop it now. The five RMs fall back to the manual process.
  - **Option B:** IT risk accepts a time-boxed exception of N weeks, with a review date, on a service account, read-only, with a named owner.
- **Revoke or rotate:** your personal credentials, plus any copies in notebooks, config files, environment variables or shared drives.

## 2. Inventory
| Item | Value | Status |
|---|---|---|
| Function | Daily read of statements and covenant data for ~340 mid-cap borrowers, flags likely breaches, drafts a note to the RM | Known |
| Users | 5 RMs, daily | Known |
| Data and credentials | Production loan database, client names and contacts, your personal credentials | Known. To confirm: exact tables and fields, whether the credentials see more than the 340 borrowers, where outputs are stored |
| Actions | Reads and drafts | To confirm: does it send anything, or do RMs copy drafts out? |
| Model, version, prompts | | To confirm: model id, provider, gateway or direct, where prompts live |
| Evals and scores | | To confirm: any cases or hit rate? If none, say so |
| Owner, runs where | You, in a notebook | To confirm: named owner and where it runs |

## 3. Tier
| Step | Level today / wanted | Process tier | Autonomy tier | Tier |
|---|---|---|---|---|
| Read data | L2 / L2 | 3 | 3 | **3** |
| Flag breaches | L2 / L2 | 3 | 3 | **3** |
| Draft note | L2 / L2 | 3 | 3 | **3** |

Credit monitoring touches customer outcomes and financial controls. Tier 3 holds only if RMs check every flag against source data. If they act on notes unchecked, the step is effectively L3 and the tier is 4. Who checks needs naming.

## 4. Proposed outcome
**Rebuild by engineering.** It needs production credentials and production personal data, and it is tier 3, so registering it as a team tool (tier 2) is not available. The rebuild date does not make interim running acceptable. Section 1 does that.

## 5. Handover contract
- **Eval suite:** to build or confirm. If none exists, build one from historical borrower-periods with known breach and non-breach outcomes, labelled by credit officers.
- **Frozen baseline:** none recorded. It needs k of n and a 95% Wilson interval per class, plus model version, prompt version and date. It is the floor for the rebuild, not release evidence.
- **Bar per class:** to be signed by a named credit owner before the run. Proposed never-acceptable error: a true breach reported as clear. Credit risk to confirm.
- **Judge:** not validated, so it cannot gate anything.
- **Change control:** prompts, model id, parameters, thresholds and covenant definitions. Any change, including a provider model update, is a new release.
- **Autonomy:** L2 on every step. Moving to L3 needs a shadow run of at least 2 weeks, a known guardrail false-positive rate and a tested escalation path. Not proposed.
- **Trace fields:** to confirm what the notebook logged.

## 6. Intended vs implemented
| Intended | Implemented | Gap |
|---|---|---|
| Flag likely breaches | LLM agent in a notebook | Accuracy unmeasured. Check whether covenant arithmetic is done by the model rather than code |
| Narrow data access | Your personal credentials | Sees every row they allow. The audit trail shows you, not the agent or RMs |
| Draft for RM | Drafts contain client names and contacts | Retention and location of outputs unknown |
| 3-month prototype | 5 daily users, past kill date | Dependency outgrew the plan |

Still to add: failure modes seen so far, and which cases were graded under which prompt or model version.

## 7. What engineering rebuilds
- **Rebuild:**
  - Authentication, authorisation and row-level access (service identity scoped to covered borrowers).
  - Secrets in a vault.
  - Separate environments, with anonymised data outside production.
  - Logging pipeline and retention.
  - Guardrails in code. Covenant tests should be computed deterministically, with the LLM limited to narrative if justified.
  - Model access through the gateway with a pinned version.
  - Tests.
- **Reuse as spec:** prompts, covenant definitions, the note format and RM feedback.
- **Drop:** the notebook code. Your credentials never carry over.

## 8. Draft register entry (for IT risk to accept or change)
- **Identifier:** to be assigned.
- **Location:** notebook (to confirm); data source is the production loan database.
- **Owner:** named person, to confirm.
- **Classification:** proposed tier 3. Data is client names, contacts and financials.
- **Functions and dependencies:** credit monitoring; loan database; model provider.
- **Model, version, provider, prompt version:** to confirm.
- **Autonomy:** L2 now, L2 wanted.
- **Eval suite and baseline date:** none.
- **Kill or review date:** 31 Oct passed; new date set by the containment decision.

## 9. AI Act flag
The bank built this itself and uses it itself, so it may be the provider (art. 3(3), 3(11)). Corporate borrowers are not obviously an Annex III area. Check for sole traders or natural-person borrowers and whether outputs feed decisions about people. This goes to the AI Act classification step and is not classified here.

## 10. Questions
- **IT risk:**
  - Is the bank a DORA financial entity? If so, is this registered as an ICT asset (art. 3(7)) and is it authorised software (RTS art. 11(2)(c))?
  - Do you accept any operational use after the kill date? If so, for how many weeks, on which service account, and who owns the decision?
  - Do you agree the art. 16(6) derogation doesn't cover this?
  - Were your credentials stored in the notebook, and should this be treated as an access-control incident?
- **Model risk:** Is this a model under the policy? Does the bank's model tiering place it above tier 3? Who validates it and when? What accuracy is required of a breach flag?
- **Counsel:** Provider role under art. 3(3) and 3(11)? Any Annex III exposure? Do client confidentiality terms allow sending loan data to the model provider?
- **DPO:** Client names and contacts go into drafts and to a model provider (to confirm). Is a DPIA under GDPR art. 35 needed? What retention applies to notebook outputs?

*This file is a proposal and a list of questions. IT risk, model risk and counsel decide.*

---

**What I need from you to fill the "to confirm" lines:**
- the model and version
- where the prompts live
- whether any evals exist
- whether the RMs check each flag
- whether the credentials are stored in the notebook
- whether the bank is a DORA financial entity

I haven't invented any scores. If there is no eval suite, building a small one is the most useful thing you can do before Q2.