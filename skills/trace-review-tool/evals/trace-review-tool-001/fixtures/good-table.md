# Review app brief: complaints-reply drafts

## Data in and masking
The export script replaces names and IBANs with placeholders (PERSON_1, IBAN_1) before writing the file the app reads. The app is registered as an ICT asset first.
Residual leak check: a second person reads all 300 masked drafts; zero leaks in 300 bounds the leak rate at about 1%.

## Sampling script (separate from the app)
| Stream | Stratum | Traces | Why |
| --- | --- | --- | --- |
| random | in proportion to complaint type | 240 | the only stream that gives a rate |
| targeted | reopened complaints, heavily rewritten drafts | 60 | finds modes, over-counts them |

Rates come with their Wilson interval.

## Audit fields per label
`trace_id, label, critique, labelled_by (the logged-in user), labelled_at (UTC)`. Append-only.

## Storage
Approved internal database with an access list.

## Capture contract
The officer's rewrite of each draft is a human override: logged per trace with who and when.
