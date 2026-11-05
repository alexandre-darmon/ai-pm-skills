---
name: dpia-prescreen-002
description: 'Product-catalog search (source - anonymised retail brief, 2026)'
tags: [dpia-prescreen, nominal, red-line]
expected_outcome: 'DPIA not needed, zero criteria, reasons on file for the DPO.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our LLM rewrites shopper queries to search the product catalog. Queries are not stored or linked to an account. Only product data is indexed. Does this need a DPIA?
