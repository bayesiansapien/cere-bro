# Gmail AI Newsletter Farmer

Automatically pulls your AI newsletters (Hugging Face daily papers, AI news digests, research blogs, vendor updates) from Gmail several times a day. No starring needed. Writes them to `raw/gmail/<digest-date>-newsletters.md`.

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
