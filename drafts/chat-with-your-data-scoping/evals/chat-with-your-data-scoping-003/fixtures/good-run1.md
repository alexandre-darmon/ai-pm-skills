I couldn't save the scope as a file because the Write tool is disabled in this session. The full text is below. Paste it into `templates/scoping.md` format if you want it kept.

# Chat-with-your-data scope: Finance analyst Q&A (8 certified metrics)

Status: draft. TODO items need facts I don't have, such as metric names, the data platform and the thresholds. I haven't invented anything about your data.

## Question classes (allowed | blocked | forbidden)
Sort the 62 questions into these classes first. The count per class is a TODO.

| Class | Status | Rule |
|---|---|---|
| Lookup on a certified metric | allowed | |
| Aggregate on a certified metric | allowed | Dimensions must exist in the semantic layer |
| Comparison on a certified metric | allowed | Both sides use the same definition and filters |
| Ambiguous (period, entity or metric unclear) | allowed after one clarifying question | No guessing |
| Metric outside the 8 certified, or disputed | **blocked** | Blocked until defined, then hand over to `semantic-layer-design` |
| Sensitive data (salaries, individual performance, personal data) | **forbidden** | Refuse in free-form questions |
| Forecasts, advice, causal "why" analysis | **forbidden** | Escalate to an analyst |

## Metric mapping (metric | definition | status)
| Metric | Definition | Status |
|---|---|---|
| TODO: metrics 1–8 | TODO: semantic-layer link | certified |

Standing filters per metric (test accounts, internal users, cancelled orders and so on) are a TODO. `semantic-layer-design` owns them. A question on any metric not in this table is blocked.

## Access (where rights are enforced | read-only | row and cost caps)
- Rights are enforced at query time in the data platform, never in the prompt. Two users asking the same question can get different rows or columns. Which platform and which row/column policies is a TODO.
- The connection is read-only.
- Row cap and query-cost cap per question: TODO.
- A dataset the platform can't enforce this on stays out of scope.

## Answer format (number, plain-language restatement, SQL, source, freshness)
Every answer contains:
1. The number.
2. A plain-language restatement of the metric, filters, period and grain. This is the check for users who can't read SQL.
3. The SQL.
4. The source.
5. Freshness.

There is no answer without its SQL.

## Golden set (≥ 50 pairs)
- Build it from the 62 real questions, as question → expected answer pairs signed off by an analyst.
- It needs at least 50 pairs across all classes. Blocked, forbidden and ambiguous questions count, and their expected answer is a refusal or a clarifying question. If fewer than 50 of the 62 are usable, collect more before go-live.
- Include pairs that fail if a standing filter is missing.
- Include one question asked by two users with different rights, with different expected results.
- Hand the set to `build-evals`.

## Accuracy target per class
Targets are measured per class, never as one global figure. Finance sets the thresholds based on the cost of an error. They are all TODO.

| Class | Target |
|---|---|
| Lookup | TODO |
| Aggregate | TODO |
| Comparison | TODO |
| Ambiguous (correct clarification) | TODO |
| Blocked / forbidden (correct refusal) | TODO (I suggest 100%) |

## Refusal and escalation
- An out-of-scope question gets a refusal that says why (metric not certified, sensitive data, outside the asker's rights). It never gets a guess.
- The user gets a handoff to a named finance analyst with the question attached. Owner and channel are a TODO.
- Refusals and escalations are logged and reviewed weekly. They show which metrics to certify next.

Autonomy level: L1

## Where this differs from the plan to check by hand
Asking a few questions by hand isn't enough for go-live. L1 requires an offline eval on the golden set that meets the per-class thresholds, plus a test with 5 users. The 62 questions are the raw material for that golden set. The hand-checking you proposed is still useful as the 5-user test, but it doesn't replace the golden set.

Certified metrics are necessary, but they don't cover everything. The 62 questions will probably include some on uncertified metrics, ambiguous questions or sensitive ones, and those need refusals. Right now I can't tell how many questions fall into each class.

Send me the 62 questions, the 8 metric names and the data platform, and I'll fill in the TODOs and draft the golden set.