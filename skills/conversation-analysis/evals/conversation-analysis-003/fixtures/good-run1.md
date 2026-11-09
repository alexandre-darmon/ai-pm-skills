# Classification plan: banking assistant (45,000 conversations)

## 0. First: these exports contain personal data
The 3 samples include names, a customer id, an email, a phone number and two IBANs. Under GDPR art. 5(1)(c), nothing else runs on raw text. I have not repeated any of those values below. Do the following before any model call, including the one that drafts the taxonomy:

- **Masking:** use deterministic patterns for IBAN, email, phone and customer id. Use named-entity recognition for names and places, including "Lyon" in the card example. Replace each with a typed placeholder (`[NAME]`, `[IBAN]`, `[EMAIL]`, `[PHONE]`, `[CUSTOMER_ID]`, `[PLACE]`).
- **Check:** hand-review at least 100 masked conversations and report the residual leak rate. Nothing else starts until that check passes. The sample should include free-text leaks, such as an IBAN with unusual spacing or a name inside a sentence.
- **Raw text** stays in the source system.
- **Retention:** set a retention period and a named owner for deleting the masked text and the classifier logs. Masked chat can still identify someone (art. 5(1)(e)).

## 1. Dimensions
| Dimension | Feeds |
|---|---|
| use_case | volume and ROI |
| domain / KB | quality by knowledge base |
| resolution (resolved, escalated, abandoned, unresolved) | KB prioritisation |
| sentiment | quality review |
| language | routing and coverage |

Drop any of these that no decision uses.

## 2. Draft taxonomy (provisional, not frozen)
Three conversations cannot support 8–12 evidence-based classes. Only the first three below come from the samples. The rest are hypotheses to confirm or discard.

**Method to finish it:**
1. Read about 50 masked conversations, sampled across months and channels.
2. Write a free-form note on what each user wanted.
3. Cluster the notes.
4. Keep reading until new conversations add no new class.
5. Freeze at 8–12 mutually exclusive classes with a definition, two examples and a counter-example each. Version it as `taxonomy_v1`.

| Class | Status | Definition |
|---|---|---|
| Update personal or account details | seen | Change IBAN, address or contact details, or the account used for salary |
| Card loss, theft, blocking or replacement | seen | Lost, stolen or swallowed card, blocking, new card |
| Fee or charge explanation | seen | Why was I charged, fee schedule, disputed fee |
| Transaction or payment question | hypothesis | Pending, failed or unrecognised transactions |
| Transfers and payment setup | hypothesis | Making or limiting transfers, direct debits, standing orders |
| Balance and account information | hypothesis | Balance, statements, documents |
| Loans, savings and products | hypothesis | Product information and applications |
| Fraud or dispute | hypothesis | Suspected fraud, chargeback |
| Digital access and app problems | hypothesis | Login, app errors, password |
| Complaint or human-agent request | hypothesis | Explicit complaint or request for an advisor |
| Other | cap at 10% | Anything that fits none of the above |

**Edge-case rules to write down:**
- A conversation with two requests takes the class of the first one the user states.
- A swallowed card is "card", even if it also triggers a fee question.
- A fraud signal outranks "card" when the user says the card was used without their consent.

## 3. Annotation guide and labelled set
- Write a guide with the definitions, examples, counter-examples and the rules above.
- Label 150–200 masked conversations, sampled across the period, channels and populations.
- Have two labellers double-label at least 50 of them. Their agreement is the ceiling a classifier can reach.

## 4. Choosing the classifier
1. Run 2–3 candidates on the labelled set: a small and cheap model, a mid-tier model and a frontier model. Every candidate sees masked text only.
2. Report agreement per dimension, never one average. Also report the confusion between the closest classes (for example fee vs transaction, and card vs fraud), cost per conversation and latency.
3. A candidate below the human ceiling on a dimension is not trusted on that dimension without review.
4. **Target setup, routed by confidence:**
   - The classifier returns a label and a confidence for each conversation, using structured output with the class list in the prompt.
   - The cheap model keeps cases above a threshold chosen on the labelled set.
   - A stronger model or a human takes the cases below it.
   - Low-confidence cases go to review or to "unclassified", never forced into a class.
   - Report blended agreement and blended cost per conversation at the chosen threshold.
   - One model alone is only an interim step.
5. Run the full 45,000 only after steps 1–4 pass. Batch processing keeps the cost down.

## 5. Monthly drift check
- Label a fresh sample of 50–100 conversations each month.
- Compare agreement per dimension with the last run, and track the shares of "other" and of low-confidence cases.
- A drop in agreement, "other" above 10%, or a new recurring request opens a taxonomy review.
- A taxonomy change creates a new version and the labelled set is relabelled.
- This is the design behind the "drift detection live" gate (L5) for the assistant.

## 6. Output schema
One row per conversation: `trace_id`, `use_case`, `domain`, `resolution`, `sentiment`, `language`, `confidence`, `classifier_version`, `taxonomy_version`.

Volume by use case comes from these rows, not from declared usage. It feeds `assistant-kpis-cost-per-outcome`. For any use case with high volume and a high unresolved share, pull a masked sample and hand it to `build-evals` as candidate golden-set cases.

## 7. Observation on resolution
In the first sample, the assistant told the user to change the details themselves in Settings, without confirming the action. Decide in the annotation guide how "redirected to self-service" counts. I suggest a separate resolution label, because it will likely be a large share of conversations.

## What I need from you
- Monthly volume, period and channels.
- Who may read raw text.
- The decisions this feeds (KPI, KB, ROI).
- Whether you have any hand-labelled conversations, and which candidate models and prices to compare.

Once the masking check is done, send me ~50 masked conversations and I'll finish the taxonomy from them.