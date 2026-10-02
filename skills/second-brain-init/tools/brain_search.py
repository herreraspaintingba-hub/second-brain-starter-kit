#!/usr/bin/env python3
"""
brain_search.py: searches your vault through the FTS5 index (bm25 ranking).

Usage:
    python3 brain_search.py "query" [--project X] [--type Y] [--folder "06 Session Logs"]
                            [--since YYYY-MM-DD] [--until YYYY-MM-DD] [--status active]
                            [--title X] [--tag X] [--limit 10] [--json] [--prefix]
                            [--raw] [--sort rank|date]

How the query works:
    - Several words = every word must appear (AND). If nothing matches, it retries
      with OR and tells you.
    - "a phrase in quotes" matches that exact phrase. AND / OR / NOT in capitals work.
    - Accents do not matter: "decision" finds "decision" and "decisi\u00f3n".
    - --prefix turns each word into word* (plan* finds plan, plans, planning).
    - Title, description, aliases and tags weigh more than the body.
    - Recipe for "what did we decide about X?":
          brain_search.py --title "X" --type decision --sort date
    - Recipe for "where did we leave project Y?":
          brain_search.py "Y" --folder "06 Session Logs" --sort date

Filters are substring matches, case-insensitive, and accept a comma list (a,b).
If the index is missing, run brain_index.py first.
"""

import argparse
import datetime as dt
import json
import os
import re
import sqlite3
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brainlib as bl  # noqa: E402

COLUMNS = ["path", "folder", "title", "type", "project", "date", "time",
           "status", "description", "tags", "aliases", "body", "mtime", "words"]
BODY_COL = COLUMNS.index("body")

# bm25 weight per column: title, description and aliases weigh more than the body.
WEIGHTS = {
    "path": 4.0, "folder": 0.5, "title": 10.0, "type": 1.0, "project": 2.0,
    "date": 0.5, "time": 0.0, "status": 0.5, "description": 6.0, "tags": 4.0,
    "aliases": 6.0, "body": 1.0, "mtime": 0.0, "words": 0.0,
}


def nfc(s):
    return unicodedata.normalize("NFC", s)


_TOKEN_RE = re.compile(r'"([^"]*)"|(\S+)')
OPERATORS = {"AND", "OR", "NOT"}


def fts_query(user_query, prefix=False, joiner=" "):
    """Turn the user query into safe FTS5 syntax.
    Each term is double-quoted; phrases are kept; AND/OR/NOT pass through."""
    parts = []
    for phrase, word in _TOKEN_RE.findall(nfc(user_query)):
        if phrase != "" or (phrase == "" and word == ""):
            text = phrase.strip()
            if not text:
                continue
            parts.append('"%s"' % text.replace('"', '""'))
            continue
        if word in OPERATORS:
            parts.append(word)
            continue
        star = word.endswith("*")
        text = word.rstrip("*").strip()
        if not text:
            continue
        # A term with hyphens or dots is treated as a phrase (the tokenizer splits them).
        term = '"%s"' % text.replace('"', '""')
        if star or prefix:
            term += "*"
        parts.append(term)
    if not parts:
        return ""
    # Explicit operators stay; the joiner goes between loose terms.
    out = []
    for i, p in enumerate(parts):
        if i and p not in OPERATORS and out[-1] not in OPERATORS:
            out.append(joiner.strip() or "")
        out.append(p)
    return " ".join(x for x in out if x)


def bare_terms(user_query):
    """Loose terms of the query (no phrases, operators or wildcards)."""
    terms = []
    for phrase, word in _TOKEN_RE.findall(nfc(user_query)):
        if phrase or word in OPERATORS or word.endswith("*") or not word:
            return []
        terms.append(word)
    return terms


def like_filters(column, value):
    """--type a,b -> (lower(type) LIKE ? OR lower(type) LIKE ?), [%a%, %b%]"""
    vals = [v.strip() for v in value.split(",") if v.strip()]
    if not vals:
        return "", []
    clause = " OR ".join("lower(%s) LIKE ?" % column for _ in vals)
    return "(%s)" % clause, ["%" + nfc(v).lower() + "%" for v in vals]


def build_where(args, match_expr):
    where, params = [], []
    if match_expr:
        where.append("notes MATCH ?")
        params.append(match_expr)
    for col, val in (("project", args.project), ("type", args.type),
                     ("folder", args.folder), ("status", args.status)):
        if val:
            clause, p = like_filters(col, val)
            if clause:
                where.append(clause)
                params.extend(p)
    if args.not_folder:
        for v in args.not_folder.split(","):
            if v.strip():
                where.append("lower(folder) NOT LIKE ?")
                params.append("%" + nfc(v.strip()).lower() + "%")
    if args.since:
        where.append("substr(COALESCE(NULLIF(date, ''), mtime), 1, 10) >= ?")
        params.append(args.since)
    if args.until:
        where.append("substr(COALESCE(NULLIF(date, ''), mtime), 1, 10) <= ?")
        params.append(args.until)
    return ("WHERE " + " AND ".join(where)) if where else "", params


def column_constraints(args):
    """--title X and --tag X become title:"X" and tags:"X" inside the MATCH."""
    parts = []
    for col, val in (("title", args.title), ("tags", args.tag)):
        if val:
            parts.append('%s:"%s"' % (col, nfc(val).replace('"', '""')))
    return parts


def run_search(con, query, args, joiner=" "):
    """Return (FTS expression used, rows). With two or more loose terms and rank order,
    notes that contain the exact phrase come first."""
    if args.raw:
        fq = query
    else:
        fq = fts_query(query, prefix=args.prefix, joiner=joiner)
    extra = column_constraints(args)
    match_expr = " ".join([fq] + extra).strip() if (fq or extra) else ""
    where, params = build_where(args, match_expr)
    weights = ", ".join(str(WEIGHTS[c]) for c in COLUMNS)
    order = "score" if args.sort == "rank" else "COALESCE(NULLIF(date, ''), mtime) DESC, score"
    snippet = "snippet(notes, %d, '[', ']', ' ... ', 20)" % BODY_COL if match_expr else "substr(body, 1, 160)"
    sql = """
        SELECT rowid, path, title, type, project, date, time, status, description, tags, mtime, words,
               bm25(notes, %s) AS score, %s AS snip
        FROM notes
        %s
        ORDER BY %s
        LIMIT ?
    """ % (weights, snippet, where, order)

    terms = bare_terms(query) if (query and not args.raw and not args.prefix and joiner == " ") else []
    phrase_first = len(terms) >= 2 and args.sort == "rank"
    if not phrase_first:
        rows = con.execute(sql, params + [args.limit]).fetchall()
    else:
        # 1) notes with the exact phrase, ordered by the phrase bm25
        phrase = '"%s"' % " ".join(terms).replace('"', '""')
        pwhere, pparams = build_where(args, " ".join([phrase] + extra))
        psql = sql.replace(where, pwhere, 1)
        prows = con.execute(psql, pparams + [max(args.limit, 400)]).fetchall()
        seen = {r[0] for r in prows}
        # 2) then the rest of the notes that have every term
        rows = prows + [r for r in con.execute(sql, params + [max(args.limit, 400)]) if r[0] not in seen]
    rows = [r[1:] for r in rows[:args.limit]]
    return match_expr, rows


# ----------------------------------------------------------------------------
# Salida
# ----------------------------------------------------------------------------

def clean_snippet(s):
    s = re.sub(r"\s+", " ", s or "").strip()
    return s


def fmt_row(i, r):
    path, title, typ, project, date, time_, status, desc, tags, mtime, words, score, snip = r
    head = "%2d. %s  %s  %s" % (i, date or mtime[:10] or "no date", (typ or "no type").ljust(14), (project or "").ljust(18))
    line2 = "    %s" % path
    text = desc.strip() if desc and desc.strip() else clean_snippet(snip)
    line3 = "    %s" % (text[:300] if text else "")
    return "\n".join([head.rstrip(), line2, line3])


def meta_line(con):
    try:
        row = con.execute("SELECT indexed_at, notes FROM meta LIMIT 1").fetchone()
    except sqlite3.Error:
        return ""
    if not row:
        return ""
    indexed_at, n = row
    age = ""
    try:
        d = dt.datetime.strptime(indexed_at, "%Y-%m-%d %H:%M:%S")
        hours = (dt.datetime.now() - d).total_seconds() / 3600
        if hours > 24:
            age = "  (%.0f h old; run brain_index.py)" % hours
    except ValueError:
        pass
    return "index of %s, %d notes%s" % (indexed_at, n, age)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Search the brain index.")
    ap.add_argument("query", nargs="*", help="words, \"phrases\", AND/OR/NOT")
    ap.add_argument("--project", help="filter on project (a,b)")
    ap.add_argument("--type", help="filter on type (a,b)")
    ap.add_argument("--folder", help="filter on folder, e.g. '06 Session Logs'")
    ap.add_argument("--status", help="filter on status")
    ap.add_argument("--not-folder", help="exclude folders (a,b)")
    ap.add_argument("--title", help="require this word or phrase in the title")
    ap.add_argument("--tag", help="require this tag")
    ap.add_argument("--since", help="from date YYYY-MM-DD (uses date, or file time if none)")
    ap.add_argument("--until", help="to date YYYY-MM-DD")
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--json", action="store_true", help="JSON output")
    ap.add_argument("--prefix", action="store_true", help="each word as word*")
    ap.add_argument("--raw", action="store_true", help="send the query to FTS5 as is")
    ap.add_argument("--sort", choices=["rank", "date"], default="rank")
    ap.add_argument("--vault")
    ap.add_argument("--db", help="index path (default: <vault>/.brain/brain.sqlite)")
    args = ap.parse_args(argv)

    db = args.db or os.path.join(bl.find_vault(args.vault), ".brain", "brain.sqlite")
    if not os.path.exists(db):
        sys.exit("No index yet at %s. Run: python3 brain_index.py" % db)
    con = sqlite3.connect("file:%s?mode=ro" % db, uri=True)
    query = " ".join(args.query).strip()
    if not query and not any([args.project, args.type, args.folder, args.status,
                              args.since, args.until, args.title, args.tag]):
        ap.error("give a query or at least one filter")

    note = ""
    try:
        fq, rows = run_search(con, query, args)
        if not rows and query and not args.raw and len(_TOKEN_RE.findall(query)) > 1:
            fq, rows = run_search(con, query, args, joiner=" OR ")
            if rows:
                note = "nothing had every word; showing notes with any of them (OR)"
    except sqlite3.OperationalError as e:
        sys.exit("Invalid search (%s). Try without --raw, or put the phrase in quotes." % e)

    meta = meta_line(con)
    if args.json:
        out = []
        for i, r in enumerate(rows, 1):
            path, title, typ, project, date, time_, status, desc, tags, mtime, words, score, snip = r
            out.append({"rank": i, "score": round(score, 3), "path": path, "title": title,
                        "type": typ, "project": project, "date": date, "time": time_,
                        "status": status, "description": desc, "snippet": clean_snippet(snip),
                        "tags": tags, "mtime": mtime, "words": words})
        print(json.dumps({"query": query, "fts": fq, "results": out, "meta": meta, "note": note},
                         ensure_ascii=False, indent=2))
        return
    if not rows:
        print("No results for: %s" % (fq or query))
        print("Try fewer words, --prefix, or fewer filters.")
        print(meta)
        return
    for i, r in enumerate(rows, 1):
        print(fmt_row(i, r))
    print("")
    tail = "%d result%s" % (len(rows), "" if len(rows) == 1 else "s")
    if note:
        tail += "  [%s]" % note
    print(tail + "  |  " + meta)


if __name__ == "__main__":
    main()
