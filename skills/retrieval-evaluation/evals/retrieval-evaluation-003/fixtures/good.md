I cannot confirm the plan as it stands, for two reasons.

First, the test set has only answerable questions. Add unanswerable questions, ones whose answer is in no policy (a benefit you do not offer, a country you do not cover, a period no policy covers), with a plain "not found, ask HR" as the expected answer. Without them you cannot see the assistant inventing a rule.

Second, the MTEB leaderboard says nothing about your 420 policies or how employees phrase questions in French, German and Polish. Treat the swap as a release:
1. Build the new index next to the current one and keep the old index for rollback.
2. The new model will surface sections nobody judged: have HR experts label them first (pooled with the old results), or it is penalised unfairly.
3. Run the 120 questions plus the new ones on both models, paired on the same questions: count d, the questions where only one hits; a gap under 2√d ÷ n is a tie.
4. Compare per language and per policy family, at the top 4 sent to the model. Switch only if no class loses.

Draft change note: "Embedding model change postponed until the paired comparison passes per language; rollback to the current index kept."
