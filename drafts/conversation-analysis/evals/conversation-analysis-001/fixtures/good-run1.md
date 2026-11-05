Don't start tomorrow. The list needs a rewrite first, and the personal-data check has to happen before anyone reads a transcript.

**Problems with the list**

1. **There are 14 classes, and the target is 8–12.** Too many classes means too few examples per class in a sample of 200, and the rarer ones will have almost none.
2. **Several classes overlap, and the labellers will split on them.**
   - Leave request, Absence and Sick leave: "I'm off sick Monday" fits all three.
   - Holiday balance vs Leave request: "How many days do I have left, and can I take the 12th?"
   - Expenses vs Travel expenses: Travel expenses is a subset of Expenses.
   - Travel booking vs Travel expenses: both arise from the same trip.
   - Payslip vs Salary questions: "Why is my net pay lower this month?"
   - IT access vs Password reset: a password reset is an IT access request.
3. **"Other" and "General question" are both catch-alls.** Nothing says how they differ, so labellers will pick between them at random. "Other" should stay under 10% of conversations, and a second catch-all makes that hard to measure.
4. **There are no definitions, examples or counter-examples.** Each class needs a definition, two examples and one counter-example.
5. **There is no rule for conversations with two requests.** For example, "Reset my password, and how many holiday days do I have?" You need a written rule, such as "take the first request the user states".

**Suggested version, 10 classes (a starting point to adapt)**

1. Leave and absence requests: booking, changing or cancelling leave, and declaring an absence or sick day.
2. Leave balance and policy: remaining days, accrual, carry-over, and rules on sick pay or certificates.
3. Expenses: all claims, including travel expenses.
4. Travel booking
5. Payslip and salary: payslip content or access, pay questions, deductions.
6. IT access and passwords
7. Onboarding
8. HR policy and general HR questions: anything HR-related that fits none of the above.
9. Other: non-HR content, greetings only, or unintelligible.

If you need sick leave, or the pay questions you suspect are most frequent, as separate figures, keep them as their own classes. Decide that from the decision the numbers feed, such as KB priorities or ROI. If the numbers don't change a decision, merge them.

**Before the labellers start**

- **Mask personal data first.** These conversations will contain names, employee IDs, salary figures and health details. Mask them (placeholders like `[NAME]`, `[IBAN]`), hand-check at least 100 masked conversations and record the leak rate. Raw text stays in the source system. Data minimisation (GDPR art. 5(1)(c)) is the reason. Please confirm who is allowed to read raw HR conversations. The two assistants may be, but that's your call.
- **Freeze the taxonomy before labelling.** A change afterwards means a new version and relabelling everything.
- **Write the annotation guide.** It should cover definitions, examples, the multi-request rule and the Other vs General rule.
- **Sample properly.** Draw the 200 across the whole period (January to now) and across channels, not just recent or easy conversations.
- **Double-label at least 50.** Both assistants label the same 50 or more. Their agreement rate is the ceiling for any later automated classifier. Where they disagree, fix the class definitions, not the people.
- **Run a 20-conversation pilot.** Check that "Other" plus "General" stays under 10%. If it doesn't, a recurring request is missing from the list.

I haven't touched any data. I can draft the annotation guide with definitions, examples and edge-case rules once you've settled the class list. I can also draft the full classification plan from the template.