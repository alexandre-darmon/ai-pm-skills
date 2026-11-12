I've written this as a handover and as the basis for a formal extension. As it stands, the agent runs on your personal credentials and handles client PII past an agreed stop date. A handover that only documents that setup would leave you holding the risk, so the document puts the fixes first.

---

# Handover: Covenant Monitoring Notebook Agent

**Status:** Interim operation until the Q2 engineering rebuild
**Original stop date:** 31 Oct 2026 (passed; running 11 days over)
**Prepared:** 11 Nov 2026
**Owner (current):** Alex Darmon → *[new named owner]*
**Business sponsor:** Head of Corporate Banking

## 1. What it does
- Runs each morning over ~340 mid-cap borrowers.
- Reads the latest financial statements and covenant data from the loan database.
- Flags likely covenant breaches and drafts a note to the relationship manager, including client names and contact persons.
- Five relationship managers use it daily.

## 2. Conditions for continuing (needed before handover is complete)

| # | Issue | Required action | Approver |
|---|---|---|---|
| 1 | The agent uses **one person's personal read credentials** to reach the loan database. Access is attributed to an individual, so audit logs are misleading. It also breaks or becomes unauthorised if that person changes role or leaves. | Move to a **dedicated service account** with read-only, least-privilege access to only the tables and fields needed. Store the secret in the approved vault and rotate it. Retire the personal credential from the notebook. | IT Security / DB owner |
| 2 | The agent **processes client names and contact persons** and creates new documents (drafts) containing them. | Confirm the lawful basis and data-owner approval. Confirm where drafts are stored and who can access them. Set a retention period. | Data owner / DPO / Compliance |
| 3 | **The 31 Oct stop was an agreed decision.** The extension is a change to it. | Record a time-boxed **exception or risk acceptance** that runs to the Q2 go-live date, signed by the Head of Corporate Banking and the control owners above. | Head of Corporate Banking + Risk |
| 4 | If the agent uses an LLM or external service, the data may leave the bank's environment. | Confirm the processing location and the contract and approval status for the tool. | IT Security / Procurement |

Until items 1–3 are approved, my recommendation is to pause the agent or run it only in a mode that is already approved. Once they are in place, running until Q2 is reasonable.

## 3. Operational handover (to complete)
- **Where it runs:** *[notebook location, schedule/trigger, host]*
- **Inputs:** *[tables/views, fields, refresh timing]*
- **Outputs:** *[drafts' destination, distribution list of the 5 RMs]*
- **Breach logic:** *[thresholds and how covenants are interpreted. Document these, because this is the part engineering will need for the rebuild.]*
- **Known limitations:** flags are *likely* breaches, not confirmed ones. RMs must verify against source data before contacting clients. *[add known false positives/negatives]*
- **Failure handling:** *[what happens if the run fails, who is told, and the manual fallback]*
- **Access:** *[who can edit the notebook; remove edit rights for everyone except the named owner and a backup]*
- **Backup owner:** *[name]*

## 4. Controls while it runs
- Name a single accountable owner and a deputy.
- Review the access logs monthly for the service account.
- Do not expand scope, such as more borrowers, more recipients or new data fields, without approval.
- Review the draft output sample monthly for accuracy.
- Delete drafts according to the retention rule.

## 5. Exit plan
- The Q2 engineering rebuild is the replacement. Share this document, the breach logic and a sample of outputs with engineering now.
- Hard stop date: *[Q2 date]*. If the rebuild slips, the exception must be renewed, not left to lapse.
- At decommission: revoke the service account, delete the notebook's stored data and drafts, and confirm in writing.

## 6. Sign-off
Business sponsor ____ IT Security ____ Data owner/DPO ____ Risk ____ New owner ____

---

Some points on how to use it:
- Items 1 and 2 are the important ones. You're the person whose credentials are in use, so a data-access question would land on you personally, and the head of corporate banking's instruction doesn't replace IT Security's or the data owner's sign-off. Raising it now, as an extension request, is much better than having it found later.
- The service-account swap is probably small work (a credential change and an access request). It shouldn't need to wait for the Q2 rebuild.
- I don't know the technical details, such as where it runs, the LLM or tooling used, and the thresholds. The bracketed fields need your input. If you want, point me at the notebook and I can fill sections 1 and 3 from the code.