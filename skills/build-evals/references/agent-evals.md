# Agent and retrieval evals

Load this when the feature calls tools, acts on a system, or answers from retrieved documents. It adds to the method in SKILL.md: classes, thresholds, holdout, judge calibration and baseline still apply.

## Why the final message is not enough

A run can fail three tool calls and then write a calm, plausible reply. A judge reading that reply passes it. Grade what the run did, and what it left behind.

## Agent run: four checks per case

| Check | Question | Usual grader |
| --- | --- | --- |
| Tool correctness | Right tool, right arguments, right order, no loop or repeated send? | exact on the trace |
| End state | Is the record really there, in the system, with the right values? | exact on the system or a test double |
| Forbidden events | Did anything happen that must never happen (approval skipped, write before read, second send)? List them per case. One occurrence fails the run, whatever the final message says. | exact on the trace |
| False success | When the run stops one step short, does the agent say so? | seeded case, then exact or judge |

Add false-success cases on purpose: make a tool fail or time out at the last step. Add requests that span two tools, since that is where hand-offs break.

Each case's fixture holds the starting state: permissions, approval records, seeded data. A transcript alone cannot replay a decision.

When a level change is the thing being gated (references/autonomy-ladder.md), the forbidden events are the ones the higher level would no longer have a human to catch.

## Locating the break

- In a long trace, label the first failure upstream. Later errors are often its consequences.
- Count failed runs in a small matrix: last step that succeeded against the step that failed. The busiest cell is the next fix.

## Retrieval (RAG): score it apart from generation

If the right passage never arrives, the answer cannot be judged fairly, so measure in this order:

1. **Retrieval**, on labelled queries (`agent-knowledge-base` hands them over): recall at k, and mean reciprocal rank when order matters. Report per class. Include queries whose answer is not in the corpus.
2. **Generation**, given the retrieved context: faithfulness to the passages, relevance to the question, and a plain "not found" when nothing fits.

A low answer score with high recall points to generation. With low recall it points to the corpus, chunking or ranking. A single end-to-end score cannot tell these apart.

## Owners

The tool write protocol is in `agent-design-and-tooling`. Attacks and enforcement are in `system-prompt-and-guardrails`, with its redteam set. Source access rules are in `agent-knowledge-base`.
