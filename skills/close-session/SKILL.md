---
name: close-session
description: >
  The ritual that closes a working session so nothing is lost: checkpoint the state,
  rewrite the project Door, save knowledge and the session log, refresh the search
  index, and (if the vault is a git repo) commit it safely. Use it whenever the user
  wants to stop, pause or wrap up: "close the session", "let's wrap up", "we'll continue
  tomorrow", "save everything", "blindemos", "cierra la sesión", "continuamos mañana",
  "ya acabamos, guardemos todo". Bilingual EN+ES.
kit: Second Brain Starter Kit
version: 2.0.0
language: en+es
---

# Close Session: shut the door properly

A session that ends without a close leaves the next one guessing. This ritual takes a
few minutes and makes the next start take seconds.

**The rule that matters:** all steps describe **the same moment**. Freeze the state
first (decide what is true now), then write it everywhere. Do not keep working between
steps, or the checkpoint, the Door and the log will tell three different stories.

## The steps, in order

### 1. Checkpoint (context)

Run `session-checkpoint` for the active project, so the rolling state is current.
Skip it if the session was short.

### 2. The project Door

If the session worked on a project that has a Door, rewrite it with `project-door`
("Updating a Door"): sections 1 to 3 rewritten to what is true now, one line on top of
section 6, `verified:` set to today. If the project has no Door and will take more
sessions, offer to create one.

### 3. Knowledge (the brain)

Run `save-to-obsidian`: the nuggets worth keeping and the session log, linked into the
graph, frontmatter validated. Link the session log to the Door.

### 4. The search index

```bash
python3 "{{VAULT_PATH}}/.brain/tools/brain_index.py" --quiet
```

### 5. The vault in git (only if it is a repo)

Skip this step entirely if the vault is not a git repository
(`git -C "{{VAULT_PATH}}" rev-parse 2>/dev/null` fails). If it is:

```bash
cd "{{VAULT_PATH}}"
git pull --ff-only          # bring changes from another device, straight line only
git add -A
git commit -m "Close session YYYY-MM-DD HH:MM: <short title>"
git push                    # only if the user has a remote and wants it pushed
```

- **If `pull --ff-only` refuses** (the histories split), stop and tell the user. Never
  merge blindly: an automatic merge inside notes can scatter conflict markers through
  them. The user decides how to reconcile.
- This step is the **only** one that commits the vault. Turn off any plugin that
  commits on its own, so two committers never collide.
- A vault that was not pushed is not backed up off the machine. Say so if there is
  no remote.

### 6. Tell the user, in five lines or fewer

```
Session closed:
- Checkpoint: Active Session State, Garden (updated)
- Door: Door, Garden (verified today; next step: order the cedar boards)
- Brain: 2 notes + session log, all pass the frontmatter check
- Index: rebuilt, 412 notes
- Git: committed and pushed / not a repo / stopped, needs you (why)
```

In Spanish when that is the user's language.

## What this skill never does

- It never deletes anything (old notes go to `Archives/`).
- It never merges diverged git histories on its own.
- It never invents numbers to fill the Door.
- It never pushes to a remote the user did not set up.

## Changelog

- **2.0.0 (2026-10-02):** New skill. Frozen-state rule, Door update, index refresh,
  optional git commit with fast-forward-only pulls.
