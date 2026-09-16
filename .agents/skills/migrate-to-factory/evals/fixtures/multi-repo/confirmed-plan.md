# Confirmed multi-repository migration plan

The user approves these behavior-changing writes:

- Add separate `reviewer` and `implementer` roles while keeping `foreman` as the only MAIN agent.
- Scope the review skill to the reviewer.
- Package the verification script in an implementer-scoped verification skill.
- Update the foreman prompt with the review-to-implementation handoff, the one-retry limit, targeted-test implementer completion, and blocker-free whole-workflow completion.
- Keep all migrated files and relative references inside the destination Factory root.
- Leave both source repositories unchanged and do not retain either as a runtime or writable-path dependency.

Do not add schedules, MCP declarations, secrets setup, or live Factory operations.
