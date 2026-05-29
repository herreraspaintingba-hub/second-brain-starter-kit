# Obsidian Canvas Reference

## What Canvas Is

Obsidian Canvas is a core feature (available in all Obsidian installations) that provides an **infinite spatial canvas for visual thinking**. It allows you to organize notes, links, and text in a 2D space, creating mind maps, project boards, dependency diagrams, and knowledge networks.

Canvas files are saved as `.canvas` files using an **open JSON format**, making them human-readable and portable. The format is not encrypted and can be edited directly if needed.

### Key Characteristics
- **Core feature**: Part of Obsidian core, not a community plugin
- **File format**: `.canvas` extension, valid JSON structure
- **Location**: Stored in your vault root or any folder
- **Infinite canvas**: No size limits — pan and zoom freely
- **Cross-linking**: Seamlessly link to vault notes, external URLs, and text cards
- **Visual organization**: Color coding, grouping, edge labeling

---

## Node Types

Canvas supports four primary node types, each with distinct purposes:

| Type | Description | Key Field | Use Case |
|---|---|---|---|
| `text` | Standalone text card | `text` | Quick notes, labels, ideas without creating new files |
| `file` | Reference to a vault note | `file` | Link existing Obsidian notes into the canvas |
| `link` | External URL card | `url` | Reference web pages, articles, or external resources |
| `group` | Container grouping other nodes | `label` | Organize related nodes visually; creates a visual grouping box |

---

## Node Schema

Every node in a canvas has a unique ID and positioning. Below is the complete schema for each node type:

### Common Fields (All Nodes)
```json
{
  "id": "unique-node-identifier",
  "type": "text|file|link|group",
  "x": 0,
  "y": 0,
  "width": 250,
  "height": 100,
  "color": "1"
}
```

### Field Definitions
- **id** (string): Unique identifier within the canvas. Format: alphanumeric, no spaces. Example: `node-1`, `task-research`, `1234567890abc`
- **type** (string): One of `text`, `file`, `link`, or `group`
- **x** (number): Horizontal position in pixels (can be negative)
- **y** (number): Vertical position in pixels (can be negative)
- **width** (number): Node width in pixels. Default: 250. Minimum recommended: 250
- **height** (number): Node height in pixels. Default: 100. Minimum recommended: 100
- **color** (string): Visual color identifier. Values: `"1"` (red), `"2"` (orange), `"3"` (yellow), `"4"` (green), `"5"` (blue), `"6"` (purple). Can also use hex values like `"#ff6b6b"`

### Text Node
A standalone text card with no file reference.

```json
{
  "id": "text-node-1",
  "type": "text",
  "x": 100,
  "y": 200,
  "width": 300,
  "height": 120,
  "color": "3",
  "text": "This is a quick note on the canvas"
}
```

**Additional fields:**
- **text** (string): The text content displayed on the card

### File Node
A reference to an existing Obsidian vault note.

```json
{
  "id": "file-node-1",
  "type": "file",
  "x": 500,
  "y": 300,
  "width": 280,
  "height": 100,
  "color": "4",
  "file": "projects/my-project.md"
}
```

**Additional fields:**
- **file** (string): Relative path to the vault note (from vault root). Examples: `notes/idea.md`, `projects/research-log.md`, `Daily Notes/2024-01-15.md`

### Link Node
An external URL reference.

```json
{
  "id": "link-node-1",
  "type": "link",
  "x": 800,
  "y": 150,
  "width": 350,
  "height": 100,
  "color": "5",
  "url": "https://www.example.com/article"
}
```

**Additional fields:**
- **url** (string): Full URL including protocol (http/https). Examples: `https://en.wikipedia.org/wiki/Canvas`, `https://help.obsidian.md`

### Group Node
A container that visually groups related nodes. Groups don't physically contain nodes but create a visual bounding box.

```json
{
  "id": "group-1",
  "type": "group",
  "x": 0,
  "y": 0,
  "width": 600,
  "height": 800,
  "color": "2",
  "label": "Project Planning"
}
```

**Additional fields:**
- **label** (string): The title displayed on the group box. Examples: `"To Do"`, `"Research Phase"`, `"Q1 Goals"`

---

## Edge Schema

Edges connect nodes with optional labels and colors.

### Complete Edge Structure
```json
{
  "id": "edge-1",
  "fromNode": "node-id-1",
  "toNode": "node-id-2",
  "fromSide": "right",
  "toSide": "left",
  "label": "depends on",
  "color": "1"
}
```

### Field Definitions
- **id** (string): Unique edge identifier. Format: alphanumeric, no spaces. Example: `edge-1`, `connection-research-draft`
- **fromNode** (string): ID of the source node
- **toNode** (string): ID of the target node
- **fromSide** (string): Which side of the source node the edge originates from. Values: `"top"`, `"right"`, `"bottom"`, `"left"`
- **toSide** (string): Which side of the target node the edge arrives at. Values: `"top"`, `"right"`, `"bottom"`, `"left"`
- **label** (string, optional): Text label displayed on the edge. Examples: `"blocks"`, `"relates to"`, `"leads to"`
- **color** (string, optional): Edge color. Values: `"1"` through `"6"` or hex values

### Common Edge Patterns
- **Sequential flow**: fromSide: `"right"`, toSide: `"left"` (left-to-right pipeline)
- **Hierarchical**: fromSide: `"bottom"`, toSide: `"top"` (parent to child)
- **Hub and spoke**: fromSide/toSide vary by node position relative to center hub

---

## Full .canvas File Structure

Every `.canvas` file follows this root structure:

```json
{
  "nodes": [
    { "id": "node-1", "type": "text", "x": 0, "y": 0, "width": 250, "height": 100, "color": "1", "text": "Sample" }
  ],
  "edges": [
    { "id": "edge-1", "fromNode": "node-1", "toNode": "node-2", "fromSide": "right", "toSide": "left" }
  ]
}
```

### Root Fields
- **nodes** (array): Array of node objects. Can be empty.
- **edges** (array): Array of edge objects. Can be empty.

### Validation Rules
- All node IDs must be unique within the canvas
- All edge IDs must be unique within the canvas
- Edges must reference valid node IDs (fromNode and toNode must exist)
- Color values must be strings (e.g., `"1"`, not `1`)
- Coordinates (x, y) can be negative (allows panning left/up from origin)

---

## Complete Example Canvas Files

### Example 1: Project Planning Board (Swim Lane / Kanban)

A kanban-style board with three columns: To Do, In Progress, Done. Includes group nodes for columns, text nodes for individual tasks, and edges showing task flow.

```json
{
  "nodes": [
    {
      "id": "group-todo",
      "type": "group",
      "x": 0,
      "y": 0,
      "width": 300,
      "height": 800,
      "color": "1",
      "label": "To Do"
    },
    {
      "id": "group-inprogress",
      "type": "group",
      "x": 400,
      "y": 0,
      "width": 300,
      "height": 800,
      "color": "3",
      "label": "In Progress"
    },
    {
      "id": "group-done",
      "type": "group",
      "x": 800,
      "y": 0,
      "width": 300,
      "height": 800,
      "color": "4",
      "label": "Done"
    },
    {
      "id": "task-1",
      "type": "text",
      "x": 20,
      "y": 50,
      "width": 260,
      "height": 100,
      "color": "1",
      "text": "Research project requirements"
    },
    {
      "id": "task-2",
      "type": "text",
      "x": 20,
      "y": 200,
      "width": 260,
      "height": 100,
      "color": "1",
      "text": "Create project timeline"
    },
    {
      "id": "task-3",
      "type": "text",
      "x": 20,
      "y": 350,
      "width": 260,
      "height": 100,
      "color": "1",
      "text": "Gather team feedback"
    },
    {
      "id": "task-4",
      "type": "text",
      "x": 420,
      "y": 50,
      "width": 260,
      "height": 100,
      "color": "3",
      "text": "Design system architecture"
    },
    {
      "id": "task-5",
      "type": "text",
      "x": 420,
      "y": 200,
      "width": 260,
      "height": 100,
      "color": "3",
      "text": "Implement core features"
    },
    {
      "id": "task-6",
      "type": "text",
      "x": 820,
      "y": 50,
      "width": 260,
      "height": 100,
      "color": "4",
      "text": "Documentation complete"
    },
    {
      "id": "task-7",
      "type": "text",
      "x": 820,
      "y": 200,
      "width": 260,
      "height": 100,
      "color": "4",
      "text": "Testing passed"
    },
    {
      "id": "milestone",
      "type": "file",
      "x": 400,
      "y": 600,
      "width": 300,
      "height": 120,
      "color": "6",
      "file": "projects/milestones.md"
    }
  ],
  "edges": [
    {
      "id": "flow-1",
      "fromNode": "task-1",
      "toNode": "task-4",
      "fromSide": "right",
      "toSide": "left",
      "label": "leads to",
      "color": "1"
    },
    {
      "id": "flow-2",
      "fromNode": "task-2",
      "toNode": "task-5",
      "fromSide": "right",
      "toSide": "left",
      "label": "leads to",
      "color": "1"
    },
    {
      "id": "flow-3",
      "fromNode": "task-4",
      "toNode": "task-6",
      "fromSide": "right",
      "toSide": "left",
      "label": "completed",
      "color": "4"
    },
    {
      "id": "flow-4",
      "fromNode": "task-5",
      "toNode": "task-7",
      "fromSide": "right",
      "toSide": "left",
      "label": "completed",
      "color": "4"
    },
    {
      "id": "milestone-link",
      "fromNode": "task-3",
      "toNode": "milestone",
      "fromSide": "bottom",
      "toSide": "top",
      "label": "updates",
      "color": "6"
    }
  ]
}
```

---

### Example 2: Topic Cluster (Hub and Spoke)

A central topic with satellite ideas and references branching outward. The hub is positioned at the center, with spokes radiating at ~400px radius.

```json
{
  "nodes": [
    {
      "id": "hub-main",
      "type": "text",
      "x": -50,
      "y": -50,
      "width": 200,
      "height": 100,
      "color": "5",
      "text": "Climate Change Impact on Ecosystems"
    },
    {
      "id": "spoke-1",
      "type": "text",
      "x": 400,
      "y": -100,
      "width": 200,
      "height": 100,
      "color": "3",
      "text": "Ocean Acidification"
    },
    {
      "id": "spoke-2",
      "type": "text",
      "x": 350,
      "y": 250,
      "width": 200,
      "height": 100,
      "color": "3",
      "text": "Forest Die-Off"
    },
    {
      "id": "spoke-3",
      "type": "text",
      "x": -300,
      "y": 250,
      "width": 200,
      "height": 100,
      "color": "3",
      "text": "Species Migration"
    },
    {
      "id": "spoke-4",
      "type": "text",
      "x": -400,
      "y": -50,
      "width": 200,
      "height": 100,
      "color": "3",
      "text": "Extreme Weather"
    },
    {
      "id": "research-1",
      "type": "link",
      "x": 550,
      "y": -150,
      "width": 280,
      "height": 80,
      "color": "2",
      "url": "https://www.nature.com/articles/s41558-020-0822-0"
    },
    {
      "id": "research-2",
      "type": "link",
      "x": 550,
      "y": 280,
      "width": 280,
      "height": 80,
      "color": "2",
      "url": "https://www.ipcc.ch/report/ar6/wg2/"
    },
    {
      "id": "note-1",
      "type": "file",
      "x": -550,
      "y": -150,
      "width": 250,
      "height": 100,
      "color": "4",
      "file": "research/climate-notes.md"
    },
    {
      "id": "note-2",
      "type": "file",
      "x": -550,
      "y": 250,
      "width": 250,
      "height": 100,
      "color": "4",
      "file": "research/species-tracking.md"
    }
  ],
  "edges": [
    {
      "id": "hub-spoke-1",
      "fromNode": "hub-main",
      "toNode": "spoke-1",
      "fromSide": "right",
      "toSide": "left",
      "color": "5"
    },
    {
      "id": "hub-spoke-2",
      "fromNode": "hub-main",
      "toNode": "spoke-2",
      "fromSide": "right",
      "toSide": "left",
      "color": "5"
    },
    {
      "id": "hub-spoke-3",
      "fromNode": "hub-main",
      "toNode": "spoke-3",
      "fromSide": "left",
      "toSide": "right",
      "color": "5"
    },
    {
      "id": "hub-spoke-4",
      "fromNode": "hub-main",
      "toNode": "spoke-4",
      "fromSide": "left",
      "toSide": "right",
      "color": "5"
    },
    {
      "id": "spoke-research-1",
      "fromNode": "spoke-1",
      "toNode": "research-1",
      "fromSide": "right",
      "toSide": "left",
      "label": "reference",
      "color": "2"
    },
    {
      "id": "spoke-research-2",
      "fromNode": "spoke-2",
      "toNode": "research-2",
      "fromSide": "right",
      "toSide": "left",
      "label": "reference",
      "color": "2"
    },
    {
      "id": "spoke-note-1",
      "fromNode": "spoke-4",
      "toNode": "note-1",
      "fromSide": "left",
      "toSide": "right",
      "label": "documented",
      "color": "4"
    },
    {
      "id": "spoke-note-2",
      "fromNode": "spoke-3",
      "toNode": "note-2",
      "fromSide": "left",
      "toSide": "right",
      "label": "documented",
      "color": "4"
    }
  ]
}
```

---

### Example 3: Content Pipeline (Left-to-Right Flow)

A content production pipeline from Idea → Research → Draft → Edit → Publish. Nodes flow horizontally with edges showing sequential progression. Includes file references for each stage.

```json
{
  "nodes": [
    {
      "id": "stage-idea",
      "type": "group",
      "x": 0,
      "y": 0,
      "width": 280,
      "height": 400,
      "color": "2",
      "label": "Stage 1: Ideation"
    },
    {
      "id": "stage-research",
      "type": "group",
      "x": 550,
      "y": 0,
      "width": 280,
      "height": 400,
      "color": "3",
      "label": "Stage 2: Research"
    },
    {
      "id": "stage-draft",
      "type": "group",
      "x": 1100,
      "y": 0,
      "width": 280,
      "height": 400,
      "color": "1",
      "label": "Stage 3: Draft"
    },
    {
      "id": "stage-edit",
      "type": "group",
      "x": 1650,
      "y": 0,
      "width": 280,
      "height": 400,
      "color": "1",
      "label": "Stage 4: Edit"
    },
    {
      "id": "stage-publish",
      "type": "group",
      "x": 2200,
      "y": 0,
      "width": 280,
      "height": 400,
      "color": "4",
      "label": "Stage 5: Publish"
    },
    {
      "id": "idea-brainstorm",
      "type": "text",
      "x": 30,
      "y": 50,
      "width": 220,
      "height": 80,
      "color": "2",
      "text": "Brainstorm topic ideas"
    },
    {
      "id": "idea-outline",
      "type": "text",
      "x": 30,
      "y": 180,
      "width": 220,
      "height": 80,
      "color": "2",
      "text": "Create outline"
    },
    {
      "id": "research-sources",
      "type": "text",
      "x": 580,
      "y": 50,
      "width": 220,
      "height": 80,
      "color": "3",
      "text": "Gather sources"
    },
    {
      "id": "research-analysis",
      "type": "file",
      "x": 580,
      "y": 180,
      "width": 220,
      "height": 80,
      "color": "3",
      "file": "content/research-notes.md"
    },
    {
      "id": "draft-write",
      "type": "text",
      "x": 1130,
      "y": 50,
      "width": 220,
      "height": 80,
      "color": "1",
      "text": "Write first draft"
    },
    {
      "id": "draft-version",
      "type": "file",
      "x": 1130,
      "y": 180,
      "width": 220,
      "height": 80,
      "color": "1",
      "file": "content/draft-v1.md"
    },
    {
      "id": "edit-review",
      "type": "text",
      "x": 1680,
      "y": 50,
      "width": 220,
      "height": 80,
      "color": "1",
      "text": "Copy editing"
    },
    {
      "id": "edit-final",
      "type": "text",
      "x": 1680,
      "y": 180,
      "width": 220,
      "height": 80,
      "color": "1",
      "text": "Final review"
    },
    {
      "id": "publish-schedule",
      "type": "text",
      "x": 2230,
      "y": 50,
      "width": 220,
      "height": 80,
      "color": "4",
      "text": "Schedule post"
    },
    {
      "id": "publish-promote",
      "type": "text",
      "x": 2230,
      "y": 180,
      "width": 220,
      "height": 80,
      "color": "4",
      "text": "Promote"
    }
  ],
  "edges": [
    {
      "id": "flow-idea-to-research",
      "fromNode": "idea-outline",
      "toNode": "research-sources",
      "fromSide": "right",
      "toSide": "left",
      "label": "ready for",
      "color": "5"
    },
    {
      "id": "flow-research-to-draft",
      "fromNode": "research-analysis",
      "toNode": "draft-write",
      "fromSide": "right",
      "toSide": "left",
      "label": "inform",
      "color": "5"
    },
    {
      "id": "flow-draft-to-edit",
      "fromNode": "draft-version",
      "toNode": "edit-review",
      "fromSide": "right",
      "toSide": "left",
      "label": "needs",
      "color": "5"
    },
    {
      "id": "flow-edit-to-publish",
      "fromNode": "edit-final",
      "toNode": "publish-schedule",
      "fromSide": "right",
      "toSide": "left",
      "label": "ready",
      "color": "5"
    },
    {
      "id": "brainstorm-outline",
      "fromNode": "idea-brainstorm",
      "toNode": "idea-outline",
      "fromSide": "bottom",
      "toSide": "top",
      "color": "2"
    },
    {
      "id": "sources-analysis",
      "fromNode": "research-sources",
      "toNode": "research-analysis",
      "fromSide": "bottom",
      "toSide": "top",
      "color": "3"
    },
    {
      "id": "write-version",
      "fromNode": "draft-write",
      "toNode": "draft-version",
      "fromSide": "bottom",
      "toSide": "top",
      "color": "1"
    },
    {
      "id": "review-final",
      "fromNode": "edit-review",
      "toNode": "edit-final",
      "fromSide": "bottom",
      "toSide": "top",
      "color": "1"
    },
    {
      "id": "schedule-promote",
      "fromNode": "publish-schedule",
      "toNode": "publish-promote",
      "fromSide": "bottom",
      "toSide": "top",
      "color": "4"
    }
  ]
}
```

---

## Layout Strategies

Different canvas layouts serve different purposes. Here are proven patterns with recommended positioning formulas:

### Swim Lane (Kanban / Column-Based)

**Purpose**: Organize items into sequential or categorical columns (e.g., project status, workflow stages, priority buckets).

**Layout Pattern**:
- Group nodes spaced **500px apart horizontally** (x-axis)
- Task nodes nested within each group, starting at x-offset +20, y-offset +50
- Vertical spacing between tasks: **150px** (height + 50px gap)
- Recommended group width: **300px**, height: **800px** (scalable based on tasks)

**Example Positioning**:
```
Column 1 (To Do):    x=0,   y=0
Column 2 (In Progress): x=500, y=0
Column 3 (Done):     x=1000, y=0

Task in Column 1:    x=20,  y=50
Task in Column 1:    x=20,  y=200
Task in Column 1:    x=20,  y=350
```

**Best for**: Project management, workflow status boards, priority matrices, agile sprints.

### Topic Cluster (Hub and Spoke)

**Purpose**: Show a central concept with related ideas radiating outward, like a mind map.

**Layout Pattern**:
- Hub node at center: **x=0, y=0** (or offset for visual balance)
- Spoke nodes positioned at **~400px radius** from hub
- Calculate angle: distribute nodes around 360° circle
- For N nodes evenly spaced: angle = 360 / N, then x = radius × cos(angle), y = radius × sin(angle)
- Outer reference nodes (links, files) at **~600px radius** from hub

**Example Positioning for 4 Spokes**:
```
Hub:      x=-50,  y=-50    (slightly offset for visual balance)
Spoke 1:  x=400,  y=-100   (right, slightly up)
Spoke 2:  x=350,  y=250    (right, down)
Spoke 3:  x=-300, y=250    (left, down)
Spoke 4:  x=-400, y=-50    (left, center)

Research link for Spoke 1: x=650, y=-150
```

**Best for**: Brainstorming, topic exploration, concept maps, decision trees.

### Pipeline (Left-to-Right Flow)

**Purpose**: Show a sequential process or workflow progressing left to right, with stages and milestones.

**Layout Pattern**:
- Stage groups spaced **550px apart horizontally** (x-axis)
- Nodes within a stage: x-offset +30, y-offset +50
- Vertical spacing within stage: **130px** (height + 50px gap)
- All stages start at y=0 for visual alignment
- Recommended stage width: **280px**, height: **400px**

**Example Positioning for 5 Stages**:
```
Stage 1:  x=0,    y=0
Stage 2:  x=550,  y=0
Stage 3:  x=1100, y=0
Stage 4:  x=1650, y=0
Stage 5:  x=2200, y=0

Task in Stage 1:   x=30,   y=50
Task in Stage 1:   x=30,   y=180
Task in Stage 2:   x=580,  y=50
Task in Stage 2:   x=580,  y=180
```

**Best for**: Content pipelines, sales funnels, development workflows, approval processes.

### Hierarchical (Parent-Child Tree)

**Purpose**: Show organizational structure, dependency trees, or nested relationships with parents at the top and children below.

**Layout Pattern**:
- Parent node at top: x=0, y=0
- Each parent spans a section horizontally based on number of children
- Children positioned **300px below** parent (y-axis)
- Horizontal spacing between children: **250px**
- Grandchildren positioned **300px below** children
- Align children centers with parent center

**Example Positioning**:
```
Parent (Project):       x=-50,   y=0

Child 1 (Phase 1):      x=-300,  y=300
Child 2 (Phase 2):      x=0,     y=300
Child 3 (Phase 3):      x=300,   y=300

Grandchild (Task):      x=-350,  y=600
Grandchild (Task):      x=-150,  y=600
```

**Best for**: Organizational charts, project breakdowns, dependency graphs, outline hierarchies.

### Matrix (Two-Axis Categorization)

**Purpose**: Organize items by two dimensions (e.g., Importance vs. Urgency, Effort vs. Impact).

**Layout Pattern**:
- Create four quadrants by positioning groups at corners
- Axis labels as text nodes (e.g., "High Effort", "Low Effort")
- Items positioned within appropriate quadrant based on their properties
- Quadrants spaced **600px apart**

**Example Positioning (Importance × Urgency)**:
```
Quadrant groups (starting at corners):
Top-Left (High Importance, Low Urgency):     x=-300, y=-300
Top-Right (High Importance, High Urgency):   x=300,  y=-300
Bottom-Left (Low Importance, Low Urgency):   x=-300, y=300
Bottom-Right (Low Importance, High Urgency): x=300,  y=300

Item in Top-Right:  x=320, y=-280
Item in Top-Right:  x=380, y=-200
```

**Best for**: Priority matrices, risk assessment, resource allocation, decision frameworks.

---

## Canvas Tips and Best Practices

### Sizing
- **Minimum recommended node size**: 250px wide × 100px tall (readable at normal zoom)
- **Group nodes**: Should be larger than their contents with padding (e.g., 300×800 for a column containing 4-5 tasks)
- **Larger nodes for emphasis**: 400px× 150px for important concepts or decision points
- **Compact nodes**: 200×80 for simple labels or secondary information

### Spacing
- **Gap between nodes**: 50-100px recommended (prevents visual crowding)
- **Edge visibility**: Position nodes so edges don't overlap; use positioning to separate parallel flows
- **Zoom-out readability**: At 50% zoom, nodes should remain readable and distinct

### Color Coding Strategy
Use colors consistently throughout your canvas:
- **Red (1)**: Urgent, blocking, or high-priority items
- **Orange (2)**: Secondary priority or warning items
- **Yellow (3)**: In-progress or active items
- **Green (4)**: Completed or low-risk items
- **Blue (5)**: Information, central concepts, or hub nodes
- **Purple (6)**: References, external links, or future items

Apply colors to both nodes and edges for consistency. Example: all "research" nodes use orange (2), and edges leading to research nodes also use orange.

### Grouping for Organization
- Use group nodes to create visual sections, not to physically contain items
- Add descriptive labels to groups: "Q1 Goals", "High Priority", "Archive"
- Overlap groups slightly if relationships cross categories
- Keep groups at consistent opacity (no overlap of unrelated groups)

### Edge Labeling
- Short, action-oriented labels: "leads to", "blocks", "depends on", "informs", "needs"
- Avoid long phrases; use verbs or verb phrases
- Label edges that represent important relationships or constraints
- Use edge colors to reinforce node color coding

### Connecting Files and External Resources
- **File nodes**: Link to related vault notes for deep dives without cluttering the canvas
- **Link nodes**: Reference articles, tools, or websites used in the canvas
- **Context**: Placing a file/link node near related concepts provides quick access without overwhelming the canvas
- **Density**: Aim for a balance between visual simplicity and actionable detail

### Pan and Zoom
- Obsidian Canvas supports infinite panning; use the full space
- Negative coordinates (x/y < 0) are valid; position content to the left and above origin if needed
- Group related clusters far apart to create "zones" you can zoom into
- Use the mini-map (if visible in your view) to navigate large canvases

### Canvas File Management
- **File naming**: Use descriptive names with prefixes (e.g., `Project-Kickoff.canvas`, `Research-Cluster.canvas`)
- **Organization**: Store canvases in a dedicated folder (e.g., `/canvases/`) or project folders
- **Versioning**: For active projects, consider dating canvases or keeping archive versions
- **Size limits**: Canvas performance remains excellent even with 100+ nodes; if slower, consider splitting into multiple canvases

### Common Pitfalls to Avoid
- **Over-crowding**: Don't place more than 20-30 nodes in a small area; use groups or multiple canvases instead
- **Unclear edges**: Ensure edges connect logically; tangled connections suggest layout needs reorganizing
- **Missing context**: Add descriptive text nodes to explain the canvas purpose or key sections
- **Dead nodes**: Regularly prune nodes that no longer serve the canvas; archived projects belong in separate canvases
- **Inconsistent colors**: Establish a color scheme early and stick to it across all project canvases

---

## Canvas as a Thinking Tool

Canvas is most powerful when used as an **external thought processor**, not just a visualization:

- **Iterative design**: Start with a rough layout, then refine positioning and connections
- **Idea capture**: Use text nodes for half-formed thoughts; elaborate later
- **Visual feedback**: The spatial arrangement often reveals gaps or connections not obvious in linear notes
- **Collaborative clarity**: A canvas serves as a shared mental model for teams
- **Process documentation**: Canvases can replace flowchart tools by leveraging your existing Obsidian vault

---

## JSON Validation Checklist

When creating or editing `.canvas` files:

- [ ] Valid JSON structure (use a JSON validator)
- [ ] All node IDs unique
- [ ] All edge IDs unique
- [ ] All edge fromNode/toNode references valid node IDs
- [ ] Color values are strings (`"1"`, not `1`)
- [ ] x, y, width, height are numbers
- [ ] file paths use relative paths from vault root
- [ ] urls include protocol (https://)
- [ ] No circular references in edges (optional, but usually indicates a layout issue)
- [ ] Coordinates spaced to avoid excessive node overlap
