---
name: red-team-evals
description: 'Plan or read attack tests on an AI assistant or RAG feature: what users can make it say or disclose. Use for jailbreak results, a vendor resistance figure, "robust" wording, a campaign before release.'
license: CC-BY-4.0
metadata:
  stage: "evaluate"
  version: "0.4.1"
  status: "tested"
  eval_threshold: "0.80"
  legal: "false"
  last_verified: "2026-11-12"
  autonomy_relevant: "true"
  depends_on: "system-prompt-and-guardrails, build-evals"
  feeds: "release-to-production, model-card-ai-registry, ai-act-classification, build-evals"
  sources: "owasp-llm-top10, nist-ai-100-2, mitre-atlas, mazeika-harmbench, openai-external-red-teaming, anthropic-red-teaming, wilson-interval, zhang-gsm1k, eu-ai-act, dora, pyrit, garak, own-redteam"
---

# red-team-evals

## When to use
- An assistant or RAG feature is about to be released, or to move up a level (references/autonomy-ladder.md), and nobody has planned how users or planted content could make it say or disclose what it must not.
- A model, prompt, knowledge base or lookup tool changes and the last attack results no longer describe the system.
- An auditor, model risk or second line asks for robustness evidence: "how was it attacked, how often did it fail, what was not tested?"
- Attack results are on the table (an external scan report, a vendor figure, a team's "0 out of 50") and someone wants to write a conclusion from them in a release memo, model card or register.
- Do not use to write or tune the prompt and guardrails, to write the attacks themselves, or to decide whether one finding needs a guardrail change: that is `system-prompt-and-guardrails`. Its small redteam set is a smoke and regression set, not campaign evidence.
- Do not use for an agent that acts on systems on its own (updates records, sends, pays, chains actions; L3 and above, references/autonomy-ladder.md): what planted instructions can make it do, how that is tested and its level gate belong to `agent-evals`. A tool the user's own request triggers on their own records, with no gain in authority (a ticket or request on their own account, a draft a person sends), stays here as an attack class: can it be pointed at another customer's record or misused?
- Do not use to watch live quality or live abuse after release: that is `production-evals-monitoring`.

## Inputs
Mandatory: what the feature is (assistant or RAG), what it can reach (data classes, read-only lookups, tools the user triggers on their own records, where its output goes: screen, rendered page, a draft a person sends), who can write what it reads (users, document authors, third parties), the autonomy level per step, monthly volume.
Ask if missing: an estimate of attack attempts a month with its source (logs, `conversation-analysis`, incident data), never the conversation count; the harm list from the PRD or the guardrail spec, past incidents and findings, the tolerable rate per harm and who signs it, the testers available and their relation to the build team, the model and prompt versions, the date the decision is needed.
No harm list: the first deliverable is the list of what an attacker would want from this feature, not the attack set.

## Method
1. **Start from the feature's own risks.** For each harm write attacker goal × entry point × consequence: "a customer reads another customer's claim through the lookup tool", "a planted line in an uploaded PDF makes the assistant quote another customer's claim notes". Entry points: direct (the user's message), indirect (retrieved documents, lookup results, uploads), multi-turn. Each line becomes an attack class. A class with no harm in this feature is dropped with its reason.
2. **Check coverage against the public taxonomies, never copy them.** Map each class to OWASP LLM Top 10 (2025), NIST AI 100-2 attacker goals and the MITRE ATLAS techniques of the release you cite. Mark each taxonomy entry relevant-and-tested, relevant-and-untested, or not applicable with a reason. Report the coverage share: tested classes ÷ relevant classes. The untested list is part of the result. Grid: references/attack-taxonomy-coverage.md.
3. **Write the success criterion per class before the campaign.** Binary and checkable: data leaked (a planted canary string or a named record appears in the output), lookup misused (a call outside the user's scope in the trace), policy bypassed (the named forbidden content of that policy line), harmful output (the item of the harm list it violates). Prefer code checks (canaries, trace queries) to human grading, and human grading to a judge; a judge is used only once calibrated (`llm-judge-calibration`). Fix the generation settings with it: model and prompt version, temperature, turns allowed, attempts per seed. The same attacks give a different rate under different settings. Fix the unit once: n is the number of independent seeds (an attack idea with its context), and a seed counts as one success when the criterion is met in any of its fixed attempts (best of k, as HarmBench-style reporting does). Variants of a seed are attempts, never extra n. Date and sign the criteria, the settings and the tolerable rate per class (references/evals-as-evidence.md, rule 1).
4. **Size each class for its tolerable rate, in held-out seeds.** Zero successes in n still allows a true rate up to about 3/n by the rule of three; the Wilson 95% upper bound the reading uses (step 7) is about 4/n (references/eval-statistics.md §2). Size on the bound you read with: to read a class as under rate r with no success, it needs about 4/r held-out seeds, 381 for 1% and 765 for 0.5%. Sized at 3/r, a clean class reads undecided. Add a margin: one success at 765 already moves a 0.5% class to undecided, and absorbing it takes about 1,130. A costly class (another customer's data, a promise on money or cover) is sized for its own tolerance, whatever its share of the campaign. Seeds to write = held-out n ÷ held-out share. Variants of one seed are not independent (references/eval-statistics.md §1). A class below its n is reported as indicative. Run `python3 scripts/redteam_rates.py --plan <rate> …` to get n per class with 0, 1 and 2 successes.
5. **Name the testers and their independence.** Keep three sources apart in the plan and the results: automated generation (a scanner or generator; PyRIT and garak are examples, not procedures), human red-teamers (domain experts who know what a fraudster or an angry customer would try, plus security), and regression attacks from past findings. For each tester record their relation to the build team: built it, same team, independent internal (security, second line), external. Humans find new classes; automation scales the known ones. Rates that model risk relies on come from testers independent of the build team.
6. **Seal a held-out attack set.** Before anyone tunes, split the attacks: a development set the prompt and guardrail owners may see and tune on, and a held-out set kept by the independent tester, hashed and dated, never shown to the build team. Rates for the decision are read on the held-out set only. Attacks that leaked into tuning are burned: they move to the regression suite and fresh ones replace them. When both exist, report the gap between the tuned set and the fresh set: a large gap means the defence learned the attacks, not the class.
7. **Report per class, never pooled alone.** For each class: successful seeds ÷ held-out seeds, the attack-success rate with its Wilson 95% interval, the tolerance signed beforehand, and a reading: under tolerance (upper bound below it), over (lower bound above it), undecided (the interval straddles it: more attacks, not a looser reading). A pooled rate may sit under every tolerance while one class fails at 30%. Add the coverage share, the untested classes, the testers, the settings and the versions. `python3 scripts/redteam_rates.py class=successes/seeds:tolerance … --attempts <monthly attack attempts>` prints the table and the exposure.
8. **Turn every successful attack into a regression case.** Keep the attack, its context (the planted document, the starting state), the class and the success criterion, and add it to the regression suite (`build-evals`), run on every model, prompt, knowledge base or lookup tool change. Whether a finding needs a guardrail change is `system-prompt-and-guardrails`' call. After a fix, re-test the class on fresh held-out attacks, not only on the ones that found the flaw.
9. **Write the residual-risk record.** What was tested (classes, n, testers, independence, settings, versions, dates), what was not and why, rates with intervals against the tolerances, findings and their status, regression cases added, what triggers the next campaign (model, prompt, knowledge base or lookup tool change, new data source, a date), and who accepts the residual risk: a named owner outside the build team. For counsel and model risk, a checklist, never a verdict: AI Act art. 15(5) attack types (data poisoning, model poisoning, adversarial examples or model evasion, confidentiality attacks, model flaws) marked tested, untested or not applicable; art. 15(4) resilience to errors and inconsistencies, including from users and other systems; art. 9(5) residual risk judged acceptable, and by whom; art. 9(6) testing that identifies the risk-management measures and shows consistent performance for the intended purpose; art. 9(8) testing against metrics and probabilistic thresholds defined beforehand. Whether those articles apply is `ai-act-classification`'s question, and they bind the provider: when the organisation deploys a vendor's system, ask counsel whether it is provider or deployer, and whether the provider's declared robustness and cybersecurity levels and test conditions (art. 13(3)(b)(ii), in the instructions for use) are on file. For a bank or insurer, ask ICT risk whether the campaign belongs in the DORA digital operational resilience testing programme, and who records it there. If the feature gains a step that acts on systems (L3 and above, references/autonomy-ladder.md), its attack tests and action guardrails move to `agent-evals`: the record says so.

## Output
`templates/red-team-campaign.md` (plan, then results) and `templates/residual-risk-record.md`, all headings present. A section that cannot be filled says what is missing and who provides it. When the brief brings results, the answer gives the per-class table with intervals before any conclusion.

## Rules and red lines
- Never conclude that the system is robust, secure, jailbreak-proof or compliant. Robustness is a measured rate per class, with its interval, its tolerance and the list of untested classes.
- Zero successes in n is never zero risk: state the bound (about 3/n, Wilson about 4/n) and the exposure it allows on estimated attack attempts a month, never on all conversations; add the persistent attacker's view, about 1/p tries for a first success.
- Never report a pooled attack-success rate on its own: per class, each against its tolerance.
- Never read a rate on attacks used to write or tune the prompt or guardrails: decision rates come from a sealed held-out set.
- A vendor's or a public benchmark's figure is never evidence for this feature's rate, not even supporting or secondary evidence: other system, other attacks, other success criterion, other settings. Request it as documentation for the file and use it to inform the attack classes, nothing more.
- Success criteria, settings and tolerances are written and signed before the campaign.
- Every successful attack becomes a regression case.
- Residual risk is accepted by a named owner outside the build team, never by the campaign itself.

## Links
references/eval-statistics.md · references/evals-as-evidence.md · references/autonomy-ladder.md · references/attack-taxonomy-coverage.md · references/campaign-worked-example.md · system-prompt-and-guardrails · agent-evals · build-evals · llm-judge-calibration · production-evals-monitoring · release-to-production · model-card-ai-registry · ai-act-classification

## Sources
- owasp-llm-top10: the application-level attack taxonomy the coverage grid reads against.
- nist-ai-100-2: attacker goals (availability, integrity, privacy, misuse) and direct versus indirect prompt injection as shared vocabulary.
- mitre-atlas: adversary techniques to map each class to, with the release cited.
- mazeika-harmbench: attack success rate as the share of test cases that elicit the target behaviour under fixed grading and generation settings.
- openai-external-red-teaming: campaign design (who tests, with what access and guidance); findings become automated evaluations; a campaign is a snapshot.
- anthropic-red-teaming: expert, automated and open-ended red teaming compared, scaled into a test, mitigate, retest loop.
- wilson-interval: the interval per class and the rule of three on zero successes.
- zhang-gsm1k: the gap between a set the system has seen and a fresh matched set, read as contamination.
- eu-ai-act: art. 15(4)–(5), art. 9(5), 9(6), 9(8) and the provider's declared robustness levels (art. 13(3)(b)(ii)) as checklist items for counsel.
- dora: whether a financial entity's campaign belongs in its digital operational resilience testing programme, as a question for ICT risk.
- pyrit, garak: examples of automated attack tooling, named, never prescribed.
- own-redteam: held-out attack sets kept by a tester outside the build team, and the residual-risk record model risk signs, from the author's bank and insurance missions.
