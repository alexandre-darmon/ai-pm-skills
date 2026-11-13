# Installing the skills in other agents

The README's [Install](../README.md#install) section has one drop-down per tool. This page lists where each instruction comes from, the manifests the repo ships for agents other than Claude, and what has not been tested. Every source was read on 2026-11-13; vendors change these pages often, so check them before a rollout.

The skills were evaluated with Claude (Sonnet 5.5) only. Another agent may choose a different skill for the same request, or follow a skill less closely; the eval numbers in the README describe Claude, not those agents.

## One layout, many readers

Each skill is `skills/<name>/SKILL.md` with its `references/`, `templates/` and `scripts/` inside, following the [Agent Skills](https://agentskills.io) standard. Frontmatter is `name` (equal to the folder), `description` (≤ 200 characters), `license` and `metadata`; every agent below requires only `name` and `description` and ignores or accepts the rest.

Two folders are read by most agents, so one copy reaches several tools:

| Folder | Read by |
| --- | --- |
| `<project>/.agents/skills/<name>/` | Codex, Cursor, Copilot, Gemini CLI, Antigravity, Devin (ex-Windsurf), OpenCode, Command Code, Amp, Goose, Roo Code |
| `~/.agents/skills/<name>/` | Codex, Cursor, Copilot, Gemini CLI, Devin, OpenCode, Command Code, Amp, Goose, Roo Code |

Not Kiro (`.kiro/skills/`), not Cline (`.cline/skills/`), and not the Antigravity IDE or App for user scope (`~/.gemini/config/skills/`).

`evals/` (cases, graders, fixtures) ships with every folder copied from the repo. Agents do not load it, since no `SKILL.md` sits under it, but it adds weight. The release zips (`scripts/package_skills.py`) leave it out: each zip holds one `<skill>/` folder, so `unzip <skill>-<version>.zip -d <skills folder>` installs it.

## Manifests in this repo

| File | For | Why |
| --- | --- | --- |
| `.claude-plugin/marketplace.json` | Claude Code; also read by Copilot CLI and VS Code, the skills CLI, and Codex as "legacy-compatible" | The bundle plus one plugin per skill (`strict: false`, `skills: [...]`) |
| `.agents/plugins/marketplace.json` | Codex | Codex's own marketplace format: one bundle plugin, source `./`, with `policy` and `category` as the docs ask |
| `.codex-plugin/plugin.json` | Codex | Plugin manifest; `skills: "./skills/"` so drafts and templates never ship |
| `gemini-extension.json` | Gemini CLI | Required for `gemini extensions install` |
| `.antigravity-plugin/plugin.json` | Antigravity CLI | Required for `agy plugin install`; the docs recommend this folder when a repo ships several vendors' manifests |

There is deliberately no root `plugin.json` and no `.claude-plugin/plugin.json`: either makes the installed Claude Code plugins fail to load (the validator checks the second). `scripts/validate_skills.py` checks that the four other manifests parse, carry the same version as `.claude-plugin/marketplace.json`, and point only at `./skills/`.

The new manifests were added after v1.1.0. Pin to a tag (`--ref`) only from the next release.

## Sources, per tool

| Tool | What the README uses | Official source |
| --- | --- | --- |
| Claude Code | `claude plugin marketplace add`, `claude plugin install`, managed settings | [code.claude.com plugins](https://code.claude.com/docs/en/plugins/org.md) |
| claude.ai, apps, Skills API | Upload a release zip under Customize > Skills | Release assets of this repo |
| Codex, skill folders | `.agents/skills/`, `~/.agents/skills/`, `$skill`, `/skills` | [learn.chatgpt.com/docs/build-skills](https://learn.chatgpt.com/docs/build-skills) |
| Codex, `$skill-installer` | Installs `skills/<name>` from a GitHub repo into `~/.codex/skills/`; `--ref` defaults to `main` | [openai/skills skill-installer](https://github.com/openai/skills/blob/main/skills/.system/skill-installer/SKILL.md) |
| Codex, plugins | `codex plugin marketplace add`, `codex plugin marketplace upgrade`, `/plugins` | [developers.openai.com/codex/plugins/build](https://developers.openai.com/codex/plugins/build/), [learn.chatgpt.com/docs/plugins](https://learn.chatgpt.com/docs/plugins) |
| ChatGPT upload | Skills > Create > Upload from your computer | [OpenAI Help Center 20001066](https://help.openai.com/en/articles/20001066) (could not be read directly: zip layout and update flow unconfirmed) |
| Cursor | `.cursor/skills/`, `.agents/skills/`, user equivalents; found at startup | [cursor.com/docs/context/skills](https://cursor.com/docs/context/skills) |
| GitHub Copilot | `gh skill install / update`, paths | [cli.github.com/manual/gh_skill_install](https://cli.github.com/manual/gh_skill_install), [gh_skill_update](https://cli.github.com/manual/gh_skill_update), [about agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) |
| Copilot CLI plugins | `copilot plugin marketplace add`, `install`, `update` | [CLI plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference) |
| Gemini CLI | `gemini skills install --path`, `--scope`, `/skills reload` | [geminicli.com/docs/cli/skills](https://geminicli.com/docs/cli/skills/), [CLI reference](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/cli-reference.md) |
| Gemini CLI extensions | `gemini extensions install --ref`, `update` | [extensions reference](https://geminicli.com/docs/extensions/reference/), [releasing](https://geminicli.com/docs/extensions/releasing/) |
| Antigravity | Skill folders; `agy plugin install`, `uninstall`, `validate` | [antigravity.google/docs/skills](https://antigravity.google/docs/skills), [plugins (CLI)](https://antigravity.google/docs/plugins?tab=cli), [build plugins](https://antigravity.google/docs/build-plugins/) |
| Windsurf / Devin | `devin plugins install`, `update`; skill folders | [Devin CLI plugins](https://docs.devin.ai/cli/extensibility/plugins/overview), [Devin Desktop customizations](https://docs.devin.ai/desktop/devin-local/customizations) |
| Kiro | `.kiro/skills/`, IDE import from a GitHub folder URL | [kiro.dev/docs/skills](https://kiro.dev/docs/skills/) |
| OpenCode | Skill folders | [opencode.ai/docs/skills](https://opencode.ai/docs/skills/) |
| Command Code | `cmd skills add`, `-s`, `-g`, `--force` | [commandcode.ai/docs/skills](https://commandcode.ai/docs/skills) |
| skills CLI | `npx skills add --list / --skill / -a / -g`, `npx skills update` | [vercel-labs/skills commands](https://github.com/vercel-labs/skills/blob/main/docs/commands.md), [agents](https://github.com/vercel-labs/skills/blob/main/docs/agents.md) (third-party) |
| Amp, Goose, Roo Code, Cline | Skill folders; `amp skill add` | [Amp](https://ampcode.com/docs/customize/skills), [Goose](https://goose-docs.ai/docs/guides/context-engineering/using-skills), [Roo Code](https://roocodeinc.github.io/Roo-Code/features/skills), [Cline](https://docs.cline.bot/features/skills) |

## Not tested yet

Everything except the Claude Code and claude.ai routes follows the vendors' docs and has not been run end to end on this repo:

- **Codex plugin**: whether `codex plugin marketplace add` prefers `.agents/plugins/marketplace.json` over `.claude-plugin/marketplace.json` when both exist. Codex does not document `strict` or per-plugin `skills` arrays, so the Claude per-skill plugins may each install all 29 skills in Codex.
- **Copilot CLI and VS Code plugins**: Copilot documents `strict` and `skills` in marketplace entries ([reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference)), and both the bundle and the single-skill plugins rely on them (there is no `plugin.json`), but neither has been tested on this repo.
- **Codex plugin source at the root**: `.agents/plugins/marketplace.json` points the plugin at `./`, the marketplace root itself. Codex asks for paths that start with `./` and stay inside the root, but its examples use subfolders and it does not say whether the root itself is allowed ([docs](https://developers.openai.com/codex/plugins/build/)).
- **Codex `$skill-installer`**: its default target `~/.codex/skills/` is not among the locations the Codex skills docs list (`.agents/skills/`, `~/.agents/skills/`, `/etc/codex/skills`, system) ([docs](https://learn.chatgpt.com/docs/build-skills)). Prefer copying into `~/.agents/skills/`.
- **Gemini CLI `--path skills`**: installing every skill from one path comes from the CLI's source code, not its docs.
- **Antigravity plugin**: the docs are recent and disagree on the name pattern; run `agy plugin validate --strict .` before a release.
- **Devin plugin**: the bare `skills/` layout should install as a skills-only plugin; installing one skill through `owner/repo#skills/<name>` is not documented.
- **Cursor GitHub import**: needs a `.cursor-plugin/marketplace.json`. Not shipped, because Cursor's docs show plugin sources as subfolders and say nothing of a plugin rooted at the repo itself.
- **Cline with the skills CLI**: `npx skills add -a cline` writes to `.agents/skills/`, a folder Cline's docs do not list. Copy into `.cline/skills/` instead.
- **Codex cloud and Kiro custom agents**: skills support in Codex cloud is not documented; Kiro custom agents need `skill://` entries in their `resources`.
