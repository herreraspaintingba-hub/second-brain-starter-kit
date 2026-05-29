# Obsidian Bases — Complete Reference

## What Obsidian Bases Is

**Obsidian Bases** is Obsidian's native database system, available as a core plugin. It transforms your vault into a queryable database without plugins like Dataview.

### Key Characteristics
- **File format:** `.base` files using YAML syntax
- **Purpose:** Create database-like views of your vault notes using frontmatter properties
- **Scope:** Filter, sort, group, and display notes across your entire vault
- **Native solution:** Built-in to Obsidian, no Dataview dependency required
- **Property-driven:** Queries notes based on YAML frontmatter properties

### How It Works
1. You enable Bases in Obsidian's core plugins
2. Create `.base` files in your vault (or use the UI to generate them)
3. Define filters, formulas, and views using YAML
4. Bases renders your notes in table, card, or list format
5. All changes are computed on-the-fly; no external database needed

---

## Views Available

Bases supports three view types to display your data:

| View Type | Description | Best For |
|---|---|---|
| `table` | Spreadsheet-style layout with columns, sorting, and filtering | Structured data, project lists, tracking tables |
| `cards` | Card or kanban-style layout, optionally grouped by a property | Progress boards, content curation, status tracking |
| `list` | Simple ordered list of notes with a few key properties visible | Quick browsing, minimal layout, reading lists |

---

## .base File Structure

A `.base` file is YAML that defines a complete database view. Here's the full structure with all possible fields:

```yaml
# Top-level filters applied to all views (optional)
filters:
  - condition: "filter expression here"

# Column/property display mappings (optional)
display:
  propertyName: "Display Label"
  anotherProperty: "Another Label"

# Formula definitions (optional)
formulas:
  formulaName: "formula expression"
  anotherFormula: "another formula expression"

# Array of view definitions
views:
  - type: "table" | "cards" | "list"
    name: "View Display Name"

    # View-level filters (optional, combined with top-level filters via AND)
    filters:
      - condition: "filter expression"

    # Grouping (cards and table only)
    groupBy: "propertyName"

    # Sorting
    order:
      - by: "propertyName"
        direction: "asc" | "desc"

    # Column configuration (table only)
    columns:
      - propertyName: "label"
        type: "string" | "number" | "date" | "boolean" | "tags" | "links"
        width: 200  # pixels
        hidden: false

    # Card display (cards only)
    cardLayout: "compact" | "full"  # determines card size

    # Display properties (list view)
    displayProperties:
      - propertyName

  # Multiple views can exist in one .base file
  - type: "list"
    name: "Another View"
    filters:
      - condition: "another filter"
```

### Field Explanations

| Field | Level | Required | Description |
|---|---|---|---|
| `filters` | Top-level or per-view | No | Array of filter conditions. Top-level filters apply to all views. View-level filters are AND'd with top-level filters. |
| `display` | Top-level | No | Object mapping property names to their display labels. Used across all views. |
| `formulas` | Top-level | No | Object defining computed properties. Referenced in filters, displays, and sorts. |
| `views` | Top-level | Yes | Array of at least one view definition. Each view renders the filtered data differently. |
| `type` | Per-view | Yes | `table`, `cards`, or `list`. Determines how notes are rendered. |
| `name` | Per-view | Yes | Human-readable name for the view, shown in the UI. |
| `groupBy` | Per-view | No | Property name to group by. Available for `table` and `cards`. Organizes results into collapsible groups. |
| `order` | Per-view | No | Array of sort definitions. Applied in order (first sort property, then second, etc.). |
| `columns` | Per-view (table) | No | Array defining visible columns and their configuration. Table view only. |
| `cardLayout` | Per-view (cards) | No | `compact` or `full`. Controls card size and visual density. Cards view only. |
| `displayProperties` | Per-view (list) | No | Array of property names to show in list items. List view only. |

---

## Filters — Complete Reference

Filters determine which notes appear in your base. All filter conditions are strings that Bases evaluates.

### Filter Logic Operators

Combine multiple conditions using logical operators:

```yaml
# AND operator: all conditions must be true
and:
  - file.inFolder("Projects")
  - status == "active"

# OR operator: at least one condition must be true
or:
  - taggedWith(file.file, "urgent")
  - priority > 3

# NOT operator: condition must be false
not:
  - file.ext == "pdf"

# Nested logic (AND inside OR, etc.)
or:
  - and:
    - status == "done"
    - file.ctime > date("2024-01-01")
  - priority > 5
```

### File Functions

Access metadata about the note file itself:

```yaml
# File location checks
file.inFolder("path/to/folder")           # True if file is in this folder
file.inFolder("path/to/folder", true)     # Include subfolders (recursive)

# File name and path
file.name == "My Note"                    # Exact name without extension
file.path == "folder/subfolder/My Note"   # Path from vault root
file.ext == "md"                          # File extension

# File timestamps
file.ctime > date("2024-01-01")           # Created after date
file.mtime < date("2024-12-31")           # Modified before date
file.ctime == now() - 7 * 86400           # Created in last 7 days (in seconds)

# File size
file.size > 10000                         # Greater than 10KB
```

### Tag & Link Functions

Filter based on tags and links in the note:

```yaml
# Tag matching
taggedWith(file.file, "project")          # Note has the #project tag
taggedWith(file.file, "#urgent")          # Tag with explicit #
not:
  - taggedWith(file.file, "archived")     # Note doesn't have #archived

# Link matching
linksTo(file.file, "Project ABC")         # Note links to "Project ABC"
linksTo(file.file, "Projects/Dashboard")  # Link to file path
not:
  - linksTo(file.file, "Completed")       # Note doesn't link to "Completed"

# Multiple tags (use AND/OR for logic)
and:
  - taggedWith(file.file, "project")
  - taggedWith(file.file, "client-work")
```

### Property Comparisons

Filter by note properties (defined in frontmatter):

```yaml
# String comparisons
status == "done"                  # Exact match
status != "active"                # Not equal
status == "in progress"           # Spaces are fine

# Number comparisons
priority > 2                      # Greater than
priority <= 5                     # Less than or equal
priority >= 1                     # Greater than or equal
hours < 8                         # Less than

# Boolean comparisons
published == true                 # Boolean property is true
archived == false                 # Boolean property is false

# List/array contains
contains(tags, "project")         # Array property contains value
contains(people, "Alice")         # List property contains name

# Null/empty checks
status == null                    # Property not set
status != null                    # Property is set

# String pattern matching
contains(title, "urgent")         # Title contains substring (case-sensitive)
startsWith(title, "Bug:")         # Title starts with
endsWith(tags, "done")            # Note: works on strings; use contains() for arrays
```

### Combined Filter Examples

```yaml
# Example 1: Active projects not yet started
and:
  - status == "active"
  - not:
    - status == "done"
  - startDate > now()

# Example 2: Archived notes in Blog folder
and:
  - file.inFolder("Blog")
  - taggedWith(file.file, "archived")

# Example 3: Recent urgent items with high priority
or:
  - and:
    - priority > 3
    - file.mtime > now() - 604800  # Last 7 days in seconds
  - taggedWith(file.file, "urgent")
```

---

## Formulas — Complete Reference

Formulas are computed properties that you can display, filter, or sort by. They are defined once and referenced throughout your base.

### Arithmetic Operations

```yaml
formulas:
  # Basic math
  totalCost: "quantity * price"
  remaining: "max - completed"
  percentage: "(completed / max) * 100"
```

### String Functions

```yaml
formulas:
  # Concatenation
  fullName: "concat(firstName, ' ', lastName)"
  taggedTitle: "concat('[', status, '] ', title)"

  # Case conversion
  lowerStatus: "lower(status)"
  upperTitle: "upper(title)"

  # Length
  titleLength: "length(title)"

  # Substring checks (returns boolean or index)
  hasUrgent: "contains(description, 'urgent')"
  startsWithBug: "startsWith(title, 'Bug:')"
  endsWithDone: "endsWith(notes, 'DONE')"

  # Substring extraction (if supported)
  substring: "substring(description, 0, 50)"
```

### Date Functions

```yaml
formulas:
  # Current date/time
  today: "now()"

  # Date formatting
  readableDate: "date(createdDate).format('YYYY-MM-DD')"
  fullDateTime: "date(dueDate).format('dddd, MMMM D, YYYY')"

  # Date arithmetic
  daysUntilDue: "(dueDate - now()) / 86400"  # In days (86400 seconds per day)
  ageInDays: "(now() - file.ctime) / 86400"
  isOverdue: "dueDate < now()"
  daysOverdue: "(now() - dueDate) / 86400"

  # Conditional on dates
  status: "if(dueDate < now(), 'OVERDUE', 'ON TIME')"
```

### Conditional Logic

```yaml
formulas:
  # Simple if-then-else
  priority: "if(urgency > 5, 'HIGH', 'NORMAL')"

  # Nested if
  label: "if(status == 'done', '✓ Done', if(status == 'in progress', '⏳ In Progress', '□ Backlog'))"

  # With boolean conditions
  isAtRisk: "if(and(status == 'in progress', daysUntilDue < 3), true, false)"
```

### List Functions

```yaml
formulas:
  # Array length
  tagCount: "length(tags)"
  assigneeCount: "length(assignees)"

  # Map: transform each element
  tagList: "list(tags).map(concat('#', item)).join(', ')"

  # Filter: select matching elements
  activeTasks: "list(tasks).filter(status == 'active').length"

  # Join: combine array into string
  allTags: "list(tags).join(', ')"
```

### Property Access in Formulas

```yaml
# Reference note properties (frontmatter)
formulas:
  displayTitle: "title"                    # Simple property name
  withPath: "concat(file.path, ' - ', status)"  # Mix file and note properties
  daysActive: "(now() - createdDate) / 86400"   # Date arithmetic

  # Reference other formulas
  statusIcon: "if(isComplete == true, '✓', '□')"  # isComplete is another formula
```

---

## Properties Access

### Note Properties (Frontmatter)

Access any property defined in a note's YAML frontmatter:

```yaml
# If your note has this frontmatter:
---
title: "My Project"
status: "in progress"
priority: 3
dueDate: 2024-06-30
assignees:
  - Alice
  - Bob
tags:
  - project
  - client-work
---

# In Bases filters and formulas, reference as:
status == "in progress"           # Direct property name
priority > 2                      # Works with numbers
contains(assignees, "Alice")      # Works with arrays
taggedWith(file.file, "project")  # Special function for tags
```

### File Properties

Access metadata about the note file itself:

| Property | Type | Description |
|---|---|---|
| `file.name` | string | Note filename without extension |
| `file.path` | string | Note path from vault root (e.g., `Folder/SubFolder/Note`) |
| `file.ext` | string | File extension (e.g., `md`) |
| `file.ctime` | date | Creation timestamp |
| `file.mtime` | date | Last modified timestamp |
| `file.size` | number | File size in bytes |

### Formula Properties

Any formula you define becomes a property you can use:

```yaml
formulas:
  daysUntilDue: "(dueDate - now()) / 86400"

# Then in your display, sort, or another formula:
order:
  - by: "daysUntilDue"
    direction: "asc"

display:
  daysUntilDue: "Days to Deadline"
```

---

## Complete Example .base Files

### Example 1: Project Tracker

A table view of all notes tagged `#project` that aren't marked done, showing status, priority, and due date. Includes a formula for days until due, sorted by due date ascending.

```yaml
filters:
  - and:
    - taggedWith(file.file, "project")
    - not:
      - status == "done"

display:
  status: "Status"
  priority: "Priority"
  dueDate: "Due Date"
  daysUntilDue: "Days Until Due"

formulas:
  daysUntilDue: "if(dueDate == null, 999, (dueDate - now()) / 86400)"

views:
  - type: "table"
    name: "Active Projects"
    order:
      - by: "dueDate"
        direction: "asc"
    columns:
      - propertyName: "title"
        type: "string"
        width: 300
      - propertyName: "status"
        type: "string"
        width: 120
      - propertyName: "priority"
        type: "number"
        width: 80
      - propertyName: "dueDate"
        type: "date"
        width: 120
      - propertyName: "daysUntilDue"
        type: "number"
        width: 100
```

### Example 2: Reading List

A base showing books in a `Books/` folder with author, rating, and read status. Includes both a table view and a card view grouped by status.

```yaml
filters:
  - file.inFolder("Books", true)

display:
  author: "Author"
  rating: "Rating (1-5)"
  status: "Read Status"
  dateRead: "Date Read"

views:
  - type: "table"
    name: "All Books"
    order:
      - by: "dateRead"
        direction: "desc"
    columns:
      - propertyName: "title"
        type: "string"
        width: 300
      - propertyName: "author"
        type: "string"
        width: 200
      - propertyName: "rating"
        type: "number"
        width: 80
      - propertyName: "status"
        type: "string"
        width: 120
      - propertyName: "dateRead"
        type: "date"
        width: 120

  - type: "cards"
    name: "Books by Status"
    groupBy: "status"
    cardLayout: "full"
    order:
      - by: "title"
        direction: "asc"
```

### Example 3: Meeting Notes Dashboard

A table view of meeting notes in a `Meetings/` folder, displaying date, attendees, and action item count. Sorted by date descending. Includes a formula to count action items.

```yaml
filters:
  - file.inFolder("Meetings", true)

display:
  date: "Meeting Date"
  attendees: "Attendees"
  actionItemCount: "Action Items"

formulas:
  actionItemCount: "if(actionItems == null, 0, length(actionItems))"

views:
  - type: "table"
    name: "All Meetings"
    order:
      - by: "date"
        direction: "desc"
    columns:
      - propertyName: "title"
        type: "string"
        width: 350
      - propertyName: "date"
        type: "date"
        width: 120
      - propertyName: "attendees"
        type: "string"
        width: 250
      - propertyName: "actionItemCount"
        type: "number"
        width: 80
      - propertyName: "notes"
        type: "string"
        width: 400
        hidden: false
```

### Example 4: Multi-View Dashboard

A comprehensive base with three views: a table of all items, a card view filtered to "in progress" items only, and a list view of recently modified notes. Includes sorting, filtering, and formulas for computed properties.

```yaml
filters:
  - file.inFolder("Projects", true)

display:
  status: "Status"
  priority: "Priority"
  dueDate: "Due Date"
  owner: "Owner"
  progress: "Progress %"
  daysUntilDue: "Days Until Due"

formulas:
  daysUntilDue: "if(dueDate == null, 999, (dueDate - now()) / 86400)"
  isOverdue: "if(dueDate < now(), true, false)"
  statusIcon: "if(status == 'done', '✓', if(status == 'in progress', '⏳', '□'))"

views:
  # View 1: Complete table of all projects
  - type: "table"
    name: "All Projects"
    order:
      - by: "priority"
        direction: "desc"
      - by: "dueDate"
        direction: "asc"
    columns:
      - propertyName: "title"
        type: "string"
        width: 300
      - propertyName: "statusIcon"
        type: "string"
        width: 60
      - propertyName: "status"
        type: "string"
        width: 120
      - propertyName: "priority"
        type: "number"
        width: 80
      - propertyName: "owner"
        type: "string"
        width: 120
      - propertyName: "progress"
        type: "number"
        width: 80
      - propertyName: "dueDate"
        type: "date"
        width: 120
      - propertyName: "daysUntilDue"
        type: "number"
        width: 100

  # View 2: Card view of in-progress items only
  - type: "cards"
    name: "In Progress"
    filters:
      - status == "in progress"
    cardLayout: "full"
    order:
      - by: "daysUntilDue"
        direction: "asc"

  # View 3: List of recently modified items
  - type: "list"
    name: "Recently Modified"
    order:
      - by: "file.mtime"
        direction: "desc"
    displayProperties:
      - title
      - status
      - owner
      - daysUntilDue
    filters:
      - file.mtime > now() - 604800  # Last 7 days (604800 seconds)
```

---

## Tips & Best Practices

### Organizing Formulas
Define complex formulas at the top level, then reference them in multiple views. This keeps your base DRY and maintainable.

### Filter Performance
Filters are evaluated in order. Put the most restrictive conditions first (e.g., `file.inFolder()` before property comparisons) for better performance.

### Date Arithmetic
Remember that timestamps in Bases are in seconds. For 7 days: `86400 * 7 = 604800` seconds.

### Null Handling
Always check for null in formulas that use optional properties:
```yaml
daysUntilDue: "if(dueDate == null, 999, (dueDate - now()) / 86400)"
```

### Display Labels
Use the `display` block to map property names to human-readable labels once, then reference the property name in views. This centralizes your naming.

### Grouping in Cards
`groupBy` is useful for kanban-style boards (group by status, priority, or owner) to organize cards into columns.

### Recursive Folder Searches
Use `file.inFolder("path", true)` with the second parameter `true` to include subfolders in your search.

---

## Common Patterns

### Find All Incomplete Tasks
```yaml
filters:
  - not:
    - status == "done"
  - not:
    - status == "archived"
```

### Track Overdue Items
```yaml
formulas:
  isOverdue: "dueDate < now()"

views:
  - type: "table"
    name: "Overdue"
    filters:
      - isOverdue == true
```

### Group by Priority and Show Progress
```yaml
display:
  priority: "Priority Level"
  progress: "% Complete"

views:
  - type: "cards"
    name: "By Priority"
    groupBy: "priority"
```

### Recent Notes Dashboard
```yaml
views:
  - type: "list"
    name: "This Week"
    filters:
      - file.mtime > now() - 604800
    order:
      - by: "file.mtime"
        direction: "desc"
```

---

## Troubleshooting

**Formula not computing?**
- Check that all property names are spelled correctly.
- Ensure date properties are in a recognized format (YYYY-MM-DD or ISO 8601).
- Verify that formulas don't reference properties that are null on some notes (use `if()` guards).

**Filter returns no results?**
- Test each filter condition individually to isolate the problem.
- Remember that `and` requires ALL conditions to be true; use `or` if you need ANY to be true.
- Check folder paths—use `file.inFolder("exact/path", true)` to be explicit.

**Column showing raw data?**
- Ensure the `type` field in your column definition matches the property type (string, number, date, boolean).
- Use `display` to set human-readable labels.

**Performance slow?**
- Reduce the number of top-level filters.
- Avoid recursive folder searches (`file.inFolder("path", true)`) on very large vaults.
- Simplify complex formulas or defer computation to multiple smaller formulas.
