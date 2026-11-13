# Invoice-dispute flow: design

**Recommendation: don't build three cooperating agents. Build one fixed pipeline with three steps, and let only the steps that need judgment call a model.** The steps always run in the same order, so nothing in the flow needs an agent to decide what happens next. Multi-agent needs a written justification for what a single loop can't do, and I can't find one here. A fixed pipeline is also easier to test, trace and cost than agents that hand work to each other.

I don't have your L-levels, failure modes or latency and cost limits. Everything marked *(assumption)* below needs confirming.

## Trigger and done state
- **Trigger:** a dispute arrives (email, form or ticket). Dedupe on the dispute or ticket ID so repeated signals don't start two runs.
- **Done:** a draft reply is attached to the case for the human agent, with the evidence it used. Nothing is sent to the customer.
- **Exits:**
  - `draft_ready`
  - `needs_human`: the dispute is unreadable, the invoice isn't found or is ambiguous, or the dispute looks out of scope.
  - `error`: the ERP is down or a step failed.
  - `budget_exhausted`
  - `policy_denied`

  Every exit except `draft_ready` goes to a human queue with the reason. None fails silently.

## Loop type
`Loop type: plan-execute` (a fixed sequence, no planner)

| Step | Model? | What it does | Output |
|---|---|---|---|
| 1. Read dispute | Yes, one call with structured output | Extracts the claimed invoice number, disputed amount, reason category, requested outcome and the customer's tone | A typed `DisputeSummary`. Missing fields are `null`, never guessed. |
| 2. ERP lookup | Mostly code | Looks up the invoice using the case's customer ID, then compares the extracted facts against ERP data | An `InvoiceFacts` record, or `not_found` / `mismatch` |
| 3. Draft reply | Yes, one call | Writes the reply from `DisputeSummary` and `InvoiceFacts` only | A draft plus the list of facts it cites |

Between steps, plain code validates the handoff. If step 1 returns no invoice reference, the run exits to `needs_human` and step 2 never runs. If you later find a step that needs to retry or branch on its own, give that step a small tool loop. Don't make it a separate agent.

**Why not three agents:** the order is fixed, each step's input and output are known, and the steps share one case record. Separate agents would add handoff and failure points and make traces harder to read. They would also make prompt injection easier, because dispute text would pass through more model hops. I'd revisit this only if the steps need different models or permissions, or if different teams own and release them separately.

## Tools and permissions
| Tool | Effect | Reversible | Level / approval |
|---|---|---|---|
| `get_invoice(invoice_number)` | Read-only ERP query | n/a | Automatic |
| `get_invoice_payments(invoice_number)` | Read-only | n/a | Automatic |
| `attach_draft_to_case(case_id, draft)` | Writes a draft to the case | Yes, it can be overwritten | Automatic, draft status only |

- **No tool sends email, issues credits or changes invoices.** A human agent reviews and sends. That keeps this at read-and-draft only.
- **Data scope comes from the trusted case record, not from the model.** The tool takes the customer ID from the session or case and enforces it inside the tool. The invoice number the model extracted from the dispute only selects within that customer's invoices. If it isn't theirs, the result is `not_found`, not another customer's data.
- **Empty versus failed:** `not_found` and `erp_error` are different results, because they lead to different exits.
- Credits, refunds and write-offs are out of scope. If you add them later they need their own protocol: prepare separate from commit, approval bound to the exact payload, a cap, and idempotency keys.

## Drafting rules
- Every figure and date in the draft must come from `InvoiceFacts`. A code check confirms each cited number appears in the facts, and a draft that fails goes to `needs_human`.
- The draft states only what the ERP supports. It makes no promises of credit, refunds or deadlines, because those are the agent's decision.
- The dispute text is untrusted input. It is passed as data, and instructions inside it are ignored.

## Stop conditions *(all values are assumptions to confirm)*
- Maximum 3 model calls per run, plus 1 retry on a schema failure.
- 60 seconds total timeout. The owner is support engineering.
- A cost cap per run, set by the product owner.
- Hitting any limit exits to `needs_human` with an alert.
- The run ends on the done state, never on the model saying it's finished.

## Memory
Nothing persists between runs except the case record. Dispute text and invoice data are personal data, so they aren't kept in prompts or logs beyond the case.

## Trace schema
Log one record per step and tool call:
- run ID, case ID, step, tool, input (as record IDs, not raw text), output status, tokens, cost and latency
- a final `outcome` field set from the exit
- later, whether the human agent sent the draft as written, edited it or discarded it

The last item gives you the quality signal and cost per resolved dispute.

## Prototype check
Not yet run. Before engineering starts, build the two ERP read tools on a local MCP server with synthetic invoices and run about 10 realistic disputes through it. Include a wrong invoice number, another customer's invoice, a dispute with no invoice number, an ERP timeout, and a dispute containing an injection attempt. Read the traces and fix tool descriptions and response sizes before you tune prompts.

## Frameworks
Use none for now: the raw sequence of three functions meets every need above. I'd consider one only if you need durable pauses for approval or visual run inspection, and I'd pick it then.

## What I need from you
1. Is draft-only the intended autonomy level, or should some disputes (for example, small amounts) get automatic replies later?
2. How large is the volume and what is the latency target?
3. Which ERP is it, and does it have a read API scoped per customer?
4. What do you want to happen when the invoice is not found?