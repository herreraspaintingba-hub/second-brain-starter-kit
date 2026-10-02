# 🧠 Second Brain Starter Kit

> **Turn any AI into a second brain** that remembers what you learn, organizes it for
> you, finds it again when you need it, and keeps itself healthy. In plain language,
> in **English or Spanish**.

A plug-and-play kit of **nine skills** that teach your AI assistant (Claude, Cowork,
Codex, Gemini, or any host that reads `SKILL.md` files) to capture knowledge into an
organized **Obsidian vault**, search it before asking you, keep one current page per
project, close every session without losing anything, and check its own health every
month.

**Built for people who are not technical.** No subscription, no server. If you can copy
a folder and type a sentence, you can run it.

**New in v2.0:** search, project Doors, checkpoints, a closing ritual, a monthly health
check, and rules that keep the vault from rotting. See [CHANGELOG.md](CHANGELOG.md).

---

## ⚡ Install in one command

```bash
curl -fsSL https://raw.githubusercontent.com/herreraspaintingba-hub/second-brain-starter-kit/main/install.sh | bash
```

It downloads the kit and copies the nine skills into your assistant's skills folder
(it detects Claude, Codex or Gemini). Then open your AI and say:

> **"Set up my second brain"** · **"Configura mi segundo cerebro"**

It asks 7 quick questions and builds your vault in about 10 minutes.

**Already on v1?** Run the same command, then say **"Upgrade my brain to v2"** ·
**"Actualiza mi cerebro a la v2"**. Nothing is moved or deleted.

> A specific host: `HOST=codex bash install.sh` (options: `claude`, `codex`, `gemini`).

### Manual install

```bash
git clone https://github.com/herreraspaintingba-hub/second-brain-starter-kit.git
cd second-brain-starter-kit
bash install.sh            # or copy skills/* into ~/.claude/skills/ yourself
```

---

## 📖 The manual, in two editions

| Edition | File |
|--------|------|
| 🇺🇸 English | `Second Brain Starter Kit - User Manual (English).pdf` |
| 🇲🇽 Español | `Second Brain Starter Kit - Manual del Usuario (Español).pdf` |

Each one is a complete walkthrough with no technical background needed: setup, daily
use, projects, maintenance and troubleshooting, with diagrams and worked examples.

---

## 🧩 The nine skills

| Skill | What it does | How you trigger it |
|-------|--------------|--------------------|
| **`second-brain-init`** | One-time setup (or v1 upgrade): vault, tools, settings | "Set up my second brain" · "Configura mi segundo cerebro" |
| **`save-to-obsidian`** | Saves the lasting lessons of a conversation and a session log, with clean links | "Save to my brain" · "Guárdalo en mi cerebro" |
| **`brain-search`** | Searches your notes before answering or asking you | "What did we decide about...?" · "¿Qué decidimos sobre...?" |
| **`project-door`** | One page per project with where it stands today, read first | "Where are we with...?" · "¿En qué quedamos con...?" |
| **`session-checkpoint`** | A save point during long sessions | Runs by itself; or "checkpoint" |
| **`close-session`** | Closes a session: checkpoint, project page, save, index | "Close the session" · "Blindemos" |
| **`brain-health`** | Monthly checkup with a traffic light and a history | "Brain health" · "Salud del cerebro" |
| **`project-advisor`** | Scores a new idea on 4 dimensions: 🟢 / 🟡 / 🔴, math shown | "Should I do this?" · "¿Vale la pena?" |
| **`obsidian-power-user`** | Runs behind the others so every note is clean and well linked | (loads in the background) |

Day to day you mostly use four phrases: *"save to my brain"*, *"where are we with X?"*,
*"should I do this?"* and *"close the session"*.

---

## 🔄 How it works

```
You (plain language, EN/ES)
        │
        ▼
Your AI assistant ──► 9 skills ──► Your vault (organized, linked notes)
        ▲                               │
        │                               ▼
        └──── brain-search ◄──── search index (.brain/)
```

- **You talk**, in your language.
- **The skills act.** Each has one job and a phrase that triggers it.
- **The vault remembers**, and the AI **looks there first** before asking you again.
- **Once a month the brain checks itself** and tells you what to fix.

---

## 🗂️ What a vault built by this kit looks like

```
Your Brain/
├── 00 Inbox/                 ← when it does not fit anywhere yet
├── 01 Personal Knowledge/    ← people, places, routines, lessons
├── 02 Strategy/              ← vision, goals, decisions, your North Star
├── 03 Ideas & Notes/         ← ideas, and saved references
├── 04 Learning/              ← books, courses, tech, business
├── 05 AI System/             ← how your tools fit together, health history
├── 06 Session Logs/          ← a record of every session, and checkpoints
├── 07 Assets/                ← finished reports and documents
├── 08 Projects/              ← working notes of active projects
├── 09 MOCs/                  ← maps of your themes, and one Door per project
├── Archives/                 ← old notes; nothing is ever deleted
├── Templates/
└── .brain/                   ← the tools and the search index (hidden in Obsidian)
```

Sections are found by their **number**, so you can rename "01 Personal Knowledge" to
"01 Company Knowledge" and everything keeps working.

---

## 🛡️ The rules that keep a brain healthy

Learned over months of real daily use:

1. **Search before asking.** If the answer is in your notes, the AI finds it.
2. **Every link works.** No broken links, no names Obsidian cannot link.
3. **Every note has the same properties** (type, date, real time, description, status),
   checked by a script, so search and filters can trust them.
4. **Save on purpose.** The brain saves when you ask, or offers once at the end.
5. **Never delete.** Old notes go to `Archives/`.
6. **Compare with last month, not with perfection.**

---

## ✅ What it needs, and what it does not

- **Obsidian** is optional: notes are plain Markdown, readable anywhere. Install it for
  the graph view and clickable links.
- **Python 3** is optional: with it you get the search index, the frontmatter check and
  the health check (macOS and Linux usually have it; python.org for Windows). Without
  it, everything still works with plain text search.
- **Notion** is optional: only `project-advisor` can mirror to it.
- **No accounts, no connectors.** The only thing that runs on its own is the monthly
  health check, and only if you say yes at setup. Your notes stay on your computer or
  your cloud drive.

---

## 🧪 For tinkerers

```bash
bash tests/run_tests.sh     # end-to-end test of the tools on an example vault
```

The tools live in `skills/second-brain-init/tools/` (standard-library Python and one
shell script) and are copied into `<vault>/.brain/tools/` at setup.

---

## ❓ Quick FAQ

- **Do I need to be technical?** No. You run one command and talk to your AI.
- **Will it work on my phone?** Your notes sync if the vault is in iCloud, Dropbox or
  OneDrive; the skills run wherever you use your assistant.
- **Is my data private?** Yes. Everything stays in your own vault, in plain files.
- **What if I stop using it?** You keep every note, forever.

---

## 🤝 Share it

Built to be **shared freely with family and friends**. Use it, remix it, and build
*vertical packs* on the same base (Painters, Real Estate, Consulting, Restaurants,
whatever shape your work takes). Hand someone the link; they run one command and have a
working brain the same day.

## 📄 License

[MIT](LICENSE): free to use, copy, modify and share.

---

*Version 2.0 · Built to be shared.*
