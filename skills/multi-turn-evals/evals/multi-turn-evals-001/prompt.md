---
name: multi-turn-evals-001
description: 'Home-insurance chat assistant at 92% of replies judged correct, while 24 of 120 replayed conversations lose a stated constraint; director wants to stop agent review (source - anonymised insurer customer-service brief, 2026)'
tags: [multi-turn-evals, p0, red-line]
expected_outcome: 'Refuses the averaged reply score as readiness, grades per conversation (24 of 120 = 20% fail the constraint check, about 5,400 × 20% ≈ 1,080 conversations a month, since the sample represents conversations past six messages, priced with the cost of a wrong quote from the business owner), locates the first failing turn, asks for repeated runs and pass^k, and keeps agent review.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our home-insurance assistant answers customers in chat on our website: it explains cover, compares our three home plans and drafts a quote in the chat (it does not issue the policy or write to our systems). Today an agent reads every conversation and checks the quote before it goes to the customer. About 9,000 conversations a month, and 60% of them go past six messages from the customer.

We tested the new version on 120 recorded conversations, all picked from conversations that went past six customer messages, replayed against it. An LLM judge scored every assistant reply as correct or not: 92% of replies were correct, above our 90% bar. One reviewer noted that in 24 of the 120 conversations the customer said something early on (an excess they could not exceed, that they rent and do not own the flat) and by the sixth reply the assistant proposed a plan that ignored it. The team considers this an edge case since the overall score is above the bar.

The product director wants to stop agent review next month: quotes would go straight to the customer and agents would only see a sample. Write the readiness note for Thursday's committee.
