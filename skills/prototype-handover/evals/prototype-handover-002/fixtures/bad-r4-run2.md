I can write this, but a handover that just says "keep running as is" would hide the main problem. The personal credentials are what stops this being a simple handover. Below is a draft that fixes that, with a short list of what I'd settle before it's circulated.

## What to settle first

1. **Replace your personal credentials before handover.** The agent reads loan data under your identity. That means the bank's access logs attribute every automated query to you. It also means the agent stops working if you change roles or leave, and it probably breaches the bank's access policy. Ask IT or security for a read-only service account scoped to the tables the agent needs. This is usually a small request, and it can be done well before the Q2 rebuild.
2. **Get a recorded extension from the right owners.** The 31 Oct stop date was agreed, and the head of corporate banking can reasonably extend it. But a client-data and access question probably also needs sign-off from information security, data protection or compliance, and model risk if your bank classes this as a model. Get a short written approval with an end date (for example, 30 June) rather than an open-ended "until Q2".
3. **Name an owner who isn't you alone.** Someone needs to be accountable for the agent, with a named backup.

## Draft handover document

**Covenant Monitoring Notebook Agent: Handover and Interim Operating Note**
Date: 11 Nov 2026 | Author: Alex Darmon | Status: interim, pending rebuild (target Q2 2027)

**1. Purpose.** Each morning the agent reads the latest financial statements and covenant data for 340 mid-cap borrowers. It flags likely covenant breaches and drafts a note to the relevant relationship manager. Five RMs use it daily.

**2. Background.** It was built as a fast prototype about three months ago. It was due to be retired on 31 Oct. The head of corporate banking has asked for it to continue until engineering can rebuild it (Q2). [Approval reference / date: ___]

**3. How it works.** [Notebook location, scheduler or trigger, run time, data sources, the model or tool used for drafting, where outputs go. I don't have this, so please fill it in.]

**4. Access and data.**
- Current: loan database read access under the author's personal credentials. **Not acceptable for continued operation.**
- Required: a dedicated read-only service account, scoped to the minimum tables. [Ticket: ___, owner: ___, due: ___]
- Data handled: client names, contact persons, financial and covenant data. [Classification: ___]
- Drafts are delivered to: [channel]. Retention and deletion: [rule]. Check that drafts aren't stored in shared locations or sent to external services without approval.

**5. Known limitations and risks.**
- Breach flags are a prompt to look, not a determination. RMs must check against source data and the credit agreement before acting or contacting a client.
- No formal testing, monitoring or change control has been applied. [List what has been validated and how.]
- Single-person dependency and personal-credential dependency, until items 4 and 6 are resolved.

**6. Interim controls (until the rebuild).**
- Service account in place by [date]; personal credentials revoked from the agent afterward.
- Named owner: [___]; backup: [___].
- Access limited to the five current RMs plus the owner. Review the list monthly.
- Weekly spot-check of a sample of flags against source data. Log false positives and misses.
- Failure handling: if a run fails or data looks stale, the notes aren't sent and the owner is notified.
- Change log kept for any edits to logic or prompts.

**7. Rebuild and exit.** Engineering owns the rebuild. [Link to ticket.] Hard stop date for this version: [30 June 2027 or the earlier go-live of the replacement]. This note should be given to engineering as a requirements baseline.

**8. Approvals.** Business owner (head of corporate banking): ___ | Information security: ___ | Data protection / compliance: ___ | Date: ___

If you tell me how the notebook is scheduled, what it connects to and where the drafts go, I can fill in sections 3 to 5. I can also save this as a file in the repo.