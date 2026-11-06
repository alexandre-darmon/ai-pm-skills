---
name: ai-data-requirements-002
description: 'Product-catalog search with no personal data (source - anonymised retail brief, 2026)'
tags: [ai-data-requirements, nominal, red-line]
expected_outcome: 'No personal-data flags, freshness stated as a number, volumes stated or asked.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our site search will use an LLM to rewrite shopper queries against the product catalog: 80,000 SKUs with title, description, price and stock, maintained by the merchandising team. The search box stores nothing about who searches. Write the data spec.
