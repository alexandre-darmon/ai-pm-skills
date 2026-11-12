# Multi-turn eval plan: <assistant>, <version>

Date: <date> · Owner: <name> · Decision fed: <release / ladder move Lx → Ly / model change> · Signed before the run by: <name>

## Conversation outcomes
| Outcome | Applies to which classes | Binary criterion | Grader (code / calibrated judge) |
| --- | --- | --- | --- |

## Per-turn checks kept
<Only turns with their own correct answer (rate, amount, policy fact); each is also a one-shot case.>

## Scripted cases
<Source logs and masking; count per class; decisive turns marked per case; divergence rule; regression suite membership.>

## Simulated users
<Cards: persona, goal, hidden fact and when it is revealed, stop rule; count per class.>

## Simulator validation
| Measure | Real (n) | Simulated (n, paired by card) | Tolerance set before | Difference with interval | Within? |
| --- | --- | --- | --- | --- | --- |
<Hand-read transcripts and invalid trials. Status: validated for <use cases> / indicative only.>

## One-shot to multi-turn drop
| Task set | One-shot rate | Multi-turn rate | Drop (paired interval) | Worst run | Tasks whose verdict changes |
| --- | --- | --- | --- | --- | --- |

## Repetitions and pass^k
<Scenarios per class (sized from the expected rate and the margin, or for the lower bound to clear the bar), k, per-conversation rate with Wilson interval on n = scenarios, observed pass^k (p^k only as a projection), bound when zero failures, cost of the run.>

## First failing turn
| Failed conversation | First failing turn | Type | Turns since the fact was given |
| --- | --- | --- | --- |
<Counts by position and by type, and what they point to.>

## Graders
<One binary criterion per grader; judge calibration status and reference.>

## Gate and exposure
<Bar per outcome and class on the rate; separate pass^k bar; maximum drop; for a ladder move, what the human reader used to catch; exposure = failure rate × monthly conversations of the population the sample represents × cost per failed conversation (from the business owner); decision rule if the interval is too wide.>

## Open questions
<What is missing, who provides it, by when.>
