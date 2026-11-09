**Recommendation: don't approve the switch yet. Approve a one-week diagnosis first, and bring the switch back to the committee only if the data supports it.**

**Why the claim doesn't hold yet**
- 71% comes from 200 answers, so the real figure is roughly 64–77% (95% interval). It also doesn't say why the other 58 answers failed.
- A larger LLM only fixes one of four failure points: wrong use of a passage it was given. It can't fix a failure at any of the other three:
  - **Coverage:** the answer isn't in any document.
  - **Chunking:** the answer is split across 512-token pieces, or a table lost its header.
  - **Ranking:** the right passage isn't in the top 5.
- Your setup makes the other three likely. There are 14 years of product versions, so the top 5 can easily be the superseded wording. Special conditions and endorsements override general conditions, so a question may need several passages, and 5 pieces may not hold them all.
- The 85% figure is a guess until someone shows that generation is where the failures are.

**Step 1: attribute the 58 failures (1–2 days, no new infrastructure)**

Two senior agents re-open each failed log entry. They have the retrieved top 5 stored, and they mark the first stage that failed:
- **Not in the corpus:** no document contains the answer.
- **Not retrieved:** the passage exists but wasn't in the 5 sent.
- **Wrong version:** the passage was retrieved but is superseded.
- **Split or stripped of context:** the answer is cut across chunks, or a table lost its header.
- **Misused:** the right passage was sent and the LLM got it wrong.

Decision rule:
- If "misused" is the largest group, the larger LLM is justified. Test it as in step 2.
- If it isn't, the switch would spend 4× per call without fixing the main problem. Fix the largest group first (reranking or hybrid keyword search, chunking by document structure, version and effective-date filtering, or a larger k).

**Step 2: test any change on frozen inputs**
- Build a set of about 200–300 real questions from logs, split by type: simple lookup, multi-document, date or version-specific, and amount or exclusion questions. Include some unanswerable questions that look in scope, such as another product or a period not covered. The correct answer to those is "not found, ask a person", and today you have no measure of that.
- Have your agents label which passages are relevant. Pool candidates from several retrievers, not just the current system's top 5. Double-label 20% of questions.
- Measure retrieval and generation separately:
  - **Retrieval:** is the needed passage in the 5 sent, per question type?
  - **Generation:** store the retrieved passages and run the old and new LLM on the same ones. That way a retrieval change can't be mistaken for a model change.
  - **Faithfulness:** any claim unsupported by the passages counts as a failure for amounts, exclusions and deadlines.
- Compare old and new on the same questions, paired, per question type. If the two versions differ on only d questions, a gap smaller than 2√d ÷ n is a tie.

**How to show it worked**
- A pre-agreed threshold per question type, not one global number. For example, a higher bar for exclusions and amounts than for simple lookups.
- Results with confidence intervals, on a private holdout set the build team hasn't tuned against.
- Cost per correct answer, not cost per call. A 4× price is justified only if quality rises by more than 4×, which is impossible from 71%. It would need other value, such as fewer escalations or less agent time spent checking. If that is the argument, measure it.
- A production check afterwards: sample and grade logged answers each month, using the same labelling process.

**For Thursday**
1. Don't approve the LLM switch now.
2. Approve a one-week diagnosis (the 58 failures, then the labelled set).
3. Agree the decision rule and the pass thresholds before seeing results.
4. Ask the data science team how they got to 85%. If it came from a benchmark rather than your own failures, treat it as unproven.

I can draft the one-page committee note or the labelling sheet for the 58 failures if you want either.