# Eval conventions

How a skill's cases are written and scored. Rationale lives in PRD §11; this file is the working reference. For the process explained with diagrams, see [docs/evaluation.md](../docs/evaluation.md).

Harness: [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals), native format, no adapter.

## Layout

```
<skill>/evals/
└── <skill>-001/            # one folder per case; folder name = case name
    ├── prompt.md           # frontmatter + the scenario sent to the agent
    ├── graders/            # one file per check
    │   ├── triggered.md
    │   ├── redline-<rule>.md
    │   └── ...
    └── fixtures/           # hand-written answers that test the graders (not sent to the agent)
        ├── good.md
        └── bad.md
```

At least 3 public cases per skill, plus at least one case tagged `negative`. `scripts/validate_skills.py` enforces the layout.

## `prompt.md`

```markdown
---
name: <skill>-<nnn>
description: <one line> (source - <origin, year>)
tags: [<skill>, <p0|p1|p2>, <nominal|edge-case|red-line|redteam|negative>]
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
4. **Negative** (mandatory, at least one): a near-miss request taken from a "Do not use" bullet, where the skill must stay silent.

A case where the model alone already scores as well as with the skill does not measure the skill's value: make it harder or replace it. It can stay as a regression guard when the skill could make the model worse on it (a red line the skill might weaken), as long as the skill's mean delta stays > 0.

## Graders

| Kind | Native type | Use for |
| --- | --- | --- |
| exact | `regex` (`match` omitted = must include; `not_contains`; `count:N`), `tool_used`, `file_exists` | mandatory words, articles cited, formula lines, red-line phrases |
| checklist | one `regex` per mandatory item | fixed headings, required fields |
| judge | `llm`, criteria in the body | coherence of a recommendation, reasoning quality |

Rules:

- **Every case has `graders/triggered.md`**: `type: tool_used`, `tool: Skill`, `input_match: '"skill"\s*:\s*"(?:[\w-]+:)?<skill>"'`. The Skill input reaches the grader as JSON (`{"skill":"<skill>"}`); anchoring on the whole name stops a sibling skill (`<skill>-lite`) from passing it. In a two-arm run it is an indicator, not part of the score.
- **Negative cases** carry `graders/not-triggered.md` instead: the same `input_match` with `min: 0`, `max: 0`, `arm: both` (`min` defaults to 1, so without `min: 0` the grader can never pass). It is the case's only grader. It is scored; the case fails if the skill fires, or the run errors, in any run, and is left out of the mean delta.
- **Deterministic first.** A yes/no check is a `regex`, not a judge.
- **Red lines are named `redline-<rule>.md`** and weigh more. The weight `w` must make one failure drop the run below threshold: `w > W × (1 − t) / t`, with `W` the other scored weights and `t` the threshold (`w > W/4` at 0.80, `w > W/9` at 0.90); the validator checks it. A red line must also pass in every run with the skill, whatever the mean of the runs. A case tagged `red-line` has at least one.
- **No echo.** A must-include `regex` must not match the prompt itself: an answer that repeats the brief would pass it. Match what the skill adds (the challenge to a number, not the number).
- **Regex patterns** use `flags: i` and tolerate wording variants (`success (metric|measure)`).
- **Fixtures test the graders.** Every case with a `regex` grader has `fixtures/good.md` (an answer that passes every `regex` grader) and `fixtures/bad.md` (an answer that crosses the red line: it scores below threshold and fails a `regex` red line if the case has one). `llm` graders count as passed in both, so the greps alone must reject the bad answer. When a paid run misses a grader on a sound answer, add that phrasing to `good.md` before widening the pattern.
- **`file_exists`** only sees files Claude created, so the case needs `Write` in `allowed_tools`.
- **Govern skills** use no `llm` or `baseline` grader.
- **Judges are calibrated** before use: ≥ 80% agreement with 20 human-labelled cases per skill, frontier model to calibrate, then a cheap pinned `--judge-model`. An `llm` grader passes on 2 of 3 votes.

## Scoring and thresholds

- Run score = weighted share of graders passed. Case score = mean of runs. A case passes at ≥ the skill's `eval_threshold` (0.80 default, 0.90 for govern and flagship).
- `claude plugin eval` does not read `eval_threshold`: it fails a case below `--threshold`, which defaults to 1.0. Pass the skill's threshold explicitly.
- Every run has two arms, with and without the skill. A skill whose mean delta is ≤ 0 fails: it adds nothing over the model alone. The CLI reports the delta but does not fail on it, so the run script checks it from the `--json` output.
- `run_evals.py` also lists the graders that pass, or fail, in every run of both arms: they measure the model, not the skill. It is a warning; make the grader harder or keep it knowingly as a regression guard.
- The summary of the first passing `--full` run (`eval-out/<skill>.json` from `scripts/run_evals.py`) is frozen in `baselines/<skill>.json` with model, judge model, date and a hash of `evals/`. PR runs reuse its scores without the skill while the hash and models match.

## Running

```bash
claude plugin eval drafts/<skill> --runs 1 --threshold 0.8 --max-cost-usd 2   # one skill, cheap check
claude plugin eval skills/<skill> --case '<skill>-003' --threshold 0.8        # one case
```

Always target one skill folder, never the repo root. Results land in `evals/results/` (git-ignored).

`python3 scripts/validate_skills.py` runs the free checks on every push: the harness schema (unknown prompt or grader keys, `match`, `flags`, a grader `name` other than its file name), fixtures, echo, red-line weights, the negative case and anchored triggers. It needs `node`: regex graders are checked with JavaScript RegExp, as the harness runs them. `run_evals.py --runs 3` confirms a red-line or discrimination finding.

`python3 scripts/run_evals.py --full <skill-folder>` runs the same with pinned models and applies the pass rules (threshold from `eval_threshold`, mean delta > 0). CI runs it only on request: on PRs labelled `run-evals`, or by hand on every skill after a major change; see PRD §11.5.

## Holdout

20% of each skill's cases live in the private repo `ai-pm-skills-holdout`, same format. They never enter this repo or articles, and are never sent to providers that train on data.

## Anonymisation

Cases come from real briefs, anonymised by a written procedure before they enter the repo, with synthetic entities and the client's sign-off for any recognisable pattern. The procedure itself is an open decision due in Wave 1 (PRD §14; leaning: scripted NER masking plus a manual review checklist).
