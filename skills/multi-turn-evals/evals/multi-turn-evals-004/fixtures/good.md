The plan measures the wrong unit, and the pass rule cannot work as written.

- Unit: the 400 replies are not 400 independent cases. Replies of one conversation share its customer, its facts and its errors, so the unit is the conversation (the scenario), and a conversation passes only if the constraints, corrections and hand-off all hold.
- Size for the estimate: at the pilot's 92%, knowing the rate within ±5 points takes n ≈ 1.96² × 0.92 × 0.08 / 0.05² ≈ 113 scenarios per gated class, not 50.
- Size for the gate: if L3 is gated on the Wilson lower bound clearing 90%, 113 to 140 scenarios cannot pass even when the assistant is as good as the pilot: 129 of 140 gives a lower bound near 86.5%. Clearing 90% on the lower bound at a true 92% takes about 830 scenarios. Choose before the run: pay for them, set the bar on the lower bound lower with a reason (for example 85% on a class where an error is caught downstream), gate a narrower class, or stay at L2.
- Runs: each scenario 3 times, k fixed before the run. The Wilson interval uses n = scenarios, with the 3 runs averaged per scenario. Report the observed pass^3, the share of scenarios whose three runs all pass. As a projection only, 0.92^3 ≈ 0.78, a floor when scenarios differ in difficulty; set the pass^3 bar from 0.90^3 ≈ 0.73, not 90%.
- Cost: 140 × 3 runs × 8 turns × 2 calls (assistant and simulated customer) ≈ 6,720 calls plus the judges.
- Exposure at L3: 25,000 × 8% ≈ 2,000 failed conversations a month at the pilot rate, times the cost of one wrong savings reply from the business owner.
