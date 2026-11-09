# Error analysis guide

Deep material for `error-analysis`, loaded when the method needs detail. Own words; ideas from husain-shankar-evals, shankar-validators and glaser-strauss-grounded-theory.

## 1. Sampling streams

| Stream | What goes in | Typical size | Gives a rate? |
| --- | --- | --- | --- |
| random | simple random draw over the period, or in proportion to each question class's volume | 50–60 | yes, with its Wilson interval |
| targeted | thumbs-down, escalations, long or abandoned conversations, low-confidence answers, complaints, recent incidents | 30–40 | no |
| targeted: risky classes | extra traces from small classes with legal, financial or privacy effects | 10–20 | no |

If the random stream is drawn out of proportion to the classes (a small class oversampled), weight each class by its share of volume before computing a global share, or report shares per class only.

Planning: a short chat trace takes about 1 to 3 minutes to read and note, so 100 traces fit in half a day to a day of the expert's time. Long agent runs take longer: plan per run, not per message.

## 2. Writing notes (open coding)

| Weak note | Useful note |
| --- | --- |
| inaccurate | quoted the 2024 deductible table for a 2026 policy |
| bad tone | told a claimant the claim "will be refused" before the assessor's report |
| hallucination | cited clause 4.2, which does not exist in this wording |
| incomplete | listed the documents for a motor claim on a home claim |
| wrong | answered from the French leave policy for a Belgian employee |

Rules: one note per trace, on the first upstream failure; later problems can be listed after it but are not counted. "Pass" is a valid note and keeps the denominator honest.

Saturation log: trace number, note, new mode yes/no. The last "yes" and the count of traces since it go in the report.

## 3. From notes to modes (axial coding)

1. Sort the notes; put together the ones that describe the same failure.
2. Split a pile that mixes two causes (wrong country policy and outdated policy both look like "wrong rule").
3. Name each mode by what fails, not by a generic quality word.
4. Write the binary definition: "Fails when the answer states a figure that differs from the policy schedule in force for this contract." Add one pass and one fail example from the traces.
5. Re-file every note against the definitions; if a definition changed, re-check the notes filed earlier (criteria drift), and bump the taxonomy version.

An LLM can do steps 1–3 as a proposal on the written notes (group these notes, name each group, list notes that fit none). The expert keeps, merges or rewrites every proposed mode. It never reads the raw traces in place of the expert.

## 4. Specification or generalisation?

Ask, for each mode:
- Was the instruction written in the prompt or spec?
- Did the model receive the input it needed (user's country, contract, date)?
- Was the right document in the KB, current, and retrieved?
- Did the tool return the data?

Any "no" → specification failure: fix it, re-run the failing traces, keep them as regression cases. All "yes" → generalisation failure: it needs an evaluator.

Evaluator ladder, cheapest first:
| Check | Example |
| --- | --- |
| code | stated balance equals the HR system value; link to the source present; answer language equals question language; length under a cap; tool called |
| LLM judge, one per mode, binary | claim not supported by the retrieved clause; exclusion relevant to the facts not mentioned |
| none (accept) | low cost, no legal or irreversible effect, rationale and re-check date written |

## 5. Pricing, worked example

Claims assistant, 9,000 conversations a month, handlers validate every answer (L2). A wrong answer caught by the handler costs 10 minutes at 54 EUR an hour = 9 EUR. A wrong answer that reaches the claimant costs about 150 EUR (complaint handling and rework, source: claims quality lead).

Mode "wrong deductible": 6 of 60 random traces = 10% (Wilson 5% to 20%). Expected: 9,000 × 10% = 900 occurrences a month (420 to 1,810). Caught by handlers: 900 × 9 EUR = 8,100 EUR a month (about 3,800 to 16,300). Each one handlers miss adds 150 EUR: the miss rate is an open question for the quality lead, not a guess.

Mode seen only in targeted traces (0 of 60 random): it exists, and can still reach up to about 6% of traffic (Wilson upper bound; rule of three gives 5%). Price it on that bound only as an upper scenario, labelled so.

## 6. Agents: where runs break

For each failing run, record the last step that succeeded and the first that failed. Count the pairs in a matrix (rows: last success, columns: first failure). A column that fills up (for example "retrieve policy" failing after "identify contract") is the step to fix or evaluate first. Hand the matrix to `agent-evals`.

## 7. When to run again

| Trigger | Sample |
| --- | --- |
| model, prompt, KB or provider version change | 50–100 fresh traces, same streams |
| complaint spike or incident | targeted on the spike, plus a random draw for the rate |
| fixed cadence (monthly or quarterly) | 50–100 fresh production traces |

A new mode found in a re-run becomes regression cases in `build-evals`.
