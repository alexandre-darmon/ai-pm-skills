Yes, you can have an answer by Friday. But I wouldn't do it as you've described, and I'd change three things before anything runs.

## What to change

**1. Don't send the real export to the model.**
- The export holds names, IBANs and account history for 2,000 customers.
- The account was opened on a company card with online terms. That makes it an unregistered third-party provider, with no processor agreement and no transfer terms.
- At a bank, that is a data-protection and operational-resilience problem. If it surfaced later, it would sink the project you're trying to start.
- "Only my team sees it" doesn't fix this. The disclosure to the provider is the issue.

**2. Remove the email-to-phone step.**
- Drafts quote customer details, and they would travel through email to a phone.
- The prototype would hold private data, read untrusted text (customer complaints) and have a way to send data out. That is the risky combination.
- Instead, write drafts to a local file and read them on your laptop. Nothing leaves.

**3. Get IT risk and the DPO moving in parallel, today.**
- The three months is for full approval of a product. A time-limited testing request for a spike is a much smaller ask.
- Send both a short note this morning: question, five-day box, synthetic data, and a request for a real-data pilot later.
- Don't wait on their answer for this week's work.

## The week, with data that doesn't need approval

**Monday: fix the question and the bar before building.**
- **Question:** "Can the model draft a first response that an adviser would send with only light edits, for our main complaint types?"
- **Bar:** write a target and a stop line per complaint type, and sign and date them. Fix the cost ceiling per usable draft, derived from what 25 minutes of adviser time costs.
- **Kill date:** Friday. A bar written after you've seen the results doesn't count.
- **Costly classes:** decide which complaint types you can't afford to get wrong, such as fraud, vulnerable customers or regulatory complaints. Hold those to a stricter bar.

**Tuesday: build the cases without real PII.**
- Pull 60–100 complaints, over-weighting the costly types. Have someone on your team replace names, IBANs, account numbers, dates and addresses with fake ones.
- Or write synthetic complaints from the real patterns. The aim is 40–120 cases, with the synthetic share stated in the report.
- Size each type before you start. At a 75% stop line you need about 19 cases per type to be able to read a good result. Ten cases can't show it.
- Keep the real export where it is and don't copy it to the laptop.

**Wednesday: run a simple script, then read before grading.**
- Use one model call per complaint, with your response policy in the prompt. Don't build an agent.
- Read the first 10–15 drafts before you score anything. Your definition of "good" will sharpen, so log each change to the criteria. The bar itself doesn't move.
- Use the model and hosting route you'd use in production, or neither the quality nor the cost will carry over.
- Check whether the company card account is acceptable even for synthetic data. Ask IT whether any approved route already exists.

**Thursday: grade with advisers.**
- Have two or three advisers grade each draft: send as-is, send after light edit, or rewrite.
- Report results per complaint type as "k of n" with a confidence interval, not one overall percentage. "9 of 10" is not evidence of a 90% rate.
- Compute cost per usable draft, which is spend divided by the drafts that were usable. Include adviser editing time, and log the hours you actually spent.

**Friday: decide.** There are three outcomes:
- **Go:** every type you can't drop is at or above the stop line, and cost is within your ceiling. Write it up as a case for a real project, with the untested types listed.
- **Reshape:** some type is undecided or short. Change one thing, such as narrowing scope or having the model only suggest the next step, and run a new spike with its own time box.
- **Stop:** a type you can't drop is clearly failing. Write down what you learned.

## What Friday's result can and can't say

- It can support "worth a real project", with the evidence labelled as a synthetic-data spike.
- It can't be quoted as the system's accuracy to risk, a committee or a regulator. A real project would need cases sampled from actual traffic and fixed criteria.
- The real-data test belongs in that project's first phase, as an approved, time-limited exercise.

## Next steps

I can draft the two short messages to IT risk and the DPO, and a one-page sign-off sheet for the question, bar, cost ceiling and kill date. I can also write the local script, which reads the cases from a file, drafts the replies and writes them to disk with no email step. Tell me which you want first.