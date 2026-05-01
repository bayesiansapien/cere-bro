"""
Gmail Starred Email Farmer for cere-bro.

Reads starred emails from personal Gmail (last N hours) and writes them
to raw/gmail/YYYY-MM-DD-starred.md for ingestion into the daily digest.

Usage:
    python connectors/gmail/farmer.py              # last 24 hours (default)
    python connectors/gmail/farmer.py --hours 48   # last 48 hours
    python connectors/gmail/farmer.py --date 2026-04-24  # specific date
"""

import argparse
import base64
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

REPO_ROOT = Path(__file__).parent.parent.parent
CREDENTIALS_DIR = Path(__file__).parent / "credentials"
TOKEN_FILE = CREDENTIALS_DIR / "token.json"
CREDENTIALS_FILE = CREDENTIALS_DIR / "credentials.json"
RAW_OUTPUT_DIR = REPO_ROOT / "raw" / "gmail"


def get_credentials():
    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            TOKEN_FILE.write_text(creds.to_json())
        else:
            print("ERROR: No valid token found. Run setup.py first.")
            sys.exit(1)
    return creds


def decode_body(payload):
    """Extract plain text body from Gmail message payload."""
    body = ""
    if payload.get("mimeType") == "text/plain":
        data = payload.get("body", {}).get("data", "")
        if data:
            body = base64.urlsafe_b64decode(data + "==").decode("utf-8", errors="replace")
    elif payload.get("mimeType", "").startswith("multipart/"):
        for part in payload.get("parts", []):
            body = decode_body(part)
            if body:
                break
    return body


def clean_body(text, max_chars=8000):
    """Trim whitespace and cap length for digest readability."""
    text = re.sub(r"\n{3,}", "\n\n", text.strip())
    if len(text) > max_chars:
        text = text[:max_chars] + f"\n\n[truncated — {len(text) - max_chars} chars omitted]"
    return text


def get_header(headers, name):
    for h in headers:
        if h["name"].lower() == name.lower():
            return h["value"]
    return ""


def fetch_starred_emails(service, after_timestamp):
    """Fetch all starred emails received after after_timestamp (Unix seconds)."""
    query = f"is:starred after:{int(after_timestamp)}"
    result = service.users().messages().list(userId="me", q=query, maxResults=50).execute()
    messages = result.get("messages", [])

    emails = []
    for msg_ref in messages:
        msg = service.users().messages().get(
            userId="me", id=msg_ref["id"], format="full"
        ).execute()

        headers = msg["payload"].get("headers", [])
        subject = get_header(headers, "Subject") or "(no subject)"
        sender = get_header(headers, "From") or "(unknown sender)"
        date_str = get_header(headers, "Date") or ""
        snippet = msg.get("snippet", "")
        body = decode_body(msg["payload"])

        emails.append({
            "id": msg["id"],
            "subject": subject,
            "sender": sender,
            "date": date_str,
            "snippet": snippet,
            "body": clean_body(body) if body else snippet,
            "gmail_link": f"https://mail.google.com/mail/u/0/#inbox/{msg['id']}",
        })

    return emails


def write_raw_file(emails, target_date):
    """Write starred emails to raw/gmail/YYYY-MM-DD-starred.md"""
    RAW_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = RAW_OUTPUT_DIR / f"{target_date}-starred.md"

    lines = [
        "---",
        "source: farmer/gmail-starred",
        f"farmed: {datetime.now(timezone.utc).isoformat()}",
        f"date: {target_date}",
        f"email_count: {len(emails)}",
        "---",
        "",
        f"# Starred Emails — {target_date}",
        "",
        f"*{len(emails)} starred email(s) from personal Gmail.*",
        "",
    ]

    for i, email in enumerate(emails, 1):
        lines += [
            f"---",
            f"",
            f"## {i}. {email['subject']}",
            f"",
            f"**From:** {email['sender']}  ",
            f"**Date:** {email['date']}  ",
            f"**Link:** [{email['gmail_link']}]({email['gmail_link']})",
            f"",
            email["body"] or email["snippet"],
            "",
        ]

    if not emails:
        lines += ["*No starred emails found for this period.*", ""]

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Fetch starred Gmail emails into raw/gmail/")
    parser.add_argument("--hours", type=int, default=24, help="Look back N hours (default: 24)")
    parser.add_argument("--date", type=str, default=None, help="Output date label YYYY-MM-DD (default: today)")
    args = parser.parse_args()

    target_date = args.date or datetime.now().strftime("%Y-%m-%d")
    after_dt = datetime.now(timezone.utc) - timedelta(hours=args.hours)
    after_timestamp = after_dt.timestamp()

    print(f"Fetching starred emails since {after_dt.strftime('%Y-%m-%d %H:%M UTC')}...")

    creds = get_credentials()
    service = build("gmail", "v1", credentials=creds)

    emails = fetch_starred_emails(service, after_timestamp)
    print(f"Found {len(emails)} starred email(s).")

    output_path = write_raw_file(emails, target_date)
    print(f"Written to: {output_path}")


if __name__ == "__main__":
    main()
