The judge reads the message, so it passes the 7 false successes: it cannot gate the move to updating without confirmation.

1. **Grade the end state.** Each task loads a starting state (the opportunity before the call) and the check queries the CRM record after the run: stage, amount, close date and next step against the expected values. The final message is graded only for what it tells the account manager.
2. **Count false success apart**: a run that says done with an unchanged record is a false success, 7 of 50 here (14%, 95% interval 7% to 26%).
3. **Seed failures**: a test double makes update_opportunity fail or time out at the last write, and returns an empty get_opportunity. The trial passes only if the agent says it did not finish.
4. **Locate the break**: label the first failing step of each of the 7 runs, and count failures in a matrix of last successful step × first failing step. The busiest cell is the next fix.
5. **Regression suite**: the 7 runs become regression tasks with their starting state, run on every prompt, tool or model change.
