---
name: manage-ai-assisted-projects
description: Adopt or maintain a document-driven AI-assisted development workflow in new or existing repositories, with curated project memory, bounded increments, explicit assumption checks, and optional contracted subagents. Use for project workflow setup, continuity, or orchestration; not as a mandatory wrapper for ordinary coding tasks.
---

# AI-Assisted Project Workflow

Document-driven collaboration and curated repository memory are the foundation. Roles are responsibilities; separate agents are optional. This skill establishes a working convention, not a product architecture, technology stack, or feature roadmap.

## Choose the requested mode

- **Adopt or upgrade:** read [adoption](references/adoption.md). Inspect before writing; map onto existing conventions. Use only needed [templates](assets/templates/). Setup does not open an increment or authorize product implementation.
- **Resume or maintain continuity:** read [project memory](references/project-memory.md). Verify actual state, follow owning documents, and update only records affected by authorized work.
- **Prepare or execute an increment:** use the cycle below and project-adapted contract/report templates. Read [agent assignments](references/agent-assignments.md) when allocating roles, delegation, or critique is needed.
- **Critique or coordinate subagents:** read [agent assignments](references/agent-assignments.md). Critique is an assignment with a contract, not a compulsory permanent role.

Explanation or drafting requests do not authorize project edits. Preserve the requested phase and existing user authority; drafts, critique, and adoption are not implementation permission.

## Development cycle

1. Establish intended user/operational outcomes. Explore alternatives when unsettled; distinguish prototype behavior from agreed implementation.
2. For substantial work, record outcome, scope/exclusions, observable criterion IDs, constraints, material assumptions/questions, verification approach, and current stage. Small corrections can use a concise task description instead.
3. Challenge consequential premises before dependent work. Use independent critique when warranted and authorized; otherwise disclose self-critique and seek human resolution of material uncertainty.
4. Record agreement and implementation authority faithfully. One user instruction may provide both; do not invent approval ceremonies. Routine choices proceed autonomously within scope. Material changes need explicit resolution and an amendment.
5. Implement and verify observable behavior. For delegated work, supply and check a subagent contract; preserve uncertainty labels in handoffs.
6. Review against authoritative requirements and an identified stable snapshot. Use independent review when assigned; report self-review honestly when independence is unavailable.
7. Complete with criterion-linked evidence, finding dispositions, limits, and next authorized action or proposed follow-up. Update curated memory after material changes, not every tool call.

## Assumption check at every boundary

Before agreement, dispatch, handoff, implementation, and completion, ask: **what must be true for this next step to be valid, and where is that established?**

Distinguish sourced facts/agreements, proposals, unverified assumptions, routine implementation choices, and unresolved questions. Correct implementation and passing tests cannot by themselves validate the underlying premise.

If uncertainty could materially change behavior, scope, integrity, architecture, security, user experience, or acceptance, record its consequence and needed evidence/decision. Pause only dependent work; investigate within authority or bring the concrete question to the human. Do not invent a fallback or silently select a convenient interpretation. Low-impact reversible choices within authority proceed with proportionate reporting.

Every subagent returns assumptions introduced or relied upon, their basis/status, open questions, and verification limits; “none identified” is valid. The coordinator checks that proposals did not become agreed facts in transit. Independent scrutiny improves detection but cannot guarantee all hidden assumptions are found.

## Adoption resources

Templates are starting material, not a fixed taxonomy. Adapt paths, remove unused sections, and replace placeholders before treating records as agreements or handoffs.

- [AGENTS section](assets/templates/agents-section.md): working convention and source map.
- [Project overview](assets/templates/project-overview.md): intent, boundaries, and discovery.
- [Increment](assets/templates/increment.md) and [completion report](assets/templates/completion-report.md): agreement and evidence, normally in one record.
- [Current status](assets/templates/current-status.md): compact handoff.
- [Decision](assets/templates/decision.md) and [open questions](assets/templates/open-questions.md): rationale and unresolved choices.
- [Subagent contract](assets/templates/subagent-contract.md): authority, inputs, evidence, and uncertainty for every dispatch, including critique.

When adopting, copy/adapt essential collaboration, memory, and applicable role guidance into the project. Project-local instructions must work without this installed skill or personal absolute paths. Preserve existing instructions, preferences, and authorization; do not impose DTW-specific semantics, technologies, or design approval rituals.
