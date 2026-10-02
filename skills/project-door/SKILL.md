---
name: project-door
description: >
  Keeps one "Door" note per project: the project's current state in one screen
  (what is true today, the numbers that matter, the next steps), read FIRST whenever
  work on that project starts, and rewritten at every session close. Use it when the
  user starts or resumes work on a project ("let's work on X", "where are we with X?",
  "status of X", "open the door of X", "vamos con X", "¿en qué quedamos con X?", "abre
  la Puerta de X"), when they start a new project ("new project", "proyecto nuevo"),
  and when close-session updates the project. Bilingual EN+ES.
kit: Second Brain Starter Kit
version: 2.0.0
language: en+es
---

# Project Door: the front door of every project

## Why it exists

Without a Door, resuming a project means crawling through old session logs and
guessing which one is current. That is slow, it fills the AI's memory with history,
and it still misses things. The Door fixes this: **one note, one screen, always
current**, and the first thing read when work on that project begins.

| Note | Answers | Changes |
|---|---|---|
| **Door** (`09 MOCs/Door, <Project>.md`) | Where does this project stand today? | Rewritten at every close |
| Checkpoint (`session-checkpoint`) | What were we doing an hour ago? | During a long session |
| Session log (`save-to-obsidian`) | What happened in that session? | Never, once written |
| MOC | Where is everything about this theme? | When notes are added |

---

## The shape of a Door

Six numbered sections. The numbers matter: the tools read sections by number, so the
headings can be in any language.

| # | English | Español | What goes there |
|---|---|---|---|
| 1 | Current state | Estado vigente | 3 to 6 lines: what is true today |
| 2 | Numbers that matter | Números que mandan | The few figures that drive decisions, each with its source and date |
| 3 | Next steps | Pendientes | Checkboxes: the next concrete steps and who owns each |
| 4 | How it runs | Cómo se opera | How to use, operate or ship it. Read only when needed |
| 5 | Where everything else lives | Dónde vive lo demás | Links to the MOC, checkpoint, decisions, files |
| 6 | History | Historial | One line per change, newest first |

Frontmatter: `type: door`, `project: <slug>`, `status: active`, and **`verified:
YYYY-MM-DD`**, the day someone last checked that sections 1 to 3 are true. A Door older
than 7 days is treated as possibly stale.

**Sections 1, 2 and 3 are the front page.** That is all that gets read when a session
starts. Sections 4 to 6 are read only when the task needs them. The note is never split;
in Obsidian it stays one screen.

---

## Opening a project (start of a session)

1. Identify the project from what the user said. If it is unclear, ask; do not guess
   a name (a guessed name creates a second Door that looks real).
2. Read the front page:

   ```bash
   python3 "{{VAULT_PATH}}/.brain/tools/door.py" "<Project>"
   ```

   Without Python, open `09 MOCs/Door, <Project>.md` and read sections 1 to 3.
3. If it says the Door is old, say so and check the numbers before deciding anything.
4. Read the checkpoint only if the Door points to it or the session was interrupted.
5. Tell the user in one line where things stand and what the next step is.

```bash
python3 "$T/door.py"                    # list all Doors with their verified date
python3 "$T/door.py" "Garden" 4         # one section
python3 "$T/door.py" "Garden" --all     # the whole note
```

---

## Creating a Door (new project)

When the user starts something that will take more than one session:

```bash
python3 "{{VAULT_PATH}}/.brain/tools/door.py" --new "Garden" --project garden          # English headings
python3 "{{VAULT_PATH}}/.brain/tools/door.py" --new "Huerto" --project huerto --lang es # Spanish headings
```

Then:

1. Add the project slug to the `project` list in `.brain/vocabulary.json` (tell the user).
2. Fill sections 1 to 3 with what you know now; leave honest placeholders, not invented
   numbers.
3. Link the Door from the theme's MOC in `09 MOCs/` (create a MOC if the project is big
   enough to need one), so it is not an orphan.
4. Validate: `python3 "$T/check_frontmatter.py" "09 MOCs/Door, Garden.md"`.

Without Python, create the note by hand with the six sections and the same frontmatter.

---

## Updating a Door (end of a session)

This is step 2 of `close-session`. **Rewrite, do not append**, for sections 1 to 3:

- Section 1: what is true now, replacing what is no longer true.
- Section 2: the numbers as they are now, each with where it came from.
- Section 3: check off what got done; add what is new; remove what was dropped.
- Section 6: add one line at the top: `- YYYY-MM-DD HH:MM: what changed`.
- Set `verified:` to today, only for what you actually checked.

Never put a number in section 2 you did not verify this session. If you could not verify
it, keep the old one and say "not verified since <date>".

## Changelog

- **2.0.0 (2026-10-02):** New skill. Six-section Door, front page, `door.py`.
