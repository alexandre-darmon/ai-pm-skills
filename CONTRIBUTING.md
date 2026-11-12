# Contributing

Skills here encode what a strong model does not do on its own for an AI or data PM in a regulated European company. A skill is accepted when its evals show it: the answer with the skill scores better than the model alone, on cases that read like real requests. The positioning is in [foundations/evals-as-evidence.md](foundations/evals-as-evidence.md); the full rules are in [PRD.md](PRD.md) and [AGENTS.md](AGENTS.md).

## Propose a skill

1. Open an issue first ("New skill" template). Say which block it belongs to (specify, build, evaluate, prove), the requests that should trigger it, and the neighbouring skill it must not compete with. The catalog is capped at 30 skills: a new one often replaces or merges into an existing one.
2. Start from the template: `cp -r templates/skill drafts/<name>`, set `name: <name>` (kebab-case, same as the folder).
3. Write `SKILL.md` with the fixed frontmatter and headings, heavy material in `references/`, output templates in `templates/`.
4. Write at least four eval cases (three positive, one negative), with `fixtures/good.md` and `fixtures/bad.md` for each.
5. Open a pull request against `main`. New skills stay in `drafts/` until a recorded paid run passes.

To change an existing skill, open a pull request directly. Bump `metadata.version`. A change to the text of a catalog skill makes its recorded run stale: it needs a new paid run before the merge.

## The rules, in plain words

- **AI-specific or out.** If the skill would read the same for a non-AI product, it does not belong here.
- **Checklists, never verdicts.** Legal skills never say "compliant". They produce classifications, checklists and questions for counsel. They need a 0.90 threshold, a `last_verified` date, and no LLM judge.
- **Every number has an anchor.** A gain is volume × quality × unit value, minus run and change costs. No free-floating percentages.
- **One autonomy ladder.** Refer to levels L0 to L5 from `references/autonomy-ladder.md`; never redefine them.
- **Skills travel alone.** Cite `references/<file>.md`, never `foundations/`. Edit shared material only in `foundations/` and run `python3 scripts/validate_skills.py --sync` to refresh the copies.
- **Your own words.** Cite ideas from books and newsletters; never copy more than a sentence.
- **Short where it is always loaded.** `description` at most 200 characters, saying when to use the skill; body at most 2,000 words.
- **No client data.** Eval cases are anonymised. Private holdout cases never enter the repo.
- **English**, except legal annexes where the law is French.

## How evals work

Each case is a request (`prompt.md`) and its graders: the skill must fire, regex graders check what the skill adds, and one `redline-*.md` grader checks the thing the answer must never do. The same case runs with the skill and without it; a control arm also runs it with the skill's output template only. A skill enters `skills/` when its score reaches `eval_threshold`, every red line holds in every run, and it beats the model alone by at least 10 points, over three runs per case.

Free checks (structure, graders against the fixtures) run on every push. Paid runs happen only on request: a maintainer adds the `run-evals` label to the pull request. Fork pull requests get no secrets, so a maintainer runs those. Diagrams and details: [docs/evaluation.md](docs/evaluation.md). Case format: [foundations/eval-conventions.md](foundations/eval-conventions.md).

## What a pull request must pass

```bash
pip install pyyaml                         # the validator also needs node
python3 -m unittest discover -s scripts
python3 scripts/validate_skills.py         # use --no-evidence while editing a draft
python3 scripts/check_generated.py         # README and skill-eval-gains.md match the generators
```

- The validator reports no problem. For a catalog skill this includes the evidence gate: the recorded run in `baselines/` matches today's text and cases.
- A skill moving to `skills/` comes with its passing run, its entry in `.claude-plugin/marketplace.json` (in the bundle and as its own plugin), and refreshed generated files (`scripts/eval_gains.py`, `scripts/readme_catalog.py`, `scripts/lifecycle_svg.py`, `scripts/evals_svg.py`).
- Do not hand-edit the generated blocks of `README.md` or `skill-eval-gains.md`.

## Licence

Skills, foundations and docs are CC BY 4.0 ([LICENSE-CC-BY-4.0](LICENSE-CC-BY-4.0)); code in `scripts/`, `.github/` and `.claude-plugin/` is MIT ([LICENSE](LICENSE)). By contributing you agree your work is published under these licences.
