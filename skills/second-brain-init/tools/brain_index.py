#!/usr/bin/env python3
"""
brain_index.py: builds the full-text search index of your vault (SQLite FTS5).

Read-only on your notes. It only writes <vault>/.brain/brain.sqlite.
It rebuilds the whole index every time; a vault of 2,000 notes takes a few seconds.
Standard library only (Python 3.8+ with SQLite FTS5, which macOS, Linux and the
python.org installers all include).

Usage:
    python3 brain_index.py              # build or rebuild the index
    python3 brain_index.py --quiet      # only the final line
    python3 brain_index.py --archives   # also index the Archives folder
"""

import argparse
import datetime as dt
import os
import sqlite3
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brainlib as bl  # noqa: E402

COLUMNS = ["path", "folder", "title", "type", "project", "date", "time",
           "status", "description", "tags", "aliases", "body"]
UNINDEXED = ["mtime", "words"]

SCHEMA = """
CREATE VIRTUAL TABLE notes USING fts5(
    {cols},
    {unindexed},
    tokenize = 'unicode61 remove_diacritics 2'
);
CREATE TABLE meta(indexed_at TEXT, notes INTEGER, vault TEXT, seconds REAL);
""".format(cols=", ".join(COLUMNS), unindexed=", ".join(c + " UNINDEXED" for c in UNINDEXED))


def read_note(full, rel):
    try:
        text = bl.read_text(full)
    except OSError:
        return None
    folder = os.path.dirname(rel)
    stem = os.path.splitext(os.path.basename(rel))[0]
    data, body = bl.parse_frontmatter(text)
    mtime = dt.datetime.fromtimestamp(os.stat(full).st_mtime).strftime("%Y-%m-%d %H:%M")
    return {
        "path": rel,
        "folder": folder,
        "title": bl.derive_title(data, body, stem),
        "type": bl.as_text(bl.pick(data, "type")).lower(),
        "project": bl.as_text(bl.pick(data, "project")),
        "date": bl.norm_date(bl.pick(data, "date"), data.get("updated"), stem),
        "time": bl.as_text(bl.pick(data, "time")),
        "status": bl.as_text(bl.pick(data, "status")).lower(),
        "description": bl.as_text(bl.pick(data, "description"), sep=" "),
        "tags": " ".join(bl.as_list(bl.pick(data, "tags"))),
        "aliases": bl.as_text(bl.pick(data, "aliases"), sep=" | "),
        "body": body,
        "mtime": mtime,
        "words": len(body.split()),
    }


def build(vault, db_path, archives=False, quiet=False):
    t0 = time.perf_counter()
    tmp = db_path + ".tmp"
    for p in (tmp, tmp + "-journal"):
        if os.path.exists(p):
            os.remove(p)
    con = sqlite3.connect(tmp)
    try:
        con.executescript(SCHEMA)
    except sqlite3.OperationalError as e:
        con.close()
        os.remove(tmp)
        sys.exit("This Python's SQLite has no FTS5 (%s). Install Python from python.org, "
                 "or use plain text search instead." % e)
    rows, errors = [], 0
    for full, rel in bl.walk_notes(vault, include_archives=archives):
        note = read_note(full, rel)
        if note is None:
            errors += 1
            continue
        rows.append(tuple(note[c] for c in COLUMNS + UNINDEXED))
    cols = COLUMNS + UNINDEXED
    con.executemany("INSERT INTO notes(%s) VALUES (%s)" % (", ".join(cols), ", ".join("?" for _ in cols)), rows)
    con.execute("INSERT INTO notes(notes) VALUES ('optimize')")
    took = time.perf_counter() - t0
    con.execute("INSERT INTO meta VALUES (?, ?, ?, ?)",
                (dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), len(rows), vault, round(took, 2)))
    con.commit()
    con.close()
    os.replace(tmp, db_path)
    if not quiet:
        print("Vault: %s" % vault)
        print("Index: %s" % db_path)
        if errors:
            print("Could not read %d note(s)" % errors)
    print("Indexed %d notes in %.2f s" % (len(rows), time.perf_counter() - t0))
    return len(rows)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Build the search index of the vault.")
    ap.add_argument("--vault", help="vault folder (default: $BRAIN_VAULT or the folder above .brain/)")
    ap.add_argument("--db", help="index path (default: <vault>/.brain/brain.sqlite)")
    ap.add_argument("--archives", action="store_true", help="also index Archives/")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)
    vault = bl.find_vault(args.vault)
    db = args.db or os.path.join(bl.brain_dir(vault), "brain.sqlite")
    build(vault, db, args.archives, args.quiet)


if __name__ == "__main__":
    main()
