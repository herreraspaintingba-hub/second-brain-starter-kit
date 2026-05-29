# Obsidian Publish Complete Reference

## Setup

### Connecting a Vault to Publish

1. In Obsidian: Settings → About → **Publish** button
2. Choose vault to publish (or create new site)
3. Log in with Obsidian account (create account if needed)
4. Select which notes to publish (see "Choosing notes" below)
5. Obsidian Publish site URL auto-generates: `yourname.obsidian.md`

### Choosing Notes to Publish vs. Keep Private

By default, **all notes are private**. To publish a note:

1. Open note in editor
2. Click **Publish** button (top-right when Publish enabled)
3. Choose "Publish note" or "Publish as new"
4. Select related notes to publish together (linked notes)
5. Configure options (see below)
6. Click **Publish**

To **unpublish** a note:
- Open published note
- Click **Publish** → **Unpublish**
- Choose to keep or delete note from site

**Note:** Unpublishing keeps local copy; only removes from public site.

---

## Managing Sites

### Multiple Publish Sites

You can create **multiple Publish sites** from the same vault or different vaults.

**To create a new site:**
1. Settings → About → Publish
2. Click **Manage sites**
3. Select "+ New site"
4. Configure name, URL path, vault
5. Start publishing notes to new site independently

**To switch between sites:**
- When publishing a note, dropdown shows available sites
- Each site has separate published notes and settings
- Same note can be published to multiple sites with different configurations

**Use case:** One site for public blog, another for team documentation, another for portfolio.

### Site Settings

**Access from:** Your Publish site → Settings icon (top-right) → Site settings

**Available settings:**

| Setting | Options | Purpose |
|---------|---------|---------|
| **Site name** | Text | Appears in header and browser title |
| **Site description** | Text | Meta description for SEO |
| **Logo** | Image upload | Displays in header (recommended 200x100px) |
| **Favicon** | Image upload | Browser tab icon (.ico, .png; 32x32px) |
| **Custom domain** | Domain URL | See "Custom Domains" section below |
| **CSS snippets** | Enable/disable | Toggle custom styling (see below) |
| **Analytics** | Google/Plausible | Set analytics provider |
| **Navigation** | Dropdown control | Choose how navigation displays |

---

## Customization

### Custom CSS (`publish.css`)

To style your published site:

1. In vault folder: Create `publish.css` file (in root)
2. Populate with custom CSS rules
3. Settings → Publish → CSS snippets → Enable
4. Obsidian auto-detects and applies `publish.css` on publish
5. Changes live on next publish action

**Note:** Only `publish.css` is published; other CSS files ignored.

**Common customizations:**

```css
/* Hide nav sidebar */
.nav { display: none; }

/* Change primary color */
:root { --color-primary: #4a90e2; }

/* Custom fonts */
body { font-family: "Georgia", serif; }

/* Adjust sidebar width */
.sidebar { width: 250px; }

/* Hide metadata/frontmatter display */
.metadata { display: none; }

/* Custom heading styles */
h1 { font-size: 2.5em; color: #333; }
```

**Pro tip:** Use CSS variables for consistency. Obsidian Publish exposes:
- `--color-primary`, `--color-secondary`
- `--background-primary`, `--background-secondary`
- `--text-normal`, `--text-faint`

### Navigation Configuration

**Options:**

1. **Default hierarchy** — Uses folder structure and backlinks
2. **Custom navigation** — Create `_nav.md` file to manually order notes
3. **No navigation** — Hide sidebar completely

**To create custom navigation (_nav.md):**

Create file named `_nav.md` in vault root:

```markdown
# Site Title

- [Home](index.md)
- [About](about.md)
- Projects
  - [Project 1](projects/project-1.md)
  - [Project 2](projects/project-2.md)
- [Blog](blog/index.md)
- [Contact](contact.md)
```

Use relative paths and markdown syntax. Obsidian parses and renders as sidebar navigation.

### Logo and Favicon

**Logo:**
- Upload via Site settings → Logo
- Displays in header (left side)
- Recommended dimensions: 200x100px (or similar width:height ratio)
- Formats: PNG, SVG, JPG
- Auto-links to home page on click

**Favicon:**
- Upload via Site settings → Favicon
- Appears in browser tab and bookmarks
- Recommended: 32x32px, square format
- Formats: `.ico`, `.png`, `.svg`
- Name your file `favicon.ico` in vault root to auto-use

---

## Publishing Content

### Publishing/Unpublishing Notes

**Publish a note:**
1. Open note in editor
2. Click **Publish** button (top-right)
3. Select site if multiple available
4. Dialog shows: note title, related notes (linked)
5. Choose related notes to publish together
6. Click **Publish**

**Unpublish a note:**
1. Open published note
2. Click **Publish** → **Unpublish**
3. Choose: "Unlink" (keep local, remove from site) or "Delete" (delete everywhere)

**Update published note:**
- Edit locally
- Click **Publish** → **Update**
- Changes live immediately

### Bulk Publish

To publish multiple notes at once:

1. Select multiple notes in file explorer (Cmd/Ctrl + click)
2. Right-click → **Publish notes**
3. Select site and options
4. Confirm

Or publish with related notes:

1. Publish one note
2. Dialog suggests linked notes
3. Check boxes for notes to include
4. Publish all together

### Navigation Control

**In published site:**
- Sidebar shows navigation based on folder structure or `_nav.md`
- Click note titles to navigate
- Backlinks section shows related notes

**To control sidebar visibility:**
- Use custom CSS: `.nav { display: none; }`
- Or disable navigation entirely in Site settings

**To reorder notes in sidebar:**
- Edit `_nav.md` manually
- Obsidian Publish re-renders on next publish

---

## Collaboration

### Adding Collaborators

**To invite collaborators:**

1. Published site → Settings → **Collaborators** tab
2. Click **Add collaborator**
3. Enter Obsidian username or email
4. Choose permission level:
   - **Editor** — can publish, unpublish, and modify settings
   - **Viewer** — can view published content only
5. Send invite link

**For collaborators to accept:**
1. Accept invite from email/link
2. Grant Obsidian app permission to manage site
3. Can now edit and publish notes to shared site

**Notes:**
- Collaborators see shared vault in Obsidian
- Syncing via Obsidian Sync (separate from Publish)
- Publish actions are collaborative but asynchronous

---

## Social Media Previews

### Open Graph: `description` and `image` in Frontmatter

When a note is shared on social media (Twitter, LinkedIn, Slack, etc.), the link preview is generated from **Open Graph metadata**.

**Default behavior:**
- Title: Note heading (first `#`)
- Description: First 150 characters of body text
- Image: First image in note

**To customize:**

Add to frontmatter at top of note:

```yaml
---
description: "A custom description that appears in link previews (max 160 chars)"
image: "https://example.com/custom-image.jpg"
---
```

**Example:**

```yaml
---
title: "Building a Knowledge Management System"
description: "How to structure notes for long-term retrieval and connection discovery."
image: "https://mysite.obsidian.md/images/km-header.png"
---

# Building a Knowledge Management System

Your note content here...
```

**Best practices:**
- `description`: 120-160 characters, actionable insight, no markdown
- `image`: Direct URL (external or published image from your site), 1200x630px ideal
- Keep description concise — most platforms truncate at 160 chars
- Test on [ogp.me](https://ogp.me) or [Social Media Preview](https://www.socialmediatoday.com/tools/open-graph-preview-tool/)

### Social Card Behavior

When link is shared:
1. Platform reads Open Graph meta tags from published note
2. Displays title, description, image preview
3. Clicking preview navigates to your site

**If no image specified:**
- Platform uses site's favicon or default image
- Falls back to first image in note body

**To verify OG tags on published note:**
1. Publish note
2. Share link on social platform
3. If preview doesn't appear, check:
   - Image URL is accessible
   - Frontmatter YAML syntax is correct
   - No special characters in description

---

## Media Files

### Images, Audio, Video Handling

**Supported formats:**

| Type | Formats | Max Size |
|------|---------|----------|
| Images | PNG, JPG, GIF, SVG, WebP | 20MB per file |
| Audio | MP3, WAV, OGG, M4A | 50MB per file |
| Video | MP4, WebM, OGG (video) | 100MB per file |
| Files | PDF, all others | 100MB per file |

**In notes, embed media:**

```markdown
![[image.jpg]]        // Image
![[audio.mp3]]        // Audio player
![[video.mp4]]        // Video player
![[document.pdf]]     // PDF viewer
```

**Image considerations:**
- Dimensions: Responsive (scales to content width)
- Alt text: Use `![[image.jpg|alt text]]` syntax
- Compression: Obsidian auto-optimizes on publish

**Video embedding:**
- Obsidian Publish supports local video files
- Use `![[video.mp4]]` syntax
- First frame shown as preview
- Click to play in-page

**Audio:**
- Plays inline with standard HTML5 player
- Supports seeking, playback speed control (browser dependent)

### File Size Limits

**Per-file limits:**
- Images: 20MB
- Audio: 50MB
- Video: 100MB
- Documents: 100MB
- Vault total: 10GB (Publish Pro plan)

**To optimize:**
1. Compress images: Use Obsidian's `Image Auto Export` plugin or external tool
2. Use WebP format for newer browsers (smaller file size than PNG/JPG)
3. For video, consider hosting externally (YouTube, Vimeo) and embed links instead
4. Archive old media in separate vault if size is concern

---

## Analytics

### Google Analytics Setup

1. Create/obtain Google Analytics 4 (GA4) property ID (format: `G-XXXXXXXXXX`)
2. Your Publish site → Settings → Analytics
3. Choose **Google Analytics**
4. Paste GA4 measurement ID
5. Save

Obsidian auto-injects Google tag (`gtag.js`) on all pages.

**To view analytics:**
1. Log into Google Analytics Dashboard
2. Select your property
3. View: Realtime, Sessions, Pageviews, etc.

**Note:** Ensure GA tracking complies with privacy regulations (GDPR, CCPA, etc.). Consider adding privacy notice.

### Plausible Analytics Setup

1. Create Plausible account and add site
2. Get Plausible domain name (e.g., `yoursite.obsidian.md`)
3. Your Publish site → Settings → Analytics
4. Choose **Plausible**
5. Enter your domain
6. Save

Obsidian auto-injects Plausible tracking script.

**To view analytics:**
1. Log into Plausible Dashboard
2. View: Realtime visitors, top pages, sources, etc.

**Advantage over GA:** Privacy-focused, no GDPR consent required, simpler dashboard.

---

## Custom Domains

### Setting Custom Domain

1. Publish site → Settings → **Custom domain**
2. Enter your domain (e.g., `notes.example.com` or `example.com`)
3. Obsidian provides DNS configuration instructions

**Note:** You must own the domain; custom domain is a Publish Pro feature.

### DNS Configuration

**Two methods:**

#### Method 1: CNAME (Recommended)

1. Access your domain registrar's DNS settings (GoDaddy, Cloudflare, etc.)
2. Create CNAME record:
   - **Name:** `notes` (or `@` for root domain)
   - **Type:** CNAME
   - **Value:** `yourusername.obsidian.md`
   - **TTL:** 3600 (or default)
3. Save changes
4. Wait 15-60 minutes for DNS propagation
5. Verify in Obsidian: Settings → Custom domain → **Verify domain**

#### Method 2: A Record (If CNAME not available)

1. In domain registrar, create A record:
   - **Name:** `notes` or `@`
   - **Type:** A
   - **Value:** `35.201.73.77` (Obsidian's IP; check docs for current)
   - **TTL:** 3600
2. Save and wait for propagation
3. Verify in Obsidian

**After verification:**
- Your site accessible at custom domain
- Original `yourusername.obsidian.md` still works
- Both URLs point to same published site

---

## Permalinks

### `permalink` Frontmatter Property

By default, published notes use the note title in URL. To customize:

Add to note frontmatter:

```yaml
---
permalink: "/custom-url-slug"
---
```

**Example:**

```yaml
---
title: "Building a Knowledge Base"
permalink: "/knowledge-base"
---
```

Results in URL: `yoursite.obsidian.md/knowledge-base` instead of `/building-a-knowledge-base`

**Best practices:**
- Use lowercase, hyphens for spaces
- Keep slugs short and descriptive
- Use consistent slug structure (e.g., all blog posts: `/blog/post-slug`)
- If changing permalink later, old URL breaks (set up 301 redirects if critical)

**Note:** Nested paths work: `permalink: "/guides/obsidian/tips"`

---

## SEO

### Complete Frontmatter Example for Well-Optimized Published Note

```yaml
---
title: "How to Build a Second Brain with Obsidian"
description: "Learn the fundamentals of personal knowledge management, note-taking systems, and connecting ideas for long-term learning."
tags: [obsidian, pkm, knowledge-management, learning]
permalink: "/second-brain-obsidian"
image: "https://mysite.obsidian.md/images/second-brain-og.png"
date: 2024-01-15
author: "Your Name"
canonical: "https://mysite.obsidian.md/second-brain-obsidian"
---

# How to Build a Second Brain with Obsidian

Your note content starting with a strong opening paragraph that expands on the title...
```

### `description` — SEO Optimization

- **Length:** 150-160 characters (Google truncates beyond ~160)
- **Content:** Answer the "what is this note about" question
- **Best practice:** Include primary keyword naturally
- **Example:** "Learn fundamentals of note-taking, organization, and connection discovery in Obsidian to build a scalable personal knowledge system."

### `title` Property

- Use in frontmatter to lock title (prevents Obsidian using filename)
- Appears in browser tab, social previews, and page header
- **Length:** 50-60 characters for optimal SERP display
- **Keyword:** Lead with primary keyword if possible

### Canonical URLs

Add if you've published the note elsewhere:

```yaml
canonical: "https://youroriginalsite.com/article"
```

Tells search engines: "This version is OK, but the canonical is here." Prevents duplicate content penalties.

**Use case:** Publishing same article on Medium and your Obsidian site.

### Complete SEO Checklist for Published Notes

- [ ] Unique, descriptive `title` (50-60 chars)
- [ ] Clear `description` (150-160 chars, includes keyword)
- [ ] `permalink` slug optimized (readable, keyword-relevant)
- [ ] `image` with Open Graph metadata (1200x630px)
- [ ] First heading (`#`) matches or expands on title
- [ ] First 100 words answer reader intent
- [ ] Internal links: 3-5 `[[wikilinks]]` to related notes
- [ ] Images with alt text: `![[image.jpg|descriptive alt text]]`
- [ ] No keyword stuffing; natural language
- [ ] Mobile responsive (tested in browser)
- [ ] Page load speed (optimize images, enable caching)
- [ ] `canonical` URL if cross-published

---

## Security & Privacy

### Password Protection

To password-protect a published site:

1. Site settings → **Password protection**
2. Enable and enter password
3. Share password with intended readers separately
4. Visitors prompted for password before accessing

**Limitations:**
- Password visible in browser console (not true encryption)
- Protects against casual browsing, not determined actors
- All published notes protected together (can't set per-note)

**Better alternative:** Use Obsidian Sync + Obsidian app for truly private content. Publish only for intended public notes.

### Private Notes

**By default, all notes are private** until explicitly published.

To keep notes private:
- Don't click **Publish** button
- Or unpublish notes (removes from public site)
- Note remains in local vault

**Note:** If you've shared a note URL publicly, the note is discoverable. Unpublishing removes it from your site.

**For truly confidential content:**
- Keep in local vault (never publish)
- Use Obsidian Sync with encryption key
- Consider end-to-end encrypted tools (Signal, ProtonMail) for sensitive sharing

---

## Limitations

### Supported File Types

**Fully supported:**
- Markdown (`.md`)
- Images (PNG, JPG, GIF, SVG, WebP)
- Audio (MP3, WAV, OGG, M4A)
- Video (MP4, WebM, OGG)
- PDFs (embedded viewer)

**Limited support:**
- External embeds (YouTube, Vimeo) → links only
- Inline HTML → stripped for security
- Dataview queries → not executed (display as code)
- Database records → flattened to markdown

**Not supported:**
- Plugins (logic stripped, styling preserved)
- Obsidian-specific syntax (e.g., `!=this.file.name`)
- Real-time sync to public site (manual publish required)

### Size Limits

| Constraint | Limit | Plan |
|-----------|-------|------|
| Per file | 20MB (images), 100MB (video/other) | All |
| Vault total | 10GB | Pro |
| Vault total | 1GB | Free |
| Collaborators | 5 | Pro |

### Plugin Support

**Plugins that work in Publish:**
- Styling/theme plugins (CSS applied)
- Basic formatting (dataview display, but not execution)

**Plugins that don't work:**
- Dataview (queries not executed; code shown)
- Database plugins
- API-based plugins (sync, CRM, etc.)
- Any plugin requiring Obsidian app logic

**Workaround:** Export dynamic content as static markdown before publishing.

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Image not showing | Check file is published, not just local vault. Verify path in note. |
| Link shows "404" | Ensure linked note is published. Wikilinks to unpublished notes break. |
| Custom CSS not applying | Verify file named `publish.css` in vault root. Re-publish after CSS update. |
| Password not working | Clear browser cache. Try incognito window. |
| Analytics not tracking | Check Analytics property ID correct. Wait 24 hours for data to appear. |
| Custom domain DNS failing | Check CNAME value in registrar. DNS changes can take up to 48 hours. Use DNS checker tool (e.g., `mxtoolbox.com`). |
| Performance slow | Compress images, reduce embed count, consider external hosting for heavy media. |

