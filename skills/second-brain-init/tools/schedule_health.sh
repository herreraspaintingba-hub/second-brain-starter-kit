#!/usr/bin/env bash
# ============================================================================
#  schedule_health.sh: runs the brain health check by itself, once a month.
#
#  On the 1st of every month at 07:00 it runs:
#     brain_health.py --write --reindex
#  which adds a row to "05 AI System/Brain Health History.md" and rebuilds the
#  search index. Output goes to <vault>/.brain/health.log.
#
#  Usage (from anywhere):
#     bash schedule_health.sh install     # turn the monthly check on
#     bash schedule_health.sh remove      # turn it off
#     bash schedule_health.sh status      # is it on?
#     bash schedule_health.sh run         # run it once now, the same way the schedule does
#
#  macOS uses launchd (~/Library/LaunchAgents). Linux uses your crontab.
#  Windows: see the schtasks line this script prints.
# ============================================================================
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT="${BRAIN_VAULT:-$(cd "$HERE/../.." && pwd)}"
PY="$(command -v python3 || true)"
LOG="$VAULT/.brain/health.log"
LABEL="com.secondbrain.health"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
CRON_TAG="# second-brain-health"

[ -n "$PY" ] || { echo "python3 is not installed, so the health check cannot be scheduled."; exit 1; }
[ -f "$HERE/brain_health.py" ] || { echo "brain_health.py not found next to this script."; exit 1; }

cmd_line() { printf '"%s" "%s/brain_health.py" --vault "%s" --write --reindex >> "%s" 2>&1' "$PY" "$HERE" "$VAULT" "$LOG"; }

xml_escape() { sed -e 's/&/\&amp;/g' -e 's/</\&lt;/g' -e 's/>/\&gt;/g'; }

install_mac() {
  mkdir -p "$HOME/Library/LaunchAgents" "$VAULT/.brain"
  local py hp vt lg
  py="$(printf '%s' "$PY" | xml_escape)"; hp="$(printf '%s' "$HERE/brain_health.py" | xml_escape)"
  vt="$(printf '%s' "$VAULT" | xml_escape)"; lg="$(printf '%s' "$LOG" | xml_escape)"
  cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>$LABEL</string>
  <key>ProgramArguments</key>
  <array>
    <string>$py</string><string>$hp</string>
    <string>--vault</string><string>$vt</string>
    <string>--write</string><string>--reindex</string>
  </array>
  <key>StartCalendarInterval</key>
  <dict><key>Day</key><integer>1</integer><key>Hour</key><integer>7</integer><key>Minute</key><integer>0</integer></dict>
  <key>StandardOutPath</key><string>$lg</string>
  <key>StandardErrorPath</key><string>$lg</string>
</dict>
</plist>
EOF
  launchctl unload "$PLIST" >/dev/null 2>&1 || true
  launchctl load "$PLIST"
  echo "On. The health check runs on the 1st of every month at 07:00 (if the Mac is asleep, it runs when it wakes)."
  case "$VAULT" in
    *"Mobile Documents"*|*"CloudStorage"*)
      echo "Your vault is in iCloud or another cloud drive. If the first run logs 'Operation not permitted',"
      echo "give python3 Full Disk Access: System Settings > Privacy & Security > Full Disk Access." ;;
  esac
}

install_linux() {
  command -v crontab >/dev/null 2>&1 || { echo "crontab is not available on this system."; exit 1; }
  mkdir -p "$VAULT/.brain"
  local line; line="0 7 1 * * $(cmd_line | sed 's/%/\\%/g') $CRON_TAG"   # cron treats % as a newline
  { crontab -l 2>/dev/null | grep -v "$CRON_TAG" || true; echo "$line"; } | crontab -
  echo "On. The health check runs on the 1st of every month at 07:00 (cron)."
}

case "${1:-}" in
  install)
    case "$(uname -s)" in
      Darwin) install_mac ;;
      Linux)  install_linux ;;
      *) echo "On Windows, run this once in a terminal:"
         echo "  schtasks /Create /SC MONTHLY /D 1 /ST 07:00 /TN SecondBrainHealth /TR \"python \\\"$HERE/brain_health.py\\\" --vault \\\"$VAULT\\\" --write --reindex\"" ;;
    esac ;;
  remove)
    case "$(uname -s)" in
      Darwin) launchctl unload "$PLIST" >/dev/null 2>&1 || true; [ -f "$PLIST" ] && mv "$PLIST" "$PLIST.off"; echo "Off." ;;
      Linux)  { crontab -l 2>/dev/null | grep -v "$CRON_TAG" || true; } | crontab -; echo "Off." ;;
      *) echo "On Windows: schtasks /Delete /TN SecondBrainHealth /F" ;;
    esac ;;
  status)
    case "$(uname -s)" in
      Darwin) if launchctl list 2>/dev/null | grep -q "$LABEL"; then echo "On (launchd)."; else echo "Off."; fi ;;
      Linux)  if crontab -l 2>/dev/null | grep -q "$CRON_TAG"; then echo "On (cron)."; else echo "Off."; fi ;;
      *) echo "On Windows: schtasks /Query /TN SecondBrainHealth" ;;
    esac
    [ -f "$LOG" ] && { echo "Last log lines:"; tail -n 5 "$LOG"; } || true ;;
  run)
    mkdir -p "$VAULT/.brain"
    "$PY" "$HERE/brain_health.py" --vault "$VAULT" --write --reindex | tee -a "$LOG" ;;
  *)
    sed -n '2,18p' "$0" | sed 's/^#  \{0,1\}//' ; exit 1 ;;
esac
