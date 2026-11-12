# Review app brief — <feature name>

<For the coding agent. The PM decides what is below; the agent builds it in one file on the bank's approved stack; a fresh session reviews the code. Owner: <name>. Kill date: <date>.>

## Purpose and decision fed
<Which decision the labels feed (error analysis, judge calibration, release), who labels (named experts), how many traces, by when. Approved tool checked first: <none fits because ...>.>

## Data in and masking
<ICT asset entry and end-user computing tier, approved before any production-derived data is loaded. Export file and its source. Masking in the export step, typed consistent placeholders. Residual leak check: <traces read, by whom, leaks found, upper bound on the leak rate>. Checks that need real values run in the source system: <which>. No connection to production.>

## Sampling script (separate from the app)
| Stream | Stratum | Traces | Why |
| --- | --- | --- | --- |
| random | <proportional to class volume> | | the only stream that gives a rate |
| targeted | <thumbs-down, escalations, low confidence, risky small classes> | | finds modes, over-counts them |
<Seed, sample file version, dev/test split for judge calibration.>

## Screen and label
<What one screen shows (input, retrieved ids and passages, tool calls, guardrail hits, output, prompt version). Label: pass / fail, critique mandatory on fail, "not sure" flag. No 1–5 scale, no pre-label.>

## Audit fields per label
`trace_id, label, critique, reviewer_id (company login), labelled_at (UTC), app_version, sample_version`. Append-only; save refused without reviewer.

## Storage
<Approved store, access list, retention, who reads raw critiques, access logged.>

## Exports
- error-analysis: `trace_id,stream,class,mode,critique,reviewer_id,labelled_at`
- llm-judge-calibration: `trace_id,split,human`

## Smoke test
<10 known traces through load, label, save, export, re-import. Checks and result. Reviewer of the code.>

## Review cost
<traces × minutes ÷ 60 × loaded cost = EUR; build hours; model cost per run of the feature from the capture fields.>

## Capture contract (upstream logging)
| Field | Logged today? | Request to engineering |
| --- | --- | --- |

## Questions for counsel and the DPO
<The questions that apply to this system and this bank, each with who answers it.>

## After the review
<Rebuilt, registered at its end-user computing tier, or retired on the kill date: prototype-handover.>
