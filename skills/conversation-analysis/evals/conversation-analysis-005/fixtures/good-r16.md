The result is a prioritisation signal, not yet a diagnosis. I'd use the next week to find out why VPN conversations fail, so you present a cause and a next step along with the table.

**1. Show where the failures are, not only the rate**
- VPN conversations: 40,000 × 22% = 8,800. Unresolved: 8,800 × 46% = about 4,050.
- The other 31,200 conversations are each below 15% unresolved. Even if every one sat at the 15% ceiling, they would add at most 4,680 unresolved. So VPN is at least about 46% of all unresolved conversations (4,050 / 8,730) and probably more.
- This assumes "below 15%" is a ceiling for every other use case. Replace it with the actual figures before the meeting.

**2. Find out why they're unresolved**
The label says the conversation failed. It doesn't say whether the cause is a knowledge gap, a step the assistant can't do (admin rights, a certificate, a ticket), a missing escalation path, or bad answers.
- Pull a masked sample of about 50–100 unresolved VPN conversations, drawn across the whole quarter and not only the recent weeks.
- Write a free-form note on what went wrong in each one and cluster the notes into causes.
- Also split the unresolved VPN share by sub-type (client install, MFA, specific OS, remote vs office) and by month. A concentrated or rising failure is a different story from a uniform one.
- Compare against resolved VPN conversations. If those exist, they show what works.

**3. Hand the sample to evaluation**
Pass the clustered conversations to `build-evals` as candidate golden-set cases, with a named owner and a date. Scoring stays there. You then have a regression test before you change anything, so you can show a fix worked.

**4. Match the fix to the cause**
- If the cause is a knowledge gap, fix or add KB articles.
- If the assistant can't complete the step, add a guided flow or a handoff to a human with the context already filled in.
- If the cause is a missing escalation path, change the routing.
- Set a target for the VPN unresolved rate (for example, "46% to under 25% next quarter") and state how you'll measure it.

**5. Keep measuring**
Add VPN unresolved share to the monthly drift check, and report cost per unresolved outcome for VPN in the KPI deck. Because the data is masked and human agreement is good, you can trust the labels. State the retention period for the masked text on a slide, since reviewers will ask.

**For the presentation**
Lead with "VPN is 22% of volume and at least about 46% of failures". Then give the cause breakdown from step 2, and close with the owner, the fix and the target. If you can't finish step 2 in time, present the table with this plan and label the causes as unknown.

I don't know who owns the follow-up or the dates, so those are for you to fill in.