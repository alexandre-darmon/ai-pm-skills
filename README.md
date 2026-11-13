<p align="center"><img src="assets/banner.svg" alt="AI PM Skills: Specify, Build, Evaluate, Prove" width="100%"></p>

<p align="center"><b>Evals as evidence.</b> Agent Skills that help AI product managers build to learn, then prove a feature works, what each correct answer costs, and what the regulator will ask for. Every skill is scored with and without it, against its own template, and by a blind judge; all three are published, including where the gain is small.</p>

<!-- gains:start -->
| Same cases, Sonnet 5.5 answering | Model alone | Skill's template only | With the skill | Gain over the model alone | Gain over the template |
| --- | --- | --- | --- | --- | --- |
| Regex graders: 29 skills, 109 cases × 3 runs | 52% | 82% | **96%** | +45 [+41, +48] | +17 [+6, +32] |
| Blind LLM judge, Haiku 5.5: 5 of these skills, 17 cases, earlier runs, not calibrated | 71% | 78% | 80% | +10 [+6, +13] | +3 [+1, +5] |
| Blind LLM judge, Sonnet 5.5: 5 of these skills, 17 cases, earlier runs, not calibrated | 69% | 76% | 80% | +11 [+6, +17] | +5 [+3, +7] |
| Red lines held (the one thing the answer must never do) | 71% | 88% | **100%** | | |
| Cost per correct answer, API equivalent (22 skills) | $0.097 | — | **$0.076** | -22% | |
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

1. **Evaluation is the spine.** Thirteen of the 29 skills evaluate: error analysis, judge validation, synthetic data, agents, retrieval, attacks, whole conversations, vendors, release and production monitoring.
2. **Built for a PM who builds.** The Build block covers what a PM makes with a coding agent to get evidence (a feasibility spike, a prompt with its red-team set, an agent's tools, a trace review app) and the handover of that prototype into a bank's IT estate, where engineers own production.
3. **Tested, and the unfavourable results stay visible.** A skill that does not beat the model alone by at least 10 points stays in `drafts/`. The table above also sets each skill against its own output template and a blind judge, with 95% intervals. [How a skill is evaluated](docs/evaluation.md).
4. **One AI Act skill, wired to the evidence.** `ai-act-classification` names the role, the risk category and the obligations, then maps each testing or monitoring duty to the eval artefact that answers it.
5. **No free-floating numbers.** Every gain traces to volume × quality × unit value − costs ([ROI model](foundations/roi-model.md)), and every autonomy step to the [ladder](foundations/autonomy-ladder.md) (L0 to L5).

## Four blocks, one loop

<p align="center"><img src="assets/lifecycle.svg" alt="Four blocks in a loop, Specify, Build, Evaluate and Prove, with their skills, marked tested or draft" width="100%"></p>

| Block | What it answers | You | The coding agent | AI engineers |
| --- | --- | --- | --- | --- |
| **Specify** | Should we use AI, what must it do, what does "correct" mean? | decide and sign the bar per class | drafts the PRD from your notes | review feasibility |
| **Build** | Can the model do it, at what cost per correct answer, and what does the prototype become? | set the question, the cases, the appetite and the kill date | writes the spike, the review app, the scripts; another session reviews them | own production code: integration, access, secrets, logging, hosting |
| **Evaluate** | Does it work, before and after release, with an interval on every score? | label, set thresholds before the run, read the failures | runs the suite and the scripts | run the pipeline and the monitoring |
| **Prove** | What does a correct answer cost, and what will the regulator ask for? | take the evidence to the sponsor and counsel | assembles the record | keep the logs the record cites |

**AI Builder**, as used here: a PM who builds prototypes, eval tooling and evidence with a coding agent; engineers build to earn, and own production. Build to learn is framed on one page: [build to learn](foundations/build-to-learn.md). Production failures and incidents come back as regression cases and new requirements, which is why the blocks form a loop.

Three ways in:

- **An idea:** `ai-opportunity-assessment` → `ai-feasibility-spike` → `llm-feature-prd`.
- **Is it good enough?** `trace-review-tool` → `error-analysis` → `build-evals` → `llm-judge-calibration`.
- **Ship it:** `prototype-handover` → `release-to-production` → `model-card-ai-registry`.

| You need to… | Run | Block |
| --- | --- | --- |
| Decide whether an AI idea is worth a PRD, and what to ask the sponsor | `/ai-pm-skills:ai-opportunity-assessment` | Specify |
| Write the PRD of a feature that generates, extracts, classifies or acts | `/ai-pm-skills:llm-feature-prd` | Specify |
| Test on the real model whether an idea holds, before writing the PRD | `/ai-pm-skills:ai-feasibility-spike` | Build |
| Decide what a prototype you built becomes: rebuilt, registered or retired | `/ai-pm-skills:prototype-handover` | Build |
| Find out how the feature really fails before choosing any metric | `/ai-pm-skills:error-analysis` | Evaluate |
| Decide whether the feature is good enough to ship | `/ai-pm-skills:build-evals` | Evaluate |
| Know whether an LLM judge can be trusted | `/ai-pm-skills:llm-judge-calibration` | Evaluate |
| Test an agent before it acts alone | `/ai-pm-skills:agent-evals` | Evaluate |
| Find out whether a RAG fails at retrieval or at generation | `/ai-pm-skills:retrieval-evaluation` | Evaluate |
| Choose an AI vendor on your own evidence | `/ai-pm-skills:ai-vendor-evaluation` | Evaluate |
| Show the comex whether the assistant helps, and what a correct answer costs | `/ai-pm-skills:assistant-kpis-cost-per-outcome` | Prove |
| Classify a use case under the EU AI Act and list the evidence it asks for | `/ai-pm-skills:ai-act-classification` | Prove |

You rarely need the command: skills load on their own when the request matches. The full list is in the [catalog](#catalog).

**Looking for discovery, roadmaps or positioning?** Not here on purpose: they read the same with or without AI, and Teresa Torres, Marty Cagan or [pm-skills](https://github.com/phuryn/pm-skills) already cover them. **Looking for how to build an eval harness?** Hamel Husain and Shreya Shankar's [evals course and skills](https://github.com/ai-evals-course/evals-skills) are the engineering reference; this repo is the decision side and credits them.

## How well the skills work

<p align="center"><img src="assets/evals.svg" alt="Per catalog skill: regex score of the model alone and with the skill" width="100%"></p>

- **Every skill is scored twice on the same cases**, with and without it, three runs per case. It enters the catalog only if it clears its threshold in every case, holds every red line in every run, and beats the model alone by at least 10 points. The numbers shown are those of its last recorded run, kept pass or fail with a log of every run; the validator fails the build if a catalog skill's text or cases changed since that run, so no number here describes a text that is not the one you install.
- **The right skill fires when all 29 are installed.** A routing suite of 58 requests aimed at the known collision zones (spike vs opportunity vs model choice, eval set vs release, handover vs model card vs AI Act, attack campaign vs guardrails vs agent tests, whole conversations vs single answers, and out-of-scope requests) picked the expected skill, or none, in 172 of 174 runs on 2026-11-12; the 2 misses fired no skill at all ([results](routing/results-2026-11-12b.md)). The requests were written by the repo's author, so this rules out collisions on known pairs, not on every phrasing. A free lexical check (`scripts/routing_check.py`) guards the same cases on every push.
- **Three ways of scoring, side by side**, in the table at the top: regex graders, the skill's own template as a control, and a blind LLM judge. The judge sees a much smaller gain than the regexes; that is published, not hidden.
- **What we fix when a run fails**: in the November 2026 runs, most failures were graders refusing correct wording, not weak skills. Every grader change is checked against the answers given without the skill, and real answers become fixtures. Two skills held the exact numbers their own cases asked for; they were rewritten. Details: [how the skills are tested](docs/testing-approach.md) and [per-skill numbers](skill-eval-gains.md).

## Install

Every folder in `skills/` follows the [Agent Skills](https://agentskills.io) standard and is self-contained (its `references/`, `templates/` and `scripts/` sit inside it), so any agent that reads `SKILL.md` folders can load it. The evals were run with Claude (Sonnet 5.5): other agents may pick and follow the skills differently, and the numbers above do not carry over to them. Each skill folder also holds its eval cases in `evals/`, which the agent never needs; the [release zips](https://github.com/alexandre-darmon/ai-pm-skills/releases/latest) leave them out.

**Fastest path, most agents, one command** ([skills CLI](https://github.com/vercel-labs/skills), third-party, not vendor-official):

```bash
npx skills add alexandre-darmon/ai-pm-skills --list                 # see the 29 skills
npx skills add alexandre-darmon/ai-pm-skills --skill build-evals     # one skill
npx skills add alexandre-darmon/ai-pm-skills --skill '*'             # all of them
```

Prefer your tool's own installer? Pick it below. Sources, paths and what is not yet tested: [docs/install.md](docs/install.md).

<details>
<summary><b>Claude Code (recommended)</b></summary>

No clone needed. Add the marketplace once:

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

Each per-skill plugin is named after its skill (see the [catalog](#catalog)). Pick the bundle or single skills, not both. A skill's full text loads only when it fires. Drafts are not installable: they join the marketplace once they pass their eval run.

**Pin a version.** Add the marketplace at a tag and it stays on that tag until you add it again: `claude plugin marketplace add alexandre-darmon/ai-pm-skills#v1.1.0`. Without a tag you follow `main`; refresh with `claude plugin marketplace update ai-pm-skills`, then `claude plugin update ai-pm-skills@ai-pm-skills`. What changed between versions: [CHANGELOG](CHANGELOG.md).

**Roll it out in your company.**

- **Claude Code**: an admin registers the marketplace pinned to a tag in managed settings (`extraKnownMarketplaces`, source `alexandre-darmon/ai-pm-skills` with `ref` set to the tag) and turns on the plugins people should have (`enabledPlugins`). `strictKnownMarketplaces` keeps everything else out. See the [organisation guide](https://code.claude.com/docs/en/plugins/org.md).
- **Before rollout**: each skill's eval record (`baselines/<skill>.json`) is the evidence your model risk or IT risk reviewer can read. The legal skills give checklists and questions for counsel, never a verdict.

</details>

<details>
<summary><b>claude.ai, the Claude apps, the Skills API</b></summary>

Download a skill's zip from the [latest release](https://github.com/alexandre-darmon/ai-pm-skills/releases/latest) and upload it under Customize > Skills. Each zip is one skill folder without its eval cases, with its licence; `SHA256SUMS` lists the checksums. One zip per skill.

**claude.ai Team or Enterprise**: an owner uploads the release zips under Organization settings > Plugins & skills and chooses who gets each skill.

</details>

<details>
<summary><b>OpenAI Codex (CLI, IDE extension, ChatGPT desktop app)</b></summary>

Codex reads skill folders natively from `.agents/skills/` in your project (walking up to the repo root) and `~/.agents/skills/` for your user ([docs](https://learn.chatgpt.com/docs/build-skills)). Copy one skill or all of them:

```bash
git clone https://github.com/alexandre-darmon/ai-pm-skills.git
mkdir -p ~/.agents/skills
cp -r ai-pm-skills/skills/build-evals ~/.agents/skills/   # one skill, user scope
cp -r ai-pm-skills/skills/* ~/.agents/skills/            # all 29
```

For one project, copy into `<your-repo>/.agents/skills/` instead. Or unzip a release zip there: `unzip build-evals-<version>.zip -d ~/.agents/skills/`. Codex picks up changes on its own (restart it if one does not show); update with `git pull` and copy again. Invoke with `$build-evals` or `/skills`, or let the description trigger it.

**From GitHub, inside Codex**: ask the bundled `$skill-installer` to install `skills/build-evals` from `alexandre-darmon/ai-pm-skills` (optionally at ref `v1.1.0`). It writes to `$CODEX_HOME/skills/` (default `~/.codex/skills/`), which is not among the skill locations the Codex skills docs list, so the copy into `~/.agents/skills/` above is the documented route. It installs one path per skill and stops if the folder already exists, so delete it before reinstalling ([installer](https://github.com/openai/skills/blob/main/skills/.system/skill-installer/SKILL.md)).

**As a Codex plugin (all 29)**: the repo ships `.agents/plugins/marketplace.json` and `.codex-plugin/plugin.json`.

```bash
codex plugin marketplace add alexandre-darmon/ai-pm-skills
codex plugin marketplace upgrade ai-pm-skills    # later, to refresh
```

Then run `codex`, open `/plugins` and install `ai-pm-skills`, or use the Plugins tab in the desktop app, and start a new session ([docs](https://developers.openai.com/codex/plugins/build/)). The Codex manifests are newer than v1.1.0: follow `main` until the next release, then pin with `--ref <tag>`.

> Limits: the IDE extension does not support plugins, only skill folders. The plugin route installs the bundle, not single skills, and has not been tested on this repo yet; Codex does not document a plugin source rooted at the marketplace root (`./`), which is what this repo uses. ChatGPT on the web can take uploaded skills (Skills > Create > Upload from your computer, if your workspace admin allows it), but the zip layout it expects is not confirmed in a doc we could read.

</details>

<details>
<summary><b>Cursor</b></summary>

Cursor reads skill folders natively ([docs](https://cursor.com/docs/context/skills)): project `.agents/skills/` or `.cursor/skills/`, user `~/.agents/skills/` or `~/.cursor/skills/`. It also reads `.claude/skills/` and `~/.claude/skills/`.

```bash
git clone https://github.com/alexandre-darmon/ai-pm-skills.git
mkdir -p ~/.cursor/skills
cp -r ai-pm-skills/skills/build-evals ~/.cursor/skills/   # one skill
cp -r ai-pm-skills/skills/* ~/.cursor/skills/            # all 29
```

Or `npx skills add alexandre-darmon/ai-pm-skills --skill build-evals -a cursor`. Skills are found at startup: restart Cursor after a copy or an update (`git pull`, copy again).

> Limits: this repo does not ship a `.cursor-plugin/marketplace.json`, so the "From GitHub Repository" import and team marketplaces do not apply yet.

</details>

<details>
<summary><b>GitHub Copilot (VS Code, Copilot CLI, cloud agent)</b></summary>

With GitHub CLI 2.90.0 or later, `gh skill` (public preview) installs from this repo as it is ([manual](https://cli.github.com/manual/gh_skill_install)):

```bash
gh skill install alexandre-darmon/ai-pm-skills build-evals                 # one skill, project scope
gh skill install alexandre-darmon/ai-pm-skills --all --scope user          # all 29, for you
gh skill install alexandre-darmon/ai-pm-skills build-evals@v1.1.0          # pinned to a tag
gh skill update --all                                                      # later
```

Copilot reads `.github/skills/`, `.claude/skills/` or `.agents/skills/` in a project and `~/.copilot/skills/` or `~/.agents/skills/` for your user, so a manual copy works too ([docs](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)).

**Copilot CLI plugin**: the CLI reads this repo's `.claude-plugin/marketplace.json` ([reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference)).

```bash
copilot plugin marketplace add alexandre-darmon/ai-pm-skills
copilot plugin install ai-pm-skills@ai-pm-skills
copilot plugin update ai-pm-skills
```

> Limits: `gh skill` is in preview and copies the whole folder, `evals/` included. Copilot documents the `strict` and `skills` fields this repo's marketplace entries use, but neither the bundle nor the single-skill plugins (`build-evals@ai-pm-skills`) have been tested on this repo.

</details>

<details>
<summary><b>Gemini CLI</b></summary>

No manifest needed for skills ([docs](https://geminicli.com/docs/cli/skills/)):

```bash
gemini skills install https://github.com/alexandre-darmon/ai-pm-skills.git --path skills/build-evals   # one skill
gemini skills install https://github.com/alexandre-darmon/ai-pm-skills.git --path skills               # all 29
```

Default scope is your user (`~/.gemini/skills/`); add `--scope workspace` for the current project. There is no skills update command: run the install again (it replaces the folder), then `/skills reload`.

**As an extension (all 29, with updates)**: the repo ships `gemini-extension.json` ([docs](https://geminicli.com/docs/extensions/reference/)).

```bash
gemini extensions install https://github.com/alexandre-darmon/ai-pm-skills
gemini extensions update ai-pm-skills
```

> Limits: `gemini-extension.json` is newer than v1.1.0, so pin with `--ref <tag>` only from the next release. Google replaced Gemini CLI with Antigravity CLI for unpaid-tier and Google One users on June 18, 2026; on those plans, use Antigravity. Installing all skills with `--path skills` follows from the CLI's source code, not its docs.

</details>

<details>
<summary><b>Google Antigravity (IDE, App, CLI)</b></summary>

**CLI, all 29 as a plugin**: the repo ships `.antigravity-plugin/plugin.json` ([docs](https://antigravity.google/docs/plugins?tab=cli)).

```bash
agy plugin install https://github.com/alexandre-darmon/ai-pm-skills
```

Skills then appear as `/<skill>` (for example `/build-evals`), with no plugin prefix ([docs](https://antigravity.google/docs/build-plugins/)). There is no documented update command: uninstall (`agy plugin uninstall ai-pm-skills`) and install again.

**IDE, App or CLI, one skill**: copy the folder; the IDE has no install command ([docs](https://antigravity.google/docs/skills)).

```bash
git clone https://github.com/alexandre-darmon/ai-pm-skills.git
mkdir -p ~/.gemini/config/skills
cp -r ai-pm-skills/skills/build-evals ~/.gemini/config/skills/   # user scope
```

For one project, copy into `<project>/.agents/skills/`. In the CLI, run `/skills reload` or start a new conversation.

> Limits: `.antigravity-plugin/plugin.json` is newer than v1.1.0. The plugin install has no documented tag pinning or scope flag, and the plugin docs are recent and still changing. Not tested on this repo yet.

</details>

<details>
<summary><b>Windsurf (now Devin Desktop and Devin CLI)</b></summary>

Windsurf's docs now redirect to Devin's. The CLI installs this repo as a skills-only plugin, all 29 at once, after `devin auth login` ([docs](https://docs.devin.ai/cli/extensibility/plugins/overview)):

```bash
devin plugins install alexandre-darmon/ai-pm-skills
devin plugins update ai-pm-skills
```

Skills are then invoked as `/ai-pm-skills:<skill>`. A plugin cannot install a single skill: for one, copy its folder into `.devin/skills/` or `.agents/skills/` (project, legacy `.windsurf/skills/`) or `~/.config/devin/skills/` or `~/.agents/skills/` (user) ([docs](https://docs.devin.ai/desktop/devin-local/customizations)).

> Limits: the plugin route is not tested on this repo yet.

</details>

<details>
<summary><b>Kiro (IDE and CLI)</b></summary>

Kiro reads `.kiro/skills/` (workspace) and `~/.kiro/skills/` (global) ([docs](https://kiro.dev/docs/skills/)). In the IDE, open Agent Steering & Skills, click +, choose Import a skill > GitHub and paste one skill's folder URL, for example `https://github.com/alexandre-darmon/ai-pm-skills/tree/main/skills/build-evals`. From a terminal, copy or use `gh skill`:

```bash
mkdir -p ~/.kiro/skills && cp -r ai-pm-skills/skills/build-evals ~/.kiro/skills/   # one skill, from a clone
gh skill install alexandre-darmon/ai-pm-skills --all --dir .kiro/skills          # all 29, this workspace
```

> Limits: one skill per import, no update mechanism (import again). Custom agents load skills only if their `resources` include `skill://.kiro/skills/*/SKILL.md`.

</details>

<details>
<summary><b>OpenCode</b></summary>

OpenCode reads `.opencode/skills/`, `.agents/skills/` and `.claude/skills/` in a project, and `~/.config/opencode/skills/`, `~/.agents/skills/` and `~/.claude/skills/` for your user, so skills installed for Claude Code show up too ([docs](https://opencode.ai/docs/skills/)). It has no install command:

```bash
npx skills add alexandre-darmon/ai-pm-skills --skill build-evals -a opencode -g   # one skill, user scope
mkdir -p ~/.config/opencode/skills
cp -r ai-pm-skills/skills/* ~/.config/opencode/skills/                          # all 29, from a clone
```

Update with `npx skills update` or copy again.

</details>

<details>
<summary><b>Command Code</b></summary>

([docs](https://commandcode.ai/docs/skills))

```bash
cmd skills add alexandre-darmon/ai-pm-skills -s build-evals        # one skill, project (.commandcode/skills/)
cmd skills add alexandre-darmon/ai-pm-skills -s build-evals -g     # one skill, user (~/.commandcode/skills/)
cmd skills add alexandre-darmon/ai-pm-skills                       # pick from a list
```

> Limits: no documented flag to install all skills at once and no update command; `--force` overwrites an installed skill.

</details>

<details>
<summary><b>Other agents (Amp, Goose, Roo Code, Cline, ...)</b></summary>

The [skills CLI](https://github.com/vercel-labs/skills) targets about 70 agents; name yours with `-a`, add `-g` for user scope:

```bash
npx skills add alexandre-darmon/ai-pm-skills --skill build-evals -a amp -g
npx skills update
```

Or copy `skills/<name>/` (or unzip a release zip) into your agent's skills folder:

| Agent | Project | User | Docs |
| --- | --- | --- | --- |
| Amp | `.agents/skills/` | `~/.config/agents/skills/` (also `amp skill add --global alexandre-darmon/ai-pm-skills`) | [ampcode.com](https://ampcode.com/docs/customize/skills) |
| Goose | `.agents/skills/` | `~/.agents/skills/` | [goose-docs.ai](https://goose-docs.ai/docs/guides/context-engineering/using-skills) |
| Roo Code | `.roo/skills/` or `.agents/skills/` | `~/.roo/skills/` or `~/.agents/skills/` | [Roo Code docs](https://roocodeinc.github.io/Roo-Code/features/skills) |
| Cline | `.cline/skills/` | `~/.cline/skills/` | [docs.cline.bot](https://docs.cline.bot/features/skills) |

</details>

## Catalog

<!-- catalog:start -->
29 skills in four blocks, hard cap 30. Each one owns its triggers: no two skills compete for the same request, and the validator flags descriptions that overlap. **Available** skills are in `skills/`: their last recorded run (three runs per case, on today's text and cases) passes, the validator checks it on every push, and they install from the marketplace. **Drafts** are written and pass the free checks, not yet the paid runs.

### Available (29)

| Skill | Block | What it does |
| --- | --- | --- |
| [`ai-opportunity-assessment`](skills/ai-opportunity-assessment/SKILL.md) | Specify | AI or not, in which form, and the dated ask with its stop conditions. |
| [`llm-feature-prd`](skills/llm-feature-prd/SKILL.md) | Specify | PRD for an LLM feature: autonomy level per step, failure paths, eval stub, guardrails, stop conditions. |
| [`process-ai-redesign`](skills/process-ai-redesign/SKILL.md) | Specify | Level per step for a whole process, gates, scenarios with ROI lines, migration path. |
| [`ai-data-requirements`](skills/ai-data-requirements/SKILL.md) | Specify | Fields and documents a feature reads and writes: owners, expiry, flows, lawful basis. |
| [`ai-interaction-patterns`](skills/ai-interaction-patterns/SKILL.md) | Specify | What users see: sources, confidence only when calibrated, correction, refusal, escalation. |
| [`agent-design-and-tooling`](skills/agent-design-and-tooling/SKILL.md) | Build | An agent's loop, tools, permission matrix, stop conditions and traces. |
| [`ai-feasibility-spike`](skills/ai-feasibility-spike/SKILL.md) | Build | A throwaway prototype on the real model: one question, appetite and bar set first, n of N with intervals, cost per correct answer. |
| [`system-prompt-and-guardrails`](skills/system-prompt-and-guardrails/SKILL.md) | Build | System prompt plus input, output and action guardrails, with a red-team set. |
| [`trace-review-tool`](skills/trace-review-tool/SKILL.md) | Build | A thin review app a coding agent builds over masked traces: pass/fail with critique, reviewer and time on every label. |
| [`prototype-handover`](skills/prototype-handover/SKILL.md) | Build | What a PM-built AI tool becomes in a bank: rebuilt, registered at its EUC tier or retired; suite and baseline as the contract. |
| [`build-evals`](skills/build-evals/SKILL.md) | Evaluate | Eval set, graders, per-class thresholds signed before the run, intervals, baseline; per-component checks. |
| [`error-analysis`](skills/error-analysis/SKILL.md) | Evaluate | Read real traces, find and price failure modes before choosing any metric or judge. |
| [`llm-judge-calibration`](skills/llm-judge-calibration/SKILL.md) | Evaluate | Validate an LLM judge with TPR and TNR on held-out labels; correct the rate it reports. |
| [`synthetic-eval-data`](skills/synthetic-eval-data/SKILL.md) | Evaluate | Synthetic inputs from dimensions grounded in real traffic, with the share declared; counterfactual variants. |
| [`agent-evals`](skills/agent-evals/SKILL.md) | Evaluate | End state, forbidden events, pass^k with bounds, prompt injection measured as utility under attack. |
| [`retrieval-evaluation`](skills/retrieval-evaluation/SKILL.md) | Evaluate | RAG evaluated in two stages: retrieval at the k sent, then generation on fixed contexts. |
| [`model-selection`](skills/model-selection/SKILL.md) | Evaluate | Choose a model on your own suite: cost per success, noise test, decision record. |
| [`ai-vendor-evaluation`](skills/ai-vendor-evaluation/SKILL.md) | Evaluate | Buy on your own bake-off: cost per correct outcome, benchmark audit, clauses that keep quality testable. |
| [`red-team-evals`](skills/red-team-evals/SKILL.md) | Evaluate | Plan and read an attack campaign on an assistant or RAG: classes, sizing, rates with intervals, residual-risk record. Never "robust". |
| [`multi-turn-evals`](skills/multi-turn-evals/SKILL.md) | Evaluate | Evaluate whole conversations: scripted and simulated cases, a validated simulator, conversation-level graders, pass^k. |
| [`release-to-production`](skills/release-to-production/SKILL.md) | Evaluate | Ship a change: offline gate, shadow, canary, A/B only if the sample allows. |
| [`production-evals-monitoring`](skills/production-evals-monitoring/SKILL.md) | Evaluate | Quality after release: sampled judges, control limits, owners, and the AI Act art. 72 plan. |
| [`conversation-analysis`](skills/conversation-analysis/SKILL.md) | Evaluate | What people really ask the assistant, and how it goes, with personal data masked first. |
| [`assistant-kpis-cost-per-outcome`](skills/assistant-kpis-cost-per-outcome/SKILL.md) | Prove | KPIs for an assistant or agent: quality by domain, adoption, cost per correct outcome. |
| [`ai-roi-quantification`](skills/ai-roi-quantification/SKILL.md) | Prove | ROI of a live AI product: volume × quality × unit value − costs, baseline, sensitivity. |
| [`ai-act-classification`](skills/ai-act-classification/SKILL.md) | Prove | EU AI Act role, risk category, obligations and the eval evidence each article asks for. Never a verdict. |
| [`model-card-ai-registry`](skills/model-card-ai-registry/SKILL.md) | Prove | The eval record of each version: results per class with intervals, judge, signed thresholds, limits. |
| [`ai-incident-playbook`](skills/ai-incident-playbook/SKILL.md) | Prove | Contain, roll back, report on time, and turn every incident into regression cases before the fix ships. |
| [`ai-adoption-plan`](skills/ai-adoption-plan/SKILL.md) | Prove | Adoption proven on correct outcomes, over-trust measured, training by role, AI Act art. 4 evidence. |
<!-- catalog:end -->

> **Not legal advice.** Skills marked `legal: true` (`ai-act-classification`, `ai-vendor-evaluation`, `model-card-ai-registry`, `production-evals-monitoring`, `ai-incident-playbook`) produce classifications, checklists and questions for counsel, never a conformity verdict.

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

After a recorded run lands in `baselines/`, refresh the numbers above and [skill-eval-gains.md](skill-eval-gains.md):

```bash
python3 scripts/eval_gains.py
python3 scripts/readme_catalog.py
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
