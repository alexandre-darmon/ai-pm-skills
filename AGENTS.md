# AGENTS.md

Repo of Agent Skills for AI / Data PMs in regulated European companies. `PRD.md` is the source of truth: read the relevant section before adding or changing a skill.

## Layout

```
skills/<name>/      # catalog: skills with a passing eval suite (status tested | verified-in-mission)
drafts/<name>/      # same structure, not yet tested; not counted in the README
templates/skill/    # copy this to start a new skill
scripts/            # validate_skills.py (structure check run by CI)
foundations/        # shared backbones: autonomy ladder, ROI model, eval conventions, sources (read before writing a skill)
```

A skill folder:

```
<name>/
├── SKILL.md            # frontmatter + method, always loaded
├── references/         # deep material, loaded on demand
├── templates/          # output templates
└── evals/              # ≥ 3 cases, native `claude plugin eval` format (PRD §11.1)
    └── <name>-001/
        ├── prompt.md   # frontmatter (name, tags: [<name>, …], description, expected_outcome) + scenario
        └── graders/    # regex (must / must not include), tool_used Skill + input_match: <name> (always), llm (judge, optional)
```

## Commands

```bash
pip install pyyaml
python3 scripts/validate_skills.py          # structure check (what CI runs)
python3 -m unittest scripts/test_validate_skills.py
claude plugin eval drafts/<name> --runs 1     # paid: runs the cases with and without the skill
```

Always point `claude plugin eval` at one skill folder, never the repo root: from the root it also picks up the cases of drafts and templates.

## Writing a skill

1. `cp -r templates/skill drafts/<name>` and set `name: <name>` (kebab-case, equals folder).
2. Frontmatter fields and body headings are fixed (PRD §7.2). The validator enforces them; don't add or rename headings.
3. Move to `skills/` only when the eval suite passes (score ≥ `eval_threshold` and better than without the skill) and `status` is `tested` or `verified-in-mission`.

Hard rules (PRD §6), the ones easy to break when generating text:

- **Specific or absent**: if the skill reads the same for a non-AI product, it doesn't belong here.
- **Checklist, not verdict**: `govern` skills never output "compliant"; they produce classifications, checklists and questions for counsel. No `llm` grader on legal skills, `eval_threshold` ≥ 0.90, `last_verified` mandatory.
- **Anchored numbers only**: any gain traces to volume × quality × unit value − run cost − change cost.
- **The ladder is the spine**: reference L0–L5 from `foundations/autonomy-ladder.md`, never redefine levels locally.
- **Own words, cited ideas**: no excerpt from a book or newsletter longer than a sentence.
- **Progressive disclosure**: `description` ≤ 200 chars and states *when* to use; body ≤ 2 000 words; heavy material goes to `references/`.
- **Thirty is the ceiling**: never more than 30 skills in `skills/`.
- **No client data**: eval cases are anonymised; private holdout cases never enter this repo.

## Language

Skills, README and code in English. French only for legal annexes where the law is French (G1, G3).
