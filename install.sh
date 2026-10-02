#!/usr/bin/env bash
# ============================================================================
#  Second Brain Starter Kit v2.0: one-command installer
#
#  Quickest way (downloads the kit and installs it):
#     curl -fsSL https://raw.githubusercontent.com/herreraspaintingba-hub/second-brain-starter-kit/main/install.sh | bash
#
#  Or, from inside a clone of this repo:
#     bash install.sh
#
#  Choose an AI host (default: auto-detect, falls back to claude):
#     HOST=codex bash install.sh         # claude | codex | gemini
#
#  After installing, open your AI assistant and say:
#     "Set up my second brain"  /  "Configura mi segundo cerebro"
#  If you already had v1:
#     "Upgrade my brain to v2"  /  "Actualiza mi cerebro a la v2"
# ============================================================================
set -euo pipefail

REPO_URL="https://github.com/herreraspaintingba-hub/second-brain-starter-kit.git"
SKILLS="second-brain-init obsidian-power-user save-to-obsidian project-advisor brain-search project-door session-checkpoint close-session brain-health"

say(){ printf '%s\n' "$1"; }
hr(){ say "------------------------------------------------------------"; }

hr
say "  Second Brain Starter Kit v2.0: installer"
hr

# 1. Find the kit's skills/ folder (this clone, or download a fresh copy)
if [ -d "skills/second-brain-init" ] && [ -f "skills/README.md" ]; then
  SRC="$(pwd)/skills"
  say "Using the skills/ folder in this directory."
else
  command -v git >/dev/null 2>&1 || { say "ERROR: git is required (or run this from inside a clone of the repo)."; exit 1; }
  TMP="$(mktemp -d)"
  say "Downloading the kit..."
  git clone --depth 1 "$REPO_URL" "$TMP/kit" >/dev/null 2>&1 || { say "ERROR: download failed. Check your internet connection."; exit 1; }
  SRC="$TMP/kit/skills"
fi

# 2. Pick the AI host's skills folder
choose_host(){
  if [ -n "${HOST:-}" ]; then printf '%s' "$HOST"; return; fi
  for h in claude codex gemini; do
    [ -d "$HOME/.$h" ] && { printf '%s' "$h"; return; }
  done
  printf '%s' "claude"
}
HOST_CHOICE="$(choose_host)"
DEST="$HOME/.$HOST_CHOICE/skills"

say ""
say "Installing into:  $DEST   (host: $HOST_CHOICE)"
say "Tip: run again with HOST=claude|codex|gemini to target another assistant."
say ""

# 3. Copy the nine skills. An older copy of a kit skill is moved aside, never deleted.
mkdir -p "$DEST"
STAMP="$(date +%Y%m%d-%H%M%S)"
for s in $SKILLS; do
  [ -d "$SRC/$s" ] || { say "ERROR: $s is missing from the kit download."; exit 1; }
  if [ -d "$DEST/$s" ]; then
    mkdir -p "$DEST/.kit-previous/$STAMP"
    mv "$DEST/$s" "$DEST/.kit-previous/$STAMP/$s"
  fi
  cp -R "$SRC/$s" "$DEST/$s"
  say "  installed $s"
done
chmod +x "$DEST/second-brain-init/tools/"*.py "$DEST/second-brain-init/tools/"*.sh 2>/dev/null || true
[ -d "$DEST/.kit-previous/$STAMP" ] && say "  (your previous copies are in $DEST/.kit-previous/$STAMP)"

# 4. Python is optional, but it unlocks search, the frontmatter check and the health check
say ""
if command -v python3 >/dev/null 2>&1 && python3 -c "import sqlite3; sqlite3.connect(':memory:').execute('create virtual table t using fts5(x)')" >/dev/null 2>&1; then
  say "Python 3 with full-text search: found. All tools will work."
else
  say "Python 3 (with SQLite FTS5) was not found. The skills still work with plain text"
  say "search. Install Python later (python.org) to unlock search and the health check."
fi

hr
say "  Installed. Your second brain is ready to set up."
hr
say ""
say "Next: open your AI assistant (Claude, Cowork, Codex, Gemini...) and say:"
say "   English:  \"Set up my second brain\""
say "   Espanol:  \"Configura mi segundo cerebro\""
say ""
say "Had v1 already? Say \"Upgrade my brain to v2\" / \"Actualiza mi cerebro a la v2\"."
say "Full guide: the PDF manuals (English and Espanol) in this repo."
