#!/usr/bin/env python3
"""
Send the Cerebro Daily email for one digest date (default: today).

Builds the HTML with build.py, then sends it through Gmail.
  - Recipients + sender: ~/.config/cere-bro/newsletter.env (gitignored, outside the repo)
      NEWSLETTER_TO=a@x.com,b@y.com
      NEWSLETTER_FROM=you@gmail.com
  - Transport, first that is set up:
      1. Gmail API with a send-only OAuth token (credentials/token.json, gitignored).
         Reuses the Gmail farmer's OAuth client; authorize once with --auth.
      2. SMTP with a Gmail app password in the Keychain item `gmail-smtp-password`.
Each date is sent once (connectors/newsletter/.state/sent.json); --force resends.

Run: python3 connectors/newsletter/send.py [YYYY-MM-DD] [--force] [--dry-run]
     python3 connectors/newsletter/send.py --auth     (one-time browser consent)
"""

import json
import os
import re
import smtplib
import subprocess
import sys
from datetime import datetime
from email.message import EmailMessage
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import build  # noqa: E402

ENV_FILE = Path.home() / ".config" / "cere-bro" / "newsletter.env"
STATE = HERE / ".state" / "sent.json"
CLIENT_FILE = HERE.parent / "gmail" / "credentials" / "credentials.json"
TOKEN_FILE = HERE / "credentials" / "token.json"
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]


def authorize():
    from google_auth_oauthlib.flow import InstalledAppFlow
    if not CLIENT_FILE.exists():
        print(f"newsletter: OAuth client missing at {CLIENT_FILE} (set up the Gmail farmer first)")
        return 1
    creds = InstalledAppFlow.from_client_secrets_file(str(CLIENT_FILE), SCOPES).run_local_server(port=0)
    TOKEN_FILE.parent.mkdir(exist_ok=True)
    TOKEN_FILE.write_text(creds.to_json())
    os.chmod(TOKEN_FILE, 0o600)
    print(f"newsletter: send token saved to {TOKEN_FILE}")
    return 0


def api_creds():
    """Send-only Gmail API credentials, refreshed if needed; None if not authorized."""
    if not TOKEN_FILE.exists():
        return None
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        TOKEN_FILE.write_text(creds.to_json())
    return creds if creds.valid else None


def env():
    vals = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            if "=" in line and not line.strip().startswith("#"):
                k, v = line.split("=", 1)
                vals[k.strip()] = v.strip().strip('"').strip("'")
    return vals


def password(account):
    r = subprocess.run(["security", "find-generic-password", "-s", "gmail-smtp-password", "-a", account, "-w"],
                       capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""


def main():
    if "--auth" in sys.argv:
        return authorize()
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    date = args[0] if args else datetime.now().strftime("%Y-%m-%d")
    force, dry = "--force" in sys.argv, "--dry-run" in sys.argv
    sent = json.loads(STATE.read_text()) if STATE.exists() else {}
    if date in sent and not force:
        print(f"newsletter {date}: already sent at {sent[date]}")
        return 0
    cfg = env()
    to = [a.strip() for a in cfg.get("NEWSLETTER_TO", "").split(",") if a.strip()]
    sender = cfg.get("NEWSLETTER_FROM", "")
    if not to or not sender:
        print(f"newsletter: no recipients/sender in {ENV_FILE}; skipping")
        return 1
    subject, page = build.build(date)
    if dry:
        print(f"dry run: would send '{subject}' to {len(to)} recipient(s)")
        return 0
    creds = api_creds()
    pw = "" if creds else password(os.environ.get("USER", ""))
    if not creds and not pw:
        print("newsletter: no send credentials (run send.py --auth, or add Keychain item gmail-smtp-password); skipping")
        return 1
    msg = EmailMessage()
    msg["Subject"], msg["From"], msg["To"] = subject, f"Cerebro <{sender}>", ", ".join(to)
    msg.set_content(f"{subject}\n\nThis is the HTML edition; open it in an HTML-capable mail client.")
    msg.add_alternative(page, subtype="html")
    # Embed the logo in the message itself (cid:), so it shows on networks that
    # block GitHub-hosted images and in clients that block remote images.
    logo = HERE / "logo.png"
    if logo.exists():
        msg.get_payload()[1].add_related(logo.read_bytes(), maintype="image", subtype="png",
                                         cid=f"<{build.LOGO_CID}>", filename="cerebro.png")
    if creds:
        import base64
        from googleapiclient.discovery import build as gbuild
        raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
        gbuild("gmail", "v1", credentials=creds, cache_discovery=False).users().messages().send(
            userId="me", body={"raw": raw}).execute()
    else:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=60) as s:
            s.login(sender, re.sub(r"\s", "", pw))
            s.send_message(msg)
    sent[date] = datetime.now().isoformat(timespec="seconds")
    STATE.parent.mkdir(exist_ok=True)
    STATE.write_text(json.dumps(sent, indent=1))
    print(f"newsletter {date}: sent to {len(to)} recipient(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
