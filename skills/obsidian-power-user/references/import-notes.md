# Importing Notes into Obsidian

## General Import Best Practices

Before importing from any source:

1. **Backup your source** — Export your original vault/library completely
2. **Test with a small batch** — Import 10-20 notes first to verify quality
3. **Run post-import cleanup:**
   - Verify frontmatter format and consistency
   - Fix broken links and references
   - Standardize tag naming and casing
   - Check media file placement and links
   - Review and normalize formatting

---

## 1. Apple Notes

**Importer:** Obsidian Community Plugin `Apple Notes Importer`

**Preserved:**
- Note text and basic formatting (bold, italic)
- Folder structure as Obsidian folders
- Checklist items (converted to `- [ ]` checkboxes)
- Images and attachments (saved locally)
- Creation and modification dates

**Lost or needs cleanup:**
- Apple Notes-specific styling (colors, pins) — becomes plain text
- Handwritten notes — not imported (export as images first if needed)
- Links to other notes — must be manually re-created with `[[wikilinks]]`
- Shared note metadata
- Apple Reminders pinned to notes

**Process:**
1. Install `Apple Notes Importer` plugin in Obsidian
2. Open plugin settings → select import location
3. Select which folders/notes to import
4. Plugin reads directly from Apple Notes database and imports
5. Post-import: Test wikilink structure, verify attachment paths

---

## 2. Bear

**Importer:** Obsidian Community Plugin `Bear Importer`

**Preserved:**
- Note title and content
- Nested folder/tag structure
- Bear tags (converted to Obsidian folder structure by default, or can use `#hashtags`)
- Images and attachments (copied to vault)
- Highlighted text (formatting preserved)
- Links to other notes (converted to `[[wikilinks]]`)
- Creation and modification dates

**Lost or needs cleanup:**
- Bear-specific metadata (archived state, pinning)
- Note icons and colors
- Shared notes sync metadata
- Some inline formatting edge cases

**Process:**
1. In Bear, export notes: File → Export Notes
2. Choose export format (best is `.enex` or via iCloud backup)
3. Install `Bear Importer` plugin in Obsidian
4. Point to exported Bear backup or `.enex` file
5. Select import options (preserve tags as hashtags or as folders)
6. Run import
7. Post-import: Check tag naming, verify media file paths

---

## 3. Craft

**Importer:** Obsidian Community Plugin `Craft Importer`

**Preserved:**
- Document structure (pages and sub-pages)
- Formatted text (bold, italic, headings)
- Embeds (convert to links or local copies)
- Backlinks within Craft documents
- Images and files (downloaded to vault)
- Code blocks with language syntax
- Database records (if available)

**Lost or needs cleanup:**
- Craft workspace metadata and settings
- Custom colors and styling beyond markdown
- Real-time collaboration metadata
- Web embeds (converted to links; embedded content not mirrored)
- Database relationships beyond simple backlinks

**Process:**
1. Export from Craft: Select workspace → Share → Export (as `.craft` or HTML)
2. Install `Craft Importer` in Obsidian
3. Upload the exported file or backup
4. Configure mapping: which Craft sections map to which Obsidian folders
5. Run import
6. Post-import: Check embed links, verify database structure integrity

---

## 4. Evernote

**Importer:** Obsidian Community Plugin `Evernote Importer` or native `.enex` support

**Preserved:**
- Note title, content, and formatting
- Notebook structure (maps to folders)
- Tags (preserved as `#hashtags` or folder structure)
- Images and PDFs (attached files downloaded)
- Creation and update dates
- Note links (converted to `[[wikilinks]]`)
- Code blocks

**Lost or needs cleanup:**
- Evernote-specific metadata (shared notebooks, permissions)
- Reminders and due dates (save as frontmatter manually)
- Business cards and contacts metadata
- Email forwarding metadata
- Tables (can be converted to markdown, but may need cleanup)
- Highlighted text color (highlighting removed; use `==syntax==` for markup)

**Process:**
1. Export from Evernote: Select notebook → Export Notes → choose `.enex` format
2. Install `Evernote Importer` plugin
3. Open plugin, select the `.enex` file(s)
4. Choose import location in vault
5. Run import
6. Post-import: Verify table formatting, check tag case consistency, fix date fields if needed

---

## 5. Google Keep

**Importer:** Obsidian Community Plugin `Google Keep Importer` or `Google Keep to Markdown`

**Preserved:**
- Note text and basic formatting
- Checklists (converted to `- [ ]` markdown checkboxes)
- Colors (can be used to inform folder organization or tags)
- Images attached to notes (saved locally)
- Labels (converted to hashtags or folder structure)
- Dates (can be extracted manually or via API)

**Lost or needs cleanup:**
- Keep color coding (no color metadata preserved; use tags instead)
- Collaborative editing metadata
- Voice memos (export separately as audio files first)
- Pin/archive state (noted in frontmatter manually if needed)
- Synced files (Google Drive links only; files not mirrored)

**Process:**
1. Export from Keep: Select note → More options → Download
2. Repeat for all notes, or use API for bulk export via third-party tool (e.g., `google-keep-to-markdown`)
3. For bulk export: Use `google-keep-to-markdown` CLI tool with Google account authentication
4. Import the resulting markdown files into Obsidian vault
5. Post-import: Organize by labels (convert to `#tags` or folders), verify checklist syntax

---

## 6. Microsoft OneNote

**Importer:** Obsidian Community Plugin `OneNote Importer` (limited native support; third-party tools recommended)

**Preserved:**
- Page structure (sections and pages map to folder hierarchy)
- Text and basic formatting (bold, italic, headings)
- Images and embedded files
- Tables (converted to markdown tables)
- Code blocks
- Page creation/modification dates

**Lost or needs cleanup:**
- OneNote-specific metadata (page tabs, section groups)
- Pen/drawing annotations (must export as images separately)
- Outline view and collapsible sections
- Handwriting (export as images first)
- Embedded Office documents
- Real-time collaboration metadata
- Hyperlinks may need fixing to point to local wikilinks

**Process:**
1. Export from OneNote: Right-click notebook → Export
2. Choose export format (HTML + images recommended)
3. Install `OneNote Importer` plugin (or use third-party tool like `o2md`)
4. Point to exported folder
5. Run import, configure section/page mapping
6. Post-import: Check table formatting, verify image links, test cross-page links

---

## 7. Notion

**Importer:** Obsidian Community Plugin `Notion Importer` (via official Notion export)

**Preserved:**
- Database records and properties (converted to markdown with frontmatter)
- Document structure (pages and nested pages → folders)
- Relations (converted to backlinks or `[[wikilinks]]`)
- Database templates (metadata, but design not preserved)
- Images, files, and embeds (downloaded locally)
- Text formatting and code blocks
- Databases with simple properties (text, multi-select, date, checkbox)

**Lost or needs cleanup:**
- Complex Notion database features (formulas, rollups, aggregations) — become plain text
- Database views (filters, sorts, groupings) — not replicated
- Inline database queries
- Synced blocks (duplicated content; delete duplicates manually)
- Database buttons and automation
- Multi-select/relation field values — converted to comma-separated text or tags
- Notion comments (thread metadata)

**Process:**
1. Export from Notion: Select workspace/database → Export → Markdown & CSV format
2. Download the exported `.zip` file
3. Install `Notion Importer` plugin in Obsidian
4. Open plugin, select the exported folder
5. Configure mapping: database fields to frontmatter properties, relation handling
6. Run import
7. Post-import: Convert database frontmatter to consistent YAML format, test backlinks, delete synced duplicates, convert multi-select fields to hashtags or [[links]]

---

## 8. Roam Research

**Importer:** Obsidian Community Plugin `Roam Importer` or third-party JSON converter

**Preserved:**
- Graph structure (backlinks and [[wikilinks]])
- Block structure and hierarchy
- Attributes (converted to frontmatter or inline properties)
- Text and formatting
- Images and attachments
- Aliases and page synonyms
- Daily notes structure

**Lost or needs cleanup:**
- Roam-specific metadata (block refs with `^xxxx` syntax — converted but may break)
- Block embeds and transclusion syntax (converted to links)
- Roam queries and dynamic content
- Custom CSS and workspace styling
- Smart block logic
- Built-in integrations (Slack, Google Drive sync, etc.)

**Process:**
1. Export from Roam: Export all → choose JSON format
2. Install `Roam Importer` plugin in Obsidian
3. Upload the JSON export file
4. Configure: block structure handling, backlink conversion, daily note format
5. Run import
6. Post-import: Verify block reference syntax, test backlinks, check for circular references, cleanup block embeds

---

## 9. CSV Files

**Importer:** Obsidian Community Plugin `CSV Importer` or manual import

**Preserved:**
- CSV data and rows (converted to table format or frontmatter)
- Column headers (become property names)
- All cell content (text, links, etc.)

**Lost or needs cleanup:**
- CSV formatting and styles
- Excel formulas (become plain text values)
- Merged cells

**Process:**
1. Export source as CSV file
2. Install `CSV Importer` plugin
3. Open plugin, select CSV file
4. Configure: delimiter (comma, tab, etc.), which column is note title, which columns become frontmatter vs. note content
5. Run import
6. Post-import: Verify property names and data types, format frontmatter consistently, convert links manually if needed

**Example:** CSV with columns: `Title`, `Topic`, `URL`, `Notes`
```csv
Title,Topic,URL,Notes
My Note,Design,https://example.com,First design note
```
→ Becomes note with title "My Note", frontmatter `topic: Design`, `url: https://example.com`, and notes in body.

---

## 10. HTML Files

**Importer:** Obsidian Community Plugin `HTML to Markdown` or third-party converter

**Preserved:**
- Heading hierarchy
- Text and formatting
- Links (href attributes)
- Images (src paths converted or downloaded)
- Lists and code blocks

**Lost or needs cleanup:**
- HTML-specific styling (colors, fonts, CSS classes)
- JavaScript and interactivity
- Complex table layouts
- Embedded media (video, audio) — links preserved, files not
- HTML comments
- Form elements

**Process:**
1. Save or export HTML file(s)
2. Use `HTML to Markdown` plugin or CLI tool (e.g., `pandoc`)
3. If using plugin: Open in Obsidian, run conversion
4. If using CLI: `pandoc input.html -t markdown -o output.md`
5. Import resulting markdown files into vault
6. Post-import: Fix relative links, verify image paths, check table formatting

---

## 11. Markdown Files

**Importer:** Direct vault import (copy/paste or drag-and-drop)

**Preserved:**
- All markdown syntax (headings, bold, italic, code)
- Links (both `[text](url)` and `[[wikilinks]]`)
- Images and embedded files
- Frontmatter (YAML at top)
- Code blocks with syntax highlighting
- Tables and lists
- Formatting edge cases

**Lost or needs cleanup:**
- File path structure (must manually organize into folders)
- Relative links may break if folder structure doesn't match original
- Some extended markdown syntax (depends on Obsidian theme/plugins)

**Process:**
1. Organize markdown files into folders matching desired vault structure
2. Drag files directly into Obsidian vault in file explorer
3. Or copy/paste files into vault folder via terminal: `cp -r source/* vault/`
4. If importing from repo, update image/link paths to match new vault structure
5. Post-import: Run `Find and Replace` on link patterns to fix relative paths, verify wikilinks work

---

## 12. Textbundle Files

**Importer:** Obsidian Community Plugin `TextBundle Importer` or third-party converter

**Preserved:**
- Text content and markdown formatting
- Assets folder (images, files)
- Metadata (creation date, modification date from metadata.json)

**Lost or needs cleanup:**
- Textbundle-specific metadata fields
- Original folder/app context

**Process:**
1. Export from source app as Textbundle (`.textbundle` package)
2. Install `TextBundle Importer` plugin
3. Open plugin, select the textbundle file
4. Configure: title handling, asset folder destination
5. Run import
6. Post-import: Verify image links point to correct asset paths, check frontmatter

---

## 13. Zettelkasten Notes

**Importer:** If exporting from Zettlr, The Archive, or similar: use markdown export + manual ID mapping

**Preserved:**
- Note ID scheme (e.g., `202401011423`) — preserved in filename or frontmatter
- Markdown content
- Tags and cross-references
- Images and attachments

**Lost or needs cleanup:**
- Original app-specific metadata
- Timestamp linking (may need to update ID format for Obsidian)
- Category/folder organization from original app
- Bidirectional link structure (becomes one-directional unless manually curated)

**Process:**
1. Export from source app (Zettlr, The Archive, etc.) as markdown
2. Files typically named with IDs: `202401011423 Note Title.md`
3. Import all files directly into vault
4. Add frontmatter with ID: `id: 202401011423`
5. Convert ID-based references (e.g., `[[202401011423]]`) to title-based wikilinks: `[[Note Title]]`
6. Post-import: Build structure notes to recreate index/outline, verify backlink relationships

---

## 14. Apple Journal

**Importer:** Limited native support; third-party export required

**Preserved:**
- Journal entry text and dates
- Images and photos attached to entries
- Mood/activity tags (if exported)

**Lost or needs cleanup:**
- Journal-specific privacy features
- Entry locking/security (export as plaintext, then add encryption at Obsidian level if needed)
- Mood/activity metadata (save as frontmatter manually)
- Geolocation data
- Apple Health integration

**Process:**
1. Apple Journal: Long press entry → Share/Export (if available)
2. If no native export: Take screenshots or copy-paste entries manually
3. For bulk export: Use automation tool (Shortcuts app) to export all as text or PDF
4. Import the exported text files, or OCR screenshots
5. Create frontmatter template for date, mood, activity
6. Post-import: Backfill frontmatter with metadata, organize by date/tag

---

## Post-Import Cleanup Checklist

After importing from any source:

- [ ] Verify frontmatter format (`title`, `date`, `tags`, `aliases`)
- [ ] Test wikilinks: run `Find unlinked mentions` or use backlinks pane
- [ ] Check for broken image/file links (use `File recovery` plugin if needed)
- [ ] Standardize tag naming and casing (e.g., `#Project` vs `#project`)
- [ ] Remove duplicate notes (especially from synced blocks or versioning)
- [ ] Test cross-vault links if importing from multiple sources
- [ ] Review and clean up any placeholder metadata (blank fields, "TODO" entries)
- [ ] Verify HTML encoding (especially for special characters: `&amp;`, `&quot;`)
- [ ] Check relative link paths — update if folder structure changed
- [ ] Run `Orphaned files` check to find and categorize unlinked notes
