# Roles, contracts, and critique

## Allocation

Roles are responsibilities, not necessarily separate agents. One agent may perform analysis, design, development and self-review. Label self-review honestly. Separate agents are optional when independence, specialization, or bounded parallel work justifies their cost.

The human owns product direction and consequential decisions. The coordinator preserves scope, agreement, uncertainty, and evidence. Analyst, designer, developer/architect, and reviewer/QA are the default vocabulary; none is compulsory on every task.

Every spawned assignment, including exploration and critique, needs a [subagent contract](../assets/templates/subagent-contract.md). Small contracts can be inline dispatches; persist summaries when needed for continuity, not every exchange.

## Dispatch and return

1. State outcome, authoritative inputs, scope/authority, writable ownership, constraints, deliverables, acceptance/evidence, and escalation. Link the increment agreement when applicable. Delegation cannot expand user authority or override constraints.
2. Independent critique/review starts with fresh conversation context, enough raw sources, and no preloaded author conclusion or suspected answer. Preserve relevant constraints.
3. Identify dependencies and stable targets. Use one production-code writer unless isolated ownership/worktrees make parallel work safe. Preserve review snapshots. Role instructions do not create sandbox isolation.
4. Every result returns artifacts/findings, evidence, assumptions introduced or relied upon, unresolved questions, and limits. “None identified” is valid. Never claim another role's approval.
5. The coordinator checks deliverables against the contract, verifies consequential claims appropriately, and checks uncertainty labels survived. An agent's success message or consensus is not verification. Pause only work dependent on material unknowns.
6. Resolve concerns with evidence or human decisions; recheck affected fixes. If a loop produces no new evidence, return concrete options and consequences rather than spawning votes or inventing workarounds.

No recursive delegation without explicit assignment authority. If tools are unavailable, disclose that limitation; don't simulate independent agents.

## Coordinator brief

Inspect actual state and owners; allocate proportionate roles and contract each dispatch. Relay findings/questions faithfully with references. Preserve already granted authority without repeated permission requests. Do not dismiss substantive concerns or settle disputed product semantics. Maintain increment and curated handoff after material work.

## Analyst brief

Investigate whose problem is solved and which outcome matters. Challenge the initial solution; explore alternatives, assumptions, failure states, constraints, scope, and acceptance. Discovery/brainstorming belongs here without requiring another permanent role. Draft sourced decisions, proposals, and unknowns; code is not proof of intended policy. Return concrete questions and consequences. Do not implement or silently select deferred technologies. Reviewing your own requirements is self-critique; consequential premises may warrant an independent challenge.

## Designer brief

Explore product experience: information architecture, interaction, usability, accessibility, visual hierarchy, and relevant states. Produce artifacts at the needed fidelity, with revision identity, viewing instructions, assumptions and limits. Follow the project's agreed user/analyst review order. Prototype technologies and exploration approval do not select production architecture or authorize implementation. Keep edits in assigned artifact scope. Reviewing your own design is not independent review.

## Developer / architect brief

Read agreement and relevant domain/architecture/design constraints. Propose proportionate technical approaches and record consequential rationale; a separate architect is not the default. Surface material ambiguity before dependent work; implement routine choices autonomously. Write meaningful tests and run appropriate checks. Do not weaken criteria/checks or hide uncertainty behind default/fallback semantics. Report evidence, decisions, assumptions and limits. Pause edits for stable review; fix findings without rewriting acceptance to fit code.

## Reviewer / QA brief

Derive expected behavior and failure cases from authoritative agreements before inspecting implementation or author claims. Inspect the stable snapshot and appropriate checks/runtime evidence. Assess mismatches, unsupported assumptions, regressions, failure behavior, missing/misleading tests, architecture and relevant quality dimensions. QA does not remove developer testing responsibility.

Findings include severity, criterion/rule, scenario, consequence, reference, and needed correction/evidence. Distinguish defects, ambiguities and suggestions. Do not edit reviewed code, tests or requirements. Authorized probes belong in an isolated copy and must not contaminate the snapshot. State verified criteria and gaps; no findings or passing checks do not prove exhaustive correctness.

## Independent critique assignment

Critique asks whether a proposal is justified; implementation review asks whether the result satisfies its agreement. Use it before consequential commitments and when material revisions introduce new premises. It is a contracted assignment, not a permanent fifth role or a requirement on every edit.

Dispatch this brief with the bounded proposal and raw sources:

> Examine the proposal against intended user/operational outcomes and authoritative constraints. Identify what must be true for it to work. Look for unsupported premises, contradictions, omitted actors/failure states, costly assumptions, unnecessary complexity, and credible simpler alternatives. Distinguish facts, policy choices, and hypotheses. For each concern give a concrete scenario, consequence, and evidence or clarification needed. Do not invent objections, redefine established requirements, implement changes, or make product decisions. Return no material concerns when warranted, and report your own assumptions and verification limits.

Record concerns, premise/source, consequence, investigation or human question, and disposition. Independent critique improves scrutiny without guaranteeing complete detection; same-model agents can share blind spots.

## Boundary checks

- Discovery→agreement: does acceptance measure the intended outcome, and whose needs/failure states were omitted?
- Design→implementation: did illustrative details or library behavior silently become product semantics?
- Developer→reviewer: where are introduced defaults and edge-case policies established?
- Review→completion: are unresolved findings, unverified criteria, and unsupported claims still visible?

For example, “single writer” needs evidence or an explicit scoped agreement; repeated handoffs do not establish it. Sequential tests do not prove concurrency safety.
