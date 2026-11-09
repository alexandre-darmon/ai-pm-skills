Recommendation for Thursday: do not switch the LLM yet. A larger model only fixes generation, and nobody knows yet whether the 29% of failures come from generation or from retrieval. The 71% on 200 answers also carries an interval of about 64% to 77%.

1. This week, re-read the 58 failed answers. For each one, check whether the passage that holds the right answer was in the top 5 pieces sent to the model. That splits failures by stage: answer in no contract (coverage), split across two pieces (chunking), not in the top 5 (ranking), or present but misused (generation).
2. Build a query set from the logs, per class (cover questions, exclusions, deductibles and amounts, older product versions), and add unanswerable questions whose answer is in no document, with a plain "not found" as the expected answer.
3. Have senior agents label relevance on candidates pooled from several retrievers (the current index, a keyword search, a second embedding model), not only on what the current system returns.
4. Score retrieval first: recall@5, at the 5 pieces the LLM actually receives, per class with its interval.
5. Score generation on the same stored contexts for every model, so the larger LLM is compared on fixed contexts: claim-level faithfulness, answer relevance, correct abstention.
6. Only if generation is the busiest stage does the model change come back, with cost per correct answer at four times the price.
