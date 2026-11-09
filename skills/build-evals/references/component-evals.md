# Component evals

Load this when the feature is a pipeline of several steps and is neither a retrieval assistant (`retrieval-evaluation`) nor an agent that acts (`agent-evals`): extraction then validation, a classifier that routes then a model that answers, text-to-SQL, a draft then a guardrail. It adds to the method in SKILL.md: classes, thresholds, holdout, judge validation and baseline still apply.

## Two evals, two jobs

- **End to end** decides the release: the user only sees the final answer. One set, thresholds per class, the gate in SKILL.md.
- **Per component** locates the failure and decides which part to change. A low end-to-end score says something is wrong; it never says what.

Run both. A component that improves while the end-to-end score does not move is not an improvement worth shipping.

## How to cut the pipeline

1. List the steps as they run: input → step 1 → step 2 → … → answer. For each, write what it receives, what it returns and what "correct" means for that output alone.
2. Give each step its own small labelled set, taken from real traffic (or from the end-to-end set, with the intermediate output labelled). Thirty to fifty cases per step is enough to locate a failure; a step that gates a costly class needs the size its threshold asks for (references/eval-statistics.md §3).
3. Pick the cheapest check per step: exact match on a field or a label, a classifier's confusion matrix, an executed query's result, a calibrated judge only when code cannot decide.
4. Freeze the upstream output when you score a downstream step: score generation on stored inputs, not on whatever the live upstream step returns that day. Otherwise two changes move at once.
5. For each failed end-to-end case, label the first step that went wrong (`error-analysis`). The counts per step say where to work next.
6. Change one component at a time and compare old and new on the same cases, paired: a gap under 2√d / n is a tie (references/eval-statistics.md §5). Then re-run end to end before release (`release-to-production`).

## Common components and their check

| Component | What "correct" means | Usual check |
| --- | --- | --- |
| Router or classifier | The request goes to the right path | Confusion matrix per class, against expert labels |
| Extraction | Each field holds the right value | Exact match per field; score the unit the business uses (a document fully right, not a field) |
| Text-to-SQL | The executed query returns the right number under the certified metric definition | Result of the executed query against the expected result, never the SQL text |
| Generation | Faithful, complete, in scope | Checklist regexes, then a validated judge per failure mode |
| Guardrail | Blocks what it must, passes what it must | True and false positive rates on a labelled attack and benign set |
| A confidence score shown to users | When it says 90%, it is right about 9 times in 10 | Reliability table: bins of stated confidence against observed accuracy |

## Text-to-SQL, in particular

A query that runs and returns a number is not a correct answer:

- Grade the executed result against the expected result, never the SQL string: two different queries can both be right.
- Check the metric definition: the right number for "active customers" is the certified one, with its standing filters (test accounts, internal users, cancelled orders). A pair that fails when a filter is missing belongs in the set.
- Include questions the data cannot answer, and questions on sensitive or undefined metrics: the expected behaviour is a refusal or a hand-off to an analyst.
- Include one question asked by two users with different access rights: the rows returned must differ, enforced by the data platform, not the prompt.
- Report accuracy per question class (lookup, aggregate, comparison, ambiguous), never one global figure.

## A confidence score shown to users

`ai-interaction-patterns` decides whether a score is shown; this is how it is checked. Group answers by stated confidence (for example 50–60%, …, 90–100%), and compare each bin with the share actually correct. A score is shown only if the bins line up, with enough answers per bin to read them (references/eval-statistics.md §2). Otherwise show sources, not a number.
