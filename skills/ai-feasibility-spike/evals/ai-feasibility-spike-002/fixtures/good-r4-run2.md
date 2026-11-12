I can help you plan the week. The plan as you described it has two problems, and I'd fix them before Monday.

## What to change

**1. Don't put the real export into the model.** It has customer names, IBANs, account history and full complaint text. The model account was opened on a company card with online terms, outside procurement. That makes it an unregistered third-party arrangement, which needs a DPO and IT-risk answer under GDPR and DORA. A laptop script that sends customer data to it is an unauthorised tool handling production personal data. If something goes wrong, "it was only a prototype" won't protect you or the bank. Complaints about a bank are also a regulated process.

You can still finish by Friday without the real data:
- **Synthetic or anonymised complaints.** Have the model write realistic complaints by category, or strip names, IBANs and account numbers from real ones. Be careful with free text, because people put identifying details in it. Real complaints are better for realism, but only if someone with authority approves the de-identification.
- **Ask IT risk and the DPO in parallel on Monday.** Ask for a time-limited testing exception. Synthetic cases don't need to wait for the answer.

**2. Remove the email-to-phone path.** The script would read private data, read untrusted text (complaints can contain anything) and send content out by email. That combination is a data-leak risk. Instead, write the drafts to a local file and read them on your laptop. If you need to read on your phone, use synthetic data only.

## Week plan

**Monday: set the rules before building.** Write these down and have your head of complaints sign them. Don't change them after you've seen results.
- **The question:** can the model draft first responses that an adviser would send with only light edits? Draft it as a yes/no, e.g. "for at least X% of cases per category, an adviser needs under 5 minutes of edits".
- **Time box:** this week, with a stop on Friday.
- **Bar per category:** a target rate and a "not worth pursuing" rate. Be stricter on the costly categories, such as vulnerable customers, fraud and regulatory deadlines.
- **Cost ceiling:** what one usable draft is worth. 25 minutes of adviser time × 3,500 complaints is roughly 1,450 hours a month. That is your benchmark.
- **Sample size:** at least 15–25 cases per category you can't drop, and about 50–120 in total. You don't need 2,000. A stop line of 80% needs about 25 cases in each category.

**Tuesday: build the cases.** Create the synthetic or anonymised set, over-represent the costly categories, and write down what a good response must contain. For example: the right acknowledgement, the right complaint reference, the correct regulatory wording and timelines, no promise of redress, and the right escalation. Get an adviser to define "good" with you.

**Wednesday: build the simplest thing.** One model call per complaint, with your template and policy text in the prompt. Your code does the lookups, and the model does the writing and judgment. Don't build an agent. Run it on the model and hosting route you'd use in production, otherwise the quality and cost won't carry over.

**Thursday: read, then grade.** Read the first 10–15 drafts before scoring anything, because your definition of "correct" will sharpen. Log any criteria changes with dates, then re-grade everything. Have two advisers grade blind.

**Friday: report per category.** Give counts like "22 of 25 usable" with a confidence interval, not one overall percentage. A few good drafts on a small sample are not proof. Report cost per *usable* draft (spend ÷ usable drafts), and add the time advisers spend fixing bad ones. Then decide:
- **Go to a real project:** every category you can't drop is promising or clears, and cost is within the ceiling.
- **Reshape:** one category is undecided or short, or cost is too high. Change one thing and run a new time-boxed spike.
- **Stop:** a category you can't drop clearly fails.

## What Friday's result will and won't tell you

It will tell you whether the idea is worth a funded project. It won't be evidence of accuracy to give a regulator, model risk or the board. A real project needs a larger test set sampled from actual traffic, frozen criteria and a private holdout.

## Next steps

I can draft the Monday one-pager (question, bars, sample sizes, kill date) and the message to IT risk and the DPO. I can also write the synthetic-case generator and the single-call drafting script, writing to local files only. Shall I start with the one-pager and the DPO note?