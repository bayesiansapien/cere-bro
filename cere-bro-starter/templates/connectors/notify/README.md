# Notification helper

Sends pipeline failure alerts via three channels in priority order:

1. **macOS notification banner** (osascript) — always tries first, no setup
2. **Gmail SMTP** — sends an email if Keychain has `gmail-smtp-password` and a sender address is configured
3. **Log file** at `.claude/logs/notifications.log` — always writes for retroactive review

Designed to be called from cron scripts on any failure path. Never raises.

## Usage

From any shell script or cron step:

```bash
python3 connectors/notify/notify.py "Subject" "Body text here"
```

Or via env vars (when args are awkward):

```bash
NOTIFY_SUBJECT="..." NOTIFY_BODY="..." python3 connectors/notify/notify.py
```

## Setup (one-time, ~3 min)

For email alerts to actually send (rather than just banner + log), set up Gmail SMTP:

### 1. Generate a Gmail app password

Go to https://myaccount.google.com/apppasswords. Create a new 16-character app password labelled "cere-bro notify."

You need 2-step verification enabled on your Google account. If you don't see App Passwords in your security settings, enable 2FA first at https://myaccount.google.com/security.

### 2. Store the password in macOS Keychain

```bash
security add-generic-password -s gmail-smtp-password -a "$USER" -w
```

The terminal prompts for the value privately. Paste the 16-char app password (with or without spaces — doesn't matter). The script reads it at send time and never logs it.

### 3. Configure your sender/recipient addresses

Create `~/.config/cere-bro/notify.env`:

```bash
mkdir -p ~/.config/cere-bro
cat > ~/.config/cere-bro/notify.env <<EOF
NOTIFY_FROM=your-gmail@gmail.com
NOTIFY_TO=where-to-send-alerts@example.com
EOF
chmod 600 ~/.config/cere-bro/notify.env
```

`NOTIFY_TO` is optional — if omitted, alerts go back to `NOTIFY_FROM`.

The script auto-loads this file at startup. Per the [Secrets policy](../../CLAUDE.md), this file is gitignored (`~/.config/cere-bro/` is in the global `.gitignore` pattern set).

### 4. Test it

```bash
python3 connectors/notify/notify.py "Test alert" "If you see this in your inbox, the wiring works."
```

You should get:
- A banner notification on screen
- An email in your inbox (if Gmail setup is complete)
- A line appended to `.claude/logs/notifications.log`

If email didn't send, check the log for `[gmail-smtp-error]` lines explaining why.

## When it fires automatically

Wired into `cerebro-morning-digest.sh` to alert on:

- Any farmer (Gmail, Twitter, Kurate, Reddit) failing
- The Claude digest-writing call failing (auth issues, rate limits, etc.)
- The NotebookLM podcast generation failing
- A missing digest preventing podcast generation (cascade failure)

Each alert includes the date, the step that failed, and a relevant tail of the log so you can act quickly without needing to SSH in and read logs.

## Why three channels?

- The **banner** catches you if you're at the laptop (most common case).
- The **email** reaches you when you're away from the laptop or asleep.
- The **log** preserves the full history regardless of which channels succeeded, so you can audit pipeline health weekly.

If the Gmail path isn't set up yet, you still get banner + log — graceful degradation rather than silent failure on the notification system itself.
