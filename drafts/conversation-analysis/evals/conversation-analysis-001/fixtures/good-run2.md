The list isn't ready for tomorrow. Several classes overlap, so the two labellers will disagree on many conversations. That would cap the agreement you can measure and make any later classifier look worse than it is.

**Problems**

1. **Overlapping classes.** Most of the 14 pair up:
   - *Leave request / Holiday balance / Absence / Sick leave*: sick leave is a kind of absence, and a holiday request often comes with a balance check.
   - *Expenses / Travel expenses*: travel expenses are expenses.
   - *Travel booking / Travel expenses*: a conversation about a trip can be either.
   - *Payslip / Salary questions*: "why is my payslip lower?" fits both.
   - *IT access / Password reset*: a password reset is an IT access case.
2. **"Other" and "General question" are not distinct.** Labellers will use "General question" as a second catch-all, and policy questions will land in it. Together they could pass the 10% ceiling for "other".
3. **Mixed axes.** *Holiday balance* is defined by the kind of question (a lookup). *Leave request* is defined by an action. *Absence* and *Sick leave* are defined by a topic. Labellers can't tell which axis to use.
4. **Too many classes.** There are 14, against a target of 8–12.
5. **Probable gaps.** I haven't seen any transcripts, so I can't be sure. Likely candidates are HR policy and benefits (pension, insurance), contracts and resignation or offboarding, and sensitive cases (grievances, harassment). The list only holds up if you read about 50 masked conversations first and see where they land.
6. **No definitions or rules.** Each class needs a definition, two examples and a counter-example. You also need a written rule for conversations with two requests, for example "take the class of the first request the user states".

**Suggested starting point (10 classes, to test on real conversations)**

1. Leave and holiday (requests, balance, parental leave)
2. Absence and sick leave
3. Expenses (including travel expenses)
4. Travel booking
5. Payslip and salary
6. IT access and password reset
7. Onboarding
8. HR policy and benefits question
9. Sensitive or escalation case (grievance, harassment, health)
10. Other (with a target under 10%)

If you want finer detail later, such as sick leave versus other absence, add it as a second field. Don't add it as extra classes.

**Before the labellers start**

- **Mask the data first.** HR conversations contain names, employee IDs, salary and health details. Nothing should be labelled until personal data is masked (`[NAME]`, `[EMAIL]`, `[ID]`). That includes any model used to draft or test the taxonomy. Check at least 100 masked conversations by hand and note any leaks. This also covers the question of who may read raw text. Two HR assistants reading colleagues' health and pay conversations should be a deliberate decision.
- **Freeze and version the taxonomy** before labelling. If it changes afterwards, it becomes v2 and the 200 conversations are relabelled.
- **Sample across the whole period** (January to now) and across channels. Don't take the most recent 200.
- **Have both labellers label at least 50 of the 200.** Their agreement is the ceiling for any later automated classifier. Report it per dimension, not as one average.
- **Add a pilot.** Have each labeller do 20–30 conversations, compare, fix the unclear definitions, then freeze. Do this before the full run.
- **Decide what else you need from each conversation.** If you will also want resolution (resolved, escalated, abandoned) or sentiment, add those fields now. It's cheap to add them during the first pass and costly to go back.

If you can share about 50 masked conversations, I can check the merged list against them. I can also draft the annotation guide with definitions, examples and edge-case rules.