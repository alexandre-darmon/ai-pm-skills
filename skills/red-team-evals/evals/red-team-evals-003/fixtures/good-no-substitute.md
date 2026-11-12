Subject: Robustness evidence for the credit chatbot

The vendor's whitepaper is no substitute for testing our chatbot, and I propose we do not file its "99% jailbreak resistance".

- It measures their model, not our configuration: our system prompt, the transaction lookup, the dispute-ticket tool and our customers' data are not in their benchmark.
- We do not know what counts as a successful jailbreak in their test, which attacks the 10,000 prompts cover, or the generation settings (temperature, turns).
- The benchmark is internal: the vendor may have tuned the model on it, and it grades its own homework.
- One figure hides the classes that matter here: reading another customer's transactions, opening fraudulent dispute tickets, indirect injection through transaction descriptions.

The whitepaper can inform which attack classes we test. The evidence has to come from our own campaign on the deployed setup: classes from our harms, a success criterion and tolerance per attack class signed before testing, testers outside the build team, a sealed held-out set, and rates per class with intervals. We will also ask the vendor for its attack set, its criteria and settings.

Timeline: a focused campaign on the two costly classes fits before January if we start in two weeks.
