# Evals as evidence

The frame every skill in this repo shares. Last verified: 2026-11-09.

In a regulated company an eval is not a best practice. It is the evidence three readers are owed, and each reader asks a different question.

| Reader | Question | Evidence that answers it | Skills |
| --- | --- | --- | --- |
| The user, and the team that serves them | Does it give correct answers on the questions people really ask? | Failure modes read on real outputs; scores per question class, with their interval; online quality on sampled production traces | `error-analysis`, `build-evals`, `conversation-analysis`, `production-evals-monitoring` |
| The sponsor | What does one correct answer cost, and is it worth it? | Cost per correct outcome, before and after; ROI from volume × quality × unit value | `assistant-kpis-cost-per-outcome`, `ai-roi-quantification`, `model-selection` |
| The regulator, the auditor, counsel | Were the bars set before the test? Are the test data representative? Is performance watched after release? | Dated, signed thresholds; set composition; eval record per version; monitoring plan; incident log | `ai-act-classification`, `model-card-ai-registry`, `production-evals-monitoring`, `ai-incident-playbook` |

## Three blocks

1. **Specify** what correct means before anything is built: question classes, the costliest error, red lines, the autonomy level of each step (references/autonomy-ladder.md).
2. **Evaluate** offline and online: golden set, graders, a judge validated against expert labels, intervals, then the same checks on sampled production traffic.
3. **Prove** to the sponsor and the regulator: cost per correct outcome, the eval record of each version, the monitoring plan and the incidents.

## Six rules that turn a score into evidence

1. **Decided before seen.** Criteria, thresholds and the choice of judge are written, dated and signed before the run they judge. A bar drawn after the scores only describes them.
2. **Measured with its uncertainty.** Every score carries its number of cases and its interval (references/eval-statistics.md). A gap inside the noise is a tie.
3. **Traceable.** Every result names the system version (model, prompt, knowledge base), the judge and its version, the set version, the harness and the date.
4. **Per class, never only global.** A large easy class must not hide a failing risky one.
5. **Kept when unfavourable.** A failed run, a moved threshold or a grader found wrong stays on record, with who decided and why.
6. **Checklist, not verdict.** Evidence feeds counsel and the sponsor. No skill states that a system is compliant, safe or good enough to ship on its own authority.

## AI Act: which eval evidence answers which article

For high-risk systems, the AI Act turns several eval habits into duties. Article numbers refer to Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744. The obligations for annex III systems apply from 2 December 2027, those for annex I systems from 2 August 2028. Outside high risk, the same evidence is good practice and is what a sponsor or an auditor will ask for anyway.

| Article | What it asks, in short | Eval evidence that answers it | Who owes it |
| --- | --- | --- | --- |
| 9(6)–(8) | Testing before release against metrics and probabilistic thresholds defined in advance | Thresholds per class signed before the run, scores with intervals, baseline | Provider |
| 10(3)–(4) | Test data that are relevant, representative, as complete and error-free as possible, fit for the setting of use | Set composition per class and risk, real and synthetic share stated, holdout kept private | Provider |
| 15(1)–(3) | Appropriate accuracy and robustness, accuracy metrics declared in the instructions for use | The eval record published with the instructions: metrics, levels, classes, limits; robustness and attack tests | Provider |
| 17(1)(d) | Test and validation procedures before, during and after development, with their frequency | The eval plan versioned inside the quality system (EN 18286 gives the structure) | Provider |
| 26(5) | Monitor operation per the instructions, inform the provider, suspend use on risk | Online evals on sampled traffic, alert thresholds, a named person who can suspend | Deployer |
| 72 | A documented post-market monitoring system that actively collects performance data over the system's lifetime, based on a plan in the technical documentation | The production monitoring plan: what is sampled, judged, alerted, fed back; the Commission template for the plan is still expected | Provider |
| 73 | Report serious incidents within fixed deadlines | Incident classes, the log, and the regression case each incident adds | Provider, deployer informs |

Whether this evidence is enough is counsel's call, never the skill's.

## What this frame is not

- Not a tool. The method works with `claude plugin eval`, Inspect, Promptfoo or a spreadsheet.
- Not a substitute for domain experts. Labels, rubrics and thresholds come from the people who own the business risk.
