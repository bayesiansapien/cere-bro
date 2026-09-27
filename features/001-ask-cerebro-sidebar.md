# 001 · Ask cere-bro: search + chat sidebar grounded in the wiki

**Status:** Parked (next up) · **Raised:** 2026-09-27

## Why

While listening to a podcast or reading a digest, the reader wants to look something up (a paper, a concept, "what did we say about KV cache offload?") without scrolling through pages or opening a separate Claude session. Today that means manual search or coming back to the terminal.

## What

A collapsible **sidebar on every page of the site** (expands from the edge, stays out of the way when closed) with two modes:

1. **Search:** keyword search across the wiki (digests, Media Zones, concept pages, summary pages) returning ranked links with snippets. Instant, works offline, no model call.
2. **Ask:** a natural-language question gets a **short synthesized answer** plus **grounding citations**: the exact wiki pages (and their underlying raw sources: paper, post, newsletter) the answer came from, as clickable links. No citation, no claim.

## How (initial design)

- **Retrieval index** built at site-build time from `wiki/**` (title, date, topic, summary, chunked body, links to sources). Shipped as a static JSON index; search mode runs fully client-side.
- **Answering backend powered by Claude Code** (the reader's preference): a small local service that receives the question plus the top-K retrieved chunks, runs Claude Code headlessly to synthesize a grounded answer, and returns answer + citations. Options to evaluate:
  - a local HTTP bridge on the Mac (works when the Mac is on; no API key in the browser);
  - tunnelling that bridge so the public site can reach it (auth required);
  - a serverless function holding a key in its own secret store (never in the repo).
- **Grounding contract:** every sentence in an answer must map to a retrieved chunk; the UI shows the source list under the answer; unsupported questions return "not in the wiki" rather than a guess.
- **Secrets policy applies:** no key ever in the repo or the browser bundle.

## Open questions

- Hosting of the answer bridge (local-only vs tunnel vs serverless) and its auth.
- Index granularity (page vs section chunks) and refresh cadence (every build vs nightly).
- Should answers be able to follow links into raw sources (papers, newsletters) or stay within the wiki?
