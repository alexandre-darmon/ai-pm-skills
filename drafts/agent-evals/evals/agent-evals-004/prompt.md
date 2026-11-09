---
name: agent-evals-004
description: Retrieval quality of a policy Q&A assistant that only retrieves and answers, which is retrieval-evaluation's job (source - anonymised insurance compliance brief, 2026)
tags: [agent-evals, negative]
expected_outcome: Plans the retrieval measurement (labelled questions, recall at k, rank) without loading agent-evals; the assistant calls no tool that acts.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our compliance team's assistant answers employees' questions from 2,300 internal policies: it retrieves the 5 closest passages and writes an answer with citations. It calls no other system and never changes anything. Since the last re-indexing, reviewers see answers citing an outdated or unrelated policy.

Before we touch chunking or the embedding model, we want to know whether retrieval brings back the right passages. What should we measure, and how many labelled questions do we need?
