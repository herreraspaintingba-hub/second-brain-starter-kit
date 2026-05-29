---
name: save-to-obsidian
description: >
  Saves knowledge AND a full session log to the user's Obsidian vault in one shot.
  Extracts knowledge nuggets (lessons, decisions, ideas, insights) routed to vault
  sections 01-05, plus creates a session summary in 06 Session Logs/ with outputs,
  reasoning, tools used, and lessons learned. Trigger on: "save to my brain,"
  "save to obsidian," "save it," "save the session," "session summary," "log this,"
  "save the chat," "save to the vault," "guárdalo en mi cerebro," "guarda el
  contexto," "resumen de sesión," "guárdalo," or ANY variation of saving
  conversation knowledge or logging a session. Works in any session — project,
  experimental, or research. This is how the knowledge base grows. Bilingual EN+ES.
kit: Second Brain Starter Kit
version: 1.0.0
language: en+es
---

# Save to Obsidian — Unified Knowledge Router + Session Logger

This skill does two things every time the user says "save to my brain":

1. **Knowledge Extraction** — Pulls out reusable knowledge nuggets (lessons, decisions,
   ideas, insights) and routes each to the correct vault section (01–05).
2. **Session Summary** — Creates a full-log record of the session in `06 Session Logs/`
   with what was accomplished, the reasoning, tools used, and lessons learned.

Both happen in one shot. The user says "save it" once, the vault gets smarter AND the
session is permanently recorded.

**The goal is zero-friction, total capture.** The user shouldn't have to summarize,
categorize, or run two commands. They just say the trigger phrase and everything worth
keeping is captured.

This works in ANY session — project work, experiments, research, skill building. If
the user likes what was created in a non-project session, this skill captures it and
brings it into the vault.

---

## Triggers / Activadores

**English:**
- "save to my brain"
- "save it"
- "save the session"
- "save this conversation"
- "log this"
- "session summary"
- "save to the vault"

**Español:**
- "guárdalo en mi cerebro"
- "guárdalo"
- "guarda la sesión"
- "guarda esta conversación"
- "registra esto"
- "resumen de sesión"
- "guarda en la bóveda"

The trigger phrase is configurable in `CLAUDE.md` as `{{TRIGGER_PHRASE_SAVE}}`.
Defaults to "save to my brain" / "guárdalo en mi cerebro".

---

## REQUIRED: Load the Obsidian Power User Skill

**Before writing ANY file to the vault, you MUST load the `obsidian-power-user` skill.**

This is non-negotiable. The `obsidian-power-user` skill contains the formatting rules
and Obsidian-native conventions that make the vault function as a connected knowledge
system, not just a folder of markdown files. Without it, notes will be missing the
structure that makes Obsidian powerful.

**What `obsidian-power-user` provides that this skill needs:**

| Feature | Why It Matters |
|---------|---------------|
| **YAML frontmatter** | Proper `title`, `date`, `tags`, `aliases`, `type`, `status` properties that power Dataview queries and graph filters |
| **Wikilinks `[[]]`** | Internal linking that builds the graph — the brain's nervous system |
| **Block references `^block-id`** | Lets other notes link to specific paragraphs, not just entire files |
| **Callouts `> [!type]`** | Visual formatting for tips, warnings, examples, quotes inside notes |
| **Tags** | Filterable metadata in both frontmatter and inline |
| **Aliases** | Multiple names for the same note so it's findable by any term |
| **Embeds `![[]]`** | Pulling content from one note into another without duplicating |
| **Backlinks** | Every `[[link]]` creates a backlink in the target note — bidirectional connections |
| **Map of Content (MOC)** | Index notes that organize topics — the vault's table of contents |
| **Graph view optimization** | Proper linking density, no orphan nodes, meaningful clusters |
| **Canvas files** | `.canvas` JSON for visual maps and diagrams |
| **Base files** | `.base` YAML for database views of vault content |
| **Mermaid diagrams** | Flowcharts, sequence diagrams, mind maps inside notes |
| **Templater syntax** | Dynamic templates with `<% %>` for reusable note structures |

**Load order every time:**
1. Load `save-to-obsidian` (this skill) — for routing, extraction, and session logging
2. Load `obsidian-power-user` — for formatting, linking, and Obsidian conventions
3. Verify vault path (see next section)
4. Then proceed with knowledge extraction and session logging

---

## Vault Location

The user's Obsidian vault path is configured in `CLAUDE.md` as `{{VAULT_PATH}}`.
The vault name is `{{VAULT_NAME}}`.

### CRITICAL: Vault Path Verification

**Before writing ANY file, verify the correct vault is mounted.** Run:

```bash
ls "{{VAULT_PATH}}/00 Inbox" 2>/dev/null
```

If the path exists and shows the expected folder structure (00-06), proceed.

If the path does NOT exist:
1. Ask the user to confirm the vault location
2. If they're in Cowork or a similar tool, ask them to mount or grant access to the vault folder
3. Never create files outside the vault as a workaround
4. Never silently create files in the working directory and call it done

If the user has the Second Brain Starter Kit but hasn't run `second-brain-init` yet,
suggest that as the first step rather than improvising.

---

## Vault Structure

The starter kit vault uses this structure. Sections referenced by number prefix
(`01`, `02`, etc.) so users who rename them keep the routing working.

```
{{VAULT_NAME}}/
├── 00 Inbox/                <- Only if nothing else fits
├── 01 Personal Knowledge/   <- Or "01 Company Knowledge" if user is business-focused
│   ├── People/              <- Clients, team, collaborators
│   ├── Places/              <- Locations, neighborhoods, venues
│   ├── Routines/            <- Habits, workflows, procedures
│   └── Lessons Learned/     <- What went wrong/right and why
├── 02 Strategy/
│   ├── Vision/              <- Long-term aspiration
│   ├── Goals/               <- Time-bound objectives
│   ├── Decision Log/        <- Decisions made and the reasoning behind them
│   └── North Star/          <- The {{NORTH_STAR_NAME}} — the user's guiding vision
├── 03 Ideas & Notes/        <- Raw ideas, sparks, things to explore later
├── 04 Learning/
│   ├── Books/               <- Book takeaways
│   ├── Courses/             <- Course notes and frameworks
│   ├── AI & Tech/           <- Tech knowledge, tool learnings
│   └── Business/            <- Business concepts, frameworks
├── 05 AI System/
│   ├── Skills/              <- What each skill does, dependencies
│   ├── Integrations/        <- How tools connect (any MCP, API, connector)
│   └── Architecture/        <- System design, data flows
├── 06 Session Logs/         <- Full session summaries (this skill creates these)
├── Excalidraw/              <- Visual diagrams and drawings
└── Templates/               <- User-managed; this skill does NOT write here
```

Users who rename sections (e.g., "01 Personal Knowledge" → "01 Company Knowledge") keep
the routing working as long as the number prefix stays the same.

---

## PART 1: Knowledge Extraction

### Step 1 — Review the Current Conversation

You already have the full conversation in your context window — that's your source
material. Read back through the entire conversation from the beginning and identify
knowledge worth keeping.

If the user pointed to something specific ("save the part about pricing"), focus on
that. If they said something general ("save to my brain"), scan everything.

### Step 2 — Extract Knowledge Nuggets

Read through the transcript and identify knowledge worth keeping. Not everything
in a conversation is knowledge — filter aggressively. Ask yourself for each piece:
**"Would this be useful context in a future conversation 3 months from now?"**

### CRITICAL RULE: Content Type Overrides Topic

**Before using the topic-based routing table below, check content type FIRST.**
A skill about marketing is still a SKILL — it goes in `05 AI System/Skills/`,
NOT in `04 Learning/Marketing/`. A skill about SEO goes in `05 AI System/Skills/`,
NOT in `04 Learning/AI & Tech/`. The content type (what it IS) always beats the
topic (what it's ABOUT).

| Content type | Always routes to | Examples |
|-------------|-----------------|----------|
| **Skill** (any SKILL.md, skill documentation, skill changelog, skill architecture note, skill dependency map) | **05 AI System/Skills/** | A new SEO skill, an updated brand-voice skill, a skill dependency map |
| **Integration** (how tools connect, API configs, MCP setups) | **05 AI System/Integrations/** | A new MCP connector setup, an API data flow |
| **Architecture** (system design, data flows, routing rules) | **05 AI System/Architecture/** | Skill routing diagram, briefing data flow |

**If the content IS one of the above types, route it there — period. Do NOT
re-route based on the skill's topic.** Only use the topic-based table below for
content that is NOT a skill, integration, or architecture note.

### Topic-Based Routing (for non-skill content only)

| Type | What to look for | Vault section |
|------|-----------------|---------------|
| **Lesson Learned** | Something that went wrong/right, with a takeaway | `01 Personal Knowledge/Lessons Learned/` |
| **Decision** | A choice the user made, with reasoning | `02 Strategy/Decision Log/` |
| **Idea** | Something to explore later, an opportunity, a hunch | `03 Ideas & Notes/` |
| **Person Insight** | Pattern about a client, collaborator, or team member | `01 Personal Knowledge/People/` |
| **Place Intel** | Location-specific info (neighborhood, venue, region) | `01 Personal Knowledge/Places/` |
| **Routine / Process** | Workflow, habit, procedure, repeatable system | `01 Personal Knowledge/Routines/` |
| **Vision / Strategy** | Long-term thinking, growth plans, aspirations | `02 Strategy/` (subfolder varies — Vision, Goals, or North Star) |
| **Book / Course Takeaway** | Insight from a book or course | `04 Learning/Books/` or `04 Learning/Courses/` |
| **Tech Learning** | Tool knowledge, workflow discovery | `04 Learning/AI & Tech/` |
| **Business Concept** | Framework or concept discussed | `04 Learning/Business/` |

**What NOT to save as knowledge nuggets:**
- Troubleshooting steps that only matter for this session (these go in the session log)
- File paths or technical debugging details (session log territory)
- Instructions already captured in a skill's SKILL.md
- Anything that duplicates what's already in the vault (check first!)
- The conversation itself verbatim — extract the knowledge, not the transcript

### Step 3 — Check for Duplicates

Before creating any note, check if the vault already has a note on the same topic.
Use `Grep` or `Glob` to search the relevant vault section.

- If a related note exists, **update it** rather than creating a new one
- If the existing note covers the same ground, skip it entirely
- Never create "v2" copies — one note per topic, kept current

This is the vault's #1 hygiene rule: no duplicates.

### Step 4 — Write the Knowledge Notes (Obsidian-Native Format)

For each piece of knowledge, create a markdown note in the correct vault section.
**Follow the `obsidian-power-user` formatting standards** — every note must use proper
Obsidian conventions.

**File naming convention:**
```
YYYY-MM-DD [Type] — [Short Title].md
```

Examples:
- `2026-05-28 Lesson — Don't Commit to a Project Before Defining Success.md`
- `2026-05-28 Decision — Migrate Tasks from Apple Notes to Obsidian.md`
- `2026-05-28 Idea — Weekly Reflection Template in Daily Note.md`

For ongoing reference notes that don't fit the dated pattern (like people or places),
use descriptive names without dates:
- `What My Best Clients Have in Common.md`
- `Downtown — Local Knowledge.md`

**Required note format (Obsidian-native):**

```markdown
---
title: "[Title]"
aliases:
  - [Alternative name 1]
  - [Alternative name 2]
date: YYYY-MM-DD
type: [lesson | decision | idea | person | place | routine | strategy | learning]
status: active
tags:
  - [relevant-tag-1]
  - [relevant-tag-2]
source: "Conversation, YYYY-MM-DD"
related:
  - "[[Related Note 1]]"
  - "[[Related Note 2]]"
---

# [Title]

> [!info] Context / Contexto
> [1-2 sentence setup of why this came up]

---

[The actual knowledge — written clearly, in the user's voice where appropriate.
Include the "why" behind decisions. Include specific numbers, names, or details
that make this actionable rather than generic.

Use [[wikilinks]] inline whenever referencing concepts, people, places, or
decisions that have (or should have) their own note in the vault.

Use > [!tip], > [!warning], > [!example], > [!quote] callouts to visually
structure important sections. Translate callout labels to the user's primary
language if it isn't English.]

---

*See also: [[Related Note 1]] | [[Related Note 2]] | [[Related Note 3]]*
```

**Additional sections by type:**

For **Lessons Learned**, also include:
> [!warning] What Happened / Qué pasó
> [The situation]

> [!tip] Takeaway / Aprendizaje
> [What we learned + what to do differently]

For **Decisions**, also include:
> [!quote] Decision / Decisión
> [What was decided]

**Why:** [The reasoning]
**Considered but rejected:** [Alternatives]

For **Ideas**, also include:
> [!note] The Idea / La idea
> [Description]

**Why it could work:** [Reasoning]
**Open questions:** [What needs to be figured out]

---

### Linking Strategy — Building the Graph

The Obsidian graph is the brain's nervous system. Every note must connect to the
network. This is NOT optional — isolated notes are dead notes.

**Rule: Every note gets at least 2 `[[wikilinks]]` to other notes in the vault.**

How to find links:

1. **Before writing any note,** scan the vault for existing notes on related topics.
   Use `Glob` to browse vault sections and `Grep` to search for keywords.
2. **Link forward:** Connect the new note to existing notes it references or builds on.
3. **Link backward:** After creating the new note, go back and ADD a link to it from
   the related existing notes. This is what makes the graph bidirectional.
4. **Link within the same session:** If you're creating multiple notes in one save,
   link them to each other where relevant.

**Where to place links:**
- In YAML frontmatter `related:` field (for Dataview queries)
- In the `*See also:*` line at the bottom of every note (for quick visual reference)
- Inline within the body text where a concept is mentioned
- In session logs, link to every knowledge nugget that was created in the same session

**Types of links to create:**

| Link type | Example | When to use |
|-----------|---------|-------------|
| **Topic link** | `[[What My Best Clients Have in Common]]` | When the note relates to an ongoing topic |
| **Decision link** | `[[2026-05-15 Decision — Switched Note Apps]]` | When referencing a past decision |
| **Session link** | `[[2026-05-28 — Built First Custom Skill]]` | When referencing the session where something happened |
| **Skill link** | `[[save-to-obsidian Skill Architecture]]` | When referencing AI system components |
| **Person/team link** | `[[Alex — Frequent Collaborator]]` | When referencing a person with a vault note |
| **Aliased link** | `[[North Star\|my long-term vision]]` | When the display text should be more natural than the note title |

**Block references for precision linking:**

When linking to a specific section of a long note, use block references:
```markdown
See the relevant section in [[Brand Notes#Pillar 2: Clear Pricing]]
```

Or with block IDs:
```markdown
This follows the rule from [[Personal Rules^always-never]]
```

**When you can't find related notes:**
If the vault is still small and there aren't related notes yet, note what SHOULD
exist with a placeholder: `[[Downtown — Local Knowledge]]`. This creates
a red link in Obsidian that shows up in graph view as an unresolved node —
breadcrumbs for future knowledge to fill in.

**Updating old notes with new links:**
When creating a new note that relates to an existing note, ALWAYS go back and add
a link to the new note from the existing one. Use the `Edit` tool to append to
the existing note's `*See also:*` line or `related:` frontmatter. This is what
turns a folder of files into an interconnected brain.

---

## PART 2: Session Summary Log

This runs AFTER Part 1 (knowledge extraction). Every session gets a log file — even
if no knowledge nuggets were extracted. The session log captures the full story of
what happened so the user can go back to it later for context.

### Step 5 — Build the Session Summary

Create a single markdown file in `{{VAULT_PATH}}/06 Session Logs/` using this template.
Every section is required unless the session was too short to justify it.

```markdown
---
title: "Session — [Short Title]"
aliases:
  - "[Short Title]"
date: YYYY-MM-DD
type: session-log
tags:
  - session
  - [topic-tags]
---

# Session Summary — [Short Title of What We Did]

> [!info] Session Details
> **Date:** YYYY-MM-DD
> **Duration:** [Approximate — e.g., "~45 min" or "long session"]
> **Triggered by:** [What kicked off the session — the user's opening request or goal]

---

## What We Accomplished / Lo que logramos

[2-4 paragraph narrative of what was done, in chronological order. Write it like
a story — "The user wanted X, so we started by doing Y, which led to Z." Keep it
readable, not a bullet dump. Use [[wikilinks]] to reference vault notes, skills,
tools, and people throughout.]

---

## Key Decisions & Reasoning / Decisiones clave

[For each significant decision made during the session:]

> [!quote] [Decision Title]
> **Decision:** [What was decided]
> **Why:** [The reasoning — what factors drove this choice]
> **Alternatives considered:** [What else was on the table, if anything]

[Repeat for each decision. Skip if the session was pure execution with no choices.]

---

## Outputs & Deliverables

[List everything that was created, modified, or delivered:]

- **[Output name]** — [What it is, where it lives]
  - Path: `[file path or location]`

---

## Tools & Data Sources Used

[List every tool, MCP, skill, API, or data source that was part of the work:]

- **[Tool/Source name]** — [What it was used for]

---

## Reasoning Log

[For each major step, briefly explain the thinking:]

1. **[Step/Action]** — [Why we did it this way]
2. **[Step/Action]** — [Why we did it this way]

[Keep each entry to 1-2 sentences. Capture the "why" chain.]

---

## Lessons Learned / Aprendizajes

> [!tip] Takeaways
> [Anything surprising, wrong, or better than expected. If nothing stands out,
> write "Clean session — no notable surprises."]

---

## Open Items / Next Steps — Pendientes

- [ ] [Open item with enough context to act on later]

[If everything wrapped cleanly: "All tasks completed. No open items."]

---

## Knowledge Saved to Vault

[List what was saved in Part 1, using wikilinks:]

- [[Note Title]] → [vault section]
- [[Updated: Note Title]] → [vault section]

[If no knowledge nuggets were extracted: "Session was task execution only —
no new knowledge nuggets extracted."]

---

*Related sessions: [[YYYY-MM-DD — Previous Related Session Title]]*
*Related vault notes: [[Any existing note this session built on or connects to]]*
```

**Session log file naming:**
```
YYYY-MM-DD — [Short Title].md
```

Examples:
- `2026-05-28 — Set Up My Second Brain.md`
- `2026-05-28 — First Project Advisor Run.md`

If multiple sessions on the same day:
- `2026-05-28 (2) — Afternoon Follow-Up.md`

---

## Step 6 — Summarize What Was Saved

After creating everything, give the user a clear summary:

```
Saved to {{VAULT_NAME}}:

Knowledge nuggets:
- [Note title] → 01 Personal Knowledge / Lessons Learned
- [Note title] → 02 Strategy / Decision Log

Session log:
- [Session title] → 06 Session Logs

[Links to each file]
```

If the user's primary language is Spanish, give the summary in Spanish:

```
Guardado en {{VAULT_NAME}}:

Conocimiento extraído:
- [Título de nota] → 01 Personal Knowledge / Lessons Learned
- [Título de nota] → 02 Strategy / Decision Log

Log de sesión:
- [Título de sesión] → 06 Session Logs
```

If the conversation had no knowledge worth extracting but was still a productive
session, say so: "No standalone knowledge nuggets this session, but the full session
log is saved so you can reference what we did."

---

## Quality Standards

- **Be specific, not generic.** "We fixed 3 broken canonical tag errors in the SEO
  audit" beats "We did some SEO work."
- **Include real numbers.** If the session involved data, include the key figures.
- **Capture the user's voice.** If they said something memorable or made a strong
  statement about direction, quote it using `> [!quote]` callouts.
- **Don't pad.** A 15-minute quick task doesn't need a 3-page log. Scale the
  detail to the session's complexity.
- **Preserve language.** If the user mixes English and Spanish, preserve their
  phrasing — don't sanitize bilingual voice into one language.
- **Use Obsidian features.** Every note should use callouts, wikilinks, block
  references, proper frontmatter, and tags. Notes that look like plain markdown
  are not acceptable — they must be Obsidian-native.

---

## Edge Cases

**Very short session (quick Q&A or one small task):**
Skip knowledge extraction if there's nothing to extract. For the session log, use
a condensed format — collapse Decisions, Reasoning Log, and Lessons into a single
"Notes" section.

**Session with sensitive data (financials, client names, private info):**
Include the data. The vault is the user's private knowledge base.

**Multiple unrelated tasks in one session:**
Use sub-headers under "What We Accomplished" for each task, and organize the
Decisions/Reasoning sections by task.

**Non-project experimental session:**
This skill works in any session. If the user was experimenting outside their
project ecosystem and liked what was created (a skill, research, an approach),
save it. The vault is the single source of truth for everything.

**User points to something specific:**
If they say "save THAT part about the pricing," focus the knowledge extraction on
what they're pointing to. Still create the full session log.

**The vault isn't mounted:**
Tell the user. Ask them to grant access to the vault folder or mount it in their
tool. Never write files to the working directory as a workaround.

**Very long conversations:**
If early parts have scrolled out of context, use whatever transcript-retrieval
capability the host LLM provides (e.g., `read_transcript`, `list_sessions`) to
recover the full conversation before extracting knowledge.

**User is primarily Spanish-speaking:**
Write callouts, headings, and prose in Spanish. Keep YAML keys and inline tags
in English (they're parsed by tooling). Frontmatter property values can be in
Spanish.

---

## Vault Hygiene Rules (Non-Negotiable)

1. **Knowledge only.** Every file must be permanent knowledge or a session record.
   No temp files, no staging, no drafts-for-elsewhere.
2. **No duplicates.** Check before writing. Update existing notes, never create
   copies alongside them.
3. **No v2 files.** Edit the original or replace it entirely.
4. **Don't pollute the graph.** Every note should connect to the vault's purpose.
   Every note must have at least 2 wikilinks. No orphan nodes.
5. **Templates stay in `Templates/`.** Don't write to that folder.
6. **Excalidraw stays in `Excalidraw/`.** Visual diagrams go there.
7. **Session logs are standalone records.** They don't replace knowledge notes —
   they complement them. A decision captured in `02 Strategy/Decision Log/` is the
   permanent reference; the session log in `06 Session Logs/` is the full context
   of when and how that decision was made.
8. **Obsidian-native formatting only.** Every note must use YAML frontmatter, wikilinks,
   callouts, tags, and block references. Plain markdown is not acceptable.
