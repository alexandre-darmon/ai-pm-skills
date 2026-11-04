---
name: ai-act-classification-002
description: Internal IT FAQ bot on a commercial LLM, answering employees' questions from IT documentation (source - anonymised insurance IT brief, 2026)
tags: [ai-act-classification, p0, edge-case]
expected_outcome: Classifies it outside the prohibited practices and Annex III, so not high-risk, with the transparency duty of art. 50(1), raises art. 50(2) for counsel and AI literacy (art. 4), flags the general-purpose model use separately, and never says there are no obligations.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our IT team built a chatbot on a commercial LLM, called through the vendor's API. It answers employees' questions (VPN, passwords, printers, software requests) from our IT documentation, and links to the ticketing tool when it cannot help. It takes no action itself. About 1,800 employees use it.

Legal asked us to classify it under the AI Act before the wider rollout. Can you do it?
