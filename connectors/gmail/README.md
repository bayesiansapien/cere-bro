# Gmail Starred Email Farmer

Reads starred emails from personal Gmail and writes them into `raw/gmail/` so the cere-bro ingest pipeline can include them in the daily digest.

## Folder layout

```
connectors/gmail/
  README.md               ← this file
  farmer.py               ← main script (run daily)
  setup.py                ← one-time OAuth setup helper
  requirements.txt        ← pip dependencies
  credentials/
    credentials.json      ← OAuth client secret (download from Google Cloud Console, never commit)
    token.json            ← stored access token after first auth (auto-created, never commit)
```

## One-time setup

1. Follow the steps in **Google Cloud Setup** below to get `credentials.json`
2. Drop `credentials.json` into `connectors/gmail/credentials/`
3. Run: `python connectors/gmail/setup.py`  
   → Opens a browser, you log in with personal Gmail, token is saved to `credentials/token.json`
4. Done. Run `farmer.py` any time after that.

## Google Cloud Setup

What you need from Google Cloud Console (console.cloud.google.com):

1. **Create or pick a project** — any name, e.g. "cere-bro"
2. **Enable Gmail API** → APIs & Services → Library → search "Gmail API" → Enable
3. **Create OAuth credentials** → APIs & Services → Credentials → Create Credentials → OAuth client ID
   - Application type: **Desktop app**
   - Name: anything, e.g. "cere-bro farmer"
   - Click Create → Download JSON → save as `credentials/credentials.json`
4. **Set OAuth consent screen** → External → add your personal Gmail as a test user

That's it. No billing required, no service account needed.

## Daily usage

```bash
python connectors/gmail/farmer.py
```

Writes files to `raw/gmail/YYYY-MM-DD-starred.md` — one file per day containing all starred emails from the last 24 hours. Each email becomes a separate section with sender, subject, date, and body.

## Automation (optional)

Add to crontab or launchd to run automatically each morning:
```
0 7 * * * cd /Users/amitsinghbhatti/Desktop/AI-LAB/cere-bro && python connectors/gmail/farmer.py
```
