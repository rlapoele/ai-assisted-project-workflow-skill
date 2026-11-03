# Adoption and upgrades

## Inspect first

Identify the actual target directory and requested scope: explanation, adoption, maintenance, planning, or implementation. A chat may be attached to another project; report the target accurately and respect filesystem permissions.

Read applicable instructions; inspect Git roots, branch/history, tracked/untracked changes, documents, ADR/issue conventions, architecture, and verification commands. Preserve unrelated work. Do not install dependencies or run potentially mutating project commands just to adopt a workflow.

## New projects

1. Preserve or clarify purpose, users, intended outcomes, exclusions, and unknowns. Do not fabricate requirements to fill templates.
2. Detect an enclosing Git repository. If genuinely absent, initialize Git locally as part of authorized adoption; do not create a nested repository unintentionally. Preserve existing branch policy.
3. Establish ignore rules based on actual files/tooling before staging generated output or local configuration. Do not blindly copy stack exclusions or hide authored records. Git initialization does not authorize committing, remote creation, visibility selection, publication, or pushing unless the request includes them.
4. Establish minimal README, AGENTS working instructions, project context, compact status, and collaboration guidance. Record verified development commands; leave unestablished tooling explicit rather than choosing a stack.
5. Supply increment/report and subagent-contract templates. Add decision/question records as actual content warrants them, avoiding empty mandatory taxonomies.
6. Establish memory ownership, resume instructions, and an accurate status such as “workflow adopted; discovery pending.”
7. Verify and report the adopted map, unresolved choices, and invocation examples. Do not start a feature unless requested.

## Existing projects

1. Inventory existing instructions, authoritative product/technical documents, issues, decisions, tests, active work, and handoffs.
2. Map framework responsibilities onto those records. Existing issues may own increments; existing ADRs may own decisions. Reference external records with access limits explicit.
3. Separate observed implementation, documented intent, and uncertain historical rationale. Never infer past agreement from code or rewrite history to imply this process was followed.
4. Add only missing mechanisms. Merge a bounded AGENTS section without replacing unrelated rules. Adoption is not permission to reorganize the repository or alter runtime code.
5. Surface material undocumented assumptions relevant to near-term work: basis, consequence, resolution timing. Do not block adoption on a full audit; unknowns can remain unknown.
6. Establish a compact current handoff grounded in inspected evidence. Propose a bounded pilot; execute only if authorized. Verify documentation changes and report limits.

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

Example invocations:

> Resume from the handoff, inspect current state, and prepare the next increment contract. Surface material assumptions; do not implement yet.

> Implement the agreed increment and report acceptance evidence. Use a separate reviewer under a subagent contract with fresh context and an identified snapshot.

> Independently critique this proposal before agreement. Identify unsupported premises and concrete consequences; bring material questions back to me.
