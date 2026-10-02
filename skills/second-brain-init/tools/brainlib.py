#!/usr/bin/env python3
"""
brainlib.py: shared helpers for the Second Brain tools (standard library only).

Where things live, by default:
    <vault>/.brain/tools/        these scripts
    <vault>/.brain/brain.sqlite  the search index
    <vault>/.brain/vocabulary.json  the frontmatter contract
The vault is found in this order: --vault flag, $BRAIN_VAULT, or the folder two
levels above this file (because the tools live in <vault>/.brain/tools/).
"""

import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))

# Equivalent frontmatter keys (English or Spanish), normalized to the left one.
KEY_ALIASES = {
    "project": ["project", "proyecto"],
    "type": ["type", "tipo"],
    "date": ["date", "fecha", "created", "creado"],
    "time": ["time", "hora"],
    "status": ["status", "estado"],
    "description": ["description", "descripcion", "descripci\u00f3n", "summary", "resumen"],
    "tags": ["tags", "tag", "etiquetas"],
    "aliases": ["aliases", "alias"],
    "title": ["title", "titulo", "t\u00edtulo"],
}

# Folders that are never scanned (exact folder name, at any depth).
EXCLUDED_DIRS = {".obsidian", ".git", ".trash", ".brain", "Archives", "Templates"}


def nfc(s):
    return unicodedata.normalize("NFC", s)


def find_vault(cli_value=None):
    """Resolve the vault folder. Exits with a clear message if it cannot."""
    for cand in (cli_value, os.environ.get("BRAIN_VAULT")):
        if cand:
            p = os.path.abspath(os.path.expanduser(cand))
            if os.path.isdir(p):
                return p
            sys.exit("Vault folder not found: %s" % p)
    parent = os.path.dirname(HERE)
    if os.path.basename(parent) == ".brain":
        return os.path.dirname(parent)
    sys.exit("Could not find the vault. Pass --vault PATH or set BRAIN_VAULT.")


def brain_dir(vault):
    d = os.path.join(vault, ".brain")
    os.makedirs(d, exist_ok=True)
    return d


def load_vocabulary(vault, path=None):
    """Load the frontmatter contract. Falls back to the copy next to this script."""
    for cand in (path, os.path.join(vault, ".brain", "vocabulary.json"),
                 os.path.join(HERE, "vocabulary.json")):
        if cand and os.path.exists(cand):
            with open(cand, encoding="utf-8") as fh:
                return json.load(fh)
    sys.exit("vocabulary.json not found (looked in <vault>/.brain/ and next to the tools).")


def walk_notes(vault, include_archives=False):
    """Yield (full_path, relative_path) for every .md note in the vault."""
    skip = set(EXCLUDED_DIRS)
    if include_archives:
        skip.discard("Archives")
    for dp, dns, fns in os.walk(vault):
        dns[:] = sorted(d for d in dns if nfc(d) not in skip and not nfc(d).startswith("."))
        for f in sorted(fns):
            fn = nfc(f)
            if fn.endswith(".md") and not fn.startswith("."):
                full = os.path.join(dp, f)
                yield full, nfc(os.path.relpath(full, vault)).replace(os.sep, "/")


def read_text(full):
    with open(full, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


_KEY_RE = re.compile(r"^(\w[\w\-\. ]*?)\s*:(?:\s+(.*)|\s*)$")  # \w includes accents (título, descripción)
_LIST_ITEM_RE = re.compile(r"^\s*-\s*(.*)$")


def unquote(v):
    """Strip wrapping quotes, wikilink brackets and spaces."""
    if v is None:
        return ""
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in ("'", '"'):
        v = v[1:-1].strip()
    if v.startswith("[[") and v.endswith("]]"):
        v = v[2:-2].strip()
        if "|" in v:
            v = v.split("|", 1)[1].strip()
    return v


def split_inline_list(inner):
    """Split 'a, "b, c", d' respecting quotes and wikilinks."""
    items, buf, quote, depth = [], [], None, 0
    for ch in inner:
        if quote:
            buf.append(ch)
            if ch == quote:
                quote = None
            continue
        if ch in ("'", '"'):
            quote = ch
            buf.append(ch)
            continue
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth = max(0, depth - 1)
        if ch == "," and depth == 0:
            items.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    items.append("".join(buf))
    return [unquote(x) for x in items if unquote(x)]


def parse_frontmatter(text):
    """Return (dict, body). Tolerates inline and block lists, quotes, '>' and '|',
    blank lines inside the block and keys without a value."""
    if text.startswith("﻿"):
        text = text[1:]
    if not text.startswith("---"):
        return {}, text
    lines = text.split("\n")
    if lines[0].strip() != "---":
        return {}, text
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() in ("---", "..."):
            end = i
            break
    if end is None:
        return {}, text
    fm_lines = [l.rstrip("\r") for l in lines[1:end]]
    body = "\n".join(lines[end + 1:])
    data = {}
    i = 0
    n = len(fm_lines)
    while i < n:
        line = fm_lines[i]
        if not line.strip() or line.lstrip().startswith("#") or line[0] in " \t":
            i += 1
            continue
        m = _KEY_RE.match(line)
        if not m:
            i += 1
            continue
        key = m.group(1).strip().lower()
        val = (m.group(2) or "").strip()
        if val == "":
            # block list, nested map, or empty key
            items = []
            j = i + 1
            while j < n:
                l2 = fm_lines[j]
                if not l2.strip():
                    j += 1
                    continue
                lm = _LIST_ITEM_RE.match(l2)
                if lm:
                    items.append(unquote(lm.group(1)))
                    j += 1
                elif l2[0] in " \t":
                    items.append(l2.strip())
                    j += 1
                else:
                    break
            data[key] = [x for x in items if x] if items else ""
            i = j
            continue
        if val in (">", "|", ">-", "|-", ">+", "|+"):
            parts = []
            j = i + 1
            while j < n and (not fm_lines[j].strip() or fm_lines[j][0] in " \t"):
                parts.append(fm_lines[j].strip())
                j += 1
            joiner = " " if val.startswith(">") else "\n"
            data[key] = joiner.join(p for p in parts if p).strip()
            i = j
            continue
        if val.startswith("[") and val.endswith("]") and not val.startswith("[["):
            data[key] = split_inline_list(val[1:-1])
            i += 1
            continue
        # scalar, maybe continued on indented lines
        j = i + 1
        extra = []
        while j < n and fm_lines[j].strip() and fm_lines[j][0] in " \t" and not _LIST_ITEM_RE.match(fm_lines[j]):
            extra.append(fm_lines[j].strip())
            j += 1
        if extra:
            val = val + " " + " ".join(extra)
        if val[:1] not in ("'", '"') and " #" in val:
            val = val.split(" #", 1)[0].rstrip()  # YAML comment after an unquoted value
        data[key] = unquote(val)
        i = j
    return data, body


def pick(data, canonical):
    """Take the first non-empty value among equivalent keys."""
    for k in KEY_ALIASES.get(canonical, [canonical]):
        v = data.get(k)
        if v not in (None, "", []):
            return v
    return ""


def as_text(v, sep=", "):
    if isinstance(v, list):
        return sep.join(str(x).strip() for x in v if str(x).strip())
    return str(v).strip()


def as_list(v):
    if isinstance(v, list):
        out = []
        for x in v:
            out.extend(as_list(x))
        return out
    s = str(v).strip()
    if not s:
        return []
    if s.startswith("[") and s.endswith("]"):
        return split_inline_list(s[1:-1])
    # "a, b" or "a b" or "#a #b"
    parts = re.split(r"[,\s]+", s) if ("," in s or s.startswith("#")) else [s]
    return [p.strip().lstrip("#") for p in parts if p.strip().lstrip("#")]


_DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")


def norm_date(*cands):
    for c in cands:
        s = as_text(c)
        m = _DATE_RE.search(s)
        if m:
            return m.group(1)
    return ""


_H1_RE = re.compile(r"^\s*#\s+(.+?)\s*$", re.M)


def derive_title(data, body, stem):
    t = as_text(pick(data, "title"))
    if t:
        return t
    m = _H1_RE.search(body[:4000])
    if m:
        return m.group(1).strip()
    return stem




_WIKILINK_RE = re.compile(r"(!?)\[\[([^\]\n]+?)\]\]")
_CODE_RE = re.compile(r"```.*?```|~~~.*?~~~|`[^`\n]*`", re.S)
# Link targets with these endings are attachments, not notes. Anything else with a dot
# ("Dr. Smith", "v1.2 plan") is a note name.
ATTACHMENT_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp", ".heic", ".pdf",
                  ".canvas", ".base", ".excalidraw", ".mp3", ".m4a", ".wav", ".ogg", ".mp4",
                  ".mov", ".webm", ".csv", ".xlsx", ".docx", ".pptx", ".zip", ".txt", ".json"}


def wikilinks(body):
    """Return the link targets in a note body (no embeds of non-notes, no code)."""
    body = _CODE_RE.sub("", body)
    out = []
    for bang, inner in _WIKILINK_RE.findall(body):
        target = inner.split("|", 1)[0].split("#", 1)[0].split("^", 1)[0].strip()
        if not target:
            continue
        ext = os.path.splitext(target)[1].lower()
        if ext in ATTACHMENT_EXT:
            continue  # images, PDFs, canvases: not notes
        out.append(nfc(target))
    return out


def note_key(name):
    """How Obsidian matches a link to a file: by basename, case-insensitive."""
    base = os.path.basename(name)
    if base.lower().endswith(".md"):
        base = base[:-3]
    return nfc(base).lower()


FORBIDDEN_NAME_CHARS = set('#^[]|:')


def safe_date(value):
    """A YYYY-MM-DD string as a date, or None if it is missing or impossible (2026-02-30)."""
    import datetime as _dt
    m = re.search(r"\d{4}-\d{2}-\d{2}", str(value or ""))
    if not m:
        return None
    try:
        return _dt.date.fromisoformat(m.group(0))
    except ValueError:
        return None


def is_backup_name(name):
    """note.md.bak, note.bak, note.bak.md, .bak-2026: yes. J.Baker.md: no."""
    return re.search(r"\.bak(\.|-|$)", name, re.I) is not None or name.lower().startswith(".bak")

