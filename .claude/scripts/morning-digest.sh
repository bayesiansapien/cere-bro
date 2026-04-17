#!/bin/bash
# morning-digest.sh
# Runs daily at 9 AM via LaunchAgent.
# Farms new content, ingests it, and writes today's daily digest.

set -euo pipefail

REPO="/Users/amitsinghbhatti/Desktop/AI-LAB/cere-bro"
CLAUDE="/Users/amitsinghbhatti/.local/bin/claude"
LOG="$REPO/.claude/logs/morning-digest.log"
TODAY=$(date +%Y-%m-%d)

mkdir -p "$REPO/.claude/logs"

echo "[$TODAY $(date +%H:%M:%S)] Starting morning digest..." >> "$LOG"

cd "$REPO"

# Pull latest before starting
git pull --rebase origin main >> "$LOG" 2>&1 || true

# Run Claude with farm + ingest prompt, non-interactive
"$CLAUDE" \
  --dangerously-skip-permissions \
  -p "Today is $TODAY. Do the following in order:
1. Run the huggingface-farmer subagent to fetch today's papers from HuggingFace into raw/huggingface/.
2. Run the rss-farmer subagent to fetch today's blog/newsletter posts into raw/rss/.
3. Ingest all new raw files per CLAUDE.md: write summary pages in the appropriate wiki/ subdirectory, update concept pages, write today's daily digest at wiki/daily-digest/$(date +%Y-%m)/$TODAY.md using the newsletter format defined in CLAUDE.md. Update index.md and append to log.md.
Do not stop until the digest is written and committed." \
  >> "$LOG" 2>&1

echo "[$TODAY $(date +%H:%M:%S)] Done." >> "$LOG"
