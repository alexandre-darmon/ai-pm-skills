---
name: agent-evals-003
description: Sales-ops agent whose runs end with "Done, the CRM is updated" while the opportunity is unchanged in 7 of 50 runs, graded by a final-message judge (source - anonymised B2B sales operations brief, 2026)
tags: [agent-evals, p1, edge-case]
expected_outcome: Grades runs on the CRM end state, not the closing message; seeds tool failures and timeouts at the last write; counts false successes apart; labels the first failing step in a last-success by first-failure matrix; turns the 7 runs into regression tasks.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

After each client call, our sales-ops agent reads the call notes and updates the opportunity in the CRM (stage, amount, close date, next step) through three tools: get_opportunity, update_opportunity and log_activity. It runs about 3,000 times a month for 140 account managers.

Last week we reviewed 50 runs by hand. In 7 of them the agent's last message was "Done, the CRM is updated", but the opportunity in the CRM had not changed. In the other 43 the update was there.

Our current eval is an LLM judge that reads the agent's final message and checks it is clear and matches the call notes. It scores 96%, and we planned to use it to let the agent update opportunities without the account manager confirming. What should we change?
