---
name: second-brain-init
description: >
  First-run setup (and v1 upgrade) for the Second Brain Starter Kit. Builds the
  Obsidian vault, checks the eight companion skills are installed, puts the brain's
  tools in the vault (search index, frontmatter contract, project Doors, health check),
  writes the personalized CLAUDE.md with the three-layer startup, turns on the monthly
  health check, and verifies everything. Trigger on "set up my second brain," "install
  the starter kit," "initialize my brain," "set up my vault," "upgrade my brain to v2,"
  "configura mi segundo cerebro," "instala el starter kit," "inicializa mi cerebro,"
  "configura mi bóveda," "actualiza mi cerebro a la v2," or when there is no CLAUDE.md
  with `second_brain_initialized: true` and the user asks how to start. Runs once per
  brain; re-running asks before changing anything. Bilingual EN+ES.
kit: Second Brain Starter Kit
version: 2.0.0
language: en+es
---

# Second Brain: Setup

> **One-time setup.** Builds your vault, sets up the tools, writes your CLAUDE.md and
> checks that everything works. About 10 minutes.
>
> **Configuración única.** Construye tu bóveda, instala las herramientas, escribe tu
> CLAUDE.md y verifica que todo funcione. Unos 10 minutos.

---

## When to run it

- First install of the kit, or the user asks to set up or initialize the brain.
- No `CLAUDE.md`, or one without `second_brain_initialized: true`.
- **Upgrade:** a CLAUDE.md with `kit_version: 1.0.0`. Then follow "Upgrading from v1"
  at the end instead of a fresh setup.

**Do not run it** when the brain is set up and the user is just working: they want
another skill. If a setup was left half done, offer to resume it.

## Triggers / Activadores

**English:** "set up my second brain" · "install the starter kit" · "initialize my brain"
· "set up my vault" · "I just installed the kit" · "upgrade my brain to v2"

**Español:** "configura mi segundo cerebro" · "instala el starter kit" · "inicializa mi
cerebro" · "configura mi bóveda" · "acabo de instalar el kit" · "actualiza mi cerebro a
la v2"

## Load first

`obsidian-power-user`, for the formatting of every note this setup writes.

---

## Step 1. Look around before asking

```bash
ls "$WORKING_DIR/CLAUDE.md" 2>/dev/null           # already set up?
ls "$WORKING_DIR" | grep -iE "vault|brain|obsidian" # a vault nearby?
uname -s                                            # macOS, Linux, Windows
python3 -c "import sqlite3; c=sqlite3.connect(':memory:'); c.execute('create virtual table t using fts5(x)'); print('python ok, fts5 ok')"
```

Use what you find as defaults for the questions. **Python is optional.** With Python 3
and FTS5 the brain gets real search, the frontmatter check and the monthly health
check. Without it, every skill still works with plain text search and manual checks.
If it is missing on a Mac, macOS offers to install it the first time `python3` runs;
on Windows, python.org has an installer. Never block the setup on it.

---

## Step 2. Seven questions

Ask them one at a time (with `AskUserQuestion` or the host's multiple choice).

**Q1. Your name / Tu nombre.** "What should I call you?" / "¿Cómo te llamo?"
→ `{{USER_NAME}}`

**Q2. Your role or business / Tu rol o negocio.** Optional. → `{{BUSINESS_NAME}}`

**Q3. Vault name / Nombre de la bóveda.** Default "My Second Brain" / "Mi Segundo
Cerebro". → `{{VAULT_NAME}}`

**Q4. Where it lives / Dónde vive.** Most people pick a synced folder.
1. iCloud Drive: `~/Library/Mobile Documents/com~apple~CloudDocs/{{VAULT_NAME}}` (Mac)
2. Dropbox: `~/Dropbox/{{VAULT_NAME}}`
3. OneDrive: `~/OneDrive/{{VAULT_NAME}}` (Windows)
4. Documents, local only: `~/Documents/{{VAULT_NAME}}`
5. A path they type
→ `{{VAULT_PATH}}`

**Q5. Main language / Idioma principal.** English / Español / Both. Every skill works
in both; this sets the default for headings and summaries. → `{{PRIMARY_LANGUAGE}}`

**Q6. Notion.** "Do you also use Notion? `project-advisor` can mirror its verdicts
there." Yes / No / Later. → `{{NOTION_ENABLED}}`

**Q7. Monthly health check / Revisión mensual.** "Once a month (the 1st, 07:00) the
brain can check itself: broken links, orphan notes, backups left inside, and keep a
history. Turn it on?" **Yes (recommended)** / No, I'll ask for it.
→ `{{HEALTH_SCHEDULED}}`. Skip this question if Python is not available.

---

## Step 3. Build the vault

Create `{{VAULT_PATH}}` with:

```
{{VAULT_NAME}}/
├── 00 Inbox/
├── 01 Personal Knowledge/   People/ Places/ Routines/ Lessons Learned/
├── 02 Strategy/             Vision/ Goals/ Decision Log/ North Star/
├── 03 Ideas & Notes/        References/
├── 04 Learning/             Books/ Courses/ AI & Tech/ Business/
├── 05 AI System/            Skills/ Integrations/ Architecture/
├── 06 Session Logs/
├── 07 Assets/
├── 08 Projects/
├── 09 MOCs/
├── Archives/
├── Templates/
├── Excalidraw/
└── .brain/                  tools/  vocabulary.json  (hidden from Obsidian)
```

Sections are found by number prefix, so "01 Personal Knowledge" can become "01 Company
Knowledge" later. Then write two starter notes so the graph has a center:

- `Home.md` at the root: one paragraph on what this brain is, and a link to each MOC.
- `09 MOCs/MOC, Start Here.md` (`type: moc`): links to `Home`, to the session log of
  this setup, and a short "how to use me" list (the four phrases from Step 8).

## Step 4. Check the skills are installed

`install.sh` copies all nine skills. Confirm they are in the host's skills folder
(`~/.claude/skills/`, `~/.codex/skills/`, `~/.gemini/skills/`, or where the user's AI
loads skills from):

| Skill | Job |
|---|---|
| `second-brain-init` | This setup |
| `obsidian-power-user` | Obsidian formatting and features |
| `save-to-obsidian` | Save knowledge and the session log |
| `project-advisor` | Score an idea before committing |
| `brain-search` | Search the brain before asking |
| `project-door` | One current-state note per project |
| `session-checkpoint` | Save point for long sessions |
| `close-session` | Close a session without losing anything |
| `brain-health` | Monthly checkup with history |

If any is missing, copy it from the kit's `skills/` folder.

## Step 5. Put the tools in the vault (when Python works)

The tools ship inside this skill, in `second-brain-init/tools/`. Copy them:

```bash
SRC="<skills folder>/second-brain-init/tools"
mkdir -p "{{VAULT_PATH}}/.brain/tools"
cp "$SRC"/*.py "$SRC"/*.sh "{{VAULT_PATH}}/.brain/tools/"
cp "$SRC/vocabulary.json" "{{VAULT_PATH}}/.brain/vocabulary.json"
```

In `.brain/vocabulary.json`, set `time_required_since` to today's date (from the
clock), so every note from today on carries the real time and older notes are not
flagged for it. Then build the first index:

```bash
python3 "{{VAULT_PATH}}/.brain/tools/brain_index.py"
```

If Python is not available, still copy the folder (it will work the day Python is
installed) and say so in the summary.

## Step 6. Write CLAUDE.md

Write `{{WORKING_DIR}}/CLAUDE.md` from this template. Keep it short: it is read at the
start of every conversation, and every line costs memory.

```markdown
# {{VAULT_NAME}}: brain configuration

second_brain_initialized: true
initialized_date: {{TODAYS_DATE}}
kit_version: 2.0.0

## Owner
- Name: {{USER_NAME}} · Role: {{BUSINESS_NAME}} · Language: {{PRIMARY_LANGUAGE}}

## Vault
- Name: {{VAULT_NAME}} · Path: {{VAULT_PATH}}
- Tools: {{VAULT_PATH}}/.brain/tools/ · Notion mirror: {{NOTION_ENABLED}}
- Monthly health check: {{HEALTH_SCHEDULED}}

## Startup, in three layers
1. Always: this file and `{{VAULT_PATH}}/CURRENT-CONTEXT.md`.
2. By topic, before answering:
   - A project is mentioned: read its Door front page first (`project-door`).
   - A past fact, decision or "have we done this": search the brain (`brain-search`).
   - Anything written into the vault: `obsidian-power-user` rules.
3. On demand only: the rest of a Door, checkpoints, old session logs, MOCs.

## Rules
- Search the brain before asking the user for a fact.
- Save only when asked, or offer once at the end of a session with something real.
- Real date and time on every note; frontmatter checked with check_frontmatter.py.
- Never delete in the vault: archive. No .bak copies inside it.
- Every link must resolve; no file names with # ^ [ ] | :

## Phrases
- "save to my brain" / "guárdalo en mi cerebro" → save-to-obsidian
- "should I do this?" / "¿vale la pena?" → project-advisor
- "where are we with X?" / "¿en qué quedamos con X?" → project-door
- "close the session" / "blindemos" → close-session
- "brain health" / "salud del cerebro" → brain-health

## North Star
(Fill this in after a few weeks: what you are building toward. project-advisor uses it.)
```

## Step 7. Seed CURRENT-CONTEXT.md

Write `{{VAULT_PATH}}/CURRENT-CONTEXT.md` (`type: note`, with date and time): active
projects (each linking its Door once it has one), this week's focus, open questions,
recent decisions. Short on purpose: it is read at every start. Keep it under one screen.

## Step 8. Turn on the health check

If `{{HEALTH_SCHEDULED}}` is yes:

```bash
bash "{{VAULT_PATH}}/.brain/tools/schedule_health.sh" install
python3 "{{VAULT_PATH}}/.brain/tools/brain_health.py" --write     # first row of the history
```

Tell the user it runs on the 1st of each month and that "turn off the monthly check"
switches it off. On a Mac with the vault in iCloud, mention the Full Disk Access tip the
script prints.

## Step 9. Verify

```bash
V="{{VAULT_PATH}}"
for d in "00 Inbox" "06 Session Logs" "09 MOCs" "Archives" ".brain/tools"; do
  test -d "$V/$d" && echo "OK   $d" || echo "MISSING $d"; done
for s in obsidian-power-user save-to-obsidian project-advisor brain-search project-door session-checkpoint close-session brain-health; do
  test -f "<skills folder>/$s/SKILL.md" && echo "OK   $s" || echo "MISSING $s"; done
grep -q "second_brain_initialized: true" "{{WORKING_DIR}}/CLAUDE.md" && echo "OK   CLAUDE.md" || echo "MISSING CLAUDE.md"
python3 "$V/.brain/tools/check_frontmatter.py" --all --summary   # the starter notes must pass
python3 "$V/.brain/tools/brain_search.py" "start here"           # finds MOC, Start Here
```

Fix anything missing before calling the setup done.

## Step 10. One next step, and the setup log

Give the user exactly one thing to try:

> **EN:** Your brain is ready. Talk about something you are working on, and at the end
> say "save to my brain".
>
> **ES:** Tu cerebro está listo. Platica de algo en lo que estés trabajando y al final
> di "guárdalo en mi cerebro".

Then run `save-to-obsidian` to log this setup as
`06 Session Logs/{{TODAYS_DATE}} Session, Second Brain Setup.md`: the answers, what was
installed, where it lives. It is the birth certificate of the brain.

---

## Upgrading from v1

When CLAUDE.md says `kit_version: 1.0.0`, ask once: "Upgrade your brain to v2? Nothing
is moved or deleted; I add what is new." If yes:

1. Add the missing folders: `03 Ideas & Notes/References`, `07 Assets`, `08 Projects`,
   `09 MOCs`, `Archives`, `.brain/tools`.
2. Steps 5, 7 (only if CURRENT-CONTEXT.md is missing) and 8.
3. Rewrite CLAUDE.md with the v2 template, **keeping** every line the user added
   (people, vocabulary, North Star).
4. Run `brain_health.py --write` and show the first light. Old vaults usually start
   yellow or red; that is the baseline, not a failure. Offer the three biggest fixes.
5. Do not mass-edit old notes to the new contract. They get fixed when they are next
   touched; the health history shows the progress.

## Edge cases

- **The user already has a vault:** use it. Add missing folders, never move or delete
  notes, and say so.
- **No Obsidian installed:** the notes are plain markdown; Obsidian adds the graph and
  clickable links. Suggest obsidian.md when they are ready.
- **Re-run by accident:** stop and ask: keep it, change some answers, or start over.
  Never overwrite silently.
- **Windows:** use OneDrive or Documents; the health schedule prints a `schtasks` line.
- **The host cannot run commands:** create the folders and notes by hand, skip the
  tools, and tell the user what they are missing.

## How to talk during setup

Plain words, concrete steps ("Creating the vault in iCloud...", "Building the search
index..."). At the end give three things only: a short confirmation in the user's
language, the verification lines, and the one next step.

## What this skill does not do

- It does not write the user's knowledge; that is `save-to-obsidian`.
- It does not import notes from Notion, Apple Notes or Evernote; `obsidian-power-user`
  has the import guide.

## Changelog

- **2.0.0 (2026-10-02):** Installs nine skills. Tools in `.brain/` (index, search,
  frontmatter contract, Doors, health). Folders 07, 08, 09, Archives, References.
  CLAUDE.md with three-layer startup and rules. Monthly health check (Q7). Home and
  Start Here notes. Upgrade path from v1. Python optional throughout.
- **1.0.0 (2026-05-29):** First public version.
