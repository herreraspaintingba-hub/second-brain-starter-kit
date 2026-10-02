# Changelog

## 2.0.0 (2026-10-02)

Everything the original brain learned in four months of daily use, packaged so anyone
can have it.

**New skills**

- `brain-search`: a local full-text index of the vault (SQLite FTS5, ranked by
  relevance, accents ignored) and the retrieval-first rule: search the brain before
  asking the user.
- `project-door`: one note per project with its current state in one screen. Only the
  front page (state, numbers, next steps) is read at the start of a session.
- `session-checkpoint`: a rolling save point per project for long sessions, with steps
  to recover after the conversation is compressed.
- `close-session`: the closing ritual. Checkpoint, Door, save, reindex, and an optional
  git commit that never merges blindly.
- `brain-health`: a monthly checkup (broken links, orphans, frontmatter, duplicates,
  backups inside the vault, bad names, stale Doors) with a traffic light compared
  against last month, a history note, and a monthly schedule for macOS, Linux and
  Windows.

**Updated skills**

- `save-to-obsidian` 2.0: the link rules (no forbidden characters, no broken or
  placeholder links, link by name, register in a MOC), the frontmatter contract with real
  time on every note and a validator, the save signal, search before writing, promotion
  of knowledge, never delete, no `.bak` copies.
- `second-brain-init` 2.0: installs nine skills, puts the tools in `.brain/`, adds
  folders 07, 08, 09, Archives and References, writes a CLAUDE.md with a three-layer
  startup, asks about the monthly health check, and upgrades v1 vaults without moving
  anything.
- `project-advisor` 2.0 and `obsidian-power-user` 2.0: aligned with the contract and the
  link rules; they search the brain and read the project Door first.

**Tools** (standard-library Python, optional): `brain_index.py`, `brain_search.py`,
`check_frontmatter.py`, `door.py`, `brain_health.py`, `schedule_health.sh`,
`vocabulary.json`, plus `tests/run_tests.sh`.

**Everything else**

- New installer: nine skills, older copies moved aside instead of overwritten, Python
  check.
- Both manuals rewritten for v2 (English and Spanish).
- No em dashes or en dashes anywhere in the kit.

## 1.0.0 (2026-05-29)

First public version: `second-brain-init`, `save-to-obsidian`, `project-advisor`,
`obsidian-power-user`, the installer and the two manuals.
