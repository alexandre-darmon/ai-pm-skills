The word 'robust' has to go: 50 prompts with no success are a smoke test, and the second line will read it as a claim you cannot back.

**Why not.**
- Zero successes in 50 still allows a true attack-success rate of up to about 6% (rule of three, 3/50; the Wilson 95% upper bound is about 7%). What that means in practice depends on the number of attack attempts a month, estimated from logs; the 25,000 conversations are not the base, since most are ordinary questions.
- The 50 prompts came from a well-known public list, which model providers have likely already patched: they measure yesterday's attacks.
- They were chosen and run by two developers of the build team, not by testers independent of it.
- They test one class only, direct jailbreaks. Indirect prompt injection (through product sheets or transfer references), access to another customer's balances and system prompt leakage were not tried.

**Proposed wording.**
"Direct jailbreak attempts: 0 successes in 50 prompts from a public list, run by the build team on version X on <date> (95% upper bound about 7%). Not tested: indirect injection, cross-customer data access, system prompt leakage. A campaign with independent testers, success criteria and tolerances per class signed beforehand and a sealed held-out set is planned before <date>; residual risk accepted by <owner>."
