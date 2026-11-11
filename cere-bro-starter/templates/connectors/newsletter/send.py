#!/usr/bin/env python3
"""
Send the Cerebro Daily email for one digest date (default: today).

Builds the HTML with build.py, then sends it over Gmail SMTP.
  - Recipients + sender: ~/.config/cere-bro/newsletter.env (gitignored, outside the repo)
      NEWSLETTER_TO=a@x.com,b@y.com
      NEWSLETTER_FROM=you@gmail.com
  - Password: macOS Keychain item `gmail-smtp-password` (a Gmail app password).
Each date is sent once (connectors/newsletter/.state/sent.json); --force resends.

Run: python3 connectors/newsletter/send.py [YYYY-MM-DD] [--force] [--dry-run]
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
    pw = password(os.environ.get("USER", ""))
    if not pw:
        print("newsletter: Keychain item gmail-smtp-password missing; skipping")
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
