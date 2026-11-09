# Retrieval eval plan — <feature name>

## Pipeline as it runs
| Item | Value |
| --- | --- |
| Corpus (documents, versions, owner register) | |
| Chunking (method, size, overlap) | |
| Embedding model and version | |
| Reranker / hybrid search | |
| k sent to the generator | |
| Generator model and prompt version | |
| Current end-to-end score (cases, how graded, interval) | |

## Failure attribution
<Failed cases read, and the first failing stage of each.>
| Stage | Failed cases | Share |
| --- | --- | --- |
| Coverage (answer in no document) | | |
| Stale version | | |
| Chunking | | |
| Ranking (not in top k sent) | | |
| Generation: unsupported claim | | |
| Generation: irrelevant answer or wrong abstention | | |

## Query set
| Class | Real queries | Unanswerable queries | Holdout | Size reason |
| --- | --- | --- | --- | --- |
<Source of queries (logs, tickets, period). Expected answer for unanswerable queries.>

## Relevance labels
<Retrievers pooled, depth, experts, label unit, agreement, LLM assistance and its review.>

## Retrieval scores
| Class | Queries | Metric at k sent | Score | 95% interval | Threshold |
| --- | --- | --- | --- | --- | --- |

## Generation scores
<Contexts used (stored per query), judge and its validation.>
| Class | Answers with an unsupported claim | Answer relevance | Correct "not found" | Needless refusals | Gold vs actual context gap |
| --- | --- | --- | --- | --- | --- |

## Diagnosis and owners
| Stage | Evidence | Fix | Owner | Re-measure on |
| --- | --- | --- | --- | --- |

## Choice of k
| k | Recall at k (risky class) | Faithfulness | Cost per query | p95 latency | Cost per correct answer |
| --- | --- | --- | --- | --- | --- |

## Retrieval changes are releases
<Change, old vs new on the same queries, unseen passages judged, d and tie bound, per-class gate, rollback.>

## Open questions
| Question | Owner |
| --- | --- |
