**Decision: no-go. Keep the treasury approval.**

1. pass@3 is the wrong gate for payments: a task counts as passed after one success in three tries, but a payment cannot be undone and production gets every attempt, not the best one. We need the per-trial success rate and pass^3 (all three trials succeed).
2. Even at 90% per trial, pass^3 = 0.9^3 = 0.73. And 9 of 10 tasks passing at least once is compatible with as little as 30% per trial.
3. Zero wrong payments in 30 trials is not zero risk: by the rule of three (3/n) the true rate can still be up to 10%, so up to 120 wrong payments a month at 1,200 a month.
4. Before the next review: 50 payment tasks with starting states and forbidden events, k = 5 fixed before the run, in a sandbox.
