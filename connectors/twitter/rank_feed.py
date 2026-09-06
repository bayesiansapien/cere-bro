#!/usr/bin/env python3
"""
Feed pre-ranker for the social-media agent.

Reads the PRIVATE captured X home feed (raw/twitter/feed/<date>-<slot>.json) and
computes engagement EVIDENCE + grift/off-topic flags for each post, so the
downstream synthesis (the LLM) applies real judgment on a pre-scored, pre-trimmed
candidate set instead of eyeballing 100+ raw posts. This is deterministic
evidence, NOT the verdict — the synthesis makes the final call.

Key design (matches the reader's "engagement but not pure stats" ask):
  - Engagement RATE (eng / views) normalizes away reach — a small account's
    high-rate post beats a big account's baseline-viral one. Views are reliably
    present in the payload, so this is the robust normalizer (follower count is
    nested inconsistently and often missing).
  - Velocity (eng / hours since post) catches rising signal early.
  - Controversy flag (replies dominate likes) = contested, not endorsed.
  - Grift/off-topic patterns are down-weighted hard (the "10 repos that print
    money" / trading-bait problem seen in the raw feed).
  - Artifact links (arxiv/github/blog) get a researcher-value boost.

Nothing is deleted — every post keeps its scores and reasons, split into
`candidates` (surface these) and `long_tail` (capture, don't foreground).

Run:  python3 connectors/twitter/rank_feed.py [YYYY-MM-DD] [--slot night]
      python3 connectors/twitter/rank_feed.py            # newest feed file
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

FEED_DIR = Path(__file__).resolve().parents[2] / "raw" / "twitter" / "feed"

# ── Tier keywords (from the Reader Profile) — a cheap first-pass topic guess.
TIER1 = ["routing", "kv cache", "kv-cache", "quantization", "quantis", "distill",
         "pruning", "compression", "flashattention", "flash attention", "kernel",
         "cuda", "gpu", "hopper", "blackwell", "semiconductor", "hbm", "wafer",
         "inference", "speculative decoding", "moe", "mixture of experts",
         "attention", "throughput", "latency", "tokens per", "token cost", "vllm"]
TIER2 = ["llm", "language model", "transformer", "ssm", "mamba", "agent", "rlhf",
         "rlvr", "grpo", "fine-tun", "alignment", "interpretability", "safety",
         "reasoning", "benchmark", "context window", "long context", "harness"]
TIER3 = ["vision", "image", "video", "audio", "speech", "multimodal", "diffusion",
         "vlm", "text-to-image", "text to video"]

# ── Grift / low-signal patterns (down-weight hard).
GRIFT = [
    r"print money", r"while you sleep", r"passive income", r"\bmoney\b.*\bsleep\b",
    r"\d+\s+(github\s+)?repos?\s+(that|you)", r"here'?s what i (learned|discovered)",
    r"steal my", r"\bhack\b.*\bproductiv", r"changed my life", r"you'?re doing .* wrong",
    r"nobody (is )?talking about", r"before it'?s too late", r"blow(s)? your account",
    r"position siz", r"\bcrypto\b", r"\baltcoin\b", r"\bwatch this\b", r"thread\s*🧵",
    r"follow me", r"drop a (comment|like)", r"bookmark this", r"\bgiveaway\b",
]
# ── Off-topic (not AI/tech at all) — drop from the AI feed entirely.
OFFTOPIC = [r"\btrading\b", r"\bforex\b", r"\bstocks?\b.*\bportfolio\b",
            r"weight loss", r"\bdiet\b", r"real estate", r"dropship"]

AI_ANY = TIER1 + TIER2 + TIER3 + ["ai ", " ai", "openai", "anthropic", "deepmind",
        "gemini", "claude", "gpt", "grok", "llama", "qwen", "mistral", "hugging",
        "arxiv", "paper", "model", "research", "neural", "training", "dataset"]


def _has(text, patterns):
    t = text.lower()
    return sum(1 for p in patterns if re.search(p, t))


def _hours_since(iso):
    if not iso:
        return 24.0
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        return max(0.5, (datetime.now(timezone.utc) - dt).total_seconds() / 3600.0)
    except Exception:
        return 24.0


def score_post(p):
    e = p.get("engagement", {})
    likes, rts = e.get("likes", 0), e.get("retweets", 0)
    replies, quotes = e.get("replies", 0), e.get("quotes", 0)
    views = max(e.get("views", 0), 1)
    text = p.get("text", "") or ""
    urls = p.get("urls", []) or []
    has_article = any(a.get("content") for a in (p.get("articles") or []))

    # weighted engagement (RT/quote worth more than a like: they cost more)
    eng = likes + 2.0 * rts + 1.5 * quotes + 0.5 * replies
    eng_rate = eng / views                      # reach-normalized (the key signal)
    velocity = eng / _hours_since(p.get("date_utc"))
    controversy = replies > max(likes, 1) * 0.6 and replies > 15

    # topic tier (best match)
    t1, t2, t3 = _has(text, TIER1), _has(text, TIER2), _has(text, TIER3)
    tier = 1 if t1 else (2 if t2 else (3 if t3 else 4))
    is_ai = _has(text, AI_ANY) > 0 or bool(urls)

    grift = _has(text, GRIFT)
    offtopic = _has(text, OFFTOPIC) > 0 or (not is_ai and grift)

    has_artifact = any(re.search(r"arxiv\.org|github\.com|/abs/|\.pdf", u) for u in urls) or has_article

    # Composite candidate score — evidence for the synthesis, not the verdict.
    score = 0.0
    score += {1: 40, 2: 22, 3: 8, 4: 0}[tier]          # topic fit dominates
    score += min(eng_rate * 4000, 30)                   # reach-normalized engagement
    score += min(velocity / 50, 12)                     # rising signal
    score += 14 if has_artifact else 0                  # researcher value
    score += 6 if quotes > rts * 0.3 and quotes > 5 else 0  # substantive amplification
    score -= grift * 18                                 # grift penalty (hard)
    score -= 8 if controversy else 0                    # contested, flag not boost
    if offtopic:
        score -= 100                                    # effectively drops it

    reasons = []
    if tier <= 2: reasons.append(f"tier{tier}")
    if has_artifact: reasons.append("artifact")
    if eng_rate > 0.005: reasons.append(f"eng-rate {eng_rate*100:.1f}%")
    if velocity > 200: reasons.append("rising")
    if controversy: reasons.append("CONTESTED")
    if grift: reasons.append(f"grift×{grift}")
    if offtopic: reasons.append("OFF-TOPIC")

    return {
        "handle": p.get("handle"), "link": p.get("link"), "text": text,
        "is_retweet": p.get("is_retweet", False),
        "tier": tier, "score": round(score, 1),
        "eng": {"likes": likes, "rts": rts, "replies": replies, "quotes": quotes, "views": views},
        "eng_rate_pct": round(eng_rate * 100, 2), "velocity": round(velocity, 1),
        "has_artifact": has_artifact, "controversy": controversy,
        "grift": grift, "offtopic": offtopic, "urls": urls,
        "articles": [a for a in (p.get("articles") or []) if a.get("content")],
        "reasons": reasons,
    }


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    slot = None
    if "--slot" in sys.argv:
        slot = sys.argv[sys.argv.index("--slot") + 1]
    if args:
        date = args[0]
        cands = sorted(FEED_DIR.glob(f"{date}-*.json"))
        path = ([c for c in cands if slot and slot in c.name] or cands or [None])[-1]
    else:
        files = sorted(FEED_DIR.glob("*.json"))
        path = files[-1] if files else None
    if not path or not path.exists():
        print("No feed file found in", FEED_DIR)
        return 1

    data = json.loads(path.read_text())
    posts = data.get("posts", [])
    scored = [score_post(p) for p in posts]
    scored.sort(key=lambda x: x["score"], reverse=True)

    candidates = [s for s in scored if s["score"] >= 25 and not s["offtopic"]]
    long_tail = [s for s in scored if s not in candidates and s["tier"] <= 2 and not s["offtopic"]]

    out = {"date": data.get("date"), "slot": data.get("slot"), "source_file": path.name,
           "total": len(scored), "candidates": candidates, "long_tail": long_tail[:40]}
    out_path = path.with_name(path.stem + "-ranked.json")
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False))

    print(f"Ranked {len(scored)} posts from {path.name}")
    print(f"  candidates (surface): {len(candidates)} | long-tail (capture): {len(long_tail)}")
    print(f"  dropped off-topic/grift: {sum(1 for s in scored if s['offtopic'])}")
    print(f"  wrote {out_path.name}\n")
    print("  TOP 12 CANDIDATES (score | tier | signals | text):")
    for s in candidates[:12]:
        e = s["eng"]
        print(f"   {s['score']:5.1f} T{s['tier']} [{','.join(s['reasons'])[:38]:38}] "
              f"@{s['handle'][:14]:14} {s['text'][:52]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
