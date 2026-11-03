# AI-Assisted Project Workflow Skill

A reusable Codex skill for document-driven collaboration, curated project memory, bounded development increments, and optional contracted subagents. It supports new and existing projects without imposing a technology stack or requiring multiple agents.

The repository name is `ai-assisted-project-workflow-skill`; the installed skill and invocation name are **`manage-ai-assisted-projects`**. The initial version is **0.1.0**; see [VERSION](VERSION) and [CHANGELOG.md](CHANGELOG.md).

## What it provides

- Adoption steps that initialize local Git when absent and preserve existing repository conventions and work.
- Document ownership, compact handoffs, decision records, and resume instructions that work across chats.
- Increment contracts, acceptance evidence, completion reports, and explicit assumption checks.
- Optional analyst, designer, developer/architect, and reviewer/QA role briefs.
- An independent critique assignment for consequential proposals.
- Subagent contracts defining authoritative inputs, scope, authority, deliverables, verification, uncertainty, and escalation.

Roles are responsibilities, not a requirement to create four agents. The human retains product direction and consequential decisions. Setup does not authorize starting a feature or publishing a repository. Independent scrutiny improves assumption detection but cannot guarantee completeness.

## Repository layout

```text
skills/manage-ai-assisted-projects/
  SKILL.md                  # Entry point and mode selection
  agents/openai.yaml        # Codex UI metadata
  references/               # Adoption, memory, roles and contracts
  assets/templates/         # Eight adaptable project document templates
scripts/install.py          # Standard-library installer; copy or development link
tests/test_install.py       # Installer behavior checks
AGENTS.md                   # Instructions for maintaining this repository
VERSION
CHANGELOG.md
```

The tracked `skills/` directory is the source of truth. An installed copy is a distribution, not the place to maintain the source. Changes to this repository do not update copies automatically. A development link follows changes immediately.

## Install locally

Requirements: Python 3.9 or newer and a local checkout of this repository. The installer needs no third-party packages or network access.

Run from this repository root:

```sh
python3 scripts/install.py
```

By default, the installer copies the skill to `~/.agents/skills/manage-ai-assisted-projects`, the personal discovery location described in [official Codex skill documentation](https://learn.chatgpt.com/docs/build-skills). It refuses to overwrite an existing destination.

**For the setup in which this skill was originally created**, an installed copy already exists under `~/.codex/skills/`. Keep one installation rather than introducing another skill with the same name. Update that copy explicitly:

```sh
python3 scripts/install.py --skills-dir "$HOME/.codex/skills" --replace
```

If your environment uses another skills directory, pass it with `--skills-dir`; for example, `--skills-dir "$CODEX_HOME/skills"` when `CODEX_HOME` is configured. The installer does not infer client-specific discovery paths.

With `--replace`, the old directory or symlink is moved into a timestamped backup **outside** the skills directory, and the replacement is installed. The command prints the backup location. Local changes are preserved in that backup; inspect them before discarding it. Backups are outside discovery to avoid duplicate skills.

Codex detects skills and changes automatically according to the official documentation. If the skill does not appear, restart Codex. Invoke it as `$manage-ai-assisted-projects`.

### Development link

To have Codex use the tracked source directly:

```sh
python3 scripts/install.py --link --skills-dir "$HOME/.codex/skills" --replace
```

Use a discovery directory appropriate to your client. Symlinked skill folders are supported by the [official skill documentation](https://learn.chatgpt.com/docs/build-skills). A linked installation follows checkout edits and branch changes immediately; use a copy for controlled updates. Do not install the same skill in both personal locations.

### Project-scoped installation

For a shared repository-specific installation:

```sh
python3 scripts/install.py --skills-dir /path/to/project/.agents/skills
```

This copies the skill package. It does not adopt the workflow or create project agreements. Commit project-scoped skill files only according to that project's policy. Repository discovery and duplicate-name behavior are documented in the [official guide](https://learn.chatgpt.com/docs/build-skills).

## Use with a new project

Open a Codex chat in the intended project directory and ask:

> Use $manage-ai-assisted-projects to adopt a lightweight document-driven workflow for this new project. The intended outcome is [describe the problem and users]. Initialize local Git if absent, checking for an enclosing repository first. Establish minimal project context, curated memory, templates, and assumption checks. Keep technology choices unresolved unless needed for setup. Do not start a feature, commit, create a remote, or publish anything yet.

Adoption creates only useful records and maps their ownership. It can initialize local Git, but remote creation, visibility, commits, and pushes require authority from the actual request. Unknown product details remain questions rather than invented specifications.

## Use with an existing project

> Use $manage-ai-assisted-projects to adopt this workflow in the current repository. Inspect existing instructions, documentation, issue/spec conventions, Git state, architecture, and verification commands. Preserve current work and map the workflow onto existing records. Add only missing continuity, contract, and assumption-handling mechanisms. Do not reorganize the project, implement features, or resolve product choices implicitly.

The skill adapts to existing ADRs, issues, and documentation; it does not require a second source of truth or retroactive claims about past agreement.

## Everyday work

### Resume and prepare an increment

> Use $manage-ai-assisted-projects to resume from the project handoff, verify current state, and prepare the next bounded increment contract. Surface consequential assumptions and unresolved decisions. Do not implement yet.

### Implement an agreed increment

> Implement the agreed increment using our adopted workflow. Continue routine work within scope, verify acceptance criteria, and complete the evidence report. Bring material ambiguities and necessary scope changes back to me.

### Optional contracted subagents

> Use separate analyst, developer, and reviewer subagents with explicit assignment contracts. Start with the analyst only. Preserve authoritative project constraints and uncertainty labels, and bring unresolved decisions back before implementation. Give the reviewer fresh context and a stable snapshot when review is authorized.

Add a designer when interaction/product design warrants it. The developer can cover architecture; reviewer/QA responsibility does not remove developer testing responsibility. The main chat coordinates assignments; manually creating separate chats is optional where subagent tools are available. If independence is unavailable, the agent must disclose self-review.

### Critique a consequential proposal

> Independently critique this proposal under a subagent contract. Check intended outcomes, authoritative constraints, unsupported premises, omitted failure states, unnecessary complexity, and simpler alternatives. Return concrete scenarios, consequences, and needed evidence or clarification. Do not implement or resolve product decisions for me.

The coordinator checks every returned assignment, including assumptions introduced or relied upon, unresolved questions, and verification gaps. Material uncertainty pauses dependent work; unaffected authorized work continues. Agent consensus is not evidence.

## Documents and memory

See the [skill entry point](skills/manage-ai-assisted-projects/SKILL.md), [adoption procedure](skills/manage-ai-assisted-projects/references/adoption.md), [curated memory guidance](skills/manage-ai-assisted-projects/references/project-memory.md), [role and critique briefs](skills/manage-ai-assisted-projects/references/agent-assignments.md), and [templates](skills/manage-ai-assisted-projects/assets/templates/).

Installed instructions guide adoption; the adopted project's records must remain understandable without this skill. Keep current status short, preserve decisions in owning documents, and recheck historical claims against current code/Git when relevant. Evolving skill instructions do not silently amend previously agreed project contracts.

## Branch policy

- **`dev`** is the default branch and the normal working branch for this repository and its Codex project.
- **`releases`** holds explicitly promoted stable versions for distribution/deployment. Advance it from a reviewed version of `dev` only when a release promotion is requested.
- **`main`** is a backup branch, not the normal development or release target. Advance it only when a backup update is requested.

Keep the project checkout on `dev` for normal Codex work. The local repository records `init.defaultBranch=dev`; that setting is local configuration, not a tracked or hosted default-branch setting. If a remote host is configured later, set its repository default branch to `dev` too. Creating these branches does not configure deployment automation.

## Maintain and version

1. Edit the tracked skill source and affected documentation together.
2. Update VERSION and the changelog for a versioned change. Use patch for corrections, minor for compatible additions, and major for breaking changes to the adopted workflow or migration expectations. Before 1.0, document incompatible changes explicitly rather than relying on a version number alone.
3. Run the checks below. For meaningful workflow changes, exercise a disposable new and existing project and use independent critique when useful.
4. Commit a focused change. Tag, publish, push, or create releases only when requested. No remote hosting or license is selected by this local setup.
5. Re-run the installer to update a copied installation; existing adopted projects need a separate, explicit migration assessment. A development link already follows source changes.

```sh
python3 -m unittest discover -s tests -v
git diff --check
```

Review Markdown links and package content. If the Codex `skill-creator` validator is available, run its `quick_validate.py` against `skills/manage-ai-assisted-projects`; it needs PyYAML. The skill and installer themselves have no PyYAML dependency.

Version 0.1.0 was checked with the bundled validator, independent critique, and disposable new/existing adoption exercises. That is initial validation, not proof that every project or agent will follow the workflow reliably.
