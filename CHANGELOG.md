# Changelog

Each release lists what changed for someone who installs the skills.

**Version numbers.** Major (2.0): a skill is removed or renamed, or an output template changes shape, so installs or downstream documents can break. Minor (1.2): a skill is added, or a skill gains a method step. Patch (1.1.1): wording, graders, docs, manifests. The release version is the same in every manifest; each skill also has its own version in `metadata.version`. Per-skill versions live in each `SKILL.md` (`metadata.version`); eval records and their history are in [`baselines/`](baselines/).

## v1.3.0 (2026-11-13)

Same 29 skills; `ai-act-classification` gains method rules, so a minor release. Release notes: [docs/releases/v1.3.0.md](docs/releases/v1.3.0.md).

- **Legal skills judged too**, on request (`judge_answers.py --include-legal`): GPT-6.1 Sol, Jev and Haiku 5.5 grade the 6 legal skills on the same rubric, information only; it does not check legal correctness, and counsel's review stays the evidence. Five skills gain +3 to +5 (GPT), +8 to +14 (Jev); `ai-act-classification` stays negative for GPT (−11), which marks down the 2026 amendments it does not know.
- **`ai-act-classification`** (0.4.0), from the judges' critiques and a legal review: emotion recognition means inferring emotions from biometric data (art. 3(39), 5(1)(f)); the use sets the Annex III category at every autonomy level, and the levels are the team's scale, not a legal category; art. 26(5) and 26(9) completed; no invented "today" date; the memo names documents, not this repo's skills or files. Rerun: 100% on every case.
- **Evals chart**: next to the regex gain, the gain GPT-6.1 Sol sees on the same answers.
- **README table**: each gain is the row's score with the skill minus the score it is compared with, on the same skills (Haiku: 80% − 71% = +9, was shown +10 from unrounded case means); the template-only control appears only on a row of the skills that have one; the first column is "Test performed".

## v1.2.0 (2026-11-13)

Same 29 skills; four gain method rules, so a minor release. Release notes: [docs/releases/v1.2.0.md](docs/releases/v1.2.0.md).

- **Judges from other vendors.** `judge_answers.py` grades saved answers through OpenRouter (`scripts/openrouter.py`, key in `OPENROUTER_API_KEY` or the git-ignored `.env`): GPT-6.1 Sol (same prompt as the Claude judges) and TypeSafe's Jev decision model, on the recorded runs of the 23 non-legal skills. Both find +9 points with the skill; the regex graders find +45.
- **Four skills improved from the judges' critiques**, each rerun (3 runs, pass) and re-judged: `model-selection` (overlapping intervals no longer read as a tie; ask for the discordant cases), `agent-design-and-tooling` (data scope from the trusted session, a concrete provisional cap and limits marked as assumptions, output checked against tool facts), `system-prompt-and-guardrails` (unprovided figures and policies become owned assumptions; a re-test never shrinks the attack set), `llm-judge-calibration` (no default target presented as given; compute which term drives the corrected rate's uncertainty). Outside-judge gains on these four went from about 0 to +2 to +7 (GPT) and +4 to +12 (Sonnet).
- `agent-design-and-tooling` case 001: grader `empty-vs-failed` accepts "X and Y are different" (it rejected a correct answer).
- README table: one number per gain column; intervals stay in [skill-eval-gains.md](skill-eval-gains.md).

## v1.1.1 (2026-11-13)

Packaging only: same skills and evidence as v1.1.0. Release notes: [docs/releases/v1.1.1.md](docs/releases/v1.1.1.md).

- Install on 12 agents: one short route per tool in the README, details in docs/install.md.
- Manifests for Codex, Gemini CLI and Antigravity; every manifest carries the release version, the validator checks they agree, and the release workflow refuses a tag that differs.
- Evals chart: model alone and with the skill only.

## v1.1.0 (2026-11-12)

Release notes: [docs/releases/v1.1.0.md](docs/releases/v1.1.0.md).

- **Two skills join the catalog (29 of 30)**: `red-team-evals` plans and reads an attack campaign on an assistant or RAG (classes, sizing, rates with intervals, coverage, residual-risk record; never "robust"), and `multi-turn-evals` evaluates whole conversations (scripted and simulated cases, a validated user simulator, conversation-level graders, pass^k).
- `system-prompt-and-guardrails`: the description now covers role-play tricks, leaks and a guardrail refusing too much; rerun, pass.
- Routing suite: 58 requests, 172 of 174 runs correct with all 29 skills installed.
- `ai-feasibility-spike`: two stronger cases (+37 and +36 points, were +3 and +5).
- `red-team-evals` case 005 replaced by one the model alone fails (+45 points, was +4); two grader false negatives fixed.
- Tooling: `judge_answers.py --key` grades the exact answers of a blind human rating sheet; `human_rating.py` stores request and goal hashes in the key.

## v1.0.0 (2026-11-12)

First stable release: 27 skills, every one with a passing recorded run on its current text. Release notes: [docs/releases/v1.0.0.md](docs/releases/v1.0.0.md).

- **Four blocks**: Specify, Build, Evaluate, Prove, drawn as a loop. New Build block for the PM who builds: `ai-feasibility-spike`, `trace-review-tool`, `prototype-handover` (new), with `system-prompt-and-guardrails` and `agent-design-and-tooling` moved in. New foundation: [build to learn](foundations/build-to-learn.md).
- **Joined the catalog**: `error-analysis`, `production-evals-monitoring`, `agent-evals`, `ai-incident-playbook` (with DORA major-incident reporting clocks), `ai-interaction-patterns`, plus the three new Build skills.
- **Agent Skills spec frontmatter**: only `name`, `description`, `license` and `metadata` at the top level, so the skills upload to claude.ai and the Skills API.
- **Evidence gate**: a run of 3 per case is recorded with fingerprints of the skill text and of its cases, pass or fail, and logged; CI fails when a catalog skill drifts from its record.
- **Routing suite**: 49 requests on known collision zones; a free lexical gate in CI and a paid run with all skills installed (147 of 147).
- **Release tooling**: one zip per skill without its eval cases, `SHA256SUMS`, a release workflow on `v*` tags; `CONTRIBUTING.md` and issue templates.

## Before v1.0.0

Untagged development, November 2026 (59 commits):

- Bootstrap: PRD, skill template, structure CI, `claude plugin eval` as the harness, foundations shipped inside each skill.
- Waves 0 to 4: drafts written and evaluated with and without the skill; free grader checks (fixtures, prompt echo, red-line weights); answers saved and regraded for free.
- Repositioned on *evals as evidence*: seven stages became three blocks; the AI Act work became one skill wired to the eval evidence; several skills retired or merged (recoverable from git history).
- Statistics: 95% intervals on every published gain, template-only control arm, blind LLM judges, cost per correct answer.
