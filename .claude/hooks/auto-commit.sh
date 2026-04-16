#!/bin/bash
# Auto-commit wiki changes after Write/Edit operations

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('tool_input',{}).get('file_path') or d.get('tool_input',{}).get('filePath') or '')")

# Exit if no file path
if [ -z "$FILE_PATH" ]; then
  exit 0
fi

# Get relative path from repo root
REPO_ROOT="$CLAUDE_PROJECT_DIR"
REL_PATH="${FILE_PATH#$REPO_ROOT/}"

# Only auto-commit wiki content directories
case "$REL_PATH" in
  wiki/*|raw/*|CLAUDE.md)
    ;;
  *)
    exit 0
    ;;
esac

FOLDER=$(echo "$REL_PATH" | cut -d'/' -f1)
FILENAME=$(basename "$REL_PATH" .md)

cd "$REPO_ROOT" || exit 0

# Recover from detached HEAD before committing
if ! git symbolic-ref --quiet HEAD >/dev/null 2>&1; then
  echo "auto-commit: HEAD is detached, recovering to origin/main"
  git fetch origin main 2>/dev/null
  git checkout main 2>/dev/null || git checkout -b main origin/main
  git reset --hard origin/main
fi

# Pull-then-push helper: rebase if possible, merge if not
sync_and_push() {
  if ! git pull --rebase; then
    git rebase --abort 2>/dev/null
    git pull --no-rebase
  fi
  git push -u origin main || true
}

# Check if file has changes
if git diff --quiet "$FILE_PATH" 2>/dev/null && git diff --cached --quiet "$FILE_PATH" 2>/dev/null; then
  # New untracked file
  if ! git ls-files --error-unmatch "$FILE_PATH" 2>/dev/null; then
    git add "$FILE_PATH"
    git commit -m "wiki: add $FOLDER/$FILENAME"
    sync_and_push
  fi
else
  git add "$FILE_PATH"
  git commit -m "wiki: update $FOLDER/$FILENAME"
  sync_and_push
fi

exit 0
