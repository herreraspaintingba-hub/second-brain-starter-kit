---
name: session-checkpoint
description: >
  Saves the live working state of a long session to the vault (one rolling file per
  project), so nothing is lost when the conversation gets long and the AI's memory of
  its start is compressed. Runs on its own every 15 to 20 substantial exchanges, at
  every milestone, before any heavy step, and right after a compression to recover.
  Also on request: "checkpoint", "save state", "don't lose track", "guarda el estado",
  "haz un checkpoint", "no pierdas el hilo". Bilingual EN+ES.
kit: Second Brain Starter Kit
version: 2.0.0
language: en+es
---

# Session Checkpoint: a save point for long sessions

## Why it exists

When a conversation gets long, the AI host compresses its earlier part to make room.
After that, the AI works from a summary: decisions blur, file names are forgotten,
questions get asked twice. A checkpoint is a save point in a video game: a detailed
snapshot of where the work stands, written to the vault, read back after a compression.

It does not replace `save-to-obsidian`:

| Skill | When | Saves | Where |
|---|---|---|---|
| `session-checkpoint` | During the session | Live working state | `06 Session Logs/Active Session State, <Project>.md`, overwritten each time |
| `save-to-obsidian` | At the end | Permanent knowledge and the session log | Sections 01 to 06, permanent |
| `project-door` | At the end | The project's current state | `09 MOCs/Door, <Project>.md` |

---

## When to checkpoint

- Every **15 to 20 substantial exchanges** of real work (not greetings or "ok").
- At a **milestone** ("part 1 done, starting part 2").
- When a **decision changes direction**.
- **Before a heavy step** (a sub-agent, a long build) and right after it returns.
- When the user asks.

Sessions under about 15 exchanges do not need one.

## Recovering after a compression

You get no explicit signal. Signs: the start of the conversation feels summarized, you
cannot recall an exact name or decision, or you are about to ask something already
answered. Then:

1. Read `06 Session Logs/Active Session State, <Project>.md` for the active project.
2. Tell the user: "The conversation was compressed; I re-read our checkpoint. We are
   at: ..." in one or two lines.
3. Continue from there. When in doubt, re-read; it costs seconds.

---

## The file

**One file per project**, overwritten in place:
`06 Session Logs/Active Session State, <Project>.md`. Never one shared file for all
projects: two projects worked the same day would erase each other, and nobody notices
until they try to resume. If the active project is unclear, ask before writing.

No `.bak` copies next to it. The file only reflects the current state, not a history.

```markdown
---
title: "Active Session State, <Project>"
type: checkpoint
project: <slug>
date: YYYY-MM-DD
time: "HH:MM"
description: "Rolling state of the current <Project> session; read after a compression."
tags: [checkpoint]
status: active
---

# Active Session State, <Project>

## Goal of the session
What the user asked for, in their words.

## Where we are
Done, in progress, next. Specific: names, numbers, paths.

## Decisions so far
- Decision, and why (the why is what matters after a compression).

## Key details
Exact values that would take time to find again: file paths, IDs, names, settings.

## Files created or changed
- path: what changed

## Task list
- [x] done
- [ ] pending

## Open questions or blockers
## Preferences the user expressed this session
```

Get the time from the clock (`date "+%Y-%m-%d %H:%M"`), never guess it. Then validate:

```bash
python3 "{{VAULT_PATH}}/.brain/tools/check_frontmatter.py" "06 Session Logs/Active Session State, <Project>.md"
```

## Writing guidelines

- **Specific beats generic.** "Door for Garden created, sections 1 to 3 filled, numbers
  pending from the seed invoice" beats "working on the garden".
- **Keep the why.** "We chose X because Y" survives a compression; "we chose X" does not.
- **Scannable.** Headings and short lines; it is read in a hurry.
- **A snapshot, not a transcript.**
- It is a working file: lean formatting is fine, and it does not need links beyond the
  Door.

## Changelog

- **2.0.0 (2026-10-02):** New in the kit. One rolling file per project, recovery steps,
  validated frontmatter.
