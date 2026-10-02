#!/usr/bin/env python3
"""
check_frontmatter.py: checks notes against the frontmatter contract (vocabulary.json).

save-to-obsidian, session-checkpoint, project-door and close-session run it before
they call a note saved. You can run it by hand on one note, a folder, or the vault.

What it checks:
    - the required keys are there (title, type, date, description, tags, status)
    - type, status (and project, when your list has projects) are in the closed lists
    - date looks like YYYY-MM-DD, and time looks like HH:MM when it is required
    - tags are lowercase with no spaces or leading #
    - the file name has none of the characters Obsidian cannot link: # ^ [ ] | :

Usage:
    python3 check_frontmatter.py "<note.md>"           # one note
    python3 check_frontmatter.py "06 Session Logs"     # a folder (relative to the vault or absolute)
    python3 check_frontmatter.py --all                 # the whole vault
    python3 check_frontmatter.py --all --summary       # only the final count

Exit code: 0 all good, 1 some note failed, 3 a path does not exist.
Standard library only.
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brainlib as bl  # noqa: E402

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TIME_RE = re.compile(r"^\d{1,2}:\d{2}(\s*[A-Za-z]{2,5})?$")
TAG_RE = re.compile(r"^[a-z0-9][a-z0-9/_\-]*$")


def hash_tags(text):
    """True if a tag starts with # in the raw frontmatter. In YAML that is a comment,
    so Obsidian sees no tag at all, even though a tolerant reader would accept it."""
    if not text.lstrip("\ufeff").startswith("---"):
        return False
    block = text.lstrip("\ufeff").split("\n")[1:]
    in_tags = False
    for line in block:
        if line.strip() in ("---", "..."):
            break
        if re.match(r"^tags\s*:", line):
            in_tags = True
            if re.match(r"^tags\s*:\s*#", line) or re.search(r"[\[,]\s*#", line):
                return True
            continue
        if in_tags and re.match(r"^\s*-\s*#", line):
            return True
        if line[:1] not in (" ", "\t", "-"):
            in_tags = False
    return False


def validate(name, data, vocab):
    """Return a list of human-readable problems for one note."""
    errors = []
    bad = sorted(set(name) & bl.FORBIDDEN_NAME_CHARS)
    if bad:
        errors.append("file name has %s (Obsidian cannot link it)" % " ".join(bad))
    if not data:
        return errors + ["no frontmatter"]
    for key in vocab.get("required_keys", []):
        if bl.pick(data, key) in ("", [], None):
            errors.append("missing %s" % key)
    for key in ("type", "status"):
        val = bl.as_text(bl.pick(data, key)).lower()
        allowed = [x.lower() for x in vocab.get(key, [])]
        if val and allowed and val not in allowed:
            errors.append("%s=%s is not in the list (%s)" % (key, val, ", ".join(allowed)))
    projects = [x.lower() for x in vocab.get("project", [])]
    proj = bl.as_text(bl.pick(data, "project")).lower()
    if vocab.get("project_required") and not proj:
        errors.append("missing project")
    if proj and projects and proj not in projects:
        errors.append("project=%s is not in the list (add it to vocabulary.json if it is new)" % proj)
    date = bl.as_text(bl.pick(data, "date"))
    if date and not DATE_RE.match(date):
        errors.append("date=%s should be YYYY-MM-DD" % date)
    since = vocab.get("time_required_since")
    time_val = bl.as_text(bl.pick(data, "time"))
    if since and DATE_RE.match(date or "") and date >= since and not time_val:
        errors.append("missing time (HH:MM, the real time from the clock)")
    if time_val and not TIME_RE.match(time_val):
        errors.append("time=%s should be HH:MM" % time_val)
    for tag in bl.as_list(bl.pick(data, "tags")):
        if not TAG_RE.match(tag):
            errors.append("tag '%s' should be lowercase, no spaces, no accents" % tag)
    return errors


def targets(paths, vault, whole):
    if whole:
        for full, rel in bl.walk_notes(vault):
            yield full, rel
        return
    for p in paths:
        cand = p if os.path.isabs(p) else (p if os.path.exists(p) else os.path.join(vault, p))
        if not os.path.exists(cand):
            print("Does not exist: %s" % p, file=sys.stderr)
            sys.exit(3)
        if os.path.isfile(cand):
            yield cand, os.path.relpath(cand, vault)
        else:
            for dp, dns, fns in os.walk(cand):
                dns[:] = sorted(d for d in dns if not d.startswith(".") and d not in bl.EXCLUDED_DIRS)
                for f in sorted(fns):
                    if f.endswith(".md"):
                        full = os.path.join(dp, f)
                        yield full, os.path.relpath(full, vault)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Check notes against the frontmatter contract.")
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--all", action="store_true", help="check the whole vault")
    ap.add_argument("--vault")
    ap.add_argument("--vocabulary", help="path to a vocabulary.json (default: <vault>/.brain/)")
    ap.add_argument("--summary", action="store_true", help="only print the final count")
    args = ap.parse_args(argv)
    if not args.paths and not args.all:
        ap.error("give a note, a folder, or --all")
    vault = bl.find_vault(args.vault)
    vocab = bl.load_vocabulary(vault, args.vocabulary)
    total = failed = 0
    for full, rel in targets(args.paths, vault, args.all):
        total += 1
        text = bl.read_text(full)
        data, _ = bl.parse_frontmatter(text)
        errs = validate(bl.nfc(os.path.basename(full))[:-3], data, vocab)
        if hash_tags(text):
            errs.append("a tag starts with # (in the properties that hides it; write it without #)")
        if errs:
            failed += 1
            if not args.summary:
                print("%s: %s" % (rel, " | ".join(errs)))
    print("%d note%s checked, %d with problems" % (total, "" if total == 1 else "s", failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
