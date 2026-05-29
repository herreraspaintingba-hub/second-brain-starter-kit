# Second Brain Starter Kit

**Turn any AI into a second brain** — one that remembers what you learn,
organizes it for you, and helps you decide what's worth your time.

A plug-and-play kit of four skills that teach your AI assistant (Claude, Cowork,
Codex, Gemini, or any host that reads `SKILL.md` files) to capture knowledge,
file it into an organized Obsidian vault, and run new ideas through an honest
decision filter — all in plain language, in **English or Spanish**.

Built for people who are **not technical**. No code, no subscription, no server.
If you can copy a folder and type a sentence, you can run it.

---

## What's in this kit

```
Second Brain Starter Kit/
├── README.md                                          ← you are here
├── Second Brain Starter Kit - User Manual (English).pdf
├── Second Brain Starter Kit - Manual del Usuario (Español).pdf
└── skills/
    ├── README.md                          ← install instructions
    ├── second-brain-init/                 ← one-time setup
    ├── save-to-obsidian/                  ← captures knowledge + session logs
    ├── project-advisor/                   ← scores ideas before you build them
    └── obsidian-power-user/               ← keeps every note clean & linked
        └── references/                    ← 12 Obsidian feature guides
```

> The manual ships in two full editions — **English** and **Spanish (Español)**.
> Each is a complete, standalone walkthrough; read whichever you prefer. The skills
> themselves are bilingual, so you can speak to your brain in either language no
> matter which manual you read.

## The four skills

| Skill | What it does | Trigger (EN / ES) |
|-------|--------------|-------------------|
| **`second-brain-init`** | Builds your vault and installs the other three. Run once. | "Set up my second brain" / "Configura mi segundo cerebro" |
| **`save-to-obsidian`** | Captures the lasting lessons from a conversation + writes a session log. | "Save to my brain" / "Guárdalo en mi cerebro" |
| **`project-advisor`** | Scores a new idea on 4 weighted dimensions → GREEN / YELLOW / RED. | "Should I do this?" / "¿Vale la pena este proyecto?" |
| **`obsidian-power-user`** | Runs automatically so every note comes out clean, linked, and formatted. | (loads in the background) |

## Quick start

1. Copy the four skill folders into your assistant's skills directory:

   ```bash
   cp -r skills/* ~/.claude/skills/      # Cowork / Claude Code
   # ~/.codex/skills/  for Codex   ·   ~/.gemini/skills/  for Gemini CLI
   ```

2. Start a new conversation and say: **"Set up my second brain"** / **"Configura mi segundo cerebro."**
3. Answer six short questions. Your vault is built and verified in about 10 minutes.

Full walkthrough — setup, daily use, maintenance, troubleshooting — is in the
manual PDF (English or Spanish edition; see `skills/README.md` for per-host
install details).

## What it does NOT require

- **Obsidian** is optional — notes are plain markdown, readable in any editor.
- **Notion** is optional — only `project-advisor` can mirror to it, if you turn it on.
- No background jobs, no connectors, no account integrations. Every action is
  something you trigger in a conversation.

## Share it

This kit is meant to be **shared freely with family and friends**. Use it, remix
it, and build vertical packs on top of the same foundation (Painters, Real
Estate, Consulting, Restaurant — whatever shape your work takes).

*Version 1.0 · Built to be shared.*
