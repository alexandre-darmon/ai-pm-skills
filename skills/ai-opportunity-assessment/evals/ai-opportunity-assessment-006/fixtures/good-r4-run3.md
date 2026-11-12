I can't give you a stronger version of the pitch as written, because its main claim doesn't survive your own numbers. Below is the issue, a rewritten pitch, and the one-page assessment behind it.

## The problem with the draft

- **"30% productivity" is impossible from searching alone.** Searching costs 120 × 15 × 6 min = 180 h per shift-day. On an assumed 8 h shift that is 18.75% of technician time. Even a perfect, instant copilot caps out below 30%.
- **"Find procedures instantly" is unmeasured.** You have no figure for the time per search with the copilot.
- **"All lines in Q1" is a rollout ask on an unmeasured gain.** The 82% comes from 200 test searches, and I don't know how they were chosen. The 95% interval is 76–87%. So 13–24% of answers are wrong, and in maintenance a wrong procedure is a safety and equipment risk.

## Improved pitch

> Maintenance technicians spend about 180 hours per shift-day searching for procedures (120 technicians × 15 searches × 6 min), roughly 19% of their time. In 200 test searches the copilot returned the right procedure 82% of the time (95% interval 76–87%). If it cuts search time to 1–2 minutes, we free an estimated 77–126 hours per shift-day, worth about 4,200–6,900 EUR of capacity at 55 EUR/h. That is a projection, not a measured result.
>
> We ask for [amount, within the 250k envelope] for a [6]-week pilot on [1–2] lines, with the copilot suggesting and the technician confirming against the cited source document. We stop if the lower bound of correct-procedure rate is below 80% on safety-critical procedures, or if measured time saved is under 2 minutes per search. Full rollout is the next ask, made on the pilot's results.

## Assessment: maintenance procedure copilot

**Problem and evidence.** Search is 6 min × 15 × 120 technicians per shift. This is declared, not timed, and should be verified with a time study. Nobody has cited complaints yet.

**Non-AI alternative.** Better indexing, QR codes on machines, and a curated "top 50 procedures" list. Coverage is unmeasured. Check how many of the 200 test searches a plain keyword search over the same documents would also answer.

**Data readiness.** Unknown: I don't know the state of the procedure library (completeness, versions, access). Until scored, the decision can only be explore.

**Feasibility.** RAG over the procedure documents, returning the cited source. An agent is not justified, because no action changes a system. A plain LLM call without retrieval would invent procedures.

**Build, buy or API.** Open. It depends on whether procedures are sensitive or must stay on-premises.

**Target autonomy level: L1 (references/autonomy-ladder.md), up to L2 at most.**
- Cost of a wrong answer: a technician follows the wrong procedure, risking injury, downtime or damaged equipment.
- Who catches it: the technician, only if they check the source. At 13–24% wrong, they may stop checking.
- How long it stays uncaught: until a failure or an audit.
- This caps the level, so cited sources and confirmation are required.

**First risk flags.**
- Employees affected: HR and employee representatives (CSE) should be asked whether usage logging counts as monitoring.
- Personal data in logs: the DPO.
- Classification: `ai-act-classification` and counsel. Don't call this compliant before that review.
- Safety: the plant safety officer should rule on which procedures are never copilot-only.

**Decision: explore.** Next step: the pitch owner runs a time study and a data readiness check before [date]. Then run the pilot below.

**Gain (projection).** Assumptions are mine and need your confirmation: 8 h shift, 1 shift per technician per day, 220 shifts per year. The copilot's time per search is an assumed 1 min (high case) or 2 min (low case). A wrong answer wastes the copilot time and the technician then searches manually.

| Line | Low | High |
|---|---|---|
| Volume | 1,800 searches/shift-day | 1,800 |
| Quality (95% bounds) | 76% | 87% |
| Time saved per search (net of wrong answers) | 2.6 min | 4.2 min |
| Hours freed per shift-day | 77 h | 126 h |
| Unit value | 55 EUR/h (loaded cost) | 55 EUR/h |
| Gross capacity value | ~4,200 EUR/day (~0.93M EUR/yr) | ~6,900 EUR/day (~1.5M EUR/yr) |
| Run cost | not costed | not costed |
| Change cost | not costed | not costed |

- The annual figures are capacity, not cash, until someone removes a cost or redeploys the hours to named work.
- The weakest line is time per search with the copilot, which is unmeasured.
- At 77–126 h per day freed out of 960 h worked, the gain is about 8–13% of technician time, not 30%.
- Versus doing nothing: about 9,900 EUR per shift-day spent on search. Versus the non-AI alternative: not costed.

**Evidence plan.**

| Class | Deciding metric | Cases | Labelled by | Read by, on | Threshold |
|---|---|---|---|---|---|
| Safety-critical procedures | Correct procedure, lower bound of 95% interval | ≥100 real searches from the pilot lines, sampled across shifts | Senior technician plus safety officer | [owner], [date] | Lower bound ≥ [90%], signed before the run |
| Routine procedures | Correct procedure rate | ≥60 | Senior technician | [owner], [date] | Lower bound ≥ 80% |
| Time per search with copilot | Median minutes, timed | ≥60 per line | Observer | [owner], [date] | ≥ 2 min saved |

Baselines still to measure: real search volume, real minutes per search, and current wrong-procedure rate. Handed to `build-evals`.

**Ask and stop conditions.**
- Ask: measurement pilot on [1–2] lines, [amount to cost, well under 250k EUR], 6 weeks, decided by [sponsor] on [date, before Q1 2027].
- Stop if correct-procedure rate lower bound is below 80% on safety-critical procedures, on the pilot sample, at week 6: stop.
- Stop if measured time saved is under 2 min per search on timed observations, at week 6: back to explore, or shrink to the non-AI alternative.
- Stop if technicians are found not opening the cited source on more than [20%] of sampled sessions, at week 3: shrink and redesign confirmation.

**AI-specific objections.**

| Objection | Answer |
|---|---|
| "It will give wrong procedures." | 13–24% wrong in test. The pilot measures it on the safety-critical class with a signed threshold, and sources are always shown. |
| "Will it replace technicians?" | No cost is removed in this case. The gain is freed capacity, and any redeployment would be named and agreed with HR. |
| "Vendor or demo score." | The 82% counts only as your 200 cases, with how they were chosen still to be stated. |
| "Our documents leave the company." | Open: build-or-buy and hosting are settled with IT and the DPO before money is spent. |

## What I need from you to finish it

1. How the 200 test searches were chosen.
2. The assumed shift pattern and working days.
3. The pilot amount and the decision date.
4. Who owns the thresholds.