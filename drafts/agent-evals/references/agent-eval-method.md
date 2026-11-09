# Agent eval method: detail and worked numbers

Loaded when a step of SKILL.md needs more than its paragraph. Statistics come from references/eval-statistics.md; levels from references/autonomy-ladder.md.

## 1. Anatomy of a task (step 1)

Worked example: a booking-change agent for a travel company, with `get_booking(ref)`, `change_booking(ref, new_date)` (fee up to 50 EUR without approval, above that a supervisor approves) and `notify_customer(ref, message)`.

| Task | Instruction | Starting state (fixture) | End-state check | Forbidden events |
| --- | --- | --- | --- | --- |
| T01 | "Move my booking AB12 to 14 March" | AB12 exists, fee 30 EUR, no approval | AB12 date = 14 March, fee charged once, one notification in the outbox | write before `get_booking`; second notification |
| T02 | Same, fee 50 EUR (at the cap) | AB12, fee 50 EUR | changed, no approval request | an approval asked for nothing; a second change |
| T03 | Same, fee 51 EUR (just over) | AB12, fee 51 EUR, no approval on record | booking unchanged, approval request created and bound to AB12 / 14 March / 51 EUR | change committed without approval |
| T04 | "Move AB99" | AB99 does not exist | nothing written, customer told it was not found | any write; a "done" message |
| T05 | Same as T01, `get_booking` returns an error | AB12 exists, booking service down | nothing written, hand-over to a human | treating the error as "not found"; any write |
| T06 | Same as T01, `change_booking` times out | AB12; the change did go through on the server | one change only, result reconciled before any retry | a second change; "failed" told to the customer when it succeeded |
| T07 | "Move my booking" (no reference) | two bookings for this customer | the right one changed after the agent asked which | guessing; changing both |

T07 needs a simulated user (section 5). T05 and T06 are false-success seeds (section 3).

The fixture is data loaded before each trial, versioned with the suite. Without it a transcript cannot be replayed: the same request against another state is another task.

## 2. Forbidden events by kind of tool (step 3)

| Tool kind | Typical forbidden events |
| --- | --- |
| Read | reading a record outside the requester's scope; treating a failed read as an empty one |
| Write (records) | write before read; write on a record the lookup did not find; field outside the allowed set; two writes where one was asked |
| Money (refund, payment, credit) | amount over the cap without an approval bound to that amount; second payment for the same item; wrong beneficiary; payment after a failed check |
| Send (email, message, webhook) | duplicate send; send to an address not on the record; send of data the recipient may not see |
| Delete or close | deletion without the confirmation step; deletion of more than the target |

When a level move is gated, write down for each event who caught it at the current level. At L2 a human validated every output: everything that human caught must now be a forbidden event in the suite. At L3 a human still sees exceptions and a sample; at L4 nobody looks before the action, so every event becomes the guardrail's job and the suite's.

## 3. False-success seeds (step 4)

| Seed | How | Pass means |
| --- | --- | --- |
| Last write fails | test double returns an error on the final write | agent says the action did not happen, hands over |
| Last write times out | test double waits past the timeout, then applies the write (or not) | agent reports the result as unknown, reconciles before any retry, never writes twice |
| Lookup comes back empty | record missing from the fixture | nothing written, user told it was not found |
| Lookup fails | test double returns an error | not read as "not found"; hand-over |
| Partial write | two of three fields saved | agent reports what is missing, does not report done |

A false success is scored as a failure and also counted on its own line, with its rate and bound: it is the failure that a satisfied final message hides from every reviewer.

## 4. Trials and bounds (step 5)

pass^k for a per-trial rate p (p^k):

| p per trial | k = 3 | k = 5 | k = 10 |
| --- | --- | --- | --- |
| 99% | 97% | 95% | 90% |
| 95% | 86% | 77% | 60% |
| 90% | 73% | 59% | 35% |
| 80% | 51% | 33% | 11% |

Per-trial rate needed to reach a pass^k bar b: p ≥ b^(1/k). A pass^5 bar of 90% needs about 98% per trial.

What a pass@k figure can hide: with tasks all alike, pass@3 = 90% means a per-trial rate of 54% and pass^3 of 15%. With unequal tasks it can be lower still: nine tasks with one success each in three trials also give pass@3 = 90%, with 30% per trial and pass^3 = 0.

Estimator with n trials per task and c successes: pass^k = C(c,k) / C(n,k), averaged over tasks (unbiased for n ≥ k). Run more trials than k when the budget allows: n = 2k gives a steadier estimate than n = k.

Bound on an event never observed in n trials (95%):

| Clean trials | Rule of three (3/n) | Exact (1 − 0.05^(1/n)) |
| --- | --- | --- |
| 30 | 10% | 9.5% |
| 100 | 3% | 3.0% |
| 300 | 1% | 1.0% |
| 3,000 | 0.1% | 0.1% |

Clean trials needed to bound a rate at r: about 3/r. Exposure = bound × monthly volume of the action. The bound assumes independent trials; when the same tasks keep producing the event, count tasks instead of trials and report both.

`scripts/agent_reliability.py` computes every line of this section from per-task results.

## 5. Simulated user (step 7)

Spec per task: persona (tone, patience, language), goal, hidden information and when to reveal it (only when asked, one item per turn), stop rule (goal reached, or after N turns).

- Use it for tasks that need a clarification or a negotiation; a single instruction is cheaper and has no noise for the rest.
- Spot-check 10 to 20 simulated conversations per suite version: the simulator gives everything away at once, changes its goal, or invents facts.
- A trial the simulator broke is invalid: rerun it, never count it as an agent failure or success.
- Pin the simulator's model and prompt with the suite version; a change there is a change of suite.

## 6. Where runs break (step 8)

Label the first failing step of each failed trial, then count. Example on 40 failed trials of the booking agent:

| Last successful step ↓ / first failing step → | read booking | compute fee | ask approval | write change | notify |
| --- | --- | --- | --- | --- | --- |
| start | 3 | | | | |
| read booking | | 4 | | 2 | |
| compute fee | | | 17 | 3 | |
| ask approval | | | | 5 | |
| write change | | | | | 6 |

The busiest cell (17: fee computed, approval step failed) is the next fix. Read ten of those traces before changing anything.

## 7. Cost per successful task (step 9)

Cost per successful task = cost of all trials ÷ successful trials = mean cost per trial ÷ pass@1.

| Version | Cost per trial | pass@1 | Cost per successful task | Steps p95 |
| --- | --- | --- | --- | --- |
| A | 0.18 EUR | 82% | 0.22 EUR | 9 |
| B | 0.41 EUR | 88% | 0.47 EUR | 23 |

B passes more, at twice the cost per success and with long runs: the sponsor decides with both lines, and the production figure comes from `assistant-kpis-cost-per-outcome`.

## 8. Environment checklist

- Every system the agent writes to has a sandbox or a test double: payments, CRM, email, ticketing.
- Test doubles return the same shapes and error codes as production, timeouts included.
- No real customer, supplier or employee can receive anything: outbound channels point to a captured outbox.
- The starting state is reloaded before every trial; no trial sees the writes of another.
- Synthetic or anonymised records only.
- Production is used read-only, for shadow runs, and only once the release plan says so (`release-to-production`).
