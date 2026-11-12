Yes, an LLM can plausibly answer this by Friday. But two parts of your setup need to change first, and I'd change them before anything runs.

## What to change

**1. Don't send the real export through this account.**
- The export has names, IBANs, account history and full complaint text. A model account opened on a company card with online terms is an unregistered third-party ICT arrangement. In a bank that triggers DORA third-party risk and register rules.
- Personal data sent to it also needs processor terms and a transfer assessment, which is a question for your DPO.
- A prototype counts as non-production use. Under the ICT rules that means synthetic, anonymised or pseudonymised cases only. "Nobody outside my team sees it" doesn't change that, because the exposure is the data leaving to the provider.
- This could cost you more than three months of IT approval. A data incident involving customer IBANs would end the project and could do worse to you personally.

**2. Don't have the script email drafts.**
- The prototype would hold private data, read untrusted text (complaints are written by customers) and have an outbound channel. A prompt-injection line in a complaint could then push data out.
- Remove one leg in code. Have the script write drafts to a local file and read them there. Reading on your phone isn't worth the risk for a feasibility test.

## What you can do this week without waiting for IT

**Monday: write down the question and the bar, and get them signed.**
- The question is: "Can the model draft a first response that an adviser would send with light edits, at a cost well under the cost of 25 minutes of adviser time?"
- Set the appetite: five days, a cost ceiling per *correct* draft, and a kill date of Friday. Derive the ceiling from what 25 minutes of adviser time costs. Your volume is about 1,450 adviser-hours a month.
- Set a bar and a stop line for each complaint class. Give the riskiest classes, such as fraud, vulnerable customers, regulatory or ombudsman threats and mis-selling, the stricter target.
- Write these down before you see any output. Don't move them afterwards.
- Also on Monday, email IT risk and your DPO in parallel, asking for a sanctioned route or an approved testing occasion. Synthetic work doesn't have to wait for their answer.

**Tuesday: build the cases.**
- Use synthetic or properly anonymised complaints modelled on your real mix. Have someone who knows the real distribution write them, and use your own judgment on realism. Don't paste real text with names swapped.
- Aim for 40–120 cases in total. A class with a stop line of 80% needs about 25 cases to ever read as promising. At 10 cases, even 10 of 10 can't clear a 75% line.
- Over-represent the costly classes and state what share is synthetic.
- Have your advisers write or approve a reference first response for a subset, so you have a standard to compare against.

**Wednesday: run it as a single model call, not an agent.**
- Code does the lookups. The model drafts from complaint text plus your response policy, tone guide and templates.
- Use the model and hosting route you'd use in production, otherwise neither quality nor cost transfers.
- Read the first 10–15 outputs *before* scoring. Your definition of "correct" will sharpen. Log each change to it and re-grade everything under the final criteria.

**Thursday: grade with 2–3 advisers on synthetic cases.**
- Grade per class, as n of N with a confidence interval, not one pooled rate.
- Track the errors that matter most: wrong promises, wrong regulatory wording, missed vulnerability flags, and invented facts about the account.
- Record cost per *correct* draft (spend ÷ correct drafts, not ÷ all drafts). Include the time advisers spend fixing wrong ones.
- Record hours from logs, not impressions.

**Friday: decide.**
- **Go:** every class you can't drop is promising or clears, and cost is within appetite. Take it to a proper project with IT approval.
- **Reshape:** one class is undecided or cost is too high. Change one thing and run a new spike.
- **Stop:** a class you can't drop is dead.

## What to tell your sponsor

A spike on a few dozen synthetic cases is evidence of feasibility, not of accuracy. Don't quote the percentage as the system's accuracy to risk, compliance or a regulator. A real project would need cases sampled from actual complaints, frozen criteria and a private holdout. That is also the point where real data is legitimate, through an approved route.

## Three things I need from you

1. What complaint classes do you use, and which ones can't the product drop?
2. What does an adviser-hour cost, so we can set the cost ceiling?
3. Which model and hosting route would production use?

Once you've answered, I can write the spike report skeleton with the bar, appetite and kill date. I can also build a harness that reads synthetic cases from a file, drafts responses, and prints n of N per class with cost per correct draft, with output going to a local file only.