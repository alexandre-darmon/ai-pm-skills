---
name: retrieval-evaluation-004
description: Test plan for an expense agent's tool calls before it submits alone, which is agent evaluation (source - anonymised finance-ops brief, 2026)
tags: [retrieval-evaluation, negative]
expected_outcome: Plans checks on tool calls, end state and forbidden actions without loading retrieval-evaluation; nothing here retrieves documents.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our expense agent reads a photographed receipt, calls create_expense with the amount, date and category, then calls submit_for_approval. Expenses above 500 EUR need the manager's approval before payment. Today an employee clicks to confirm each step; next quarter we want the agent to submit on its own.

How should we test it before we let it submit alone? What exactly do we check on each run?
