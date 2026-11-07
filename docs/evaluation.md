# How a skill is evaluated

This page explains the evaluation process with diagrams. The rules themselves live in [`foundations/eval-conventions.md`](../foundations/eval-conventions.md) (working reference) and [PRD §11](../PRD.md#11-evaluation-strategy) (rationale). When they change, update this page too.

## The idea in one picture

A skill is a cheat sheet for the model. To know if it helps, we ask the same question to the model **with** the skill and **without** it, and grade both answers with the same marking rules (the graders). A skill is worth keeping only if the answer with the skill scores better.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FFFFFF', 'primaryBorderColor': '#CFCBD6', 'primaryTextColor': '#0A0A0A', 'secondaryColor': '#F4F2F5', 'tertiaryColor': '#F4F2F5', 'clusterBkg': '#F4F2F5', 'clusterBorder': '#E6E3EA', 'lineColor': '#8C52EE', 'edgeLabelBackground': '#F4F2F5'}}}%%
flowchart LR
    Q["Case<br/>prompt.md"] --> W["Model + skill"]
    Q --> O["Model alone"]
    W --> G["Graders<br/>graders/*.md"]
    O --> G
    G --> R["Report<br/>score with, score without, delta"]
```

## The life of a skill

Free checks run on every push and catch most mistakes before any money is spent. Paid runs happen only on request: the `run-evals` label on a pull request, or a manual run after a major change.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FFFFFF', 'primaryBorderColor': '#CFCBD6', 'primaryTextColor': '#0A0A0A', 'secondaryColor': '#F4F2F5', 'tertiaryColor': '#F4F2F5', 'clusterBkg': '#F4F2F5', 'clusterBorder': '#E6E3EA', 'lineColor': '#8C52EE', 'edgeLabelBackground': '#F4F2F5'}}}%%
flowchart TD
    A["Write or change a skill<br/>in drafts/"] --> V{"validate<br/>free, every push"}
    V -- "fails" --> A
    V -- "passes" --> E{"evals<br/>paid, on request"}
    E -- "fails" --> A
    E -- "passes" --> B["Freeze baseline<br/>baselines/skill-name.json"]
    B --> P["Move to skills/<br/>status tested"]
```

| Step | Command | Cost | What it checks |
| --- | --- | --- | --- |
| validate | `python3 scripts/validate_skills.py` (needs Python with pyyaml, and node) | free | structure, the harness schema (unknown keys fail the load), plus the free checks below |
| evals | `python3 scripts/run_evals.py --full drafts/<skill>` | a few cents per case | real answers, with and without the skill; every answer is saved to `eval-out/answers/` |
| regrade | `python3 scripts/run_evals.py --regrade drafts/<skill>` | free | the saved answers re-scored with the current graders, no model call; valid for grader changes, stale after a change to the skill |

## Anatomy of a case

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FFFFFF', 'primaryBorderColor': '#CFCBD6', 'primaryTextColor': '#0A0A0A', 'secondaryColor': '#F4F2F5', 'tertiaryColor': '#F4F2F5', 'clusterBkg': '#F4F2F5', 'clusterBorder': '#E6E3EA', 'lineColor': '#8C52EE', 'edgeLabelBackground': '#F4F2F5'}}}%%
flowchart LR
    subgraph C["evals/skill-name-001/"]
        P["prompt.md<br/>the question"]
        subgraph G["graders/"]
            T["triggered.md<br/>the skill fired"]
            R1["must-include greps"]
            RL["redline-*.md<br/>the never-do rule"]
        end
        subgraph F["fixtures/"]
            GO["good.md<br/>a passing answer"]
            BA["bad.md<br/>an answer crossing the red line"]
        end
    end
```

- `prompt.md` is the question, written like a real request. It never names the skill: triggering is part of the test.
- `graders/` holds the marking rules: greps (`regex`) first, a judge (`llm`) only when a grep cannot decide.
- `fixtures/` holds the answers that test the graders themselves: `good.md` and `bad.md` written by hand, plus real answers saved from paid runs (`good-<run>.md`, and `bad-<run>.md` for a model-alone answer that crosses a red line). The model never sees them, and they do not count in the eval hash.

## How an answer is scored

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FFFFFF', 'primaryBorderColor': '#CFCBD6', 'primaryTextColor': '#0A0A0A', 'secondaryColor': '#F4F2F5', 'tertiaryColor': '#F4F2F5', 'clusterBkg': '#F4F2F5', 'clusterBorder': '#E6E3EA', 'lineColor': '#8C52EE', 'edgeLabelBackground': '#F4F2F5'}}}%%
flowchart TD
    A["One answer"] --> S["Run score = weighted share<br/>of graders passed"]
    S --> C["Case score = mean of its runs"]
    C --> T{"Case score ≥ eval_threshold?<br/>Every redline-* passed in every run?"}
    T -- "no" --> X["Case fails"]
    T -- "yes" --> D{"Mean delta over the skill's cases ≥ 10 points?<br/>(with − without)"}
    D -- "no" --> Y["Skill fails: it adds too little<br/>over the model alone"]
    D -- "yes" --> Z["Skill passes"]
```

The `triggered` grader is not part of the score: it reports whether the skill fired. Negative cases are left out of the delta, because without the skill they cannot fire.

## The template-only control

The model alone is an easy opponent, so a gain over it can come from the output format rather than the method. `python3 scripts/template_arm.py <skill>` adds a third arm: same name, description, cases and graders, but the skill's body is only its own `templates/` files, with no method, rules or references. The other two scores come from `baselines/<skill>.json`, and the result goes to `baselines/template-arm/`.

Rules, written and committed before the first run (2026-11-06), on `llm-feature-prd`, `conversation-analysis` and `ai-act-classification`, 3 runs per case:

- **Method gain** = with the skill − template only, mean over the scored cases.
- **At least 10 points:** the method beats its format.
- **Under 10 points:** the gain comes mostly from the format, and the skill's gain is reported that way.
- **Graders are frozen for this test.** A grader found wrong afterwards is reported, then fixed for every arm by re-scoring, and both results stay published.

This is a strict test: these templates are the skill's own and already carry part of its method, such as the columns of a table. A plain generic template would be easier to beat.

Extended under the same rules to `build-evals`, `assistant-kpis-cost-per-outcome` and `cse-consultation`, committed before their run. Drafts have no frozen baseline yet, so they wait for a 3-run confirmation.

## The blind LLM judge

Regexes check words, not the quality of the advice. `python3 scripts/judge_answers.py <folder>` asks a cheaper model (Haiku 5.5) to grade the saved answers on a generic rubric: sound, actionable, honest about unknowns, risk-aware, specific. Results go to `baselines/judge/`.

Rules, written and committed before the full run (2026-11-06):

- **Information only.** It never changes a pass. Regexes and red lines keep the verdict.
- **Blind.** The judge does not see the arm, answers are shuffled, and mentions of a skill or its reference files are removed.
- **Not calibrated yet.** Calibration needs at least 80% agreement with 20 human-scored answers (PRD §11.2). Until then its scores are read as a signal, not a measure.
- **Never on legal skills** (AGENTS.md): `ai-act-classification`, `cse-consultation` and the other Govern skills get counsel's review instead.
- **The headline is the generic score.** "Meets the goal" is reported apart, because the skills' author wrote those goals.
- **Known biases are reported:** each answer is judged twice to show the judge's noise, and length is shown next to the scores.

**Choosing the judge** (rules committed before the Sonnet run and before any human score, 2026-11-07). Haiku 5.5 and Sonnet 5.5 grade the same answers. Sonnet also wrote those answers, so it may be lenient. A person then scores 20 answers drawn at random, blind to the arm, from 1 to 5 overall. Each judge's mean on the five criteria is compared with that score:

- **A judge is calibrated** if it lands within 1 point of the human score on at least 80% of the 20 answers.
- **If both pass,** the closer one is kept, measured by mean absolute gap; on a gap under 0.2 points, the cheaper one.
- **If neither passes,** the judge stays out of any reported score, and the rubric is revised before a new test.

## The four free checks

Paid runs can only be trusted if the marking rules are right. Four checks protect them, and three of them cost nothing.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FFFFFF', 'primaryBorderColor': '#CFCBD6', 'primaryTextColor': '#0A0A0A', 'secondaryColor': '#F4F2F5', 'tertiaryColor': '#F4F2F5', 'clusterBkg': '#F4F2F5', 'clusterBorder': '#E6E3EA', 'lineColor': '#8C52EE', 'edgeLabelBackground': '#F4F2F5'}}}%%
flowchart LR
    Q["Question"] --> W["Model + skill"]
    Q --> O["Model alone"]
    W --> G["Graders"]
    O --> G
    G --> R["Report"]
    C1(["1 · Fixtures:<br/>test the graders first"]) -.-> G
    C3(["3 · Red lines:<br/>instant fail"]) -.-> G
    C2(["2 · Discrimination:<br/>spot too-easy graders"]) -.-> R
    C4(["4 · Negative case:<br/>skill stays silent"]) -.-> W
```

| # | Check | Where it runs | Cost | It catches |
| --- | --- | --- | --- | --- |
| 1 | Grader fixtures, prompt echo | `validate_skills.py`, every push | free | a grader too narrow to accept a good answer, too loose to reject a bad one, or matching words the prompt already contains |
| 2 | Discrimination report | `run_evals.py`, after a paid run | free (reuses the run) | a grader that passes, or fails, with and without the skill: it measures the model, not the skill |
| 3 | Red lines | weight in `validate_skills.py`, every run in `run_evals.py` | free | a never-do rule hidden by the average of good marks elsewhere |
| 4 | Negative case | a paid case per skill | about 5 cents | a skill that fires on a request belonging to another skill |

### 1. Test the graders first

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#FFFFFF', 'primaryBorderColor': '#CFCBD6', 'primaryTextColor': '#0A0A0A', 'secondaryColor': '#F4F2F5', 'tertiaryColor': '#F4F2F5', 'clusterBkg': '#F4F2F5', 'clusterBorder': '#E6E3EA', 'lineColor': '#8C52EE', 'edgeLabelBackground': '#F4F2F5'}}}%%
flowchart LR
    GO["fixtures/good.md"] --> G["Regex graders<br/>of the case"]
    BA["fixtures/bad.md"] --> G
    G --> OK1{"good.md passes<br/>every grader?"}
    G --> OK2{"bad.md scores below threshold<br/>and fails a red line?"}
```

The validator also checks that each must-include grep does not match the prompt itself: if it does, an answer that repeats the brief passes. Example: a grader looking for `30%` when the brief says "30% productivity" proves nothing; it must look for the challenge ("the 30% is unanchored").

The greps run with JavaScript RegExp through `node`, exactly as the harness runs them (Python's `re` disagrees on accents next to `\b`, on some flags and on some syntax). `llm` graders cannot run offline, so they count as passed in both fixtures: the greps alone must reject the bad answer.

### 2. Spot the graders that do not tell the arms apart

After a paid run, the report lists each grader that passed in every run of both arms ("measures the model, not the skill") or failed in every run of both arms ("check the grader"). It is a warning, not a failure: such a grader can stay as a regression guard. With one run per case it is a hint; confirm with `python3 scripts/run_evals.py --full --runs 3 drafts/<skill>`.

### 3. A red line means instant fail

A grader named `graders/redline-*.md` is a never-do rule. Two rules apply:

- **Weight** (validator): a red line must weigh more than `W × (1 − t) / t`, where `W` is the sum of the other scored weights and `t` the threshold. At 0.80 that is a quarter of the other weights, at 0.90 a ninth. One miss then fails the case on its own.
- **Every run** (`run_evals.py`): a red line missed in any run with the skill fails the case, even when the mean of the runs is above the threshold.

A case tagged `red-line` must have at least one `redline-*` grader.

### 4. The skill stays in the bag

Every skill has at least one case tagged `negative`: a request close to its job but covered by one of its "Do not use" bullets. Its only grader (the validator enforces it) checks that the skill was **not** called, and an errored run fails the case too: silence must be shown, not assumed.

```yaml
type: tool_used
tool: Skill
input_match: '"skill"\s*:\s*"(?:[\w-]+:)?build-evals"'
min: 0   # the default min is 1, so without it the grader could never pass
max: 0
arm: both
```

`input_match` is anchored on the whole skill name, in every case, and every `tool: Skill` grader must use exactly this form. The Skill tool input reaches the grader as JSON (`{"skill":"build-evals"}`), so a bare `build-evals` would also match a sibling such as `build-evals-lite`.
