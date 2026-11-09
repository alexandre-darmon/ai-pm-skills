---
name: retrieval-evaluation-003
description: HR policy assistant whose test set has only answerable questions, and an embedding-model swap planned next week with no re-run (source - anonymised industrial group HR brief, 2026)
tags: [retrieval-evaluation, p0, red-line]
expected_outcome: Refuses to confirm the swap without a re-run; adds questions whose answer is in no document with a plain "not found" as expected answer; treats the swap as a release compared on the same questions, per class, after judging newly surfaced passages.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our HR assistant answers the 9,000 employees of our industrial group (France, Germany, Poland) from 420 HR policies: leave, remote work, travel, benefits.

Our test set is 120 questions the project team wrote from the policies, one per policy section, each with the section that answers it. We ran it in June: the right section came back in the top 4 for 88% of questions.

Our vendor ships a new multilingual embedding model. It ranks much higher than our current one on the public MTEB leaderboard, so we plan to switch next Tuesday and rebuild the index overnight. We do not intend to re-run our test: the leaderboard is clear and the test set took weeks to build.

Please confirm the plan and draft the change note for the HR steering group.
