#!/usr/bin/env python3
"""
door.py: reads a project Door one piece at a time, and creates new Doors.

A Door is one note per project, in 09 MOCs/, named "Door, <Project>.md"
(or "Puerta, <Proyecto>.md"). It holds the project's current state in one screen,
with six numbered sections:

    1. Current state         (what is true today)
    2. Numbers that matter   (the few figures that drive decisions)
    3. Next steps            (what is pending, and who owns it)
    4. How it runs           (how to operate or ship it)
    5. Where everything else lives (links to the rest)
    6. History               (what changed, newest first)

At the start of a session only sections 1, 2 and 3 are needed (the "front page").
The note is never split: in Obsidian it stays one screen. This script only controls
how much the AI reads when it opens it.

Usage:
    python3 door.py                       # list the Doors with their verified date
    python3 door.py "Kitchen Remodel"     # front page: sections 1, 2 and 3
    python3 door.py "Kitchen Remodel" 5   # one section
    python3 door.py "Kitchen Remodel" --all
    python3 door.py --new "Kitchen Remodel" [--lang es] [--project kitchen-remodel]
"""

import argparse
import datetime as dt
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brainlib as bl  # noqa: E402

FRONT = ("1", "2", "3")
PREFIXES = ("Door, ", "Puerta, ")
STALE_DAYS = 7

SECTIONS = {
    "en": ["Current state", "Numbers that matter", "Next steps", "How it runs",
           "Where everything else lives", "History"],
    "es": ["Estado vigente", "Números que mandan", "Pendientes", "Cómo se opera",
           "Dónde vive lo demás", "Historial"],
}
HINTS = {
    "en": ["Three to six lines: what is true about this project today.",
           "The few figures that drive decisions (dates, money, counts), each with its source.",
           "- [ ] The next concrete step, and who owns it",
           "How to run, use or ship it, step by step. Read only when the task needs it.",
           "Links to the MOC, the checkpoint, the decisions and the files of this project.",
           "- {date}: Door created."],
    "es": ["De tres a seis renglones: lo que es verdad hoy en este proyecto.",
           "Las pocas cifras que deciden (fechas, dinero, conteos), cada una con su fuente.",
           "- [ ] El siguiente paso concreto, y de quién es",
           "Cómo se corre, se usa o se entrega, paso a paso. Se lee solo cuando la tarea lo pide.",
           "Links al MOC, al checkpoint, a las decisiones y a los archivos de este proyecto.",
           "- {date}: se creó la Puerta."],
}


def mocs_dir(vault):
    hits = sorted(d for d in os.listdir(vault) if d.startswith("09") and os.path.isdir(os.path.join(vault, d)))
    return os.path.join(vault, hits[0] if hits else "09 MOCs")


def all_doors(vault):
    out = []
    for pre in PREFIXES:
        out += glob.glob(os.path.join(mocs_dir(vault), pre + "*.md"))
    return sorted(out)


def find(vault, name):
    squash = lambda s: bl.nfc(s).lower().replace(" ", "")
    for pre in PREFIXES:
        exact = os.path.join(mocs_dir(vault), pre + name + ".md")
        if os.path.exists(exact):
            return exact
    for p in all_doors(vault):
        if squash(name) in squash(os.path.basename(p)):
            return p
    return None


def verified(txt):
    m = re.search(r'^verified:\s*"?(\d{4}-\d{2}-\d{2})', txt, re.M)
    if not m:
        return None, None
    d = dt.date.fromisoformat(m.group(1))
    return m.group(1), (dt.date.today() - d).days


def section(txt, n):
    m = re.search(r"^## %s\. " % re.escape(n), txt, re.M)
    if not m:
        return ""
    nxt = re.search(r"^## \d+\. ", txt[m.end():], re.M)
    return txt[m.start(): m.end() + nxt.start()] if nxt else txt[m.start():]


def label(path):
    base = os.path.basename(path)[:-3]
    for pre in PREFIXES:
        if base.startswith(pre):
            return base[len(pre):]
    return base


def create(vault, name, lang, project):
    bad = sorted(set(name) & bl.FORBIDDEN_NAME_CHARS)
    if bad:
        sys.exit("The name has %s, which Obsidian cannot link. Choose another name." % " ".join(bad))
    os.makedirs(mocs_dir(vault), exist_ok=True)
    pre = "Puerta, " if lang == "es" else "Door, "
    path = os.path.join(mocs_dir(vault), pre + name + ".md")
    if os.path.exists(path):
        sys.exit("That Door already exists: %s" % path)
    now = dt.datetime.now()
    today = now.strftime("%Y-%m-%d")
    desc = ("Estado vigente de %s en una pantalla; se sobrescribe en cada cierre de sesión" % name
            if lang == "es" else "Current state of %s in one screen; rewritten at every session close" % name)
    lines = ["---", 'title: "%s%s"' % (pre, name), "type: door"]
    if project:
        lines.append("project: %s" % project)
    lines += ["date: %s" % today, 'time: "%s"' % now.strftime("%H:%M"), "verified: %s" % today,
              'description: "%s"' % desc, "tags: [door]", "status: active", "---", "",
              "# %s%s" % (pre, name), ""]
    for i, (title, hint) in enumerate(zip(SECTIONS[lang], HINTS[lang]), 1):
        lines += ["## %d. %s" % (i, title), "", hint.format(date=today), ""]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print("Created %s" % os.path.relpath(path, vault))
    if project:
        print("Remember: add '%s' to the project list in .brain/vocabulary.json if it is new." % project)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Read or create project Doors.")
    ap.add_argument("name", nargs="?")
    ap.add_argument("part", nargs="?", help="a section number, or --all")
    ap.add_argument("--all", action="store_true", help="print the whole Door")
    ap.add_argument("--new", metavar="NAME", help="create a Door for this project")
    ap.add_argument("--lang", choices=["en", "es"], default="en")
    ap.add_argument("--project", help="project slug for the frontmatter")
    ap.add_argument("--vault")
    args = ap.parse_args(argv)
    vault = bl.find_vault(args.vault)

    if args.new:
        create(vault, args.new.strip(), args.lang, args.project)
        return 0
    if not args.name:
        doors = all_doors(vault)
        if not doors:
            print("No Doors yet. Create one with: door.py --new \"Project name\"")
            return 0
        print("Doors:\n")
        for p in doors:
            d, days = verified(bl.read_text(p))
            print("  %-28s verified %s (%s days ago)" % (label(p), d or "never", "?" if days is None else days))
        return 0

    p = find(vault, args.name)
    if not p:
        print("No Door matches '%s'. Run door.py with no arguments to list them." % args.name)
        return 1
    txt = bl.read_text(p)
    if args.all or args.part == "--all":
        print(txt)
        return 0
    d, days = verified(txt)
    note = "verified %s, %s days ago" % (d or "never", "?" if days is None else days)
    if days is None or days >= STALE_DAYS:
        note += ". These figures may be old: check them before deciding"
    print("# %s (%s)\n" % (os.path.basename(p)[:-3], note))
    wanted = (args.part,) if args.part else FRONT
    for n in wanted:
        s = section(txt, n)
        if s:
            print(s.rstrip() + "\n")
    if not args.part:
        print("> Sections 4 (how it runs), 5 (where everything else lives) and 6 (history)")
        print("> were not loaded. Read one when the task needs it: door.py \"%s\" 4" % args.name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
