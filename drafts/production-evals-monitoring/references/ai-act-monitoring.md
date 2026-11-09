# AI Act: what the monitoring plan answers

Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744 (Digital Omnibus on AI, in force 27 July 2026). Checked on the EUR-Lex consolidated text of 27 July 2026 (CELEX 02024R1689-20260727) on the skill's `last_verified` date. Own summary, not the text: counsel reads the articles. Role and category come from `ai-act-classification`.

## Provider of a high-risk system

| Article | What it asks, in short | Plan section that answers | Evidence status | Question for counsel |
| --- | --- | --- | --- | --- |
| 72(1) | A documented post-market monitoring system, proportionate to the technology and its risks | The whole plan, versioned, with an owner | on file · draft · missing | Is the sampling depth proportionate to the risk of each class? |
| 72(2) | Active, systematic collection, documentation and analysis of performance data over the system's lifetime, including data deployers provide, to evaluate continued compliance with Chapter III Section 2; interaction with other AI systems where relevant | Evaluator tiers, sample sizes, per-class metrics and limits, deployer data feed, review cadence; tool and upstream-model calls in the traces | | What must deployers send, under which contract and data protection role? |
| 72(3) | The system rests on a plan that is part of the technical documentation (Annex IV); Commission guidance with a template due by 2 September 2027 | The plan filed in the technical documentation | | Re-map the plan when the template is published |
| 72(4) | Integration into existing monitoring for Annex I Section A products, and for Annex III point 5 systems of financial institutions | — | | Does the integration route apply here? |
| 9(2)(c) | Risk management uses data from post-market monitoring | Feedback loop to the risk register | | |
| 12(2) | Logs record events relevant to risks, substantial modifications, post-market monitoring and deployer monitoring | Instrumentation (references/otel-genai-fields.md) | | Are the logged fields enough? |
| 17(1)(d), (h) | Test and validation procedures before, during and after development, with their frequency; the monitoring system inside the quality management system | Review cadence; the plan as a quality-system procedure (EN 18286 gives the structure) | | |
| 43(4) | A substantial modification needs a new conformity assessment; changes the provider pre-determined in the technical documentation (Annex IV point 2(f)) do not count | Drift watch: model, embedding and judge changes treated as releases | | Is a provider model update a substantial modification? Which updates are pre-determined? |
| 73 | Serious incidents reported: immediately once a causal link is established or reasonably likely, at the latest 15 days after awareness; 2 days for a widespread infringement or critical-infrastructure disruption; 10 days for a death | Feedback loop to `ai-incident-playbook` | | Does a discriminatory output pattern count as a fundamental-rights infringement (art. 3(49)(c))? |

## Deployer of a high-risk system

| Article | What it asks, in short | Plan section that answers | Evidence status | Question for counsel |
| --- | --- | --- | --- | --- |
| 26(5), first sentence | Monitor operation on the basis of the instructions for use; where relevant, inform the provider (art. 72) | Metrics taken from the instructions for use (accuracy metrics declared under art. 15(3)); channel to the provider | | Do the instructions say what to monitor? |
| 26(5), risk | Reason to think use per the instructions presents a risk (art. 79(1)): inform the provider or distributor and the market surveillance authority without undue delay, and suspend use | Action ladder: the named person who can suspend | | Which alert levels mean "risk" in this sense? |
| 26(5), serious incident | Inform the provider first, then importer or distributor and the authorities | `ai-incident-playbook` | | |
| 26(5), last subparagraph | Financial institutions: the monitoring duty is deemed met by complying with internal-governance rules of EU financial-services law | Link to the bank's existing model-risk or ICT governance | | Does the deemed-compliance route cover this system? |
| 26(6) | Keep the logs under the deployer's control at least six months, unless EU or national law (e.g. GDPR) says otherwise; financial institutions keep them in their financial-services documentation | Privacy: retention | | How does this square with the GDPR retention set by the DPO? |

## Dates

- Chapter III Sections 1–3 (arts. 6–27) apply to Annex III systems from 2 December 2027 and to Annex I systems from 2 August 2028 (art. 113(c) as amended).
- Arts. 72–73 sit in Chapter IX, which art. 113 does not date separately: when they bite for a system whose Chapter III duties start later is a question for counsel.
- Art. 111(2): high-risk systems placed on the market before the Chapter III date are covered only if their design changes significantly afterwards. Whether a model swap is such a change is a question for counsel.

## Evidence status

Record paper, not conformity: on file (link), draft, missing, not applicable (with the reason). The plan never states that it meets or complies with an article; it ends with "This plan is evidence for counsel, not a conformity assessment."
