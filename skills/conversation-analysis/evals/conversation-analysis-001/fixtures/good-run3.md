The list isn't ready to use yet. I'd fix four things before tomorrow.

**1. Too many classes, and several overlap**

The method calls for 8–12 mutually exclusive classes, and this list has 14. Labellers will disagree on these pairs:

| Overlap | Example of the problem |
|---|---|
| Leave request / Holiday balance / Absence / Sick leave | "I'm off sick Monday, how many days do I have left?" fits all four. |
| Expenses / Travel expenses / Travel booking | "Can I claim the hotel I booked?" fits all three. |
| Payslip / Salary questions | "Why is my net pay lower this month?" fits both. |
| IT access / Password reset | A password reset is an IT access request. |
| Other / General question | These two are indistinguishable, so "Other" will swell. |

**2. Suggested merges**

This gives about 8 classes:
1. Time off (request or balance)
2. Sickness and other absence
3. Expenses (including travel expenses)
4. Travel booking
5. Pay (payslip and salary)
6. IT access (including password reset)
7. Onboarding
8. HR policy or general question
9. Other (residual only, kept under 10%)

Before you merge, check whether a decision depends on the split. For example, you may need holiday balance volume on its own to prioritise the knowledge base. If so, keep it as its own class.

**3. Missing from the list**

- **Class definitions:** each class needs a definition, two examples and a counter-example.
- **A tie-break rule:** for example, "a conversation with two requests takes the class of the first one the user states".
- **Possibly missing classes:** the list has nothing for benefits, contracts, offboarding or complaints. Skim a masked sample of 50 or so conversations to see whether any of these is common before you freeze the list.
- **A frozen version:** freeze and version the taxonomy before labelling. A change after that means relabelling everything.

**4. Personal data comes before labelling**

Sick leave and salary conversations contain health and pay details, plus names and employee ids. Mask them first (typed placeholders such as `[NAME]` and `[EMAIL]`), then check 100 or more masked conversations by hand and report the residual leak rate. The HR assistants should only see the masked text. If you plan to use a model to help draft or test the taxonomy, it also only sees masked text.

**Setup for the 200 conversations**
- Sample them across the whole period (January to now) and across channels. Don't just take the most recent ones.
- Have both labellers label at least 50 of the same conversations. Their agreement is the ceiling for any later automated classifier.
- Write a short annotation guide with the edge-case rules, and track how often "Other" is used.

If you send me the masked sample, or the current definitions, I can draft the class definitions, examples and tie-break rules, and the classification plan.