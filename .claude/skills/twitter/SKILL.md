# /twitter — X/Twitter Ingest Skill

Runs the Twitter farmer and/or ingests existing `raw/twitter/` files into the wiki.

---

## When invoked

`/twitter` — run the farmer for today, then ingest the results into the wiki and update the digest.
`/twitter ingest` — skip the farmer, ingest whatever `raw/twitter/` files exist for today.
`/twitter farm` — run the farmer only, do not ingest.

---

## Step 1: Run the farmer (unless `ingest`-only)

```bash
python3 connectors/twitter/farmer.py
```

If the file for today's slot already exists, the farmer exits cleanly. Use `--force` to re-run.

Check output: `raw/twitter/YYYY-MM-DD-am.md` or `raw/twitter/YYYY-MM-DD-pm.md`

If the farmer fails, check:
- `APIFY_API_TOKEN` in `.env`
- Apify account at console.apify.com for run errors

---

## Step 2: Read raw Twitter files

Find all `raw/twitter/YYYY-MM-DD-*.md` files for today. Read them all.

The file has two sections:
- **@bayesiansapien retweets** — treat these like starred Gmail. These are Amit's curated picks. Every item here is worth reading and potentially ingesting, regardless of AI topic (Amit retweeted it for a reason).
- **AI Account Feed** — tweets from tracked AI handles, pre-filtered by AI keywords. These are original posts and quote tweets from Anthropic, xAI, Google Research, NVIDIA, Cursor, etc.

---

## Step 3: Classify and triage

For each item in the file:

**@bayesiansapien retweets:**
- Include all retweets in the digest regardless of topic
- For retweets with article content attached, treat the article content as the primary source
- For retweets of AI research (papers, blog posts, announcements): write a summary page if substantive enough
- For retweets of non-AI content (opinions, news): include in digest Industry Pulse or Quick Hits

**AI Account Feed:**
- Already keyword-filtered, but apply tier judgment:
  - Tier 1 (routing, KV cache, compression, GPU): Deep Dive candidate
  - Tier 2 (LLMs, agents, architectures): standard treatment
  - Tier 3 (multimodal, etc.): Quick Hit
  - Pure opinion with no substance: skip
- For tweets with article links and content: treat the article as the source, the tweet as the pointer

---

## Step 4: Write wiki pages

For any substantive item (tweet with an article, a paper announcement, a significant industry move):
- Write a summary page in the appropriate `wiki/<topic>/YYYY-MM-DD-slug.md`
- Update relevant concept pages
- Follow the same ingest process as any other raw source

For quick items (opinions, announcements, brief insights):
- Capture in the digest directly without a separate wiki page

---

## Step 5: Update the digest

Add Twitter content to `wiki/daily-digest/YYYY-MM/YYYY-MM-DD.md`:

- **@bayesiansapien retweets** → label the source as "(via @bayesiansapien retweet)" in Industry Pulse or Deep Dive as appropriate
- **AI handle tweets** → label as "(via @handle on X)" 
- Substantive items with article content → Deep Dive or Industry Pulse with the tweet as context
- Brief items → Quick Hits

Treat Twitter content at the same tier level as any other source. A paper linked by @jekbradbury gets the same Deep Dive treatment as one from HuggingFace.

---

## Step 6: Update index and log

Update `wiki/index.md` for any new wiki pages written.

Append to `wiki/log.md`:
```
## [YYYY-MM-DD] twitter | Twitter/X digest | twitter
- Slot: am/pm
- Own retweets: N
- AI handle tweets: N
- Wiki pages written: N
```

---

## Timing context

- **AM run (10am IST)**: captures Amit's morning X session (8-10am IST) retweets + overnight US posts
- **PM run (8pm IST)**: captures US morning/afternoon posts (7:30am-2:30pm PT)

Most tracked accounts are in PT timezone (Anthropic, xAI, Google, NVIDIA, Cursor all in SF/Bay Area). Peak content arrives 9am-6pm PT which is 9:30pm-6:30am IST. The PM farmer run catches the start of this window.
