# Cerebro Daily (email edition)

A compressed email of each day's digest, sent right after the morning run writes it.

- `build.py YYYY-MM-DD`: renders `out/YYYY-MM-DD.html` from the digest: the theme line, Today's 5, every Deep Dive as title + source links (with a one-line hook if it is not already in Today's 5), Industry Pulse with repeated stories removed, and Global View headlines. No TL;DR: everything in it already appears in one of those sections. Only original-source links are kept (arXiv, blogs, X, news); wiki links and GitHub-hosted links are dropped so it reads on networks that block GitHub.
- `logo.png` (optional): the brand logo on its own black band (baked into the image, so it survives clients that strip backgrounds), shown at the top of the header, embedded in each email so it shows even where image hosts are blocked. Missing = text-only header.
- `send.py [YYYY-MM-DD] [--force] [--dry-run]`: builds and sends through Gmail, once per date (`.state/sent.json`). `send.py --auth` does the one-time sign-in.

Setup (one time, nothing goes in the repo):
1. `~/.config/cere-bro/newsletter.env` (chmod 600):
   ```
   NEWSLETTER_TO=reader@example.com,other@example.com
   NEWSLETTER_FROM=you@gmail.com
   ```
2. Sending, either one:
   - **Gmail API (preferred):** `python3 connectors/newsletter/send.py --auth` once. It reuses the Gmail farmer's OAuth client (`connectors/gmail/credentials/credentials.json`), asks only for the send scope, and saves a refreshing token to `connectors/newsletter/credentials/token.json` (gitignored). If your OAuth app is in "Testing" mode, Google expires the token after 7 days; publish the app to keep it.
   - **SMTP fallback:** a Gmail app password (https://myaccount.google.com/apppasswords) in Keychain:
     `security add-generic-password -s gmail-smtp-password -a "$USER" -w`

Without recipients or a way to send, the morning run logs "Newsletter not sent" and carries on.
