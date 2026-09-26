# Gmail AI Newsletter Farmer

Automatically pulls your AI newsletters (Hugging Face daily papers, AI news digests, research blogs, vendor updates) from Gmail several times a day. No starring needed. Writes them to `raw/gmail/<digest-date>-newsletters.md` for the daily digest.

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

## Usage

```bash
python connectors/gmail/farmer.py              # incremental: everything since the last run
python connectors/gmail/farmer.py --hours 48   # force a 48-hour window
python connectors/gmail/farmer.py --dry-run    # classify and print what would be pulled; writes nothing
```

Output: `raw/gmail/<digest-date>-newsletters.md` plus a `.json` sidecar. `<digest-date>` is the **next daily
digest that hasn't been written yet**, so a newsletter arriving in the evening, after today's digest ran,
lands in tomorrow's file instead of being missed. Each run merges into that file (deduped by message id).

## What gets pulled (no starring needed)

The farmer scans your inbox on a rolling timestamp window (since the previous run, with a small overlap,
capped at `max_catchup_hours` after a long gap) and keeps an email if **any** of these hold:

1. **Allowlisted sender**: the From address matches a pattern in `config.json:allow_senders`. Groups:
   `papers` (Hugging Face daily papers), `digests` (AI news digests), `blogs` (research blogs and essays),
   `vendor_updates` (tool and platform newsletters). The group sets the section in the output file.
2. **Auto-detected AI newsletter**: it has a `List-Unsubscribe` or `List-Id` header (a newsletter), its
   domain isn't on `block_domains`, and its subject + preview hits at least `min_keyword_hits` of `ai_keywords`.
   This picks up new AI newsletters you subscribe to without editing the config.
3. **Starred by you**: if `include_starred` is true, starred mail is still included as manual curation.

`exclude_senders` always wins; put **your own** newsletter address there. `block_domains` stops banks,
brokers, shopping, travel and job alerts from being auto-detected. Tune both after a `--dry-run`.

Body handling: prefers the plain-text part, falls back to HTML-to-text for HTML-only newsletters, strips
long tracking links and unsubscribe/footer lines, and caps each body at `max_body_chars`.

## Privacy

`raw/gmail/` and `connectors/gmail/.state/` are **gitignored**. These are your own emails (and some are
paid newsletters), so they stay on your machine. Only the daily digest's synthesis is published. The OAuth
scope is read-only (`gmail.readonly`).

## Automating

The scheduled scripts run it at the morning digest and at each feed capture (`cerebro-morning-digest.sh`,
`cerebro-feed-capture.sh`), so newsletters flow in several times a day. Manually:
```bash
cd /path/to/your-wiki && python connectors/gmail/farmer.py
```
