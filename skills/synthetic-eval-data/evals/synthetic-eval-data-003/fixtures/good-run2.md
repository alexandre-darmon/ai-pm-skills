**Short answer:** Stop treating the 500 questions as your quality number. Keep them as a regression check on clean English. Build a new test set from the 1,800 real conversations, and use synthetic data only to fill gaps in it.

**Why the 94% misleads.** The set differs from your traffic in four ways, and each one makes it easier:
- **Language:** it is English, and your customers write mostly French.
- **Style:** it is tidy, 22 words per question, with no typos, accent loss or code-switching.
- **Topic mix:** it is spread evenly over six topics, while repayment difficulties and early settlement dominate real traffic.
- **Origin:** an LLM wrote it, so the questions are the ones your team would imagine. They are not the ones customers ask.

The 94% is probably accurate for what it measures. It just doesn't measure your pilot.

**What to do**

1. **Relabel the old set.** Report it as "clean English, synthetic, regression only". Never put it next to a headline score again.

2. **Run error analysis on the pilot first.** Read the escalated conversations, a few dozen to start. Note why each one failed: a misunderstood message, a wrong answer, a missing policy, or a case that should have gone to a human. Those failure types become your test dimensions. Without this step you will build another set that misses the problem.

3. **Sample real conversations into the new set.**
   - Stratify by topic, but over-sample the risky classes. Repayment difficulty is probably the highest-stakes one, since it involves vulnerable customers.
   - Include escalated and non-escalated cases, and keep the real messy phrasing.
   - Mask personal data before anything goes into the set.
   - Have domain experts write or approve the expected answers, citing the policy or document. The assistant itself must never write them.
   - Keep a separate holdout that nobody tunes against.

4. **Use synthetic data only for gaps.** Examples are rare but risky cases (a legal threat, a fraud claim) and combinations that the pilot hasn't produced yet.
   - Define dimensions from real traffic: topic, French with typos and no accents, mobile, English mixed in, missing loan number, two requests in one.
   - Generate the combinations (tuples) first, and have experts review them.
   - Then write the messages in a separate step, using real messages as style anchors.
   - Prefer a generator from a different model family than the assistant.
   - Have experts reject unrealistic messages. Then compare length, language share, typo rate and topic mix with real traffic.
   - Flag every synthetic case as synthetic.
   - Never paraphrase one real person's case.
   - Don't reuse these cases in prompts or few-shot examples.

5. **Report differently.** Show scores per topic and per language and style, with the real and synthetic cases separated, and the synthetic share stated per class. Weight the headline number to match real traffic. Check that the new set reproduces your actual escalation rate, because if it doesn't, it's still not measuring the right thing.

6. **Keep refreshing.** Sample new real conversations each month, and retire synthetic cases class by class. Set a target date after which a class that is still mostly synthetic gets reported as "indicative".

**Order of work:** error analysis on escalations, then the real-sample set with expert answers, then synthetic gap-filling, then the new reporting. The first two steps take days, not weeks, and the first one will probably tell you what to fix in the assistant itself.

I can draft the synthetic-set spec (dimensions, tuple plan, flag schema, replacement dates) if you want. I'd need a sample of the pilot conversations, or at least the topic and escalation counts, to ground it.