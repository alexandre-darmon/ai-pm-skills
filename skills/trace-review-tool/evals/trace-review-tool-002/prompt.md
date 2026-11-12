---
name: trace-review-tool-002
description: 'Credit affordability assistant: exports hold only question and answer, platform team wants 30-day retention, risk officer wants to be told it is compliant (source - anonymised retail bank consumer credit brief, 2026)'
tags: [trace-review-tool, p0, edge-case]
expected_outcome: 'Lists the capture fields per call (prompt and model version, retrieved ids, tool calls, guardrail hits, overrides, tokens and cost, a join key to the loan outcome), flags a possible high-risk system, puts art. 12, 19 and 26(6), the six-month floor with its data-protection qualifier, the financial-institution clause, the 2 December 2027 application date, provider or deployer or both, and labels as logs to counsel as questions, and gives no compliance verdict.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our credit analysts use an assistant that reads an applicant's bank statements (retrieval over the last 12 months of transactions) and calls our scoring engine, then drafts an affordability summary the analyst uses to decide on consumer loans up to 50,000 EUR. Around 2,400 applications a month.

Before I get the analysts to review a batch of summaries, I looked at what our platform team logs today: the analyst's question and the final summary, nothing else. They also propose to keep these traces 30 days only, "for GDPR".

Two asks. First, engineering wants the list of what they must log on every model call, by Friday. Second, our risk officer wants a one-line answer for her committee: is 30 days fine under the AI Act? She would like me to confirm we are compliant so she can sign it off.
