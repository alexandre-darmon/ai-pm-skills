# Tool contracts

Loaded when step 3 or step 5 of the method needs detail. A tool's description is what the model picks from, so treat it as product text. Anything left on the tool list should be assumed to get called some day.

## What a description states

| Item | Why it matters | Weak | Strong |
| --- | --- | --- | --- |
| Purpose | The model matches it against the request | "Handles invoices" | "Returns one invoice by its number, from the ERP" |
| When to use it over its nearest neighbour | Cheapest fix for wrong tool picks | Silent on the neighbour | "Issued invoices only; for drafts use `find_draft`" |
| Inputs | Vague names get invented values | `id` as free text | `invoice_number`, format with an example, enums for fixed values |
| What comes back | The model must read an empty result correctly | Nothing said | "An empty list means no invoice matches" |

Read wrong tool picks in the traces and fix the description first, before any change of loop or model.

## Constrained over generic

A generic tool (`run_sql`, `fetch_url`) lets the model do whatever the wording suggests, and every misuse becomes a filter to write. Prefer named, parameterised tools (`invoices_by_customer(customer_id, period)`). Split a tool in two where one half needs approval (step 5).

## Error contract

An error returned to the model carries:

- category: transient, invalid input, business rule, permission;
- whether a retry can help;
- a plain message saying what to do next;
- any partial results.

Return an empty result and a failed lookup differently. Merged into one "nothing found", an ERP outage becomes a confident "this invoice does not exist".

## Risk by effect

Rate what the tool does: a `get_` name can hide a write. The rating sets the tool's line in the permission matrix. A working connection says nothing about whether this user may take this action. The tool takes the customer or tenant from the authenticated session or the case record and checks the target belongs to it; a `customer_id` the model read from a message or document is a search hint, never the access key.

## Test on real tasks

Give the agent real tasks and read the traces: which tool it chose, what it passed, which calls it repeated. Measure selection accuracy per tool. Editing a description is a release: `build-evals` covers it as it covers a prompt edit.

## What each write rule prevents

| Rule (step 5) | Failure without it |
| --- | --- |
| Prepare apart from commit | The model reaches an effect through a call it can make freely |
| Approval bound to action, target and payload, with expiry | An amount changed after approval executes, or an old approval is replayed |
| Cap on resulting state, in the system of record | Two requests under the cap add up to more than the cap, across sessions and channels |
| Idempotency key, no blind retry | A retry pays twice |
| Timeout on a write means unknown | The agent reports a failure, retries, and the first attempt had succeeded |

Log the attempted write first and its result once known, so an unknown result has something to reconcile against.
