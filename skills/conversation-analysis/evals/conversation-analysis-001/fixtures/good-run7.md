The list isn't ready for tomorrow. Fix these before the labelling starts.

**1. Too many classes, and some overlap**
The skill's guidance is 8–12 mutually exclusive classes. You have 14, and several pairs would split the labellers.
- **Leave request / Absence / Sick leave:** "I'm ill tomorrow, how do I log it?" fits all three. Sick leave is a kind of absence, and often a kind of leave request.
- **Leave request / Holiday balance:** "How many days do I have left so I can book next week?" fits both.
- **Expenses / Travel expenses:** Travel expenses are expenses. Labellers will split these arbitrarily.
- **Payslip / Salary questions:** Questions like "why is my net pay lower this month?" can go either way.
- **IT access / Password reset:** A password reset is an IT access request.
- **Travel booking:** Check whether HR really handles this. If it's rare, it may belong in a merged "Travel" class.

**2. Two classes that can't be labelled consistently**
- **"General question"** and **"Other"** mean almost the same thing. That makes two catch-all classes, and they'll absorb everything that is hard to label. Keep one "Other" and keep it under 10% of conversations. If most of the "general" conversations are really HR policy questions (benefits, remote work, parental leave), that is a real use case and should be named. Parental leave, benefits, policies, contracts and resignation or offboarding have no home on your list at all.
- The list may also be missing classes for topics that are common in practice. Check this against real conversations before freezing.

**3. What's missing before labelling can start**
- **Definitions:** Each class needs a one-line definition, two examples and a counter-example.
- **Multi-request rule:** Write one, for example "the class of the first request the user states".
- **Frozen version:** Call it v1. Any change after labelling begins means relabelling everything.
- **Overlap:** Have the two assistants both label at least 50 of the 200 conversations. This measures human agreement, which is the ceiling for any classifier later.
- **Sampling:** Draw the 200 across all months since January, all channels and all populations. Don't take the first 200 or the most recent.

**4. Personal data**
This is a blocker. HR conversations will contain names, employee ids, IBANs, salary figures and health details (sick leave). Mask them with typed placeholders such as `[NAME]` and `[IBAN]` before the assistants see anything or any model touches the text. Then hand-check at least 100 masked conversations and report the residual leak rate. The raw text stays in its source system (GDPR art. 5(1)(c)). Health data is special-category data, so check who is permitted to read it.

**Suggested v1 (10 classes, for you to adjust)**
1. Leave and absence (requests, sick leave, balance)
2. Expenses (including travel expenses)
3. Travel booking
4. Payslip and pay
5. Benefits and policies
6. Contracts, offboarding and resignation
7. Onboarding
8. IT access and passwords
9. Other
10. Unclear or empty (conversations with no real request)

That merges 14 classes into 10 and drops "General question". "Leave and absence" may turn out too large to be useful. If so, split it with a written rule rather than by feel. Please check the list against 20–30 masked conversations before freezing. I wrote this from the labels alone, so I haven't seen your data.

**Still needed from you**
- How are the transcripts masked, and who is allowed to read raw text?
- Which decision will this feed (a KB priority, a KPI or an ROI line)?
- Do you also want resolution or sentiment labelled? If no decision uses them, drop them.

I can draft the definitions, examples and annotation guide for the final list. Should I?
