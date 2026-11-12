Subject: Robustness evidence for the credit chatbot

Dear model risk team,

Ahead of the January go-live, we propose to attach the vendor's security whitepaper, which reports 99% jailbreak resistance on an internal benchmark of 10,000 adversarial prompts. We won't submit the 99% figure as robustness evidence on its own; a short smoke test of our own integration goes with it.

- We will run a short test of our configured tools (transaction lookup and dispute ticket) for unauthorized access, for example attempts to read another customer's transactions or open fraudulent dispute tickets.
- We will ask the vendor what counts as a jailbreak in their benchmark and the temperature used; the vendor may have tuned on its own benchmark.
- Results will be reported per attack class.

We believe this gives a proportionate level of assurance for go-live.
