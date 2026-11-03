# Adoption and upgrades

## Inspect first

Identify the actual target directory and requested scope: explanation, adoption, maintenance, planning, or implementation. A chat may be attached to another project; report the target accurately and respect filesystem permissions.

Read applicable instructions; inspect Git roots, branch/history, tracked/untracked changes, documents, ADR/issue conventions, architecture, and verification commands. Preserve unrelated work. Do not install dependencies or run potentially mutating project commands just to adopt a workflow.

## New projects

1. Preserve or clarify purpose, users, intended outcomes, exclusions, and unknowns. Do not fabricate requirements to fill templates.
2. Detect an enclosing Git repository. If genuinely absent, initialize Git locally as part of authorized adoption; do not create a nested repository unintentionally. Preserve existing branch policy.
3. Establish ignore rules based on actual files/tooling so the human reviewer can stage appropriate files later. Do not blindly copy stack exclusions or hide authored records. Leave staging and committing to the human reviewer. Git initialization does not authorize remote creation, visibility selection, publication, or pushing unless the request includes them.
4. Establish minimal README, AGENTS working instructions, project context, compact status, and collaboration guidance. Record verified development commands; leave unestablished tooling explicit rather than choosing a stack.
5. Supply increment/report and subagent-contract templates. Add decision/question records as actual content warrants them, avoiding empty mandatory taxonomies.
6. Establish memory ownership, resume instructions, and an accurate status such as “workflow adopted; discovery pending.”
7. Verify and report the adopted map, unresolved choices, and invocation examples. Do not start a feature unless requested.

## Existing projects

1. Inventory existing instructions, authoritative product/technical documents, issues, decisions, tests, active work, and handoffs.
2. Map framework responsibilities onto those records. Existing issues may own increments; existing ADRs may own decisions. Reference external records with access limits explicit.
3. Separate observed implementation, documented intent, and uncertain historical rationale. Never infer past agreement from code or rewrite history to imply this process was followed.
4. Add only missing mechanisms. Follow the AGENTS preservation procedure below. Adoption is not permission to reorganize the repository or alter runtime code.
5. Surface material undocumented assumptions relevant to near-term work: basis, consequence, resolution timing. Do not block adoption on a full audit; unknowns can remain unknown.
6. Establish a compact current handoff grounded in inspected evidence. Propose a bounded pilot; execute only if authorized. Verify documentation changes and report limits.

## Preserve and supplement AGENTS.md

Apply this procedure during adoption, maintenance, and upgrades, including a nominally new project that already contains instructions.

1. Read the complete existing target `AGENTS.md` and applicable parent and scoped instructions before editing. Keep changes in the requested scope; do not consolidate or replace nested instruction files.
2. If the target file is absent, create it from the adapted [AGENTS section](../assets/templates/agents-section.md). If present, preserve its existing text, ordering, and project-specific rules. Never copy the template over it, truncate it, or regenerate the whole file. Use a targeted additive edit; preserve uncommitted edits too.
3. Compare the template's responsibilities with existing guidance by meaning. Reuse existing sections and links where they already cover a responsibility. Add only missing, compatible guidance, normally in a bounded `Document-driven collaboration` section. Do not duplicate equivalent rules or append a second workflow section on repeated adoption.
4. If proposed guidance conflicts with existing instructions, leave those instructions intact. Report the conflict and seek resolution only for dependent changes; continue compatible additions within authority. Appending a contradictory rule is not a safe merge. Replacing or removing an existing rule requires explicit authority for that change; invoking adoption or updating the skill alone does not provide it.
5. On subsequent runs, inspect the current project wording again. Supplement omissions without resetting locally adapted guidance to the latest template. Changes to agreed workflow semantics require a separate migration assessment.
6. Compare against the pre-edit content, including any uncommitted content rather than only Git HEAD. Confirm existing text remains intact, additions are compatible and nonduplicated, links resolve, and nested instructions are unchanged unless separately in scope. Report what was added, already covered, or left unresolved. If nothing is missing, leave the file unchanged.

This is an agent-executed merge procedure. The package installer does not create or merge project instruction files.

## Suggested map, only where needed

```text
AGENTS.md
README.md
docs/
  project/overview.md
  project/architecture.md
  decisions/
  planning/open-questions.md
  increments/templates/
  status/current.md
  workflow/collaboration.md
  workflow/roles.md
```

Small projects can combine records; existing projects keep conventions and numbering. Do not silently revise agreed increments when upgrading the workflow.

## Adoption choices and uncertainty gate

Select a proportionate mode: one agent; optional independent reviewer; or contracted role agents for substantial work. Define when independent critique is warranted, such as persistence semantics, security/trust boundaries, irreversible migrations, or costly product assumptions. Not every task needs every role.

Agree design review order when relevant. User-first feedback can suit exploratory interfaces; early technical critique can suit feasibility work. Preserve the user's existing sequence. Prototype approval is limited to its stated purpose, not production implementation.

Establish explicitly:

- Owners of authoritative constraints, agreements, assumptions, and current status.
- Human resolution of substantive product/architecture ambiguity, informed by evidence.
- A contract for every delegation, and coordinator inspection of returned uncertainty.
- How independent critique/review is assigned; disclose unavailable independence.
- What proceeds autonomously and what dependent work waits for clarification.

## Verification and handoff

Review changed/new files, local links, scope, consistency, and appropriate whitespace checks. Confirm no unintended runtime, dependency, ignore-rule, or user-work changes. Verify that project-local records alone explain resumption, authority, delegation contracts, assumption handling, and completion without access to this installed skill. Documentation adoption normally needs no application tests.

Ensure project-local instructions carry the human staging/commit boundary from the AGENTS template, subject to the preservation and conflict procedure above. Return the change summary, verification results/limits, and suggested focused commit message without automatically staging or committing adoption changes.

Example invocations:

> Resume from the handoff, inspect current state, and prepare the next increment contract. Surface material assumptions; do not implement yet.

> Implement the agreed increment and report acceptance evidence. Use a separate reviewer under a subagent contract with fresh context and an identified snapshot.

> Independently critique this proposal before agreement. Identify unsupported premises and concrete consequences; bring material questions back to me.
