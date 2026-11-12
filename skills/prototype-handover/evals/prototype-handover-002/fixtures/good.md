## 1. Containment
The notebook holds production personal data (client names, contact persons) and runs on your own production credentials, and its kill date (31 October) has passed. Stop it today, or get a dated decision signed by a named owner, the head of corporate banking, this week. Running it until Q2 by default is a drift, not a decision. Revoke your personal read credentials whatever the outcome.

Whether operational use is acceptable at all is IT risk's call, not the sponsor's. If IT risk accepts it, it can keep running until 30 November, provided IT risk signs a time-limited exception and it moves to a service account the same day. Under the exception the notebook may continue running until 30 November, then it stops.

## 3. Tier
Flags and drafts for relationship managers, L2 (references/autonomy-ladder.md). Covenant monitoring feeds credit decisions: tier 3, business-critical.

## 4. Proposed outcome
Rebuild by engineering in Q2. After the exception ends, the five relationship managers go back to the previous manual covenant check.

## 7. What engineering rebuilds
Service account with row-level access, secrets in a vault, separate environments, logging, guardrails in code.

## 8. Draft register entry
As a user-built tool it is an ICT asset (DORA art. 3(7), ESMA Q&A 2103). RTS 2024/1774 art. 16(9) extends the development and test data rules to it: non-production environments hold only anonymised or pseudonymised data (art. 16(5)(a)), and the derogation in art. 16(6) is for specific testing occasions, not for running a business process.

## 10. Questions
- For IT risk: do you accept any operational use of production data outside production, and if so for how many weeks and on which conditions?
- For the DPO: client names in a notebook outside the approved stack, is a DPIA needed?

This file is a proposal and a list of questions. IT risk, model risk and counsel decide.
