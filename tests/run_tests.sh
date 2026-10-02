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

echo "7. regressions from the code review"
FM='---\ntitle: X\ntype: note\ndate: 2026-09-01\ntime: "09:00"\ndescription: "d"\ntags: [t]\nstatus: active\n---\n'
printf -- "---\ntitle: 'Door, Typo'\ntype: door\ndate: 2026-09-01\ntime: \"09:00\"\nverified: 2026-02-30\ndescription: d\ntags: [door]\nstatus: active\n---\n## 1. Current state\n" > "$V/09 MOCs/Door, Typo.md"
out="$(python3 "$T/brain_health.py" 2>&1)"; expect "impossible verified date does not crash health" "$out" "stale doors"
out="$(python3 "$T/door.py" 2>&1)"; expect "impossible verified date does not crash door.py" "$out" "invalid date"
mkdir -p "$V/01 Personal Knowledge/People"
printf -- "$FM" > "$V/01 Personal Knowledge/People/Dr. Smith.md"
printf -- "$FM\nSee [[Dr. Smith]] and [[v1.2 plan]].\n~~~\n[[InTilde]]\n~~~\n" > "$V/03 Ideas & Notes/Dots.md"
printf -- "$FM" > "$V/01 Personal Knowledge/People/J.Baker.md"
out="$(python3 "$T/brain_health.py")"; expect "a name with a dot is a note, and a missing one is broken" "$out" "broken 2 (2 targets)"
expect "J.Baker.md is not a backup file" "$out" ".bak 0"
printf -- "---\ntítulo: Hola\ntype: note\ndate: 2026-09-01\ntime: \"09:00\"\ndescripción: d\ntags: [t]\nstatus: active # done soon\n---\n" > "$V/03 Ideas & Notes/Acentos.md"
out="$(python3 "$T/check_frontmatter.py" "03 Ideas & Notes/Acentos.md")"; expect "accented Spanish keys and a trailing comment pass" "$out" "0 with problems"
printf -- "---\ntitle: H\ntype: note\ndate: 2026-09-01\ntime: \"09:00\"\ndescription: d\ntags: #garden\nstatus: active\n---\n" > "$V/03 Ideas & Notes/Hash.md"
out="$(python3 "$T/check_frontmatter.py" "03 Ideas & Notes/Hash.md" || true)"; expect "a tag written with # is flagged" "$out" "starts with #"
H="$V/05 AI System/Brain Health History.md"
python3 "$T/brain_health.py" --write >/dev/null; echo "My own comment, keep me." >> "$H"
python3 "$T/brain_health.py" --write >/dev/null
grep -q "My own comment, keep me." "$H" && ok "the history note keeps the user's own words" || ko "history note lost the user's words"
mkdir -p "$V/04 Learning/Órdenes"; printf -- "$FM\ncedar order\n" > "$V/04 Learning/Órdenes/Pedido.md"
python3 "$T/brain_index.py" --quiet >/dev/null
out="$(python3 "$T/brain_search.py" cedar --folder "Órdenes")"; expect "folder filter with an accented capital" "$out" "Pedido"
out="$(python3 "$T/brain_search.py" cedar tomatoes --title Beds 2>&1 || true)"; expect "--title with the OR fallback is a valid search" "$out" "Raised Beds"
if echo "$out" | grep -q "Watering\|Invalid search"; then ko "--title must hold in the OR fallback"; else ok "--title holds in the OR fallback"; fi
out="$(cd /tmp && bash "$ROOT/skills/second-brain-init/tools/schedule_health.sh" run 2>&1 || true)"; expect "schedule script refuses to run outside a vault" "$out" "Run this from the copy inside your vault"
[ ! -e "$ROOT/skills/.brain" ] && ok "nothing was written into the repo" || ko "schedule script wrote into the repo"
out="$(python3 "$T/door.py" --new "Ana/Luis" 2>&1 || true)"; expect "door name with a slash is refused" "$out" "cannot link"
out="$(python3 "$T/door.py" --new "   " 2>&1 || true)"; expect "empty door name is refused" "$out" "Give the project a name"
python3 "$T/door.py" --new 'The "Big" Move' >/dev/null
out="$(python3 "$T/door.py" "Big" 2>&1)"; expect "a door name with quotes is created and readable" "$out" "Door, The \"Big\" Move"
grep -q "^title: 'Door, The \"Big\" Move'$" "$V/09 MOCs/Door, The \"Big\" Move.md" && ok "its title is valid YAML" || ko "title YAML"

echo; echo "$pass passed, $fail failed"; echo "(example vault left at $V)"
[ "$fail" = 0 ]
