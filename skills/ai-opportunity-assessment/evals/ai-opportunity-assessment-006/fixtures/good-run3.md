**Pitch rewrite (the working version is below the assessment)**

> Technicians at our plant spend about 90 minutes of each shift (15 searches × 6 min) looking for maintenance procedures. In a 200-search test, our AI copilot returned the right procedure 82% of the time (95% interval 76% to 87%). If it does that in daily use, it frees about 15% of technician time. That is roughly 8,100 EUR of capacity per day, but the figure is a projection. We ask for a 6-week pilot on two lines to measure the real time saved and the error rate on safety-critical procedures. The rollout request comes after the pilot results, against stop conditions we sign now.

## What changed in your draft

- **"30% productivity" cannot be reached.** Search is 90 min of an 8 h shift, which is 18.75%. Even instant search would cap the gain below 30%. At 82% quality and instant find, the figure is about 15%, so I rewrote it from the lines.
- **"Instantly" is replaced by the measured rate.** The 82% means about 1 search in 5 fails, and the pitch should say so.
- **The ask is now a pilot.** Nothing has been measured in the plant yet, so a 250k EUR all-lines rollout is premature. The rollout becomes the next ask, made on pilot evidence.

---

# AI opportunity assessment: maintenance procedure copilot

## Problem and evidence
Technicians lose time finding the right maintenance procedure. The declared figures are 120 technicians, about 15 searches per shift and 6 min per search. The evidence is declared, not measured. Who complained, and how often, is not stated.

## Non-AI alternative
A better index or keyword search over the existing procedures, or QR codes on machines linking to their procedures.
Rule coverage: unmeasured. Nothing yet rests on a test. The first step is to replay the 200 test searches with plain keyword search. Cost: not costed.

## Data readiness (0–5 per axis, mean x/5)
Unknown. The procedure corpus has not been described (format, currency, access rights). Labels partly exist from the 200 tests. The decision can therefore only be explore.

## Feasibility by approach
- **Rule or keyword search:** untested, so it is the baseline to beat.
- **RAG over the procedures:** fits, because the answer sits in documents.
- **Agent:** not needed. The copilot takes no actions on any system.
- **Pick:** RAG, but only if the keyword baseline falls short.

## Build, buy or API
Not decided. Settle it after the readiness check, with data sensitivity (plant documents) and run cost as the criteria. Run cost: not costed.

## Target autonomy level
**Cost of a wrong answer:** the technician follows the wrong procedure. That can mean equipment damage or a safety incident. The technician is the only catch, and may not notice until the work is done.
**Level:** L1 at pilot start, L2 as the target (the technician opens the cited procedure and confirms). L3 and above are out, because a wrong output can reach the machine before anyone sees it.

## First risk flags
- **Employees affected and monitoring:** timing searches and logging usage involve employee data. Owner: DPO and HR, who also settle whether the works council must be consulted.
- **AI Act classification:** owner is `ai-act-classification` and counsel. The question is whether safety-relevant maintenance guidance changes the classification.
- **Confidential plant documents sent to an external model:** owner is the DPO and security.
- I am not calling this compliant. These items need their owners' answers before spending.

## Decision
**Decision: explore.** Next step: measure the baseline and the keyword alternative on real searches. Owner: the maintenance manager. Date: to be set by you.

## Gain (five lines)
**Status: projection.**
- **Volume:** 120 × 15 = 1,800 searches per day, assuming one shift per technician per day. Declared, not measured.
- **Quality:** 82% (95% interval 76% to 87% on 200 tests, chosen how: unknown).
- **Unit value:** 6 min × 55 EUR/h = 5.50 EUR per correct find. It assumes the copilot answer takes about 0 min. That is optimistic, because verification takes time.
- **Run cost:** not costed.
- **Change cost:** up to 250k EUR if the ask stands, spread over a period to be stated.

**Result per day (gross capacity):**
- Central: 1,800 × 0.82 × 5.50 = 8,118 EUR, or 148 h, or 15.4% of 960 technician-hours.
- Low (quality 76%): 7,524 EUR, about 14%.
- High (quality 87%): 8,613 EUR, about 16%.
- The weakest lines are really the declared volume and the 6 min, not the quality. Halve either one and the gain halves.

This is capacity, not cash, until someone removes a cost or assigns the freed hours to named work.

**Versus:**
- Doing nothing: about 9,900 EUR of capacity per day goes to searching, but no cash changes.
- Non-AI alternative: not costed.

## Evidence plan
| Class | Deciding metric | Cases (real, sampled how) | Labelled by | Read by, on | Threshold, signed by, on |
|---|---|---|---|---|---|
| Safety-critical procedures | Share of searches where the right procedure is returned | 75 real pilot searches, all tagged safety-critical | Two senior technicians (kappa ≥ 0.6) | Maintenance manager, week 6 | Lower bound ≥ 90% (proposed), sponsor, before the run |
| Routine procedures | Same metric | 62 real pilot searches, random | Same | Same | Point estimate in a bracket of 80–85%, to settle before funding |

**Baseline lines still to measure:**
- Searches per technician-shift (declared today, so measure it from logs or a time study).
- Minutes per search, from a timed sample.
- Current wrong-procedure rate with manual search.
- Copilot time per search, including verification.

Handed to `build-evals`. If the pilot traffic cannot fill the cases by the date, move the date, not the bar.

## Ask and stop conditions
**Ask:** pilot on 2 lines, <amount to cost>, 6 weeks, decided by <sponsor> on <date>. The 250k EUR is the rollout figure and is not the ask yet. For example, baseline time study in the weeks from 16 Nov 2026, pilot from January 2027, readout around mid-February.

- **Stop if** the safety-critical lower bound is below 90% on 75 real searches at week 6: stop.
- **Stop if** measured time saved is below 3 min per search on a timed sample of 60 searches at week 6: shrink to the lines where it holds.
- **Stop if** the baseline shows fewer than 8 searches per technician-shift, or the keyword alternative gets within 5 points of the copilot's quality on the replayed 200 searches, at the end of the baseline phase: back to explore.

The thresholds are my proposals. You sign them before any spending.

## AI-specific objections
| Objection | Answer |
|---|---|
| "It gives wrong answers." | About 18% fail (interval 13% to 24%). The pilot measures the safety-critical class separately, shows the cited source, and keeps the technician in the loop at L1–L2. |
| "The 82% is a demo score." | It comes from 200 searches. How they were chosen is unknown, so the pilot re-measures on real searches. |
| "It will replace technicians." | The gain is capacity, and no cost removal is claimed. Say which work the freed hours go to. |
| "Our documents leave the company." | Open until build, buy or API is settled. Owner: DPO and security. |

---

## What I need from you

1. How the 200 test searches were chosen: real queries or ones the team wrote.
2. Whether each technician works one shift per day.
3. The pilot cost, the decision-maker and the date.
4. What the freed hours would be used for.