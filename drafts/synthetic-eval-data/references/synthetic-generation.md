# Synthetic generation: skeletons and checks

Load this for steps 1 to 6 and 10 of SKILL.md. The wording below is a starting point; adapt it to the domain and keep each prompt versioned.

## Dimension examples (financial services)

| Dimension | Example values | Grounded in |
| --- | --- | --- |
| Persona | first-time borrower, existing customer, broker, heir | real examples: who asked |
| Intent (class) | early repayment, rate change, payment holiday, loan insurance, documents | class list from `build-evals` |
| Difficulty | single fact, needs two documents, needs the customer's own contract | failure hypothesis: multi-document questions fail |
| Channel | mobile chat, web chat, email forwarded by an adviser | traffic statistics |
| Language and style | formal French, French with typos and no accents, French and English mixed, terse English | real examples |
| Edge condition | missing loan number, two requests in one, outdated product name, angry tone | `error-analysis` notes |

Every row says where its values come from. A row grounded in nothing is "assumed", and its cases are a small, labelled share.

## Tuple plan

- Count: enough tuples per class to reach the class size from references/eval-statistics.md §3, plus about 30% for rejections.
- Coverage: every value of every dimension at least 5 times; every pair of values from the two riskiest dimensions at least once.
- Weights: risky classes and edge conditions above their traffic share; state the weight next to the traffic share.
- Exclusions: written rules ("a broker never asks about their own payment holiday").
- Review: an expert reads the tuple table and strikes or adds rows before step 3.

## Step 3 prompt skeleton (one tuple per call)

> You write one message that a real customer of a French mortgage lender would send to its chat assistant.
> Customer: {persona}. Wants: {intent}. Difficulty: {difficulty}. Channel: {channel}. Style: {language and style}. Condition: {edge condition}.
> Here are three real messages, for style only, not content: {anchors}.
> Write only the message, as the customer would type it. Do not explain. Do not invent names, account numbers or addresses.

Rotate anchors across calls so no single real message shapes the set. Keep the temperature high enough for variety, and de-duplicate near-identical outputs.

## Review sheet (one row per input)

| Case id | Tuple | Input | Realistic? (yes/no) | Reason if no | Expected answer | Source document and section | Reviewer | Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Rejection rate per dimension value = rejected ÷ reviewed for that value. Above about 20%: new anchors, regenerate that value, review again.

## Realism checks against real traffic

| Measure | Real traffic | Synthetic set | Tolerance (written before) |
| --- | --- | --- | --- |
| Median length (words) | | | e.g. within 30% |
| 90th-percentile length | | | |
| Language share | | | e.g. within 10 points per language |
| Class mix (after weights) | | | stated weights |
| Share with typos or missing accents | | | |
| Share of incomplete or two-request messages | | | |

With fewer than about 50 real messages, the real column is itself uncertain: say so and widen the tolerance rather than skip the check.

## Flag schema (per case)

`case_id`, `origin` (real | synthetic), `generator_model`, `generator_version`, `prompt_version`, `tuple`, `created`, `reviewed_by`, `expected_answer_source` (expert | document), `replaced_by` (real case id, once replaced).

## RAG question generation

- From documents: one question per section that users would ask, in their vocabulary. Reject questions that copy three or more consecutive content words from the section: they make retrieval look easier than it is.
- Unanswerable: as many as needed to size that class, built from neighbouring products, periods or procedures the corpus does not cover. An expert confirms no document answers them.
- Labels: the section (document, version, span) for answerable questions; "not found" for the others. Hand both to `retrieval-evaluation`.
