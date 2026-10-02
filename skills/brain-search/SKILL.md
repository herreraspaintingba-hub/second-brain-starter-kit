---
name: brain-search
description: >
  Searches the user's second brain (their Obsidian vault) BEFORE answering or asking,
  with a local full-text index ranked by relevance. Use it whenever the answer might
  already be in the vault: "what did we decide about X?", "where did we leave Y?",
  "have we done this before?", "find my notes on Z", "search my brain", "¿qué decidimos
  sobre X?", "¿dónde quedó Y?", "¿ya hicimos esto?", "busca en mi cerebro", and also on
  your own initiative before asking the user for a fact (a name, a number, a past
  choice) that the vault may hold. Bilingual EN+ES.
kit: Second Brain Starter Kit
version: 2.0.0
language: en+es
---

# Brain Search: look in the brain before you ask

## The rule: retrieval first

A fact about the user's life or work (a decision, a price, a person, a date, how
something was done) is **searched before it is asked**. The order:

1. `brain_search.py` (this skill).
2. The project Door, if the question is about a project (`project-door`).
3. A plain text search of the vault, for an exact number or phrase.
4. Only then, ask the user. If they answer with a durable fact, offer to save it.

Asking the user something their own brain already knows wastes their time and teaches
them the brain is not worth feeding.

---

## How it works

The kit keeps a search index of the whole vault at `{{VAULT_PATH}}/.brain/brain.sqlite`
(SQLite FTS5, built with only the Python standard library). It ranks by relevance
(bm25): a word in the **title, description, aliases or tags weighs more** than the same
word in the body. Accents do not matter.

```bash
T="{{VAULT_PATH}}/.brain/tools"
python3 "$T/brain_search.py" "raised beds"                       # every word must appear
python3 "$T/brain_search.py" "\"raised beds\""                   # exact phrase
python3 "$T/brain_search.py" compost --prefix                    # compost* (composting, composts)
python3 "$T/brain_search.py" budget --type decision --sort date  # newest decision first
python3 "$T/brain_search.py" garden --folder "06 Session Logs" --since 2026-09-01
python3 "$T/brain_search.py" "pricing" --project kitchen --limit 5
python3 "$T/brain_search.py" roof --json                         # for further processing
```

If nothing has every word, it retries with any of them and says so.

### Recipes

| The user asks | Run |
|---|---|
| "What did we decide about X?" | `--title "X" --type decision --sort date` (newest first; if empty, drop `--title`) |
| "Where did we leave project Y?" | `project-door` first; then `"Y" --folder "06 Session Logs" --sort date` |
| "Have we done this before?" | the 2 or 3 key words, then `--type session,lesson` |
| "What do I know about person Z?" | `"Z" --type person`, then without the filter |
| "Find that article about W" | `"W" --type reference` |

### Filters

`--type`, `--project`, `--folder`, `--status`, `--not-folder`, `--title`, `--tag`,
`--since`, `--until`, `--limit`, `--sort rank|date`, `--prefix`, `--raw` (FTS5 syntax
as is, e.g. `title:budget`, `NEAR(a b)`). Filters are case-insensitive substring matches
and accept a comma list.

---

## Keeping the index fresh

The index is rebuilt in seconds, whole, every time:

```bash
python3 "{{VAULT_PATH}}/.brain/tools/brain_index.py"
```

It runs at the end of `save-to-obsidian` and `close-session`, and every month with the
health check. If a search says the index is more than 24 hours old, rebuild it first.

---

## Without Python

If `python3` is not available (or the index cannot be built), fall back to a plain text
search of the vault with the host's file search (Grep/Glob, or `grep -ril "word"`),
starting with file names and the `description:` lines, then the bodies. Same order,
less ranking.

---

## How to answer

- Answer from what the notes say, and **name the note** each fact came from as a
  `[[link]]`, so the user can open it.
- Read the top 1 to 3 notes before answering; the snippet is a pointer, not the answer.
- If two notes disagree, say so and show both, newest first. Do not pick one silently.
- If nothing is found, say it plainly ("nothing in the brain about X"), then ask.
- Show the work in one line: "Searched the brain for X: 3 notes, used the first two."

## Changelog

- **2.0.0 (2026-10-02):** New skill. Local FTS5 index, retrieval-first rule, recipes.
