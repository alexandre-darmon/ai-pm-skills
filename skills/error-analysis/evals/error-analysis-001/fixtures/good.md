No: do not set up a 1–5 judge on helpfulness, accuracy and tone. Those metrics were picked from a generic list before anyone read the outputs, a weekly average of 3.8 tells nobody what to fix, and a Likert scale is hard to calibrate. Read the real traces first, then choose graders from what you find.

**1. Mask, then sample (about 100 traces).** Mask claimant names, policy numbers and injury details before anyone reads a trace or sends it to a model. Draw a random stream of 60 traces, in proportion to motor and home, and a targeted stream of 40: thumbs-down, escalations to a senior, long conversations. Rates come from the random stream only: the targeted traces over-represent failures.

**2. One accountable expert reads.** The claims quality lead (one named person) reads each trace and writes a free note on what went wrong, on the first upstream failure: a wrong clause retrieved and then a wrong deductible is one retrieval failure.

**3. Read to saturation.** Stop when about 20 consecutive traces add no new failure mode (usually 50–100). Below that, the list is provisional.

**4. Group the notes into failure modes**, each with a binary pass/fail definition and a pass and a fail example (e.g. "fails when the deductible stated differs from the policy schedule").

**5. Price each mode.** A caught error costs 10 min × 54 EUR/h = 9 EUR; one that reaches a claimant about 150 EUR. Expected monthly cost = 9,000 × share in the random stream × cost per occurrence. If 6 of 60 random traces show a wrong deductible: 10% (5%–20%) × 9,000 × 9 EUR ≈ 8,100 EUR a month, plus 150 EUR for each one handlers miss.

**6. Decide per mode.** A specification failure (the prompt never asked for it, a wording missing from the index) is fixed, with no evaluator. A generalisation failure gets an evaluator: a code check first (deductible against the policy system), an LLM judge per mode only when code cannot decide, calibrated against the expert's labels.
