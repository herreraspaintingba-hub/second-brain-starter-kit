---
name: second-brain-init
description: >
  First-run setup skill for the Second Brain Starter Kit. Use this skill the
  very first time a user installs the kit — it creates their Obsidian vault,
  installs the three companion skills (obsidian-power-user, save-to-obsidian,
  project-advisor), writes their personalized CLAUDE.md, and runs a verification
  pass. Trigger when the user says "set up my second brain," "install the
  starter kit," "initialize my brain," "set up my vault," "configura mi segundo
  cerebro," "instala el starter kit," "inicializa mi cerebro," "configura mi
  bóveda," or when the user is in their first conversation with no
  CLAUDE.md present and asks how to get started. Also auto-trigger when the
  assistant detects that none of the other Second Brain skills have been
  configured yet (no `second_brain_initialized: true` marker in CLAUDE.md).
  This skill runs ONCE per brain. Re-running is safe but will prompt for
  confirmation before overwriting existing setup. Bilingual EN+ES.
version: 1.0.0
kit: Second Brain Starter Kit
language: en+es
---

# Second Brain — Init Skill

> **One-time setup.** This skill runs the first time you install the Second
> Brain Starter Kit. It builds your vault, installs the three companion skills,
> writes your personalized CLAUDE.md, and verifies everything works.
>
> **Setup único.** Esta skill corre la primera vez que instalas el Starter Kit.
> Construye tu bóveda, instala las tres skills compañeras, escribe tu CLAUDE.md
> personalizado, y verifica que todo funcione.

---

## When to run this skill / Cuándo correr esta skill

**Run once when:**
- The user is installing the Second Brain Starter Kit for the first time
- The user explicitly asks to "set up my brain" / "initialize the kit"
- No `CLAUDE.md` exists in the working directory, or it exists but lacks the marker `second_brain_initialized: true`

**Correr una vez cuando:**
- El usuario está instalando el Starter Kit por primera vez
- El usuario pide explícitamente "configura mi cerebro" / "inicializa el kit"
- No existe `CLAUDE.md` en el directorio de trabajo, o existe pero sin el marcador `second_brain_initialized: true`

**Do NOT re-run if:**
- `CLAUDE.md` exists and has `second_brain_initialized: true` — the brain is already set up
- The user is in a normal working session — they want a different skill (probably `save-to-obsidian` or `obsidian-power-user`)

If a partial setup is detected, offer to resume rather than restart.

---

## Triggers / Activadores

**English:**
- "set up my second brain"
- "install the starter kit"
- "initialize my brain"
- "set up my vault"
- "I just installed the kit"
- "start the setup"
- "first-time setup"

**Español:**
- "configura mi segundo cerebro"
- "instala el starter kit"
- "inicializa mi cerebro"
- "configura mi bóveda"
- "acabo de instalar el kit"
- "empieza el setup"
- "configuración inicial"

---

## Required: Load companion skills before writing files

Before creating any vault file or skill placement, load:

1. **`obsidian-power-user`** — provides the formatting standards used in CLAUDE.md, the seed CURRENT-CONTEXT.md note, and the vault templates.

This skill (`second-brain-init`) handles orchestration. `obsidian-power-user` handles the actual Obsidian-native formatting. Without it, the seed files will be plain markdown instead of vault-ready notes.

---

## Step 1 — Detect environment / Detectar entorno

Before asking anything, check:

```bash
# Is there a CLAUDE.md already?
ls "$WORKING_DIR/CLAUDE.md" 2>/dev/null

# Is there a vault folder hint?
ls "$WORKING_DIR" | grep -iE "vault|brain|obsidian"

# Is the user on macOS, Windows, Linux?
uname -s
```

Use the output to pre-fill defaults in Step 2 questions. Never assume — always confirm with the user.

---

## Step 2 — Six setup questions / Seis preguntas de configuración

Ask these via `AskUserQuestion` (or the equivalent multiple-choice mechanism in the host LLM). Ask one at a time, do not batch. Capture all six answers before moving on.

### Question 1 — Your name / Tu nombre

> **EN:** What should I call you?
> **ES:** ¿Cómo te llamo?

Free-text. Default: empty. Stores as `{{USER_NAME}}`.

### Question 2 — Your role or business / Tu rol o negocio

> **EN:** What do you do? (Optional — leave blank if personal use only.)
> **ES:** ¿A qué te dedicas? (Opcional — déjalo en blanco si es uso personal.)

Free-text. Default: empty. Stores as `{{BUSINESS_NAME}}`.

### Question 3 — Vault name / Nombre de la bóveda

> **EN:** What do you want to call your brain? Examples: "My Second Brain," "Knowledge Base," "[Your Name]'s Brain."
> **ES:** ¿Cómo quieres llamar a tu cerebro? Ejemplos: "Mi Segundo Cerebro," "Base de Conocimiento," "Cerebro de [Tu Nombre]."

Free-text. Default: `"My Second Brain"`. Stores as `{{VAULT_NAME}}`.

### Question 4 — Vault location / Ubicación de la bóveda

> **EN:** Where should the vault live? Most users pick iCloud or Dropbox so it syncs across devices.
> **ES:** ¿Dónde quieres guardar la bóveda? La mayoría elige iCloud o Dropbox para que sincronice entre dispositivos.

Options:
1. iCloud Drive (`~/Library/Mobile Documents/com~apple~CloudDocs/{{VAULT_NAME}}`) — Recommended for macOS
2. Dropbox (`~/Dropbox/{{VAULT_NAME}}`) — Cross-platform
3. Documents folder (`~/Documents/{{VAULT_NAME}}`) — Local only
4. Custom path — User enters absolute path

Stores as `{{VAULT_PATH}}`.

### Question 5 — Primary language / Idioma principal

> **EN:** Which language should the brain default to? (Skills work in both — this just sets the default for outputs and labels.)
> **ES:** ¿Qué idioma debe usar el cerebro por defecto? (Las skills funcionan en ambos — esto solo configura el default de outputs y etiquetas.)

Options: EN / ES / Both at parity. Stores as `{{PRIMARY_LANGUAGE}}`.

### Question 6 — Notion integration / Integración con Notion

> **EN:** Do you also use Notion? If yes, some skills can mirror outputs there. If no, everything stays in Obsidian.
> **ES:** ¿También usas Notion? Si sí, algunas skills pueden reflejar outputs ahí. Si no, todo queda en Obsidian.

Options: Yes / No / Maybe later. Stores as `{{NOTION_ENABLED}}` (boolean).

---

## Step 3 — Create vault folder structure / Crear estructura de carpetas

Create the vault at `{{VAULT_PATH}}` with this exact structure:

```
{{VAULT_NAME}}/
├── 00 Inbox/
├── 01 Personal Knowledge/
│   ├── People/
│   ├── Places/
│   ├── Routines/
│   └── Lessons Learned/
├── 02 Strategy/
│   ├── Vision/
│   ├── Goals/
│   ├── Decision Log/
│   └── North Star/
├── 03 Ideas & Notes/
├── 04 Learning/
│   ├── Books/
│   ├── Courses/
│   ├── AI & Tech/
│   └── Business/
├── 05 AI System/
│   ├── Skills/
│   ├── Integrations/
│   └── Architecture/
├── 06 Session Logs/
├── Templates/
└── Excalidraw/
```

> **Note on naming:** The vault sections use generic names by default. Users with a business focus may want to rename "01 Personal Knowledge" → "01 Company Knowledge" later — that's fine. The skills resolve the section by number prefix (`01`, `02`, etc.), not by full name.

After creating folders, write a `.obsidian-vault-marker` file in the root so other tools can detect this is a managed vault.

---

## Step 4 — Install the 3 companion skills / Instalar las 3 skills compañeras

Copy the following skill folders into the user's skills directory:

| Skill | Source (in kit) | Destination |
|-------|-----------------|-------------|
| `obsidian-power-user` | `kit/skills/obsidian-power-user/` | `{{SKILLS_DIR}}/obsidian-power-user/` |
| `save-to-obsidian` | `kit/skills/save-to-obsidian/` | `{{SKILLS_DIR}}/save-to-obsidian/` |
| `project-advisor` | `kit/skills/project-advisor/` | `{{SKILLS_DIR}}/project-advisor/` |

**Skills directory by host:**

| Host | Skills directory |
|------|-----------------|
| Claude Code / Cowork | `~/.claude/skills/` |
| Codex | `~/.codex/skills/` |
| Gemini CLI | `~/.gemini/skills/` |
| OpenCloud | User-configured path |
| Other | Ask the user where their LLM loads skills from |

If the user is unsure, ask them to check their LLM's documentation. The kit is portable — it ships as a folder, not a plugin.

---

## Step 5 — Write personalized CLAUDE.md / Escribir CLAUDE.md personalizado

Write `{{WORKING_DIR}}/CLAUDE.md` using this template, filling all `{{ }}` placeholders from Step 2 answers:

```markdown
# {{VAULT_NAME}} — Brain Configuration

> This file configures how the Second Brain Starter Kit operates for {{USER_NAME}}.
> It is read at the start of every conversation. Keep it updated when context changes.

second_brain_initialized: true
initialized_date: {{TODAYS_DATE}}
kit_version: 1.0.0

## Owner / Dueño

- **Name / Nombre:** {{USER_NAME}}
- **Role / Rol:** {{BUSINESS_NAME}}
- **Primary language / Idioma principal:** {{PRIMARY_LANGUAGE}}

## Vault / Bóveda

- **Name / Nombre:** {{VAULT_NAME}}
- **Path / Ruta:** {{VAULT_PATH}}
- **Notion integration enabled / Integración Notion:** {{NOTION_ENABLED}}

## Installed skills / Skills instaladas

- `second-brain-init` — One-time setup (this skill)
- `obsidian-power-user` — Master Obsidian skill
- `save-to-obsidian` — Capture knowledge to the vault
- `project-advisor` — Evaluate ideas before committing

## Trigger phrases / Frases de activación

- **Save knowledge / Guardar conocimiento:** "save to my brain" / "guárdalo en mi cerebro"
- **Evaluate a project / Evaluar un proyecto:** "should I do this?" / "¿debería hacer esto?"
- **Write to vault / Escribir en la bóveda:** any mention of the vault triggers `obsidian-power-user` formatting standards

## Routing rules / Reglas de routing

When the user asks to "save to my brain" → load `save-to-obsidian`.
When the user describes a new project idea → load `project-advisor`.
When writing any file inside the vault → always load `obsidian-power-user` first for formatting.
When the user asks about Obsidian features (canvas, base, Dataview, etc.) → load `obsidian-power-user`.

## North Star / Estrella polar

> Edit this section to capture your long-term vision. Skills like `project-advisor`
> use it to evaluate whether new ideas align with what you're building toward.

(empty — fill this in after a few weeks of use)

## How to extend this file

As you use the kit, the brain will learn more about you. Update this file with:
- People who matter (clients, team, collaborators)
- Recurring projects
- Vocabulary specific to your work
- Trigger phrases you prefer

Keep this file under 200 lines — long contexts cost tokens. Move detailed knowledge
into the vault instead.
```

---

## Step 6 — Seed CURRENT-CONTEXT.md / Sembrar CURRENT-CONTEXT.md

Write `{{VAULT_PATH}}/CURRENT-CONTEXT.md` as a rolling summary file the user updates over time:

```markdown
---
title: "Current Context"
type: meta
updated: {{TODAYS_DATE}}
---

# Current Context — {{USER_NAME}}'s Brain

> What's happening right now. Update this file weekly. It's the first thing
> every Claude session reads to get oriented.

## Active projects

- (none yet — add as you start things)

## This week's focus

- (set this on Monday)

## Open questions

- (capture things you want to think about but haven't resolved)

## Recent decisions

- (link to notes in `02 Strategy/Decision Log/` as you make them)

---

*This file is intentionally short. Detailed knowledge lives in the vault sections.*
```

---

## Step 7 — Verification / Verificación

Run three checks and report results to the user:

```bash
# 1. Vault structure
test -d "{{VAULT_PATH}}/00 Inbox" && echo "✅ Vault created" || echo "❌ Vault missing"

# 2. Skills installed
for skill in obsidian-power-user save-to-obsidian project-advisor; do
  test -f "{{SKILLS_DIR}}/$skill/SKILL.md" \
    && echo "✅ $skill installed" \
    || echo "❌ $skill missing"
done

# 3. CLAUDE.md written
grep -q "second_brain_initialized: true" "{{WORKING_DIR}}/CLAUDE.md" \
  && echo "✅ CLAUDE.md configured" \
  || echo "❌ CLAUDE.md not configured"
```

If any check fails, walk the user through the fix before declaring setup complete.

---

## Step 8 — First-action suggestion / Sugerencia de primera acción

After verification passes, give the user one concrete next step:

> **EN:** Your brain is ready. Try this: have a normal conversation about something you're working on, and at the end say "save to my brain." I'll extract the useful knowledge into your vault and write a session log.
>
> **ES:** Tu cerebro está listo. Prueba esto: ten una conversación normal sobre algo en lo que estés trabajando, y al final di "guárdalo en mi cerebro." Yo extraigo el conocimiento útil hacia tu bóveda y escribo un session log.

Do not suggest more than one next action. Overwhelm kills adoption.

---

## Step 9 — Save the setup session itself / Guardar la sesión de setup

Load `save-to-obsidian` and write a session log in `{{VAULT_PATH}}/06 Session Logs/` titled:

```
{{TODAYS_DATE}} — Second Brain Initial Setup.md
```

The log captures: the 6 answers, what was installed, where it lives, and any decisions the user made along the way. This becomes the historical record of how their brain was born.

---

## Edge cases / Casos especiales

**The user already has an Obsidian vault and wants to use it:**
- Skip Step 3 (vault creation)
- Detect the existing structure
- Add missing folders (`00 Inbox` through `06 Session Logs`) without deleting anything
- Warn the user: "Your existing notes weren't moved. The kit adds new sections alongside what you have."

**The user is on Windows / Linux / Codex / Gemini:**
- Path conventions differ — use the host's native conventions
- iCloud option in Question 4 becomes "OneDrive" on Windows or hides on Linux
- Skill directory in Step 4 depends on the host

**The user doesn't have Obsidian installed yet:**
- The kit doesn't depend on Obsidian.app being installed — it just writes markdown files
- After setup, tell the user: "These are plain markdown files. You can open them in any editor, but Obsidian gives you the graph view and linking that makes this a real brain. Install it from obsidian.md when you're ready."

**The user re-runs `second-brain-init` accidentally:**
- Detect `second_brain_initialized: true` in CLAUDE.md
- Stop and ask: "Your brain is already set up. Do you want to (A) keep what you have, (B) update specific answers, or (C) start over from scratch?"
- Never silently overwrite

**The user wants to migrate from Notion / Apple Notes / Evernote later:**
- Out of scope for this skill — point them to `obsidian-power-user` and the kit's PDF manual

---

## Output format / Formato de output

When the skill is running, talk plainly. No emoji unless the user uses them first. Show progress as concrete steps ("Creating vault at /path...", "Installing obsidian-power-user...") not as percentages or progress bars.

When the skill finishes, give exactly three things:

1. A one-paragraph confirmation in the user's primary language
2. The list of verification check results (✅ / ❌)
3. The single suggested next action (Step 8)

Nothing else. Setup is over. Get out of the way.

---

## What this skill does NOT do / Lo que esta skill NO hace

- It does not customize the other 3 skills — sanitization is the kit author's job, not the user's
- It does not write actual knowledge into the vault — that's `save-to-obsidian`'s job
- It does not configure third-party tools (Notion connectors, MCP servers) — out of scope for v1.0
- It does not run periodically — runs once, then never again
- It does not validate the user's CLAUDE.md edits over time — the user owns their config
