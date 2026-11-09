# Process redesign: complaint handling (6,000/month, email and letter)

**Verdict on "fully automated by 2027":** I can't recommend it for all four steps. Sorting, routing and file-gathering can reach high autonomy by 2027. The founded/unfounded and compensation decision, and the reply that communicates it, should stay at L2. That means AI proposes and a person validates each one. These decisions have a financial effect on customers. Under the red lines I apply, they stay at L2 at most. Your sector may also bring GDPR art. 22 (solely automated decisions) and possibly AI Act high-risk duties. The DPO and counsel need to confirm both. Here, "fully automated" really means "every complaint is pre-decided and drafted by AI, and a person validates it in minutes".

## Current process

I only have the steps and the volume. I don't have time per step, exception rate or current cost, so I've left them as items to measure rather than invent them.

| Step | Volume/month | Time per item | Exception rate |
| --- | --- | --- | --- |
| Sort and route | 6,000 | to measure | to measure (misroutes, multi-topic complaints) |
| Gather the file | 6,000 | to measure | to measure (missing records, scanned letters) |
| Decide founded and compensation | 6,000 | to measure | to measure (escalations, legal threats) |
| Write the reply | 6,000 | to measure | to measure |

Letters add a scanning and OCR step that the process doesn't list. Measure the share of letters, because OCR quality caps everything downstream.

**Measure first.** Before any step goes above L2, run a 4-week baseline. Take a sample of about 300 complaints and have the team label routing, outcome and compensation. This gives you time per item, the exception rate, the founded rate and the current cost. It also becomes the golden set for evals. If exceptions turn out to exceed about 25%, redesign exception handling before raising any level.

## Step table

| Step | Current level | Target level (end 2027) | Why not L+1 | Gate to reach target | Approach |
| --- | --- | --- | --- | --- | --- |
| Intake and OCR (letters) | L0 | L3 | Bad scans and handwriting cause silent errors | Shadow run ≥2 weeks. Character and field accuracy on the golden set ≥ threshold. Low-confidence items escalate, and that path is tested. | Workflow (OCR plus extraction) |
| Sort and route | L0 | L4 | L5 is excluded: a process with exceptions can't be self-improving without oversight | Eval ≥ threshold on golden set (`build-evals`). Shadow run ≥2 weeks. Guardrail false-positive rate known. Canary passed. One-click rollback (`release-to-production`). | Rules for obvious categories, LLM classifier for the rest |
| Gather the file | L0 | L3 | Read-only retrieval is low risk, but a wrong or missing document feeds the decision | Retrieval recall on golden set ≥ threshold. Shadow run ≥2 weeks. Missing-document escalation tested. | RAG and workflow over CRM, contracts and history. No agent needed. |
| Decide founded and compensation | L0 | **L2** | Legal and financial effect on a person. Above L2 is not allowed. | L1 first: offline eval on golden set (agreement with senior handlers ≥ threshold, with compensation error bounded). L1 in production 4 weeks, quality KPI stable, output guardrails tested. | Rules for the compensation scale and caps, LLM to assess against the file, with cited evidence |
| Write the reply | L0 | L2 | The reply communicates the decision and carries commitments. At most L3 for unfounded complaints without compensation, after a measured error record. | Same as the decision step. Tone, policy and factual-accuracy evals on golden set. | LLM with templates and policy RAG |

I treat compensation as a rule-bounded output. A fixed scale and caps do the arithmetic, and the model only classifies facts. That makes the 180 EUR average auditable.

## Scenarios

All three scenarios use the five ROI lines. The figures marked "to measure" come from the baseline. Until then, this is a projection with no baseline, and I'm not showing any savings number.

| Line | Conservative | Target | Ambitious |
| --- | --- | --- | --- |
| Scope | Routing L3, file L2, decision and reply L1 | Routing L4, file L3, decision and reply L2 | As target, plus reply L3 for unfounded, no-compensation cases |
| Volume | 6,000 × share handled by AI | same | same |
| Quality | Share correct on routing, file, decision, reply (sampled eval) | same | same |
| Unit value | Minutes saved per complaint × loaded cost, to measure | same | same |
| Run cost | Tokens, OCR, infra, eval upkeep, monitoring | same | same |
| Change cost | Build spread over a stated period, training, reviewer hours | Higher: more reviewer hours at L2 | Highest: adds sampling at L3 |

**Compensation exposure, not a saving.** If an average of 180 EUR applies to every complaint, the flow is up to about 1.08M EUR a month. The real figure depends on the founded rate. A 5% drift in decisions in either direction is therefore a larger line than most of the labour saving. Quality on the decision step needs to be measured on money as well as on accept/refuse agreement.

**Human fallback, sized:**
- Review items per month = (decisions and replies at L2 = 6,000) + (routing, file and OCR exceptions) + (sample at L3).
- Reviewer hours = items × time per validation, to measure.
- Compare with the hours the team has left after the redesign.
- Queue owner: head of complaints (to confirm). SLA: to set from regulatory reply deadlines. Timeout: the complaint goes to a senior handler, never to auto-approval.

If the team can't staff the review, lower the level or the volume. Don't count the fallback as available.

## Trade-offs

| | Cost per outcome | Risk | Reversibility | Obligations |
| --- | --- | --- | --- | --- |
| Conservative | Highest, small saving | Low | Full | Transparency, logging |
| Target | Lower. Cost per correct outcome, with reviewer time in the numerator. | Medium: wrong compensation caught at validation | Full: demote any step | DPIA, DPO, CSE consultation (work changes), AI Act check |
| Ambitious | Lowest on paper | Higher: unfounded rulings sent without human check | Partial: sent replies can't be recalled | As target, plus the L3 sampling plan and incident playbook |
| "Fully automated" (not offered) | Nominally lowest | High: unreviewed financial and legal decisions | Poor | Likely GDPR art. 22 exposure. Needs counsel. |

I recommend the **target** scenario.

## Migration path and gates

One level at a time, each move behind its gate. Nothing skips a level in production.

| Step | Demotion trigger (observed value) | Who acts |
| --- | --- | --- |
| Intake and OCR | Field accuracy on weekly sample falls below the gate threshold, or after any OCR/model change | Operations lead |
| Sort and route | Misroute rate above threshold in the weekly sample, or reroute requests rise | Head of complaints |
| Gather the file | Missing or wrong document found in more than the threshold share of sampled files | Head of complaints, data owner |
| Decide founded and compensation | Validator override rate above threshold, or any compensation outside the scale | Head of complaints, legal |
| Write the reply | Rewrite rate above threshold, or any complaint about tone or factual error | Head of complaints |

All thresholds come from the baseline and the golden set. Moving down needs no approval. The rollback mechanism belongs to `release-to-production`.

## Dependencies

- **`ai-act-classification`:** required for the routing step (L4), and I'd run it on the whole process too. Whether the decision step falls under a high-risk category depends on your sector. For example, complaints about credit, insurance or access to essential services can. I don't know your sector, so this is open.
- **DPO:** DPIA for personal data, and the art. 22 position on automated decisions.
- **HR and employee representatives:** the work of complaint handlers changes from drafting to validating. Workers' representatives must be informed before use (AI Act art. 26(7)). In France the CSE is informed and consulted.
- **Legal:** regulatory reply deadlines, and any duty to explain a decision to the customer.
- **Letters:** a scanning and OCR pipeline with a retention policy.

## Plan and milestones

| When | Milestone | Owner |
| --- | --- | --- |
| Q4 2026 | 4-week baseline, golden set of ~300 labelled complaints, exception rate. **Decision point: continue, redesign exceptions, or stop.** | Head of complaints, data lead |
| Q4 2026 | AI Act classification, DPO and counsel opinion, HR and CSE informed | Legal, DPO, HR |
| Q1 2027 | Routing and OCR at L1, then shadow run. File gathering at L1. | Product, ops |
| Q1–Q2 2027 | Decision and reply at L1, then 4 weeks in production with KPI stable | Product, complaints |
| Q2–Q3 2027 | Routing to L3 then L4 after canary. File gathering to L3. Decision and reply to L2. | Product, ops |
| Q3 2027 | Reviewer staffing confirmed against measured hours | Head of complaints |
| Q4 2027 | Review of results and decision on the ambitious scenario | Board sponsor |

**What to tell the board:** by end 2027, every complaint is sorted, routed, filed, assessed and drafted by AI. People validate the decisions and replies, and they handle the exceptions. Full removal of human validation on compensation is not on the plan. The risk and the legal exposure don't justify it.

**What I need from you:** time per step, the current cost of the process, the share of letters, your sector (for the AI Act check), and the size of the team.