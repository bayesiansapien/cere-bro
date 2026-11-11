#!/usr/bin/env python3
"""
Cerebro Daily: a compressed email edition of one day's digest.

Reads wiki/daily-digest/YYYY-MM/YYYY-MM-DD.md and builds a short HTML email:
framing line, Today's 5, TL;DR, every Deep Dive (hook + top takeaways + source
links), Industry Pulse, and the Global View headlines.

Links point only at the original sources (arXiv, blogs, X, news sites). Wiki
links and GitHub-hosted links are dropped, so the email works on networks
that block GitHub.

Run:  python3 connectors/newsletter/build.py YYYY-MM-DD   (writes out/YYYY-MM-DD.html)
"""

import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
REPO = HERE.parent.parent
CFG = json.loads((HERE / "config.json").read_text())
OUT = HERE / "out"

BLOCKED_HOSTS = tuple(CFG.get("blocked_link_hosts", ["github.com", "github.io", "githubusercontent.com"]))
LINK_RX = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
# Brand palette, matched to the cere-bro site: amber accent, dark-cyan links (the
# logo's cyan, darkened for white paper). logo.png is the dark-ink logo variant.
ACCENT, LINK, RULE = "#d97706", "#0e7490", "#f1e4cc"
LOGO_CID = "cerebro-logo"


def ok_url(u):
    if not u.startswith("http"):
        return False                      # relative wiki links
    host = re.sub(r"^https?://", "", u).split("/")[0].lower()
    return not any(host == b or host.endswith("." + b) for b in BLOCKED_HOSTS)


def inline(md):
    """Markdown inline (bold, italics, links) to HTML; drops blocked links but keeps their text."""
    out, pos = [], 0
    for m in LINK_RX.finditer(md):
        out.append(html.escape(md[pos:m.start()]))
        text, url = m.group(1), m.group(2)
        out.append(f'<a href="{html.escape(url)}" style="color:{LINK}">{html.escape(text)}</a>'
                   if ok_url(url) else html.escape(text))
        pos = m.end()
    out.append(html.escape(md[pos:]))
    s = "".join(out)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+)`", r"\1", s)
    s = re.sub(r"\(\s*\)", "", s)          # "( )" left behind by a dropped link
    return s.strip()


def html_li(li):
    """A Today's-5 <li> from the digest: keep text and allowed anchors only."""
    verb = (re.search(r'class="verb [a-z]+">([^<]+)<', li) or [None, ""])[1]
    li = re.sub(r'<span class="verb[^"]*">[^<]*</span>', "", li)
    def a(m):
        return f'<a href="{m.group(1)}" style="color:{LINK}">{m.group(2)}</a>' if ok_url(m.group(1)) else m.group(2)
    li = re.sub(r'<a href="([^"]+)"[^>]*>(.*?)</a>', a, li)
    li = re.sub(r"<(?!/?(a|strong)\b)[^>]+>", "", li)
    return verb, li.strip()


def sections(md):
    parts, cur = {}, None
    for line in md.split("\n"):
        h = re.match(r"^## (.+)$", line)
        if h:
            cur = h.group(1).strip()
            parts[cur] = []
        elif cur:
            parts[cur].append(line)
    return {k: "\n".join(v) for k, v in parts.items()}


def bullets(block):
    return [l[2:].strip() for l in block.split("\n") if l.startswith("- ")]


def deep_dives(block, n_take):
    items = []
    for chunk in re.split(r"(?m)^### ", block)[1:]:
        lines = chunk.split("\n")
        title = lines[0].strip()
        hook = next((l[1:].strip() for l in lines[1:] if l.startswith(">")), "")
        links_line = next((l for l in lines if l.startswith("**Links:**")), "")
        links = [(t, u) for t, u in LINK_RX.findall(links_line) if ok_url(u)]
        take, grab = [], False
        for l in lines:
            if l.startswith("**Key takeaways**"):
                grab = True
                continue
            if grab:
                if l.startswith("- "):
                    take.append(l[2:].strip())
                elif l.startswith("**") and take:
                    break
        items.append({"title": title, "hook": hook, "links": links, "take": take[:n_take]})
    return items


def pulse(block, max_general):
    """Industry Pulse: general bullets (capped) + every bullet under bold sub-heads (funding, chips)."""
    groups, cur = [("", [])], None
    for l in block.split("\n"):
        h = re.match(r"^\*\*([^*]+)\*\*\s*$", l.strip())
        if h:
            groups.append((h.group(1), []))
        elif l.startswith("- "):
            groups[-1][1].append(l[2:].strip())
    head, rest = groups[0], groups[1:]
    return [(head[0], head[1][:max_general])] + rest if head[1] else rest


NUM_RX = re.compile(r"\$\d[\d.,]*[KMBT]?|\d+(?:\.\d+)?(?:x|%)")


def nums(text):
    """Distinctive figures in a line ($64.4B, 2.6x, 46%), used to spot repeats."""
    return set(NUM_RX.findall(text))



def build(date, logo_src=f"cid:{LOGO_CID}"):
    p = REPO / "wiki" / "daily-digest" / date[:7] / f"{date}.md"
    md = p.read_text()
    framing = (re.search(r"(?m)^> (.+)$", md) or [None, ""])[1]
    framing = re.split(r"(?<=[.!?])\s+", framing.strip())[0]   # the theme only; the items follow below
    lis = re.findall(r"<li>(.*?)</li>", md.split("## TL;DR")[0], re.S)
    sec = sections(md)
    dd = deep_dives(sec.get("Deep Dives", ""), CFG.get("takeaways_per_deep_dive", 2))
    pl = pulse(sec.get("Industry Pulse", ""), CFG.get("max_pulse_bullets", 14))
    gv = re.findall(r"(?m)^\*\*(.+?)\*\*", sec.get("Global View", ""))
    brand, purple = CFG.get("brand", "Cerebro"), ACCENT

    H = []
    w = H.append
    w('<div style="max-width:680px;margin:0 auto;font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif;'
      'color:#1b1b1b;font-size:15px;line-height:1.55">')
    # Header renders the same with or without background colours (print view and
    # some mail clients drop them): dark-ink logo on white, amber rule underneath.
    w(f'<div style="padding:20px 22px 12px;text-align:center;border:1px solid {RULE};border-bottom:3px solid {ACCENT};border-radius:10px 10px 0 0">'
      f'<img src="{logo_src}" alt="{brand}" width="240" style="display:block;margin:0 auto;width:240px;max-width:70%;height:auto;border:0">'
      f'<div style="font-size:12px;letter-spacing:3px;font-weight:700;color:{ACCENT};margin-top:10px">{brand.upper()} DAILY &middot; {date}</div>'
      f'<div style="font-size:13px;color:#666;margin-top:2px">{html.escape(CFG.get("tagline", ""))}</div></div>')
    w(f'<div style="border:1px solid {RULE};border-top:none;padding:18px 22px;border-radius:0 0 10px 10px">')
    if framing:
        w(f'<p style="font-style:italic;color:#444;border-left:3px solid {purple};padding-left:12px;margin-top:0">{inline(framing)}</p>')

    def h2(t):
        w(f'<h2 style="font-size:17px;color:{purple};border-bottom:1px solid {RULE};padding-bottom:4px;margin:22px 0 10px">{t}</h2>')

    if lis:
        h2("Today's 5 for you")
        # A table, not <ol>: mail clients pad list markers unpredictably, which left
        # a wide gap after "1.". Number, badge and text now sit tight together.
        w('<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;width:100%">')
        colors = {"Read": "#2f9e44", "Skim": "#1971c2", "Track": "#f08c00"}
        for n, li in enumerate(lis, 1):
            verb, body = html_li(li)
            c = colors.get(verb, purple)   # outlined, not filled, so it survives clients that strip backgrounds
            badge = (f'<span style="color:{c};border:1px solid {c};font-size:10.5px;font-weight:700;letter-spacing:.5px;'
                     f'padding:0 5px;border-radius:4px;margin-right:6px;white-space:nowrap">{verb.upper()}</span>') if verb else ""
            w(f'<tr><td style="vertical-align:top;width:18px;padding:0 4px 9px 0;font-weight:700;color:{purple}">{n}.</td>'
              f'<td style="vertical-align:top;padding:0 0 9px 0;line-height:1.55">{badge}{body}</td></tr>')
        w("</table>")
    # The email is pruned for zero repetition (2026-11-11). The digest's TL;DR is
    # left out: every bullet is already in Today's 5, a Deep Dive, or Industry Pulse.
    # Deep Dives already in Today's 5 appear as title + source link, no re-summary.
    top_urls = set(re.findall(r'href="([^"]+)"', " ".join(lis)))
    tl = bullets(sec.get("TL;DR", ""))   # used only for the subject line
    if dd:
        h2("All papers and posts")
        for d in dd:
            urls = [u for _, u in d["links"]]
            title = inline(d["title"])
            if urls:
                title = f'<a href="{html.escape(urls[0])}" style="color:#1b1b1b;text-decoration:none">{title}</a>'
            more = " · ".join(f'<a href="{html.escape(u)}" style="color:{LINK}">{html.escape(t)}</a>' for t, u in d["links"])
            w(f'<div style="margin-bottom:10px"><div style="font-weight:700">{title}</div>')
            if d["hook"] and not set(urls) & top_urls:
                w(f'<div style="color:#444;font-size:14px">{inline(d["hook"])}</div>')
            if more:
                w(f'<div style="font-size:13px">{more}</div>')
            w("</div>")
    seen_nums, pruned = [], []
    for name, bs in pl:
        keep = []
        for b in bs:
            n = nums(b)
            if any(len(n & prev) >= 2 for prev in seen_nums):
                continue          # same story told twice (e.g. a headline and its funding line)
            seen_nums.append(n)
            keep.append(b)
        if keep:
            pruned.append((name, keep))
    pl = pruned
    if pl:
        h2("Industry Pulse")
        for name, bs in pl:
            if name:
                w(f'<div style="font-weight:700;margin:10px 0 4px">{html.escape(name)}</div>')
            w('<ul style="padding-left:20px;margin:0;font-size:14px">' + "".join(
                f'<li style="margin-bottom:3px">{inline(b)}</li>' for b in bs) + "</ul>")
    if gv:
        h2("Global View")
        w('<ul style="padding-left:20px;margin:0">' + "".join(f"<li>{inline(g)}</li>" for g in gv) + "</ul>")
    foot = CFG.get("podcast_url")
    w(f'<div style="margin-top:24px;padding-top:10px;border-top:1px solid {RULE};font-size:12.5px;color:#666">'
      f'<strong style="color:{purple}">{brand}</strong> · {html.escape(CFG.get("footer", ""))}'
      + (f' · 🎧 <a href="{foot}" style="color:{LINK}">{brand} Radio on Spotify</a>' if foot else "")
      + "</div></div></div>")
    page = "\n".join(H)
    leads = [re.sub(r"\*\*|\[|\]\([^)]*\)", "", b).split(":")[0].strip() for b in tl[:3]]
    subject = f"{brand} Daily | {date}: " + (", ".join(leads) if leads else "today's digest")
    return subject, page


if __name__ == "__main__":
    date = sys.argv[1]
    subject, page = build(date, logo_src="../logo.png")   # local preview; the sent email embeds the logo inline
    OUT.mkdir(exist_ok=True)
    (OUT / f"{date}.html").write_text(page)
    (OUT / f"{date}.subject.txt").write_text(subject)
    print(subject)
    print(OUT / f"{date}.html")
