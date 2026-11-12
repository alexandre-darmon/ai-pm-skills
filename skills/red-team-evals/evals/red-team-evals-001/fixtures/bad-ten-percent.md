# Attack testing plan: claims assistant

Your developers' 30 jailbreaks are a good start. Sample 10% of conversations in production for review.

Run 300 attacks per class with the CISO's team; a single week is not enough for more. The 30 jailbreaks show the assistant resists attacks, so the plan focuses on the tools.

Classes: indirect prompt injection through uploads, another customer's claim, coverage promises, prompt leakage. Write a success criterion per class and a tolerance per class before testing, keep a held-out set sealed from the developers, list what stays untested, and turn every success into a regression case.
