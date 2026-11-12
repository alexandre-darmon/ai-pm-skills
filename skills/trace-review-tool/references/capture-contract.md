# Minimum capture contract per model call

What the system under review must log on every model call, so a domain expert can judge a trace and the bank can answer an auditor. Engineers build the pipeline and its retention store; the PM signs this list. Field names follow the OpenTelemetry GenAI semantic conventions where one exists (`otel-genai`, Development status: pin the version you follow); this list is the minimum a review needs; `production-evals-monitoring` instruments the same fields in production and sets their live retention, and `agent-design-and-tooling` adds the agent's own step schema.

## Fields

| Field | Why the review needs it | What breaks without it |
| --- | --- | --- |
| `trace_id`, `span_id`, timestamp | One trace per screen, ordered steps | Labels cannot be joined back to what happened |
| Prompt name and version (or hash) | A failure mode is attributed to the prompt that produced it | After a prompt change, nobody knows which labels still hold |
| Model asked, model that answered, provider version | Same reason for model and provider updates | A silent provider update looks like a quality drift |
| Retrieved document ids (and version of the knowledge base) | The expert sees what the model was given; retrieval failures are told apart from generation failures | Every wrong answer looks like a model error |
| Tool calls: name, arguments, result status, error | The first failing step of a multi-step trace | Agent failures cannot be located |
| Guardrail hits: which rule, block or rewrite | Over-blocking and missed blocks are both visible | The guardrail's false-positive rate stays unknown |
| Human overrides: who, when, what changed, reason code | Evidence that the human in the loop acts (L2, L3) | An override rate of zero cannot be told from a log that never captured it |
| Input and output tokens, cost in EUR | Cost per run and cost per correct answer (references/roi-model.md) | Economics rest on invoices, not on outcomes |
| Latency | Long or abandoned interactions as a targeted stratum | One sampling stream fewer |
| Join key to the business outcome (case, claim, loan, complaint id) | Labels joined to what happened next (upheld complaint, reopened claim) | Quality never meets the KPI or the ROI |
| Question class, if a classifier runs (`conversation-analysis`) | Per-class rates and stratified samples | One global rate hides the risky class |

Message content (inputs, outputs, retrieved text) is captured only where masking and access rules are in place. Personal data is masked with typed, consistent placeholders before any export leaves the logging store.

## Retention: questions for counsel and the DPO

Verified against Regulation (EU) 2024/1689, as amended by Regulation (EU) 2026/1744 (`eu-digital-omnibus-ai`), on 2026-11-11. These are questions, not answers.

- **Is the system high-risk** (annex III, e.g. creditworthiness of natural persons)? Ask `ai-act-classification`. Art. 12 asks high-risk systems to allow automatic recording of events over their lifetime, enough to spot risks and substantial modifications, support post-market monitoring and the deployer's monitoring.
- **From which date?** Annex III high-risk duties, arts. 12, 19 and 26 included, apply from 2 December 2027 (`eu-digital-omnibus-ai`). From which date must the bank meet the six-month floor, and must logs created now already satisfy it if the system is still running on that date?
- **Provider, deployer or both?** Art. 19 has providers keep the automatically generated logs under their control for a period fit for the intended purpose, at least six months unless other Union or national law (data protection in particular) says otherwise. Art. 26(6) sets the same floor for deployers. An in-house build for the bank's own use may make the bank both: flag it to `prototype-handover`.
- **Financial institutions.** Both articles let a financial institution subject to internal-governance rules under Union financial-services law keep these logs as part of the documentation that law already requires. Which documentation, which retention, which owner?
- **GDPR and the floor.** The six-month floor applies unless other Union or national law, in particular data protection law, provides otherwise; storage limitation and minimisation (GDPR art. 5(1)(c), (e)) are part of that law. Masked traces are pseudonymised, so still personal data. Which period wins for raw content, for masked traces, for labels and critiques?
- **Do review labels count as logs?** Labels with reviewer and timestamp document human oversight. Are they kept with the logs, for the same period?
- **Who may read raw traces**, and is that access itself logged?

If the system is not high-risk, the articles above do not apply as such; the bank's own record-keeping, DORA ICT rules and GDPR still set the period.
