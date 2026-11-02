# Eval conventions

How a skill's cases are written and scored. Rationale lives in PRD §11; this file is the working reference.

Harness: [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals), native format, no adapter.

## Layout

```
<skill>/evals/
└── <skill>-001/            # one folder per case; folder name = case name
    ├── prompt.md           # frontmatter + the scenario sent to the agent
    └── graders/            # one file per check
        ├── triggered.md
        └── ...
```

At least 3 public cases per skill. `scripts/validate_skills.py` enforces the layout.

## `prompt.md`

```markdown
---
name: <skill>-<nnn>
description: <one line> (source - <origin, year>)
tags: [<skill>, <p0|p1|p2>, <nominal|edge-case|red-line|redteam>]
expected_outcome: <one sentence, what a good run does>
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

<the scenario, anonymised, written as the user would ask it>
```

- The first tag is always the skill name (the validator checks it). CI runs each changed skill by targeting its folder.
- The scenario reads like a real request. It never names the skill: triggering is part of the test.
- Unknown frontmatter keys make the case fail to load.
- `runs` defaults to 3; CI overrides it with `--runs`.

## Which cases

A skill's cases are the ones its PRD §9 entry lists (3 minimum); that list takes precedence. When adding cases, a useful mix is:

1. **Nominal**: a typical brief the skill should handle end to end.
2. **Edge case**: a mandatory input missing, or a borderline situation.
3. **Red line**: an input that pushes the skill to break one of its rules.

A case where the model alone already scores as well as with the skill does not measure the skill's value: make it harder or replace it. It can stay as a regression guard when the skill could make the model worse on it (a red line the skill might weaken), as long as the skill's mean delta stays > 0.

## Graders

| Kind | Native type | Use for |
| --- | --- | --- |
| exact | `regex` (`match` omitted = must include; `not_contains`; `count:N`), `tool_used`, `file_exists` | mandatory words, articles cited, formula lines, red-line phrases |
| checklist | one `regex` per mandatory item | fixed headings, required fields |
| judge | `llm`, criteria in the body | coherence of a recommendation, reasoning quality |

Rules:

- **Every case has `graders/triggered.md`**: `type: tool_used`, `tool: Skill`, `input_match: <skill>`. Without `input_match`, any skill of the plugin firing would pass it. In a two-arm run it is an indicator, not part of the score.
- **Deterministic first.** A yes/no check is a `regex`, not a judge.
- **Red lines weigh more.** A red-line grader's weight `w` must make one failure drop the run below threshold: `w > W × (1 − t) / t`, with `W` the other scored weights and `t` the threshold (`w > W/4` at 0.80, `w > W/9` at 0.90). Known ceiling: the case score is the mean of its runs, so a red line missed in one run of three can still pass.
- **Regex patterns** use `flags: i` and tolerate wording variants (`success (metric|measure)`); check them against a good and a bad answer before committing.
- **`file_exists`** only sees files Claude created, so the case needs `Write` in `allowed_tools`.
- **Govern skills** use no `llm` or `baseline` grader.
- **Judges are calibrated** before use: ≥ 80% agreement with 20 human-labelled cases per skill, frontier model to calibrate, then a cheap pinned `--judge-model`. An `llm` grader passes on 2 of 3 votes.

## Scoring and thresholds

- Run score = weighted share of graders passed. Case score = mean of runs. A case passes at ≥ the skill's `eval_threshold` (0.80 default, 0.90 for govern and flagship).
- `claude plugin eval` does not read `eval_threshold`: it fails a case below `--threshold`, which defaults to 1.0. Pass the skill's threshold explicitly.
- Every run has two arms, with and without the skill. A skill whose mean delta is ≤ 0 fails: it adds nothing over the model alone. The CLI reports the delta but does not fail on it, so the run script checks it from the `--json` output.
- The summary of the first passing `--full` run (`eval-out/<skill>.json` from `scripts/run_evals.py`) is frozen in `baselines/<skill>.json` with model, judge model, date and a hash of `evals/`. PR runs reuse its scores without the skill while the hash and models match.

## Running

```bash
claude plugin eval drafts/<skill> --runs 1 --threshold 0.8 --max-cost-usd 2   # one skill, cheap check
claude plugin eval skills/<skill> --case '<skill>-003' --threshold 0.8        # one case
```

Always target one skill folder, never the repo root. Results land in `evals/results/` (git-ignored).

`python3 scripts/run_evals.py --full <skill-folder>` runs the same with pinned models and applies the pass rules (threshold from `eval_threshold`, mean delta > 0). CI runs it on PRs labelled `run-evals` and weekly; see PRD §11.5.

## Holdout

20% of each skill's cases live in the private repo `ai-pm-skills-holdout`, same format. They never enter this repo or articles, and are never sent to providers that train on data.

## Anonymisation

Cases come from real briefs, anonymised by a written procedure before they enter the repo, with synthetic entities and the client's sign-off for any recognisable pattern. The procedure itself is an open decision due in Wave 1 (PRD §14; leaning: scripted NER masking plus a manual review checklist).
