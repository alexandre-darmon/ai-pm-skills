# Installing the skills

The README's [Install](../README.md#install) section gives the shortest route for each tool. This page holds the rest: other scopes, single skills, updates, pinning, limits and sources. Every source was read on 2026-11-13; vendors change these pages often, so check them before a rollout.

The skills were evaluated with Claude (Sonnet 5.5) only. Another agent may pick a different skill for the same request, or follow a skill less closely; the eval numbers in the README describe Claude.

**Versions.** Every manifest (Claude Code, Codex, Gemini CLI, Antigravity) carries the release version, and a release tag always matches it. Pin a tag for a fixed set of skills, or follow `main` for every change.

**Release zips.** Each skill folder copied from the repo also carries its eval cases in `evals/`. Agents ignore them, but they add weight. The [release zips](https://github.com/alexandre-darmon/ai-pm-skills/releases/latest) leave them out: each holds one `<skill>/` folder, so `unzip <skill>-<version>.zip -d <skills folder>` installs it. `SHA256SUMS` lists the checksums.

## skills CLI

`npx skills` ([vercel-labs/skills](https://github.com/vercel-labs/skills/blob/main/docs/commands.md), third-party, not vendor-official) works for most agents below.

```bash
npx skills add alexandre-darmon/ai-pm-skills                                   # interactive
npx skills add alexandre-darmon/ai-pm-skills --list                            # see the 29 skills
npx skills add alexandre-darmon/ai-pm-skills --skill build-evals -a <agent> -g # one skill, user scope
npx skills add alexandre-darmon/ai-pm-skills --skill '*' -a <agent> -g -y      # all, no prompts
npx skills update
```

Drop `-g` to install into the current project. It reads `skills/` and the skills listed in `.claude-plugin/marketplace.json`, so drafts and templates are never installed. Agent ids and paths: [agents list](https://github.com/vercel-labs/skills/blob/main/docs/agents.md).

## Claude Code

Sources: [discover plugins](https://code.claude.com/docs/en/discover-plugins), [organisation guide](https://code.claude.com/docs/en/plugins/org.md).

- **One command.** Claude Code 2.1.292 or later can add the marketplace and install in one go: `claude plugin install ai-pm-skills --marketplace alexandre-darmon/ai-pm-skills` (in a session, `/plugin install ... --marketplace ...` from 2.1.275).
- **Bundle or single skills.** `ai-pm-skills@ai-pm-skills` installs all 29; each skill is also its own plugin, named after the skill (see the [catalog](../README.md#catalog)). Pick one or the other, not both. Drafts are not installable: they join the marketplace once they pass their eval run.
- **Pin a version.** Add the marketplace at a tag and it stays there: `claude plugin marketplace add alexandre-darmon/ai-pm-skills#v1.2.0`. Without a tag you follow `main`.
- **Update.** `claude plugin marketplace update ai-pm-skills`, then `claude plugin update ai-pm-skills@ai-pm-skills`. What changed: [CHANGELOG](../CHANGELOG.md).
- **Company rollout.** An admin registers the marketplace, pinned to a tag, in managed settings (`extraKnownMarketplaces`, source `alexandre-darmon/ai-pm-skills` with `ref` set to the tag) and turns on the plugins people should have (`enabledPlugins`). `strictKnownMarketplaces` keeps every other marketplace out.
- **Before rollout.** Each skill's eval record (`baselines/<skill>.json`) is the evidence a model risk or IT risk reviewer can read. The legal skills give checklists and questions for counsel, never a verdict.

## Claude apps

claude.ai, the Claude desktop and mobile apps, and the Skills API take one zip per skill. Download it from the [latest release](https://github.com/alexandre-darmon/ai-pm-skills/releases/latest) and upload it under Customize > Skills.

- **Team or Enterprise.** An owner uploads the zips under Organization settings > Plugins & skills and chooses who gets each skill.
- **Update.** Upload the newer zip.

## Codex

Sources: [CLI reference](https://learn.chatgpt.com/docs/developer-commands?surface=cli) (`codex plugin add`, `codex plugin marketplace add / upgrade`), [build plugins](https://developers.openai.com/codex/plugins/build/), [skills](https://learn.chatgpt.com/docs/build-skills).

- **Version.** `codex plugin add` needs Codex CLI 0.131.0 or later. On an older CLI, run `codex plugin marketplace add` and then install `ai-pm-skills` from `/plugins` (or the Plugins tab in the desktop app).
- **What installs.** The plugin is the bundle, all 29. The marketplace name comes from `.agents/plugins/marketplace.json` (Codex reads it before `.claude-plugin/marketplace.json`), so the Claude per-skill plugins do not appear in Codex.
- **Invoke.** Codex puts the plugin name in front of its skills: `$ai-pm-skills:build-evals`, or type `$` or `@` and pick from the list, or just describe the task. Start a new session after installing.
- **Update.** `codex plugin marketplace upgrade ai-pm-skills`. Pin with `codex plugin marketplace add alexandre-darmon/ai-pm-skills --ref <tag>` from the next release.
- **One skill, or the IDE extension** (which does not support plugins): copy skill folders. Codex reads `.agents/skills/` in a project (walking up to the repo root) and `~/.agents/skills/` for your user.

  ```bash
  npx skills add alexandre-darmon/ai-pm-skills --skill build-evals -a codex -g
  # or from a clone:
  mkdir -p ~/.agents/skills && cp -r ai-pm-skills/skills/build-evals ~/.agents/skills/
  ```

  A copied folder has no plugin prefix: invoke it with `$build-evals`.

- **`$skill-installer`** (bundled in Codex) can install `skills/build-evals` from this repo, but writes to `~/.codex/skills/`, which the skills docs do not list; prefer `~/.agents/skills/` ([installer](https://github.com/openai/skills/blob/main/skills/.system/skill-installer/SKILL.md)).
- **ChatGPT on the web** takes uploaded skills (Skills > Create > Upload from your computer, if your admin allows it; [Help Center](https://help.openai.com/en/articles/20001066)); the zip layout it expects is not confirmed.
- **Codex cloud.** Skills support there is not documented.
- (not tested on this repo)

## Cursor

Source: [cursor.com/docs/context/skills](https://cursor.com/docs/context/skills).

- **Folders.** Project `.agents/skills/` or `.cursor/skills/`; user `~/.agents/skills/` or `~/.cursor/skills/`. Cursor also reads `.claude/skills/` and `~/.claude/skills/`, so skills installed for Claude Code show up too.
- **Without npx.** `cp -r ai-pm-skills/skills/* ~/.cursor/skills/` from a clone.
- **Update.** `npx skills update`, or copy again. Skills are found at startup: restart Cursor.
- **Limit.** The repo ships no `.cursor-plugin/marketplace.json`, so Cursor's "From GitHub Repository" import and team marketplaces do not apply.

## GitHub Copilot

Sources: [CLI plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference), [gh skill install](https://cli.github.com/manual/gh_skill_install), [gh skill update](https://cli.github.com/manual/gh_skill_update), [about agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills).

- **Copilot CLI.** It reads this repo's `.claude-plugin/marketplace.json`: `ai-pm-skills@ai-pm-skills` for all 29, `build-evals@ai-pm-skills` for one. Update with `copilot plugin update ai-pm-skills`. (not tested on this repo)
- **VS Code and the cloud agent.** With GitHub CLI 2.90.0 or later, `gh skill` (public preview):

  ```bash
  gh skill install alexandre-darmon/ai-pm-skills --all --scope user      # all 29
  gh skill install alexandre-darmon/ai-pm-skills build-evals             # one skill, this project
  gh skill install alexandre-darmon/ai-pm-skills build-evals@v1.2.0      # pinned to a tag
  gh skill update --all
  ```

  `gh skill` copies the whole folder, `evals/` included.
- **Folders.** Copilot reads `.github/skills/`, `.claude/skills/` or `.agents/skills/` in a project and `~/.copilot/skills/` or `~/.agents/skills/` for your user.

## Gemini CLI

Sources: [extensions reference](https://geminicli.com/docs/extensions/reference/), [releasing](https://geminicli.com/docs/extensions/releasing/), [skills](https://geminicli.com/docs/cli/skills/), [CLI reference](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/cli-reference.md).

- **Extension (all 29).** Uses the repo's `gemini-extension.json`. Update with `gemini extensions update ai-pm-skills`; pin with `--ref <tag>` from the next release.
- **One skill.** `gemini skills install https://github.com/alexandre-darmon/ai-pm-skills.git --path skills/build-evals`. Default scope is your user (`~/.gemini/skills/`); add `--scope workspace` for the current project. No update command: install again, then `/skills reload`.
- **All skills without the extension.** `--path skills` follows from the CLI's source code, not its docs, which describe `--path` as one skill's folder (not tested on this repo).
- **Plans.** Google replaced Gemini CLI with Antigravity CLI for unpaid-tier and Google One users on June 18, 2026; on those plans, use Antigravity.

## Antigravity

Sources: [plugins (CLI)](https://antigravity.google/docs/plugins?tab=cli), [build plugins](https://antigravity.google/docs/build-plugins/), [skills](https://antigravity.google/docs/skills).

- **Plugin (CLI, all 29).** Uses the repo's `.antigravity-plugin/plugin.json`. Skills appear as `/<skill>`, with no plugin prefix. Global scope lands in `~/.gemini/config/plugins/`. (not tested on this repo)
- **Update.** No update command: `agy plugin uninstall ai-pm-skills`, then install again. No documented tag pinning.
- **Maintainers.** The docs are recent and disagree on the name pattern: run `agy plugin validate --strict .` before a release.
- **IDE, App, or one skill.** Copy the folder; the IDE has no install command. User scope is `~/.gemini/config/skills/`, project scope `.agents/skills/`. Run `/skills reload` in the CLI or start a new conversation.

  ```bash
  npx skills add alexandre-darmon/ai-pm-skills --skill build-evals -a antigravity -g
  ```

## Devin and Windsurf

Windsurf's docs now redirect to Devin's. Sources: [Devin CLI plugins](https://docs.devin.ai/cli/extensibility/plugins/overview), [Devin Desktop customizations](https://docs.devin.ai/desktop/devin-local/customizations).

- **Plugin (Devin CLI, all 29).** Run `devin auth login` first. The repo has no Devin manifest, so it installs as a skills-only plugin; skills are invoked as `/<plugin>:<skill>`, presumably `/ai-pm-skills:build-evals`. Update with `devin plugins update ai-pm-skills`. (not tested on this repo)
- **One skill.** `npx skills add alexandre-darmon/ai-pm-skills --skill build-evals -a devin -g`, or copy the folder into `.devin/skills/` or `.agents/skills/` (project; legacy `.windsurf/skills/`), `~/.config/devin/skills/` or `~/.agents/skills/` (user).

## Kiro

Source: [kiro.dev/docs/skills](https://kiro.dev/docs/skills/).

- **Folders.** `.kiro/skills/` (workspace) and `~/.kiro/skills/` (global). Kiro does not read `.agents/skills/`.
- **IDE import, one skill.** Agent Steering & Skills > + > Import a skill > GitHub, then paste a skill's folder URL, for example `https://github.com/alexandre-darmon/ai-pm-skills/tree/main/skills/build-evals`. No update: import again.
- **All skills without npx.** `gh skill install alexandre-darmon/ai-pm-skills --all --dir .kiro/skills` (this workspace).
- **Custom agents** load skills only if their `resources` include `skill://.kiro/skills/**/SKILL.md`.

## OpenCode

Source: [opencode.ai/docs/skills](https://opencode.ai/docs/skills/).

- **Folders.** `.opencode/skills/`, `.agents/skills/` and `.claude/skills/` in a project; `~/.config/opencode/skills/`, `~/.agents/skills/` and `~/.claude/skills/` for your user. Skills installed for Claude Code show up too.
- **No installer of its own.** Without npx: `cp -r ai-pm-skills/skills/* ~/.config/opencode/skills/` from a clone. Update with `npx skills update` or copy again.

## Command Code

Source: [commandcode.ai/docs/skills](https://commandcode.ai/docs/skills).

- **Scope.** Without `-g`, skills go to the project (`.commandcode/skills/`); with it, to `~/.commandcode/skills/`.
- **Limits.** No documented flag to install all skills at once, and no update command: `--force` overwrites an installed skill.

## Other agents

Name your agent with `-a` in the [skills CLI](#skills-cli), or copy `skills/<name>/` (or unzip a release zip) into its skills folder:

| Agent | `-a` | Project | User | Docs |
| --- | --- | --- | --- | --- |
| Amp | `amp` | `.agents/skills/` | `~/.config/agents/skills/` (also `amp skill add --global alexandre-darmon/ai-pm-skills`) | [ampcode.com](https://ampcode.com/docs/customize/skills) |
| Goose | `goose` | `.agents/skills/` | `~/.agents/skills/` | [goose-docs.ai](https://goose-docs.ai/docs/guides/context-engineering/using-skills) |
| Roo Code | `roo` | `.roo/skills/` or `.agents/skills/` | `~/.roo/skills/` or `~/.agents/skills/` | [Roo Code docs](https://roocodeinc.github.io/Roo-Code/features/skills) |
| Cline | `cline` | `.cline/skills/` | `~/.cline/skills/` | [docs.cline.bot](https://docs.cline.bot/features/skills) |

Cline: `npx skills add -a cline` writes to `.agents/skills/`, which Cline's docs do not list; copy into `.cline/skills/` instead. Goose: `-a goose` writes to `.goose/skills/` and `~/.config/goose/skills/`, not the folders in the row.

## One layout, many readers

Each skill is `skills/<name>/SKILL.md` with its `references/`, `templates/` and `scripts/` inside. Frontmatter is `name` (equal to the folder), `description` (≤ 200 characters), `license` and `metadata`; every agent above requires only `name` and `description`.

Two folders are read by most agents, so one copy reaches several tools:

| Folder | Read by |
| --- | --- |
| `<project>/.agents/skills/<name>/` | Codex, Cursor, Copilot, Gemini CLI, Antigravity, Devin, OpenCode, Command Code, Amp, Goose, Roo Code |
| `~/.agents/skills/<name>/` | Codex, Cursor, Copilot, Gemini CLI, Devin, OpenCode, Command Code, Amp, Goose, Roo Code |

Not Kiro, not Cline, and not the Antigravity IDE or App for user scope.

## Manifests in this repo

| File | For | Why |
| --- | --- | --- |
| `.claude-plugin/marketplace.json` | Claude Code; also read by Copilot CLI and the skills CLI | Marketplace `ai-pm-skills`: the bundle plus one plugin per skill (`strict: false`, `skills: [...]`) |
| `.agents/plugins/marketplace.json` | Codex | Marketplace `ai-pm-skills` with one plugin, `ai-pm-skills`, source `./` (Codex maps `./` to the marketplace root) |
| `.codex-plugin/plugin.json` | Codex | Plugin manifest, `skills: "./skills/"`, with the `interface` block `/plugins` displays |
| `gemini-extension.json` | Gemini CLI | Required for `gemini extensions install` |
| `.antigravity-plugin/plugin.json` | Antigravity CLI | Required for `agy plugin install`; takes precedence over a root `plugin.json` |

There is deliberately no root `plugin.json` and no `.claude-plugin/plugin.json`: either makes the installed Claude Code plugins fail to load (the validator checks the second). `scripts/validate_skills.py` checks that the other manifests parse, carry the same version as `.claude-plugin/marketplace.json` (top level and plugin entries), and point only at `./skills/`.
