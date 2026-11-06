| Step | Current level | Target level | Why not L+1 | Gate to reach target | Approach |
| --- | --- | --- | --- | --- | --- |
| Document extraction | L0 | L2 | errors on scans | eval ≥ 97% | LLM extraction |
| Sanctions and rules check | L0 | L3 | false positives | shadow 2 weeks | Rules engine, no model |
| Account decision | L0 | L1 | legal effect | user test | LLM summary for the analyst |

Scenarios: conservative, target, ambitious.

Human fallback in the target scenario: 9,000 files × 5 min of validation = 750 reviewer hours a month, against 1,500 hours left in the team. Queue owner: KYC lead; SLA one working day; at timeout the file goes back to manual handling.
