I checked the list against the method. **It isn't ready for tomorrow.** Fix the five problems below first; they should take about an hour.

**1. Too many classes, and they overlap (8–12 mutually exclusive classes is the target).** There are 14 now.
- **Leave request, Holiday balance, Absence and Sick leave** will be confused constantly. "I'm off Friday, am I sick-listed?" fits three of them. Merge them into **Leave & absence**, or keep two classes: *Leave booking* (request and balance) and *Sickness/absence reporting*.
- **Expenses and Travel expenses** overlap. Merge them into one class, or add a written rule such as "any claim for money back is Expenses, even if travel-related".
- **Travel booking** is a separate action from expense claims, so keep it.
- **Payslip and Salary questions** overlap in the same way. Merge them into **Pay**, or add a rule.
- **IT access and Password reset** overlap. A password reset is an IT access problem, so merge them, or define Password reset narrowly.

Merging as above gives roughly: Leave & absence · Sick leave · Expenses · Travel booking · Pay · IT access · Onboarding · Other · General question. That is 9 classes, within the target.

**2. "General question" and "Other" are ambiguous.** Labellers can't tell them apart. Either drop "General question", or define it (for example, HR policy questions that fit no specific class) and keep "Other" for everything else, including off-topic conversations. Aim to keep "Other" under 10% of conversations. If labellers use it more than that, the taxonomy is missing a class.

**3. There are no definitions, examples or counter-examples.** Each class needs a one-line definition, two examples and one counter-example, written into an annotation guide. Without these, two labellers will disagree for no useful reason.

**4. There are no edge-case rules.** You need at least these two:
- Multi-request conversations: "a conversation with two requests takes the class of the first one the user states."
- Conversations where the assistant couldn't tell what the user wanted.

**5. Personal data must be masked before anyone reads the conversations.** These are HR conversations, so they will contain names, employee IDs, IBANs, health details (sick leave) and salary figures. Before the labellers see anything:
- Replace structured data with placeholders (`[NAME]`, `[IBAN]`, `[EMAIL]`, `[EMPLOYEE_ID]`) and apply named-entity recognition for names.
- Hand-check at least 100 masked conversations and record the leak rate.
- Confirm that the two HR assistants are allowed to read this data at all. Data minimisation (GDPR art. 5(1)(c)) argues for showing them masked text only.

Mask first, then freeze the taxonomy. The taxonomy should be frozen before labelling starts. If you change it afterwards, the labelled set has to be relabelled.

**Sampling and agreement for the 200 conversations**
- Sample across the whole January–now period and across all channels. Don't take the most recent conversations or one slice.
- Have both labellers independently label at least 50 of the 200. Their agreement is the ceiling for any later automated classifier, so this overlap is how you'll know how reliable the labels are.

**Questions for you**
- What decision will the results feed (knowledge base priorities, cost per outcome, ROI)? That determines which other dimensions to label, such as resolution or sentiment. Skip any dimension that feeds no decision.
- Is there masking in place already, and who approved the HR assistants' access?

I can draft the revised taxonomy and annotation guide, and a short masking-check plan, if you'd like. I'd need your answers to the two questions above first.