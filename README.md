<p align="center"><img src="assets/banner.svg" alt="AI PM Skills: Specify, Evaluate, Prove" width="100%"></p>

<p align="center"><b>Evals as evidence.</b> Agent Skills that help AI product managers prove a feature works, what each correct answer costs, and what the regulator will ask for. Every skill is scored with and without it, against its own template, and by a blind judge; all three are published, including where the gain is small.</p>

<!-- gains:start -->
| Same cases, Sonnet 5.5 answering | Model alone | Skill's template only | With the skill | Gain over the model alone | Gain over the template |
| --- | --- | --- | --- | --- | --- |
| Regex graders: 5 skills, 17 cases × 3 runs | 39% | 82% | **99%** | +60 [+51, +68] | +17 [+9, +26] |
| Blind LLM judge, Haiku 5.5: 4 of these skills, 14 cases, not calibrated | 71% | 78% | 81% | +10 [+6, +14] | +3 [+1, +5] |
| Blind LLM judge, Sonnet 5.5: 4 of these skills, 14 cases, not calibrated | 70% | 76% | 82% | +11 [+6, +17] | +5 [+3, +7] |
| Red lines held (the one thing the answer must never do) | 54% | 90% | **100%** | | |
| Stays silent on near-miss requests | — | — | **100%** | | |

<sub>Sonnet 5.5 answers each case 3 times per arm. **Regex graders** check that the answer contains what the skill asks for; the skills' author wrote them, so they favour the skill. The **blind LLM judge** scores general quality without knowing the arm; it is not calibrated on human scores yet, tends to favour longer answers, and never grades the legal skills. Gains in points; brackets: 95% interval from resampling the cases, which shows how much the gain depends on the cases written, not on the graders chosen. [How the skills are tested](docs/testing-approach.md) · [per-skill numbers](skill-eval-gains.md).</sub>
<!-- gains:end -->

## Why evals as evidence?

In a bank or an insurer, "is it good enough?" is not a feeling. Three readers ask for proof, and each asks a different question:

| Reader | Asks | Answered by |
| --- | --- | --- |
| The user, and the team that serves them | Does it give correct answers on the questions people really ask? | `error-analysis`, `build-evals`, `llm-judge-calibration`, `production-evals-monitoring` |
| The sponsor | What does one correct answer cost, and is it worth it? | `assistant-kpis-cost-per-outcome`, `ai-roi-quantification`, `model-selection` |
| The regulator, the auditor, counsel | Were the bars set before testing? Are the test data representative? Is performance watched after release? | `ai-act-classification`, `model-card-ai-registry`, `production-evals-monitoring` |

Engineering courses teach how to build evals. These skills encode the decisions around them, the way a PM has to take them in a regulated company: read real outputs before choosing metrics, validate a judge with TPR and TNR rather than raw agreement, give every score its number of cases and its interval, set thresholds per class before the run, gate an agent on pass^k, and turn the AI Act articles that ask for testing and monitoring (arts. 9, 10, 15, 17, 26, 72, 73) into a checklist for counsel, never a verdict. The frame fits on one page: [evals as evidence](foundations/evals-as-evidence.md); the numbers behind it on another: [eval statistics](foundations/eval-statistics.md).

What makes it different:

1. **Evaluation is the spine.** Eleven of the 27 skills evaluate: error analysis, judge validation, synthetic data, agents, retrieval, vendors, release and production monitoring.
2. **Tested, and the unfavourable results stay visible.** A skill that does not beat the model alone by at least 10 points stays in `drafts/`. The table above also sets each skill against its own output template and a blind judge, with 95% intervals. [How a skill is evaluated](docs/evaluation.md).
3. **One AI Act skill, wired to the evidence.** `ai-act-classification` names the role, the risk category and the obligations, then maps each testing or monitoring duty to the eval artefact that answers it.
4. **No free-floating numbers.** Every gain traces to volume × quality × unit value − costs ([ROI model](foundations/roi-model.md)), and every autonomy step to the [ladder](foundations/autonomy-ladder.md) (L0 to L5).

## Three blocks

<p align="center"><img src="assets/lifecycle.svg" alt="Three blocks, Specify, Evaluate and Prove, with their skills, marked tested or draft" width="100%"></p>

| You need to… | Run | Block |
| --- | --- | --- |
| Write the PRD of a feature that generates, extracts, classifies or acts | `/ai-pm-skills:llm-feature-prd` | Specify |
| Decide whether the feature is good enough to ship | `/ai-pm-skills:build-evals` | Evaluate |
| Find out what people really ask the assistant, and how it goes | `/ai-pm-skills:conversation-analysis` | Evaluate |
| Show the comex whether the assistant helps, and what a correct answer costs | `/ai-pm-skills:assistant-kpis-cost-per-outcome` | Prove |
| Classify a use case under the EU AI Act and list the evidence it asks for | `/ai-pm-skills:ai-act-classification` | Prove |

You rarely need the command: skills load on their own when the request matches. The other 22 skills are drafts: written, checked for structure and graders, not yet scored over three runs. They stay in [`drafts/`](drafts/) until they pass.

**Looking for discovery, roadmaps or positioning?** Not here on purpose: they read the same with or without AI, and Teresa Torres, Marty Cagan or [pm-skills](https://github.com/phuryn/pm-skills) already cover them. **Looking for how to build an eval harness?** Hamel Husain and Shreya Shankar's [evals course and skills](https://github.com/ai-evals-course/evals-skills) are the engineering reference; this repo is the decision side and credits them.

## Install

Claude Code, no clone needed. Add the marketplace once:

```bash
claude plugin marketplace add alexandre-darmon/ai-pm-skills
```

Then install every tested skill:

```bash
claude plugin install ai-pm-skills@ai-pm-skills
```

Or a single skill, by its name:

```bash
claude plugin install build-evals@ai-pm-skills
```

Each per-skill plugin is named after its skill: `llm-feature-prd`, `build-evals`, `conversation-analysis`, `assistant-kpis-cost-per-outcome`, `ai-act-classification`. Pick the bundle or single skills, not both. A skill's full text loads only when it fires. Drafts are not installable: they join the marketplace once they pass their eval run.

Other agents (Codex, Cursor, custom): each folder in `skills/` follows the [Agent Skills](https://agentskills.io) standard and is self-contained, so the skills CLI can install it:

```bash
npx skills add alexandre-darmon/ai-pm-skills
```

Not yet verified on every agent; copying a folder into your agent's skills directory also works.

## Catalog

27 skills in three blocks, hard cap 30. **Available** skills are in `skills/` with a passing eval suite. **Drafts** are written and pass the free checks, and are not installable yet.

### Available

| Skill | Block | What it does |
| --- | --- | --- |
| [`llm-feature-prd`](skills/llm-feature-prd/SKILL.md) | Specify | PRD for an LLM feature: autonomy level per step, four failure paths, eval stub, guardrails, outcome KPIs, stop conditions. |
| [`build-evals`](skills/build-evals/SKILL.md) | Evaluate | Eval set, graders, per-class thresholds signed before the run, judge validated with TPR and TNR, scores with intervals, baseline. |
| [`conversation-analysis`](skills/conversation-analysis/SKILL.md) | Evaluate | Classifies conversations by use case, resolution and sentiment, PII masked, to learn what people use the assistant for. |
| [`assistant-kpis-cost-per-outcome`](skills/assistant-kpis-cost-per-outcome/SKILL.md) | Prove | KPIs for an assistant or agent: quality by domain, adoption, cost per correct outcome, not usage alone. |
| [`ai-act-classification`](skills/ai-act-classification/SKILL.md) | Prove | EU AI Act role, risk category, obligations, the eval evidence each article asks for, and dated questions for counsel. Never a compliance verdict. |

### Drafts

| Block | Skills |
| --- | --- |
| Specify | `ai-opportunity-assessment` (AI or not, in which form, the dated ask and its stop conditions) · `ai-data-requirements` (fields, quality bar, legal basis, owner) · `chat-with-your-data-scoping` (bounded text-to-SQL with a golden set) · `ai-interaction-patterns` (trust calibration, correction, refusal UX) · `system-prompt-and-guardrails` (prompt plus input, output and action guardrails) · `agent-design-and-tooling` (loop, tools, permission matrix) · `agent-knowledge-base` (source register, owners, expiry) · `semantic-layer-design` (one definition and one owner per metric) · `process-ai-redesign` (level per step, gates, scenarios) |
| Evaluate | `error-analysis` (read traces, find failure modes before metrics) · `llm-judge-calibration` (TPR, TNR, bias checks, corrected pass rate, with a script) · `synthetic-eval-data` (dimensions, tuples, synthetic share declared) · `agent-evals` (end state, forbidden events, pass^k) · `retrieval-evaluation` (retrieval apart from generation) · `model-selection` (cost per success on your suite) · `ai-vendor-evaluation` (bake-off on your cases, clauses that keep quality testable) · `release-to-production` (shadow, canary, A/B) · `production-evals-monitoring` (online evals, control limits, AI Act art. 72 plan) |
| Prove | `ai-roi-quantification` (volume × quality × value − costs) · `model-card-ai-registry` (the eval record per version) · `ai-incident-playbook` (incident to regression case, art. 73) · `ai-adoption-plan` (adoption proven on outcomes, AI literacy evidence) |

> **Not legal advice.** Skills marked legal (`ai-act-classification` and the drafts that map the AI Act, DORA or GDPR) produce classifications, checklists and questions for counsel, never a conformity verdict.

## Contributing a skill

```bash
cp -r templates/skill drafts/<your-skill-name>
pip install pyyaml   # node is needed too; Python 3.10 or later
python3 scripts/validate_skills.py
```

The validator checks the frontmatter, the fixed body headings and the eval cases (PRD §7.2 and §11.1), and tests the graders for free against a good and a bad answer per case. [docs/evaluation.md](docs/evaluation.md) explains the whole evaluation process with diagrams. CI runs it on every push and pull request. To score a skill (paid, uses your Claude credentials):

```bash
claude plugin eval drafts/<your-skill-name> --runs 1
```

After a scoring run is frozen in `baselines/`, refresh the numbers above and [skill-eval-gains.md](skill-eval-gains.md):

```bash
python3 scripts/eval_gains.py
```

## Built on the work of

The skills cite these works by idea, in their own words ([full register](foundations/sources.md)):

- **Evaluation.** Hamel Husain and Shreya Shankar, [*AI Evals for Engineers and PMs*](https://maven.com/parlance-labs/evals) and their evals FAQ on [hamel.dev](https://hamel.dev) · Shankar et al., [*Who Validates the Validators?*](https://arxiv.org/abs/2404.12272) · Zheng et al., [*Judging LLM-as-a-Judge*](https://arxiv.org/abs/2306.05685) · Eugene Yan, [*Evaluating the Effectiveness of LLM-Evaluators*](https://eugeneyan.com/writing/llm-evaluators/) · Evan Miller, [*Adding Error Bars to Evals*](https://arxiv.org/abs/2411.00640) · Anthropic, [*Demystifying evals for AI agents*](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) · Yao et al., [*τ-bench*](https://arxiv.org/abs/2406.12045) · Es et al., [*RAGAS*](https://arxiv.org/abs/2309.15217) · Manning, Raghavan, Schütze, [*Introduction to Information Retrieval*](https://nlp.stanford.edu/IR-book/)
- **Statistics.** Wilson (1927) and the rule of three · Rogan and Gladen (1978) on correcting a rate with a test's errors · Cohen's kappa (1960) · Efron and Tibshirani, *An Introduction to the Bootstrap* · Montgomery, *Introduction to Statistical Quality Control* · Kohavi, Tang, Xu, [*Trustworthy Online Controlled Experiments*](https://experimentguide.com)
- **Product.** Marty Cagan, [*Inspired*](https://svpg.com) · Teresa Torres, [*Continuous Discovery Habits*](https://www.producttalk.org) · Rob Fitzpatrick, [*The Mom Test*](https://www.momtestbook.com)
- **AI engineering and operations.** Anthropic, [*Building effective agents*](https://www.anthropic.com/engineering/building-effective-agents) · OWASP, [*Top 10 for LLM Applications*](https://genai.owasp.org/llm-top-10/) · Mitchell et al., [*Model Cards for Model Reporting*](https://arxiv.org/abs/1810.03993) · [OpenTelemetry GenAI conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) · Beyer et al., [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/) · Microsoft, [*Guidelines for Human-AI Interaction*](https://www.microsoft.com/en-us/haxtoolkit/) · Google, [*People + AI Guidebook*](https://pair.withgoogle.com/guidebook/)
- **Regulation.** [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) as amended by Regulation (EU) 2026/1744 · [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) · EN 18286 (quality management for the AI Act)

## Author

Alex Darmon, AI and data product manager in banking and retail, with an analytics and observability background. The skills come from client missions on internal assistants, chat-with-your-data products and agents; client data never leaves the client. Writing at [aiunmagic.com](https://aiunmagic.com).

## License

Code (`scripts/`, `.github/`, `.claude-plugin/`) is MIT. Skills, foundations and docs are [CC BY 4.0](LICENSE-CC-BY-4.0): reuse and adapt them, with credit. See [LICENSE](LICENSE).
