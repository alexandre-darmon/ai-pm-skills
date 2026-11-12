# Changelog

Each release lists what changed for someone who installs the skills. Per-skill versions live in each `SKILL.md` (`metadata.version`); eval records and their history are in [`baselines/`](baselines/).

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
