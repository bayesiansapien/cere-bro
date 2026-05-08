# Schedule scripts (LaunchAgent / cron templates)

Five script templates that drive the daily pipeline.

| Script | When | What it does |
|---|---|---|
| `cerebro-morning-digest.sh.template` | 09:00 IST (or your morning time) | Runs Gmail + Twitter + Kurate farmers, then invokes Claude to write the daily digest + morning slot synthesis |
| `cerebro-twitter-afternoon.sh.template` | 15:00 | Runs Twitter farmer for afternoon slot, then writes afternoon synthesis |
| `cerebro-twitter-evening.sh.template` | 22:00 | Runs Twitter farmer for evening slot, then writes evening synthesis |
| `cerebro-synth-slot.sh.template` | called by afternoon/evening scripts | Shared helper that calls Claude to write per-slot synthesis |
| `cerebro-rollup-midnight.sh.template` | 23:55 | Reads all slot syntheses for the day, writes daily roll-up |

## Install

1. **Copy each template to `~/.local/bin/`** and strip the `.template` suffix:
   ```bash
   mkdir -p ~/.local/bin
   for f in cerebro-*.template; do
     cp "$f" ~/.local/bin/"${f%.template}"
   done
   chmod +x ~/.local/bin/cerebro-*.sh
   ```

2. **Replace `{{REPO_PATH}}`** with your local repo path:
   ```bash
   sed -i '' "s|{{REPO_PATH}}|$(pwd)|g" ~/.local/bin/cerebro-*.sh
   ```
   (Use `sed -i ""` on macOS, `sed -i` on Linux.)

3. **Replace `{{CLAUDE_BIN}}`** with your Claude binary path. Find it:
   ```bash
   which claude
   ```
   Then:
   ```bash
   sed -i '' "s|{{CLAUDE_BIN}}|/Users/you/.local/bin/claude|g" ~/.local/bin/cerebro-*.sh
   ```

4. **Schedule them.** On macOS, use the LaunchAgent plists in `../launchagents/`:
   ```bash
   cp ../launchagents/com.cerebro.*.plist ~/Library/LaunchAgents/
   for plist in ~/Library/LaunchAgents/com.cerebro.*.plist; do
     launchctl load "$plist"
   done
   ```

   On Linux, use cron (run `crontab -e` and add):
   ```cron
   0  9 * * * ~/.local/bin/cerebro-morning-digest.sh
   0 15 * * * ~/.local/bin/cerebro-twitter-afternoon.sh
   0 22 * * * ~/.local/bin/cerebro-twitter-evening.sh
   55 23 * * * ~/.local/bin/cerebro-rollup-midnight.sh
   ```

## Verify

After install:
```bash
launchctl list | grep cerebro    # macOS
crontab -l | grep cerebro        # Linux
```

You should see the four scheduled agents. Logs accumulate at `<repo>/.claude/logs/`.

## Optional: skip individual slots

If you don't want 4× polling, comment out the cron line / unload the LaunchAgent for the slots you want to skip. The morning slot is the only one that drives the daily digest, so keep that.
