#!/usr/bin/env python3
"""
Pipeline failure notification helper for cere-bro.

Sends an alert via three channels, in priority order:
  1. macOS notification banner (osascript) — always tries first, no creds
  2. Email via Gmail SMTP — if Keychain has `gmail-smtp-password` for $USER
  3. Append to .claude/logs/notifications.log — always writes for retroactive review

Designed to be called from cron scripts on any failure path. Never raises.

Usage:
  python3 connectors/notify/notify.py "Subject line" "Body text…"

Or via env (when stdin/args are awkward):
  NOTIFY_SUBJECT="..." NOTIFY_BODY="..." python3 connectors/notify/notify.py

Setup for Gmail SMTP path (one-time, ~2 min):
  1. Go to https://myaccount.google.com/apppasswords
  2. Generate a 16-char app password (label it "cere-bro notify")
  3. Save to macOS Keychain:
       security add-generic-password -s gmail-smtp-password -a "$USER" -w
     (it prompts for the value privately; never echo or log it)
  4. Set NOTIFY_FROM env var (or hardcode in ~/.config/cere-bro/notify.env)
     with your Gmail address. The script reads it at send time.

If Keychain has no password, the Gmail path is skipped silently and you only
get banner + log. No errors raised either way.
"""

import os
import smtplib
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from email.message import EmailMessage
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
LOG_PATH  = REPO_ROOT / ".claude" / "logs" / "notifications.log"
ENV_FILE  = Path.home() / ".config" / "cere-bro" / "notify.env"

def _read_env_file():
    """Load NOTIFY_FROM and other vars from ~/.config/cere-bro/notify.env if present."""
    if not ENV_FILE.exists():
        return
    try:
        for line in ENV_FILE.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
    except Exception:
        pass

def _macos_notification(title: str, body: str):
    """Show a banner via osascript. Silent on non-macOS or any failure."""
    if sys.platform != "darwin":
        return False
    try:
        # Escape double-quotes for AppleScript
        t = title.replace('"', '\\"')
        b = body.replace('"', '\\"').replace("\n", " ")[:240]
        subprocess.run(
            ["osascript", "-e",
             f'display notification "{b}" with title "{t}" sound name "Submarine"'],
            check=False, capture_output=True, timeout=5,
        )
        return True
    except Exception:
        return False

def _keychain_get(service: str):
    """Read a secret from macOS Keychain. Returns None if missing or non-macOS."""
    if sys.platform != "darwin":
        return None
    try:
        r = subprocess.run(
            ["security", "find-generic-password", "-s", service,
             "-a", os.environ.get("USER", ""), "-w"],
            capture_output=True, text=True, timeout=5, check=False,
        )
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip()
    except Exception:
        pass
    return None

def _gmail_send(subject: str, body: str):
    """Send via Gmail SMTP. Returns True on success, False otherwise. Never raises."""
    pw = _keychain_get("gmail-smtp-password")
    if not pw:
        return False
    sender = os.environ.get("NOTIFY_FROM")
    recipient = os.environ.get("NOTIFY_TO") or sender
    if not sender or not recipient:
        return False
    try:
        msg = EmailMessage()
        msg["From"]    = sender
        msg["To"]      = recipient
        msg["Subject"] = f"[cere-bro] {subject}"
        msg.set_content(body)
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as s:
            s.starttls()
            s.login(sender, pw)
            s.send_message(msg)
        return True
    except Exception as e:
        # Last-resort: write the SMTP error itself to log so we know why it failed
        _log(f"[gmail-smtp-error] {type(e).__name__}: {e}")
        return False

def _log(line: str):
    """Always-on log of notification attempts. Path: .claude/logs/notifications.log."""
    try:
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        ts = (datetime.now(timezone.utc) + timedelta(hours=5, minutes=30)).strftime("%Y-%m-%d %H:%M:%S IST")
        with LOG_PATH.open("a", encoding="utf-8") as f:
            f.write(f"[{ts}] {line}\n")
    except Exception:
        pass

def notify(subject: str, body: str):
    _read_env_file()
    banner_ok = _macos_notification(subject, body)
    email_ok  = _gmail_send(subject, body)
    channels  = []
    if banner_ok: channels.append("banner")
    if email_ok:  channels.append("email")
    if not channels: channels.append("log-only")
    _log(f"NOTIFY [{','.join(channels)}] {subject}: {body[:180]}")
    return {"banner": banner_ok, "email": email_ok}

def _from_cli():
    if len(sys.argv) >= 3:
        return sys.argv[1], sys.argv[2]
    subject = os.environ.get("NOTIFY_SUBJECT", "cere-bro pipeline event")
    body    = os.environ.get("NOTIFY_BODY", "(no body)")
    return subject, body

if __name__ == "__main__":
    subj, body = _from_cli()
    result = notify(subj, body)
    print(f"Sent: {result}")
