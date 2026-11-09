**Short answer:** Don't throw the 500 away, and don't just top them up with more of the same. Demote them to a "clean-input regression" set. Build the main eval from your 1,800 real conversations, and use synthetic data only to fill gaps in that real set.

**Why the 94% is misleading**
The set differs from your traffic in every way that matters:
- **Language:** clean English versus mostly French.
- **Style:** 22-word well-formed questions versus short phone messages with typos, no accents and mixed English.
- **Topic mix:** an even split over six topics versus two topics making up most of the traffic.

The 94% is a valid number for the population the set describes. Your customers aren't that population. The high escalation rate is the real signal.

**What to do**

1. **Keep the old set, relabelled.** Report it separately as "synthetic, clean English". It still catches regressions and basic knowledge errors. Never report it as the headline number.

2. **Build a real-traffic set from the pilot.**
   - Sample the 1,800 conversations, masking personal data first.
   - Stratify the sample so repayment difficulties and early settlement dominate, as in traffic. Also oversample the escalated conversations and the risky cases, such as vulnerable customers or legal threats.
   - Have domain experts write or approve the expected answers, citing the source document. Don't let the assistant or the question-generating model write them.
   - Keep a holdout that is never used for prompt tuning or few-shot examples.

3. **Do error analysis on the escalations first.** Read a few dozen escalated conversations and name the failure modes: French understanding, missing accents, topic knowledge, a failure to hand off. That tells you which dimensions matter, and it will probably explain most of the gap.

4. **Use synthetic data only for gaps.** Rare but risky classes, or topics with too few real cases, are where it helps.
   - First define dimensions from real traffic and your failure notes: topic, persona, language style, missing information.
   - Then generate tuples, have experts review them, and only afterwards write the questions.
   - Ask for the real style: typos, no accents, French–English mixing, fragments.
   - Use a generator from a different model family than your assistant.
   - Have experts reject unrealistic questions.
   - Compare length, language share, typo share and topic mix against real traffic, with tolerances written beforehand.

5. **Flag and report separately.** Every case should carry an `origin` (real or synthetic) tag. Report the score on real and on synthetic cases separately, and show the synthetic share per topic. Don't let synthetic cases into the holdout, prompts or few-shot examples.

6. **Retire synthetic cases on a schedule.** As real traffic arrives, replace synthetic cases topic by topic, with a target share and a date. Refresh the real set regularly, since traffic drifts.

7. **Check the judge, if you use one.** An LLM judge needs validating against expert labels. It's especially important in French, where judges are less reliable.

**Expect lower numbers.** The first score on the real set will likely be well below 94%. That is the number that tracks your escalation rate, and you can improve against it.

I can draft the spec for the real-traffic set next if you'd like, covering the sampling plan, dimensions and flag schema. It would help to know whether you have access to the conversation logs and which domain experts can write the expected answers.