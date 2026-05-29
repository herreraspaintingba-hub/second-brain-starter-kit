---
name: project-advisor
description: >
  Evaluates new project ideas BEFORE committing execution time. Use whenever the
  user brings an idea, skill, automation, SOP, or workflow and wants to decide if
  it's worth building now. Triggers on "let's analyze this project," "analicemos
  este proyecto," "is this worth working on," "vale la pena este proyecto,"
  "should I build this," "should I do this," "before I invest more time," "analyze
  this idea," "analiza esta idea," "evaluate this project," "evalúa este
  proyecto," "run this through the advisor," or any English/Spanish variation of
  wanting structured evaluation of a new idea. Auto-pulls vault context, runs a
  7-question Socratic sequence, scores on 4 weighted dimensions (Systemization,
  North Star Alignment, Revenue/Cost, Timing), delivers GREEN/YELLOW/RED verdict,
  and writes to the vault Decision Log + an optional Notion database + a .docx
  brief. The ONLY skill for pre-work project evaluation. Bilingual EN+ES.
kit: Second Brain Starter Kit
version: 1.0.0
language: en+es
---

# Project Advisor

The single source of truth for deciding whether an idea becomes a project.

Users generate ideas constantly — some are gold, some aren't the right fit right now,
and some shouldn't be built at all. This skill's job is to catch every idea before
it consumes time, force it through a repeatable evaluation, and give a clear verdict
backed by the user's own documented priorities (their North Star).

It does NOT execute the project. It decides whether to execute it.

---

## Triggers / Activadores

**English:**
- "Let's analyze this project"
- "Let's make sure this project helps me improve"
- "Is this worth working on?"
- "Should I build this?"
- "Should I do this?"
- "Should we commit time to this?"
- "Before I invest more time in this"
- "Analyze this idea"
- "Evaluate this project"
- "Is this the right move?"
- "I have an idea — help me think through it"
- "Run this through the advisor"

**Español:**
- "Analicemos este proyecto"
- "¿Vale la pena este proyecto?"
- "Analiza esta idea"
- "Evalúa este proyecto"
- "¿Debería hacer esto?"
- "¿Es el momento correcto?"
- "Antes de invertir más tiempo"
- "¿Vale la pena trabajar en esto?"

**Intent-based triggers (fire even without exact wording):**
- The user describes an idea and then pauses asking for judgment
- The user compares two possible projects and asks which to start
- The user is about to start executing something new and hasn't run it through an evaluation yet

**Do NOT use for:** executing a project (use the relevant execution skill), creating
a process doc (use the user's SOP skill if they have one), or building a skill
(use a skill-creator skill if available). Advisor evaluates BEFORE those skills
are called.

---

## The Framework

Four phases, executed in order. Never skip a phase.

```
Phase 1: CONTEXT PULL   →  Auto-read vault files so the advisor walks in informed
Phase 2: QUESTIONING    →  Socratic sequence to surface what the idea actually is
Phase 3: SCORING        →  4-dimension weighted scorecard (out of 10)
Phase 4: OUTPUT         →  Verdict + write to up to 3 destinations
```

---

## Phase 1 — Auto-Context Pull

Before asking the user anything, you MUST read these vault files. This is non-negotiable
— it's what separates advice from speculation.

**Always read (the core 4):**

1. `02 Strategy/North Star/` — the user's guiding vision (whatever they call it)
2. `02 Strategy/Vision/` — long-term aspiration
3. `02 Strategy/Goals/` — current time-bound objectives
4. The most recent file in `06 Session Logs/` — for continuity with prior work

**Conditionally read (if the idea domain matches):**

| If the idea touches… | Also read… |
|----------------------|------------|
| Pricing, offers, packaging | `01 Personal Knowledge/Routines/` (relevant SOPs) |
| Content, marketing, audience | `04 Learning/Business/` and any marketing notes in `04 Learning/` |
| Team, collaborators, delegation | `01 Personal Knowledge/People/` |
| A new skill or automation | `05 AI System/Skills/` and `05 AI System/Architecture/` |
| A decision that reverses or modifies a past one | `02 Strategy/Decision Log/` (search for related entries) |
| Business operations | `01 Personal Knowledge/Routines/` (relevant SOPs) |

**Also check:** Has the user brought up a similar idea before? Search `03 Ideas & Notes/`
for overlap. If a prior note exists, open it and merge context into the new evaluation
instead of starting fresh.

**How to present context:** Do NOT dump the file contents back to the user. Absorb the
context silently, then reference it only when it matters to the evaluation ("Your
{{NORTH_STAR_NAME}} note lists X as a priority — this idea supports that").

---

## Phase 2 — Socratic Questioning

Ask these questions IN ORDER. Use the host LLM's question-asking mechanism
(e.g., `AskUserQuestion`) one question at a time — not all at once. Each answer
should inform the next. Match the user's language (English or Spanish).

### Q1 — The Core Idea / La idea central

> **EN:** In one sentence, what is this project?
> **ES:** En una sola oración, ¿qué es este proyecto?

If the user rambles, play it back to them in one sentence and confirm.

### Q2 — The Problem / El problema

> **EN:** What specific problem does this solve? Whose problem is it — yours, a teammate's, a customer's, or the system itself?
> **ES:** ¿Qué problema específico resuelve esto? ¿De quién es el problema — tuyo, de un colaborador, de un cliente, o del sistema mismo?

Offer options: You / Teammate / Client / Operations / The brain system / Other.

### Q3 — The Current Workaround / El workaround actual

> **EN:** How is this problem being handled right now? Manually? Not at all? By another system?
> **ES:** ¿Cómo se está manejando este problema ahora? ¿Manualmente? ¿No se está manejando? ¿Por otro sistema?

This reveals whether the idea replaces something painful (high value) or creates a
new category of work (lower value unless strategic).

### Q4 — The Outcome / El resultado

> **EN:** What does success look like in 90 days? Be specific — a number, time saved, revenue, a new capability.
> **ES:** ¿Cómo se ve el éxito en 90 días? Sé específico — un número, tiempo ahorrado, ingresos, una nueva capacidad.

If they can't answer, that's a signal — the idea isn't ready to build yet
(YELLOW territory).

### Q5 — The Cost / El costo

> **EN:** What will it take to build this? Time, money, tools, outside help. Rough estimate is fine.
> **ES:** ¿Qué se necesita para construir esto? Tiempo, dinero, herramientas, ayuda externa. Una estimación aproximada está bien.

Offer options: Under 4 hours / 4–20 hours / 20–80 hours / 80+ hours / I don't know yet.

### Q6 — The Tradeoff / La negociación

> **EN:** If we build this now, what DOESN'T get built? What are you saying no to?
> **ES:** Si construimos esto ahora, ¿qué NO se construye? ¿A qué le estás diciendo que no?

This is the most important question. Every yes is a no to something else.

### Q7 — The Fit (only if unclear after Q1–Q6) / El encaje

> **EN:** Which part of your life or work does this strengthen most — finances, output, learning, relationships, or the brain itself?
> **ES:** ¿Qué parte de tu vida o trabajo fortalece más esto — finanzas, producción, aprendizaje, relaciones, o el cerebro mismo?

Skip if already obvious from the conversation.

---

## Phase 3 — The Scorecard

Score the idea on 4 dimensions, 1–10 each. Weights sum to 100%.

| Dimension | Weight | What it measures |
|-----------|--------|------------------|
| **Systemization** | 25% | Does this turn manual, repeated work into a reusable system, SOP, or skill? |
| **{{NORTH_STAR_NAME}} Alignment** | 30% | Does it advance the user's long-term vision? |
| **Revenue / Cost Impact** | 25% | Does it generate revenue, reduce cost, or prevent expensive mistakes? |
| **Timing** | 20% | Is this the right moment — current capacity, season, competing priorities? |

The North Star is weighted highest because it is the user's guiding vision. Timing
is weighted lowest because even great ideas that are slightly mistimed can be
re-opened later — this skill preserves them in the vault for exactly that reason.

> **Note:** `{{NORTH_STAR_NAME}}` is set in `CLAUDE.md` during `second-brain-init`.
> If the user hasn't named their North Star yet, use the generic label
> "North Star Alignment" and prompt them to name it after the run.

### Scoring Rubric

For each dimension, use this rubric:

| Score | Meaning |
|-------|---------|
| **9–10** | Bullseye. Perfect alignment. Rare. |
| **7–8** | Strong. Clear fit with real impact. |
| **5–6** | Mixed. Some signal, some noise. |
| **3–4** | Weak. Minor or indirect value. |
| **1–2** | Negative or absent. Fails this dimension. |

### Scoring Guidance by Dimension

**Systemization (25%)**
- 9–10: Replaces a weekly-or-more manual task with an automated system
- 7–8: Builds a reusable asset (SOP, skill, template) that compounds
- 5–6: Improves a process but doesn't eliminate manual work
- 3–4: One-time fix with no reusable output
- 1–2: Adds manual work or creates a new category of ongoing effort

**{{NORTH_STAR_NAME}} Alignment (30%)**
- 9–10: Directly advances the user's guiding vision — closes a gap they've named as critical
- 7–8: Supports an existing pillar of the vision
- 5–6: Tangentially related — helps in general but doesn't move the vision forward
- 3–4: Operates outside the vision entirely
- 1–2: Distracts from or fragments the vision

**Revenue / Cost Impact (25%)**
- 9–10: Clear path to substantial new revenue OR substantial hours saved per week
- 7–8: Measurable revenue or cost improvement
- 5–6: Indirect impact (brand, positioning, faster response)
- 3–4: No clear financial link
- 1–2: Costs money or time with no return

**Timing (20%)**
- 9–10: Fits current capacity, leverages current season, no blocking dependencies
- 7–8: Fits with minor reshuffling
- 5–6: Would work but pulls focus from something higher-priority
- 3–4: Competes with an in-flight priority
- 1–2: Wrong season, wrong capacity, or requires something that doesn't exist yet

### Compute the Weighted Score

```
Final = (Systemization × 0.25) + (NorthStar × 0.30) + (Revenue × 0.25) + (Timing × 0.20)
```

Show the math in the output — don't just show the final number.

### Verdict Thresholds

| Weighted Score | Verdict | Meaning |
|----------------|---------|---------|
| **7.5 – 10.0** | 🟢 **GREEN — Build it** | Move into execution. Open the relevant skill next. |
| **5.0 – 7.4**  | 🟡 **YELLOW — Refine first** | Idea has merit but something's missing. Advisor writes what specifically needs to change before re-scoring. |
| **0 – 4.9**    | 🔴 **RED — Shelve it** | Don't build now. Archived in the vault with reasoning so it can be reopened later if conditions change. |

**Override rule:** If {{NORTH_STAR_NAME}} scores 9 or 10 AND weighted score is ≥ 5.0,
bump to GREEN regardless of timing. Vision-critical ideas don't wait.

**Veto rule:** If Timing scores 1 or 2, cap verdict at YELLOW no matter what.
Wrong-time ideas are not build-now ideas.

---

## Phase 4 — Output Protocol

Write to up to three destinations. Obsidian is always required; Notion is optional;
the .docx brief is always generated.

### Destination 1 — Obsidian `03 Ideas & Notes/` (always)

Create a new note named: `{YYYY-MM-DD} — {Idea Name}.md`

Use this template:

```markdown
---
created: {{date}}
verdict: {{GREEN | YELLOW | RED}}
score: {{weighted_score}}/10
tags: [project-advisor, {{domain-tag}}, verdict-{{green|yellow|red}}]
---

# {{Idea Name}}

## The Idea
{{one-sentence version from Q1}}

## The Problem
{{from Q2 — who it's for}}

## Current Workaround
{{from Q3}}

## 90-Day Outcome
{{from Q4}}

## Estimated Cost
{{from Q5}}

## What It Displaces
{{from Q6}}

## Life/Work Fit
{{from Q7 or inferred}}

---

## Scorecard

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| Systemization | {{s}}/10 | 25% | {{s*.25}} |
| {{NORTH_STAR_NAME}} | {{n}}/10 | 30% | {{n*.30}} |
| Revenue/Cost | {{r}}/10 | 25% | {{r*.25}} |
| Timing | {{t}}/10 | 20% | {{t*.20}} |
| **TOTAL** | | | **{{weighted}}/10** |

## Verdict: {{GREEN | YELLOW | RED}}

{{2-4 sentences explaining WHY, referencing vault context pulled in Phase 1}}

## Next Steps
- {{specific action 1}}
- {{specific action 2}}
- {{specific action 3}}

## Related Notes
- [[{{any related idea or decision from vault search}}]]
```

### Destination 2 — Obsidian `02 Strategy/Decision Log/` (GREEN or RED only)

Only create a Decision Log entry if verdict is **GREEN** or **RED** (both are real
go/no-go decisions). YELLOW is a "not yet," not a decision — skip the log.

File name: `{YYYY-MM-DD} — Decision — {Idea Name}.md`

Template:

```markdown
---
date: {{date}}
type: project-advisor-decision
verdict: {{GREEN | RED}}
idea-link: [[03 Ideas & Notes/{{date}} — {{Idea Name}}]]
---

# Decision: {{Build | Shelve}} — {{Idea Name}}

## What Was Decided
{{one sentence}}

## Why
{{3-5 bullets with the reasoning — score summary + vault context}}

## What We're Saying No To (if GREEN)
{{from Q6 — the displaced work}}

## When to Revisit (if RED)
{{condition under which this could come back — e.g., "After Q3" or "If capacity opens"}}

## Linked Idea Note
[[03 Ideas & Notes/{{date}} — {{Idea Name}}]]
```

### Destination 3 — Optional Notion Mirror

**Only fires if Notion integration is enabled** (`{{NOTION_ENABLED}}: true` in
`CLAUDE.md`) AND the verdict is GREEN. If Notion isn't enabled, skip this step
entirely — the Obsidian outputs are sufficient.

If enabled, ask the user once for their Notion projects database ID and store it
in `CLAUDE.md` as `{{NOTION_PROJECTS_DB}}`. On subsequent runs, use the stored ID
without re-asking.

Suggested fields to populate (adapt to the user's actual database schema):

| Field | Value source |
|-------|--------------|
| Project Name | The idea name (title) |
| Verdict | `🟢 GREEN` |
| Status | `Not started` |
| Priority | P1–P4 based on advisor judgment + weighted score |
| Start Date | Today |
| Due Date | Today + estimated calendar weeks from Q5 |
| Estimated Hours | From Q5 (midpoint of range) |
| Score — Systemization | Raw 1–10 score |
| Score — North Star | Raw 1–10 score |
| Score — Revenue/Cost | Raw 1–10 score |
| Score — Timing | Raw 1–10 score |
| Weighted Score | Computed |
| 90-Day Outcome | From Q4 |
| Obsidian Idea Note | URL to the `03 Ideas & Notes/` entry |
| Decision Log Link | URL to the `02 Strategy/Decision Log/` entry |

### Destination 4 — Printable `.docx` Brief (always)

Always generate. Save to the user's working directory (or their selected output
folder) so they can view, share, or print.

File name: `Project Advisor Brief — {{Idea Name}} — {{date}}.docx`

Structure:
1. **Cover** — Idea name, verdict badge, date, weighted score
2. **Executive Summary** — 3 sentences: what, verdict, why
3. **The Idea** (Q1–Q7 answers, cleanly formatted)
4. **Scorecard** (table with all 4 dimensions + weighted math)
5. **Vault Context Applied** — which files were consulted and what they said
6. **Verdict & Reasoning** — 1/2 page
7. **Next Steps** — numbered list
8. **Revisit Criteria** (if YELLOW or RED) — what would need to change

Use the host LLM's docx-generation skill (e.g., a `docx` skill) to produce this.
If the user has a brand-voice skill, apply it to the prose sections.

---

## Operating Rules

1. **Never skip Phase 1.** Walking in without context produces generic advice. The vault has the answers.
2. **Never ask all 7 questions at once.** One at a time — each answer shapes the next.
3. **Show the scoring math.** Users learn from seeing the weights applied, not just the final number.
4. **Be honest with RED.** If an idea shouldn't be built, say so clearly and kindly. A shelved idea preserved in the vault is more valuable than a half-built one that drains attention.
5. **Language-match.** If the user opens in Spanish, evaluate in Spanish. Match their energy.
6. **No stacking with other skills.** Advisor runs BEFORE execution skills. Do not also trigger build skills or content skills inside the same run — recommend the next skill in the verdict, then stop.
7. **Session log it.** The advisor run is worth a session log entry. At the end, offer to run `save-to-obsidian`.

---

## Example Run

> **User:** "Let's analyze this project — I want to build a weekly email digest of everything new in my industry, auto-summarized."

> **Advisor (silent):** Reads the 4 core vault files. Notices the North Star file mentions "stay current with the field without doom-scrolling" as a pillar. Notices an existing note in `03 Ideas & Notes/` about an RSS reader setup. Notices the user's last session log shows they're heads-down on a launch this week.

> **Advisor (to user):** "In one sentence — this is an automated weekly industry digest that replaces manual scrolling with a single summary email. Is that right?"

(…continues through Q2–Q7, scores, delivers verdict, writes outputs…)

> **Verdict:** 🟡 YELLOW — 6.4/10.
> - Systemization 8 (high — automates a manual habit)
> - North Star 9 (directly serves the "stay current without doom-scrolling" pillar)
> - Revenue/Cost 4 (no direct revenue link)
> - Timing 3 (user is mid-launch — wrong week to add a side project)
>
> **Override rule check:** North Star = 9 AND weighted ≥ 5.0 → would bump to GREEN.
> **Veto rule check:** Timing = 3, not 1–2 → no veto.
> **Result:** GREEN by override.
>
> **Next skill recommended:** the relevant skill-building or automation skill.

---

## Verification Checklist

Before closing out an advisor run, verify:

- [ ] All 4 core vault files were read (or the session log notes why any were skipped)
- [ ] All 7 questions were answered or explicitly skipped with reason
- [ ] All 4 scorecard dimensions have a score AND a one-line justification
- [ ] Weighted math is shown
- [ ] Verdict respects override and veto rules
- [ ] Obsidian idea note is created (all verdicts)
- [ ] Decision Log is created (GREEN/RED only)
- [ ] Notion entry is created (GREEN only AND Notion enabled)
- [ ] .docx brief is saved to the working directory
- [ ] Next-skill recommendation is named (or "none — shelve")

---

## Relationship to Other Skills

- **`save-to-obsidian`** — Called at the end of every advisor run. Captures the
  evaluation as a session log so the reasoning is preserved.
- **`obsidian-power-user`** — Loaded by the advisor when writing the idea note
  and Decision Log entry, so the output follows Obsidian-native formatting.
- **`second-brain-init`** — Must have already run; the advisor depends on the
  vault structure and the `{{NORTH_STAR_NAME}}` placeholder being configured.
