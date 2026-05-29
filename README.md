# 🧠 Second Brain Starter Kit

> **Turn any AI into a second brain** — one that remembers what you learn, organizes it
> for you, and helps you decide what's worth your time. In plain language, in **English or Spanish**.

A plug-and-play kit of **four skills** that teach your AI assistant (Claude, Cowork, Codex,
Gemini, or any host that reads `SKILL.md` files) to capture knowledge, file it into an
organized **Obsidian vault**, and run new ideas through an honest decision filter.

**Built for people who are _not_ technical.** No code, no subscription, no server.
If you can copy a folder and type a sentence, you can run it.

---

## ⚡ Install in one command

```bash
curl -fsSL https://raw.githubusercontent.com/herreraspaintingba-hub/second-brain-starter-kit/main/install.sh | bash
```

This downloads the kit and copies the four skills into your assistant's skills folder
(auto-detects Claude / Codex / Gemini). Then open your AI and say:

> **"Set up my second brain"**  ·  **"Configura mi segundo cerebro"**

It asks 6 quick questions and builds your vault in ~10 minutes.

> Want a specific host? `HOST=codex bash install.sh` (options: `claude`, `codex`, `gemini`).

### Manual install (no script)

```bash
git clone https://github.com/herreraspaintingba-hub/second-brain-starter-kit.git
cd second-brain-starter-kit
cp -r skills/* ~/.claude/skills/      # or ~/.codex/skills/  ·  ~/.gemini/skills/
```

---

## 📖 The manual — two full editions

| Edition | File |
|--------|------|
| 🇺🇸 English | `Second Brain Starter Kit - User Manual (English).pdf` |
| 🇲🇽 Español | `Second Brain Starter Kit - Manual del Usuario (Español).pdf` |

Each is a complete, standalone, zero-technical walkthrough (setup → daily use →
maintenance → troubleshooting), with diagrams and worked examples. The skills themselves
are bilingual, so you can talk to your brain in either language regardless of which
manual you read.

---

## 🧩 The four skills

| Skill | What it does | How you trigger it |
|-------|--------------|--------------------|
| **`second-brain-init`** | One-time setup: builds your vault, installs the other three, writes your settings. | "Set up my second brain" / "Configura mi segundo cerebro" |
| **`save-to-obsidian`** | Captures the lasting lessons from any conversation **and** writes a full session log. | "Save to my brain" / "Guárdalo en mi cerebro" |
| **`project-advisor`** | Scores a new idea on 4 weighted dimensions → 🟢 GREEN / 🟡 YELLOW / 🔴 RED, with the math shown. | "Should I do this?" / "¿Vale la pena este proyecto?" |
| **`obsidian-power-user`** | Runs automatically behind the others so every note is clean, linked, and well-formatted. | (loads in the background) |

In daily life you only ever use **two** phrases: *"save to my brain"* and *"should I do this?"*

---

## 🔄 How it works

```
You (plain language, EN/ES)
        │
        ▼
Your AI assistant ──► 4 skills ──► Your vault (organized, linked notes)
                                          │
                                          ▼
                                   Future you finds it instantly
```

- **You talk.** In your language.
- **The skills act.** Each has one job and a trigger phrase.
- **The vault remembers.** Everything lands in a labeled folder, connected to what came before.

---

## 🗂️ What a vault built by this kit looks like

```
Your Brain/
├── 00 Inbox/                 ← when it doesn't fit anywhere else yet
├── 01 Personal Knowledge/    ← people, places, routines, lessons
├── 02 Strategy/              ← vision, goals, decisions, your "North Star"
├── 03 Ideas & Notes/         ← ideas before they become projects
├── 04 Learning/              ← books, courses, tech, business
├── 05 AI System/             ← how your tools and skills fit together
├── 06 Session Logs/          ← a record of every working session
├── Templates/
└── Excalidraw/
```

Skills find a section by its **number prefix** (`01`, `02`…), so you can rename
"01 Personal Knowledge" → "01 Company Knowledge" and everything still works.

---

## 📦 What's in this repo

```
.
├── install.sh                                         ← one-command installer
├── README.md
├── Second Brain Starter Kit - User Manual (English).pdf
├── Second Brain Starter Kit - Manual del Usuario (Español).pdf
└── skills/
    ├── README.md                  ← per-host install details
    ├── second-brain-init/
    ├── save-to-obsidian/
    ├── project-advisor/
    └── obsidian-power-user/
        └── references/            ← 12 Obsidian feature guides
```

---

## ✅ What it does NOT require

- **Obsidian** is optional — notes are plain Markdown, readable in any editor. Install it
  later for the graph view and clickable links.
- **Notion** is optional — only `project-advisor` can mirror to it, if you turn it on.
- **No** background jobs, **no** connectors, **no** account integrations. Every action is
  something you trigger in a conversation. Your notes stay on your own computer or cloud drive.

---

## ❓ Quick FAQ

- **Do I need to be technical?** No. You copy a folder and talk to your AI.
- **Will it work on my phone?** Your notes sync to your phone if you pick iCloud/Dropbox at setup; the skills run wherever you use your assistant.
- **Is my data private?** Yes — everything stays in your own vault. Nothing is locked in a special format.
- **What if I stop using it?** You keep every note. They're plain Markdown, yours forever.

---

## 🤝 Share it

This kit was built to be **shared freely with family and friends**. Use it, remix it, and
build *vertical packs* on the same foundation (Painters, Real Estate, Consulting,
Restaurant — whatever shape your work takes). Hand someone the link, they run one command,
and they have a working brain the same day.

## 📄 License

[MIT](LICENSE) — free to use, copy, modify, and share.

---

*Version 1.0 · Built to be shared.*
