#!/usr/bin/env python3
"""
brain_health.py: measures the health of your vault with the same rules every month,
and keeps a history so this month is compared against last month.

What it measures:
    notes           how many notes, and how many per section (00 to 09)
    broken links    [[links]] that point to a note that does not exist
    orphans         notes nothing links to (MOCs, Doors and session logs excluded)
    no frontmatter  notes without the properties block at the top
    contract        % of notes that pass check_frontmatter.py
    .bak files      backup copies sitting inside the vault (should be 0)
    duplicates      notes whose body is an exact copy of another note
    bad names       file names with # ^ [ ] | : (Obsidian cannot link them)
    stale doors     project Doors not verified in 30 days

The light:
    RED     .bak files inside the vault, or broken links grew more than 10% since last time
    YELLOW  broken links grew, contract % dropped, bad names, or stale Doors
    GREEN   none of the above

Usage:
    python3 brain_health.py                # measure and print, change nothing
    python3 brain_health.py --write        # also add today's row to the history note
    python3 brain_health.py --write --reindex   # and rebuild the search index (monthly job)

The history note is "05 AI System/Brain Health History.md". Earlier rows are kept.
Exit code is always 0 (a red light is information, not a crash). Standard library only.
"""

import argparse
import datetime as dt
import hashlib
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brainlib as bl  # noqa: E402
import check_frontmatter as cf  # noqa: E402

HISTORY_REL = os.path.join("05 AI System", "Brain Health History.md")
RED_BROKEN_GROWTH = 0.10
STALE_DOOR_DAYS = 30
NOT_ORPHAN_TYPES = {"moc", "door", "health", "checkpoint", "session"}


def measure(vault, vocab):
    notes = {}
    for full, rel in bl.walk_notes(vault):
        text = bl.read_text(full)
        data, body = bl.parse_frontmatter(text)
        notes[rel] = {"full": full, "data": data, "body": body, "has_fm": text.lstrip("﻿").startswith("---")}

    keys = {}
    for rel in notes:
        keys.setdefault(bl.note_key(rel), []).append(rel)
    # every file in the vault can be a link target (images, PDFs, canvases too)
    all_names = set()
    bak = []
    for dp, dns, fns in os.walk(vault):
        dns[:] = [d for d in dns if d not in (".git", ".trash", ".obsidian")]
        in_archives = os.path.relpath(dp, vault).split(os.sep)[0] == "Archives"
        for f in fns:
            all_names.add(bl.note_key(f))
            if ".bak" in f.lower() and not in_archives:
                bak.append(os.path.relpath(os.path.join(dp, f), vault))

    inbound = {rel: 0 for rel in notes}
    broken = {}
    for rel, n in notes.items():
        for target in bl.wikilinks(n["body"]):
            k = bl.note_key(target)
            hits = keys.get(k)
            if hits:
                for h in hits:
                    if h != rel:
                        inbound[h] += 1
            elif k not in all_names:
                broken.setdefault(target, []).append(rel)

    orphans = []
    for rel, n in notes.items():
        typ = bl.as_text(bl.pick(n["data"], "type")).lower()
        if inbound[rel] or typ in NOT_ORPHAN_TYPES or rel.startswith("06") or "/" not in rel:
            continue
        orphans.append(rel)

    passing = 0
    for rel, n in notes.items():
        if not cf.validate(bl.nfc(os.path.basename(rel))[:-3], n["data"], vocab):
            passing += 1

    seen, dups = {}, []
    for rel, n in notes.items():
        b = n["body"].strip()
        if len(b) < 40:
            continue
        h = hashlib.md5(b.encode("utf-8")).hexdigest()
        if h in seen:
            dups.append((rel, seen[h]))
        else:
            seen[h] = rel

    bad_names = [rel for rel in notes if set(os.path.basename(rel)[:-3]) & bl.FORBIDDEN_NAME_CHARS]

    stale = []
    today = dt.date.today()
    for rel, n in notes.items():
        if bl.as_text(bl.pick(n["data"], "type")).lower() != "door":
            continue
        v = bl.norm_date(n["data"].get("verified", ""))
        if not v or (today - dt.date.fromisoformat(v)).days > STALE_DOOR_DAYS:
            stale.append(rel)

    sections = {}
    for rel in notes:
        top = rel.split("/", 1)[0] if "/" in rel else "(root)"
        sections[top] = sections.get(top, 0) + 1

    total = len(notes)
    return {
        "notes": total,
        "sections": dict(sorted(sections.items())),
        "broken": sum(len(v) for v in broken.values()),
        "broken_targets": len(broken),
        "broken_list": sorted(broken.items(), key=lambda kv: -len(kv[1])),
        "orphans": len(orphans), "orphan_list": sorted(orphans),
        "no_fm": sum(1 for n in notes.values() if not n["has_fm"]),
        "contract": round(100.0 * passing / total, 1) if total else 100.0,
        "bak": len(bak), "bak_list": sorted(bak),
        "dups": len(dups), "dup_list": dups,
        "bad_names": len(bad_names), "bad_list": sorted(bad_names),
        "stale": len(stale), "stale_list": sorted(stale),
    }


ROW_RE = re.compile(r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|")


def previous_rows(path):
    if not os.path.exists(path):
        return []
    rows = []
    for line in bl.read_text(path).splitlines():
        if ROW_RE.match(line):
            rows.append(line.rstrip())
    return rows


def parse_row(line):
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    try:
        broken = int(cells[2].split()[0])
        contract = float(cells[5].rstrip("%"))
    except (IndexError, ValueError):
        return None
    return {"date": cells[0], "broken": broken, "contract": contract}


def light(prev, cur):
    reasons, color = [], "GREEN"

    def at_least(c):
        nonlocal color
        order = ["GREEN", "YELLOW", "RED"]
        if order.index(c) > order.index(color):
            color = c

    if cur["bak"]:
        at_least("RED")
        reasons.append("%d .bak file(s) inside the vault" % cur["bak"])
    if prev:
        d = cur["broken"] - prev["broken"]
        if d > 0 and (prev["broken"] == 0 or cur["broken"] > prev["broken"] * (1 + RED_BROKEN_GROWTH)):
            at_least("RED")
            reasons.append("broken links %d to %d (more than 10%% up)" % (prev["broken"], cur["broken"]))
        elif d > 0:
            at_least("YELLOW")
            reasons.append("broken links %d to %d" % (prev["broken"], cur["broken"]))
        elif d < 0:
            reasons.append("broken links down, %d to %d" % (prev["broken"], cur["broken"]))
        if cur["contract"] < prev["contract"]:
            at_least("YELLOW")
            reasons.append("contract %.1f%% to %.1f%%" % (prev["contract"], cur["contract"]))
    if cur["bad_names"]:
        at_least("YELLOW")
        reasons.append("%d file name(s) Obsidian cannot link" % cur["bad_names"])
    if cur["stale"]:
        at_least("YELLOW")
        reasons.append("%d Door(s) not verified in %d days" % (cur["stale"], STALE_DOOR_DAYS))
    if not reasons:
        reasons.append("first run, nothing to compare yet" if not prev else "no changes worth flagging")
    return color, reasons


def row_text(date, m, color, reasons):
    return "| %s | %d | %d (%d) | %d | %d | %.1f%% | %d | %d | %s | %s |" % (
        date, m["notes"], m["broken"], m["broken_targets"], m["orphans"], m["no_fm"],
        m["contract"], m["bak"], m["dups"], color, "; ".join(reasons).replace("|", "/"))


def bullets(items, fmt, cap=15):
    out = [fmt(x) for x in items[:cap]]
    if len(items) > cap:
        out.append("- ...and %d more" % (len(items) - cap))
    return out or ["- none"]


def write_note(path, rows, m, color, reasons, now):
    first_date = rows[0].split("|")[1].strip() if rows else now.strftime("%Y-%m-%d")
    L = ["---", 'title: "Brain Health History"', "type: health", "date: %s" % first_date,
         'time: "%s"' % now.strftime("%H:%M"),
         'description: "One row per health check, so the vault is compared month against month with the same rules."',
         "tags: [brain-health]", "status: active", "---", "",
         "# Brain Health History", "",
         "> [!info] What this is",
         "> Written by `brain_health.py`. One row per run. Compare against last month, not against perfection.", "",
         "## Latest: %s, %s" % (now.strftime("%Y-%m-%d %H:%M"), color), ""]
    L += ["- " + r for r in reasons]
    L += ["", "| Section | Notes |", "|---|---|"]
    L += ["| %s | %d |" % (k, v) for k, v in m["sections"].items()]
    L += ["", "### Broken links (most repeated first)", ""]
    L += bullets(m["broken_list"], lambda kv: "- `%s` from %d note(s), e.g. %s" % (kv[0], len(kv[1]), kv[1][0]))
    L += ["", "### Orphans (nothing links to them)", ""]
    L += bullets(m["orphan_list"], lambda r: "- %s" % r)
    if m["bak_list"]:
        L += ["", "### .bak files to move out of the vault", ""] + bullets(m["bak_list"], lambda r: "- %s" % r)
    if m["dup_list"]:
        L += ["", "### Exact duplicates", ""] + bullets(m["dup_list"], lambda p: "- %s = %s" % p)
    if m["bad_list"]:
        L += ["", "### Names Obsidian cannot link", ""] + bullets(m["bad_list"], lambda r: "- %s" % r)
    if m["stale_list"]:
        L += ["", "### Doors to verify", ""] + bullets(m["stale_list"], lambda r: "- %s" % r)
    L += ["", "## History", "",
          "| Date | Notes | Broken (targets) | Orphans | No frontmatter | Contract | .bak | Duplicates | Light | Why |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    L += rows
    L += ["", "### What to do if it is not green", "",
          "1. `.bak` files: move them to `Archives/` (never delete; the brain archives).",
          "2. Broken links: create the missing note as a short stub, or fix the link. Start with the most repeated.",
          "3. Orphans: link each one from its MOC or a related note, or archive it.",
          "4. Contract: run `check_frontmatter.py --all` and fix the notes it lists.",
          "5. Two months in a row not green: ask your AI for a deep review of the vault.", ""]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))


def main(argv=None):
    ap = argparse.ArgumentParser(description="Measure the health of the vault.")
    ap.add_argument("--vault")
    ap.add_argument("--write", action="store_true", help="add today's row to the history note")
    ap.add_argument("--reindex", action="store_true", help="also rebuild the search index")
    args = ap.parse_args(argv)
    vault = bl.find_vault(args.vault)
    vocab = bl.load_vocabulary(vault)
    now = dt.datetime.now()

    m = measure(vault, vocab)
    hist = os.path.join(vault, HISTORY_REL)
    today = now.strftime("%Y-%m-%d")
    rows = [x for x in previous_rows(hist) if not x.startswith("| %s " % today)]
    prev = parse_row(rows[-1]) if rows else None
    color, reasons = light(prev, m)

    print("Brain health %s: %s" % (now.strftime("%Y-%m-%d %H:%M"), color))
    for r in reasons:
        print("  - " + r)
    print("  notes %d | broken %d (%d targets) | orphans %d | no frontmatter %d | contract %.1f%% | "
          ".bak %d | duplicates %d | bad names %d | stale doors %d"
          % (m["notes"], m["broken"], m["broken_targets"], m["orphans"], m["no_fm"], m["contract"],
             m["bak"], m["dups"], m["bad_names"], m["stale"]))

    if args.reindex:
        idx = os.path.join(os.path.dirname(os.path.abspath(__file__)), "brain_index.py")
        r = subprocess.run([sys.executable, idx, "--vault", vault, "--quiet"], capture_output=True, text=True)
        print("  index: " + (r.stdout.strip() or r.stderr.strip()))

    if args.write:
        rows.append(row_text(today, m, color, reasons))
        write_note(hist, rows, m, color, reasons, now)
        print("  history: %s" % HISTORY_REL)
    return 0


if __name__ == "__main__":
    sys.exit(main())
