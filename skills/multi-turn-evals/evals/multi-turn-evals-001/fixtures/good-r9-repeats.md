# Readiness note: removing agent review of home-insurance quotes

**Recommendation: don't remove agent review next month.** The evidence supports "the assistant answers individual questions well." It doesn't support "quotes can go to customers unchecked."

## Why the 92% doesn't answer the question

- **The score is per reply, but the customer gets a conversation.** A reply can be correct on its own and still break something the customer said five messages earlier. A per-reply average can't show that.
- **Constraint failures were found, not measured.** In 24 of 120 conversations (20%), the assistant proposed a plan that ignored a constraint the customer had stated, such as a maximum excess or "I rent." The reviewer spotted these. Nobody graded for them systematically, so 20% is a floor for this one failure type.
- **At best, 80% of conversations pass.** That is 96 of 120, with a 95% interval of about 72–86%. The upper end is below the 90% bar. Any other conversation-level failures would lower it further.
- **These are the failures that matter most.** A quote for an owner-occupier given to a renter, or one over the customer's stated excess limit, is a wrong quote. Agent review exists to catch exactly this.
- **The sample is the long conversations only.** All 120 went past six customer messages, so the result describes that 60% of traffic. The other 40% was not tested, and no conclusion should be drawn for it.

## Exposure if review stops

- 60% of 9,000 is about 5,400 long conversations a month.
- At a 20% failure rate, that is roughly 1,080 a month (about 750–1,540 across the interval) reaching customers with a quote that ignores something they said.
- We don't have the cost of one failed conversation (rework, complaint, remediation, any regulatory exposure of a mis-sold policy). Please get that figure from the business owner before Thursday. It turns the count above into a money figure.
- Sampling after the fact would detect the problem, but only after customers have received the bad quotes.

## What the test did not establish

- **No repeated runs.** Each conversation was replayed once, so we don't know how often the same conversation passes or fails.
- **The judge is unchecked.** I haven't seen it calibrated against expert labels. That matters because it scored every reply.
- **Replays can drift.** The customer's scripted messages may stop making sense after the new assistant's replies. Diverged cases should be marked as such, not as failures.
- **Replies aren't independent.** They come from 120 conversations, so the sample is effectively 120, not the number of replies.
- **There is no one-shot versus multi-turn comparison on the same tasks.** That is the direct measure of how much the assistant degrades over a conversation.

## Proposed path

1. **Keep full agent review now.** Agents can also tag each constraint failure as they review. That builds the real failure data cheaply.
2. **Find where each failure starts.** For the 24 conversations, record the turn where the constraint was dropped and how far that is from where the customer stated it. This points to the fix: context handling, premature quoting, or correction handling.
3. **Fix, then re-test at conversation level.** Each conversation passes only if every check holds. The checks are:
   - stated constraints kept to the end
   - no self-contradiction
   - corrections applied and not reverted
   - missing facts asked for, not guessed
   - correct hand-off when needed

   Use a code check where possible (for example, the stated excess appears in the quote). Otherwise use a judge calibrated against expert labels.
4. **Fix the gate before the run.** The committee should agree on these before the next test:
   - the number of scenarios
   - the number of repeats per scenario (3–5)
   - a bar for each check, strictest on "constraint kept"
   - a separate bar for conversations that pass on every repeat (a 92% per-conversation rate gives only about 78% over 3 runs)
   - a maximum allowed drop from one-shot to multi-turn performance
5. **Size the test honestly.** About 113 scenarios gives ±5 points at 92%. Gating on the lower bound against a 90% bar takes about 830, so either test more or narrow the claim.
6. **Phase the change.** If it passes, relax review first for the lower-risk population (short conversations, once those are tested too). Keep review for long conversations or any conversation where the customer stated a constraint, until the data supports more.

## Suggested wording for the committee

"The new version scored 92% of replies correct, but only about 80% of the long conversations tested handled the customer's own constraints. Those conversations are about 5,400 a month. We recommend keeping agent review, fixing the constraint handling, and re-testing on whole conversations against a gate set in advance."

I haven't verified any of the figures beyond what you gave me. The cost per failed conversation and the judge's calibration status are the two open items.