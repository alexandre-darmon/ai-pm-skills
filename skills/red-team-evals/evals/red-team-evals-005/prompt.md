---
name: red-team-evals-005
description: 'A mortgage assistant team iterated its prompt and filters for three weeks on 200 injection attacks they wrote until none got through, then presents "0% attack success on 200 attacks" to model risk (source - anonymised retail mortgage assistant brief, 2026)'
tags: [red-team-evals, p1, red-line]
expected_outcome: 'Says a rate measured on the attacks the defence was tuned on proves nothing about new attacks; asks for a sealed held-out set written by testers outside the build team, compares the tuned set with the fresh set, gives the bound (zero in 200 still allows about 1.5%, Wilson about 1.9%) and sizes the fresh set on the tolerance (about 4/r held-out attacks), and moves the 200 attacks into the regression suite.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our mortgage pre-qualification assistant (about 15,000 conversations a month) goes to the model risk committee on Thursday. Over the last three weeks the prompt engineer and our two ML engineers wrote 200 prompt-injection attacks, ran them after each change to the system prompt and the input filter, and kept iterating until none of the 200 got through. The last run: 0 out of 200.

Our evidence slide says: "Attack success rate: 0% on 200 injection attacks (version 1.4). Release requested."

Can you review that slide before Thursday and tell me what to change?
