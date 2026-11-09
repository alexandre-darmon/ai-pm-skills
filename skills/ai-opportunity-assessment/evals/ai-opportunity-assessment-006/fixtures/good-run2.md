I used the AI opportunity assessment method. Your facts support a pilot, not a plant-wide rollout, and the 30% doesn't trace to them.

## What's wrong with the draft

- **The 30% can't come from your numbers.** Your facts put search time at 15 × 6 = 90 min per shift, about 19% of an 8 h shift. Even instant search couldn't reach 30%. With the 82% hit rate and an assumed 1 min search with the copilot, the gain is about 13% of shift time, with a range of 12% to 14%.
- **"Instantly" is unproven.** You have no measured time with the copilot.
- **82% is a point estimate.** On 200 cases, the 95% interval is 76% to 87%. I also don't know how the 200 searches were chosen.
- **A wrong procedure is a safety issue.** About 1 search in 5 or 6 misses, and the pitch doesn't say who catches it.
- **The ask is a rollout.** Nobody has measured the gain yet, so the first ask should be a measurement pilot.

## Suggested pitch

> Maintenance technicians spend about 90 minutes per shift searching for procedures (120 technicians × 15 searches × 6 min). In a test of 200 searches, our copilot found the right procedure 82% of the time (95% interval 76–87%). If searches drop to about 1 minute, that frees roughly 13% of shift time. That is a projection, worth about 1.4–1.6 M EUR a year of capacity before run and change costs. It is capacity, not cash.
>
> Wrong procedures are the main risk, so the copilot only suggests, with a cited source. The technician opens and confirms the document. We ask for **<amount>** to run a 6-week pilot on 1–2 lines. It will measure real search time and accuracy on safety-critical procedures. We scale to all lines only if the stop conditions below are met.

## Assessment

**Problem and evidence:** Technicians lose about 90 min per shift searching for procedures. The 15 searches per shift and 6 min per search come from your facts. I don't know if they were measured or estimated, so check this with the technicians.

**Non-AI alternative:** Better indexing of the procedure library, plus a QR code on each machine linking to its procedures. Rule coverage: unmeasured. Test it on the same 200 searches.

**Data readiness:** Unknown. I have no information on the procedure documents' quality, format, version control, languages or access rights.

**Feasibility:**
- **Rule or better search:** unmeasured, see above.
- **RAG over your procedures:** the answer sits in documents, so this is the simplest approach that plausibly fits.
- **Agent:** not needed, because no action changes a system.

**Build, buy or API:** Provisionally an API with RAG over your own documents. Data sovereignty and where the documents are stored are still open.

**Target autonomy level:** L1, assisted.
- **Cost of a wrong answer:** the technician may follow a wrong maintenance procedure on a machine. That is a safety and equipment risk.
- **Who catches it:** the technician, only if they check the cited source.
- **How long it stays uncaught:** possibly until a fault occurs.
- Because a wrong output can reach the machine before anyone sees it, L3 and above are out.

**First risk flags:**
- **Employees affected** (productivity tracking): HR and employee representatives. Does the pilot change working conditions?
- **Personal data** (search logs tied to named technicians): the DPO. Can logs be anonymised?
- **Possible AI Act high-risk domain** (safety of machinery): `ai-act-classification` and counsel.

**Decision:** Explore. Data readiness is unknown, so a go isn't possible yet. Next step: the sponsor names an owner to audit the procedure corpus (score the five axes, aim for at least 2/5) and set pilot dates.

**Gain (projection, not a result):**
- **Assumptions I made:**
  - 1 shift per technician per day.
  - 220 working days a year.
  - 1 min per search with the copilot.
  - An 8 h shift.
- **Volume:** 1,800 searches per day.
- **Quality:** 82% found the right procedure (low 76%, high 87%).
- **Unit value:** (6 − 1) min × 55 EUR/h ≈ 4.58 EUR per correct search.
- **Run cost:** not costed.
- **Change cost:** not costed.
- **Gross figures:** about 6.8 k EUR per day (low 6.3 k, high 7.2 k). That is about 1.49 M EUR a year (low 1.38 M, high 1.58 M).
- **Weakest line:** the bounds above use only the quality interval. The copilot's search time is the weaker unknown. At 3 min instead of 1, the gain falls about 40%.
- **Not counted:** the cost of wrong answers.

**Versus:** Doing nothing costs about 2.2 M EUR a year of search time (1,800 × 6 min × 55 EUR/h × 220 days). The non-AI alternative is not costed.

**Evidence plan** (handed to `build-evals`):

| Class | Deciding metric | Cases | Labelled by | Read by, on | Threshold, signed by, on |
|---|---|---|---|---|---|
| Safety-critical procedures | Right procedure found | At least 100 real pilot searches, sampled across lines | Senior technicians | Pilot lead, at pilot end | Lower bound of 95% interval ≥ **<bracket>**, signed before the run |
| Other procedures | Right procedure found | At least 60 real searches (about ±10 points near 80%) | Technicians | Pilot lead, at pilot end | Point estimate ≥ **<bracket>** |

Baseline lines still to measure:
- Searches per shift.
- Time per search today.
- Time per search with the copilot.
- The current rate of wrong procedures used.

**Ask and stop conditions:**
- **Ask:** pilot, **<amount>**, 6 weeks on 1–2 lines, decided by **<sponsor>** on **<date>**.
- **Stop if** the lower bound of accuracy on safety-critical searches is below the signed threshold, read on the pilot sample at week 6: stop.
- **Stop if** time per search with the copilot is above **<bracket>** min, read on the pilot sample at week 6: back to explore.
- **Stop if** the corpus audit scores below 2/5, read before the pilot starts: stop.

**AI-specific objections:**

| Objection | Answer |
|---|---|
| "It gives wrong procedures." | The target is L1 with a cited source, and the safety-critical class is tested on at least 100 cases. |
| "The 82% is from a test, not reality." | It comes from 200 test searches (76–87%). The pilot re-measures it on real searches. |
| "It will replace technicians." | The gain is capacity, not cash. Say what the freed hours will be used for. |
| "Our documents leave the company." | Open, pending the build, buy or API decision and the DPO. |

## What I need from you

- The pilot amount, the decision-maker and the date.
- Whether the 15 searches and 6 min are measured or estimated.
- How the 200 test searches were chosen.
- Where the procedure documents are, and in what state.