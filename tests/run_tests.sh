#!/usr/bin/env bash
# End-to-end test of the Second Brain tools on an example vault.
# Usage: bash tests/run_tests.sh   (from the repo root). Needs python3.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"; V="$TMP/Test Brain"
python3 "$ROOT/tests/make_sample_vault.py" "$V"
mkdir -p "$V/.brain/tools"
cp "$ROOT"/skills/second-brain-init/tools/*.py "$ROOT"/skills/second-brain-init/tools/*.sh "$V/.brain/tools/"
cp "$ROOT/skills/second-brain-init/tools/vocabulary.json" "$V/.brain/"
T="$V/.brain/tools"; pass=0; fail=0
ok(){ echo "  PASS $1"; pass=$((pass+1)); }
ko(){ echo "  FAIL $1"; fail=$((fail+1)); }
expect(){ if echo "$2" | grep -q -- "$3"; then ok "$1"; else ko "$1"; echo "$2" | sed 's/^/      /'; fi; }

echo "1. index"
out="$(python3 "$T/brain_index.py")"; expect "indexes the notes (Archives excluded)" "$out" "Indexed 7 notes"
echo "2. search"
out="$(python3 "$T/brain_search.py" cedar)"; expect "finds a word in the body" "$out" "Raised Beds"
out="$(python3 "$T/brain_search.py" decision --type decision)"; expect "type filter" "$out" "1 result"
out="$(python3 "$T/brain_search.py" decision)"; expect "accents do not matter (decision finds Decisión)" "$out" "Compost Basics"
out="$(python3 "$T/brain_search.py" cedar tomatoes)"; expect "falls back to OR" "$out" "(OR)"
out="$(python3 "$T/brain_search.py" "water*" --raw)"; expect "raw FTS prefix" "$out" "Watering"
echo "3. frontmatter contract"
set +e; out="$(python3 "$T/check_frontmatter.py" --all)"; code=$?; set -e
[ "$code" = 1 ] && ok "exit code 1 when notes fail" || ko "exit code ($code)"
expect "unknown type is caught" "$out" "type=book is not in the list"
expect "missing time is caught" "$out" "missing time"
expect "bad tag is caught" "$out" "tag 'Garden Notes'"
expect "bad file name is caught" "$out" "file name has #"
expect "no frontmatter is caught" "$out" "no frontmatter"
set +e; out="$(python3 "$T/check_frontmatter.py" "02 Strategy")"; code=$?; set -e
[ "$code" = 0 ] && ok "a clean folder passes" || { ko "clean folder ($code)"; echo "$out"; }
echo "4. doors"
out="$(python3 "$T/door.py" --new "Garden" --project garden)"; expect "creates a Door" "$out" "Created 09 MOCs/Door, Garden.md"
out="$(python3 "$T/door.py" Garden)"; expect "front page shows section 3" "$out" "## 3. Next steps"
if echo "$out" | grep -q "## 4. How it runs"; then ko "front page must not load section 4"; else ok "front page leaves section 4 out"; fi
out="$(python3 "$T/door.py" Garden 6)"; expect "reads one section" "$out" "Door created"
out="$(python3 "$T/door.py" --new "Huerto" --lang es)"; expect "Spanish Door" "$out" "Puerta, Huerto"
out="$(python3 "$T/door.py")"; expect "lists Doors" "$out" "Huerto"
set +e; out="$(python3 "$T/door.py" --new "Bad|Name" 2>&1)"; set -e; expect "refuses names Obsidian cannot link" "$out" "cannot link"
echo "5. health"
out="$(python3 "$T/brain_health.py" --write)"; expect "red light because of the .bak file" "$out" "RED"
expect "counts broken links (the Door template adds none)" "$out" "broken 1 (1 targets)"
expect "counts duplicates" "$out" "duplicates 1"
[ -f "$V/05 AI System/Brain Health History.md" ] && ok "writes the history note" || ko "history note"
mkdir -p "$V/Archives"; mv "$V/01 Personal Knowledge/Old note.md.bak" "$V/Archives/" 2>/dev/null || true
out="$(python3 "$T/brain_health.py" --write --reindex)"; expect "the .bak is gone from the count" "$out" ".bak 0"
expect "reindex runs" "$out" "index: Indexed"
rows="$(grep -c '^| 20' "$V/05 AI System/Brain Health History.md")"
[ "$rows" = 1 ] && ok "same-day run replaces its row" || ko "rows=$rows"
out="$(python3 "$T/check_frontmatter.py" "$V/05 AI System/Brain Health History.md")"; expect "history note passes the contract" "$out" "0 with problems"
python3 -c "import json,sys;p=sys.argv[1];d=json.load(open(p));d['project']=['kitchen'];json.dump(d,open(p,'w'))" "$V/.brain/vocabulary.json"
out="$(python3 "$T/check_frontmatter.py" "$V/09 MOCs/Door, Garden.md")" || true
expect "a new Door with an unknown project is flagged" "$out" "project=garden is not in the list"
echo "6. schedule script"
bash -n "$T/schedule_health.sh" && ok "schedule_health.sh parses" || ko "schedule_health.sh syntax"
out="$(bash "$T/schedule_health.sh" 2>&1 || true)"; expect "prints its help" "$out" "install"

echo; echo "$pass passed, $fail failed"; echo "(example vault left at $V)"
[ "$fail" = 0 ]
