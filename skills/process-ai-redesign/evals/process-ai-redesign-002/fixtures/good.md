| Step | Current level | Target level | Why not L+1 | Gate to reach target |
| --- | --- | --- | --- | --- |
| Sort and route | L0 | L4 | — | canary passed |
| Compensation decision | L0 | L1 | financial effect | eval |

The L4 routing step calls ai-act-classification. Trade-off table on cost per outcome and reversibility; human fallback in every scenario.

Routing moves back one level when misrouting rises above 5% over a week, also after a model change. The complaints lead acts on it, without approval.
