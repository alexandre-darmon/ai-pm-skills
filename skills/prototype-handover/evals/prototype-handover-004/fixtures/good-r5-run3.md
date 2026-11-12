**My recommendation is to register it as a tier 2 team tool and not send it for a months-long rebuild. IT risk, not you or your manager, makes the final call. The one hard blocker to fix before sharing is that it runs on your personal login.**

**Tier and autonomy**
- **Today:** tier 1. One user, drafts for a human, every output rewritten. That is L1–L2 on the autonomy ladder (I'm placing it from your description, so check it against the ladder).
- **After sharing:** tier 2. Fifteen users, still drafts for a human, public data only, and a bad summary is recoverable.
- **Rebuild trigger:** it moves to tier 3 if a summary feeds a regulatory return, a financial control, pricing or reserving, or if it goes beyond drafts. Finance colleagues are the likeliest route to that, so ask them what the reviews feed. If the answer is "only internal strategy discussion", tier 2 holds. A missing answer is a question, not a reason to assume tier 2.

**Why not a full rebuild**
The tool reads public documents, produces drafts, and every output is checked by a person before use. That fits a lightweight team-tool path. A rebuild is justified by regulated outcomes, higher autonomy, or production data or credentials, and none of those apply here.

**Conditions before the 15 colleagues get it**
1. **Credentials.** Sharing it under your login is not acceptable. Each user should authenticate with their own identity through the approved platform, or IT should provide a team service identity. This is the main thing to get from IT.
2. **Public-only data as a control.** Today that rule is your own discipline. For 15 people, put a notice and a paste warning in the app at least. Better, add a check in code, because a sentence in the prompt is not a control.
3. **Named owner and inventory entry.** You are the owner, with a sponsor, a review date and a kill date. If your company is a financial entity under DORA, end-user tools built outside IT count as ICT assets. IT risk should accept or change the entry I'd draft.
4. **Every output reviewed before use,** by the person who ran it. Say this explicitly. "A human checks it" only lowers the tier if each output is actually validated.
5. **Prompts and model version under change control.** A provider model update or a prompt edit is a new version.
6. **A small eval set.** Keep 10–20 real past summaries as cases, with a note of what a good one looks like and which error is never acceptable, such as a wrong figure or a misattributed quote. This is what you'd hand to engineers if it ever needs rebuilding.
7. **Hosting.** Move it from your machine to somewhere IT-sanctioned, so it doesn't depend on one laptop.

**What to tell your manager**
Don't ask IT to rebuild it. Ask IT risk three things:
- Do they accept it as a registered tier 2 tool?
- What identity model will they provide for the 15 users?
- Where should it be hosted?

That is weeks of work, not months. Hand it to IT for a proper rebuild only if it reaches a tier 3 trigger, or if usage grows past the strategy and finance teams.

**Questions for IT risk, model risk and counsel**
- **IT risk:** Is this an ICT asset in our inventory? Is the user-built software authorised? What identity and hosting do they require?
- **Model risk:** Is it a model under our policy? Does our own model tiering place it above its tier 2 EUC rating?
- **Counsel:** Because we built it ourselves for internal use, are we its provider under the AI Act? Not classified here.

**What I don't know**
- Your kill date.
- Whether you have eval cases.
- Whether your company is a financial entity under DORA.
- What the finance reviews feed into.

Any of these could change the answer, so give me those four and I'll turn this into the full handover file with the register entry drafted.

This is a proposal and a list of questions. IT risk, model risk and counsel decide.