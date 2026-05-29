#!/usr/bin/env bash
# ============================================================================
#  Second Brain Starter Kit — one-command installer
#
#  Quickest way (downloads the kit and installs it):
#     curl -fsSL https://raw.githubusercontent.com/herreraspaintingba-hub/second-brain-starter-kit/main/install.sh | bash
#
#  Or, from inside a clone of this repo:
#     bash install.sh
#
#  Choose a different AI host (default auto-detects, falls back to claude):
#     HOST=codex bash install.sh         # claude | codex | gemini
#
#  After install, open your AI assistant and say:
#     "Set up my second brain"  /  "Configura mi segundo cerebro"
# ============================================================================
set -euo pipefail

REPO_URL="https://github.com/herreraspaintingba-hub/second-brain-starter-kit.git"

say(){ printf '%s\n' "$1"; }
hr(){ say "------------------------------------------------------------"; }

hr
say "  Second Brain Starter Kit — installer"
hr

# --- 1. Locate the kit's skills/ folder (local clone, or clone a fresh copy) --
if [ -d "skills" ] && [ -f "skills/README.md" ]; then
  SRC="$(pwd)/skills"
  say "Using the skills/ folder in the current directory."
else
  command -v git >/dev/null 2>&1 || { say "ERROR: git is required (or run this from inside a clone of the repo)."; exit 1; }
  TMP="$(mktemp -d)"
  say "Downloading the kit..."
  git clone --depth 1 "$REPO_URL" "$TMP/kit" >/dev/null 2>&1 || { say "ERROR: download failed. Check your internet connection."; exit 1; }
  SRC="$TMP/kit/skills"
fi

# --- 2. Decide which AI host's skills directory to install into ---------------
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
say "Tip: re-run with HOST=claude|codex|gemini to target a different assistant."
say ""

# --- 3. Copy the four skills into place ---------------------------------------
mkdir -p "$DEST"
cp -R "$SRC"/. "$DEST"/

hr
say "  Installed. Your second brain is ready to set up."
hr
say ""
say "Next step -> open your AI assistant (Claude, Cowork, Codex, Gemini...) and say:"
say "   English:  \"Set up my second brain\""
say "   Espanol:  \"Configura mi segundo cerebro\""
say ""
say "It will ask 6 quick questions and build your vault. Full guide: see the PDF manual"
say "(English + Espanol editions) in this repo."
