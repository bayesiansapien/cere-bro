#!/bin/bash
# One-shot catch-up: generate the podcast episodes missing after the
# 2026-08-15..25 outage, then reconcile them to GitHub Releases (Spotify).
#
# PREREQUISITE: `nlm login` must be done first (NotebookLM Google OAuth expired
# during the outage). Run:  nlm login   then:  bash scripts/catchup-podcasts.sh
#
# Dates: 08-22 (Saturday weekly review), 08-24 (Mon daily), 08-25 (Tue daily).
# 08-16 is a Sunday (podcast.py skips Sundays by design) so it is intentionally
# omitted; 08-17..21 and 08-23 have no digest per the user's backfill scope.
set -u
export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:$PATH"
cd "$(dirname "$0")/.." || exit 1

# Fail fast with a clear message if nlm auth is still expired.
if ! nlm notebook list >/dev/null 2>&1; then
  echo "✗ nlm is not authenticated. Run 'nlm login' first, then re-run this script." >&2
  exit 1
fi

for d in 2026-08-22 2026-08-24 2026-08-25; do
  echo "=== generating podcast for $d ==="
  python3 connectors/notebooklm/podcast.py "$d" || echo "  WARN: $d generation failed — continuing."
done

echo "=== reconciling all episodes to GitHub Releases (Spotify) ==="
python3 connectors/notebooklm/reconcile_releases.py

echo "=== cleaning up leftover NotebookLM notebooks ==="
python3 connectors/notebooklm/cleanup_notebooks.py || echo "  (cleanup skipped — non-fatal)"

echo "=== done. New episodes should appear on Spotify after the next feed poll. ==="
