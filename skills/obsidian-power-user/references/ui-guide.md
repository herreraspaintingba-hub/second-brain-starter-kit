# Obsidian UI Reference Guide

A complete guide to navigating and customizing Obsidian's interface.

---

## Appearance

### Themes

**Installing community themes:**
1. Settings → Appearance → Themes → Browse
2. Search for theme name
3. Click Install, then Use to activate

**Switching themes:**
- Settings → Appearance → Themes → Manage
- Click the theme name to activate
- Light/dark toggle: Settings → Appearance → toggle "Light" or "Dark" under Themes

**Base color scheme:**
- Settings → Appearance → Accent color
- Choose from preset colors or enter custom hex code

**Custom fonts:**
- **Interface font:** Settings → Appearance → Interface font dropdown
- **Editor (monospace) font:** Settings → Appearance → Editor font dropdown
- Both dropdowns show system fonts plus any installed custom fonts

**CSS snippet activation:**
1. Settings → Appearance → CSS snippets → Open snippets folder
2. Place `.css` files in the `snippets` directory
3. Return to Settings → Appearance → CSS snippets
4. Toggle snippets on/off with the eye icon
5. Reload with Ctrl+Shift+R (Windows/Linux) or Cmd+Shift+R (macOS)

**Font size:**
- Settings → Appearance → Font size slider
- Adjusts interface and editor text size proportionally

---

## Drag and Drop

**Reorganizing files in File Explorer:**
- Click and drag files/folders to new locations within the vault
- Drop zones highlight when dragging over valid targets

**Moving tabs between panes:**
- Click and drag a tab to another pane
- Drag to the edge of a pane to create a new split

**Dragging tabs to new windows:**
- Drag a tab outside the main window to create a pop-out window
- Drag between windows to move tabs

**External files into vault:**
- Drag files from your file system into File Explorer
- Files are copied into the vault folder
- Drag images directly into an open note to embed them

**Creating links via drag:**
- Drag a file from File Explorer into the editor
- Automatically creates a link: `[[filename]]`
- Drag with Shift held to insert embed: `![[filename]]`

---

## Hotkeys

### Managing Hotkeys

**View all hotkeys:**
- Settings → Hotkeys

**Search for commands:**
- Settings → Hotkeys → search box at top
- Type action name to find its hotkey

**Assign custom hotkeys:**
1. Settings → Hotkeys
2. Find the command
3. Click the pencil icon
4. Press your desired key combination
5. Click the check mark to save

**Resolving conflicts:**
- When assigning a hotkey that conflicts with another command, Obsidian shows a warning
- Reassign one of the conflicting commands

### Essential Default Hotkeys

| Action | Windows/Linux | macOS |
|---|---|---|
| Command palette | `Ctrl+P` | `Cmd+P` |
| Quick switcher | `Ctrl+O` | `Cmd+O` |
| Search current vault | `Ctrl+Shift+F` | `Cmd+Shift+F` |
| Bold | `Ctrl+B` | `Cmd+B` |
| Italic | `Ctrl+I` | `Cmd+I` |
| New note | `Ctrl+N` | `Cmd+N` |
| Close current tab | `Ctrl+W` | `Cmd+W` |
| Split pane right | `Ctrl+\` | `Cmd+\` |
| Toggle edit/preview mode | `Ctrl+E` | `Cmd+E` |
| Toggle left sidebar | `Ctrl+J` | `Cmd+J` |
| Toggle right sidebar | `Ctrl+I` | `Cmd+I` |
| Cycle through open tabs | `Ctrl+Tab` | `Cmd+Tab` |
| Toggle focus mode (reading view) | — | — |
| Follow link | `Ctrl+Click` | `Cmd+Click` |

---

## Language Settings

**Change interface language:**
1. Settings → About
2. Language dropdown near top
3. Select from available languages
4. Interface updates immediately

**Available languages include:**
- English (default)
- 中文 (Simplified Chinese)
- 繁體中文 (Traditional Chinese)
- Español
- Français
- Deutsch
- 日本語
- 한국어
- Português (Brasil)
- Русский
- And 15+ others

---

## Pop-out Windows

**Detach a tab into floating window:**
- Right-click tab → Open in new window
- Or drag tab outside the main window boundary

**Managing multiple windows:**
- Each window is independent but accesses the same vault
- Sync between windows is automatic
- Close individual windows without closing Obsidian

**Dragging between windows:**
- Drag tabs between open windows
- Useful for side-by-side reference or multi-monitor setups

---

## Ribbon

**What it is:**
- Vertical icon strip on the far left side of the interface
- Quick access to frequently used actions
- Default icons: New note, Create folder, Search, Bookmarks, etc.

**Show/hide ribbon items:**
1. Right-click on the ribbon
2. Toggle commands on/off
3. Only active commands display as icons

**Reorder ribbon icons:**
- Click and drag icons up/down to reorder
- Changes persist in your workspace

**Default ribbon icons and their functions:**
- **New note**: Create a blank note (Ctrl+N)
- **Create folder**: Add a new folder to the vault
- **Search**: Open search panel (Ctrl+Shift+F)
- **Bookmarks**: Toggle bookmarks sidebar
- **Toggle left sidebar**: Show/hide file explorer and search (Ctrl+J)
- **Command palette**: Open command palette (Ctrl+P)
- **Theme toggle**: Switch between light/dark themes
- **Additional icons**: Added by enabled plugins

---

## Settings Navigation

**Opening Settings:**
- Click the gear icon in the top-right corner
- Or use Command Palette → "Open settings"

**Main settings sections:**

**Editor**
- Editor indentation (spaces vs. tabs)
- Line wrapping behavior
- Show/hide line numbers
- Cursor blinking
- Spellcheck language
- Default markdown flavor

**Files & Links**
- New note location
- New file location
- Automatically update internal links
- Confirm file deletion
- Detect all file extensions

**Appearance**
- Themes and colors
- Font customization
- Accent color
- CSS snippets
- Font size
- Readable line length (toggle)

**Hotkeys**
- View and customize all command hotkeys
- Resolve conflicts

**Core Plugins**
- Toggle built-in plugins on/off
- Plugins include: File explorer, Search, Bookmarks, Outline, Backlinks, Tag pane, Quick switcher, File recovery, Command palette, Graph view, Publish, Slash commands, Templates, and more

**Community Plugins**
- Browse and install third-party plugins
- Enable/disable installed plugins
- Configure individual plugin settings

**About**
- Obsidian version
- Interface language selection
- Vault statistics (file count, total size)
- Help and documentation links

---

## Sidebar

### Left Sidebar

**Panels:**
- **File Explorer**: Browse and manage vault files and folders
- **Search**: Find notes by text, tags, or properties
- **Bookmarks**: Quick access to favorite files and searches

**Actions:**
- Click panel icons at the top of the left sidebar to switch views
- Collapse/expand individual panels by clicking the panel header
- Pinning: Click the pin icon to keep a panel visible when switching between others

### Right Sidebar

**Panels:**
- **Backlinks**: Notes that link to the current note
- **Outgoing Links**: Links from the current note to other notes
- **Tags**: All tags used in the current note
- **Outline**: Heading hierarchy of the current note

**Actions:**
- Click panel icons at the top of the right sidebar to switch views
- Collapse/expand panels by clicking headers
- Pin important panels for constant visibility

**Moving panels between sidebars:**
- Drag a panel header to the opposite sidebar
- Left sidebar can hold any right sidebar panel and vice versa

**Toggle sidebars:**
- Click toggle icons in the ribbon
- Hotkey: Ctrl+J (Windows/Linux) or Cmd+J (macOS) for left sidebar
- Hotkey: Ctrl+I (Windows/Linux) or Cmd+I (macOS) for right sidebar

---

## Status Bar

**Location:**
- Bottom bar of the Obsidian window

**Default information:**
- **Word count**: Total words in the current note (hover for character/line count)
- **Cursor position**: Line and column number of cursor
- **Sync status**: Cloud sync indicator (if using Obsidian Sync)

**Plugin additions:**
- Community and core plugins can add status bar items
- Examples: word count display, reading time, character count, spell check status
- Click status bar items to open related panels

---

## Tabs

### Tab Groups and Splits

**Creating splits:**
- Right-click tab → Split right (vertical split) or Split down (horizontal split)
- Hotkey: Ctrl+\ (Windows/Linux) or Cmd+\ (macOS) for split right
- Each pane is independent and can hold multiple tabs

**Tab cycling:**
- Ctrl+Tab (Windows/Linux) or Cmd+Tab (macOS) cycles through open tabs
- Tab list shows recently accessed files first

**Closing tabs:**
- Click the X on a tab to close it
- Middle-click a tab to close it
- Hotkey: Ctrl+W (Windows/Linux) or Cmd+W (macOS)

### Stacked Tabs (Andy Matuschak Mode)

**What it is:**
- Tabs stack horizontally instead of displaying in a traditional tab bar
- Each tab shows as a small card with preview
- Space-efficient for viewing multiple notes
- Named after the note-taking approach that inspired it

**Enable stacked tabs:**
1. Settings → Editor → Tab stacking
2. Choose "Stacked tabs" option
3. Tabs now display as overlapping cards when multiple files open

### Pinned Tabs

**Pin a tab:**
- Right-click tab → Pin
- Or click the pushpin icon on the tab

**Pinned tab behavior:**
- Stays visible at the start of the tab group
- Not closed by "Close others" actions
- Indicates which notes you want constant access to

**Unpinning:**
- Right-click pinned tab → Unpin
- Or click the pushpin icon again

### Linked Panes

**Link panes together:**
- Right-click a pane header → Link panes
- When you follow a link in one pane, the linked pane opens it in a preview panel
- Useful for editing one note while previewing another

---

## Workspace Layouts

**Saving current layout:**
1. Arrange panes, sidebars, and panels as desired
2. Settings → Workspaces → Create new workspace
3. Enter a name (e.g., "Writing Mode", "Research")
4. Your current layout is saved

**Loading saved workspaces:**
- Settings → Workspaces → click workspace name to load
- Or use Command Palette → search workspace name

**Switching between workspaces:**
- Workspaces are quick-switchable from settings or command palette
- Each workspace remembers its own tab arrangement, sidebar state, and pane positions
- Switching workspaces preserves each workspace's state

### Example Workspace Setups

**Writing Mode**
- Single editor pane, full width
- Left sidebar hidden
- Right sidebar hidden
- Minimal distractions
- Use for deep work on a single note

**Research Mode**
- Split panes: source material on left, notes on right
- Left sidebar visible with file explorer
- Right sidebar visible with outline panel
- Allows cross-referencing while taking notes

**Review Mode**
- Editor pane in center
- Left sidebar: file explorer for navigation
- Right sidebar: outline panel (for heading structure) and backlinks panel (to see what references this note)
- Good for editing and understanding context

**Reference Mode**
- Multiple stacked tabs in one pane
- Right sidebar showing backlinks and outgoing links
- Left sidebar hidden to maximize space
- Quick jumping between related notes

---

## Quick Tips

- **Command Palette (Ctrl+P / Cmd+P)** is the fastest way to do anything — learn it first
- **Quick Switcher (Ctrl+O / Cmd+O)** for rapid note switching by typing filename
- Create custom hotkeys for actions you use frequently
- Use workspaces to separate your work modes (writing vs. research vs. admin)
- Pin the Outline panel in your right sidebar when working on longer documents
- Experiment with different themes and fonts to find what feels best
