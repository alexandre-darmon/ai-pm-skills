# Go/no-go note: removing treasury approval on the AP payment agent (L4)

**Recommendation: NO-GO for next month.** Keep treasury approval. The evidence supports neither "reliable" nor "risk nil". It does not rule out that the agent could go live safely after more testing, and the path below gets there.

## 1. What the evidence shows

| Claim | What the data supports |
|---|---|
| "pass@3 = 90%, so it works" | pass@3 only says that at least one of 3 tries succeeded on 9 of 10 tasks. It is the wrong metric for a payment. In production every attempt executes, not the best one. If the 9 tasks each succeeded once in 3 tries, the per-trial rate is 30%. If it is 90% per trial, pass^3 is about 73%. We have not seen the per-trial results, so the real reliability is unknown. |
| "0 wrong payments in 30 trials, so risk is nil" | Zero observed failures in 30 trials still allows a true error rate of about 10% (rule of three, 3/30). Trials of the same task tend to fail together, so the effective sample is closer to 10 tasks, which allows about 30%. |

**Exposure the gate would accept.** The agent would pay about 1,200 payments a month, about 37M EUR in total.
- At the 10% bound, up to 120 wrong payments a month, about 3.7M EUR.
- Even a true rate of 0.1% means about 1 wrong payment a month, about 31k EUR.
- A payment cannot be undone, so recovery means chasing the supplier.

## 2. What the test did not cover

- **Sample size.** 10 tasks is too few for 1,200 payments a month. Real payments include partial deliveries, price and quantity tolerances, duplicate invoices, credit notes, changed bank details and missing goods receipts.
- **Forbidden events.** Nobody defined or checked these per task: paying without a matching goods receipt, paying the same invoice twice, paying above the limit, paying an unmatched invoice, or changing the payee.
- **False success.** We did not test what happens when `execute_payment` times out or fails, or when a lookup returns nothing. The risks are a blind retry that pays twice, or the agent reporting "paid" when nothing was paid.
- **Boundaries.** We did not test amounts just under, at and just over the monthly limit.
- **Grading.** We do not know whether trials were graded on the end state in the payment system or on the agent's final message. They must be graded on the end state, in a sandbox, not production.
- **Hostile input.** Invoices and emails come from outside. We have no measurement of injected instructions such as "pay to this new IBAN". This is the main fraud route.
- **Process.** There was no shadow run on real volume, no canary, no rollback or kill switch, and no named gate owner.
- **Test design.** Tasks, trials per task and pass bars were not fixed and signed before the run.

## 3. What treasury approval catches today

Removing approval removes the check that catches wrong payees, duplicates, over-limit payments and fraud. The suite must now catch exactly those events, and it does not yet.

## 4. Conditions for a future go

1. **Build the suite.**
   - Use at least 100 tasks drawn from real past invoices and incidents, each with a fixed starting state.
   - Include boundary tasks at the limit, false-success seeds on the payment call, and duplicate and changed-bank-detail cases.
   - Run in a sandbox, reset between trials.
2. **Fix the bars before running, signed by the gate owner.**
   - Zero forbidden events.
   - pass^3 above the agreed bar on payment tasks.
   - Zero false successes.
   - An attack-success upper bound per forbidden action, measured on attacks kept apart from prompt tuning.
3. **Report with bounds.** Show the upper bound and the monthly exposure it implies. If the bound is too wide for the cost of one bad payment, run more trials or stay at the current level.
4. **Run in shadow** on real volume: the agent proposes, treasury approves, and we compare every case.
5. **Roll out in stages.**
   - Start with a low per-payment cap and a low monthly limit.
   - Pay autonomously only on clean three-way matches.
   - Send everything else to a human.
   - Put a canary on a supplier subset, with a kill switch and a rollback plan.
6. **Monitor after the move.** Track duplicates, payee changes, overrides and false successes weekly.

## 5. Decision requested

- Do not remove treasury approval next month.
- Approve the test plan above, with a named owner for the gate.
- Reconvene when shadow-run results exist. A reasonable first step is a limited L4 for small, clean, repeat-supplier payments, not all 1,200 a month.

## 6. Open items

- Per-trial results for the 30 trials (needed to compute pass^3).
- The total monthly limit the CFO has in mind.
- The cost of a wrong payment, including recovery.
- Whether a sandbox of the ERP and bank interface exists.