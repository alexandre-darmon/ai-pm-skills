**Recommendation: don't hand it to IT for a rebuild. Register it as a team tool (tier 2) with a named owner, and let the 15 colleagues use it under a few conditions. A rebuild is the wrong answer for what this is today.**

**Tier and autonomy level**
- **Today:** tier 1 (personal, one user, every output reviewed). The tool only drafts, and you rewrite every summary, which is L1–L2 on the autonomy ladder.
- **After sharing with 15 people:** tier 2 (team, no regulated outcome, failures recoverable), still at L2 (drafts for a human). The tier moves because the number of users changes, not because the tool does.
- **Rebuild triggers:** a rebuild is warranted at tier 3 or 4, at L3 or above, or if it needs production credentials or production personal data. None applies here, because the inputs are public and it only drafts.

**Conditions that keep it at tier 2**
1. **Every colleague reviews and rewrites each output before use**, as you do now. If that stops, "a human checks it" no longer holds the tier down.
2. **Each user signs in with their own login on the approved platform.** Your login is never shared.
3. **The outputs stay out of regulated or financial-control uses.** If a summary feeds pricing, reserving, ORSA or a regulatory return, the tier is at least 3 and the answer changes. Please confirm this with finance.
4. **A named owner, a sponsor, and a review date.** I'd also want a kill or review date. If you didn't set one before the build, set one now.
5. **Prompts and the model version are kept under change control.** A model or prompt change means re-running your test cases before colleagues get it.
6. **No client data goes in.** Say so in the tool and in the guidance for users.

**What I'd do over the next couple of weeks**
- Write a one-page inventory entry: purpose, users, data (public only), model and version, where the prompts live, where it runs, owner, review date.
- Save 5–10 representative reports with your rewritten summaries as a small eval set. If someone later wants a rebuild, those cases are the baseline the rebuild has to match.
- Write a short note on what the app actually does versus what you intended. Check for hard-coded keys, no login, and any guardrail that exists only as a sentence in the prompt.
- Check the licence terms on the analyst notes. Some research licences restrict sharing with colleagues or processing by AI tools.

**What I don't know, and who decides**
- **IT risk** decides whether it is an ICT asset and whether it sits on an authorised-software list. As an insurer you are probably a DORA financial entity, so I'd assume it must be registered.
- **Model risk** decides whether it counts as a model under your policy and whether it needs validation.
- **Counsel and the DPO** only need to be involved if the inputs or use change, for example if personal data is added or the outputs start to feed decisions about people.

For your manager: the months-long rebuild would buy controls that suit tier 3 or 4 systems. For a drafting aid with human review and public inputs, the proportionate step is registering it and putting basic controls in place, which takes days.

This file is a proposal and a list of questions. IT risk, model risk and counsel decide.