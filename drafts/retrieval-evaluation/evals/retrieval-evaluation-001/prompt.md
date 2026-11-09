---
name: retrieval-evaluation-001
description: Insurer policy-documents assistant at 71% answer accuracy, the team wants to switch LLM (source - anonymised insurance customer-service brief, 2026)
tags: [retrieval-evaluation, p0, nominal]
expected_outcome: Does not endorse the LLM switch yet; attributes the failed answers to a stage, measures retrieval apart (recall at the k sent, labelled queries including unanswerable ones, relevance pooled across retrievers), then generation on fixed contexts.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our customer-service agents use an internal assistant to answer questions on our home and motor insurance contracts. It searches about 2,300 PDFs (general conditions, special conditions, endorsements across 14 years of product versions), cut into 512-token pieces, and the top 5 pieces go to the LLM with the question.

Last month two senior agents graded 200 answers taken from the logs: 142 were correct, so 71%. The data science team proposes moving to a larger LLM, about four times the price per call, and says that should get us above 85%.

The steering committee meets next Thursday and wants a recommendation: do we switch the LLM, and how do we show it worked?
