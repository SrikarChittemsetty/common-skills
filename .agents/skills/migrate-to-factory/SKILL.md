---
name: migrate-to-factory
description: Migrates existing file-defined agentic workflows, Oz agent prompts, roles, skills, scripts, and orchestration instructions into an existing Warp Factory configuration repository. Use when a user asks to migrate, translate, convert, or port current agent resources into idiomatic Factory files rooted at an existing factory.yaml. Do not use for routine edits to an already-understood Factory tree or for registering, running, or otherwise operating a live Factory.
---

# Migrate to Factory

Translate existing agentic workflows into an existing file-defined Warp Factory without changing the source repositories.

## Boundaries

- Start in the destination Factory configuration repository as part of a Factory task. Locate its existing `factory.yaml`; if none exists, stop because Factory onboarding or setup is a different workflow.
- Treat every source repository as read-only. Create and edit files only under the destination Factory root.
- Migrate file-defined behavior: prompts, roles, skills, scripts, and orchestration instructions.
- For this migration, omit schedules, MCP declarations, secrets setup, and live Factory registration or operation. Record any resulting manual follow-up without reading secret values.
- Do not invoke `factory-mcp`, apply the configuration, or otherwise change a live Factory.
- Load the bundled `factory-files` skill before authoring. It owns the current Factory schema, resource examples, file conventions, and validator; never reproduce or infer its schema here.

## Workflow

### 1. Establish the destination and sources

Read `factory.yaml`, existing Factory resources, repository guidance, and the files likely to receive changes. Confirm which repositories and revisions are sources. Do not follow source symlinks outside their repositories or execute source scripts merely to understand them.

Record a stable repository-relative path and commit SHA for each source when Git metadata is available. Notice destination name collisions and existing behavior that a migration could replace.

### 2. Inventory behavior

Search the named sources for:

- skill files and their bundled scripts, references, templates, and assets
- agent, role, system, and workflow prompts
- scripts invoked by those instructions
- orchestration, delegation, handoff, retry, and completion rules
- inputs, outputs, side effects, dependencies, and failure behavior
- schedule, MCP, secret, or unsupported declarations that must be left out

Follow references far enough to understand the behavior being migrated. Do not sweep unrelated application code.

Build an inventory with these columns:

| Source | Kind | Used by | Behavior/dependencies | Proposed destination | Decision |
| --- | --- | --- | --- | --- | --- |
| `<repo>:<path>@<sha>` | skill/script/prompt/workflow | role or entry point | concise contract | relative Factory path | migrate, adapt, omit, or clarify |

For every omitted item, give a reason. Flag conflicting instructions, hidden runtime assumptions, missing entry points, unknown role ownership, and destructive side effects as ambiguities rather than guessing.

### 3. Design an idiomatic mapping

Map behavior rather than blindly copying formats:

- Put reusable guidance needed by every role under `skills/<name>/`.
- Put role-specific guidance under `agents/<role>/skills/<name>/`.
- Keep a script as a bundled skill helper when migrated instructions still call it. Preserve its supporting files and relative invocation, but adapt paths that assumed the source checkout was writable.
- Translate a workflow driver that delegates among roles into the MAIN agent's routing and handoff instructions.
- Translate distinct responsibilities and permissions into separate agents when the source genuinely enforces those boundaries. Preserve the destination's single existing MAIN agent unless the user approves replacing it.
- Create a non-scheduled automation only when an existing event-driven entry point maps cleanly to one supported by the current schema.
- Update `factory.yaml` only for required repository or default changes supported by `factory-files`.

Preserve source behavior where it is compatible: inputs, outputs, ordering, retry and failure rules, approval gates, role isolation, and side-effect boundaries. Rewrite tool-specific syntax and harness assumptions into clear Factory instructions.

When useful, add a short `Source provenance` section to a migrated prompt or skill with source repository, relative path, and revision. Preserve applicable copyright and license notices. Do not add provenance that exposes local absolute paths, credentials, or customer-private URLs.

### 4. Present the migration plan

Before writing, show:

1. the inventory and decisions
2. the proposed destination tree
3. files to add, edit, rename, or remove
4. behavior intentionally adapted or omitted
5. ambiguities and manual follow-ups

Ask focused questions for unresolved semantics. Obtain explicit user confirmation before any destructive or behavior-changing write, including replacing prompts, deleting or renaming resources, changing the MAIN role or routing, adding event triggers, or changing repository declarations. If confirmation is unavailable in the current task, stop with the proposal instead of writing.

Read [references/mapping-examples.md](references/mapping-examples.md) when choosing between shared skills, scoped skills, agents, helpers, and automations.

### 5. Author the migration

After confirmation, use `factory-files` to fetch the destination's declared schema and make the smallest compatible edits. Preserve unrelated fields and prompt bodies.

Copy only the source material selected in the plan. Keep every migrated artifact and its relative file references inside the destination Factory root.

Treat a configured repository as an explicit external runtime dependency, never as the location of a migrated artifact, bundled helper, or writable path. Do not retain a dependency on a supplied migration source. If preserving behavior genuinely requires one, stop for a user decision and record the proposed dependency as read-only before continuing.

Do not modify, normalize, or commit anything in a source repository.

### 6. Validate the Factory tree

Run the validator exactly as directed by `factory-files` against the destination Factory root. Fix every server diagnostic and rerun until clean.

Distinguish the validator outcomes:

- Exit `0`: quote the validator's success sentence and its list of checks deferred until apply.
- Exit `1`: the server checked the tree and found diagnostics; the migration is not complete.
- Exit `2`: the tree was not checked. State why and do not call it valid.

Validation does not authorize applying or registering the Factory.

### 7. Report

Summarize:

- destination files added, changed, moved, or removed
- source-to-destination mappings and preserved provenance
- behavior adaptations and omissions
- validation command, exit status, and exact result
- ambiguities resolved by the user
- manual follow-ups for schedules, MCP, secrets, live setup, or state-dependent checks

Confirm that source repositories remained unchanged.
