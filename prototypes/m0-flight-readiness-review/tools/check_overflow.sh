#!/bin/sh
# Measure horizontal overflow of the review surface across widths.
#
# Loads tests/overflow.html in headless Chrome, which embeds the surface in a
# sized iframe and reports any element whose right edge escapes the viewport
# without being inside a scrollable container. Local file access only; no
# network, no sign-in, throwaway profile.
#
# Exit status is 0 only when every width and route passes.

set -eu

HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/.." && pwd)
CHROME=${CHROME:-"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"}
WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT

if [ ! -x "$CHROME" ]; then
  echo "Chrome not found at: $CHROME" >&2
  exit 2
fi

"$CHROME" \
  --headless=new \
  --disable-gpu \
  --no-sandbox \
  --no-first-run \
  --no-default-browser-check \
  --disable-extensions \
  --disable-background-networking \
  --disable-sync \
  --disable-component-update \
  --disable-default-apps \
  --allow-file-access-from-files \
  --user-data-dir="$WORK/profile" \
  --virtual-time-budget=30000 \
  --dump-dom \
  "file://$ROOT/tests/overflow.html" \
  > "$WORK/dom.html" 2>/dev/null &
pid=$!

waited=0
while ! grep -q "DONE" "$WORK/dom.html" 2>/dev/null && [ "$waited" -lt 90 ]; do
  sleep 1
  waited=$((waited + 1))
done
kill "$pid" 2>/dev/null || true
wait "$pid" 2>/dev/null || true

if ! grep -q "DONE" "$WORK/dom.html" 2>/dev/null; then
  echo "the overflow probe did not finish" >&2
  exit 3
fi

# The probe writes a multi-line report into <pre id="out">, so the block is
# extracted whole and unescaped.
awk '/<pre id="out">/,/<\/pre>/' "$WORK/dom.html" \
  | sed 's/<pre id="out">//; s/<\/pre>//' \
  | sed 's/&lt;/</g; s/&gt;/>/g; s/&amp;/\&/g' > "$WORK/report.txt"

cat "$WORK/report.txt"

failures=$(grep -c '^FAIL' "$WORK/report.txt" || true)
passes=$(grep -c '^PASS' "$WORK/report.txt" || true)
echo ""
echo "$passes passed, $failures failed"
[ "$failures" -eq 0 ]
