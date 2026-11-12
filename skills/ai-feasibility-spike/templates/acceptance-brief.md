# Acceptance brief for a coding agent: <task>

## The question
<One sentence, from the spike report.>

## Cases
- Folder: `cases/<class>/<id>.input.<ext>` and `cases/<class>/<id>.expected.json`, <n> per class, synthetic or anonymised only.
- No production personal data, no production credentials, no outbound network call except the model endpoint.

## Check per class
| Class | Check (exact match, field equality, rule) | Target | Stop line |
| --- | --- | --- | --- |
| <class> | <check> | <%> | <%> |

## Design constraint
<Workflow: code does <lookups>, one model call does <judgment>. No agent loop unless the brief is revised.>

## Done when
One command (`<run command>`) prints, per class: n of N, rate, 95% Wilson interval, and overall: model spend, cost per correct answer, wall-clock time. It writes every output to `outputs/` for reading.

## Review
A fresh session or another model reviews the harness. Smoke test: three cases with known answers (one pass, one fail, one abstain) give the expected verdicts.
