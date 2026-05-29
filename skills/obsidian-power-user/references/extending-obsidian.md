# Extending Obsidian: Plugins, Themes, and Customization

## Community Plugins

### Installing and Managing Plugins

1. Open **Settings → Community plugins**
2. Click **Browse** to browse the community plugin directory
3. Search for a plugin by name or function
4. Click the plugin card and select **Install**
5. Once installed, toggle the plugin **On** in the Community plugins list to enable it

**Disabling plugins:** Toggle off without uninstalling (preserves settings).

**Updating plugins:** In Community plugins list, check for an **Update** button next to each plugin. Obsidian also shows a notification when updates are available.

**Restricted Mode**
- By default, Obsidian runs in **Restricted Mode** — third-party plugins are disabled
- When you enable your first plugin, Obsidian asks if you want to exit Restricted Mode
- **What it does:** Restricted Mode prevents any third-party plugins from running, isolating you from potential security risks
- **When to use it:** Use if you're concerned about plugin security or want to troubleshoot issues caused by plugin conflicts
- **Toggling:** Settings → Community plugins → toggle **Restricted Mode** (top of the plugins list)

## Themes

### Installing and Switching Themes

1. **Settings → Appearance → Themes**
2. Click **Manage** (in the Theme section)
3. Browse themes and click **Use** next to any theme to apply it immediately
4. Switch back to **Default** theme at any time

### Light and Dark Variants

Most Obsidian themes include both light and dark color schemes:
- **Settings → Appearance → Color scheme** — choose **Light**, **Dark**, or **System** (follows OS settings)
- A well-designed theme has distinct palettes for each variant
- Not all themes support both — check the community plugin directory listing

### Popular Themes Worth Exploring

| Theme | Characteristics | Best For |
|---|---|---|
| **Minimal** | Clean, distraction-free, highly customizable | Minimalist workflow, custom CSS tweaking |
| **Things** | Inspired by Things.app, warm and inviting | Visual notes, task tracking, aesthetics |
| **Blue Topaz** | Modern, colorful, rich visual hierarchy | High-volume reading/organizing, visual learners |
| **Prism** | Vibrant colors, strong contrast, playful | Creative work, color-coded organization |

## CSS Snippets

### Creating and Activating CSS Snippets

1. Open your vault folder on disk
2. Navigate to `.obsidian/snippets/` (create the folder if it doesn't exist)
3. Create a new file with `.css` extension (e.g., `custom-colors.css`)
4. Write your CSS
5. In Obsidian: **Settings → Appearance → CSS Snippets** → click the refresh icon
6. Toggle each snippet **On** to enable it

**Snippets are loaded automatically** once enabled — no restart needed.

### Common CSS Snippet Examples

#### 1. Custom Callout Colors

```css
/* Create a new callout type with custom colors */
.callout[data-callout="custom"] {
  --callout-color: 147, 51, 234; /* purple RGB */
  --callout-icon: 💡;
}

/* Or override an existing callout */
.callout[data-callout="note"] {
  --callout-color: 59, 130, 246; /* blue */
}
```

#### 2. Editor Width Adjustment

```css
/* Make editor wider (increase from default 40em) */
.cm-editor {
  max-width: 60em;
}

/* Or narrower for focused reading */
.markdown-source-view.mod-cm6 .cm-content {
  max-width: 50em;
  margin: 0 auto;
}
```

#### 3. Font Override

```css
/* Change editor font */
.cm-editor {
  font-family: "Monaco", "Menlo", monospace;
  font-size: 15px;
  line-height: 1.6;
}

/* Change UI font */
body {
  font-family: "Inter", "Helvetica Neue", sans-serif;
}
```

#### 4. Custom Checkbox Styles

```css
/* Style checkbox behavior */
input[type="checkbox"] {
  accent-color: #4a9eff; /* checked color */
}

/* Hide default checkbox, use emoji instead */
.task-list-item-checkbox {
  display: none;
}

.task-list-item {
  list-style-image: url("data:image/svg+xml,..."); /* custom SVG */
}

/* Alternative: style completed tasks */
.task-list-item input[type="checkbox"]:checked {
  background-color: #22c55e;
  border-color: #22c55e;
}
```

#### 5. Hide Specific UI Elements

```css
/* Hide the ribbon (left sidebar icons) */
.side-dock-ribbon {
  display: none;
}

/* Hide the status bar (bottom bar) */
.status-bar {
  display: none;
}

/* Hide document properties/metadata */
.metadata-container {
  display: none;
}

/* Hide heading indicators in edit mode */
.cm-header {
  font-weight: 400;
  color: inherit;
}

/* Reduce indentation depth visibility */
.cm-indent {
  display: none;
}
```

## Plugin Security

### Understanding Restricted Mode

Obsidian's **Restricted Mode** is designed to protect you from potentially malicious plugins:
- When enabled, all third-party plugins are **completely disabled**
- Only core Obsidian functionality is available
- No plugins can access your vault data, file system, or network

### What Community Plugins Can Access

Depending on their code, community plugins *could* theoretically:
- Read and write files in your vault
- Access your file system (if using Obsidian.md sync or other paths)
- Make network requests (call external APIs, send data)
- Execute arbitrary JavaScript

### Best Practices for Plugin Security

1. **Install only plugins you trust** — check ratings, reviews, and GitHub repos
2. **Review plugin source code** on GitHub before installing if possible
3. **Keep plugins updated** — security patches are released regularly
4. **Audit inactive plugins** — regularly uninstall plugins you no longer use
5. **Use Restricted Mode for sensitive vaults** — if you have a vault with highly sensitive data, keep it in Restricted Mode
6. **Check permissions in plugin descriptions** — a good plugin author documents what their plugin accesses
7. **Disable plugins if you notice strange behavior** — test if a plugin is causing issues by toggling it off

## Obsidian URI Protocol

Obsidian uses the `obsidian://` protocol to enable deep linking and automation from other apps.

### URI Actions and Patterns

| Action | URI Pattern | Purpose | Example |
|---|---|---|---|
| `open` | `obsidian://open?vault=VaultName&file=NotePath` | Open a vault or file | `obsidian://open?vault=MyVault&file=Projects%2FQ1%202025` |
| `new` | `obsidian://new?vault=VaultName&name=NewNote&content=Hello` | Create a new note with optional content | `obsidian://new?vault=MyVault&name=Meeting%20Notes&content=Date%3A%202025-03-01` |
| `search` | `obsidian://search?vault=VaultName&query=searchterm` | Open vault and run a search | `obsidian://search?vault=MyVault&query=budget` |
| `hook-get-address` | `obsidian://hook-get-address` | Hook integration (returns current note URL) | Used by Hook app for bidirectional linking |

### URL Encoding Requirements

Spaces and special characters must be **URL-encoded** in URIs:
- Space → `%20`
- Slash (for folder paths) → `/` (literal, not encoded)
- Colon → `%3A`
- Question mark → `%3F`
- Ampersand → `%26`

**Example:**
```
Bad:  obsidian://new?vault=My Vault&name=Meeting Notes
Good: obsidian://new?vault=My%20Vault&name=Meeting%20Notes
```

### Use Cases

- **Deep links from other apps** — Create a link in Notion, Todoist, or email that opens a specific Obsidian note
- **Automation triggers** — Use Zapier or IFTTT to create Obsidian notes from external events
- **iOS Shortcuts** — Build automation on iPhone that creates or opens Obsidian notes
- **Alfred workflows** — Create custom Alfred searches that open Obsidian files
- **Browser bookmarklets** — Save a web page URL as a new Obsidian note with a click

**Example browser bookmarklet:**
```javascript
javascript:location.href='obsidian://new?vault=MyVault&name='+document.title+'&content=Source%3A%20'+window.location.href;
```

## Obsidian CLI

The **Obsidian CLI** is a command-line tool for interacting with Obsidian vaults programmatically.

### What It Can Do

- Create, read, update, delete notes from the command line
- Run searches across vaults
- List vault contents and file metadata
- Integrate Obsidian with shell scripts and automation tools

### Basic Commands

```bash
# Install (requires Node.js)
npm install -g @obsidian/cli

# Create a new note
obsidian create "vault-name" "Note Title" "note content"

# Read a note
obsidian read "vault-name" "Path/To/Note"

# List vault contents
obsidian list "vault-name" --folder "Folder/Path"

# Search vault
obsidian search "vault-name" "searchterm"

# Delete a note
obsidian delete "vault-name" "Path/To/Note"
```

### Integration with External Tools

- **Bash scripts** — Automate vault operations in shell scripts
- **cron jobs** — Schedule periodic note creation or archival
- **Git hooks** — Trigger Obsidian actions on code commits
- **CI/CD pipelines** — Create release notes or build documentation automatically
- **Python scripts** — Call Obsidian CLI from Python automation

**Example: Bash script that creates daily notes**
```bash
#!/bin/bash
DATE=$(date +%Y-%m-%d)
obsidian create "MyVault" "Daily/$DATE" "## $DATE
- [ ] Task 1
- [ ] Task 2"
```

## Obsidian Headless

**Obsidian Headless** is a server-side version of Obsidian that runs without a GUI, enabling vault operations from the command line or over HTTP.

### What It Does

- Syncs vaults from the server without running the Obsidian desktop app
- Reads, writes, and searches vault files programmatically
- Integrates with CI/CD, server-side automation, and scheduled tasks

### Use Cases

- **Automated backup** — Sync vault from server on a schedule
- **Server-side sync** — Keep vaults synchronized across multiple servers
- **CI/CD pipelines** — Generate documentation or release notes automatically
- **Scheduled exports** — Export vault to PDF or HTML on a schedule
- **Webhook integrations** — Receive data from external services and create notes

### Installation and Setup

```bash
# Install Headless CLI
npm install -g @obsidian/headless-cli

# Initialize a headless vault
obsidian-headless init /path/to/vault

# Run headless server
obsidian-headless serve /path/to/vault --port 3000
```

### HTTP API Example

```bash
# Create a note via HTTP
curl -X POST http://localhost:3000/notes \
  -H "Content-Type: application/json" \
  -d '{"path":"My Note","content":"Hello world"}'

# Read a note
curl http://localhost:3000/notes/My%20Note

# Search
curl http://localhost:3000/search?q=budget
```

### Integration Pattern

Use Headless Obsidian in combination with scheduled tasks (cron, systemd timer) to:
1. Pull data from external APIs
2. Process and transform data
3. Write results to vault as new notes
4. Version control vault files in Git

This enables **data pipeline automation** where Obsidian becomes the storage and UI layer for processed information.
