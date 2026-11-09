# Retrieval metrics, labelling and comparison

Load this for the formulas behind steps 3, 4, 5 and 8 of SKILL.md. Intervals and paired tests come from references/eval-statistics.md.

## Labelling protocol

1. **Pool.** For each query, take the top 10 to 20 results of at least three retrievers: the current index, a keyword search (BM25), and a second embedding model or a hybrid. Merge and de-duplicate by document span.
2. **Judge.** A domain expert marks each pooled passage: `required` (the answer cannot be given without it), `relevant` (helps, not needed), `not relevant`. For an unanswerable query the expert confirms that no pooled passage, and no document found by hand, holds the answer.
3. **Key labels to spans.** Store `doc_id`, `version`, and the answer-bearing span (section, page, character range). A retrieved chunk counts as a hit when it contains the required span. Chunk ids change with every re-chunking; spans do not.
4. **Unjudged = not relevant**, which is why a new retriever's unseen passages are judged before it is compared (step 8).
5. **Agreement.** Two experts on 20% of the queries, Cohen's kappa on `required` vs the rest. Below about 0.6, rewrite the relevance definition with examples and re-label.
6. **LLM help, bounded.** An LLM may propose paraphrased queries or pre-label pooled passages. An expert reviews every label it proposes; the model that drafted the queries never labels them alone.

## Retrieval metrics (per query, then averaged per class)

| Metric | Per query | Use when |
| --- | --- | --- |
| Hit@k | 1 if a required span is in the top k, else 0 | single-passage questions; binary, so a Wilson interval applies |
| Recall@k | required spans in top k ÷ required spans | multi-document questions; fractional, so bootstrap over queries |
| MRR | 1 ÷ rank of the first required span (0 if beyond the cutoff) | one answer is enough and rank 1 matters |
| nDCG@k | DCG@k ÷ ideal DCG@k, DCG = Σ (2^rel − 1) ÷ log2(rank + 1) | graded relevance, order matters |
| Context precision@k | relevant passages in top k ÷ k | how much noise the generator receives |

k is the number of passages the generator actually receives after reranking and truncation. Recall at 50 is a diagnostic (is the passage findable at all?), never the headline.

Worked nDCG@5: relevance by rank = 0, 2, 1, 0, 0 (2 = required, 1 = relevant). DCG = 3 ÷ log2 3 + 1 ÷ log2 4 = 1.89 + 0.50 = 2.39. Ideal order 2, 1: 3 + 0.63 = 3.63. nDCG@5 = 0.66.

Worked interval: a class of 62 queries with 56 hits at k = 5 gives hit@5 = 90%, 95% interval 81% to 96%. With 50 hits: 81%, interval 69% to 89%.

## Generation metrics (on fixed contexts)

- **Claim-level faithfulness.** Split the answer into atomic claims (one fact, amount, condition or date each). A claim is supported when a passage of the context states it or entails it. Report: share of claims supported, and share of answers with at least one unsupported claim (the number users feel). A claim true in the world but absent from the context is still unsupported: the user cannot check it.
- **Answer relevance.** Does the answer address the question asked, compared with the expert reference? Binary pass or fail per answer.
- **Abstention.** On unanswerable queries: share answered with a plain "not found" and a route. On answerable queries with the required passage in context: share of needless refusals. Both, per class.
- **Gold vs actual context.** Same generator, same questions, once on the gold passages, once on the retrieved top k. The difference in answer pass rate is the cost of retrieval.

Each check that an LLM judge scores is a binary criterion validated against expert labels (TPR and TNR, references/eval-statistics.md §7) before it gates anything.

## Failure attribution

For each failed end-to-end case, record the first failing stage, upstream first:

| Order | Question | If no |
| --- | --- | --- |
| 1 | Is the answer in some indexed document, in the version in force? | coverage or stale corpus |
| 2 | Is it within one chunk that keeps its context (title, product, table header)? | chunking |
| 3 | Is that chunk in the top k sent to the generator? | ranking |
| 4 | Is every claim of the answer supported by the context? | generation (faithfulness) |
| 5 | Does the answer address the question, or abstain when it should? | generation (relevance, abstention) |

## Paired comparison of two retrieval versions

Same queries, same labels (after judging the new version's unseen passages). Per query, hit or miss for each version.

Example: 300 queries. Old version: 246 hits (82%). New version: 255 hits (85%). 18 queries hit only with the new one, 9 only with the old one, so d = 27. Tie bound: 2√27 ÷ 300 = 3.5 points. The 3-point gain is inside it: a tie. Read the 9 queries the new version lost before switching, and check per class: a tie overall can hide a loss in a risky class.

## Pricing k

Added input tokens per query = (new k − old k) × tokens per chunk. Example: from k = 5 to k = 20 with 512-token chunks adds 7,680 tokens per query. At a price of P per million input tokens and V queries a month, the added monthly cost is 7,680 × V × P ÷ 1,000,000. Put it next to the recall gained and the faithfulness measured at each k, then compare cost per correct answer.
