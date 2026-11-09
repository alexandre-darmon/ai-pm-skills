Your 94% was measuring the wrong thing, and you now have real traffic to replace it. The 500 questions answer "does the assistant handle tidy English on all six topics?", which isn't your pilot. So don't fix the old set. Demote it and build a new one from the pilot conversations.

**1. Demote the old set.**
- Keep it as a regression smoke test for clean-input behaviour, and label it that way.
- Stop quoting 94% as a quality figure.
- Don't tune prompts against it any further.

**2. Build the main set from real conversations (this is the big change).**
- You have 1,800 real conversations, so make real cases the core of the set and use synthetic ones only to fill gaps.
- Sample them stratified by topic. Over-sample escalated conversations, because that's where the failures are.
- Mask personal data first.
- Start with a read-through of about 100 escalations to find out why they escalate. Typos and French may not be the cause. Missing knowledge, wrong policy answers, or failure to detect distress on repayment difficulties are all plausible. This error analysis tells you which dimensions to test.
- Have domain experts write the expected answers or expected behaviour, citing policy documents. The assistant must not write them.

**3. Match the set to real traffic.**
- Compare it with the pilot on median and 90th-percentile length, French share, share with typos or missing accents, English mixing, and topic mix.
- Write your tolerances down before you generate or sample anything.
- Weight the set toward repayment difficulties and early settlement. The remaining four topics still need enough cases to catch regressions.
- Report scores per topic. Don't report one global number, because a single average hides exactly the gap you just ran into.

**4. Use synthetic data only for rare or risky gaps.**
Examples are a vulnerable customer, a legal threat, or a topic with too few real cases.
- Define the dimensions first: topic, intent, persona, channel, language and writing style, and edge conditions such as a missing loan number or two requests in one message. Ground each value in a real conversation or an error-analysis finding.
- Generate the combinations of dimension values first, and write the question text in a separate step.
- Use real messages as style anchors, and ask explicitly for typos, missing accents and French/English mixing.
- Prefer a generator from a different model family than the assistant. Have experts review every input and reject unrealistic ones.
- Never paraphrase an individual customer's case.

**5. Keep the books honest.**
- Tag each case as real or synthetic, with generator, date and reviewer.
- Report scores separately for real and synthetic cases, and state the synthetic share per topic.
- Keep synthetic cases out of prompts, few-shot examples and fine-tuning data.
- Each month, add fresh real cases and retire synthetic ones. Treat a topic that's still mostly synthetic after your target date as indicative only.
- Hold out a portion of the real cases that nobody tunes against.

**6. Check the measurement.**
- If you use an LLM judge, validate it against expert labels on a sample before trusting it.
- Check that the new set explains the escalations. If the assistant fails the cases that escalated and passes the ones that didn't, the set is measuring the right thing. If not, go back to the error analysis.

**Order of work:**
1. This week: read about 100 escalations and sample the real set.
2. Next: experts write the expected answers.
3. Then: measure the assistant on the real set to get an honest baseline.
4. Last: add synthetic cases for the gaps that remain.

I can draft the sampling plan, the dimension table, or the set spec template if you want. I can't see your data from here, so I'd need the conversation export to do the sampling.