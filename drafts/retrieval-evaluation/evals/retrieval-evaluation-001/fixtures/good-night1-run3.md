**Recommendation: don't approve the switch yet. Ask the committee to approve a one-week diagnosis first, with a decision rule agreed in advance.**

**Why not switch now**

- **The 71% is a rough figure.** 142/200 has a 95% Wilson interval of about 64% to 77%. The sample also doesn't say which question types fail. It likely has no unanswerable questions, where the right answer is "not found, ask a colleague".
- **The 85% has no stated basis.** Ask the data science team what it rests on. A bigger LLM can only fix failures where the right passage was already in the 5 pieces sent. If the passage isn't in those 5 pieces, a larger model will answer from the wrong text, or guess.
- **Your corpus makes retrieval failures likely.** It has 2,300 PDFs across 14 years of product versions, 512-token pieces and only 5 sent. Likely problems:
  - The wrong version of a clause is retrieved.
  - An exclusion or amount sits in a different piece from its header or conditions.
  - A question needs both the general and the special conditions, and only one comes back.
- **The cost is steep.** At 4× the price, cost per correct answer goes from 1/0.71 ≈ 1.4 to 4/0.85 ≈ 4.7 units, about 3.3× more. Even a perfect model would cost more per correct answer than today.

**The one-week diagnosis (the senior agents can do it in about a day)**

1. Take the 58 wrong answers. For each, find the stage where it first failed:
   - **Coverage:** the answer isn't in any document.
   - **Chunking:** the answer is split across pieces, or a table lost its header.
   - **Ranking:** the right piece wasn't in the top 5.
   - **Stale version:** a superseded document was retrieved.
   - **Generation:** the right piece was sent and the model still got it wrong.

   This needs the retrieved pieces from the logs. If they weren't logged, start logging them now.
2. Build a query set by class, such as simple lookups, multi-document questions, time-bound or version questions, and exclusion or amount questions. Add 30 to 50 unanswerable questions. Have experts label the relevant passages. Pool candidates from the current index, keyword search and a second embedding model, so the current system isn't graded on its own results.
3. Score retrieval and generation separately:
   - Report recall at k=5, per class, with intervals.
   - Run the generator on stored contexts, so a retrieval change can't move the generation score.
   - Check faithfulness claim by claim. In your domain, one wrong amount or exclusion fails the answer.
   - Check abstention on unanswerable questions.
4. Test cheaper fixes: a larger k (say 8 to 10) against the cost of its extra tokens, a reranker, hybrid keyword and dense search, structure-aware chunking with document title and version on every piece, and filtering by effective date.

**Decision rule to agree now**

- If most failures are in coverage, chunking, ranking or versions, fix those. A bigger LLM is not justified.
- If generation on correct contexts is the busiest failure stage, test the larger model on fixed contexts. Adopt it only if it beats the current model on the classes that matter, and only if cost per correct answer is acceptable. It could be used just for the hard classes.
- If the failures are mixed, fix retrieval first and then re-measure. Retrieval fixes are usually cheaper.

**How to show it worked**

- Use a fresh set of questions that nobody tuned against, graded blind by the same two senior agents. Include the unanswerable questions.
- Compare the old and new versions on the same questions. Count d, the questions where exactly one version is right. A gap smaller than 2√d ÷ n is a tie. Gate per class, not on the overall average.
- Set targets before the test, for example no class below an agreed floor and a near-zero rate of wrong amounts or exclusions. Don't quote "85%" without its interval.
- After launch, keep sampling real answers every month, and re-run the test whenever the index, chunking or corpus changes.

**Slide for Thursday**

- **Ask:** one week and two agent-days, to find where the 58 failures happen.
- **Decision:** switch the LLM only if generation turns out to be the main failure stage.
- **Risk of switching now:** about 3.3× the cost per correct answer, with a likely small gain if the cause is in retrieval.

I can draft the full evaluation plan (query classes, labelling protocol, sample sizes, k and cost table) as a one-pager for the committee. Do you have the retrieved pieces in the logs, and what is your monthly call volume? With those I can put real numbers on the cost comparison.