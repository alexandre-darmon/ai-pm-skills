I can help you answer the question by Friday, but not with the plan as written. The real-data version is the part most likely to end the project before it starts.

## Why I'd change the plan

- **Real customer data on an unapproved account.** Names, IBANs and account history would go to an API account opened on a company card. At a bank that is an unregistered third-party arrangement. Under GDPR it also lacks processor terms and transfer terms. "Prototype" and "team only" don't change that.
- **A full CRM export in a spreadsheet on a laptop.** That is a copy of 2,000 customers' data outside your controls.
- **Drafts emailed to your phone.** This is the worst leg. The script would read private data and untrusted text (the complaints themselves, which can contain instructions). It could also send data out by email. With all three together, an injected instruction could mail customer data somewhere else. Drop the email.
- **The cost of getting caught.** A data-handling incident would kill the project and could hurt you personally. A 3-month IT approval is a problem, but this risk is worse.

You don't need real data to answer a feasibility question. You need realistic cases.

## Plan for the week

Your Friday deadline may leave only 2–3 working days, since today is Wednesday 11 Nov. This version fits that, and anything that doesn't fit gets cut.

**Today (Day 1) – fix the question, and ask IT in parallel**
1. **Write the one question and sign it.** For example: "Can the model draft a first response that an adviser would send with light edits, in at least X% of cases, at under Y per correct draft?"
2. **Set the bar before running anything.**
   - Put a target and a stop line on each complaint class.
   - Set the strictest bar on the classes that cost most when wrong: vulnerable customers, fraud and unauthorised transactions, and anything with a regulatory deadline or an ombudsman threat.
   - Work out the value of one correct draft from the 25 minutes of adviser time, at 3,500 complaints a month. That sets your cost ceiling per correct answer.
   - Set a kill date of Friday.
3. **Send IT risk and the DPO a one-page note today.** Ask two things:
   - Does the bank already have an approved model route, such as an enterprise cloud contract?
   - Can they grant a time-limited testing exception for pseudonymised data?

   Synthetic work doesn't wait on their answer, and the note starts the clock on the real project. I can draft it.

**Day 2 – build the case set (synthetic)**
- Aim for about 60–100 cases. A class with only 10 cases can't show a clear pass even if every draft is right, so 15–35 per class that you gate on is the working range.
- Have advisers write the complaints from their experience of real patterns, with invented names and IBANs and no real details. Over-represent the costly classes and include messy, angry and ambiguous complaints.
- Don't try to scrub real complaint text. Free text leaks identifiers in ways redaction misses, and the result is still personal data.
- Use fake account-history fields in the same shape the CRM would supply.
- Write a short "what a good first response contains" checklist per class. This covers the apology, the factual acknowledgement, next steps, the regulatory timeline and no promises about the outcome.

**Day 2–3 – run it**
- Use one model call per case, with a fixed prompt. Your code does the lookups and the model drafts. Don't build an agent.
- Use the model you'd use in production. Otherwise neither quality nor cost carries over.
- Write the drafts to local files. Don't send email.
- Read the first 10–15 drafts before grading anything, then fix your definition of "correct" if it was off. Log each change, and don't move the bar.

**Day 3 – grade and decide**
- Have 2–3 advisers grade each draft blind against the checklist: send as is, send with light edits, or rewrite.
- Report results per class as "k of n" with a confidence interval, not one pooled percentage.
- Report cost per correct draft, not per draft. Also report the hours you spent, from logs.
- Decide one of three ways:
  - **Go to a real project.** Every class you can't drop is promising or clears, cost is within the ceiling, and the data route is resolved.
  - **Reshape.** One class is undecided or short, so change one thing and re-run.
  - **Stop.** A class you can't drop is clearly failing.

## What Friday's result is and isn't
It tells you whether a real project is worth funding. It is not evidence of production accuracy. Don't quote it to a steering committee or a regulator as the system's accuracy. A real project would test on cases sampled from live traffic, with frozen criteria and a larger sample per class.

## What I can do next
1. Draft the one-page note to IT risk and the DPO.
2. Draft the question, bar and appetite sheet for you to fill in and sign.
3. Build the harness: a case-file format, a prompt template, a runner that writes drafts to local files, and a readout script giving per-class results and cost per correct draft.
4. Write a prompt for generating realistic synthetic cases for your advisers to edit.

Which should I start with? I'd begin with the IT/DPO note and the harness. For the bar sheet I'll need your complaint classes and a rough value per correct draft.