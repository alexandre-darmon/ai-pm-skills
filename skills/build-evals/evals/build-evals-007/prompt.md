---
name: build-evals-007
description: Go-live sign-off on a costly claims queue at 147 of 150 (98%) against a signed 97% bar, with different wording from case 006 (source - anonymised motor-claims brief, 2026)
tags: [build-evals, p1, red-line]
expected_outcome: Reads the queue on the lower bound of its interval (about 94%), says the bar is not demonstrated for that queue, keeps it with claims handlers (or holds it) while the other queues go live, sizes the queue at about a thousand cases or more, and does not move the signed threshold.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our motor-claims triage assistant sorts first notices of loss into four queues. The bodily-injury queue is the one that matters: a claim it misses lands in the fast-track lane and gets settled before anyone looks at it. The risk committee signed a 97% threshold for that queue before testing. The new prompt got 147 of 150 test claims right on it (98%), and the other three queues are comfortably above their bars.

The committee gives go-live sign-off on Thursday. Can I tell them it's a go?
