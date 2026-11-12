# Feasibility spike: <task>

Owner: <PM> · Decision taker: <name, role> · Model and hosting route: <model, version, route production would use>

## 1. The question
<One sentence, answered yes or no. Includes the model, the autonomy level of the step (references/autonomy-ladder.md) and the cost ceiling.>

## 2. Fixed before the build
Written <date>, signed by <name, role>. None of these moves after the first result.

| Item | Value |
| --- | --- |
| Time box | <n> days, from <date> |
| Maximum cost per correct answer | <amount>, from <unit value or cost of today's process, source> |
| Kill date | <date>: past it, the spike stops by default |
| Decision it feeds | <go to PRD / budget bet>, taken by <name> on <date> |

| Class | Share of traffic | Cost of an error | Target | Stop line | Can the product drop it? |
| --- | --- | --- | --- | --- | --- |
| <class> | <%> | <what goes wrong, who pays> | <%> | <%> | <yes / no> |

## 3. Data and tool check
- Cases per class, sized for its stop line before the run: <class: n (stop line)>. <synthetic share>% synthetic, <origin of the rest, how anonymised or pseudonymised>.
- Tool the spike runs in: <tool>. Authorised and registered as an ICT asset, or allowed by the end-user computing policy: <yes / no / asked to IT risk on date>.
- Contract with the model provider: <through procurement / opened outside it: third-party question to IT risk, processor terms to the DPO, on date>.
- Production credentials: none. Production personal data: <none, or the approved time-limited testing occasion, approver, end date>.

## 4. Lethal-trifecta check
| Leg | Present? | How |
| --- | --- | --- |
| Private data | <yes/no> | <> |
| Untrusted content | <yes/no> | <> |
| Way to send data out | <yes/no> | <> |
Leg removed in code if all three: <which, how>.

## 5. Design
<Workflow (one call or fixed chain: what code does, what the model does) or agent, and the cases that justified an agent.>

## 6. Criteria drift log
| Date | Criterion before | Criterion after | Why (output that triggered it) |
| --- | --- | --- | --- |
All cases re-graded under the final criteria: <yes, date>.

## 7. Results
| Class | n of N | Rate | 95% interval (Wilson) | Target | Stop line | Reading |
| --- | --- | --- | --- | --- | --- | --- |
| <class> | <k of n> | <%> | <lo to hi> | <%> | <%> | <clears / promising / undecided / short / dead> |

- Model spend: <amount> · correct answers: <k> · cost per correct answer: <amount> against the appetite of <amount> (<within / over, x times>).
- Rework cost of wrong answers: <wrong answers> × <cost of one human correction> = <amount>, or none (say why).
- Hours spent, from logs: <h> against the time box of <days>.

## 8. Decision
<Go to PRD / Reshape / Stop>, because <reading per class, cost, trifecta>.
- If go: classes not demonstrated, for build-evals to size: <list>.
- If reshape: the one thing that changes, the new appetite, the new kill date.
- If stop: what was learned.

## 9. What this spike is not
These numbers are not release evidence and are not the system's accuracy. Before any release claim, build-evals must: sample cases from production traffic per class; size each gated class for the margin between its expected rate and the bar (<n> cases to show <bar> when <expected rate> is expected); freeze the criteria (section 6 is the input); keep a private holdout; sign thresholds before the run; run on the engineering build, gated by release-to-production.
