<p align="center" style="margin: 8px 0">
  <img src="site/public/cerebro-icon.png" alt="cere-bro" width="280" />
</p>

<p align="center"><strong>The cognitive bro you always needed — reads the papers, tracks the industry, connects the dots, and briefs you every morning like a research partner who never sleeps.</strong></p>

<p align="center">
  <a href="https://bayesiansapien.github.io/cere-bro/">Live site</a> ·
  <a href="https://bayesiansapien.github.io/cere-bro/atlas">Atlas</a> ·
  <a href="https://bayesiansapien.github.io/cere-bro/browse">Wiki Pages</a>
</p>

---

## What it is

cere-bro reads papers, blog posts, newsletters, and RSS feeds every morning and synthesizes them into a structured knowledge base. It writes wiki pages, updates concept pages, and produces a daily digest — all without manual intervention.

The live site updates automatically on every push via GitHub Actions.

---

## How it works

```
raw/          ← farmers drop source files here daily
wiki/         ← Claude writes and maintains everything here
site/         ← Astro site, deployed to GitHub Pages
connectors/   ← Python scripts that pull from sources
```

### Farmers pull from sources

| Source | What it pulls | Auth needed |
|--------|--------------|---|
| HuggingFace Daily Papers | Latest ML paper digests, ranked by community upvotes | None |
| **Kurate.org leaderboards** | Weekly arXiv top-20 ranked by 3-LLM tournament, plus rising-author tracking | None (public API) |
| RSS feeds | Blogs, newsletters (Lilian Weng, Karpathy, SemiAnalysis, TLDR AI, The Decoder, Interconnects, etc.) | None |
| **Twitter/X** | Reposts from your account (curated signal) + AI handle feed (filtered) + 4× daily polling | Optional Apify token for auto-discovery |
| Gmail starred emails | AI Breakfast, Ken Huang, Pragmatic Engineer, Marcus on AI, etc. | Google OAuth (one-time) |
| **alphaxiv.org** (enrichment) | On-demand AI-generated 3000-word paper overviews used to ground Tier 1/2 Deep Dives | None |

Farmers run on a schedule and write files into `raw/`. Claude then ingests them.

### Claude synthesizes the knowledge base

For every new source, Claude:

1. Reads the raw file
2. Writes a **source summary page** in the relevant topic directory (`wiki/<topic>/YYYY-MM-DD-slug.md`)
3. Updates the relevant **concept pages** (`wiki/<topic>/<concept>.md`) with new findings, confirmations, or contradictions
4. Writes or updates the **daily digest** (`wiki/daily-digest/YYYY-MM/YYYY-MM-DD.md`)
5. Updates `wiki/index.md` and appends to `wiki/log.md`
6. Pushes everything to the repo

### The site builds itself

The Astro site reads `wiki/` at build time, parses every markdown file, and generates:

- **Today** — the latest daily digest with sidebar of recent additions
- **Atlas** — topic heatmaps, cumulative growth charts, momentum strips (what's heating up / cooling)
- **Wiki Pages** — tabbed index of every wiki page, grouped by topic

GitHub Actions rebuilds and deploys the site on every push to `main`.

---

## Wiki structure

```
wiki/
├── ai-routing/              # LLM routing, multimodal routing, agent trajectory routing
├── inference-efficiency/    # KV cache, compression, quantization, distillation, GPU opt
├── hardware/                # GPU architecture, Hopper, Blackwell, memory hierarchy
├── llms-foundation-models/  # LLMs, foundation models, new architectures (SSM, MoE, hybrid)
├── agentic-systems/         # Agents, tool use, agentic reasoning, multi-agent
├── responsible-ai/          # Interpretability, alignment, safety, explainability, governance
├── vision-audio-video/      # Multimodal, vision-language, image/video generation, speech
├── ai-industry/             # Company news, funding, policy, regulation
├── social-stream/           # Twitter slot syntheses + daily roll-ups (Media Live)
├── daily-digest/
│   └── YYYY-MM/
│       └── YYYY-MM-DD.md   # One newsletter per day
├── index.md                 # Catalog of every wiki page
└── log.md                   # Append-only ingest timeline
```

The site exposes four tabs: **Today** (latest digest), **Atlas** (topic heatmaps + industry breakdown), **Media Live** (live Twitter feed with synthesized slot summaries), **Wiki Pages** (full catalog).

---

## Running it locally

**1. Pull today's sources**

```bash
python connectors/gmail/farmer.py       # starred Gmail emails
python connectors/rss/farmer.py         # RSS feeds
python connectors/huggingface/farmer.py # HF Daily Papers
```

**2. Open Claude Code and run the digest skill**

```bash
claude
/digest
```

**3. Preview the site**

```bash
cd site
npm install
npm run dev
```

---

## Automated daily run

A macOS LaunchAgent fires at 9am, runs all farmers, then invokes Claude to write the digest and push. The site deploys automatically from the push.

---

## Starting your own

See [`cere-bro-starter/`](./cere-bro-starter/) — a self-contained folder you can copy into a fresh repo and set up with your own topics, tiers, and sources.

**Quick start:**

1. **Fork or clone** this repo, then copy `cere-bro-starter/` contents to your fresh project root.
2. **Open Claude Code** in your project root and run `/bootstrap`. It interviews you for: wiki name, your role, topic tiers (Tier 1 / Tier 2 / Tier 3 areas you care about), industry tracking on/off, source toggles (Gmail / Twitter / Kurate / etc.), GitHub deployment target. Bootstrap then generates your customized `CLAUDE.md`, `wiki-config.json`, and copies all the connector + site templates into place.
3. **Configure secrets**:
   - Copy `.env.example` to `.env` and fill in `TWITTER_BEARER_TOKEN` (optional) and `APIFY_API_TOKEN` (optional, for Twitter auto-discovery)
   - For Gmail: follow `connectors/gmail/README.md` (Google Cloud Console → OAuth client → download JSON → run `python3 connectors/gmail/setup.py`)
4. **Schedule the pipeline**: copy `templates/scripts/*.template` to `~/.local/bin/`, fill in `{{REPO_PATH}}` and `{{CLAUDE_BIN}}`, then load the LaunchAgent plists from `templates/launchagents/`. See `templates/scripts/README.md` for exact commands.
5. **Run the site locally**: `cd site && npm install && npm run dev`. Push to GitHub to deploy via Actions.

After step 5, your wiki is live at `https://<your-username>.github.io/<your-repo>/` and updates daily.
