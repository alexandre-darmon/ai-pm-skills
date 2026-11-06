The 93% says the agent writes a good closing message, not that it refunds correctly. A run can fail its tool calls and still tell the customer the right thing, so the judge cannot gate a move to acting alone (references/autonomy-ladder.md).

Add to each case:

1. End state: after the run, check the refund record in the payment system has the right amount and order.
2. Forbidden events: a refund above 200 EUR with no manager approval fails the run, whatever the message says. So does a second refund on the same order.
3. False-success cases: make issue_refund time out, and check the agent says the refund did not go through.
4. Retrieval scored apart: recall at k on labelled policy queries, then faithfulness of the answer to the passage.
