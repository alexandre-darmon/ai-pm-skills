# Multi-turn method: cards, checks and a worked example

Loaded on demand by `multi-turn-evals`. Statistics are in references/eval-statistics.md; the ladder in references/autonomy-ladder.md.

## 1. Conversation outcomes, as binary checks

| Outcome | Passes when | Typical grader |
| --- | --- | --- |
| Goal reached | the user leaves with what they came for, or a correct refusal or hand-off | code check on the final state of the answer (an offer, a summary) or a judge on the transcript |
| Constraint kept | every constraint stated earlier is respected at every later turn that depends on it | list the constraints per case; code check where the value is visible (amount, product type), judge otherwise |
| No self-contradiction | no later turn states the opposite of an earlier one without saying it changed and why | judge on the whole transcript, one criterion |
| Recovery after correction | once the user corrects a fact, every later turn uses the corrected fact | decisive turn marked after the correction; code check on the value |
| Correct hand-off | it escalates when the case requires it, and the hand-off carries the facts already given | code check on the hand-off event and its fields |
| No premature answer | when a fact the answer depends on is missing, it asks before answering | decisive turn = the first turn where the fact is missing |

A conversation passes when every outcome that applies to it holds. Report each outcome's rate apart too: a single figure hides which one fails.

## 2. Scripted case card (from a real log)

```
id: savings-017 (source: anonymised log, month, channel)
use case and class: savings product question, retail
turns: 9 (user turns kept verbatim after masking)
facts and constraints: t1 "I can't lock money for more than 12 months"; t3 "joint account with my partner"
decisive turns: t5 offer must respect the 12-month limit; t7 correction "actually it is in my name only" -> t8 onward uses single holder
expected at the end: product proposed within the constraints, or a hand-off to an adviser
divergence rule: if the new reply makes t6 meaningless, mark diverged and rewrite the case
```

## 3. Simulated user card

```
persona: retired customer, low digital confidence, short messages, French
goal: move 20,000 EUR to a savings product without locking it more than 12 months
hidden fact: the money comes from an inheritance still in probate (reveal only if asked about the source of funds, or at turn 6)
behaviour: answers one question at a time; corrects the assistant once if it assumes a joint account
stop: goal reached, says goodbye, or 14 turns
```

Write cards from real conversations, not from imagination: the share of vague openings, corrections and late facts in the cards follows what step 4 measured in real logs.

## 4. Simulator validation sheet

Fix the tolerances before simulating. Each simulated conversation is paired with the real conversation its card came from, so every row is a paired difference: report it with its interval, and a row passes only when the whole interval sits inside the tolerance. A point estimate inside the tolerance is not enough: with 80 unpaired conversations a side and pass rates near 80%, the interval on the difference is about ±12 points.

Size the cards for the tolerance. On the outcome row, the paired interval is about ±1.96 × √(d / n), with d the share of cards whose two verdicts disagree: at d = 10%, 50 cards give about ±9 points, 80 about ±7, 100 about ±6, and ±5 needs about 150. Those half-widths are what the tolerance allows only when the true gap is near zero. The whole interval sits inside ±T only when the half-width is at most T minus the gap you expect, so size for T − |gap|: with a 6-point gap against ±8, the half-width must be 2 points or less, about 1.96² × d / 0.02² cards (some 1,700 at d = 18%). When that is out of reach, fix the simulator first (a gap that leans one way is usually a too-cooperative simulator), then size a fresh comparison for a gap near zero; or widen the tolerance and write the wider one down before the comparison.

| Measure | Real (n = 80) | Simulated (n = 80, paired) | Tolerance | Within? |
| --- | --- | --- | --- | --- |
| Turns per conversation, median / 90th percentile | 7 / 13 | 4 / 6 | ±1 / ±2 | no |
| Share with a user correction | 28% | 4% | ±7 points | no |
| Share of first messages missing a needed fact | 45% | 10% | ±10 points | no |
| Facts given only when asked | 60% | 15% | ±10 points | no |
| Abandonment | 12% | 0% | ±5 points | no |
| Assistant pass rate, simulated vs real rated by people | 71% | 90% | difference within ±7 points (what 80 cards support) | no: +19 points, paired 95% interval about +8 to +29 |

Such a simulator is too cooperative: it gives everything up front, never corrects, never gives up, so the assistant looks better than it is. Fix the cards (vaguer openings, scripted corrections, hidden facts) or condition the simulator on real user profiles, then measure again. A simulator that passes on one use case is not validated for another.

## 5. Measuring the one-shot to multi-turn drop

1. Take 50 or more tasks from the one-shot suite whose answer depends on two or more facts.
2. For each, write the multi-turn version: one fact per turn, the order users actually follow, optionally one correction.
3. Run both versions k times with the same model, prompt and settings.
4. Report per task: one-shot pass rate, multi-turn pass rate, difference; over tasks: the mean drop with its paired interval (references/eval-statistics.md §5), the worst run, and the share of tasks whose verdict changes between runs.

A drop that comes with a wide spread between runs is an unreliability problem (same task, different outcome); a drop with a narrow spread is a capability problem on that pattern. The fixes differ: the first calls for recaps, constraint lists carried in the prompt, or asking before answering; the second for a different model or a narrower scope.

## 6. Worked example: averaged turn scores against conversations

A home-insurance assistant, 120 test conversations drawn from conversations past six customer messages, a judge marked 92% of assistant turns correct. Read per conversation, 24 of 120 lost a constraint the customer stated (excess cap, tenant not owner) by turn 6.

- Per-conversation failure on that outcome: 24/120 = 20%, Wilson 95% interval about 14% to 28%.
- Apply the rate to the population the sample represents. The 120 are all past six messages, so with 9,000 conversations a month and 60% past turn 6: 5,400 × 20% ≈ 1,080 conversations a month with a lost constraint, between about 750 and 1,500. Applying it to all 9,000 would assume short conversations fail as often, which was not tested. Had the 120 been drawn from all traffic, the exposure would be 9,000 × 20% ≈ 1,800.
- Price it: 1,080 × the cost of one wrong quote that reaches a customer (rework, complaint handling, remediation if a policy was sold on it). Ask the business owner for that cost (references/roi-model.md); do not invent it.
- First failing turn: count where each of the 24 dropped the constraint and how far back it was stated.
- Gate: not ready for L3; the reviewer stays until constraint kept reaches its bar on the lower bound, over k = 3 runs per scenario, with the observed pass^3 against its own bar.

## 7. Sizing a gate on the lower bound

Estimating a rate and passing a gate on its lower bound need different sizes. At 92% expected, ±5 points takes about 113 scenarios; but a gate that asks the Wilson lower bound to clear 90% fails at that size even when the assistant is exactly as good as expected (129 of 140 gives about 86.5% to 95.6%). Clearing 90% on the lower bound at a true 92% takes about 830 scenarios. The choices, written before the run: pay for those scenarios; set the bar on the lower bound lower, with the reason (for example 85% on the lower bound for a class where a failure is caught downstream); gate a narrower class; or keep the current level.

pass^k has its own bar. The observed pass^k is the share of scenarios whose k runs all pass. p^k is a projection that assumes every scenario has the same p; when difficulty varies, the observed value is higher, so p^k is a floor for planning. Start the pass^k bar from the per-conversation bar to the power k (0.90^3 ≈ 0.73), never from the per-conversation bar itself.

## 8. Cost of a run

Calls = scenarios × k × turns × (1 assistant + 1 simulator) + scenarios × k × judge calls per outcome. Example: 140 scenarios × 3 runs × 8 turns × 2 = 6,720 calls, plus 420 conversations × 3 outcome judges = 1,260 judge calls. Price it before the run and cut classes, not k.
