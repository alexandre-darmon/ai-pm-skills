---
name: retrieval-evaluation
description: 'Evaluate a RAG or search feature in two stages, retrieval then generation. Use when answers are wrong or cite the wrong document, before changing the LLM, or for a new embedding model or re-index.'
stage: evaluate
version: 0.1.1
depends_on: [build-evals, ai-data-requirements, llm-judge-calibration]
feeds: [release-to-production, model-selection, ai-data-requirements, system-prompt-and-guardrails, production-evals-monitoring]
autonomy_relevant: false
sources: [manning-ir, es-ragas, husain-shankar-evals, anthropic-evals, miller-error-bars, own-rag-practice]
eval_threshold: 0.80
status: tested
---

# retrieval-evaluation

## When to use
- "Our document assistant answers wrong, should we change the LLM?": a retrieval-augmented (RAG) or search feature underperforms and someone proposes a fix before the failing stage is known.
- Answers cite the wrong document, an outdated version, or miss a passage everyone knows exists.
- A change to the retrieval stack: new embedding model, chunking, reranker, hybrid search, re-index, or choosing k (how many passages the generator receives).
- A RAG eval reports one end-to-end answer score and nobody can say whether the corpus, the ranking or the generation fails.
- Do not use to evaluate an agent's tool calls, end state or forbidden actions: that is `agent-evals`.
- Do not use to decide which documents enter the corpus, who owns them or how often they are refreshed: that is `ai-data-requirements`.

## Inputs
Mandatory: the pipeline as it runs (corpus and its size, chunking, embedding model, reranker, the k the generator actually receives), a sample of real queries from logs or tickets with their class, and who can label relevance (domain experts, not the build team).
Ask if missing: the current end-to-end score and how it was graded, traffic share per class, the source register from `ai-data-requirements` (owners, versions, effective dates), price and latency per call, any judge in use and its validation.

## Method
1. **Locate before you change.** A RAG answer fails at one of four stages: the answer is not in the corpus (coverage), it is cut across chunks or stripped of its context (chunking), the right chunk is not in the top k the generator receives (ranking), or the generator misuses a passage it received (generation). Changing the LLM can only fix the last one. If graded failures already exist, attribute each to its first failing stage now: was the right passage in the context sent? That split takes a day and often settles the debate.
2. **Build the query set from real traffic, per class.** Sample logged queries stratified by class (lookup, multi-document, time-bound, exclusion or amount questions), sized per class with references/eval-statistics.md §3. Add **unanswerable queries**: questions that look in scope but whose answer is in no document (another product, a period not covered, a missing procedure). They are a class of their own, sized like one, and their expected answer is a plain "not found" with a route to a person. Keep a private holdout (`build-evals`).
3. **Label relevance on pooled candidates.** For each query, pool the top results of several retrievers (the current index, a keyword search such as BM25, a second embedding model or a hybrid), de-duplicate, and have domain experts mark which passages are relevant and which one is needed to answer. Labelling only the current system's top results grades it on its own homework: a relevant passage it never retrieves is never labelled, so recall looks high. Unjudged passages count as not relevant. Key each label to the document, its version and the answer-bearing span, not to a chunk id, so labels survive a re-chunking. Double-label 20% of queries; a kappa below 0.6 means the relevance definition needs fixing (references/eval-statistics.md §7). An LLM may draft candidate queries or pre-label, but never writes both the queries and their labels without expert review.
4. **Score retrieval first.** Recall@k at the k the generator actually receives, after reranking and truncation to the context budget, not at a k nobody uses. For single-passage questions this is a hit rate; for multi-document questions require every needed passage. Add MRR when only the first relevant result matters, nDCG when graded relevance and order matter (a list shown to users, or a context cut by budget). Report per class with the number of queries and a Wilson interval (references/eval-statistics.md §2); bootstrap when per-query recall is fractional (§6). Formulas and a worked example: references/retrieval-metrics.md.
5. **Score generation on fixed contexts.** Store the retrieved context of each query and run the generator on those same contexts, so a retrieval change cannot move the generation score. Run twice when you can: on the gold passages (what generation alone can do) and on the actual top k (real conditions); the gap is what retrieval costs. Three checks:
   - **Faithfulness at claim level**: split each answer into atomic claims; each must be supported by a passage in its context. Report the share of answers with at least one unsupported claim, per class; in a class with amounts, exclusions or deadlines one unsupported claim fails the case.
   - **Answer relevance**: the answer addresses the question asked, against the expert reference.
   - **Abstention**: on unanswerable queries, a plain "not found"; on answerable ones with the passage present, no needless refusal. Report both rates.
   Any LLM judge for these checks is validated against expert labels with `llm-judge-calibration` (TPR and TNR) before its numbers gate anything.
6. **Diagnose with the table.**

   | Signal | Points to | Next step, owner |
   | --- | --- | --- |
   | Low recall@k; experts find no document with the answer | Corpus coverage | Add or certify a source: `ai-data-requirements` owners |
   | Low recall@k; answer exists but is split across chunks, or a table lost its header | Chunking | Chunk along document structure, keep titles on chunks; re-run step 4 |
   | Low recall@k, high recall at 50 | Ranking | Reranker, hybrid keyword + dense, query rewriting, or k (step 7) |
   | Right passage retrieved, but a superseded version | Stale corpus | Effective dates and expiry: `ai-data-requirements` owners |
   | High recall@k, unsupported claims or wrong use of the passage | Generation | Prompt: answer only from passages, cite a passage per claim, abstain when none fits; then, measured on fixed contexts, `model-selection` |
   | Unanswerable queries get answered | Abstention | Abstention rule and retrieval-score floor: `system-prompt-and-guardrails` |

   Count failures per stage; the busiest stage is the next fix. A model change is discussed only when generation is the busiest stage on fixed contexts.
7. **Price k.** A larger k raises recall but adds input tokens (k × chunk size), latency, and distractors that can lower faithfulness. For each candidate k, report recall@k, faithfulness at that k, cost per query and p95 latency. Pick the smallest k that clears the recall threshold of the riskiest class; judge the choice on cost per correct answer = cost ÷ (volume × quality) (references/roi-model.md), not on recall alone.
8. **Treat every retrieval change as a release.** A new embedding model, chunking, reranker, k, index rebuild or a large corpus refresh: first judge the passages the new version surfaces that nobody has labelled (otherwise it is penalised for them), then re-run the retrieval set on old and new versions and compare them paired on the same queries (references/eval-statistics.md §5). Count d, the queries where exactly one version hits: a gap under 2√d ÷ n is a tie. Gate per class, keep the old index until the gate passes, and hand the result to `release-to-production`. A public leaderboard says nothing about your corpus and your users' wording.

## Output
A retrieval eval plan following `templates/retrieval-eval-plan.md`: pipeline as run, failure attribution, query set per class with unanswerable queries, labelling protocol (pooling, experts, agreement), retrieval scores per class at the k sent, generation scores on fixed contexts, diagnosis and owners, k pricing, release rule for retrieval changes. A section that cannot be filled says what is missing and who provides it. A short answer, such as a recommendation for a committee, still names each of these in a line: failures attributed to a stage, a query set per class with unanswerable queries, relevance labelled by experts on candidates pooled from several retrievers, recall at the k sent, generation on fixed contexts, and the paired comparison that will show whether a change worked.

## Rules and red lines
- Never judge a RAG feature on an end-to-end answer score alone: retrieval and generation are scored apart before any fix.
- Never a query set without unanswerable queries; their expected answer is a plain "not found".
- Never let the same LLM write the queries and their relevance labels without expert review; relevance is labelled by experts on pooled candidates.
- Never swap the embedding model, chunking, reranker or k without re-running the retrieval set and comparing paired, per class.
- Recall is reported at the k the generator receives, per class, with its interval.
- Never change the LLM to fix a failure the diagnosis puts in the corpus, chunking or ranking.

## Links
references/eval-statistics.md · references/roi-model.md · references/retrieval-metrics.md · build-evals · llm-judge-calibration · error-analysis · ai-data-requirements · model-selection · release-to-production · system-prompt-and-guardrails · production-evals-monitoring

## Sources
- manning-ir: recall at k, mean reciprocal rank, nDCG, pooled relevance judgements with unjudged passages counted as not relevant.
- es-ragas: faithfulness, answer relevance and context recall measured apart; faithfulness as the share of claims the context supports.
- husain-shankar-evals: locating the failing stage on real traces before choosing a metric or a fix.
- anthropic-evals: graders matched to each check, judges validated before use.
- miller-error-bars: paired comparison of two versions on the same queries.
- own-rag-practice: labels keyed to document spans, generation on frozen contexts, the diagnosis table and k pricing, from RAG assistants in production (method only).
