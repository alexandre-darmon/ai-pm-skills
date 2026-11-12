# Attack taxonomy coverage grid

The campaign's classes come from the feature's harms (SKILL.md step 1). This grid is the check that runs afterwards: which public taxonomy entries are relevant to this feature, which of them the campaign tests, and which it leaves out and why. It is a coverage check, never the list of classes itself: a taxonomy entry with no harm in this feature is marked not applicable, with its reason.

## OWASP Top 10 for LLM Applications (2025 edition)

| Entry | Typical class in an assistant or RAG feature | Typical success criterion | Often not applicable when |
| --- | --- | --- | --- |
| LLM01 Prompt injection | direct jailbreak of a policy line; indirect instruction planted in a retrieved document, upload or lookup result | the forbidden output appears; the planted goal is reached | never: every feature that reads text is exposed |
| LLM02 Sensitive information disclosure | another customer's record, internal data, personal data in the output | a planted canary or a named out-of-scope record appears in the output | the feature reaches no data beyond the user's own |
| LLM03 Supply chain | a third-party model, plugin or connector behaves unexpectedly | tested through vendor evidence and contract, rarely by prompting | the PM has no say on components: route to vendor review |
| LLM04 Data and model poisoning | a poisoned knowledge-base document or fine-tuning example changes answers | the planted claim is repeated as fact | no fine-tuning and a closed, owned knowledge base |
| LLM05 Improper output handling | the output is executed or rendered downstream (SQL, HTML, a link) | the downstream system runs or renders the payload | the output is shown as plain text only |
| LLM06 Excessive agency | a lookup is called outside the user's scope; a tool the user triggers on their own record (a ticket, a draft) is pointed at another customer's record or misused | a forbidden call or argument in the trace | no tool; a tool that acts on systems on its own (L3 and above) makes it an agent: `agent-evals` |
| LLM07 System prompt leakage | the prompt, its rules or secrets in it are revealed | a canary placed in the prompt appears in the output | the prompt holds nothing sensitive (still test: it reveals the rules to bypass) |
| LLM08 Vector and embedding weaknesses | retrieval across tenants or access levels; a crafted document that ranks first for many queries | a document outside the user's rights is retrieved or cited | no retrieval |
| LLM09 Misinformation | a confident false statement on a regulated topic induced by the attacker | the named false claim appears | rarely: usually relevant for advice and claims |
| LLM10 Unbounded consumption | prompts that inflate tokens, lookups or cost | cost or tokens per request above a set cap | hard caps on tokens and calls exist and are tested elsewhere |

## NIST AI 100-2: attacker goals

Tag each class with one goal so the grid shows which goals the campaign leaves empty: availability (the system stops serving or costs explode), integrity (it does what the attacker wants), privacy (it reveals data or its own internals), misuse (generative output used for harm). Note whether the attacker needs the user's access only, can write content the system reads, or reaches training data.

## MITRE ATLAS

Map each class to the ATLAS techniques of the release you cite (technique ids and counts change between releases; write the release next to the mapping). ATLAS also holds case studies: read the ones for LLM applications to find classes the harm list missed.

## Coverage share

Coverage = classes tested in this campaign ÷ classes judged relevant (tested + untested). The untested relevant classes go, with their reason, into the residual-risk record. A campaign at 100% of a short list that skipped indirect injection on a feature that reads uploads is not complete: the relevance judgement is reviewed by the independent tester.
