# Gmail Starred Email Farmer

Pulls starred emails from your Gmail account and writes them to `raw/gmail/YYYY-MM-DD-starred.md`.

## Setup (one-time)

### 1. Create a Google Cloud project

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project (or use an existing one)
3. Enable the Gmail API: APIs & Services → Enable APIs → search "Gmail API" → Enable

### 2. Create OAuth credentials

1. APIs & Services → Credentials → Create Credentials → OAuth 2.0 Client ID
2. Application type: **Desktop app**
3. Download the JSON file
4. Save it to `connectors/gmail/credentials/credentials.json`

The `credentials/` directory is in `.gitignore` — your OAuth credentials will never be committed.

### 3. Run one-time OAuth setup

```bash
cd connectors/gmail
pip install -r requirements.txt
python setup.py
```

This opens a browser window to authorize your Gmail account. After authorization, a `token.json` is saved in `credentials/`. Future runs of `farmer.py` will use this token silently.

## Daily usage

```bash
python connectors/gmail/farmer.py              # last 24 hours
python connectors/gmail/farmer.py --hours 48   # last 48 hours
python connectors/gmail/farmer.py --date 2026-05-01  # specific date label
```

Output: `raw/gmail/YYYY-MM-DD-starred.md`

## What gets included

Only emails that you have **starred** in Gmail. Star newsletters, AI updates, and papers you want to include in your daily digest. Unstarred emails are ignored.

## Automating

Add to a daily cron or shell script:
```bash
cd /path/to/your-wiki
python connectors/gmail/farmer.py
```
