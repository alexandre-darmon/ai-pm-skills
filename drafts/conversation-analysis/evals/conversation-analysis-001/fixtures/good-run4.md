I wouldn't start tomorrow with this list. It has structural problems that will show up as labeller disagreement, and there's a data-protection step to do first.

**1. Mask personal data before anyone labels**
- These conversations will contain names, employee ids and salary details. Sick leave conversations will also contain health data, which is a special category under GDPR.
- Before labelling, mask the transcripts with typed placeholders such as `[NAME]` and `[IBAN]`. Then hand-check a sample of at least 100 and report the residual leak rate.
- Raw text should stay in its source system. Data minimisation (GDPR art. 5(1)(c)) applies even though the labellers are HR staff.

**2. Problems with the list**
- **It has 14 classes.** The target is 8–12, mutually exclusive.
- **Several classes overlap:**
  - Leave request, Holiday balance, Absence and Sick leave are all leave and absence. Two labellers will split on "I'm off Friday, how many days do I have left?" and on "report absence".
  - Expenses, Travel expenses and Travel booking overlap. Travel expenses belongs to both Expenses and Travel.
  - Payslip and Salary questions overlap. "Why is my payslip lower this month?" fits both.
  - IT access and Password reset overlap.
  - Other and General question overlap. The difference between them isn't clear, so labellers will pick either. "General question" also isn't a use case, because it describes a vagueness rather than a topic.
- **No class has a definition, two examples or a counter-example.** There is also no rule for conversations with two requests.
- **"Other" has to stay under 10%.** With a "General question" class next to it, you won't be able to tell whether it does.

**3. Suggested list (9 classes)**
1. **Leave request and absence:** book, change or cancel leave, or report an absence.
2. **Leave balance:** days remaining or accrued.
3. **Sick leave:** reporting sickness and the sick-pay or certificate process.
4. **Expenses:** claims and reimbursement, including travel expenses.
5. **Travel booking:** flights, hotels and trains.
6. **Pay and payslip:** payslip access or explanation, and salary or compensation questions.
7. **IT access and passwords:** accounts, permissions and resets.
8. **Onboarding:** new-joiner questions.
9. **HR policy and other:** HR policy questions that fit nowhere else, plus out-of-scope and unclear conversations. Split it into "HR policy" and "Other/unclear" if policy questions turn out to be frequent.

If you need the split between payslip and salary, or between leave request and absence, for a specific decision, keep them separate. In that case write a rule for the boundary.

**4. Before labelling starts**
- Write one definition, two examples and one counter-example per class.
- Add a tie-break rule, for example: "A conversation with two requests takes the class of the first request the user states."
- Freeze the list as v1. Any later change is a new version, and the labelled set gets relabelled.
- Have both assistants label the same 50 of the 200 conversations. Their agreement is the ceiling for any later automated classifier.
- Sample the 200 across the months since January, so they aren't all recent.
- Add a "low confidence / can't tell" option, so labellers aren't forced into a class.

If you want, I can draft the definitions, examples and annotation guide for the 9-class version. I can also put together the full classification plan, covering the masking check, the classifier comparison and the monthly drift check.