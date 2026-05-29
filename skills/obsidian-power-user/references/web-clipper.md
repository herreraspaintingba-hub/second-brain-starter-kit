# Obsidian Web Clipper Complete Reference

## Installation

### Browser Extension Links

Download and install Obsidian Web Clipper for your browser:

**Chrome / Brave / Edge:**
- [Obsidian Web Clipper on Chrome Web Store](https://chrome.google.com/webstore/detail/obsidian-web-clipper/)
- Open link → Click **Add to Chrome** (or equivalent for your Chromium browser)

**Firefox:**
- [Obsidian Web Clipper on Firefox Add-ons](https://addons.mozilla.org/firefox/addon/obsidian-web-clipper/)
- Click **Add to Firefox**

**Safari:**
- [Obsidian Web Clipper on App Store](https://apps.apple.com/app/id1475833169)
- Click **Get** or **Install**

**After installation:**
1. Open Obsidian → Settings → Web Clipper
2. Generate access token
3. Log in to browser extension with Obsidian credentials
4. Choose default vault and folder for clipped content

---

## Clipping

### Full Page Clipping

1. Browse to any webpage
2. Click **Obsidian Web Clipper** extension icon (browser toolbar)
3. Choose "Clip entire page"
4. Confirm clipping options (see "Options" below)
5. Content saves to vault with clipping template

**Content captured:**
- Full HTML content (converted to markdown)
- All text, images, links
- Page title
- Source URL
- Clipping date/time

### Selection Clipping

1. On webpage, highlight/select text or content
2. Click **Obsidian Web Clipper** icon
3. Choose "Clip selection"
4. Only selected content saves (preserves surrounding context)

**Use case:** Quick clip of specific paragraph, quote, or data without full page clutter.

### Article Mode

1. Open article/blog post
2. Click **Obsidian Web Clipper** icon
3. Choose "Clip article" (or "Article mode" if available)
4. Clipper analyzes content and extracts main text only
5. Removes: navigation, ads, sidebars, distractions

**Smart content extraction:**
- Identifies and extracts article body
- Removes boilerplate (header, footer, nav)
- Preserves reading context and formatting
- Best for blog posts, news articles, Medium posts

### Where Clipped Content is Saved

**Default location:**
- Obsidian Clipper folder (set in Settings → Web Clipper)
- Default: `Clippings` folder in root of vault

**To customize save location:**
1. Settings → Web Clipper → **Default folder**
2. Choose or create target folder
3. All new clips save here by default

**To override for specific clip:**
1. When clipping appears, confirm dialog shows save location
2. Click folder icon to change destination
3. Select new folder
4. Confirm clip

---

## Highlighting

### Highlighting Before Clipping

1. On webpage, select text you want to highlight
2. Click **Obsidian Web Clipper** icon
3. Choose "Clip with highlights" or "Clip full page"
4. Highlights are captured in the clipped note

**How highlights appear in saved note:**
- Highlighted text preserved with special formatting
- Usually marked with `==highlight syntax==` or bold/emphasis
- Creates visual distinction in vault note

### How Highlights Appear in Saved Note

**Default format:**
```
This is ==highlighted text== from the original page.
```

Or (depending on template):
```
**This is highlighted text** from the original page.
```

**To change highlight formatting:**
1. Edit your clipping template (see "Templates" section)
2. Use template variables and filters to customize highlight display
3. Example: `<mark>{{content}}</mark>` wraps highlights in HTML `<mark>` tag

**Multiple highlights:**
- Each selection preserves highlights individually
- Useful for marking important passages in research articles

---

## AI Interpretation

### AI-Powered Extraction

Obsidian Web Clipper can use AI to automatically extract and summarize content:

**To enable AI interpretation:**
1. Settings → Web Clipper → **AI Extraction**
2. Enable toggle
3. Choose AI model (OpenAI, Claude, or Obsidian's built-in)
4. When clipping, choose "Clip with AI summary" or "AI interpretation"

**What AI does:**
- Extracts key points from article
- Generates summary (optional)
- Identifies main topics/tags
- Structures content for faster review
- Can auto-generate title

**Use cases:**
- Long research papers → quick summary
- News articles → extract facts and claims
- Product pages → extract specs, pricing, reviews
- Academic papers → abstract + key findings

**Note:** Requires API key/credits for external AI models. Obsidian's built-in extraction is limited but free.

---

## Templates

### Custom Clip Templates

Clipping templates control how content is saved to your vault. Customize to match your workflow.

**Access templates:**
1. Settings → Web Clipper → **Default template**
2. Or create `_templates/` folder in vault → Web Clipper auto-detects

**Template syntax:**
- Variables: `{{variable}}`
- Filters: `{{ variable | filter }}`
- Conditionals: `{% if condition %}...{% endif %}`
- Loops: `{% for item in list %}...{% endfor %}`

**Basic template example:**

```
---
url: {{url}}
date: {{date}}
source: {{domain}}
---

# {{title}}

> {{description}}

{{content}}

[[{{url}}]]
```

### Variables — Complete Reference

| Variable | Description | Example |
|---|---|---|
| `{{title}}` | Page title / first heading | "How to Build a Second Brain" |
| `{{url}}` | Full source URL | `https://example.com/article` |
| `{{date}}` | Clip date in format `YYYY-MM-DD HH:MM` | `2024-01-15 14:30` |
| `{{content}}` | Main page content (markdown) | Full article text |
| `{{author}}` | Author name (if detected) | "John Smith" |
| `{{description}}` | Meta description or subtitle | "A guide to personal knowledge management" |
| `{{image}}` | Open Graph image URL (largest image) | `https://example.com/og-image.png` |
| `{{published}}` | Publication date (if detected) | `2024-01-01` |
| `{{domain}}` | Domain name only | `example.com` |
| `{{hostname}}` | Hostname with subdomain | `blog.example.com` |
| `{{pathname}}` | URL path | `/article/knowledge-base` |
| `{{excerpt}}` | Page excerpt / first 200 chars | "A guide to personal knowledge..." |
| `{{favicon}}` | Favicon URL | `https://example.com/favicon.ico` |
| `{{byline}}` | Author + publication (if available) | "John Smith, Medium" |
| `{{quote}}` | Highlighted text (if any) | "Text you selected before clipping" |

---

## Filters

Filters transform variable output. Chain multiple filters with `|`.

### `replace` — Replace text pattern

```
{{title | replace("Old", "New")}}
```

**Example:**
```
{{title | replace("—", "-")}}  // Replace em-dash with hyphen
{{url | replace("https://", "")}}  // Remove protocol
```

### `trim` — Remove whitespace

```
{{content | trim}}
```

Removes leading/trailing spaces and newlines. Useful for cleaning up extracted content.

### `upper` — Convert to uppercase

```
{{title | upper}}
```

Output: "HOW TO BUILD A SECOND BRAIN"

### `lower` — Convert to lowercase

```
{{author | lower}}
```

Output: "john smith"

### `slice` — Extract substring

```
{{url | slice(0, 50)}}
```

Extracts first 50 characters of URL.

```
{{content | slice(0, 200)}}
```

First 200 characters of content (useful for excerpts).

### `date` — Format date

```
{{date | date("YYYY-MM-DD")}}
```

Available formats:
- `YYYY-MM-DD` — "2024-01-15"
- `MMM DD, YYYY` — "Jan 15, 2024"
- `DD/MM/YYYY` — "15/01/2024"
- `YYYY-MM-DD HH:MM:SS` — "2024-01-15 14:30:45"

**Example:**
```
Clipped on: {{date | date("MMMM DD, YYYY")}}
// Output: "Clipped on: January 15, 2024"
```

### Chaining Filters

Combine multiple filters:

```
{{title | lower | replace(" ", "-")}}
```

Output: "how-to-build-a-second-brain"

---

## Logic

### Conditionals: `if...endif`

Display content only if condition is true:

```
{% if author %}
**Author:** {{author}}
{% endif %}
```

Only shows author section if author data exists.

**Common conditions:**
- `{% if author %}` — Author exists
- `{% if description %}` — Description exists
- `{% if published %}` — Has publication date
- `{% if image %}` — Page has image

**Multiple conditions (AND):**
```
{% if author and published %}
By {{author}} on {{published | date("MMM DD, YYYY")}}
{% endif %}
```

**Multiple conditions (OR):**
```
{% if author or byline %}
Source: {{author | default(byline)}}
{% endif %}
```

### Loops: `for...endfor`

Iterate over lists:

```
{% for tag in tags %}
- {{tag}}
{% endfor %}
```

**Less common** in web clipper (limited list support), but useful if template processes array data.

### Fallbacks: `default`

Provide fallback value if variable is empty:

```
{{author | default("Unknown Author")}}
```

If no author detected, displays "Unknown Author".

**Chained example:**
```
{{byline | default(author | default("Anonymous"))}}
```

Use `byline`, or if empty use `author`, or if empty use "Anonymous".

---

## Complete Template Examples

### 1. Article Clipper with Full Metadata

Captures article with structured frontmatter for easy searching and linking:

```
---
title: {{title}}
url: {{url}}
date: {{date}}
published: {{published}}
author: {{author}}
domain: {{domain}}
tags: [article, research]
---

# {{title}}

**Source:** [{{domain}}]({{url}})
**Author:** {{author | default("Unknown")}}
**Published:** {{published | default("Unknown")}}

---

## Summary
{{description}}

---

## Content

{{content}}

---

## Metadata
- **Clipped:** {{date | date("MMMM DD, YYYY at HH:MM")}}
- **Domain:** {{domain}}
- **Read time estimate:** [Time article in browser]
```

**Use case:** Save research articles with all metadata for later citation or review.

### 2. Recipe Clipper

Extracts recipe title, ingredients, instructions with consistent formatting:

```
---
title: {{title}}
source: {{url}}
domain: {{domain}}
date: {{date}}
tags: [recipe, cooking]
---

# {{title}}

**Source:** [{{domain}}]({{url}})

---

## Ingredients

(Copy ingredient list from {{content}})

---

## Instructions

(Copy step-by-step instructions)

---

## Notes

{{description}}

---

**Clipped:** {{date | date("MMM DD, YYYY")}}
```

**Note:** Recipe clipper requires manual extraction of ingredients/instructions since `{{content}}` is full HTML. Consider using a dedicated recipe clipper extension for automation.

### 3. Research Paper Clipper

Structured template for academic papers or research articles:

```
---
title: {{title}}
authors: {{author}}
published: {{published}}
url: {{url}}
domain: {{domain}}
type: research
tags: [paper, research, reading]
---

# {{title}}

**Authors:** {{author}}
**Published:** {{published | date("YYYY-MM-DD")}}
**Source:** [{{domain}}]({{url}})

---

## Abstract / Summary

{{description}}

---

## Key Points

-
-
-

---

## Highlights

{{quote | default("(Add your own highlights)")}}

---

## Full Content

{{content}}

---

## Personal Notes

(Add your thoughts and connections)

---

## References

- Link 1
- Link 2

**Clipped:** {{date | date("MMM DD, YYYY")}}
```

**Use case:** Save research papers with structured sections for literature review and synthesis.

---

## Clipping Workflow Best Practices

1. **Choose the right clipping mode:**
   - Full page for general research
   - Article mode for blog posts and news
   - Selection for specific quotes or data

2. **Highlight important passages before clipping** to preserve context

3. **Use consistent template** for all clippings in same category (articles, recipes, research)

4. **Tag immediately** after clipping:
   - Add frontmatter tags: `tags: [source, topic, status]`
   - Use consistent tag naming: `#article`, `#recipe`, `#research`, etc.

5. **Review and process clippings regularly:**
   - Add personal notes and connections
   - Link to related notes with `[[wikilinks]]`
   - Delete or archive unused clippings

6. **Organize clippings folder:**
   - Create subfolders: `Clippings/Articles/`, `Clippings/Research/`, etc.
   - Or tag with `#to-process` and review periodically

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Content not saving | Check vault connection in Settings. Verify folder permissions. |
| Variables showing as blank | Variable may not exist for that page. Use `default` filter: `{{author \| default("Unknown")}}` |
| Template not applying | Ensure template is in correct folder (`_templates/`) or set as default in Settings. |
| Highlights not captured | Highlight before clipping, not after. Use "Clip with highlights" option. |
| Images not embedding | Check image URL is still valid. Obsidian may need to download locally (Settings → Web Clipper → Download images). |
| Date format wrong | Check `date` filter syntax matches format string (e.g., `YYYY`, `yyyy`, case-sensitive). |
| Special characters broken | Use URL encoding or `trim` filter. Check file encoding is UTF-8. |
| Performance slow | Disable AI extraction if enabled. Check vault sync isn't blocking saves. |

---

## Advanced: Creating Smart Clipping Workflows

**Example workflow for research:**

1. **Clip with article mode** for article content
2. **Template automatically adds:** frontmatter with source, date, domain
3. **Conditionals check:** if published date exists, format nicely; if author exists, show; etc.
4. **Post-clipping:** Add personal tags, link to related notes, extract key points

**Template with smart conditionals:**

```
---
title: {{title}}
source: {{url}}
type: {% if author and published %}academic{% elif author %}article{% else %}web{% endif %}
tags: [clipped, {{domain | lower}}]
published: {{published}}
---

# {{title}}

{% if author %}
**By:** {{author}}
{% endif %}

{% if published %}
**Published:** {{published | date("MMM DD, YYYY")}}
{% endif %}

---

{{description}}

---

{{content}}

---

**Source:** [{{domain}}]({{url}})
**Clipped:** {{date | date("YYYY-MM-DD HH:MM")}}
```

This template:
- Auto-sets `type` based on whether author/published data exists
- Shows author and date only if available
- Maintains consistent frontmatter structure
- Useful for automating metadata capture

