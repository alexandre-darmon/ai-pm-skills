# Calibration test

Load this when a population reviews or validates AI outputs. It shows whether people can catch a wrong output, which completion cannot show.

## Why two scores

A reviewer can fail in two opposite ways. Missing errors means they trust the tool too much, and the oversight exists on paper only. Flagging sound outputs means they trust it too little, and re-checking everything erases the time the tool was meant to save. Scoring catches alone rewards whoever flags everything.

AI Act art. 14(4)(b) asks that a high-risk system be provided so that the people assigned to oversee it can stay aware of the tendency to over-rely on its output (automation bias). It sets no test or training format. Whether it applies to a given tool goes to counsel through `ai-act-classification`. The test is useful either way.

## Build the batch

1. Start from real outputs of this tool, in the form reviewers see them.
2. Take the errors from its own failures: failed cases from `build-evals`, incident cases from `ai-incident-playbook`. Before launch, failed eval cases may be all there is.
3. Make them plausible and cover the failure modes in the objectives. A typo tests attention, not judgement of the tool.
4. Keep sound outputs in the batch, otherwise false alarms cannot be measured.
5. Do not mark the seeded items or say how many there are. Reviewers work as they would on the job.
6. Have a subject expert confirm the answer key: a seeded error must be wrong, and a sound output must be sound.

## Score and read

| Population | Batch date | Errors caught / seeded | Sound outputs wrongly flagged / sound | Team's pass mark |
| --- | --- | --- | --- | --- |

- Report counts with the batch size. With five seeded errors, one miss moves the rate by 20 points.
- The batch holds more errors than production does, to fit the time available. It measures whether people can catch errors, not how vigilant they stay when errors are rare. Say so when reporting it.
- Many misses on one failure mode across a population: retrain on it, and tell the tool's owner, since the screen or the tool's level may be the cause.
- Wide gaps between reviewers: compare decisions and align on what counts as an error.
- Acceptance rates in production are a related signal, owned by `assistant-kpis-cost-per-outcome`.

## Retest

Use fresh errors at each refresh: people remember a batch. Add errors from whatever caused the refresh, such as the incident or the new release's failed eval cases.

## Results about staff

Individual scores are personal data about employees and may read as performance evaluation. Decide before the first test who sees them and what they may be used for, and take that to the DPO; whether employee representatives must be informed or consulted is a question for counsel. The registry needs the result per population; individual results serve retraining.
