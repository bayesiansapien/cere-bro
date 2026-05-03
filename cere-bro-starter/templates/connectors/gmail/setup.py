"""
One-time OAuth setup. Run this once to authorize against personal Gmail.
After this completes, farmer.py will run silently without browser prompts.

Usage:
    python connectors/gmail/setup.py
"""

import os
from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

CREDENTIALS_DIR = Path(__file__).parent / "credentials"
CREDENTIALS_FILE = CREDENTIALS_DIR / "credentials.json"
TOKEN_FILE = CREDENTIALS_DIR / "token.json"


def main():
    if not CREDENTIALS_FILE.exists():
        print(f"ERROR: credentials.json not found at {CREDENTIALS_FILE}")
        print("Download it from Google Cloud Console:")
        print("  APIs & Services → Credentials → OAuth 2.0 Client IDs → Download JSON")
        print(f"  Save it to: {CREDENTIALS_FILE}")
        return

    print("Opening browser for Google authorization...")
    print("Log in with your PERSONAL Gmail account.\n")

    flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_FILE), SCOPES)
    creds = flow.run_local_server(port=0)

    TOKEN_FILE.write_text(creds.to_json())
    print(f"\nAuthorization complete. Token saved to {TOKEN_FILE}")
    print("You can now run farmer.py without any browser interaction.")


if __name__ == "__main__":
    main()
