---
name: save-to-obsidian
description: >
  Saves knowledge AND a full session log to the user's Obsidian vault in one shot.
  Extracts knowledge nuggets (lessons, decisions, ideas, insights, references) and
  routes each to its vault section (00 to 09), writes a session summary in
  06 Session Logs/, links everything into the graph with zero broken links, and
  checks every note against the frontmatter contract before calling it saved.
  Trigger on: "save to my brain," "save to obsidian," "save it," "save the session,"
  "session summary," "log this," "save the chat," "save to the vault," "guárdalo en
  mi cerebro," "guárdalo," "guarda la sesión," "guarda el contexto," "resumen de
  sesión," or ANY variation of saving conversation knowledge or logging a session.
  Bilingual EN+ES.
kit: Second Brain Starter Kit
version: 2.0.0
language: en+es
---

# Save to Obsidian: Knowledge Router + Session Logger

Every time the user says "save to my brain", this skill does two things in one shot:

1. **Knowledge extraction.** Pulls out the knowledge worth keeping (lessons, decisions,
   ideas, insights) and files each piece in the right vault section.
2. **Session log.** Writes a record of the session in `06 Session Logs/`: what was
   done, why, with which tools, and what is still open.

The user says it once. The vault gets smarter and the session is on record.

---

## When to save (the save signal)

Saving is **not automatic**. Finishing a task does not trigger a save. Save when:

- **The user asks.** "Save it", "guárdalo", "log this", "save the session".
- **You offer it once, at the end of a session that produced something real**, and the
  user says yes. Real means: a decision with reasons, a lesson learned the hard way, a
  new process, a new piece of the system, a pattern that repeated, or a strategy.

Never save in the middle of a session "just in case", and never offer more than once.
If the same kind of work has happened 3 or more times, offer to turn it into a skill
instead of saving it again.

---

## Triggers / Activadores

**English:** "save to my brain" · "save it" · "save the session" · "save this
conversation" · "log this" · "session summary" · "save to the vault"

**Español:** "guárdalo en mi cerebro" · "guárdalo" · "guarda la sesión" · "guarda esta
conversación" · "registra esto" · "resumen de sesión" · "guarda en la bóveda"

The main phrase is configurable in `CLAUDE.md` as `{{TRIGGER_PHRASE_SAVE}}`.

---

## Load order (every time)

1. This skill: routing, extraction, session log.
2. `obsidian-power-user`: formatting, linking, Obsidian conventions. The link rules
   below override anything there that conflicts.
3. Verify the vault path (next section).
4. Get the real date and time from the clock: `date "+%Y-%m-%d %H:%M"`. Never guess it.
5. Work.

---

## Vault location

The vault path is in `CLAUDE.md` as `{{VAULT_PATH}}`; its name is `{{VAULT_NAME}}`.

**Verify before writing anything:**

```bash
ls "{{VAULT_PATH}}/00 Inbox" 2>/dev/null
```

If it does not exist: ask the user to confirm the location or grant access to the
folder. Never write somewhere else as a workaround, and never leave files in the
working directory and call it done. If the user has the kit but never ran
`second-brain-init`, suggest that first.

---

## Vault structure (00 to 09)

Sections are found by their **number prefix**, so a user who renames
"01 Personal Knowledge" to "01 Company Knowledge" keeps everything working.

```
{{VAULT_NAME}}/
├── 00 Inbox/                <- Only when nothing else fits yet
├── 01 Personal Knowledge/   <- People/, Places/, Routines/, Lessons Learned/
├── 02 Strategy/             <- Vision/, Goals/, Decision Log/, North Star/
├── 03 Ideas & Notes/        <- Ideas, plus References/ (saved sources and web clips)
├── 04 Learning/             <- Books/, Courses/, AI & Tech/, Business/
├── 05 AI System/            <- Skills/, Integrations/, Architecture/
├── 06 Session Logs/         <- Session logs and project checkpoints
├── 07 Assets/               <- Finished outputs: reports, dashboards, documents
├── 08 Projects/             <- Working notes of active projects, one folder each
├── 09 MOCs/                 <- Maps of Content and project Doors
├── Archives/                <- Old or replaced notes. Nothing is ever deleted
├── Excalidraw/              <- Drawings
└── Templates/               <- The user's templates. This skill never writes here
```

---

## THE LINK RULES (non-negotiable)

Broken links are the most common way a vault rots. These rules exist so it never does.

1. **Forbidden characters in file names: `# ^ [ ] | :`** Obsidian cannot link a note
   whose name has one of them. Write `No.1` instead of `#1`, `(Draft)` instead of
   `[Draft]`, and a comma or a hyphen instead of a colon.
2. **Every link must resolve.** Before writing `[[Target]]`, check that a note with that
   name exists (search the vault by file name). A link to nothing is a broken promise.
3. **No placeholder links.** If the related note does not exist yet, either create it as
   a short stub (frontmatter plus two lines, `status: stub`) so the link resolves, or do
   not write the link. Never leave red links on purpose.
4. **Link by name, never by path.** Write `[[Note Name]]`, never `[[../folder/note]]`.
5. **Every new note enters the graph connected.** At least 2 outgoing links that resolve,
   and at least 1 incoming link: add it to the matching MOC in `09 MOCs/`, or to the
   `*See also:*` line of a related note.

---

## The frontmatter contract

Every note this skill writes carries the same properties, so search, filters and the
health check can trust them:

```yaml
---
title: "Decision, Raised Beds"
type: decision          # from the closed list in .brain/vocabulary.json
project: garden         # optional; when used, it must be in the project list
date: 2026-10-02        # YYYY-MM-DD, real date
time: "14:35"           # HH:MM, real time from the clock, never guessed
description: "One line that says what this note is and when to read it."
tags: [garden, decisions]   # lowercase, no spaces, no accents, no #
status: active          # active | done | superseded | parked | stub | draft
aliases:
  - "Raised bed decision"
source: "Conversation, 2026-10-02"
---
```

**The closed lists live in `{{VAULT_PATH}}/.brain/vocabulary.json`.** Types:
session, decision, lesson, idea, learning, reference, person, process, architecture,
integration, moc, door, checkpoint, health, note. If a note needs a new type, status or
project, add it to that file first (tell the user), then use it.

**Validate before calling it saved.** If `python3` is available, run:

```bash
python3 "{{VAULT_PATH}}/.brain/tools/check_frontmatter.py" "<the note>.md"
```

It must print `0 with problems`. If it lists a problem, fix the note and run it again.
Without Python, check the required keys, the lists and the date and time format by
reading the note back.

The `description` is the most valuable line in the note: the search ranks it high and
the AI reads it to decide whether to open the note. Write it for a stranger.

---

## PART 1: Knowledge extraction

### Step 1. Review the conversation

The whole conversation is the source. If the user pointed at something ("save the part
about pricing"), focus there. Otherwise scan everything.

### Step 2. Extract the nuggets

Filter hard. For each piece ask: **"Would this be useful in a conversation three months
from now?"**

**Content type beats topic.** A skill about marketing is still a skill, so it goes to
`05 AI System/Skills/`, not to `04 Learning/`. What it IS beats what it is ABOUT.

| Content type | Always goes to |
|---|---|
| Skill (a SKILL.md, its docs, its changelog) | `05 AI System/Skills/` |
| Integration (how tools connect, an API or connector setup) | `05 AI System/Integrations/` |
| Architecture (system design, data flows, routing rules) | `05 AI System/Architecture/` |
| Doctrine (a named principle that cuts across many notes) | `05 AI System/Architecture/` |
| MOC (a hub that maps a theme) | `09 MOCs/` |
| Finished output (report, dashboard, document) | `07 Assets/` |

For everything else, route by topic:

| Type | What to look for | Section |
|---|---|---|
| Lesson | Something that went wrong or right, with a takeaway | `01 .../Lessons Learned/` |
| Decision | A choice the user made, with reasons | `02 Strategy/Decision Log/` |
| Idea | Something to explore later | `03 Ideas & Notes/` |
| Reference | A source worth keeping (article, clip, quote) | `03 Ideas & Notes/References/` |
| Person | A pattern about a person they work or live with | `01 .../People/` |
| Place | Knowledge about a location | `01 .../Places/` |
| Routine or process | A repeatable way of doing something | `01 .../Routines/` |
| Vision or strategy | Long-term thinking, goals | `02 Strategy/` (Vision, Goals or North Star) |
| Book or course | A takeaway from something they studied | `04 Learning/Books/` or `Courses/` |
| Tech or business learning | A tool discovery, a framework | `04 Learning/AI & Tech/` or `Business/` |
| Project working note | Detail that belongs to one active project | `08 Projects/<Project>/` |

**Do not save as nuggets:** troubleshooting that only mattered today (session log),
file paths and debugging detail (session log), what a skill file already says,
anything already in the vault, or the conversation verbatim.

### Step 3. Search before you write

Look for an existing note on the same topic first. If `python3` and the index exist:

```bash
python3 "{{VAULT_PATH}}/.brain/tools/brain_search.py" "<topic words>"
```

Otherwise search file names and text in the relevant section.

- A related note exists: **update it.** Add the new knowledge and the date.
- It already says the same: skip it.
- Never create "v2" copies, never leave `.bak` copies next to a note. One note per
  topic, kept current.

### Step 4. Write the notes

**File names:** `YYYY-MM-DD Type, Short Title.md` for dated notes, a plain descriptive
name for evergreen notes. No forbidden characters.

- `2026-10-02 Lesson, Define Success Before Starting.md`
- `2026-10-02 Decision, Move Tasks to Obsidian.md`
- `What My Best Clients Have in Common.md`

**Body:**

```markdown
# [Title]

> [!info] Context / Contexto
> One or two sentences on why this came up.

[The knowledge itself, specific, with numbers and names, in the user's voice.
[[Wikilinks]] inline wherever a concept, person or decision has its own note.]

*See also: [[Related Note 1]] | [[Related Note 2]]*
```

By type, add:

- **Lesson:** `> [!warning] What happened / Qué pasó` and `> [!tip] Takeaway / Aprendizaje`.
- **Decision:** `> [!quote] Decision / Decisión`, then **Why**, then **Considered and
  rejected**.
- **Idea:** `> [!note] The idea / La idea`, then **Why it could work**, then **Open
  questions**.

### Step 5. Link it into the graph

1. Link forward to existing notes (each target verified, rule 2).
2. Link backward: add the new note to the `*See also:*` line or `related:` property of
   the notes it relates to.
3. Register it in the matching MOC in `09 MOCs/`. If a section passes about 7 notes on
   one theme and has no MOC, propose one to the user.
4. Notes created in the same save link to each other.
5. Use `[[Note#Heading]]` or `[[Note^block-id]]` to point at a precise spot, and
   `[[Note|natural words]]` when the title reads badly inline.

---

## Promotion: how knowledge moves up

The brain compounds by promoting what repeats, not by piling up notes.

- **A reference graduates.** When a saved clip in `References/` gets the user's own
  thoughts, their links, or is cited by other notes, move it to its real home
  (01, 02 or 04) and fix the links that pointed to it.
- **Many connections become a doctrine.** When about five notes keep circling the same
  principle, write one canonical note for it in `05 AI System/Architecture/` and link
  it from a MOC, so the next session reads the principle instead of rediscovering it.
- **A growing theme gets a MOC.** Propose it first; never invent a new top-level
  section on your own.

---

## PART 2: Session log

Every save gets a session log in `06 Session Logs/`, even when no nuggets were
extracted. Name: `YYYY-MM-DD Session, Short Title.md` (add `(2)`, `(3)` for more
sessions the same day).

```markdown
---
title: "Session, [Short Title]"
type: session
date: YYYY-MM-DD
time: "HH:MM"
description: "One line: what this session did and why it matters."
tags: [session, topic-tag]
status: done
---

# Session, [Short Title]

> [!info] Session details
> **Date:** YYYY-MM-DD HH:MM · **Length:** about 45 min · **Started by:** the user's opening request

## What we accomplished / Lo que logramos
A short narrative (2 to 4 paragraphs) with [[links]] to the notes, tools and people involved.

## Key decisions / Decisiones clave
> [!quote] [Decision]
> **Decision:** ... **Why:** ... **Alternatives:** ...

## Outputs
- **[Output]**: what it is and where it lives

## Tools and sources used
- **[Tool]**: what it was used for

## Lessons / Aprendizajes
> [!tip] Takeaways
> What surprised us. If nothing: "Clean session, nothing notable."

## Open items / Pendientes
- [ ] Item with enough context to act on later

## Knowledge saved
- [[Note Title]] → section
```

Scale the detail to the session: a 15-minute task gets a short log. Quote the user's
memorable lines. Keep their mix of English and Spanish as they said it.

If the session belongs to a project with a Door (`09 MOCs/Door, <Project>.md`), link the
Door from the log. Updating the Door itself is the job of `close-session`.

---

## Step 6. Tell the user what was saved

```
Saved to {{VAULT_NAME}}:
- [Note] → 02 Strategy / Decision Log
- [Note] (updated) → 01 Personal Knowledge / Lessons Learned
- Session log → 06 Session Logs
All notes pass the frontmatter check.
```

In Spanish when that is the user's language ("Guardado en ...", "Todas las notas pasan
la revisión del frontmatter"). If nothing was worth extracting, say so and save only the
log. If the search index exists, end by refreshing it:
`python3 "{{VAULT_PATH}}/.brain/tools/brain_index.py" --quiet`.

---

## Edge cases

- **Short session:** skip extraction if there is nothing, and write a condensed log.
- **Sensitive data:** the vault is private, so include it, unless the user asks not to.
- **Several unrelated tasks:** one sub-heading per task in the log.
- **Vault not reachable:** say so and ask for access. Never write elsewhere.
- **Long conversation:** if the start fell out of context, use the host's transcript
  tools to recover it before extracting.
- **Spanish-speaking user:** headings, callouts and prose in Spanish; property names
  and tags stay in English, because the tools read them.

## Vault hygiene (non-negotiable)

1. Knowledge and session records only. No temp files, no drafts for elsewhere.
2. No duplicates and no "v2" files. Update the original.
3. **Never delete.** Old or replaced notes move to `Archives/`, with `status: superseded`.
4. No `.bak` copies inside the vault. A manual backup goes to `Archives/Backups/<date>/`.
5. No orphans: 2 or more resolving links out, 1 or more in.
6. `Templates/` is read-only for this skill; `Excalidraw/` is only for drawings.
7. Session logs complement knowledge notes; they never replace them.
8. Real date and time on every note, validated frontmatter on every note.
9. **The link rules above override everything else.**

## Changelog

- **2.0.0 (2026-10-02):** The link rules (forbidden characters, no broken or placeholder
  links, link by name, MOC registration). The frontmatter contract with closed lists in
  `.brain/vocabulary.json`, real time on every note, and validation with
  `check_frontmatter.py`. The save signal. Search before writing with `brain_search.py`.
  Promotion (references, doctrines, MOCs). Never delete, no `.bak` files. Sections 07 to
  09 and Archives. File names without dashes.
- **1.0.0 (2026-05-29):** First public version.
