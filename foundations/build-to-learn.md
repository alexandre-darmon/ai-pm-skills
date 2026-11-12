# Build to learn

The frame every Build skill shares. Last verified: 2026-11-11.

A PM with a coding agent can now build in an afternoon what took a team weeks. In a bank or an insurer that speed is useful only if everyone agrees on what the thing is for. Cagan draws the line: discovery builds to learn, delivery builds to earn (`cagan-prototypes-products`). A PM-built artefact sits on the learning side, and it stays there.

## What a PM-built artefact is for

| It is | It is not |
| --- | --- |
| Evidence: an answer to one question, with n of N per class, an interval and a cost per correct answer (references/eval-statistics.md) | Production code, however clean it looks |
| A handover: the cases, the bar, the prompts, the trace fields and the eval suite that engineers rebuild against | A system that real customers, real money or real personal data flow through |
| Thrown away, or registered at its end-user computing tier, on a date set in advance | Kept running because nobody switched it off |

A good-looking prototype hides the distance to a product: authorisation, reliability, logging, security and change control are most of the work, and none of it shows in a demo (`cagan-prototypes-products`). The handover is what turns that distance into a list engineering can price.

## Who does what

| Role | Owns |
| --- | --- |
| **You**, the PM | The question, the cases, the bar, the trace fields and the thresholds, written down and signed before the run |
| **The coding agent** | The spike, the review app and the scripts. A fresh session or another model reviews what it wrote, never the session that wrote it |
| **AI engineers** | Everything production: integration with core systems, authentication and authorisation, secrets, environments, CI/CD, guardrails enforced in code, the logging pipeline and its retention, security testing, hosting and the model gateway, on-call |

A bank that lets traders build tools in hours still puts senior developers between those tools and live trading (`bloomberg-ing-vibe-coding`). The split above is that supervision layer, written in advance.

## Before the first run

Plan the loop in reverse: decide what must be true and how you will measure it, then build the smallest thing that measures it (`kromer-learn-measure-build`). Three items are written, dated and signed before anything runs (references/evals-as-evidence.md, rule 1).

1. **The appetite.** A time box (days, not weeks) and a maximum cost per correct answer. The appetite is what the question is worth, not an estimate of the work (`singer-shape-up`).
2. **The bar.** The pass rate per question class, and the error that is never acceptable, set by the people who own the business risk.
3. **The kill date.** If the spike has not answered its question by then, it stops by default. Extending it is a new decision with a new appetite, never a drift (`singer-shape-up`, circuit breaker).

A spike that starts without these three only produces a demo, and a demo persuades without proving anything.

## Red lines for anything a PM builds

1. **No production credentials and no private or customer data** in a tool that is not authorised and registered as an ICT asset. Under DORA, end-user tools and systems built outside the ICT function are ICT assets, and the development and testing rules apply to them on a risk basis (`esma-qa-2103`, `dora-rts-ict-risk`). Production data stays out of non-production environments (RTS art. 16(5)–(6)). Use synthetic or anonymised cases until IT risk has answered the asset question and the DPO the data question.
2. **Controls enforced in code, not asked in a prompt.** An instruction such as "change nothing without approval" is a wish. A coding agent told exactly that has wiped a live database (`replit-db-incident`). Read-only credentials, a separate environment and an approval step outside the model are controls; a sentence in the prompt is not.
3. **The lethal trifecta check** before any prototype touches private or customer data. If one agent has access to private data, reads untrusted content (emails, web pages, uploaded files, tool outputs) and can send data out, an attacker can make it leak that data (`willison-lethal-trifecta`). Remove one of the three, in code, or stop.
4. **A spike number is never release evidence.** It was measured on a small set, on a throwaway harness, with criteria you were still refining (`shankar-validators`). It decides whether to invest further. Release evidence comes from the frozen suite run on the engineering build (`release-to-production`).
5. **Measure time and cost per correct output, not perceived speed.** Experienced developers using AI tools felt about 20% faster while taking 19% longer on their tasks (`metr-ai-dev-productivity`). Report hours spent and cost per correct answer from the logs, never the team's impression.
6. **Review by a fresh session or another model.** The session that wrote the code shares its blind spots. Every script and every review app gets a review it did not write, and a smoke test on known cases.

## Where it goes next

The Build block ends with a decision, not a deployment. `prototype-handover` decides what the artefact becomes: rebuilt by engineering against its eval suite, registered at its end-user computing tier (`aws-euc-tiers`), or retired on its kill date. It lists what engineering must rebuild and the questions for IT risk, model risk and counsel. Then `release-to-production` accepts the engineering build against the scenarios declared before it was written, and gates it with the frozen suite. Autonomy levels in either step are cited from references/autonomy-ladder.md, never set by the prototype.

## What this frame is not

- Not a coding guide. Tools and platforms change in months; the roles, the appetite and the red lines do not.
- Not a licence to skip IT risk. A prototype that answers its question still enters the bank through the same door as any other system.
