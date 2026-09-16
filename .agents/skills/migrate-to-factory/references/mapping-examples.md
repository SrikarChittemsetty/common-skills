# Mapping examples

These examples show migration decisions, not a substitute for the live Factory schema. Use the bundled `factory-files` skill for resource fields and validation.

## Skill and helper script

The destination already contains:

```text
factory.yaml
agents/foreman/agent.md
```

The source repository contains:

```text
.agents/skills/release-notes/SKILL.md
.agents/skills/release-notes/scripts/collect_changes.py
.agents/workflows/publish-release.md
```

The workflow tells a release role to run the skill, check the generated notes, and ask for approval before publishing. It also declares a nightly schedule, a GitHub MCP server, and `RELEASE_TOKEN`.

Proposed destination:

```text
factory.yaml
agents/foreman/agent.md
agents/release-manager/agent.md
agents/release-manager/skills/release-notes/SKILL.md
agents/release-manager/skills/release-notes/scripts/collect_changes.py
```

| Source | Proposed destination | Decision |
| --- | --- | --- |
| `source:.agents/skills/release-notes/SKILL.md@<sha>` | `agents/release-manager/skills/release-notes/SKILL.md` | Adapt tool-specific commands; preserve inputs and approval gate. |
| `source:.agents/skills/release-notes/scripts/collect_changes.py@<sha>` | `agents/release-manager/skills/release-notes/scripts/collect_changes.py` | Copy as the skill's deterministic helper and keep its relative invocation. |
| `source:.agents/workflows/publish-release.md@<sha>` | `agents/release-manager/agent.md` and MAIN routing | Split role behavior from delegation instructions. |
| Nightly trigger | None | Omit schedules in this migration and list manual follow-up. |
| GitHub MCP declaration | None | Omit MCP declarations and identify the capability the workflow still needs. |
| `RELEASE_TOKEN` declaration | None | Omit secrets setup; never inspect or copy a value. |

Adding the role and changing MAIN routing affects behavior, so present this mapping and obtain confirmation before writing.

## Multiple repositories and roles

Suppose one repository defines a reviewer prompt and code-review skill, while another defines an implementer prompt, a verification script, and handoff rules. Inventory both at pinned revisions. Map the distinct responsibilities to `agents/reviewer/` and `agents/implementer/`, scope each skill to its role, and translate the handoff contract into the existing MAIN agent.

Do not merge the roles only because their source formats differ. Conversely, do not create separate agents when two files are merely reusable instructions for the same responsibility.

If both sources define completion or retry behavior, compare them explicitly. Ask which contract wins when they conflict.

## Ambiguous or unsupported semantics

A source workflow runs on a schedule, calls a custom MCP tool, reads a managed secret, and alternates between "reviewer" and "release approver" without saying whether they are separate trust boundaries.

The safe plan is to:

1. migrate the reusable task instructions
2. omit schedule, MCP, and secret declarations
3. list the required tool capability and secret name as manual follow-ups without reading values
4. ask whether review and approval require separate agents
5. wait for confirmation before creating roles or changing routing

Do not manufacture an automation trigger, a substitute tool, or a role boundary to make the mapping look complete.
