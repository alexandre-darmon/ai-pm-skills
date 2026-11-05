# ai-pm-skills

> Tested skills for AI product managers who ship in regulated companies.

An open-source set of [Agent Skills](https://agentskills.io) that take an AI or Data product from framing to budget, build, measurement and compliance, in a regulated European enterprise. Each skill is a folder an agent (Claude Code, Codex, Cursor, a custom agent) loads on demand: a `SKILL.md` with the method, templates, sources and an eval suite.

**Status: Wave 1 complete.** Six skills are in the catalogue (`skills/`, status `tested`), each with 4 cases (3 scored against the model alone, 1 where the skill must stay silent; Sonnet 5.5, 3 runs per case, November 2026):

| Skill | Stage | Threshold | Mean delta vs model alone |
| --- | --- | --- | --- |
| [`llm-feature-prd`](skills/llm-feature-prd/SKILL.md) | specify | 0.80 | +0.71 |
| [`build-evals`](skills/build-evals/SKILL.md) | measure | 0.80 | +0.53 |
| [`assistant-kpis-cost-per-outcome`](skills/assistant-kpis-cost-per-outcome/SKILL.md) | measure | 0.80 | +0.75 |
| [`conversation-analysis`](skills/conversation-analysis/SKILL.md) | measure | 0.80 | +0.62 |
| [`ai-act-classification`](skills/ai-act-classification/SKILL.md) | govern | 0.90 | +0.26 |
| [`cse-consultation`](skills/cse-consultation/SKILL.md) | govern | 0.90 | +0.28 |

Pending re-confirmation (paid runs paused): `build-evals` and `conversation-analysis` each missed one red line in 1 run of 3 on their last paid run. Those two graders have since been refitted and checked for free against real answers and probes, but not re-run. `llm-feature-prd` changed after its last run (regex red line instead of an LLM judge, four failure paths). The shared backbones are in [`foundations/`](foundations/). See [PRD.md](PRD.md) for the full plan.

## What makes it different

1. **Tested.** Every skill ships with eval cases run by `claude plugin eval`, with and without the skill, and a visible pass rate. A skill without a passing suite stays in `drafts/`. [How a skill is evaluated](docs/evaluation.md), with diagrams.
2. **Compliance as skills.** AI Act classification, DPIA pre-screen, CSE consultation, model card, incident playbook — checklists and questions, inside the agent.
3. **A spine.** Every skill plugs into two shared backbones: the **autonomy ladder** (L0 to L5) and the **ROI model** (volume × quality × value).
4. **Lived.** Every rule comes from a real deployment; eval cases are anonymised real briefs.

## Catalog

26 skills planned across 7 stages, hard cap 30. **Available** skills are in `skills/` with a passing eval suite; **planned** ones are in the [PRD](PRD.md#9-skill-catalog--26-skills-across-7-stages) or in `drafts/`.

### Available

| Skill | Stage | What it does |
| --- | --- | --- |
| [`llm-feature-prd`](skills/llm-feature-prd/SKILL.md) | Specify | PRD for an LLM feature: autonomy level per step, four failure paths, eval stub, guardrails, outcome KPIs, shadow → canary → GA. |
| [`build-evals`](skills/build-evals/SKILL.md) | Measure | Builds or reviews the eval set, graders, threshold and baseline that decide if an AI feature is good enough. |
| [`assistant-kpis-cost-per-outcome`](skills/assistant-kpis-cost-per-outcome/SKILL.md) | Measure | KPIs for an assistant or agent: quality by domain, adoption, cost per correct outcome, not usage alone. |
| [`conversation-analysis`](skills/conversation-analysis/SKILL.md) | Measure | Classifies conversations by use case, resolution and sentiment, PII masked, to learn what people use the assistant for. |
| [`ai-act-classification`](skills/ai-act-classification/SKILL.md) | Govern | EU AI Act role, risk category, obligations and dated questions for counsel. Never a compliance verdict. |
| [`cse-consultation`](skills/cse-consultation/SKILL.md) | Govern | Whether an AI tool in a French company needs CSE information or consultation, and the file to prepare. |

### Planned

| Stage | Skills |
| --- | --- |
| Strategy | `ai-opportunity-assessment` (AI or not, in which form) · `ai-initiative-pitch` (one-pager with anchored numbers and one dated ask) · `ai-moat-7-powers` (where defensibility lies when the model is a commodity) |
| Specify | `ai-data-requirements` (fields, quality bar, legal basis, owner) · `chat-with-your-data-scoping` (bounded text-to-SQL with a golden set) · `ai-interaction-patterns` (trust calibration, correction, refusal UX) |
| Data & Knowledge | `semantic-layer-design` (one definition and one owner per metric) · `agent-knowledge-base` (source register, owners, expiry) |
| Build | `prd-to-claude-code` (brief an agentic coding tool) · `system-prompt-and-guardrails` (prompt plus input, output and action guardrails) · `agent-design-and-tooling` (loop, tools, permission matrix) |
| Measure | `model-selection` (cost per success on your suite, sovereignty as a filter) · `release-to-production` (shadow, canary, A/B) · `ai-roi-quantification` (volume × quality × value − costs) |
| Govern | `dpia-prescreen` (the nine EDPB criteria) · `model-card-ai-registry` · `ai-incident-playbook` |
| Transform | `process-ai-redesign` (flagship: level per step, gates, three scenarios) · `ai-adoption-plan` · `ai-literacy-program` (AI Act art. 4) |

Wave 2 is written and waiting for its paid eval run in [`drafts/`](drafts/): `ai-opportunity-assessment`, `ai-initiative-pitch`, `model-selection`, `system-prompt-and-guardrails`, `agent-knowledge-base`, `process-ai-redesign`. Their graders already pass the free checks.

> **Not legal advice.** Govern skills produce classifications, checklists and questions for counsel, never a conformity verdict.

## Install

Claude Code: clone the repo and point your skills directory at `skills/`. Other agents: via the Agent Skills standard. Verified install matrix will land with Wave 1.

## Contributing a skill

```bash
cp -r templates/skill drafts/<your-skill-name>
pip install pyyaml   # node is needed too
python3 scripts/validate_skills.py
```

The validator checks the frontmatter, the fixed body headings and the eval cases (PRD §7.2 and §11.1), and tests the graders for free against a good and a bad answer per case. [docs/evaluation.md](docs/evaluation.md) explains the whole evaluation process with diagrams. CI runs it on every push and pull request. To score a skill (paid, uses your Claude credentials):

```bash
claude plugin eval drafts/<your-skill-name> --runs 1
```

## License

Code (`scripts/`, `.github/`, `.claude-plugin/`) is MIT. Skills, foundations and docs are [CC BY 4.0](LICENSE-CC-BY-4.0): reuse and adapt them, with credit. See [LICENSE](LICENSE).
