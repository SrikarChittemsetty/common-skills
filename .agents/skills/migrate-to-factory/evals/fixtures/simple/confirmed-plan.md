# Confirmed simple migration plan

The user approves these behavior-changing writes:

- Add a `release-manager` role while keeping `foreman` as the only MAIN agent.
- Copy and adapt the release-notes skill and its helper under `agents/release-manager/skills/release-notes/`.
- Update the foreman prompt to route release-note tasks to the release manager.
- Keep all migrated files and relative references inside the destination Factory root.
- Leave the source repository unchanged and do not retain it as a runtime or writable-path dependency.

Do not add schedules, MCP declarations, secrets setup, or live Factory operations.
