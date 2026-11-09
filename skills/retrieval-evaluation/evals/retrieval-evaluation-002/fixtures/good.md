No, do not re-index now. With the right passage in the top 5 for 93% of questions, and labels pooled from three setups, retrieval is healthy: the unsupported deadlines and fees are a generation problem. A newer embedding model would not fix a model that states things absent from the passages it received.

1. Measure faithfulness at claim level: split each answer into atomic claims (each deadline, fee, condition) and check every claim against the passages sent. Report the share of answers with at least one unsupported claim per procedure family.
2. Store the 180 retrieved contexts and run every prompt variant on the same stored contexts, so only generation changes.
3. Fix the prompt: answer only from the passages, cite a passage for each claim, and abstain with a plain "not found in the procedures" when no passage gives the deadline or fee. Add questions whose answer is in no procedure to check abstention.
4. If a judge scores faithfulness, validate it against the procedure owners' labels (TPR and TNR) before it gates anything.
5. Re-measure; only if generation still fails on fixed contexts compare models.
