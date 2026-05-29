# Obsidian Files & Folders Reference

Complete guide to file formats, configuration structures, and folder organization patterns in Obsidian.

---

## Accepted File Formats

Obsidian supports a wide range of file types natively and through plugins. Below is the comprehensive reference:

| Category | Formats | Notes |
|---|---|---|
| **Notes** | `.md` | Markdown format. The primary note-taking format in Obsidian. Plain text, version-control friendly. |
| **Database** | `.base` | Obsidian Publish database format (not commonly used locally). Limited support. |
| **Canvas** | `.canvas` | Obsidian Canvas files. JSON-based visual workspaces for connecting notes and media. |
| **Documents** | `.pdf` | Embeddable in notes. Searchable with plugins. |
| **Images** | `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`, `.webp`, `.bmp` | Embed with `![[filename]]` syntax. SVG is resizable. |
| **Audio** | `.mp3`, `.wav`, `.ogg`, `.m4a`, `.flac` | Playback embedded in notes. Requires audio-capable plugin. |
| **Video** | `.mp4`, `.webm`, `.ogv`, `.mov`, `.mkv` | Embed with `![](filename)` syntax. Browser support varies by format. |

**Obsidian Index**: All vault files are indexed except those matching `.gitignore` patterns and files in `.obsidian/` (except themes and snippets).

---

## Configuration Folder: `.obsidian/`

The `.obsidian/` directory is a hidden folder (prefixed with `.`) at the vault root. It contains all Obsidian-specific configuration, plugins, themes, and metadata.

### Directory Structure

```
vault-root/
└── .obsidian/
    ├── app.json                    # Core app settings
    ├── appearance.json             # UI appearance (font, theme, sidebars)
    ├── hotkeys.json                # Custom keyboard shortcuts
    ├── core-plugins.json           # Enabled/disabled core plugins
    ├── community-plugins.json       # Third-party plugin registry
    ├── plugins/                    # Community plugin installations
    │   ├── obsidian-dataview/      # Example: Dataview plugin
    │   ├── obsidian-tasks-plugin/  # Example: Tasks plugin
    │   └── [plugin-id]/
    │       ├── manifest.json       # Plugin metadata
    │       ├── main.js             # Plugin code
    │       └── data.json           # Plugin-specific settings
    ├── snippets/                   # CSS custom snippets
    │   ├── custom-theme.css        # Example: custom styles
    │   ├── dark-mode-override.css
    │   └── [snippet-name].css
    ├── themes/                     # Community themes
    │   ├── Minimal/                # Example: Minimal theme
    │   │   ├── manifest.json
    │   │   ├── theme.css
    │   │   └── obsidian.css
    │   └── [theme-name]/
    ├── graph.json                  # Graph view settings
    ├── workspaces.json             # Saved workspace layouts
    ├── sync.json                   # Obsidian Sync settings (if enabled)
    ├── publish.json                # Obsidian Publish settings (if enabled)
    └── vault-stats.json            # Vault statistics
```

### Key Configuration Files

#### `app.json`
Controls core Obsidian behavior:
- Default note-creation location
- Auto-save interval
- Link format (markdown or wiki-style)
- Tab width and indentation
- Spellcheck language
- Mobile-specific settings

#### `appearance.json`
Controls UI aesthetics:
- Active theme name
- Font (default and monospace)
- Font size (12-20px)
- Line width and height
- Sidebar visibility
- Accent color
- Dark/light mode settings

#### `hotkeys.json`
Custom keyboard shortcuts. Stores overrides of default hotkeys:
```json
{
  "obsidian:open-quick-switcher": [
    {
      "modifiers": ["Mod", "P"],
      "key": "P"
    }
  ],
  "editor:toggle-bold": [
    {
      "modifiers": ["Mod"],
      "key": "b"
    }
  ]
}
```

#### `core-plugins.json`
Toggles built-in plugins on/off:
- File explorer
- Search
- Backlinks panel
- Tags panel
- Outline
- Daily notes
- Graph view
- Canvas
- Command palette
- etc.

#### `community-plugins.json`
Registry of installed third-party plugins and their settings.

#### `plugins/` Directory
Each installed community plugin gets its own subdirectory containing:
- `manifest.json`: Plugin metadata (name, version, author)
- `main.js`: Compiled plugin code
- `data.json`: Plugin-specific settings (if applicable)

#### `snippets/` Directory
CSS override files loaded after theme CSS. Allows per-vault style customization without modifying themes.

**Example use cases:**
- Adjust heading sizes
- Change table styling
- Customize link colors
- Add custom font weights
- Adjust sidebar width

#### `themes/` Directory
Community theme packages. Each theme includes:
- `manifest.json`: Theme metadata
- `theme.css`: Main theme styles
- `obsidian.css`: Compatibility layer (optional)

### Hidden Configuration Files

Obsidian also creates these without user interaction:
- `.DS_Store` (macOS metadata)
- `Thumbs.db` (Windows metadata)
- `.obsidian-cache-metadata` (internal metadata cache)

---

## Core Concepts

### 1. Notes Are Plain Text
All Obsidian notes are stored as plaintext `.md` files. This means:
- **No lock-in**: Open notes in any text editor
- **Version control**: Use Git, Mercurial, etc. directly
- **Portability**: Copy the vault folder anywhere
- **Durability**: Will be readable for decades
- **Searchable**: Use command-line tools (`grep`, `ripgrep`) on the vault

### 2. Vault = Folder on Filesystem
A "vault" is simply a folder containing `.md` files and a `.obsidian/` configuration directory. Multiple vaults are independent folders.

**Example vaults:**
```
~/Vaults/Personal/
~/Vaults/Work/
~/Vaults/Research/
~/Documents/MySecondBrain/
```

Obsidian stores vault registry in:
- **macOS/Linux**: `~/.config/Obsidian/obsidian.json`
- **Windows**: `%APPDATA%\Obsidian\obsidian.json`

### 3. Symbolic Links and OS-Level Junctions
Obsidian vault folders can be:
- **Symbolic links** (`ln -s` on Unix, `mklink /D` on Windows): Point to another location
- **Hard folders**: Direct subdirectories
- **Cloud-synced**: Stored in Dropbox, iCloud, OneDrive, or Obsidian Sync
- **Git repositories**: Full version control with commit history

**Use cases for symbolic links:**
- Store vault on external SSD while keeping it accessible from standard location
- Share vault across multiple machines via cloud storage (with caution for sync conflicts)
- Separate active vault from archived vault while keeping both accessible

**Create a symbolic link:**
```bash
# Unix/macOS
ln -s /actual/vault/path ~/Vaults/vault-alias

# Windows PowerShell (admin)
New-Item -ItemType SymbolicLink -Path "C:\Users\User\Vaults\vault-alias" -Target "C:\actual\vault\path"

# Windows cmd (admin)
mklink /D "C:\Users\User\Vaults\vault-alias" "C:\actual\vault\path"
```

### 4. Indexing and `.gitignore`
Obsidian indexes all files in the vault except:
- Files matching patterns in a `.gitignore` file (if present)
- Files in `.obsidian/` (except themes and snippets)
- Temporary system files (`.DS_Store`, `Thumbs.db`)

**Example `.gitignore` for Obsidian vault:**
```
# OS files
.DS_Store
Thumbs.db
.obsidian/plugins/*/data.json

# Sensitive files
secrets.md
private/

# Build artifacts
*.tmp
*.log
```

---

## Folder Structure Archetypes

Each archetype below is designed for a specific use case. Choose the one that matches your workflow, or adapt one to your needs.

---

## Archetype 1: Personal PKM (Knowledge Management)

**For whom**: Individuals who want a simple, low-friction system to capture thoughts, store references, and retrieve information. Emphasis on capturing quickly (inbox), processing into atomic notes, and maintaining a growing reference library.

**Core principles**:
- **Inbox**: Capture fleeting thoughts without organizing
- **Daily Notes**: Chronological record
- **Notes**: Your atomic knowledge base
- **References**: External sources, reading lists, templates
- **Archives**: Old processed items

### Tree Diagram

```
vault-root/
├── Inbox/
│   ├── 2026-04-03.md              # Daily capture
│   ├── Random thoughts.md
│   └── Ideas to process.md
├── Daily Notes/
│   ├── 2026-04-03.md
│   ├── 2026-04-02.md
│   └── 2026-04-01.md
├── Notes/
│   ├── 01 - Writing/
│   │   ├── Hemingway's principles.md
│   │   ├── Short sentences.md
│   │   └── Active vs passive voice.md
│   ├── 02 - Productivity/
│   │   ├── Time blocking.md
│   │   ├── Deep work.md
│   │   └── Context switching costs.md
│   ├── 03 - Health/
│   │   ├── Sleep science.md
│   │   ├── Strength training.md
│   │   └── Nutrition basics.md
│   └── 04 - Technology/
│       ├── Git workflows.md
│       ├── REST APIs.md
│       └── Docker basics.md
├── References/
│   ├── Articles/
│   │   ├── Deep work - Newport.md
│   │   └── Atomic Habits - Clear.md
│   ├── Books/
│   │   ├── Thinking Fast and Slow.md
│   │   └── The Pragmatic Programmer.md
│   ├── People/
│   │   ├── Paul Graham.md
│   │   └── Naval Ravikant.md
│   ├── Templates/
│   │   ├── Book summary template.md
│   │   ├── Article summary template.md
│   │   └── Meeting notes template.md
│   └── Resources/
│       ├── Learning resources.md
│       ├── Tool recommendations.md
│       └── Reading list 2026.md
├── Index.md                       # Landing page
├── Dashboard.md                   # Quick links, stats
└── .obsidian/
    ├── app.json
    ├── appearance.json
    ├── hotkeys.json
    └── plugins/
        ├── obsidian-daily-notes-plugin/
        └── obsidian-dataview/
```

### Bash Setup Script

```bash
#!/bin/bash
# Personal PKM Vault Setup

VAULT_PATH="${1:-.}/my-vault"

# Create root directory
mkdir -p "$VAULT_PATH"

# Create main folders
mkdir -p "$VAULT_PATH/Inbox"
mkdir -p "$VAULT_PATH/Daily Notes"
mkdir -p "$VAULT_PATH/Notes"/{01\ -\ Writing,02\ -\ Productivity,03\ -\ Health,04\ -\ Technology}
mkdir -p "$VAULT_PATH/References"/{Articles,Books,People,Templates,Resources}

# Create .obsidian configuration
mkdir -p "$VAULT_PATH/.obsidian/plugins"
mkdir -p "$VAULT_PATH/.obsidian/snippets"
mkdir -p "$VAULT_PATH/.obsidian/themes"

# Create core configuration files
cat > "$VAULT_PATH/.obsidian/app.json" << 'EOF'
{
  "dailyNotesFormat": "YYYY-MM-DD",
  "newFileLocation": "folder",
  "newFileFolderPath": "Inbox",
  "autoSaveInterval": 10,
  "promptDelete": false,
  "trashOption": "system"
}
EOF

cat > "$VAULT_PATH/.obsidian/appearance.json" << 'EOF'
{
  "accentColor": "",
  "baseFontSize": 16,
  "theme": "obsidian",
  "cssTheme": ""
}
EOF

cat > "$VAULT_PATH/.obsidian/core-plugins.json" << 'EOF'
{
  "file-explorer": true,
  "global-search": true,
  "switcher": true,
  "graph": true,
  "backlink": true,
  "tag-pane": true,
  "outline": true,
  "word-count": true,
  "pages": false,
  "daily-notes": true,
  "templates": true,
  "publish": false,
  "sync": false
}
EOF

# Create landing pages
cat > "$VAULT_PATH/Index.md" << 'EOF'
# My Knowledge Vault

Quick navigation:
- [[Daily Notes/2026-04-03|Today's Notes]]
- [[Inbox|Inbox]]
- [[Dashboard|Dashboard]]

## Recent Notes
- Notes go here

## By Category
- [[Notes/01 - Writing|Writing]]
- [[Notes/02 - Productivity|Productivity]]
- [[Notes/03 - Health|Health]]
- [[Notes/04 - Technology|Technology]]

## Resources
- [[References|References]]
- [[References/Templates|Templates]]
EOF

cat > "$VAULT_PATH/Dashboard.md" << 'EOF'
# Dashboard

## Quick Access
- [[Inbox|Inbox]] - Process later
- [[Daily Notes|Daily Notes]] - Today's log
- [[Index|Index]] - Main navigation

## Statistics
- Total notes: `=this.file.folder.file.length`

## Today
- Date: 2026-04-03
- Task: Review and process inbox
EOF

echo "✓ Personal PKM vault created at: $VAULT_PATH"
echo "✓ Next: Open $VAULT_PATH in Obsidian"
```

---

## Archetype 2: Zettelkasten (Slip-Box Method)

**For whom**: Researchers, writers, and deep learners who use the Zettelkasten method to build a networked knowledge base. Emphasis on granular, atomic notes with explicit linking to create emergent understanding.

**Core principles**:
- **Fleeting Notes**: Quick daily captures (inbox)
- **Literature Notes**: Processed summaries from sources (key ideas + page numbers)
- **Permanent Notes**: Atomic, self-contained ideas (can stand alone)
- **Index Notes**: Topic entry points with key reference links
- **Structure Notes**: Higher-level synthesis of related permanent notes

**Naming convention**: Use timestamp prefixes (e.g., `202604031430 - Note title.md`) for permanent notes to preserve creation order and enable unique identification.

### Tree Diagram

```
vault-root/
├── 0 - Fleeting Notes/
│   ├── 2026-04-03.md              # Daily fleeting notes
│   ├── 2026-04-02.md
│   └── Quick capture ideas.md
├── 1 - Literature Notes/
│   ├── Thinking Fast and Slow - Kahneman.md
│   ├── Deep Work - Newport.md
│   ├── Atomic Habits - Clear.md
│   ├── Finite and Infinite Games - Carse.md
│   └── The Pragmatic Programmer.md
├── 2 - Permanent Notes/
│   ├── 202604030945 - Deep work requires elimination of distraction.md
│   ├── 202604020830 - Flow state characteristics.md
│   ├── 202604020815 - Context switching has cognitive cost.md
│   ├── 202603290900 - Habits form through consistent repetition.md
│   ├── 202603280730 - Decision fatigue reduces willpower.md
│   ├── 202603270650 - System 1 thinking is fast and intuitive.md
│   └── 202603260900 - Atomic notes are more reusable than long essays.md
├── 3 - Index Notes/
│   ├── Productivity Index.md       # Links to all productivity permanent notes
│   ├── Learning Index.md
│   ├── Decision Making Index.md
│   ├── Behavior Change Index.md
│   └── Work & Flow Index.md
├── 4 - Structure Notes/
│   ├── How to maintain deep work - synthesis.md
│   ├── Habit formation process - synthesis.md
│   ├── Decision making under uncertainty - synthesis.md
│   └── Cognitive biases - synthesis.md
├── 5 - Source Library/
│   ├── Books/
│   │   ├── Thinking Fast and Slow.md
│   │   └── Deep Work.md
│   ├── Articles/
│   │   ├── The Science of Sleep.md
│   │   └── AI and Cognition.md
│   └── People/
│       ├── Cal Newport.md
│       └── James Clear.md
├── 6 - References/
│   ├── Templates/
│   │   ├── Literature note template.md
│   │   ├── Permanent note template.md
│   │   └── Index note template.md
│   ├── Zettelkasten guide.md
│   └── Linking guide.md
├── README.md                      # Zettelkasten overview
└── .obsidian/
    ├── app.json
    ├── appearance.json
    ├── hotkeys.json
    └── plugins/
        ├── obsidian-dataview/
        ├── obsidian-graph/
        └── obsidian-backlinks/
```

### Bash Setup Script

```bash
#!/bin/bash
# Zettelkasten (Slip-Box) Vault Setup

VAULT_PATH="${1:-.}/zettelkasten-vault"

# Create root directory
mkdir -p "$VAULT_PATH"

# Create numbered folder structure (Luhmann's method)
mkdir -p "$VAULT_PATH/0 - Fleeting Notes"
mkdir -p "$VAULT_PATH/1 - Literature Notes"
mkdir -p "$VAULT_PATH/2 - Permanent Notes"
mkdir -p "$VAULT_PATH/3 - Index Notes"
mkdir -p "$VAULT_PATH/4 - Structure Notes"
mkdir -p "$VAULT_PATH/5 - Source Library"/{Books,Articles,People}
mkdir -p "$VAULT_PATH/6 - References"/{Templates,Guides}

# Create .obsidian configuration
mkdir -p "$VAULT_PATH/.obsidian/plugins"
mkdir -p "$VAULT_PATH/.obsidian/snippets"
mkdir -p "$VAULT_PATH/.obsidian/themes"

# Configuration files
cat > "$VAULT_PATH/.obsidian/app.json" << 'EOF'
{
  "newFileLocation": "folder",
  "newFileFolderPath": "0 - Fleeting Notes",
  "autoSaveInterval": 10,
  "promptDelete": false,
  "useMarkdownLinks": true,
  "trashOption": "system"
}
EOF

cat > "$VAULT_PATH/.obsidian/appearance.json" << 'EOF'
{
  "baseFontSize": 15,
  "theme": "obsidian"
}
EOF

cat > "$VAULT_PATH/.obsidian/core-plugins.json" << 'EOF'
{
  "file-explorer": true,
  "global-search": true,
  "switcher": true,
  "graph": true,
  "backlink": true,
  "tag-pane": true,
  "outline": true,
  "page-preview": true,
  "word-count": true
}
EOF

# Create templates
mkdir -p "$VAULT_PATH/6 - References/Templates"

cat > "$VAULT_PATH/6 - References/Templates/Literature Note Template.md" << 'EOF'
# Literature Note: [Title]

**Author(s)**:
**Date**:
**Source Type**: [Book/Article/Paper]
**URL/Citation**:

## Key Ideas
- Idea 1 (p. XX)
- Idea 2 (p. XX)
- Idea 3 (p. XX)

## Direct Quotes
> "Quote here" (p. XX)

## My Thoughts
- Connection to existing notes
- What this adds to my understanding

## Related Permanent Notes
- [[202604030945 - Related note]]
EOF

cat > "$VAULT_PATH/6 - References/Templates/Permanent Note Template.md" << 'EOF'
# [Timestamp] - Note Title

One clear idea, stated as a complete sentence or assertion.

## Explanation
Elaborate on the core idea. Why is it important? What makes it distinct from related concepts?

## Context
- [[Link to index note]]
- [[Link to related permanent note]]
- [[Link to source material]]

## Implications
How does this idea connect to other areas of knowledge?
EOF

cat > "$VAULT_PATH/6 - References/Templates/Index Note Template.md" << 'EOF'
# [Topic] Index

Overview of this topic area.

## Core Permanent Notes
- [[Permanent note 1]]
- [[Permanent note 2]]
- [[Permanent note 3]]

## Structure Notes
- [[Structure note 1]]

## Source Materials
- [[Literature note 1]]
- [[Literature note 2]]

## Related Indexes
- [[Related index 1]]
EOF

# Create README
cat > "$VAULT_PATH/README.md" << 'EOF'
# Zettelkasten Vault

A networked knowledge base using the Zettelkasten (slip-box) method.

## Folder Structure

**0 - Fleeting Notes**: Quick daily captures (ephemeral)
**1 - Literature Notes**: Summaries of source materials
**2 - Permanent Notes**: Atomic ideas (timestamped)
**3 - Index Notes**: Topic entry points
**4 - Structure Notes**: Synthesis and connections
**5 - Source Library**: Original source materials
**6 - References**: Templates and guides

## Workflow

1. Capture thoughts in Fleeting Notes
2. Read sources → create Literature Notes
3. Convert insights into Permanent Notes (use timestamp)
4. Link Permanent Notes together
5. Create Index Notes as topic entry points
6. Write Structure Notes to synthesize clusters

## Naming Convention

Permanent notes: `YYYYMMDDHHMM - Note Title.md`
Example: `202604031430 - Deep work requires elimination of distractions.md`

## Key Principles

- **Atomicity**: One idea per note
- **Autonomy**: Each note should be understandable in isolation
- **Connectivity**: Explicit links between related notes
- **Emergence**: Network structure reveals unexpected connections

## Getting Started

- Review the templates in `6 - References/Templates/`
- Start with fleeting notes in `0 - Fleeting Notes/`
- Create your first literature note from a source
- Extract key ideas into permanent notes
EOF

echo "✓ Zettelkasten vault created at: $VAULT_PATH"
echo "✓ Next: Read README.md and start with fleeting notes"
```

---

## Archetype 3: Second Brain (PARA Method)

**For whom**: Project-oriented teams and individuals using Tiago Forte's PARA method (Projects, Areas, Resources, Archives). Emphasis on actionable organization where everything maps to projects or ongoing responsibilities.

**Core principles**:
- **Projects**: Time-bound goals with deadlines
- **Areas**: Ongoing responsibilities without deadlines
- **Resources**: Reference materials and collections
- **Archives**: Completed projects and inactive areas

### Tree Diagram

```
vault-root/
├── 1 - Projects/
│   ├── Launch email course (Mar-Apr 2026)/
│   │   ├── Project brief.md
│   │   ├── Outline.md
│   │   ├── Lesson 1 - Draft.md
│   │   ├── Lesson 2 - Draft.md
│   │   ├── Timeline.md
│   │   └── Resources/
│   │       ├── Email templates.md
│   │       └── Design assets.md
│   ├── Redesign website (Feb-May 2026)/
│   │   ├── Brief.md
│   │   ├── Design system.md
│   │   ├── Homepage mockup.md
│   │   ├── Sitemap.md
│   │   └── Handoff notes.md
│   ├── Q2 business planning (Apr-Jun 2026)/
│   │   ├── Goals.md
│   │   ├── Market analysis.md
│   │   ├── Budget.md
│   │   └── Team assignments.md
│   └── [Active project]/
├── 2 - Areas/
│   ├── Product Management/
│   │   ├── Area overview.md
│   │   ├── Feature priorities.md
│   │   ├── Roadmap.md
│   │   ├── User research.md
│   │   └── Metrics dashboard.md
│   ├── Writing/
│   │   ├── Area overview.md
│   │   ├── Blog ideas.md
│   │   ├── Published articles/
│   │   │   ├── Article 1.md
│   │   │   └── Article 2.md
│   │   ├── Drafts/
│   │   │   ├── Draft 1.md
│   │   │   └── Draft 2.md
│   │   └── Writing guidelines.md
│   ├── Health/
│   │   ├── Area overview.md
│   │   ├── Fitness log.md
│   │   ├── Sleep tracking.md
│   │   ├── Nutrition guidelines.md
│   │   └── Doctor appointments.md
│   ├── Finance/
│   │   ├── Area overview.md
│   │   ├── Budget 2026.md
│   │   ├── Investments.md
│   │   └── Tax notes.md
│   └── [Ongoing area]/
├── 3 - Resources/
│   ├── Frameworks/
│   │   ├── PARA method.md
│   │   ├── OKRs.md
│   │   ├── SWOT analysis.md
│   │   └── Design thinking.md
│   ├── Tools & Software/
│   │   ├── Obsidian plugins.md
│   │   ├── Notion database templates.md
│   │   └── Productivity tools.md
│   ├── Articles & Bookmarks/
│   │   ├── Deep work.md
│   │   ├── Team dynamics.md
│   │   └── Product strategy.md
│   ├── Templates/
│   │   ├── Project brief template.md
│   │   ├── Meeting notes template.md
│   │   ├── Weekly review template.md
│   │   └── Decision log template.md
│   ├── People & Contacts/
│   │   ├── Team members.md
│   │   ├── Advisors.md
│   │   └── Key collaborators.md
│   └── Media/
│       ├── Screenshots/
│       └── Reference images/
├── 4 - Archives/
│   ├── Projects/
│   │   ├── Completed - 2025 Q4 Campaign/
│   │   ├── Completed - Website v2/
│   │   └── On hold - Mobile app/
│   ├── Areas/
│   │   ├── Archived - Customer support/
│   │   └── Archived - Event planning/
│   └── [Historical content]/
├── Dashboard.md                   # Quick access to active projects/areas
├── Weekly Review.md               # Template and latest review
├── Index.md                       # Top-level navigation
└── .obsidian/
    ├── app.json
    ├── appearance.json
    ├── hotkeys.json
    └── plugins/
        ├── obsidian-dataview/
        ├── obsidian-kanban/
        ├── obsidian-tasks-plugin/
        └── calendar/
```

### Bash Setup Script

```bash
#!/bin/bash
# PARA Method Vault Setup

VAULT_PATH="${1:-.}/para-vault"

# Create root directory
mkdir -p "$VAULT_PATH"

# Create PARA structure
mkdir -p "$VAULT_PATH/1 - Projects"
mkdir -p "$VAULT_PATH/2 - Areas"/{Product\ Management,Writing,Health,Finance}
mkdir -p "$VAULT_PATH/3 - Resources"/{Frameworks,Tools\ \&\ Software,Articles\ \&\ Bookmarks,Templates,People\ \&\ Contacts,Media}
mkdir -p "$VAULT_PATH/4 - Archives"/{Projects,Areas}

# Create .obsidian configuration
mkdir -p "$VAULT_PATH/.obsidian/plugins"
mkdir -p "$VAULT_PATH/.obsidian/snippets"
mkdir -p "$VAULT_PATH/.obsidian/themes"

cat > "$VAULT_PATH/.obsidian/app.json" << 'EOF'
{
  "newFileLocation": "folder",
  "newFileFolderPath": "1 - Projects",
  "autoSaveInterval": 10,
  "promptDelete": false,
  "trashOption": "system"
}
EOF

cat > "$VAULT_PATH/.obsidian/appearance.json" << 'EOF'
{
  "baseFontSize": 16,
  "theme": "obsidian"
}
EOF

cat > "$VAULT_PATH/.obsidian/core-plugins.json" << 'EOF'
{
  "file-explorer": true,
  "global-search": true,
  "switcher": true,
  "backlink": true,
  "tag-pane": true,
  "outline": true,
  "word-count": true
}
EOF

# Create core templates
cat > "$VAULT_PATH/3 - Resources/Templates/Project Brief Template.md" << 'EOF'
# Project: [Name]

**Status**: 🟡 Active
**Timeline**: [Start date] - [End date]
**Owner**:
**Goal**: One-sentence objective

## Outcome
What does done look like?

## Scope
What's included / excluded?

## Key Tasks
- [ ] Task 1
- [ ] Task 2
- [ ] Task 3

## Dependencies
- Resource 1
- Person/team 1

## Progress
- [ ] Phase 1
- [ ] Phase 2
- [ ] Phase 3

## Notes
Project updates and decisions
EOF

cat > "$VAULT_PATH/3 - Resources/Templates/Area Overview Template.md" << 'EOF'
# Area: [Name]

**Status**: Active
**Responsibility**: Who owns this ongoing area?
**Purpose**: Why does this matter?

## Key Objectives
- Objective 1
- Objective 2

## Current Priorities
- [ ] Priority 1
- [ ] Priority 2

## Related Notes
- [[Project or resource 1]]
- [[Project or resource 2]]

## Metrics
What indicates success in this area?

## Review Schedule
Last reviewed:
Next review:
EOF

cat > "$VAULT_PATH/3 - Resources/Templates/Weekly Review Template.md" << 'EOF'
# Weekly Review - [Week of Mon, Apr 03]

## Wins This Week
- Win 1
- Win 2

## Incomplete Items
- [ ] Item 1
- [ ] Item 2

## Next Week Priorities
- [ ] Priority 1
- [ ] Priority 2
- [ ] Priority 3

## Reflection
What worked? What didn't?

## Projects Status
- [[Project 1]]
- [[Project 2]]

## Areas Check-in
- [[Area 1]]
- [[Area 2]]
EOF

# Create dashboard
cat > "$VAULT_PATH/Dashboard.md" << 'EOF'
# Dashboard

## Active Projects
- [[1 - Projects/Project 1|Project 1]]
- [[1 - Projects/Project 2|Project 2]]

## Key Areas
- [[2 - Areas/Product Management|Product Management]]
- [[2 - Areas/Writing|Writing]]
- [[2 - Areas/Health|Health]]

## This Week
- [[Weekly Review|Weekly Review]]

## Quick Resources
- [[3 - Resources/Templates|Templates]]
- [[3 - Resources/Frameworks|Frameworks]]
EOF

# Create index
cat > "$VAULT_PATH/Index.md" << 'EOF'
# Second Brain (PARA Method)

## Navigation
- [[Dashboard|Dashboard]] - Quick access to active work
- [[1 - Projects|Projects]] - Time-bound goals
- [[2 - Areas|Areas]] - Ongoing responsibilities
- [[3 - Resources|Resources]] - Reference materials
- [[4 - Archives|Archives]] - Completed work

## Getting Started
1. Review templates in `3 - Resources/Templates/`
2. Create your first project
3. Define your key areas of responsibility
4. Run weekly reviews
5. Archive completed work
EOF

echo "✓ PARA vault created at: $VAULT_PATH"
echo "✓ Next: Create your first project and define your areas"
```

---

## Archetype 4: Work / Team Vault

**For whom**: Teams, departments, and organizations organizing information by function. Emphasis on shared context, meeting notes, projects, and knowledge relevant to the team.

**Core principles**:
- **Organized by department/function**: Sales, Engineering, Marketing, etc.
- **Shared context**: Meeting notes, decisions, docs
- **People directory**: Team members and external contacts
- **Projects & initiatives**: Departmental or cross-functional projects
- **Knowledge base**: Procedures, guidelines, FAQ

### Tree Diagram

```
vault-root/
├── 00 - Hub/
│   ├── Dashboard.md               # Team quick links
│   ├── Team directory.md
│   ├── Calendar & events.md
│   ├── OKRs & goals.md
│   ├── Decision log.md
│   └── Knowledge base index.md
├── 10 - Sales/
│   ├── Overview.md
│   ├── Q2 goals.md
│   ├── Pipeline.md
│   ├── Accounts/
│   │   ├── Account 1 - Company A.md
│   │   ├── Account 2 - Company B.md
│   │   └── Prospect tracker.md
│   ├── Processes/
│   │   ├── Sales process.md
│   │   ├── Proposal template.md
│   │   ├── Deal stages.md
│   │   └── CRM sync guide.md
│   ├── Meetings/
│   │   ├── 2026-04-02 Weekly standup.md
│   │   ├── 2026-03-29 Customer discovery.md
│   │   └── Meeting template.md
│   └── Resources/
│       ├── Product positioning.md
│       ├── Competitive analysis.md
│       └── Sales deck.md
├── 20 - Engineering/
│   ├── Overview.md
│   ├── Technical roadmap.md
│   ├── Architecture/
│   │   ├── System overview.md
│   │   ├── API documentation.md
│   │   └── Database schema.md
│   ├── Processes/
│   │   ├── Code review guidelines.md
│   │   ├── Deployment procedure.md
│   │   ├── On-call runbook.md
│   │   └── Development setup.md
│   ├── Meetings/
│   │   ├── 2026-04-03 Sprint planning.md
│   │   ├── 2026-03-31 Retrospective.md
│   │   └── Architecture review - 2026-03-27.md
│   └── Projects/
│       ├── Performance optimization.md
│       ├── Database migration.md
│       └── Infrastructure upgrade.md
├── 30 - Marketing/
│   ├── Overview.md
│   ├── Q2 campaigns.md
│   ├── Content calendar.md
│   ├── Campaigns/
│   │   ├── Spring launch campaign.md
│   │   ├── Email sequence - Q2.md
│   │   └── Social media strategy.md
│   ├── Processes/
│   │   ├── Content approval workflow.md
│   │   ├── Brand guidelines.md
│   │   └── Asset templates.md
│   ├── Meetings/
│   │   ├── 2026-04-03 Campaign brainstorm.md
│   │   └── 2026-03-30 Planning.md
│   └── Performance/
│       ├── Website analytics.md
│       ├── Ad performance.md
│       └── Content performance.md
├── 40 - People Operations/
│   ├── Overview.md
│   ├── Team members/
│   │   ├── Alice - Engineering.md
│   │   ├── Bob - Sales.md
│   │   └── Carol - Marketing.md
│   ├── Hiring/
│   │   ├── Open roles.md
│   │   └── Interview guide.md
│   ├── Onboarding/
│   │   ├── Onboarding checklist.md
│   │   └── New hire checklist.md
│   └── Policies/
│       ├── Time off policy.md
│       ├── Remote work policy.md
│       └── Code of conduct.md
├── 50 - Company/
│   ├── Strategic plan.md
│   ├── Annual goals.md
│   ├── Board meetings/
│   │   ├── 2026-Q2 Planning.md
│   │   └── 2026-Q1 Review.md
│   ├── Financial/
│   │   ├── Budget 2026.md
│   │   └── Quarterly metrics.md
│   └── Company handbook.md
└── .obsidian/
    ├── app.json
    ├── appearance.json
    ├── hotkeys.json
    └── plugins/
        ├── obsidian-dataview/
        ├── obsidian-daily-notes/
        ├── obsidian-tasks/
        └── calendar/
```

### Bash Setup Script

```bash
#!/bin/bash
# Work/Team Vault Setup

VAULT_PATH="${1:-.}/team-vault"

# Create root directory
mkdir -p "$VAULT_PATH"

# Create department structure with numbering for sorting
mkdir -p "$VAULT_PATH/00 - Hub"
mkdir -p "$VAULT_PATH/10 - Sales"/{Accounts,Processes,Meetings,Resources}
mkdir -p "$VAULT_PATH/20 - Engineering"/{Architecture,Processes,Meetings,Projects}
mkdir -p "$VAULT_PATH/30 - Marketing"/{Campaigns,Processes,Meetings,Performance}
mkdir -p "$VAULT_PATH/40 - People Operations"/{Team\ Members,Hiring,Onboarding,Policies}
mkdir -p "$VAULT_PATH/50 - Company"/{Board\ Meetings,Financial}

# Create .obsidian configuration
mkdir -p "$VAULT_PATH/.obsidian/plugins"
mkdir -p "$VAULT_PATH/.obsidian/snippets"
mkdir -p "$VAULT_PATH/.obsidian/themes"

cat > "$VAULT_PATH/.obsidian/app.json" << 'EOF'
{
  "newFileLocation": "folder",
  "newFileFolderPath": "00 - Hub",
  "autoSaveInterval": 10,
  "promptDelete": false,
  "trashOption": "system"
}
EOF

cat > "$VAULT_PATH/.obsidian/appearance.json" << 'EOF'
{
  "baseFontSize": 15,
  "theme": "obsidian"
}
EOF

cat > "$VAULT_PATH/.obsidian/core-plugins.json" << 'EOF'
{
  "file-explorer": true,
  "global-search": true,
  "switcher": true,
  "backlink": true,
  "tag-pane": true,
  "outline": true,
  "word-count": true,
  "daily-notes": true
}
EOF

# Create meeting notes template
cat > "$VAULT_PATH/00 - Hub/Meeting Notes Template.md" << 'EOF'
# Meeting: [Title]

**Date**: 2026-04-03
**Attendees**: Name 1, Name 2, Name 3
**Duration**:
**Organizer**:

## Agenda
- [ ] Topic 1
- [ ] Topic 2
- [ ] Topic 3

## Discussion Notes
### Topic 1
- Note 1
- Note 2

### Topic 2
- Note 1
- Note 2

## Decisions
- Decision 1: ...
- Decision 2: ...

## Action Items
- [ ] Item 1 (owner: Name, due: Date)
- [ ] Item 2 (owner: Name, due: Date)

## Next Steps
- Follow-up meeting: Date/Time
- Document to update: Link
EOF

# Create department overview template
cat > "$VAULT_PATH/00 - Hub/Department Overview Template.md" << 'EOF'
# [Department] Overview

## Mission
One-sentence purpose of this department.

## OKRs (Q2 2026)
- Objective 1 - Key Result 1
- Objective 2 - Key Result 1

## Key Projects
- [[Project 1]]
- [[Project 2]]

## Team Members
- [Name] - Role
- [Name] - Role

## Key Processes
- [[Process 1]]
- [[Process 2]]

## Meeting Schedule
- [Day] [Time] - [Meeting name]
- [Day] [Time] - [Meeting name]

## Knowledge Base
- [[Resource 1]]
- [[Resource 2]]
EOF

# Create dashboard
cat > "$VAULT_PATH/00 - Hub/Dashboard.md" << 'EOF'
# Team Dashboard

## Departments
- [[10 - Sales|Sales]]
- [[20 - Engineering|Engineering]]
- [[30 - Marketing|Marketing]]
- [[40 - People Operations|People Ops]]
- [[50 - Company|Company]]

## This Week
- [[00 - Hub/Decision log|Decisions]]
- [[00 - Hub/Calendar & events|Events]]

## Quick Links
- [[Team directory|Team directory]]
- [[OKRs & goals|OKRs & goals]]
- [[Knowledge base index|Knowledge base]]

## Team Directory
- Alice - Engineering
- Bob - Sales
- Carol - Marketing
EOF

# Create team directory
cat > "$VAULT_PATH/00 - Hub/Team Directory.md" << 'EOF'
# Team Directory

## Leadership
- [CEO Name] - CEO, email@company.com

## Sales
- [Name] - VP Sales
- [Name] - Account Executive

## Engineering
- [Name] - VP Engineering
- [Name] - Backend Lead
- [Name] - Frontend Lead

## Marketing
- [Name] - Marketing Director

## People Ops
- [Name] - People Operations Manager

## Contact Info
Use this section for shared contacts.
EOF

# Create index
cat > "$VAULT_PATH/Index.md" << 'EOF'
# Team Vault

## Quick Access
- [[Dashboard|Dashboard]] - Team overview
- [[Team directory|Team directory]] - People and contacts
- [[Decision log|Decision log]] - Key decisions

## By Department
- [[10 - Sales|Sales]]
- [[20 - Engineering|Engineering]]
- [[30 - Marketing|Marketing]]
- [[40 - People Operations|People Operations]]
- [[50 - Company|Company]]

## Getting Started
1. Create a team member profile
2. Document your department overview
3. Create a meeting notes template
4. Start logging decisions in the decision log
EOF

echo "✓ Team vault created at: $VAULT_PATH"
echo "✓ Next: Fill in team members and create department overviews"
```

---

## Archetype 5: Content Creation Vault

**For whom**: Writers, content creators, YouTubers, podcasters, and journalists. Emphasis on idea management, drafting, publishing workflow, and performance tracking.

**Core principles**:
- **Ideas & Inspiration**: Brainstorm and collect raw ideas
- **Research**: Source materials, references, fact-checking
- **Drafts**: Work-in-progress content
- **Published**: Live content with links
- **Analytics**: Performance data for published content
- **Media Assets**: Images, video clips, audio files

### Tree Diagram

```
vault-root/
├── 1 - Ideas & Inspiration/
│   ├── Brainstorm - Blog topics 2026.md
│   ├── Brainstorm - YouTube videos.md
│   ├── Inspiration clips/
│   │   ├── Interview snippet.md
│   │   └── Headline ideas.md
│   ├── Ideas backlog/
│   │   ├── Productivity tips listicle.md
│   │   ├── Interview series.md
│   │   └── Case study ideas.md
│   └── Content calendar.md
├── 2 - Research/
│   ├── Articles & sources/
│   │   ├── Study - Sleep science 2024.md
│   │   ├── Article - Deep work.md
│   │   └── Interview notes - Expert.md
│   ├── Fact-checking/
│   │   ├── Statistics to verify.md
│   │   └── Claims verified.md
│   ├── References/
│   │   ├── People to quote.md
│   │   └── Case studies.md
│   └── Topic research - Productivity.md
├── 3 - Drafts/
│   ├── Blog/
│   │   ├── 0% - How to build habit.md
│   │   ├── 30% - The real cost of context switching.md
│   │   ├── 60% - Time management systems.md
│   │   └── 90% - Deep work in 2026.md
│   ├── Newsletters/
│   │   ├── April 2026 Newsletter.md
│   │   └── May 2026 Newsletter.md
│   ├── YouTube/
│   │   ├── Script - My morning routine.md
│   │   ├── Outline - Productivity tools.md
│   │   └── Talking points - Interview.md
│   └── Social Media/
│       ├── Thread ideas.md
│       └── Caption bank.md
├── 4 - Published/
│   ├── Blog/
│   │   ├── 2025-12-15 - Why deep work matters.md
│   │   ├── 2025-11-20 - Habit tracking tips.md
│   │   └── 2025-10-05 - Remote work setup.md
│   ├── Newsletter/
│   │   ├── 2026-04-01 - Edition 12.md
│   │   ├── 2026-03-18 - Edition 11.md
│   │   └── 2026-03-04 - Edition 10.md
│   ├── YouTube/
│   │   ├── 2025-12-10 - My 5-step morning routine.md
│   │   ├── 2025-11-15 - Tools I use daily.md
│   │   └── 2025-10-20 - Productivity myths busted.md
│   └── Social Media/
│       ├── Twitter/
│       └── LinkedIn/
├── 5 - Analytics & Performance/
│   ├── Blog performance.md
│   ├── Newsletter metrics.md
│   ├── YouTube analytics.md
│   ├── Social media metrics.md
│   └── Publishing checklist.md
├── 6 - Media Assets/
│   ├── Images/
│   │   ├── Blog headers/
│   │   ├── Social thumbnails/
│   │   └── Featured images/
│   ├── Video/
│   │   ├── B-roll clips/
│   │   ├── Transitions/
│   │   └── Intros/
│   ├── Audio/
│   │   ├── Background music/
│   │   ├── Sound effects/
│   │   └── Intro music/
│   └── Design templates/
│       ├── Blog header template.png
│       ├── YouTube thumbnail template.png
│       └── Social card template.png
├── 7 - Resources/
│   ├── Style guide.md
│   ├── Templates/
│   │   ├── Blog post template.md
│   │   ├── Newsletter template.md
│   │   ├── YouTube script template.md
│   │   └── Social post template.md
│   ├── Tools & platforms.md
│   ├── Publishing platforms.md
│   └── Distribution checklist.md
├── Dashboard.md                   # Current projects, metrics at a glance
├── Content Calendar.md
└── .obsidian/
    ├── app.json
    ├── appearance.json
    ├── hotkeys.json
    └── plugins/
        ├── obsidian-dataview/
        ├── obsidian-kanban/
        ├── obsidian-calendar/
        └── obsidian-word-statistics/
```

### Bash Setup Script

```bash
#!/bin/bash
# Content Creation Vault Setup

VAULT_PATH="${1:-.}/content-vault"

# Create root directory
mkdir -p "$VAULT_PATH"

# Create content-focused structure
mkdir -p "$VAULT_PATH/1 - Ideas & Inspiration"/{Brainstorm,Inspiration\ clips,Ideas\ backlog}
mkdir -p "$VAULT_PATH/2 - Research"/{Articles\ \&\ sources,Fact-checking,References}
mkdir -p "$VAULT_PATH/3 - Drafts"/{Blog,Newsletters,YouTube,Social\ Media}
mkdir -p "$VAULT_PATH/4 - Published"/{Blog,Newsletter,YouTube,Social\ Media/{Twitter,LinkedIn}}
mkdir -p "$VAULT_PATH/5 - Analytics & Performance"
mkdir -p "$VAULT_PATH/6 - Media Assets"/{Images/{Blog\ headers,Social\ thumbnails,Featured\ images},Video/{B-roll,Transitions,Intros},Audio/{Background\ music,Sound\ effects,Intro\ music},Design\ templates}
mkdir -p "$VAULT_PATH/7 - Resources"/{Templates}

# Create .obsidian configuration
mkdir -p "$VAULT_PATH/.obsidian/plugins"
mkdir -p "$VAULT_PATH/.obsidian/snippets"
mkdir -p "$VAULT_PATH/.obsidian/themes"

cat > "$VAULT_PATH/.obsidian/app.json" << 'EOF'
{
  "newFileLocation": "folder",
  "newFileFolderPath": "1 - Ideas & Inspiration",
  "autoSaveInterval": 10,
  "promptDelete": false,
  "trashOption": "system"
}
EOF

cat > "$VAULT_PATH/.obsidian/appearance.json" << 'EOF'
{
  "baseFontSize": 16,
  "theme": "obsidian"
}
EOF

cat > "$VAULT_PATH/.obsidian/core-plugins.json" << 'EOF'
{
  "file-explorer": true,
  "global-search": true,
  "switcher": true,
  "backlink": true,
  "tag-pane": true,
  "outline": true,
  "word-count": true
}
EOF

# Create templates

cat > "$VAULT_PATH/7 - Resources/Templates/Blog Post Template.md" << 'EOF'
# [Article Title]

**Status**: 0% Draft
**Target Publish Date**:
**Content Type**: Blog post
**Target Audience**:
**Keywords**:

## Outline
- Introduction
  - Hook
  - Problem statement
  - Promise
- Section 1
  - Key point
  - Supporting detail
- Section 2
  - Key point
  - Supporting detail
- Conclusion
  - Summary
  - Call to action

## First Draft
[Write your draft here]

## Research & References
- [[Research note 1]]
- Source: [URL]

## Meta
- SEO Title:
- Meta Description:
- Featured Image:
- Categories/Tags:
EOF

cat > "$VAULT_PATH/7 - Resources/Templates/Newsletter Template.md" << 'EOF'
# Newsletter - [Month] [Year]

**Issue**: #
**Send Date**:
**Target Audience**: Subscribers
**Goal**:

## Header
Welcome message or theme for this edition

## Section 1 - Main Article
- Title:
- Summary:
- Link:

## Section 2 - Interesting Find
- What I'm reading:
- Key takeaway:

## Section 3 - Highlight Reel
- Recent blog:
- Video:
- Social post:

## Call to Action
What do you want readers to do?

## Footer
Unsubscribe link, social links, contact info
EOF

cat > "$VAULT_PATH/7 - Resources/Templates/YouTube Script Template.md" << 'EOF'
# Video: [Title]

**Video ID**:
**Status**: Script Draft
**Target Length**: 10 minutes
**Target Audience**:

## Hook (0-30 seconds)
Grab attention in first 5 seconds.

## Introduction (30 seconds - 1 minute)
- Problem you're solving
- What viewer will learn
- Promise of value

## Main Content (1-7 minutes)
### Point 1 (2-3 minutes)
- Explanation
- Example or demonstration
- Visual cue: [describe what should be shown]

### Point 2 (2-3 minutes)
- Explanation
- Example
- Visual cue:

### Point 3 (1-2 minutes)
- Explanation
- Visual cue:

## Conclusion (7-9 minutes)
- Recap key points
- Call to action (subscribe, like, comment)

## Outro (9-10 minutes)
- Thank you
- Next video tease
- End screen elements

## B-Roll Needed
- [ ] Footage item 1
- [ ] Footage item 2
- [ ] Stock footage needed

## Audio
- Background music: [track name]
- Sound effects: [list]
EOF

cat > "$VAULT_PATH/7 - Resources/Templates/Social Media Template.md" << 'EOF'
# Social Post - [Platform]

**Platform**: Twitter / LinkedIn / Instagram
**Status**: Draft
**Best Time to Post**:
**Goal**: Engagement / Traffic / Awareness

## Headline / Hook
Attention-grabbing first line

## Body Copy
Main message

## CTA
What do you want followers to do?

## Visual
- Image: [describe]
- Video: [describe]
- Link:

## Hashtags
#hashtag1 #hashtag2 #hashtag3

## Metrics Goal
- Target impressions:
- Target engagement rate:
EOF

# Create publishing checklist
cat > "$VAULT_PATH/5 - Analytics & Performance/Publishing Checklist.md" << 'EOF'
# Pre-Publish Checklist

## Content Review
- [ ] Read through for spelling/grammar
- [ ] Fact-check claims
- [ ] Verify all links work
- [ ] Check formatting
- [ ] Review for tone and voice

## SEO (Blog Posts)
- [ ] Add SEO title
- [ ] Write meta description
- [ ] Add alt text to images
- [ ] Include keywords naturally
- [ ] Create slug/URL

## Media
- [ ] Featured image is high quality
- [ ] All images have alt text
- [ ] Video is properly embedded
- [ ] Audio files are working

## Meta
- [ ] Publish date set
- [ ] Categories/tags added
- [ ] Author bio added
- [ ] Call to action visible

## Distribution
- [ ] Schedule social media posts
- [ ] Email subscribers (if applicable)
- [ ] Add to content calendar
- [ ] Share in communities

## Post-Publish
- [ ] Monitor for feedback
- [ ] Respond to comments
- [ ] Update performance tracking
- [ ] Plan follow-up content
EOF

# Create dashboard
cat > "$VAULT_PATH/Dashboard.md" << 'EOF'
# Content Creation Dashboard

## Current Projects
| Title | Status | Target Date | Type |
|-------|--------|-------------|------|
| Project 1 | 30% | 2026-04-15 | Blog |
| Project 2 | 60% | 2026-04-30 | YouTube |

## Upcoming Publishing
- 2026-04-10: Blog post
- 2026-04-15: Newsletter
- 2026-04-20: YouTube video

## Performance This Month
- Blog views: 2,450
- Newsletter opens: 38%
- YouTube watch time: 450 hours

## Next Steps
1. Finish outline for next blog post
2. Record YouTube intro
3. Edit newsletter
EOF

# Create index
cat > "$VAULT_PATH/Index.md" << 'EOF'
# Content Creation Vault

## Quick Access
- [[Dashboard|Dashboard]] - Current projects and metrics
- [[Content Calendar|Content Calendar]] - Publishing schedule
- [[7 - Resources/Templates|Templates]] - Ready-to-use formats

## Content Sections
- [[1 - Ideas & Inspiration|Ideas]] - Brainstorm and inspiration
- [[2 - Research|Research]] - Source materials and fact-checking
- [[3 - Drafts|Drafts]] - Works in progress
- [[4 - Published|Published]] - Live content
- [[5 - Analytics & Performance|Analytics]] - Metrics and performance

## By Content Type
- Blog: Drafts → Published → Analytics
- Newsletter: Ideas → Draft → Published
- YouTube: Ideas → Script → Draft → Published
- Social Media: Ideas → Draft → Published

## Getting Started
1. Check out [[Content Calendar|Content Calendar]]
2. Pick a content type and use the template
3. Research and gather materials
4. Draft your content
5. Publish and track performance
EOF

echo "✓ Content Creation vault created at: $VAULT_PATH"
echo "✓ Next: Review templates and create your first piece"
```

---

## Archetype 6: Research Vault

**For whom**: Academics, researchers, data analysts, and professionals conducting research. Emphasis on rigorous documentation, literature review, methodology, and findings.

**Core principles**:
- **Research questions**: The driving questions
- **Literature review**: Papers, studies, and existing knowledge
- **Methodology**: Approach, design, and procedures
- **Data & experiments**: Raw data, analysis, results
- **Findings**: Conclusions and implications
- **Publications**: Papers, theses, reports

### Tree Diagram

```
vault-root/
├── 0 - Research Overview/
│   ├── Research agenda.md          # High-level research goals
│   ├── Active projects.md          # Current research projects
│   ├── Timeline.md                 # Milestones and deadlines
│   └── Resources & tools.md        # Research tools and platforms
├── 1 - Research Questions/
│   ├── Primary question.md
│   ├── Sub-questions.md
│   ├── Hypotheses.md
│   └── Research scope.md
├── 2 - Literature Review/
│   ├── 2.1 - Core papers/
│   │   ├── Smith 2024 - Deep learning approaches.md
│   │   ├── Chen 2023 - Network analysis.md
│   │   └── Johnson 2022 - Methodology review.md
│   ├── 2.2 - Related studies/
│   │   ├── Category 1 - Background.md
│   │   ├── Category 2 - Precedent work.md
│   │   └── Category 3 - Competing approaches.md
│   ├── 2.3 - Author database/
│   │   ├── Smith, Jane - Scholar profile.md
│   │   ├── Chen, David - Scholar profile.md
│   │   └── Johnson, Alex - Scholar profile.md
│   ├── 2.4 - Concept map/
│   │   └── Knowledge map - Deep learning.md
│   └── Literature review synthesis.md
├── 3 - Methodology/
│   ├── Research design.md           # Overall approach
│   ├── Methodology framework.md     # Specific method details
│   ├── Data collection protocol.md  # How data is collected
│   ├── Analysis procedure.md        # How analysis is performed
│   ├── Quality assurance.md         # Validity and reliability checks
│   ├── Ethical considerations.md    # IRB, consent, etc.
│   └── Timeline & milestones.md     # Phase schedule
├── 4 - Data & Experiments/
│   ├── 4.1 - Raw data/
│   │   ├── Dataset 1 - Description.md
│   │   ├── Dataset 2 - Metadata.md
│   │   ├── Participant pool.md
│   │   └── Data collection log.md
│   ├── 4.2 - Analysis/
│   │   ├── Data cleaning notes.md
│   │   ├── Statistical analysis results.md
│   │   ├── Qualitative coding.md
│   │   ├── Visualization notes.md
│   │   └── Analysis log.md
│   ├── 4.3 - Experiments/
│   │   ├── Experiment 1 - Design.md
│   │   ├── Experiment 1 - Results.md
│   │   ├── Experiment 2 - Design.md
│   │   └── Experiment 2 - Results.md
│   └── 4.4 - Outputs/
│       ├── Figures/
│       ├── Tables/
│       └── Charts/
├── 5 - Findings & Analysis/
│   ├── Key findings.md             # Major discoveries
│   ├── Interpretation.md           # Meaning of findings
│   ├── Unexpected results.md       # Surprises and anomalies
│   ├── Limitations.md              # Constraints of study
│   ├── Implications.md             # Practical applications
│   └── Future directions.md        # Next research steps
├── 6 - Publications/
│   ├── Journal articles/
│   │   ├── 2026 - Paper title (submitted).md
│   │   ├── 2025 - Paper title (published).md
│   │   └── 2024 - Paper title (published).md
│   ├── Conference papers/
│   │   ├── 2026-04 - Conference name - Abstract.md
│   │   └── 2026-06 - Conference name - Abstract.md
│   ├── Thesis/
│   │   ├── Outline.md
│   │   ├── Chapters/
│   │   │   ├── Chapter 1 - Introduction.md
│   │   │   ├── Chapter 2 - Literature.md
│   │   │   ├── Chapter 3 - Methodology.md
│   │   │   └── Chapter 4 - Findings.md
│   │   └── Draft timeline.md
│   └── Reports/
│       ├── Annual report 2025.md
│       └── Preliminary findings report.md
├── 7 - References & Tools/
│   ├── Citation format guide.md
│   ├── Research databases.md       # PubMed, JSTOR, etc.
│   ├── Statistical tools.md        # R, Python, SPSS, etc.
│   ├── Templates/
│   │   ├── Literature note template.md
│   │   ├── Experiment log template.md
│   │   └── Analysis report template.md
│   └── Resources/
│       ├── Research ethics guide.md
│       ├── Data management plan.md
│       └── Grant writing tips.md
├── Index.md
└── .obsidian/
    ├── app.json
    ├── appearance.json
    ├── hotkeys.json
    └── plugins/
        ├── obsidian-dataview/
        ├── obsidian-citation/
        ├── obsidian-zotero/
        └── obsidian-excalidraw/
```

### Bash Setup Script

```bash
#!/bin/bash
# Research Vault Setup

VAULT_PATH="${1:-.}/research-vault"

# Create root directory
mkdir -p "$VAULT_PATH"

# Create research-focused structure
mkdir -p "$VAULT_PATH/0 - Research Overview"
mkdir -p "$VAULT_PATH/1 - Research Questions"
mkdir -p "$VAULT_PATH/2 - Literature Review"/{2.1\ -\ Core\ papers,2.2\ -\ Related\ studies,2.3\ -\ Author\ database,2.4\ -\ Concept\ map}
mkdir -p "$VAULT_PATH/3 - Methodology"
mkdir -p "$VAULT_PATH/4 - Data & Experiments"/{4.1\ -\ Raw\ data,4.2\ -\ Analysis,4.3\ -\ Experiments,4.4\ -\ Outputs/{Figures,Tables,Charts}}
mkdir -p "$VAULT_PATH/5 - Findings & Analysis"
mkdir -p "$VAULT_PATH/6 - Publications"/{Journal\ articles,Conference\ papers,Thesis/{Chapters},Reports}
mkdir -p "$VAULT_PATH/7 - References & Tools"/{Templates}

# Create .obsidian configuration
mkdir -p "$VAULT_PATH/.obsidian/plugins"
mkdir -p "$VAULT_PATH/.obsidian/snippets"
mkdir -p "$VAULT_PATH/.obsidian/themes"

cat > "$VAULT_PATH/.obsidian/app.json" << 'EOF'
{
  "newFileLocation": "folder",
  "newFileFolderPath": "0 - Research Overview",
  "autoSaveInterval": 10,
  "promptDelete": false,
  "trashOption": "system"
}
EOF

cat > "$VAULT_PATH/.obsidian/appearance.json" << 'EOF'
{
  "baseFontSize": 15,
  "theme": "obsidian"
}
EOF

cat > "$VAULT_PATH/.obsidian/core-plugins.json" << 'EOF'
{
  "file-explorer": true,
  "global-search": true,
  "switcher": true,
  "backlink": true,
  "tag-pane": true,
  "outline": true,
  "word-count": true,
  "graph": true
}
EOF

# Create templates

cat > "$VAULT_PATH/7 - References & Tools/Templates/Literature Note Template.md" << 'EOF'
# [Author] [Year] - [Title]

**Authors**:
**Year**:
**Publication**: [Journal/Conference]
**DOI**:
**URL**:

## Summary
One-paragraph summary of the entire paper.

## Research Question
What question does this paper address?

## Methodology
How did they conduct their research?

## Key Findings
- Finding 1
- Finding 2
- Finding 3

## Relevant Quotes
> "Important quote" (p. XX)
> "Another relevant quote" (p. XX)

## Relation to My Research
How does this connect to my questions and work?

## Strengths
- Strength 1
- Strength 2

## Limitations
- Limitation 1
- Limitation 2

## Future Work / Open Questions
What did they leave unanswered?

## Tags
#topic #method #key-finding
EOF

cat > "$VAULT_PATH/7 - References & Tools/Templates/Experiment Log Template.md" << 'EOF'
# Experiment: [Name]

**Date**: 2026-04-03
**Experiment ID**: EXP-001
**Status**: Planning / In Progress / Complete
**Hypothesis**:

## Objective
What is this experiment designed to test?

## Design
### Participants
- Sample size:
- Recruitment method:
- Inclusion criteria:
- Exclusion criteria:

### Procedure
1. Step 1
2. Step 2
3. Step 3

### Materials
- [ ] Material 1
- [ ] Material 2

### Variables
- **Independent**:
- **Dependent**:
- **Controls**:

## Execution Log
- 2026-04-03: Started pilot test
- 2026-04-04: Completed n=10 participants

## Results
[Summary of findings]

## Analysis
[Statistical or qualitative analysis]

## Conclusions
What do the results tell us about the hypothesis?

## Next Steps
What to do based on these results?
EOF

cat > "$VAULT_PATH/7 - References & Tools/Templates/Analysis Report Template.md" << 'EOF'
# Analysis Report - [Title]

**Date**: 2026-04-03
**Data Source**: [Dataset name]
**Analyst**:

## Objective
What question are we answering with this analysis?

## Methodology
### Data Description
- Sample size:
- Variables:
- Missing data:

### Analysis Methods
- Method 1: [description]
- Method 2: [description]

## Results

### Main Findings
[Present results in narrative form]

### Visualizations
[Describe figures and tables]

### Statistical Summary
[Key statistics]

## Interpretation
What do these results mean?

## Limitations
- Limitation 1
- Limitation 2

## Recommendations
What actions or further analyses are suggested?

## Appendix
- Code/syntax used
- Additional tables
- Supplementary figures
EOF

# Create research overview
cat > "$VAULT_PATH/0 - Research Overview/Research Agenda.md" << 'EOF'
# Research Agenda

## Overall Goal
Long-term research vision and objectives.

## Research Questions
- Primary question: ?
- Sub-question 1: ?
- Sub-question 2: ?

## Scope
What will this research cover?

## Timeline
- Phase 1 (Start-End): Literature review
- Phase 2 (Start-End): Methodology development
- Phase 3 (Start-End): Data collection
- Phase 4 (Start-End): Analysis
- Phase 5 (Start-End): Publication

## Key Deliverables
- [ ] Literature review synthesis
- [ ] Methodology paper
- [ ] Dataset(s)
- [ ] Journal article
- [ ] Conference presentation
- [ ] Thesis

## Success Criteria
How will we know this research was successful?
EOF

cat > "$VAULT_PATH/0 - Research Overview/Active Projects.md" << 'EOF'
# Active Research Projects

| Project | Status | Start | Target End | Lead | Key Contacts |
|---------|--------|-------|-----------|------|--------------|
| Project A | 40% | 2026-01 | 2026-06 | You | Collaborator 1 |
| Project B | 10% | 2026-03 | 2026-09 | You | Collaborator 2 |

## Project A Details
[[Link to full project notes]]

## Project B Details
[[Link to full project notes]]
EOF

# Create index
cat > "$VAULT_PATH/Index.md" << 'EOF'
# Research Vault

## Navigation
- [[0 - Research Overview|Overview]] - Research goals and timeline
- [[1 - Research Questions|Research Questions]] - Core questions and hypotheses
- [[2 - Literature Review|Literature Review]] - Existing knowledge and papers
- [[3 - Methodology|Methodology]] - Research approach and procedures
- [[4 - Data & Experiments|Data & Experiments]] - Datasets and analysis
- [[5 - Findings & Analysis|Findings]] - Results and interpretation
- [[6 - Publications|Publications]] - Papers and reports
- [[7 - References & Tools|Resources]] - References and tools

## Current Status
- [[0 - Research Overview/Active Projects|Active Projects]]
- [[0 - Research Overview/Timeline|Timeline]]

## Getting Started
1. Define your [[1 - Research Questions|research questions]]
2. Conduct [[2 - Literature Review|literature review]]
3. Design your [[3 - Methodology|methodology]]
4. Collect and analyze [[4 - Data & Experiments|data]]
5. Document your [[5 - Findings & Analysis|findings]]
6. Prepare [[6 - Publications|publications]]
EOF

echo "✓ Research vault created at: $VAULT_PATH"
echo "✓ Next: Define your research questions and begin literature review"
```

---

## Summary

This reference covers:

- **Accepted file formats**: Full table of all supported file types
- **Configuration folder (`.obsidian/`)**: Complete directory structure and purpose of each file
- **Core concepts**: Plain-text storage, vault as filesystem folder, symbolic links, indexing
- **Six folder archetypes**:
  1. **Personal PKM**: Simple inbox → notes → references → archives
  2. **Zettelkasten**: Atomic notes with timestamp prefixes and network connections
  3. **PARA Method**: Projects, Areas, Resources, Archives for GTD-style organization
  4. **Work/Team Vault**: Department-organized vault for teams and organizations
  5. **Content Creation**: Idea → Research → Draft → Published → Analytics workflow
  6. **Research**: Literature → Methodology → Data → Findings → Publications structure

Each archetype includes a complete directory tree (2+ levels deep with examples) and a full, runnable bash script for quick setup.

Choose the archetype that matches your workflow or adapt one to your needs.
