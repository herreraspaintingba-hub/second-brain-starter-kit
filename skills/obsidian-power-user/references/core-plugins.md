# Obsidian Core Plugins Reference

Complete guide to every Obsidian core plugin: what it does, how to enable/configure it, and key usage tips.

---

## Audio Recorder

**What it does:** Records audio notes directly into your vault as audio files. Useful for capturing voice thoughts, meeting recordings, or verbal notes without typing.

**Enable/Configure:**
- Settings → Core plugins → toggle **Audio Recorder** on
- Configure storage location: Settings → Audio Recorder → Audio folder (defaults to vault root)
- Set audio quality and format (typically MP3 or WebM depending on OS)

**Key tips:**
- File naming: automatically timestamps recordings (e.g., `Recording 2026-04-03 10-30.mp3`)
- Click the microphone icon in the toolbar or use Command Palette (`Ctrl/Cmd+P` → "Audio Recorder: Start recording")
- Save recording to vault to make it linkable and searchable via backlinks
- Embedded audio can be played directly in notes using syntax: `![audio](filename.mp3)`

---

## Backlinks

**What it does:** Shows all notes and mentions that link to the current note. Displays both explicit wikilinks and unlinked mentions. Helps map knowledge connections.

**Enable/Configure:**
- Settings → Core plugins → toggle **Backlinks** on
- Panel appears in the right sidebar by default
- No additional configuration needed

**Key tips:**
- **Backlinks panel** shows two sections: "Linked mentions" (explicit `[[links]]`) and "Unlinked mentions" (text matching your note title but not formally linked)
- Click any result to jump to that note
- Right-click a backlink to "Open in new pane" or "Open in new tab"
- Toggle backlinks in document footer (gear icon in panel) to show/hide the panel
- Unlinked mentions are valuable for finding references you forgot to link
- Use to identify orphaned notes (notes with no backlinks) — good candidates for archiving or relinking

---

## Bookmarks

**What it does:** Quickly save and organize bookmarks to notes, headings, searches, graph views, and URLs. Acts as a quick-access menu in the sidebar.

**Enable/Configure:**
- Settings → Core plugins → toggle **Bookmarks** on
- Bookmark panel appears as a sidebar tab (ribbon icon)

**Key tips:**
- **Bookmark a note:** Right-click note in File Explorer → Bookmark, or click the bookmark icon in note header
- **Bookmark a heading:** Click the bookmark icon next to any heading (appears on hover)
- **Bookmark a saved search:** Right-click a search result in the Search panel → "Bookmark this search"
- **Bookmark a graph view:** Click the bookmark icon in the Graph View panel
- **Bookmark a URL:** In a note, highlight a link, then right-click → Bookmark (stores the URL reference)
- **Organize groups:** Create bookmark folders by collapsing/expanding groups in the Bookmarks panel for organization
- Drag and drop bookmarks to reorder; drag between groups to move
- Use for "Daily driver" notes, frequently referenced sources, or project hubs

---

## Canvas

**What it does:** Create visual, card-based diagrams by combining notes, files, and text blocks in a spatial layout. Great for mind maps, project planning, and visual thinking.

**Enable/Configure:**
- Settings → Core plugins → toggle **Canvas** on
- Create a new canvas: File → New canvas, or right-click in File Explorer → New canvas
- Save as `.canvas` files (plain JSON, version-controllable)

**Key tips:**
- Drag notes or files onto the canvas from File Explorer
- Add text blocks, images, and links directly on the canvas
- Organize spatially — layout reflects your thinking process
- **See `canvas.md`** in this reference for full Canvas usage details
- Use for literature maps, zettelkasten visualization, or sprint planning boards

---

## Command Palette

**What it does:** Universal search and trigger for all Obsidian commands (built-in and custom). Dramatically speeds up workflow by eliminating menu navigation.

**Enable/Configure:**
- Always enabled; open with **`Ctrl+P`** (Windows/Linux) or **`Cmd+P`** (Mac)
- No configuration required

**Key tips:**
- Type partial command names to fuzzy search (e.g., "fold" finds "Toggle fold")
- Show recently used commands at the top
- **Pin frequently used commands:** Click the pin icon next to a command to pin it for faster access
- Pinned commands appear at the top of the palette
- Use aliases: if a command has a longer name, type shorter keywords
- Many users bind Command Palette to a single key for ultimate speed
- Combine with hotkey customization (Settings → Hotkeys) to create custom shortcuts

---

## Daily Notes

**What it does:** Automatically create and open a new note for today with a customizable template and folder location. Foundation for journaling and daily logging workflows.

**Enable/Configure:**
- Settings → Core plugins → toggle **Daily Notes** on
- Settings → Daily Notes:
  - **Date format:** `YYYY-MM-DD` (ISO standard; can customize to `MMMM DD, YYYY` or other formats)
  - **Template file path:** Link to a template note (e.g., `_templates/daily-template`)
  - **New file location:** Folder where daily notes are saved (e.g., `Daily Notes/`)
  - **Open on startup:** Toggle to auto-open today's daily note when Obsidian launches

**Key tips:**
- Date format tokens: `YYYY` (year), `MM` (month), `DD` (day), `HH` (hour), `mm` (minutes), `ss` (seconds), `ddd` (day name), `MMMM` (month name)
- Example format: `YYYY-MM-DD ddd` produces `2026-04-03 Fri`
- Hotkey (default `Ctrl+Alt+D`) opens today's daily note instantly
- Daily note template can include frontmatter properties, agenda sections, or reflection prompts
- Combine with Templater plugin for dynamic template variables (date math, current time, etc.)
- Create "weekly notes" or "monthly notes" using the same plugin with different date formats
- Daily notes form the backbone of GTD, bullet journaling, and morning briefing workflows

---

## File Explorer

**What it does:** Navigate your vault's folder structure, create and delete notes/folders, and manage files with drag-and-drop.

**Enable/Configure:**
- Settings → Core plugins → toggle **File Explorer** on (always enabled by default)
- Panel appears in the left sidebar

**Key tips:**
- **Create notes:** Right-click folder → New note, or use Command Palette ("Create new note")
- **Create folders:** Right-click folder → New folder
- **Drag and drop:** Drag notes between folders, or drag external files into the vault
- **Reveal in system file manager:** Right-click note → Reveal in system explorer (opens OS file manager)
- **Sort options:** Click three-dot menu in File Explorer header:
  - Name (A–Z)
  - Modified (newest first)
  - Created (newest first)
  - Custom (manual reordering)
- **Collapse/expand folders:** Click arrow next to folder name
- **Quick navigation:** Type folder name to filter visible folders
- File Explorer is your structural view; use in conjunction with Search and Graph View for different perspectives

---

## File Recovery

**What it does:** Automatically creates snapshots of your notes at regular intervals. Recovers deleted or corrupted notes from snapshots without manual backups.

**Enable/Configure:**
- Settings → Core plugins → toggle **File Recovery** on
- Settings → File Recovery:
  - **Snapshot interval:** How often snapshots are created (default: 10 seconds while editing)
  - **Retention period:** How long snapshots are kept (default: 7 days)
  - Snapshots are stored in `.obsidian/plugins/obsidian-file-recovery/data/`

**Key tips:**
- **How it works:** Each time you pause editing, a snapshot is created. No action needed — automatic.
- **Recover a note:** Command Palette → "Open file recovery" or right-click a note → "Restore from snapshot"
- **View snapshots:** Shows a timeline of versions with timestamps; click to preview or restore
- **Deleted notes:** If you permanently delete a note, snapshots may still exist if recovery was enabled
- **System snapshots:** Different from version control (Git); this is a lightweight, local safety net
- **Disk space:** Snapshots take up space; adjust retention period if storage is constrained
- Use as a safety mechanism, not a replacement for Git or cloud backup

---

## Format Converter

**What it does:** Converts legacy Markdown syntax (like Wikilinks and Obsidian-specific formatting) to standard Markdown for portability and compatibility.

**Enable/Configure:**
- Settings → Core plugins → toggle **Format Converter** on
- Triggered manually on demand

**Key tips:**
- **Converts:**
  - Wikilinks `[[note]]` → standard markdown links `[note](note.md)`
  - Obsidian highlights `==text==` → strikethrough or other formats
  - Obsidian callouts to standard syntax
  - Embedded images and files to portable references
- **Use case:** Before exporting vault to another app (Notion, published website) or sharing with non-Obsidian users
- **How to run:** Command Palette → "Format Converter: Convert format" (converts entire note)
- **Backup first:** Always back up your vault before bulk conversions
- Not needed if you stay within Obsidian ecosystem; useful for future-proofing

---

## Graph View

**What it does:** Visualize your vault as an interactive network graph. Shows notes as nodes and links as edges. Reveals structure, clusters, and isolated content at a glance.

**Enable/Configure:**
- Settings → Core plugins → toggle **Graph View** on
- Open with Command Palette → "Open graph view" (global) or "Open local graph view" (current note)
- Local graph icon in note header also opens local graph

**Display Settings (gear icon in Graph View panel):**
- **Show arrows:** Display link direction
- **Show orphans:** Highlight notes with no connections
- **Show tags:** Visualize tag relationships
- **Show attachments:** Include images and files as nodes
- **Text fade threshold:** Fade text on zoomed-out view

**Advanced Settings:**
- **Filters:** Syntax examples:
  - `tag:#project` — show only nodes tagged #project
  - `path:archive` — exclude archived notes
  - `file:Daily` — show only daily notes
  - Combine with AND/OR: `tag:#work AND path:projects`
- **Groups with color coding:** Settings → Graph View → Colors (assign colors to tags, file types, or paths for visual organization)
- **Forces (physics simulation):**
  - **Repel:** Higher = nodes push apart more (default: 1)
  - **Link distance:** Length of connecting lines (default: 1)
  - **Center force:** Pull toward center (default: 0.3)

**Key tips:**
- **Global graph:** Shows entire vault structure
- **Local graph:** Shows current note and 1–2 hops of linked neighbors (more focused)
- **Click and drag nodes:** Rearrange layout manually; physics re-balances
- **Zoom:** Scroll or pinch to zoom
- **Search within graph:** Text box at top filters displayed nodes in real-time
- **Double-click a node:** Jump to that note
- **Colors and clusters:** Visually identify highly connected areas (hubs) vs. isolated branches
- Use to spot missing connections, find orphaned notes, or audit vault structure
- Bookmark your custom graph layouts (e.g., "Project Overview Graph") for quick access

---

## Note Composer

**What it does:** Merge two notes together or extract selected text into a new note. Useful for consolidating fragmented ideas or splitting overgrown notes.

**Enable/Configure:**
- Settings → Core plugins → toggle **Note Composer** on
- No additional configuration needed

**Key tips:**
- **Merge notes:**
  - Command Palette → "Note Composer: Merge current file with another"
  - Select the note to merge in
  - Choose merge location: before, after, or as a heading section
- **Extract text:**
  - Select text in a note
  - Command Palette → "Note Composer: Extract current selection"
  - Choose new note name and location
  - Original text is replaced with a link to the new note
- **Use templates during extraction:** If you set a template folder in Daily Notes or Templates settings, extracted notes can inherit template structure
- **Preserve links:** Extracted text retains internal links to other notes
- **Common use:** Split a "capture note" into separate topic notes; consolidate scattered daily notes into a weekly summary
- Combine with Templates plugin for automated heading structure after extraction

---

## Outgoing Links

**What it does:** Shows all notes and URLs that the current note links to. Complements Backlinks by showing your outward connections rather than inbound ones.

**Enable/Configure:**
- Settings → Core plugins → toggle **Outgoing Links** on
- Panel appears in the right sidebar

**Key tips:**
- **Two sections:**
  - **Links:** Notes you link to via `[[wikilinks]]` or markdown links
  - **Unlinked mentions:** References to other notes by name without formal links
- **Click a link** to jump to that note
- **Right-click for options:** "Open in new pane," "Open in new tab," etc.
- **Unlinked mentions:** Useful for discovering informal references or typos in note names
- **Paired with Backlinks:** Backlinks show who links to you; Outgoing Links show who you link to — together they map your network
- **Use for:**
  - Auditing sources and references in a note
  - Finding orphaned external URLs (links to deleted notes)
  - Ensuring proper citation and attribution

---

## Outline

**What it does:** Display a navigable outline of all headings in the current note. Click a heading to jump to that section. Invaluable for long documents.

**Enable/Configure:**
- Settings → Core plugins → toggle **Outline** on
- Panel appears in the right sidebar (or manually open with Command Palette → "Outline: Show outline")

**Key tips:**
- **Heading hierarchy:** Outline reflects your markdown heading structure (`# H1`, `## H2`, etc.)
- **Click to jump:** Click any heading in the outline to instantly scroll to that section
- **Sticky outline:** Keep outline open while you edit — stays synchronized as you scroll
- **Filter headings:** Type in the outline search box to filter by heading name
- **Keyboard shortcut:** Use arrow keys to navigate between headings if outline is focused
- **Nested structure:** Visually shows how deep your heading hierarchy is (good for spotting unbalanced structure)
- **Best practice:** Use consistent H2/H3 structure; avoid skipping levels (H1 → H4) for cleaner outlines
- Essential for large notes (meeting notes, long articles, wikis) where scrolling is tedious

---

## Page Preview

**What it does:** Hover preview of linked notes without leaving the current note. Hold `Ctrl` (or `Cmd` on Mac) and hover over an internal link to see a quick preview pane.

**Enable/Configure:**
- Settings → Core plugins → toggle **Page Preview** on (enabled by default)
- No additional configuration needed

**Key tips:**
- **Trigger:** Hold `Ctrl+hover` (Windows/Linux) or `Cmd+hover` (Mac) over any `[[wikilink]]` or markdown `[link](file.md)`
- **Preview appears:** In a small floating panel showing the first few lines of the linked note
- **Disable:** Toggle off in Core plugins if previews feel intrusive
- **Read without switching:** Skim linked content without committing to a full pane switch
- **Common use:** Verify a link before clicking, check reference notes while taking notes, explore without losing your place
- **Customize preview size:** Settings → Page Preview → Preview size (small, medium, large)
- Works with headings too: `[[note#heading]]` previews from that heading onward

---

## Properties View

**What it does:** Browse and edit all properties (frontmatter fields) across your vault. Sidebar panel for managing metadata without editing YAML directly.

**Enable/Configure:**
- Settings → Core plugins → toggle **Properties View** on
- Panel appears in the right sidebar

**Key tips:**
- **View all properties:** Properties View panel shows every field defined in the current note's frontmatter
- **Edit properties:** Click any property value to edit it inline in the panel (no need to open raw YAML)
- **Add new properties:** Click "+" in Properties View to add a new field
- **Property types:** Settings → Properties → manage types (text, number, checkbox, date, multi-select, etc.)
- **Change property type:** Edit a property in the panel; a dropdown shows available types
- **Frontmatter:** Edits in Properties View sync directly with note's YAML frontmatter at the top
- **Property inheritance:** Can set default properties in folder templates for automatic metadata
- **Use for:**
  - Books database (author, ISBN, rating)
  - Projects (status, deadline, assignee)
  - Tasks (priority, due date, tags)
- **Search by property:** Combine with Search plugin to filter notes by property values (e.g., `status:done`)

---

## Quick Switcher

**What it does:** Ultra-fast fuzzy file search and navigation. Open any note in your vault within milliseconds.

**Enable/Configure:**
- Always enabled; open with **`Ctrl+O`** (Windows/Linux) or **`Cmd+O`** (Mac)
- No configuration needed

**Key tips:**
- **Fuzzy search:** Type any part of a note title (e.g., "proj" finds "2026 Q2 Project Plan")
- **Results ranked:** Most recent, most linked, and closest name matches appear first
- **Create new note:** Type a name that doesn't exist → press `Enter` → creates a new note with that name
- **Separate search from create:** Use `>` prefix to search only (skip create)
- **Open in new pane:** Press `Ctrl+Enter` (Windows) or `Cmd+Enter` (Mac) to open in split view
- **Open in new tab:** Press `Ctrl+Tab` (Windows) or `Cmd+Tab` (Mac)
- **Recent files:** Top of list shows recently opened notes
- **Speed tip:** Remember it's faster than File Explorer for navigation; use as your primary "go to" tool
- **Keyboard-only workflow:** Master this and Command Palette for distraction-free editing

---

## Random Note

**What it does:** Open a random note from your vault with a single command. Great for serendipitous discovery, review, or breaking out of linear thinking.

**Enable/Configure:**
- Settings → Core plugins → toggle **Random Note** on
- Trigger: Command Palette → "Open random note" or set a custom hotkey

**Key tips:**
- **Serendipitous discovery:** Jump to an old note you forgot about; reminds you of prior ideas
- **Vault review:** Use daily as a way to review and refresh your knowledge base
- **Connect ideas:** When stuck, use random notes to find unexpected connections
- **Refactoring:** Regularly open random notes to audit structure, update links, or consolidate duplicates
- **Not just for fun:** Studies show spaced randomization improves retention and idea synthesis
- **Caveat:** Won't open template or archive folders if you have them; configure if needed
- Combine with Backlinks and Outgoing Links to explore your knowledge graph organically

---

## Search

**What it does:** Full-text search across your entire vault with advanced operators and regex support. Core discovery and retrieval tool.

**Enable/Configure:**
- Settings → Core plugins → toggle **Search** on (always enabled)
- Open with **`Ctrl+Shift+F`** (Windows/Linux) or **`Cmd+Shift+F`** (Mac)
- Search panel appears in left sidebar

**Search Operators:**
- **`path:folder`** — Limit search to a specific folder (e.g., `path:projects`)
- **`tag:#work`** — Search only notes with a specific tag
- **`file:name`** — Search only in filenames, not content
- **`line:text`** — Find exact lines of text
- **`block:id`** — Search for block references
- **`section:heading`** — Search within a specific heading section
- **`content:text`** — Explicit content search (default if no operator)
- **`match-case`** — Case-sensitive search
- **`ignore-case`** — Case-insensitive (default)

**Regex Search:**
- Prefix pattern with `/` and suffix with `/`: `/\bword\b/` finds whole words only
- Use regex quantifiers: `/word{2,}/` matches "word" repeated 2+ times
- Combine with operators: `path:projects /deadline:\d{4}-\d{2}-\d{2}/`

**Boolean Operators:**
- **`AND`** — Both terms required (default): `apple AND orange`
- **`OR`** — Either term: `apple OR orange`
- **`NOT`** — Exclude term: `apple NOT orange`
- Combine: `(apple OR orange) AND garden`

**Grouping & Sorting:**
- **Group results:** Settings → Search → Group results by (file, tag, heading)
- **Sort:** Click sort button in Search panel (relevance, modified date, filename)

**Embed Search Results:**
- In a note, use: `![[query: your search here]]`
- Displays live, updating search results inline in a note
- Useful for dynamic lists (all open projects, recent notes, etc.)

**Key tips:**
- Search is real-time as you type
- Star favorite searches for quick access
- Use for daily note backlinks, literature maps, or status tracking
- Combine multiple operators: `path:projects tag:#urgent file:` searches urgent project files
- Regex is powerful but slow on large vaults; use simple operators when possible

---

## Slash Commands

**What it does:** Quick command picker triggered by typing `/` while editing a note. Inserts templates, dates, or executes commands without leaving edit mode.

**Enable/Configure:**
- Settings → Core plugins → toggle **Slash Commands** on
- Trigger by typing `/` anywhere in edit mode

**Available Commands:**
- **`/date`** — Insert current date (format depends on settings)
- **`/time`** — Insert current time
- **`/template`** — Insert a template from your templates folder
- **`/heading`** — Insert a heading
- **`/link`** — Insert a wikilink with quick note selector
- **`/codeblock`** — Insert a code block with language selector
- Custom commands can be added via Community Plugins and Templater

**Key tips:**
- **No context switching:** Use slash commands to insert without opening Command Palette
- **Template insertion:** `/template` is faster than copy-paste if you have templates ready
- **Dynamic content:** With Templater plugin installed, slash commands can include date math, note titles, etc.
- **Keyboard-friendly:** Type `/` and first letters of command you want (e.g., `/t` for template)
- **Fuzzy search:** If multiple matches, navigate with arrow keys
- Reduces friction in daily note workflows

---

## Slides

**What it does:** Present a note as a slideshow directly in Obsidian. Create presentations by separating slides with `---`.

**Enable/Configure:**
- Settings → Core plugins → toggle **Slides** on
- Trigger: Command Palette → "Slides: Open presentation view" (in current note)

**Slide Syntax:**
- **Separator:** Each `---` marks a new slide
- **Multiple slides per note:** Single note can contain multiple slides
- **Example:**
  ```
  # Title Slide

  ---

  ## Content Slide

  Content here

  ---

  ## Final Slide
  ```

**Navigation Controls:**
- **Arrow keys:** Previous/next slide
- **Space bar:** Advance slide
- **Esc:** Exit presentation mode
- **Speaker notes:** Not visible in presentation; add below slides as regular content

**Themes:**
- Settings → Slides → Theme (dark, light, black, white)
- Theme affects presentation background and text colors

**Key tips:**
- **Minimal syntax:** Any note with `---` becomes presentable
- **No speaker notes in sidebar:** Speaker notes must be outside slide view
- **Use for:**
  - Pitch presentations using your vault as the source
  - Client walkthroughs of project notes
  - Internal status reviews
  - Informal talks (no need for external presentation software)
- **Combine with Canvas:** Canvas is better for mind-map presentations; Slides are better for narrative/linear talks
- **Export:** No native export to PowerPoint, but `---` format is simple enough to copy into other tools

---

## Tags View

**What it does:** Browse all tags in your vault and their hierarchy. Click a tag to filter notes with that tag. Visualize tag structure.

**Enable/Configure:**
- Settings → Core plugins → toggle **Tags View** on
- Panel appears in left or right sidebar (ribbon icon)

**Key tips:**
- **Tag hierarchy:** Nested tags (e.g., `#work/project/urgent`) display as a tree
- **Expand/collapse:** Click arrow next to a tag to expand its children
- **Filter by tag:** Click a tag name to show all notes with that tag in the main view
- **Combined tags:** Click multiple tags to filter by all of them (AND logic)
- **Tag statistics:** Numbers next to each tag show how many notes use it (useful for identifying unused tags)
- **Organize by hierarchy:** Use dot or slash notation to create nested tag structures:
  - `#work.meetings`
  - `#project/2026/q1`
- **Keep flat or hierarchical:** Depends on your preference; both work in Obsidian
- **Combine with Search:** Search is more powerful, but Tags View is visual and intuitive for browsing

---

## Templates

**What it does:** Save static note templates and insert them on demand. Includes simple date/time tokens. (Note: Core Templates is basic; Templater plugin adds advanced functions like date math and note titles.)

**Enable/Configure:**
- Settings → Core plugins → toggle **Templates** on
- Settings → Templates:
  - **Template folder path:** Where template notes are stored (e.g., `_templates/`)

**Available Tokens (Core Templates):**
- **`{{title}}`** — Inserted note's filename
- **`{{date}}`** — Current date (format from Daily Notes settings)
- **`{{time}}`** — Current time (HH:mm format)
- **`{{date:format}}`** — Custom date format (e.g., `{{date:YYYY-MM-DD ddd}}`)

**How to Create and Use:**
1. Create a note in your template folder (e.g., `_templates/Meeting Notes.md`)
2. Add content and tokens:
   ```
   # {{title}}
   Date: {{date}}
   Time: {{time}}

   ## Attendees

   ## Agenda

   ## Notes
   ```
3. Insert: Command Palette → "Insert template" → select template
4. Tokens are replaced with actual values

**Key tips:**
- **Keep templates simple:** Core Templates lacks loops and conditionals; use Templater plugin for advanced templating
- **Difference from Daily Notes:** Daily Notes auto-create dated notes; Templates insert into existing notes on demand
- **Difference from Templater:** Templater is a plugin with date math, file operations, and custom functions; Templates is core with basic tokens only
- **Organize templates:** Create subfolders within template folder (e.g., `_templates/meetings/`, `_templates/projects/`)
- **Template hygiene:** Keep templates in a hidden folder (start with `_` or `.`) to avoid cluttering File Explorer
- **Common templates:** Meeting notes, project kickoff, weekly review, book summary, daily journal
- Use with Note Composer to auto-apply templates when extracting text

---

## Unique Note Creator

**What it does:** Create timestamped notes with auto-generated unique filenames. Foundation for zettelkasten and time-based note systems.

**Enable/Configure:**
- Settings → Core plugins → toggle **Unique Note Creator** on
- Settings → Unique Note Creator:
  - **Filename format:** Customize timestamp format (default: `YYYYMMDDHHmmss`, creates `202604031030.md`)
  - **Custom prefix:** Add prefix to timestamp (e.g., `note-` creates `note-202604031030.md`)
  - **New file location:** Folder where timestamped notes are saved (default: vault root)
  - **Open new note:** Auto-open newly created note

**Timestamp Format Tokens:**
- `YYYY` = 4-digit year
- `MM` = 2-digit month
- `DD` = 2-digit day
- `HH` = 2-digit hour (24h)
- `mm` = 2-digit minutes
- `ss` = 2-digit seconds
- Example: `YYYYMMDDHHmmss` → `202604031030` (zettelkasten style, sortable)

**How to Use:**
- Command Palette → "Create unique note" or set a custom hotkey
- Note is created with auto-generated timestamp filename
- Optionally apply a template during creation (via settings or manual post-creation)

**Key tips:**
- **Zettelkasten workflow:** Perfect for fleeting notes, fleeting ideas, permanent note creation
- **Sortable by time:** Timestamp format is naturally sortable in File Explorer (oldest → newest)
- **No filename conflicts:** Timestamps guarantee unique filenames; never overwrite existing notes
- **Combine with template:** Create a template with structure (e.g., tags, source, reflection prompts) and apply it post-creation
- **Hybrid approach:** Use Unique Note Creator for capture, then rename to semantic titles later (e.g., `202604031030.md` → `Obsidian Core Plugins.md`)
- **Batch processing:** If you create many notes daily, timestamp format keeps your vault organized by creation time

---

## Web Viewer

**What it does:** Embed and display web pages within Obsidian panes. View websites, web apps, or online documents without leaving the editor.

**Enable/Configure:**
- Settings → Core plugins → toggle **Web Viewer** on
- No additional configuration needed

**How to Use:**
- Command Palette → "Open web URL"
- Enter a full URL (e.g., `https://example.com`)
- Webpage loads in a new pane or embedded in a note

**Embedding in Notes:**
- Use iframe syntax in a note:
  ```
  <iframe src="https://example.com" width="100%" height="600"></iframe>
  ```
- Renders the embedded content directly in reading view

**Key tips:**
- **Read-only:** Cannot interact with forms or inputs in embedded views (limitation)
- **Performance:** Loading web pages inside Obsidian can be slow; use for references only
- **Use cases:** Embed collaborative tools (Figma, Google Sheets), public wikis, dashboards, documentation
- **Alternative:** Often better to bookmark URLs in Bookmarks plugin and use Page Preview for quick reference
- **Offline limitation:** Web Viewer requires internet; doesn't cache pages
- **Responsive:** Embedded pages scale with pane width (set iframe width to `100%`)

---

## Word Count

**What it does:** Display word and character count for the current note in the status bar. Minimal but useful for tracking writing progress.

**Enable/Configure:**
- Settings → Core plugins → toggle **Word Count** on
- Appears automatically in the status bar at the bottom right

**What It Shows:**
- **Word count:** Total words in the current note
- **Character count:** Total characters (including spaces)
- **Updated in real-time:** Count updates as you type

**Key tips:**
- **Status bar location:** Look at bottom right of the Obsidian window
- **Click for details:** Click the word count to see breakdown (words, characters, with/without spaces)
- **Goal tracking:** Useful for daily writing challenges (e.g., "1000 words today")
- **No configuration needed:** Works out of the box
- **Note:** Count includes markdown syntax; `[[links]]` and `**bold**` are counted as characters
- **Not for accuracy:** Use external tool if you need final manuscript counts (excluding markdown); Word Count is for drafting feedback only

---

## Workspaces

**What it does:** Save pane layouts and quickly switch between them. Organize your editor environment for different working modes.

**Enable/Configure:**
- Settings → Core plugins → toggle **Workspaces** on
- Workspace panel appears in left sidebar ribbon

**How to Create and Use:**
1. Arrange your panes exactly as you want (note editor, outline, backlinks, graph view, search, etc.)
2. Command Palette → "Workspaces: Save layout as new workspace"
3. Name the workspace (e.g., "Writing Mode," "Research," "Review")
4. Click saved workspace in Workspaces panel to switch layouts instantly

**Workspace Operations:**
- **Load workspace:** Click workspace name in Workspaces panel or Command Palette → "Workspaces: Load [workspace name]"
- **Delete workspace:** Right-click workspace name → Delete
- **Rename workspace:** Double-click workspace name to edit
- **Export/Import:** Workspaces are stored in `.obsidian/workspaces.json` for backup or sharing

**Common Workspace Examples:**
- **Writing Mode:** Note editor full-width, minimal sidebar, Outline open
- **Research Mode:** Split panes (left: source note, right: current writing), Graph View, Tags View
- **Review Mode:** Note editor center, Backlinks + Outline on right, File Explorer on left
- **Reference Mode:** Web Viewer + Note editor split, Page Preview enabled

**Key tips:**
- **Fast context switching:** Jump between writing, research, and review without manual pane rearrangement
- **Persistence:** Workspaces retain their layouts even after Obsidian restarts (if enabled)
- **Minimize friction:** Each workspace pre-configures the tools you need for that task
- **Combine with hotkeys:** Assign hotkeys to load specific workspaces for one-keystroke switching
- **Team collaboration:** Export workspaces in `.obsidian/workspaces.json` and share with team members
- **Experiment:** Create test workspaces; delete ones that don't work for you
- **Mobile note:** Workspaces may be limited on mobile; primarily a desktop feature

---

## Summary Table

| Plugin | Use Case | Key Hotkey |
|--------|----------|-----------|
| Audio Recorder | Voice notes | See toolbar |
| Backlinks | Inbound connections | Open sidebar |
| Bookmarks | Quick access favorites | Sidebar icon |
| Canvas | Visual knowledge maps | Create new canvas |
| Command Palette | Universal command search | `Ctrl/Cmd+P` |
| Daily Notes | Journaling, daily logging | `Ctrl/Cmd+Alt+D` |
| File Explorer | Vault navigation | Sidebar (always on) |
| File Recovery | Snapshot recovery | Command Palette |
| Format Converter | Export/legacy conversion | Command Palette |
| Graph View | Visualize vault structure | Command Palette |
| Note Composer | Merge/extract notes | Command Palette |
| Outgoing Links | Outbound connections | Sidebar |
| Outline | Navigate long notes | Sidebar |
| Page Preview | Hover link preview | `Ctrl/Cmd+hover` |
| Properties View | Metadata management | Sidebar |
| Quick Switcher | Fast file navigation | `Ctrl/Cmd+O` |
| Random Note | Serendipitous discovery | Command Palette |
| Search | Full-text vault search | `Ctrl/Cmd+Shift+F` |
| Slash Commands | Quick insertion | Type `/` in edit mode |
| Slides | Present notes as slides | Command Palette |
| Tags View | Browse tag hierarchy | Sidebar |
| Templates | Reusable static templates | Command Palette |
| Unique Note Creator | Timestamped notes | Command Palette |
| Web Viewer | Embed web pages | Command Palette |
| Word Count | Writing progress | Status bar |
| Workspaces | Save pane layouts | Command Palette |

---

**Last updated:** 2026-04-03
**Obsidian version:** Current (1.0+)
**Note:** Settings paths and options may vary slightly with Obsidian updates. Refer to in-app documentation for latest changes.
