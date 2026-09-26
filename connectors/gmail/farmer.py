"""
Gmail Newsletter Farmer for cere-bro.

Automatically pulls the reader's AI newsletters from Gmail on a rolling
timestamp window. No starring required. Runs several times a day; each run
fetches only mail that arrived since the previous run (plus a small overlap),
dedupes by message id, and keeps an email if:

  1. its sender matches an `allow_senders` pattern in config.json
     (curated AI newsletters: HF daily papers, AI digests, research blogs), or
  2. it is a newsletter (List-Unsubscribe / List-Id header) from a non-blocked
     domain whose subject + snippet hits >= `min_keyword_hits` AI keywords
     (auto-discovers new AI newsletters you subscribe to), or
  3. `include_starred` is on and you starred it (legacy manual curation).

Output routing follows the digest window, not the calendar: emails go into
raw/gmail/<D>-newsletters.md (+ .json sidecar) where <D> is the next daily
digest that has NOT been written yet. So a newsletter arriving at 22:00, after
today's digest ran, lands in tomorrow's file instead of being missed.

PRIVACY: raw/gmail/ is gitignored. These are the reader's own emails (and some
are paid newsletters); only the digest synthesis is published.

Usage:
    python connectors/gmail/farmer.py              # incremental since last run
    python connectors/gmail/farmer.py --hours 48   # force a 48h window
    python connectors/gmail/farmer.py --dry-run    # classify + print, write nothing
"""

import argparse
import base64
import html
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

HERE = Path(__file__).parent
REPO_ROOT = HERE.parent.parent
CREDENTIALS_DIR = HERE / "credentials"
TOKEN_FILE = CREDENTIALS_DIR / "token.json"
RAW_OUTPUT_DIR = REPO_ROOT / "raw" / "gmail"
DIGEST_DIR = REPO_ROOT / "wiki" / "daily-digest"
STATE_DIR = HERE / ".state"
LAST_RUN_FILE = STATE_DIR / "last_run.json"
SEEN_FILE = STATE_DIR / "seen_ids.json"

CFG = json.loads((HERE / "config.json").read_text())


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


# ── Body extraction ────────────────────────────────────────────────────────────

class _HTMLText(HTMLParser):
    """Minimal HTML → text: drops script/style, keeps block structure."""
    BLOCK = {"p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6", "table", "section", "article"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "head"):
            self.skip += 1
        elif tag in self.BLOCK:
            self.out.append("\n")
        if tag == "li":
            self.out.append("- ")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "head") and self.skip:
            self.skip -= 1
        elif tag in self.BLOCK:
            self.out.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


def html_to_text(raw_html: str) -> str:
    p = _HTMLText()
    try:
        p.feed(raw_html)
    except Exception:
        return re.sub(r"<[^>]+>", " ", raw_html)
    return html.unescape("".join(p.out))


def _part_text(payload, mime):
    """Depth-first search for the first part of the given mime type."""
    if payload.get("mimeType") == mime:
        data = payload.get("body", {}).get("data", "")
        if data:
            return base64.urlsafe_b64decode(data + "==").decode("utf-8", errors="replace")
    for part in payload.get("parts", []) or []:
        t = _part_text(part, mime)
        if t:
            return t
    return ""


def decode_body(payload) -> str:
    """Prefer text/plain; fall back to text/html converted to text."""
    text = _part_text(payload, "text/plain")
    if len(text.strip()) < 200:  # many newsletters ship an empty/stub plain part
        h = _part_text(payload, "text/html")
        if h:
            text = html_to_text(h)
    return text


_NOISE = re.compile(r"(unsubscribe|manage (your )?(preferences|subscription)|view (this|in) (email|browser)|"
                    r"update your preferences|you are receiving this|forward(ed)? to a friend)", re.I)


def clean_body(text: str, max_chars: int) -> str:
    text = re.sub(r"https?://\S{120,}", "[link]", text)        # tracking redirects
    text = re.sub(r"(?m)^#{1,3}\s", "#### ", text)              # keep newsletter headings below our sections
    text = re.sub(r"\[\s*\]|\(\s*\)", "", text)
    lines = [ln.rstrip() for ln in text.splitlines() if not _NOISE.search(ln)]
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()
    text = re.sub(r"[ \t ‌͏]{2,}", " ", text)
    if len(text) > max_chars:
        text = text[:max_chars] + f"\n\n[truncated, {len(text) - max_chars} chars omitted]"
    return text


# ── Classification ─────────────────────────────────────────────────────────────

_KW = [re.compile(r"(?<![a-z0-9])" + re.escape(k.lower()) + r"(?![a-z0-9])") for k in CFG["ai_keywords"]]


def _addr(from_header: str) -> str:
    m = re.search(r"<([^>]+)>", from_header or "")
    return (m.group(1) if m else from_header or "").strip().lower()


def classify(headers: dict, labels: list, snippet: str):
    """Return (keep: bool, category: str, reason: str)."""
    addr = _addr(headers.get("from", ""))
    domain = addr.split("@")[-1]
    if any(p.lower() in addr for p in CFG.get("exclude_senders", [])):
        return False, "", "excluded sender"
    for cat, pats in CFG["allow_senders"].items():
        if any(p.lower() in addr for p in pats):
            return True, cat, "subscribed AI newsletter"
    if CFG.get("include_starred") and "STARRED" in labels:
        return True, "starred", "starred by you"
    if any(domain == d or domain.endswith("." + d) for d in CFG["block_domains"]):
        return False, "", "blocked domain"
    if "list-unsubscribe" in headers or "list-id" in headers:
        text = f"{headers.get('subject', '')} {snippet}".lower()
        hits = sum(1 for k in _KW if k.search(text))
        if hits >= CFG["min_keyword_hits"]:
            return True, "digests", f"auto-detected AI newsletter ({hits} keyword hits)"
    return False, "", "not an AI newsletter"


# ── Windowing, routing, state ──────────────────────────────────────────────────

def _load(path, default):
    try:
        return json.loads(path.read_text())
    except Exception:
        return default


def window_start(now_utc, hours_override):
    if hours_override:
        return now_utc - timedelta(hours=hours_override)
    last = _load(LAST_RUN_FILE, {}).get("ts")
    floor = now_utc - timedelta(hours=CFG["max_catchup_hours"])
    if not last:
        return now_utc - timedelta(hours=CFG["lookback_hours_first_run"])
    start = datetime.fromisoformat(last) - timedelta(minutes=CFG["overlap_minutes"])
    if start < floor:
        print(f"  last run {last} is older than the {CFG['max_catchup_hours']}h cap; catching up from the cap.")
    return max(start, floor)


def target_digest_date(now_local: datetime) -> str:
    """The next daily digest not yet written: today unless today's already exists."""
    today = now_local.strftime("%Y-%m-%d")
    if (DIGEST_DIR / today[:7] / f"{today}.md").exists():
        return (now_local + timedelta(days=1)).strftime("%Y-%m-%d")
    return today


# ── Fetch ──────────────────────────────────────────────────────────────────────

def fetch(service, after_utc, seen: set):
    q = f"after:{int(after_utc.timestamp())} -in:chats -in:sent -in:drafts -in:spam -in:trash"
    ids, token = [], None
    while len(ids) < CFG["max_messages_per_run"]:
        r = service.users().messages().list(userId="me", q=q, maxResults=500, pageToken=token).execute()
        ids += [m["id"] for m in r.get("messages", [])]
        token = r.get("nextPageToken")
        if not token:
            break
    ids = [i for i in ids if i not in seen][: CFG["max_messages_per_run"]]

    meta = {}

    def cb(rid, resp, exc):
        if not exc:
            meta[resp["id"]] = resp

    def get_meta(mid):
        return service.users().messages().get(
            userId="me", id=mid, format="metadata",
            metadataHeaders=["From", "Subject", "Date", "List-Unsubscribe", "List-Id"])

    # Small batches: Gmail rate-limits large batches (429s show up as silently
    # dropped items). Anything that still fails is retried one-by-one, so no
    # message is ever skipped without being classified.
    for i in range(0, len(ids), 20):
        b = service.new_batch_http_request(callback=cb)
        for mid in ids[i:i + 20]:
            b.add(get_meta(mid))
        b.execute()
    for mid in [m for m in ids if m not in meta]:
        for attempt in range(3):
            try:
                meta[mid] = get_meta(mid).execute()
                break
            except Exception:
                import time
                time.sleep(1.5 * (attempt + 1))
    missing = [m for m in ids if m not in meta]
    if missing:
        print(f"  WARNING: {len(missing)} message(s) could not be fetched; they stay unseen and retry next run.")
        ids[:] = [m for m in ids if m in meta]

    kept, skipped = [], 0
    for mid, m in meta.items():
        h = {x["name"].lower(): x["value"] for x in m["payload"].get("headers", [])}
        keep, cat, reason = classify(h, m.get("labelIds", []), m.get("snippet", ""))
        if keep:
            kept.append((mid, cat, reason, h))
        else:
            skipped += 1
    return ids, kept, skipped


def hydrate(service, kept):
    out = []
    for mid, cat, reason, h in kept:
        full = service.users().messages().get(userId="me", id=mid, format="full").execute()
        body = clean_body(decode_body(full["payload"]), CFG["max_body_chars"])
        try:
            received = parsedate_to_datetime(h.get("date", "")).astimezone(timezone.utc).isoformat()
        except Exception:
            received = datetime.fromtimestamp(int(full.get("internalDate", 0)) / 1000, timezone.utc).isoformat()
        out.append({
            "id": mid, "category": cat, "reason": reason,
            "subject": h.get("subject", "(no subject)"), "sender": h.get("from", "(unknown)"),
            "received_utc": received, "body": body or full.get("snippet", ""),
            "gmail_link": f"https://mail.google.com/mail/u/0/#inbox/{mid}",
        })
    return out


# ── Output ─────────────────────────────────────────────────────────────────────

SECTION_TITLES = {
    "papers": "Hugging Face / paper digests",
    "digests": "AI news digests & newsletters",
    "blogs": "Research blogs & essays",
    "starred": "Other emails you starred",
    "vendor_updates": "Vendor & tool updates",
}


def write_outputs(emails, target_date):
    RAW_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    jpath = RAW_OUTPUT_DIR / f"{target_date}-newsletters.json"
    existing = _load(jpath, {"emails": []})["emails"]
    by_id = {e["id"]: e for e in existing}
    for e in emails:
        by_id[e["id"]] = e
    allm = sorted(by_id.values(), key=lambda e: e["received_utc"])
    jpath.write_text(json.dumps({"digest_date": target_date, "updated_utc": datetime.now(timezone.utc).isoformat(),
                                 "emails": allm}, indent=2, ensure_ascii=False), encoding="utf-8")

    lines = ["---", "source: farmer/gmail-newsletters", f"digest_date: {target_date}",
             f"farmed: {datetime.now(timezone.utc).isoformat()}", f"email_count: {len(allm)}", "---", "",
             f"# AI Newsletters — for the {target_date} digest", "",
             f"*{len(allm)} newsletter email(s) auto-pulled from Gmail since the previous digest "
             "(no starring needed). Private: raw/gmail/ is gitignored.*", ""]
    for cat in list(SECTION_TITLES):
        group = [e for e in allm if e["category"] == cat]
        if not group:
            continue
        lines += [f"## {SECTION_TITLES[cat]} ({len(group)})", ""]
        for e in group:
            lines += ["---", "", f"### {e['subject']}", "",
                      f"**From:** {e['sender']}  ", f"**Received (UTC):** {e['received_utc']}  ",
                      f"**Why pulled:** {e['reason']}  ", f"**Link:** [{e['gmail_link']}]({e['gmail_link']})", "",
                      e["body"], ""]
    if not allm:
        lines += ["*No AI newsletters in this window yet.*", ""]
    mpath = RAW_OUTPUT_DIR / f"{target_date}-newsletters.md"
    mpath.write_text("\n".join(lines), encoding="utf-8")
    return mpath, len(allm)


def main():
    ap = argparse.ArgumentParser(description="Auto-pull AI newsletters from Gmail into raw/gmail/")
    ap.add_argument("--hours", type=int, default=None, help="Force an N-hour window (ignores last-run state)")
    ap.add_argument("--dry-run", action="store_true", help="Classify and print; write nothing, keep state")
    args = ap.parse_args()

    now_utc = datetime.now(timezone.utc)
    now_local = datetime.now()
    start = window_start(now_utc, args.hours)
    target = target_digest_date(now_local)
    seen = set(_load(SEEN_FILE, []))
    print(f"Gmail newsletters | window since {start.strftime('%Y-%m-%d %H:%M UTC')} | routing to {target} digest")

    service = build("gmail", "v1", credentials=get_credentials(), cache_discovery=False)
    ids, kept, skipped = fetch(service, start, set() if args.dry_run else seen)
    print(f"  scanned {len(ids)} new message(s) | keeping {len(kept)} | skipped {skipped}")

    if args.dry_run:
        for _, cat, reason, h in sorted(kept, key=lambda k: k[1]):
            print(f"   [{cat:14s}] {h.get('from', '')[:42]:42s} | {h.get('subject', '')[:60]}  ({reason})")
        return

    emails = hydrate(service, kept)
    path, total = write_outputs(emails, target)
    STATE_DIR.mkdir(exist_ok=True)
    SEEN_FILE.write_text(json.dumps(sorted(seen | set(ids))[-8000:]))
    LAST_RUN_FILE.write_text(json.dumps({"ts": now_utc.isoformat()}))
    print(f"  +{len(emails)} new | {total} total in {path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
