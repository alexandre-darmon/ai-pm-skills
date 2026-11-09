**What's missing, and why the framework choice waits**

Neither framework fixes the gaps below. Close them first, because they decide whether you need a framework at all.

1. **A done state.** "Loops until confident" isn't a stop condition. Model-reported confidence is unreliable. Define done as something checkable: for example, a summary is produced where every claim cites a retrieved policy clause and a claims API field, and the claim ID matches the case. Then add a hard cap on steps, spend and time.
2. **Named exits.** Each of these needs an outcome and a next step:
   - success
   - tool error
   - no policy found, which is different from a failed search
   - escalation to the adjuster
   - budget exhausted
   - policy denied

   Hitting a cap should hand the case to a human with the partial work attached. It should never fail silently.
3. **Tool contracts.** For the policy search and the claims API, write down:
   - when to use each one
   - named parameters
   - an empty result kept distinct from a failed call
   - that the claims API credential is read-only

   If the agent only reads and summarises, it stays at a low autonomy level and needs no write protocol. If anyone later adds a write such as notes, status changes or payments, it needs its own protocol: prepare then commit, approval, an idempotency key and a cap.
4. **A permission matrix.** List tool × level × approval, and scope the claims data to the adjuster's own cases.
5. **A memory and data policy.** Claims data is personal data. Decide what persists between runs, for how long, and what gets logged.
6. **Traces.** Log every tool call with its input, output and cost. Add an outcome field set from the exit, so you can compute cost per resolved case.
7. **Evals.** You need a set of real L1 cases with known answers, run repeatedly. The main failure to test for is a confident summary that cites a clause that doesn't apply.
8. **A loop type decision.** As described, this is a single loop: search, call the API, summarise, check done. Multi-agent needs a written justification for what one loop can't do, and I don't see one here.

**The two candidates, against what this design needs**

- **CrewAI** is built around role-based multi-agent crews. Your design has no need for that yet, so you'd pay for abstraction you don't use. Its looping and stop behaviour is also harder to control precisely.
- **LangGraph** gives you explicit state, checkpointing and resume, and human-in-the-loop interrupts. Those fit your needs if you add approval pauses or long-running cases, or if you want replayable traces. It's the better fit of the two for this use case.
- **Neither** may be necessary. A raw loop of about 100 lines against the model API, with the stop conditions and trace above, covers the current design. Pick LangGraph only if you can name a concrete need from the list above that the raw loop can't meet.

If you share the process steps, the claims API's capabilities (read-only or not) and your latency and cost limits, I can draft the full agent design document.