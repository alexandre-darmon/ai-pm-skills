**Don't start tomorrow. Two things need fixing first: the list itself, and masking.** I haven't seen any transcripts, so this review is based on the list alone.

## 1. Masking has to happen before labelling

Two HR assistants reading raw HR conversations is the exposure to avoid. These chats will contain names, employee IDs, IBANs, and health details (sick leave) and pay details.

- Mask first, using patterns for IBAN, email, phone and IDs, plus name recognition. Replace them with `[NAME]`, `[IBAN]`, `[EMAIL]` and so on.
- Check at least 100 masked conversations by hand, with the pass bar set beforehand:
  - No structured identifier left.
  - Name leaks under a limit your DPO agrees to.
  - A clean sample of 100 only shows the leak rate is below about 3%, not that it is zero.
- The labellers work only on masked text. Set a retention period and an owner for deleting it (GDPR art. 5(1)(c) and (e)).

## 2. Problems with the list

- **It has 14 classes, and the target is 8–12.**
- **Several classes overlap, so labellers will disagree:**
  - Leave request, Absence and Sick leave.
  - Expenses and Travel expenses.
  - Payslip and Salary questions.
  - IT access and Password reset.
  - Other and General question. Nobody can tell where a vague question goes, and "Other" will swell.
- **It looks drawn from an org chart, not from the data.** Real requests that don't fit, such as benefits, contracts, parental leave and policy lookups, will land in "Other". Keep "Other" under 10%.
- **There are no definitions, examples or tie-break rules.**

## 3. Corrected draft (v0.1, to be frozen after step 4)

| # | Class | Covers | Not this |
|---|---|---|---|
| 1 | Leave booking and changes | Request, cancel or change planned leave | Sick or unplanned absence (→3) |
| 2 | Leave balance and entitlement | Days left, carry-over, accrual rules | Booking the leave (→1) |
| 3 | Sick leave and unplanned absence | Reporting sickness, certificates, unplanned absence | Planned leave (→1) |
| 4 | Expense claims | Reimbursement of any expense, including travel receipts | Booking a trip (→5) |
| 5 | Business travel booking | Flights, hotels, trains, travel policy | Claiming the cost afterwards (→4) |
| 6 | Payslip and payroll | A specific payslip, deductions, payment date | Raise or band questions (→7) |
| 7 | Salary and compensation | Raise, bonus, pay band, review | Reading a payslip (→6) |
| 8 | IT access and passwords | Account access, resets, tools | HR questions (→10) |
| 9 | Onboarding | New-joiner steps, first-day questions | |
| 10 | HR policy and general information | How-to or policy question that fits no class above | Out of scope (→11) |
| 11 | Other / unclear | Out of scope, greetings, empty or unreadable | |

That makes 11 classes. Rules to write into the guide:
- **Several requests in one conversation:** take the class of the first request the user states.
- **Escape hatch:** low-confidence or unclear conversations go to 11 or to a review queue, not into a guess.

The examples and counter-examples for each class must come from the masked sample, not from me. I haven't seen any transcripts, so any I wrote would be placeholders.

## 4. Before the 200 are labelled

1. Mask the conversations and run the check.
2. Read about 50 masked conversations. Write a one-line note on what each person wanted. Adjust the draft until new conversations add no new class. Likely additions are benefits, parental leave and contracts. That is a guess to test, not a finding.
3. Freeze the taxonomy as a numbered version. Write the guide with a definition, two examples and a counter-example per class.
4. Sample the 200 across months and channels, not just the most recent ones.
5. Have both labellers label at least 50 of the same conversations. Their agreement is the ceiling for any later automated classifier.
6. Any change after freezing is a new version, and the labelled set is relabelled.

I can turn this into the full annotation guide once the masked sample exists. Do you know who can run the masking and agree the leak limit with the DPO?