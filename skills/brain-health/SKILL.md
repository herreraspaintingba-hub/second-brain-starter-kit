---
name: brain-health
description: >
  Measures the health of the user's second brain with the same rules every month and
  keeps a history, so this month is compared with last month: broken links, orphan
  notes, notes outside the frontmatter contract, duplicates, backup files inside the
  vault, names Obsidian cannot link, and stale project Doors. Answers with a traffic
  light (green, yellow, red) and what to fix first. Use it for "brain health", "how is
  my brain doing?", "check my vault", "broken links", "orphan notes", "salud del
  cerebro", "¿cómo está mi cerebro?", "revisa el vault", "links rotos", and to manage
  the monthly schedule ("turn on the monthly check", "apaga la revisión mensual").
  Bilingual EN+ES.
kit: Second Brain Starter Kit
version: 2.0.0
language: en+es
---

# Brain Health: the same checkup, every month

A vault rots quietly: a renamed note leaves broken links, a quick save leaves an
orphan, a copy is left as `.bak`. None of it hurts on the day it happens. Measured once
a month with the same rules, it is caught while it is small.

## What it measures

| Measure | What it means | Healthy |
|---|---|---|
| Notes | How many, and per section 00 to 09 | Growing where the user works |
| Broken links | `[[links]]` to notes that do not exist | Going down |
| Orphans | Notes nothing links to (MOCs, Doors, logs excluded) | Few, and shrinking |
| No frontmatter | Notes without the properties block | 0 for new notes |
| Contract | % of notes that pass `check_frontmatter.py` | Going up |
| `.bak` files | Backup copies sitting inside the vault | **0** |
| Duplicates | Notes whose body is an exact copy of another | 0 |
| Bad names | File names with `# ^ [ ] \| :` | 0 |
| Stale Doors | Project Doors not verified in 30 days | 0 |

**The light:** RED if there are `.bak` files in the vault or broken links grew more than
10% since the last run. YELLOW if broken links grew at all, the contract % dropped, or
there are bad names or stale Doors. GREEN otherwise. It compares against **last month,
not against perfection**: an old vault starts with many broken links, and that is fine
as long as the number goes down.

## How to run it

```bash
T="{{VAULT_PATH}}/.brain/tools"
python3 "$T/brain_health.py"                     # measure and print; changes nothing
python3 "$T/brain_health.py" --write             # also add a row to the history note
python3 "$T/brain_health.py" --write --reindex   # the full monthly run
```

The history lives in `05 AI System/Brain Health History.md`: the latest light and its
reasons, the top broken links and orphans, and one row per run. Earlier rows are kept.

## The monthly schedule

The kit can run the check by itself on the **1st of every month at 07:00**:

```bash
bash "{{VAULT_PATH}}/.brain/tools/schedule_health.sh" install   # turn it on
bash "{{VAULT_PATH}}/.brain/tools/schedule_health.sh" status    # is it on? last log lines
bash "{{VAULT_PATH}}/.brain/tools/schedule_health.sh" remove    # turn it off
bash "{{VAULT_PATH}}/.brain/tools/schedule_health.sh" run       # run it now, like the schedule
```

macOS uses launchd, Linux uses cron, Windows gets a one-line `schtasks` command to
paste. On a Mac with the vault in iCloud, the first run may need Python to have Full
Disk Access (the script says how). The log is `.brain/health.log`.

## How to answer the user

1. If the monthly run already happened this month, read the history note instead of
   running it again.
2. Lead with the light and the one reason that matters most.
3. Show the measures as a short table, with last month next to this month.
4. Give **at most three fixes**, the most repeated broken link first. Offer to do them.
5. Two months in a row not green: offer a deeper review of the vault (contradictions,
   outdated notes, MOCs that no longer match), which the numbers cannot see.

## How to fix what it finds

- **`.bak` files:** move them to `Archives/Backups/<date>/`. Never delete.
- **Broken links:** create the missing note as a short stub, or fix the link to the
  right name. One fix often repairs many links.
- **Orphans:** link each from its MOC or a related note; archive what is truly dead.
- **Contract:** `python3 "$T/check_frontmatter.py" --all` lists each note and what is
  wrong. Fix the newest notes first.
- **Bad names:** rename the file and let Obsidian update the links.
- **Stale Doors:** run `project-door` on that project to verify it, or set the project
  `status: parked`.

Without Python, do a lighter manual pass: search for `.bak` files, for `[[` links whose
target has no file, and read the Doors' `verified:` dates.

## Changelog

- **2.0.0 (2026-10-02):** New skill. Nine measures, traffic light against last month,
  history note, monthly schedule on macOS, Linux and Windows.
