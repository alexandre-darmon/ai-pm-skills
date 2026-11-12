---
name: ai-feasibility-spike
description: 'Use when someone wants to prototype or spike an AI feature or agent on the real model before a PRD, or has spike results to read, write up as a go note or offer as validation evidence.'
license: CC-BY-4.0
metadata:
  stage: "build"
  version: "0.2.3"
  status: "tested"
  eval_threshold: "0.80"
  legal: "false"
  last_verified: "2026-11-11"
  autonomy_relevant: "true"
  depends_on: "ai-opportunity-assessment"
  feeds: "llm-feature-prd, build-evals, prototype-handover"
  sources: "cagan-prototypes-products, singer-shape-up, kromer-learn-measure-build, shankar-validators, wilson-interval, willison-lethal-trifecta, metr-ai-dev-productivity, anthropic-agents, esma-qa-2103, dora-rts-ict-risk, dora, gdpr, replit-db-incident, own-spikes"
---

# ai-feasibility-spike

## When to use
- Before a PRD or a budget bet, someone asks "can the model actually do this?" and nobody has run it on realistic cases.
- A PM or engineer wants to prototype an AI feature or agent with a coding agent "to see if it works": a spike, a POC, a hackathon build.
- An opportunity assessment ended on "explore": one question must be answered before a go or a no-go.
- A spike has run and its numbers need reading, or reusing as validation evidence.
- Do not use to decide whether AI fits at all, or for a sponsor pitch, even after a prototype: that is `ai-opportunity-assessment`.
- Do not use to choose between models on an existing suite (`model-selection`) or to build the eval set that gates a release (`build-evals`).

## Inputs
Mandatory: the task (input, output, who uses it), the question classes and the error that costs most, the model and hosting route production would use, where the cases can come from.
Ask if missing: the decision the spike feeds and who takes it; the cost of today's process or the value of one correct answer (for the appetite); the target autonomy level of the step (references/autonomy-ladder.md); whether the spike's tool and model contract are authorised (step 3).
When results are already in: counts per class, the bar and appetite written before the run (if any), spend and hours from logs.

## Method
1. **Write the one question.** One sentence the spike answers yes or no: "can model X, at L2, sort claims emails into four types well enough, under 0.02 EUR per correct answer?" Two questions are two spikes. Plan in reverse (references/build-to-learn.md): the question, then the measurement, then the smallest build that produces it.
2. **Fix four items before building**, dated and signed by the person who owns the business risk:
   - **Appetite**: a time box in days (five by default, never "a few weeks") and a maximum cost per correct answer, derived from what one correct answer is worth (references/roi-model.md), not from what the build will cost.
   - **Bar per class**: a target rate and a stop line, the rate under which the idea is not worth pursuing. The class whose error costs most gets the stricter target. Say which classes the product cannot drop.
   - **Kill date**: past it, the spike stops by default. Extending it is a new decision with a new appetite, never a drift.
   - **The decision it feeds** and who takes it.
   A bar written after the run describes the results; it does not judge them.
3. **Check the tool, the data and the size before any case enters it.**
   - **The tool.** In a financial entity, a laptop script, notebook or API account built outside the ICT function is an ICT asset, and only authorised software may run: it must be authorised and registered (`esma-qa-2103`; RTS 2024/1774 art. 11(2)(c)). Elsewhere, the company's end-user computing policy sets the same check. A model account opened outside procurement (a company card, accepted online terms) is an unregistered ICT third-party arrangement: DORA third-party risk and the register of information apply (`esma-qa-2103`, `dora`). Personal data sent to it needs processor terms, and transfer terms outside the EEA: a question for the DPO (`gdpr`). Ask IT risk and the DPO in parallel; synthetic cases do not wait.
   - **The data.** An authorised tool does not unlock production data. A spike is a non-production use: synthetic, anonymised or pseudonymised cases only (art. 16(5), applied to user-built systems by art. 16(9)). Real data only for an approved, time-limited testing occasion reported to ICT risk (art. 16(6)). No production credentials, ever (references/build-to-learn.md, red line 1).
   - **The size.** Size each gated class before writing cases: the smallest n where n−1 of n still has a Wilson lower bound at or above the stop line (`python3 scripts/spike_readout.py --plan <stop>`). Stop line 70%: 15 cases; 75%: 19; 80%: 25; 85%: 34; 90%: 53 (9, 12, 16, 22, 35 if no error is allowed). At 10 cases even 10 of 10 has a lower bound near 72%, so a 75% stop line can never read promising. A stop line out of reach within the appetite is lowered and signed before the run, or the class leaves scope. Over-represent the costly classes and state the synthetic share; most spikes land at 40 to 120 cases.
4. **Run the lethal-trifecta check** on the prototype's design: does it touch private data, read untrusted content (emails, uploads, web pages, tool outputs), and have a way to send data out (send a mail, call a URL, write to a shared system)? All three together: remove one in code (no outbound tool, read-only access, a human sends) or stop. A sentence in the prompt removes nothing.
5. **Workflow before agent.** Start with one model call or a fixed chain: code does the lookups, the model does the judgment. Move to an agent loop only when the workflow fails on cases that need the model to choose its next step, and name those cases. Use production's model and hosting route, or neither quality nor cost transfers.
6. **Read outputs, then grade.** Read the first 10 to 15 outputs before scoring anything: the definition of "correct" sharpens on real answers (criteria drift). Revise the criteria, log each revision with its date and reason, and re-grade every case under the final criteria. Only the definition of correct may move; the bar, stop line and appetite do not. The drift log goes to `build-evals`.
7. **Report per class as n of N with a Wilson interval** (references/eval-statistics.md §2), never one pooled rate. Read each class against its bar and stop line, by hand or with `python3 scripts/spike_readout.py --class name=k/n --bar 0.90 --stop 0.75 --spend <total> --appetite <max>`:
   - **clears**: lower bound at or above the bar.
   - **promising**: point at or above the bar, lower bound under it but at or above the stop line. Plausible, not demonstrated.
   - **undecided**: the interval straddles the stop line, or the point is under the bar with the upper bound above it.
   - **short**: upper bound under the bar. This approach does not reach it.
   - **dead**: upper bound under the stop line.
   A point above the bar with the lower bound under it is "not demonstrated", never "meets the bar": 9 of 10 fits a true rate near 60%.
8. **Cost per correct answer** = model spend ÷ correct answers, never ÷ all answers, set against the appetite. When a person must fix wrong answers, price the rework beside the spend: wrong answers × the cost of one correction (today's unit cost by default). Report the hours spent from the logs, not the team's impression (references/build-to-learn.md, red line 5). "It will get cheaper with a smaller model" is a hypothesis for the next spike, not a result.
9. **Decide**, one of three:
   - **Go to PRD** (`llm-feature-prd`, with the spike report as input): every class the product cannot drop is promising or clears, cost within appetite, trifecta resolved. Promising classes are listed as not demonstrated, for `build-evals` to size.
   - **Reshape**: a class undecided or short, or cost over appetite. Change one thing (workflow instead of agent, narrower scope, a class dropped, a lower autonomy level, a cheaper model) and run a new spike with its own appetite and kill date. More cases for an undecided class is a reshape, not an extension.
   - **Stop**: a class the product cannot drop is dead, or the kill date passed without an answer. Write down what was learned.
10. **Say what the spike is not.** A spike number is never release evidence: a few dozen cases not sampled from traffic, criteria refined during the run, a throwaway harness (references/build-to-learn.md, red line 4). Name what `build-evals` must do instead: cases sampled from production traffic per class; criteria frozen; a private holdout; thresholds signed before the run; a run on the engineering build, gated by `release-to-production`; and each gated class sized for the margin between its expected rate and the bar, because a class meets the bar only when its lower bound does (references/eval-statistics.md §3, `--size <expected> --bar <bar>`). About 139 cases read a rate near 90% within ±5 points; showing a 90% bar takes about 73 per class at an expected 95%, far more as the expected rate nears the bar, or a lower bar signed before the run. Never give a spike rate to model risk, a comex or a regulator as the system's accuracy.
11. **Optional: an acceptance brief for a coding agent** (`templates/acceptance-brief.md`): the question, the cases as input and expected-output files, the check per class, the bar, one command that prints n of N per class and cost per correct answer. Another session reviews the harness and smoke-tests three known cases.

## Output
A spike report following `templates/spike-report.md`: the items fixed before the build with date and signer, tool, data and size check, trifecta check, design, drift log, results per class with reading, cost per correct answer, hours, the decision, and what `build-evals` must do before any release claim. Optional: `templates/acceptance-brief.md`. Unfillable sections say what is missing and who provides it.

## Rules and red lines
- Never put production credentials, or production personal data, in a spike, whatever the deadline or "it's only a prototype". The tool must be authorised and registered, and even then the cases are synthetic, anonymised or pseudonymised; real data only under an approved, time-limited testing derogation reported to ICT risk.
- Never present a spike number as release, validation or go-live evidence, and never quote it as the system's accuracy.
- Never start the build before the question, appetite (a time box in days or one week, never open-ended weeks, and a cost ceiling), bar per class, case count per class and kill date are written down. Never move the bar or the appetite after seeing results; only the criteria for "correct" may be revised, and every revision is logged.
- Never call a class "meets the bar" on its point estimate when the interval's lower bound is under it.
- Never compute cost per answer where cost per correct answer is asked, and never treat a future price drop as a measured cost.
- Never extend past the kill date without a new appetite and a new signature.
- Never build an agent where a fixed workflow has not been tried first.
- Never leave all three legs of the lethal trifecta in a prototype that touches private or customer data.
- The spike never sets an autonomy level; it tests whether the model can serve at the level the PRD will propose (references/autonomy-ladder.md).

## Links
references/build-to-learn.md · references/eval-statistics.md · references/autonomy-ladder.md · references/roi-model.md · references/evals-as-evidence.md · ai-opportunity-assessment · llm-feature-prd · build-evals · model-selection · synthetic-eval-data · agent-design-and-tooling · prototype-handover · release-to-production

## Sources
- cagan-prototypes-products: the spike builds to learn, not to earn; a convincing prototype hides most of a product's work.
- singer-shape-up: the appetite fixed before the work, the circuit breaker as a kill date.
- kromer-learn-measure-build: the question first, then the measurement, then the smallest build.
- shankar-validators: criteria drift; criteria revised after reading outputs, and logged.
- wilson-interval: n of N with an interval per class; a high point on few cases is not a demonstrated rate.
- willison-lethal-trifecta: private data, untrusted content and an outbound channel never together.
- metr-ai-dev-productivity: hours and cost from logs, not perceived speed.
- anthropic-agents: workflow before agent.
- esma-qa-2103, dora-rts-ict-risk: user-built tools are ICT assets that must be authorised; non-production data rules (RTS art. 16(5), (6), (9)); terms an employee accepts can make a provider an ICT third party.
- dora: third-party risk and register for an account opened outside procurement.
- gdpr: processor terms for personal data sent to a provider.
- replit-db-incident: controls in code and permissions, not in the prompt.
- own-spikes: the five readings per class and the three-way decision, from feasibility spikes run before PRDs in banking and insurance.
