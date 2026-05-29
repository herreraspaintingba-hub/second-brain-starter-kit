# Essential Community Plugins Deep Dive

## Dataview (Third-Party Community Plugin)

Dataview is a query engine that turns your vault into a database. It lets you search, filter, sort, and aggregate data from your notes using a SQL-like query language.

### Query Types

**TABLE** — Tabular output with columns
```dataview
TABLE status, priority, due
FROM #project
WHERE status != "done"
SORT due ASC
```
Output: Table with file names and specified properties as columns.

**LIST** — Simple list of links
```dataview
LIST
FROM "Projects"
WHERE status = "active"
SORT file.name
```
Output: Bulleted list of matching file links.

**TASK** — Aggregated tasks from across the vault
```dataview
TASK
WHERE !completed
SORT due ASC
```
Output: Checklist items extracted from all notes, sortable and filterable.

**CALENDAR** — Calendar visualization by date
```dataview
CALENDAR file.day
FROM ""
WHERE file.day
```
Output: Calendar grid showing which days have notes/events. Click day to see notes created that day.

### FROM Clause — Data Sources

Specify where Dataview should query:

```dataview
FROM #project           /* Notes with tag #project */
FROM "Folder/Path"      /* All notes in a folder */
FROM [[MOC]]            /* Notes linked to MOC page */
FROM #tag and #subtag   /* Multiple tags (AND logic) */
FROM #tag or #subtag    /* Multiple tags (OR logic) */
```

### WHERE Clause — Filtering

Filter results by property or field values:

```dataview
WHERE status != "done"
WHERE priority = "high"
WHERE due >= date(today) and due <= date(tomorrow)
WHERE !completed           /* NOT completed */
WHERE type = "book"
WHERE contains(tags, "urgent")
WHERE length(aliases) > 0
```

### SORT Clause — Ordering

Sort results by one or more fields:

```dataview
SORT due ASC              /* Earliest due date first */
SORT file.mtime DESC      /* Newest modified first */
SORT priority DESC, due ASC  /* Priority first, then due date */
SORT file.name            /* Alphabetical by file name */
SORT file.size DESC       /* Largest files first */
```

### GROUP BY Clause — Grouping

Group results by a field:

```dataview
GROUP BY status           /* One group per unique status value */
GROUP BY file.folder      /* One group per folder */
GROUP BY file.day         /* One group per day */
GROUP BY priority         /* One group per priority level */
```

### LIMIT Clause — Cap Results

Limit how many results are returned:

```dataview
LIMIT 10                  /* Return first 10 results */
LIMIT 5                   /* Return first 5 results */
```

### FLATTEN Clause — Expand Lists

Expand multi-value fields into separate rows:

```dataview
FLATTEN tags              /* Each tag becomes a separate row */
FLATTEN assignees         /* Each assignee becomes a separate row */
```

### Implicit Fields — Built-in Properties

Dataview provides fields automatically available on every note:

| Field | Type | Example |
|---|---|---|
| `file.name` | string | `"My Note"` |
| `file.path` | string | `"Projects/Q1/My Note"` |
| `file.folder` | string | `"Projects/Q1"` |
| `file.ext` | string | `"md"` |
| `file.ctime` | date | Note creation date |
| `file.mtime` | date | Note last modified date |
| `file.size` | number | File size in bytes |
| `file.day` | date | Date parsed from YYYY-MM-DD in filename |
| `file.tags` | array | All tags in note (includes subtags) |
| `file.etags` | array | Only explicit tags (not subtags) |
| `file.inlinks` | array | Links pointing to this note |
| `file.outlinks` | array | Links this note points to |
| `file.aliases` | array | Note aliases |
| `file.tasks` | array | All tasks in note |

### Date Functions

Work with dates in queries:

```dataview
date(today)               /* Current date */
date(tomorrow)            /* Tomorrow's date */
date(yesterday)           /* Yesterday's date */
dur(7 days)               /* Duration: 7 days */
dur(1 month)              /* Duration: 1 month */
dur(2 weeks)              /* Duration: 2 weeks */

/* Example usage */
WHERE due >= date(today)
WHERE due <= date(today) + dur(7 days)
```

### Inline Queries

Display values inline in note text using backticks:

```dataview
`` `= this.status` ``     /* Display this note's status value */
`` `= date(today)` ``     /* Display today's date */
`` `= this.priority` ``   /* Display this note's priority */
```

### Complete Dataview Examples

**1. Project Tracker with Status, Priority, Due Date**
```dataview
TABLE status, priority, due
FROM "Projects"
WHERE status != "done"
SORT priority DESC, due ASC
LIMIT 20
```

**2. All Tasks Due This Week**
```dataview
TASK
WHERE !completed
WHERE due >= date(today) and due <= date(today) + dur(7 days)
SORT due ASC
GROUP BY file.folder
```

**3. Recently Modified Notes (Last 7 Days)**
```dataview
LIST file.mtime
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
```

**4. Reading Log by Month**
```dataview
TABLE author, rating, date_finished
FROM #book
WHERE date_finished
SORT date_finished DESC
GROUP BY dateformat(date_finished, "yyyy-MM")
```

**5. Unfinished Tasks Grouped by Project**
```dataview
TASK
WHERE !completed
GROUP BY file.folder
```

---

## Templater (Third-Party Community Plugin)

Templater turns note templates into dynamic generators. It executes JavaScript functions to insert dates, user input, file metadata, and custom logic into new notes.

### Syntax Overview

| Delimiter | Purpose | Example |
|---|---|---|
| `<% %>` | Execution block — runs code | `<% tp.date.now("YYYY-MM-DD") %>` |
| `<%* %>` | Execution block with whitespace control | `<%* let x = 5 %>` |
| `<%= %>` | Output block (rarely needed, `<% %>` usually suffices) | `<%= myVariable %>` |
| `<%- %>` | Output with dash for whitespace trimming | `<%-  result %>` |

### Key Functions

#### Date Functions

```javascript
tp.date.now("YYYY-MM-DD")          /* Today's date */
tp.date.now("dddd, MMMM D")        /* "Monday, March 3" */
tp.date.now("HH:mm A")             /* "02:30 PM" */
tp.date.now("YYYY-MM-DD", -1)      /* Yesterday's date (offset -1) */
tp.date.now("YYYY-MM-DD", 7)       /* Date 7 days from now */
tp.date.now("YYYY-MM-DD", -30)     /* Date 30 days ago */
```

#### File Functions

```javascript
tp.file.title                      /* Current note's title */
tp.file.creation_date("YYYY-MM-DD") /* When note was created */
tp.file.cursor()                   /* Place cursor here after template applies */
tp.file.rename("New Name")         /* Rename the note */
tp.file.move("/New/Path/{{title}}") /* Move to new folder */
```

#### User Input Functions

```javascript
tp.system.prompt("Enter project name:")
  /* Ask user to type input */

tp.system.suggester(["Option 1", "Option 2", "Option 3"],
                    ["value1", "value2", "value3"])
  /* Show dropdown menu, return selected value */
```

#### Web Functions

```javascript
tp.web.daily_quote()               /* Get a random daily quote */
```

### User Functions

Define custom JavaScript functions in a designated folder, then call them in templates:

1. **Settings → Templater → Script files folder** — Set path to folder containing custom functions
2. Create files like `my-function.js` containing:
   ```javascript
   module.exports = async (tp) => {
     return "Custom output: " + tp.file.title;
   }
   ```
3. In template, call: `<% tp.user.myFunction() %>`

### Startup Templates

Templater can run a template automatically when Obsidian starts:
1. **Settings → Templater → Startup templates** — List templates to run on startup
2. Use case: Create a daily note, open a dashboard, generate a work log

### Complete Templater Examples

**1. Daily Note Template**
```
# <% tp.date.now("dddd, MMMM D, YYYY") %>

## Today's Tasks
- [ ]

## Log
<% tp.file.cursor() %>

## Gratitude
-

---
Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
```

**2. Meeting Notes Template**
```
# Meeting: <% tp.system.prompt("Meeting title?") %>
**Date:** <% tp.date.now("YYYY-MM-DD") %>
**Attendees:** <% tp.system.prompt("Who attended?") %>

## Agenda
-

## Notes
<% tp.file.cursor() %>

## Action Items
- [ ]

## Next Steps
-
```

**3. Book Notes Template**
```
# <% tp.file.title %>

**Author:** <% tp.system.prompt("Author name?") %>
**Genre:** <% tp.system.prompt("Genre?") %>
**Rating:** <% tp.system.suggester(["⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐", "⭐⭐", "⭐"], [5, 4, 3, 2, 1]) %>

## Summary
<% tp.file.cursor() %>

## Key Quotes
-

## What I Learned
-

---
Started: <% tp.date.now("YYYY-MM-DD") %>
```

**4. Weekly Review Template (with Dataview)**
```
# Weekly Review — <% tp.date.now("YYYY-MM-DD") %>

## This Week's Wins
-

## Completed Tasks
\`\`\`dataview
TASK
WHERE completed
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
\`\`\`

## Unfinished Tasks
\`\`\`dataview
TASK
WHERE !completed
SORT due ASC
\`\`\`

## Next Week's Goals
- [ ] <% tp.file.cursor() %>
- [ ]

---
Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
```

**5. Project Kickoff Template**
```
# Project: <% tp.system.prompt("Project name?") %>

**Status:** Active
**Start Date:** <% tp.date.now("YYYY-MM-DD") %>
**Owner:** <% tp.system.prompt("Project owner?") %>

## Objective
<% tp.file.cursor() %>

## Deliverables
- [ ]
- [ ]

## Timeline
| Phase | Start | End | Owner |
|---|---|---|---|
| Planning | | | |
| Execution | | | |
| Launch | | | |

## Success Metrics
-

## Team
-

## Related Notes
- [[]]
```

---

## Tasks Plugin (Third-Party Community Plugin)

Tasks plugin adds rich task management to Obsidian. It extends Markdown checkboxes with dates, priorities, recurrence, and query syntax.

### Task Syntax

Standard task format with optional emojis for metadata:

```markdown
- [ ] Buy groceries 📅 2025-03-15 ⏳ 2025-03-10 🛫 2025-03-01 🔁 every week ⏫
```

Each emoji adds a layer of meaning to the task.

### Date Emojis

| Emoji | Name | Meaning | Format | Example |
|---|---|---|---|---|
| 📅 | Due | Task due date | `📅 YYYY-MM-DD` | `📅 2025-03-15` |
| ⏳ | Scheduled | Day to work on task | `⏳ YYYY-MM-DD` | `⏳ 2025-03-10` |
| 🛫 | Start | Day task becomes available | `🛫 YYYY-MM-DD` | `🛫 2025-03-01` |
| ✅ | Done | Task completion date | Auto-added on ✓ | `✅ 2025-03-15` |
| ➕ | Created | Task creation date | `➕ YYYY-MM-DD` | `➕ 2025-02-15` |

### Priority Emojis

| Emoji | Name | Priority |
|---|---|---|
| 🔺 | Highest | Highest (5) |
| ⏫ | High | High (4) |
| 🔼 | Medium | Medium (3) |
| (none) | Normal | Normal (2) |
| 🔽 | Low | Low (1) |
| ⏬ | Lowest | Lowest (0) |

### Recurrence Syntax

Add repeating tasks with `🔁` emoji:

```markdown
- [ ] Daily standup 🔁 every day
- [ ] Weekly review 🔁 every week
- [ ] Bi-weekly check-in 🔁 every 2 weeks
- [ ] Monthly budget 🔁 every month
- [ ] Weekday meetings 🔁 every weekday
- [ ] Quarterly planning 🔁 every 3 months
```

When you mark a recurring task done, a new instance automatically appears on the next recurrence date.

### Query Blocks

Create filtered task lists using query blocks:

````markdown
```tasks
not done
due before tomorrow
sort by priority
group by due
```
````

Place anywhere in your vault — the block displays matching tasks.

### Query Filters

**Completion Status**
```
done                /* Only completed tasks */
not done            /* Only incomplete tasks */
```

**Date Filters**
```
due before 2025-03-15
due after 2025-03-01
due on 2025-03-15
due today
due this week
due this month
scheduled before tomorrow
scheduled on today
happens before 2025-04-01     /* Checks all date types */
```

**Priority Filters**
```
priority is high
priority is medium
priority is low
priority above medium          /* High and Highest */
priority below medium          /* Low and Lowest */
```

**Path and Tag Filters**
```
path includes Projects         /* Notes in Projects folder */
path includes "2025/Q1"
tags include work
tags include #urgent
```

**Description Filters**
```
description includes budget
description includes review
```

### Complete Task Query Examples

**1. All Overdue Tasks**
```tasks
not done
due before today
sort by due
```

**2. Tasks Due This Week (Grouped by Project)**
```tasks
not done
due before 2025-03-22
due on or after 2025-03-15
group by path
sort by priority desc, due asc
```

**3. High Priority Incomplete Tasks**
```tasks
not done
priority is high
sort by due asc
```

**4. Tasks With No Due Date**
```tasks
not done
no due date
sort by created asc
```

**5. Tasks by Status and Priority (Combined)**
```tasks
not done
(priority is high OR priority is highest)
(path includes Projects OR tags include work)
sort by priority desc
group by path
```
