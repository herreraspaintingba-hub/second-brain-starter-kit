#!/usr/bin/env python3
"""Builds a small example vault with known problems, for the end-to-end test."""
import os, shutil, sys
dst = sys.argv[1]
if os.path.exists(dst):
    sys.exit("Refusing to write over an existing folder: %s" % dst)
def w(rel, text):
    p = os.path.join(dst, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(text)
FM = '---\ntitle: "{t}"\ntype: {ty}\ndate: 2026-09-01\ntime: "09:15"\ndescription: "{d}"\ntags: [{tags}]\nstatus: active\n---\n\n'
w("09 MOCs/MOC, Garden.md", FM.format(t="MOC, Garden", ty="moc", d="Hub for the garden project", tags="garden") +
  "# MOC, Garden\n\n- [[2026-09-01 Decision, Raised Beds]]\n- [[Watering Schedule]]\n- [[Compost Basics]]\n")
w("02 Strategy/Decision Log/2026-09-01 Decision, Raised Beds.md", FM.format(t="Decision, Raised Beds", ty="decision", d="We chose cedar raised beds over in-ground rows", tags="garden") +
  "# Decision, Raised Beds\n\nWe decided on cedar raised beds. See [[MOC, Garden]] and [[Soil Mix Recipe]].\n")
w("01 Personal Knowledge/Routines/Watering Schedule.md", FM.format(t="Watering Schedule", ty="process", d="When and how much to water", tags="garden") +
  "Water at 6:00 every other day. Linked from [[MOC, Garden]].\n")
w("04 Learning/Books/Compost Basics.md", '---\ntitle: Compost Basics\ntype: book\ndate: 2026-09-02\ndescription: "Notes on composting"\ntags: [Garden Notes]\nstatus: active\n---\n\nBrown and green layers. Decisión: empezar en octubre.\n')
w("03 Ideas & Notes/Lonely idea.md", "No frontmatter here and nothing links to me.\n")
w("03 Ideas & Notes/Lonely idea copy.md", "No frontmatter here and nothing links to me.\n")
w("03 Ideas & Notes/Idea #1.md", FM.format(t="Idea No.1", ty="idea", d="Bad file name on purpose", tags="garden") + "Sell extra tomatoes.\n")
w("01 Personal Knowledge/Old note.md.bak", "backup\n")
w("Archives/Old.md", "archived, never scanned\n")
