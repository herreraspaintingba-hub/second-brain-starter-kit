# Obsidian Linking & Embedding Reference

## Internal Links

### Basic Syntax
```
[[Note Name]]                    Links to a note; displays note name
[[My Project]]                   Links to "My Project" note
[[Daily/2026-04-03]]             Links to daily note (folder path supported)
```

### Link to Heading
```
[[Note Name#Heading]]            Links to specific heading in a note
[[Projects#Current Focus]]       Links to "Current Focus" heading
[[Architecture#Database Layer]]  Links to nested heading
```

**Note:** Heading must exactly match (case-sensitive). Use `#` for H1, `##` for H2, etc. in the link syntax—Obsidian normalizes it.

### Link to Block
```
[[Note Name^block-id]]           Links to specific block (paragraph, list item, etc.)
[[Meeting Notes^action-items]]   Links to block with ID "action-items"
```

### Link with Display Text
```
[[Note Name|Custom Label]]       Shows "Custom Label" but links to "Note Name"
[[2026-04-03|Today]]             Shows "Today" but links to the daily note
[[Projects#Goals|Our Roadmap]]   Shows "Our Roadmap", links to #Goals in Projects
[[Meeting Notes^decisions|Key Decisions]]  Shows "Key Decisions", links to block
```

---

## Block References

### Creating Block IDs

**End-of-line syntax:** Add `^block-id` at the end of any paragraph, list item, or block:

```
This is a paragraph about project scope.
^scope-definition

- Research user needs
- Validate assumptions
- Define success metrics
^research-phase

| Feature | Status |
| - | - |
| Auth | Done |
^feature-table
```

**Rules:**
- Block ID must come after the content (at line end)
- Use lowercase, hyphens, numbers (no spaces)
- One block ID per block
- IDs are invisible in preview; only show in edit mode

### Linking to Blocks

```
[[Product Roadmap^q1-milestones]]              Link to a block
[[Q1 Planning#Strategy^timeline]]              Link to block within a heading section
[[Research^findings|See findings]]             Link to block with custom text
```

**Why use blocks?** Reusable references to specific content without creating new notes. Ideal for decision logs, action items, key quotes, definitions.

### Auto-Generated Block IDs

- Obsidian can auto-generate random IDs (e.g., `^a1b2c3d4`)
- Hover over a block → click three dots → "Copy block link"
- Obsidian creates the ID automatically if not manually set

---

## Aliases

### Inline Aliases (Wikilink Style)

```
[[Real Note Name|Alias]]         Alternative name in the link
[[John Smith|John]]              Link shows as "John", goes to "John Smith" note
[[Q1 2026 Planning|Spring Planning]]  Shows "Spring Planning"
```

**Use case:** Refer to notes by common names, abbreviations, or context-specific terms without renaming the actual file.

### Frontmatter Aliases

Add to note's YAML frontmatter (top of file):

```yaml
---
aliases:
  - Alternative Name
  - Short Form
  - Context Label
---
```

**Example:**
```yaml
---
title: John Smith
aliases:
  - John
  - Sales Lead
  - js-john
---
```

Now `[[John]]`, `[[Sales Lead]]`, and `[[js-john]]` all resolve to the John Smith note.

### How Aliases Appear

- **Quick Switcher** (`Cmd+O` / `Ctrl+O`): Type alias → note appears under original name
- **Link Suggestions**: When typing `[[`, aliases appear as completion options
- **Backlinks pane**: Shows note by original name, but you can link via alias
- **Unlinked mentions**: Detects alias text as a mention

**Best practice:** Use aliases for terminology that changes by context (e.g., "CRM" alias for "HubSpot Notes Database").

---

## Embedding Files

### Embed Entire Note

```
![[Note Name]]                   Embeds full content of "Note Name"
![[Project Brief]]               Shows entire project brief inline
```

**In preview:** Full content displays where the embed code is. Headings, lists, formatting all render.

**In edit mode:** Shows the embed syntax; click to expand preview.

### Embed Specific Heading

```
![[Note Name#Heading]]           Embeds only content under that heading
![[Project Brief#Timeline]]      Embeds only the Timeline section
![[Meeting Notes#Action Items]]  Embeds action items list
```

**Behavior:** Includes the heading and all content under it until the next heading of the same or higher level.

### Embed Block

```
![[Note Name^block-id]]          Embeds single paragraph, list, or block
![[Decisions^approved-budget]]   Embeds block with ID "approved-budget"
![[Research^key-finding]]        Embeds one key finding block
```

**Use case:** Pull in specific facts, definitions, or decisions from other notes without embedding entire sections.

### Embed Image with Width

```
![[image.png]]                   Embeds image (full width)
![[image.png|300]]               Embeds image, max width 300px
![[screenshot.png|50%]]          Embeds image at 50% width
![[diagram.svg|250x400]]         Embeds image, 250px wide, 400px tall
```

**Supported formats:** PNG, JPG, GIF, SVG, WebP.

**In note:** Images scale responsively; width parameter constrains max size.

---

## Embedding Other File Types

### PDF Embeds

```
![[document.pdf]]                Embeds entire PDF (shows all pages)
![[document.pdf#page=3]]         Embeds starting at page 3
![[contract.pdf#page=2&size=200]] Embed page 2, 200px width
```

**Behavior:**
- Entire PDF displays as preview; users can scroll, search, and navigate
- Page parameter selects starting page; renders from there onward
- Size parameter constrains width

### Audio Embeds

```
![[recording.mp3]]               Embeds audio player
![[podcast-episode.m4a]]         Embeds M4A audio file
![[meeting-notes.aac]]           Embeds AAC audio file
```

**In preview:** Interactive audio player with play/pause, progress bar, volume control.

**Supported:** MP3, M4A, AAC, OGG, WAV.

### Video Embeds

```
![[video.mp4]]                   Embeds video player
![[tutorial.webm]]               Embeds WebM video
![[demo.mkv]]                    Embeds MKV video (if browser supports)
```

**In preview:** Interactive video player with play/pause, timeline, fullscreen.

**Supported:** MP4, WebM, MKV, OGG (video), MOV.

**Caveat:** Video embed support depends on browser codecs; MP4 is most reliable.

---

## External Links

### Standard Markdown Links

```
[text](url)                      Standard markdown link syntax
[Obsidian Help](https://help.obsidian.md)
[Google Search](https://google.com)
[Internal + External](https://example.com#section)  Links with anchors
```

**Rendering:** Shows link text in blue/accent color; clickable to open URL.

**Use case:** Links to web pages, external documentation, resources outside your vault.

### Bare URLs Auto-Link

```
https://example.com              Auto-converts to clickable link
http://github.com/username/repo  Also clickable without [text](url) syntax
```

**In preview:** Bare URLs automatically become clickable links without formatting.

**Caveat:** Works best with `https://` or `http://` prefix; unclear URLs may not auto-link.

### Protocol Links (Open Apps)

```
[Open Slack](slack://user?team=XXXXXX&id=UXXXXX)
[Open Bear Note](bear://x-callback-url/open-note?title=MyNote)
[Call](tel:+15551234567)
[Email](mailto:person@example.com)
```

**Use case:** Deep links to specific apps, contacts, or external tools from within notes.

---

## Backlinks & Outgoing Links

### Backlinks Pane

**Right sidebar → Backlinks tab** shows all notes linking to the current note:

```
Current note: "Project X"
Backlinks:
  Quarterly Goals (linked from heading #Q1 Focus)
  Team Roadmap (linked from ^milestones block)
  Board Decisions (2 links)
```

**Click any backlink** → opens that note and jumps to the link context.

**Use case:** See what's connected to this note — dependencies, related projects, cross-references.

### Outgoing Links Pane

**Right sidebar → Outgoing links tab** shows all links FROM the current note TO others:

```
Current note: "Project X"
Outgoing links:
  [[Team Members]]
  [[Timeline#Milestones]]
  [[Budget Tracker^approved-spend]]
```

**Click to navigate** → opens the linked note.

**Use case:** Audit what this note references; navigate the web from the current page.

### Unlinked Mentions

**Right sidebar → Unlinked mentions** shows text in the note that matches other note names (or aliases) but isn't explicitly linked:

```
Current note: "Project X"
Unlinked mentions:
  John Smith (mentioned 2x but not linked)
  Timeline (mentioned 1x but not linked)
  Budget (matches a note, mentioned but not linked)
```

**Action:** Click "Link" next to any mention → automatically creates a wikilink.

**Why it matters:** Discover implicit connections. Enrich your graph by linking what you've already mentioned.

---

## Linking Best Practices

### Wikilinks vs. Standard Markdown Links

**Use wikilinks `[[Note]]` for:**
- Internal notes and concepts
- Building a connected knowledge graph
- Creating backlinks and graph relationships
- Bi-directional navigation
- Cross-references within your vault

```
[[Project Management]]           Go here when you want Obsidian to track the relationship
```

**Use markdown links `[text](url)` for:**
- External websites and URLs
- Web-based documentation
- Links that don't deserve a new note
- External tools and services
- Protocol-based deep links

```
[Obsidian Help](https://help.obsidian.md)  Go here for external web resources
```

### Building a Connected Graph

**Why links matter:**
- **Graph visualization** (`Graph view`): See all notes as nodes, links as edges
- **Serendipity**: Discover unexpected connections between ideas
- **Context**: Every note becomes a hub; backlinks show related thinking
- **Refactoring**: Easy to see what breaks if you rename or delete a note

**Linking strategy:**
1. Link to general concepts, not every mention (avoid over-linking)
2. Use aliases to refer to notes by context-appropriate names
3. Create hub notes (MOCs) that aggregate links in one place
4. Trust backlinks to surface relationships; don't link everything

### Hub Notes / Maps of Content (MOCs)

A hub note is an **index** that lists links to related notes:

```
# Project X - Hub

## Team
- [[John Smith]]
- [[Sarah Johnson]]
- [[Project Manager]]

## Timeline
- [[Q1 Milestones]]
- [[Deliverables#Phase 1]]
- [[Timeline^deadline]]

## Resources
- [[Budget Tracker]]
- [[Knowledge Base]]

## Related
- [[Similar Project Y]]
- [[Lessons Learned]]
```

**Why use MOCs:**
- Single entry point to explore a topic
- Organizes links thematically
- Makes graphs navigable (too many random links = hairball)
- Serves as table of contents for a project or area

**Build MOCs for:**
- Large projects (root hub → sub-hubs)
- Areas of focus (Sales, Engineering, Product)
- Reference topics (Frameworks, Tools, Concepts)
- Time-based structures (Annual → Quarterly → Weekly)

---

## Quick Reference Cheat Sheet

| Syntax | Purpose |
| - | - |
| `[[Note]]` | Link to note |
| `[[Note#Heading]]` | Link to heading |
| `[[Note^id]]` | Link to block |
| `[[Note\|Text]]` | Link with display text |
| `^block-id` | Create block ID (end of line) |
| `[[Real\|Alias]]` | Use alias in wikilink |
| `aliases: [alias1]` | Set alias in frontmatter |
| `![[Note]]` | Embed entire note |
| `![[Note#Heading]]` | Embed section |
| `![[Note^id]]` | Embed block |
| `![[image.png\|300]]` | Embed image, 300px width |
| `![[doc.pdf#page=3]]` | Embed PDF from page 3 |
| `![[audio.mp3]]` | Embed audio player |
| `![[video.mp4]]` | Embed video player |
| `[text](url)` | External link |
| `https://example.com` | Auto-link bare URL |

---

**Last updated:** 2026-04-03
