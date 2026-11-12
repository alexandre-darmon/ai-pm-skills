## 1. What engineering must log on every model call

| Field | Why |
| --- | --- |
| trace id, span id, timestamp | one application = one trace |
| prompt and model version | ties a failure to the prompt that produced it |
| model asked, model that answered, provider version | silent provider updates show up |
| retrieved transaction ids and the statement period | the analyst sees what the model was given |
| tool calls to the scoring engine: arguments, result status, errors | locates the failing step |
| guardrail hits: which rule fired, block or rewrite | over-blocking becomes visible |
| analyst overrides: who changed what in the summary, reason code | evidence the human in the loop acts |
| input and output tokens, cost in EUR | cost per run and per correct summary |
| join key: the loan application id | joins each trace to the credit decision and later defaults |

## 2. The 30 days, as questions for counsel

I cannot tell the committee whether 30 days is enough; this is for counsel and the DPO. Creditworthiness assessment of natural persons is listed in annex III, so the system may be high-risk. If it is:

- art. 12 asks for automatic logging over the system's lifetime;
- art. 19 has providers keep the logs under their control at least six months, and art. 26(6) sets the same floor for deployers, unless other Union or national law, in particular data protection law, provides otherwise;
- both let a financial institution keep the logs within the documentation required by financial services law: which documentation, which owner?
- annex III duties apply from 2 December 2027 under the Digital Omnibus: from which date does the floor bind, and must logs created now meet it if the assistant still runs then?

Questions: is the system high-risk? Is the bank provider, deployer or both for an in-house build? Does GDPR minimisation justify less than the six-month floor, or the reverse? Do analysts' review labels count as logs?
