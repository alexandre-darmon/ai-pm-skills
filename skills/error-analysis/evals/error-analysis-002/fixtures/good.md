These 25 notes give a provisional taxonomy (v0.1), not a final one: a new kind of failure still appears at T22, only 3 traces before the end, far from saturation (about 20 traces in a row with no new mode). And they all come from thumbs-down conversations, so they tell you which failures exist, not how often they happen: the shares below are shares of flagged traces, not of the 6,000 monthly conversations. To get rates, the policy lead reads a random sample of 60 conversations next.

Each trace is counted once, on its first upstream failure: T19 retrieved the French policy for a Belgian employee, so it counts under wrong country, not under leave arithmetic.

| Mode | Fails when… | Count (of 25 flagged) | Kind | Action |
| --- | --- | --- | --- | --- |
| Wrong country policy | the answer applies a rule of another country than the employee's | 7 (T01, T04, T09, T13, T16, T19, T24) | specification: the country is never passed | fix: pass the entity and filter retrieval; no judge |
| Outdated policy | the answer relies on a 2025 policy replaced in 2026 | 3 | specification: 2026 policies not loaded | fix: load them (KB owner) |
| No source link | the answer has no link to the policy page | 3 | specification: the prompt says nothing about sources | fix the prompt, then a code check for the link |
| Leave arithmetic | the stated balance differs from the HR system | 3 | generalisation | code check against the HR system |
| Invented rule or benefit | the answer states a rule found in no policy | 2 | generalisation | one binary LLM judge, calibrated on the lead's labels |
| No route to the HR business partner on a dispute | a disputed decision is not routed | 2 | specification | fix the prompt |
| Colleague's salary disclosed | the answer gives another employee's pay data | 1 | guardrail | severity: top priority regardless of count; access control and a test |
| Too long | answer over 10 lines for a yes/no question | 2 | generalisation | code check on length |
| Wrong language | answer language differs from the question's | 1 | specification: the prompt imposes English | fix the spec |
| No clarifying question | answers again without asking the missing contract type | 1 | generalisation | watch in the next read |

So: not one judge per category. Five modes are fixed in the prompt, the inputs or the KB with no evaluator; three get a deterministic code check; only invented rules need an LLM judge.
