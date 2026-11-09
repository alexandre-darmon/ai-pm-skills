---
name: retrieval-evaluation-002
description: Bank procedures assistant with recall@5 at 93% but a fifth of answers stating things the passages do not back; platform team wants to re-index (source - anonymised retail banking back-office brief, 2026)
tags: [retrieval-evaluation, p1, edge-case]
expected_outcome: Places the failure in generation, not retrieval; measures faithfulness claim by claim on fixed contexts with a validated judge; fixes the prompt and abstention before any re-index or model change.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our back-office assistant answers operators' questions from 600 internal procedures (account closures, successions, garnishments). The generator receives the top 5 passages.

Our retrieval test: 180 questions from operator tickets, each labelled by two procedure owners with the passages that hold the answer, pooled from three search setups. The right passage is in the top 5 for 93% of them, and roughly the same across the three procedure families.

But when the procedure owners read the answers, about 20% of them contain at least one statement the passages do not back up, typically a deadline or a fee that is in none of the passages sent, or one taken from a neighbouring procedure.

The platform team proposes two sprints to re-index with a newer embedding model and smaller pieces. Is that the right next step? What should we do?
