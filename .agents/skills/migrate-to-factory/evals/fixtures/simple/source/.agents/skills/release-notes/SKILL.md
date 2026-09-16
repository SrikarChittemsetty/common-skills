---
name: release-notes
description: Builds release notes from merged changes and pauses for approval before publishing them.
---

# Release notes

Run `python3 scripts/collect_changes.py --output /tmp/release-notes.txt`.
Review the generated notes for missing user-facing changes. Present the draft for approval and publish only after approval.
