---
name: multi-turn-evals-002
description: 'Card-dispute chat assistant: simulated customer checked on 50 real cases, 6-point gap inside a ±8 tolerance, so the team calls it validated and wants its 91% as the gate (source - anonymised retail bank brief, 2026)'
tags: [multi-turn-evals, p0, red-line]
expected_outcome: 'Says a point estimate inside the tolerance does not validate the simulator: the paired interval on the 6-point gap (9 of 50 pairs disagree) is about ±12 points, roughly -6 to +18, so it crosses the ±8 tolerance; with the observed 6-point gap, holding the whole interval inside ±8 needs a half-width of 2 points, about 1,700 cards at that disagreement rate, so fix the simulator first and size a fresh comparison for a gap near zero (about 110 cards), or write down a wider tolerance first. Adds the missing behaviour checks (median and 90th percentile, corrections, vague openings, facts given only when asked), notes the simulator scores higher than people, and keeps the 91% indicative: it gates nothing yet.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We run a chat assistant for card disputes at a retail bank: customers explain a card payment they do not recognise, the assistant asks what it needs, explains the procedure and prepares a dispute summary that an adviser checks.

We test new versions with a simulated customer (an LLM given a card: the customer's situation and the payment in question). Before trusting it we checked it against our logs, with tolerances agreed in advance. We took 50 real dispute conversations, wrote a card from each, and simulated each card once. Average customer messages: 5.1 in the real conversations, 4.6 simulated, inside our ±1 message tolerance. Resolved correctly: 41 of the 50 real conversations as rated by advisers, 44 of the 50 simulated ones as rated by our LLM judge, a gap of 6 points, inside our ±8 point tolerance. In 9 of the 50 pairs the two verdicts differ.

So the simulator is validated. We then ran 500 simulated conversations against the new version: 91% resolved correctly. Risk wants a release gate for next month's version. Can we use the 91% as the gate?
