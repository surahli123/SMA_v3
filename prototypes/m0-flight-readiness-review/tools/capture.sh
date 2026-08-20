#!/bin/sh
# Capture desktop and narrow-width evidence of the review surface.
#
# Uses the locally installed Chrome in headless mode against a file:// URL. No
# network, no sign-in, no profile of the user's is touched: a throwaway
# --user-data-dir is created under the output directory and removed after.
#
# Chrome writes the screenshot and then lingers, so each capture is backgrounded
# and waited on by polling for the file rather than for process exit.
#
# Usage: tools/capture.sh [output-directory]

set -eu

HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/.." && pwd)
OUT=${1:-"$ROOT/evidence"}
CHROME=${CHROME:-"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"}
PROFILE="$OUT/.chrome-profile"

if [ ! -x "$CHROME" ]; then
  echo "Chrome not found at: $CHROME" >&2
  echo "Set CHROME=/path/to/chrome and retry." >&2
  exit 2
fi

mkdir -p "$OUT"

# Headless Chrome clamps the window to 500px wide, so a narrow capture is taken
# through tools/narrow-frame.html, which hosts the surface in a fixed 390px
# iframe. Without that, a "390px" screenshot is a 500px layout cropped to 390
# and every line looks truncated.
#
# scenario_id | route | width | height | label
CAPTURES='trusted-decision-grade|readiness|1440|1180|trusted-desktop
trusted-decision-grade|readiness|390|1500|trusted-narrow
unauthorized-read|readiness|1440|1180|blocked-desktop
unauthorized-read|readiness|390|1500|blocked-narrow
stale-superseded-read|gaps|1440|1180|invalidated-desktop
stale-superseded-read|gaps|390|1500|invalidated-narrow
incomplete-observations|readiness|1440|1180|incomplete-desktop
incomplete-observations|readiness|390|1500|incomplete-narrow
trusted-decision-grade|receipts|1440|1180|receipts-desktop
trusted-decision-grade|receipts|390|1500|receipts-narrow
trusted-decision-grade|boundaries|1440|1180|boundaries-desktop
trusted-decision-grade|boundaries|390|1500|boundaries-narrow'

echo "$CAPTURES" | while IFS='|' read -r scenario route width height label; do
  [ -n "$label" ] || continue
  target="$OUT/$label.png"
  rm -f "$target"

  if [ "$width" -lt 500 ]; then
    url="file://$ROOT/tools/narrow-frame.html#/$scenario/$route@$width"
    window="$((width + 30)),$height"
  else
    url="file://$ROOT/index.html#/$scenario/$route"
    window="$width,$height"
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
    --user-data-dir="$PROFILE" \
    --hide-scrollbars \
    --force-device-scale-factor=2 \
    --window-size="$window" \
    --screenshot="$target" \
    "$url" \
    >/dev/null 2>&1 &
  pid=$!

  waited=0
  while [ ! -s "$target" ] && [ "$waited" -lt 40 ]; do
    sleep 1
    waited=$((waited + 1))
  done
  kill "$pid" 2>/dev/null || true
  wait "$pid" 2>/dev/null || true

  if [ -s "$target" ]; then
    echo "captured $label.png  ($width x $height)  $scenario/$route"
  else
    echo "FAILED   $label.png" >&2
  fi
done

rm -rf "$PROFILE"
echo "evidence written to $OUT"
