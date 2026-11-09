# Synthetic generation: skeletons and checks

Load this for steps 1 to 6 and 10 to 12 of SKILL.md. The wording below is a starting point; adapt it to the domain and keep each prompt versioned.

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

## Meaning-preserving variants (step 11)

| Variant family | What changes | What must not change |
| --- | --- | --- |
| Paraphrase | wording, sentence order | facts, amounts, dates, the request |
| Users' style | typos, missing accents, abbreviations, mixed French and English | the same facts |
| Format | field order in a form or table, line breaks, bullet vs prose | the fields themselves |
| Length | terse version, rambling version with the request buried | the request |

- About five variants per case; an expert checks a sample that the expected answer is unchanged, otherwise the variant is a new case, not a variant.
- Report per class: mean pass rate, worst-variant pass rate (the pass rate of the weakest variant family), flip share (cases whose verdict differs between variants). Two systems whose variant ranges overlap are tied (references/eval-statistics.md §13).
- Typos and accents seen in real traffic belong in the base set too (step 1); variants test robustness on top of that, they do not replace realistic inputs.

## Counterfactual pairs for decisions about people (step 12)

| Attribute | Direct form | Proxies to swap one at a time |
| --- | --- | --- |
| Sex or gender | stated gender | first name, title, gendered job or family words |
| Origin | stated nationality | first and last name, birthplace, language or spelling |
| Age | stated age | birth year, "retired", "student", years of employment |
| Place | — | postcode or town (can stand for origin or income) |
| Disability or health | stated condition | mention of a care allowance or adapted housing |

- Build from tuples: one base case, then one copy per attribute value, everything else byte-identical. Keep the base cases close to the decision boundary as well as clear-cut ones: flips happen at the margin.
- Run each pair, and run each unchanged base case twice. Flip rate = pairs whose decision differs ÷ pairs, per attribute. The rate between identical runs is the noise floor; report both.
- Interval: Wilson on the flip rate over pairs (references/eval-statistics.md §2); with 0 flips in n pairs, up to about 3/n remains possible. Size pairs per attribute for the margin the review needs (§3).
- Direction: among discordant pairs, count those favouring each value (b and c). A share b ÷ (b + c) far from 50% means the flips lean one way; McNemar's test on b and c says whether that is more than chance.
- Output to counsel: a table per attribute (pairs, flips, rate, interval, noise floor, direction) and the open questions for the art. 10(2)(f)-(g) bias examination of a high-risk system. Whether the result is acceptable is counsel's and the risk owner's call, not the eval's.
