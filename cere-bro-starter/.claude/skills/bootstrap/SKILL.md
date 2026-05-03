# bootstrap

One-time setup wizard. Collects the user's wiki configuration, creates the wiki directory structure, generates a customized `CLAUDE.md` and `wiki-config.json`, sets up the Astro site, and copies connector scripts.

---

## Instructions

When this skill is invoked, follow these steps in order. Do not skip steps. Do not assume answers — ask each question and wait for the user's response.

---

### Phase 1: Collect configuration

Ask the following questions one at a time. Acknowledge each answer before moving to the next.

**Q1. Wiki name**
> "What do you want to call your wiki? (This becomes the site title and brand name — e.g. 'neuro-lab', 'quant-brain', 'ml-notes')"

**Q2. Your name and role**
> "What's your name, and what's your background? (e.g. 'Sarah, ML engineer at a startup', 'David, PhD student in NLP', 'Priya, AI product manager')"
> This goes into the Reader Profile in CLAUDE.md and calibrates how deep explanations go.

**Q3. Topics and tiers**
> "What are the research or domain areas you want to track? List them with a rough priority — which ones do you want deep coverage on (Tier 1), standard coverage (Tier 2), light coverage (Tier 3), and anything you want to flag as low priority (Tier 4)?
>
> Example format:
> - Tier 1 (deep): transformers, fine-tuning, RLHF
> - Tier 2 (standard): multimodal models, agents
> - Tier 3 (light): robotics, 3D vision
> - Tier 4 (skip): game benchmarks, hardware reviews
>
> You can always adjust this later by editing your CLAUDE.md."

Wait for the user's full tier list. Parse it carefully — identify the topic names and their tier assignments.

**Q4. Industry tracking**
> "Do you want to track industry news (funding rounds, product launches, regulation, company moves)? If yes, I'll add an Industry section to your wiki and Atlas dashboard."

**Q5. Sources**
> "Which sources will you use? Check all that apply:
> - HuggingFace Daily Papers (ML paper feed)
> - RSS feeds (blogs, newsletters — you'll add your own URLs)
> - Gmail starred emails (AI newsletters you forward to yourself)
> - Manual drops (you drop files into raw/ yourself)
>
> You can enable all of them. Farmers for each are included in the connectors/ folder."

**Q6. GitHub deployment**
> "What's your GitHub username and the repo name you'll use for this wiki? (e.g. username: johndoe, repo: my-research-wiki)
>
> The site will deploy to https://johndoe.github.io/my-research-wiki/
> If you're not deploying yet, you can skip this and update astro.config.mjs later."

---

### Phase 2: Confirm and summarize

Before writing anything, show the user a summary of what you're about to create:

```
Here's what I'll set up:

Wiki name: <name>
Reader: <name, role>
Topics:
  Tier 1 (deep dives): <list>
  Tier 2 (standard): <list>
  Tier 3 (light): <list>
  Tier 4 (skip): <list>
Industry tracking: yes/no
Sources: <list>
Site: https://<username>.github.io/<repo>/

Directory structure:
  wiki/<topic>/ for each Tier 1–3 topic
  wiki/daily-digest/
  wiki/index.md, wiki/log.md
  connectors/ with farmer scripts
  site/ with Astro project

Shall I proceed?
```

Wait for confirmation before writing any files.

---

### Phase 3: Write wiki-config.json

Write `wiki-config.json` to the repo root. This file is read by `site/scripts/build-data.mjs` to configure topic colors, tier assignments, and industry tags.

Choose distinct colors for each topic. Use a visually distinct palette:
- Tier 1 topics: warm/bright colors (amber #f59e0b, emerald #10b981, violet #8b5cf6, rose #f43f5e, orange #f97316)
- Tier 2 topics: medium saturation (blue #3b82f6, pink #ec4899, indigo #6366f1, teal #14b8a6)
- Tier 3 topics: cooler/dimmer (cyan #06b6d4, sky #0ea5e9, stone #a8a29e)
- Tier 4 topics: muted (#64748b, #78716c)
- Industry (if enabled): slate #94a3b8
- Daily digest: gold #fbbf24

The wiki-config.json format:

```json
{
  "wikiName": "<wiki-name>",
  "githubUsername": "<github-username>",
  "githubRepo": "<repo-name>",
  "readerName": "<first-name>",
  "readerRole": "<full role description>",
  "topics": [
    {
      "key": "<topic-key>",
      "label": "<display label>",
      "tier": 1,
      "color": "#f59e0b",
      "description": "<one-line description of what this topic covers>"
    }
  ],
  "industryEnabled": true,
  "sources": {
    "huggingface": true,
    "rss": true,
    "gmail": false
  }
}
```

Rules for `key`: lowercase, hyphens only, no spaces. E.g. "transformer-architectures", "rl-theory", "nlp-applications".

---

### Phase 4: Create wiki directory structure

For each Tier 1, 2, and 3 topic (skip Tier 4), create the wiki subdirectory. Also create ai-industry/ if industry is enabled.

Create these files:

**wiki/index.md**
```markdown
# Wiki Index

Catalog of all pages in this wiki. Updated automatically on every ingest.

---
```

**wiki/log.md**
```markdown
# Ingest Log

Append-only timeline of all ingested sources and wiki updates.

---
```

**wiki/<topic-key>/<topic-key>.md** (concept page stub for each Tier 1 topic):
```markdown
# <Topic Label>

> Concept page — updated as new sources are ingested.

## Current state of knowledge

*No entries yet. This page will be updated when the first source on this topic is ingested.*

## Open questions

*To be populated during ingest.*

## Key sources

*To be populated during ingest.*
```

---

### Phase 5: Write the customized CLAUDE.md

Write a new `CLAUDE.md` to the repo root, replacing the starter one. This is the most important output — it will guide every future Claude Code session.

The CLAUDE.md template is in `templates/CLAUDE.md.template`. Use that as the base, filling in:
- `{{WIKI_NAME}}` → user's wiki name
- `{{READER_NAME}}` → user's name
- `{{READER_ROLE}}` → user's role description
- `{{TIER_TABLE}}` → formatted tier table with their topics
- `{{TIER_1_DETAIL}}` → Tier 1 topics with descriptions
- `{{TIER_2_DETAIL}}` → Tier 2 topics
- `{{TIER_3_DETAIL}}` → Tier 3 topics
- `{{TIER_4_DETAIL}}` → Tier 4 topics (or "nothing in this tier" if empty)
- `{{WIKI_TOPICS_LIST}}` → the wiki/ subdirectory structure
- `{{GITHUB_USERNAME}}` → GitHub username
- `{{GITHUB_REPO}}` → repo name
- `{{INDUSTRY_SECTION}}` → include the ai-industry/ section if enabled, or omit

If the template file is unavailable, write the CLAUDE.md directly using the structure below. The key sections:
1. Reader Profile with the tier table
2. Architecture (directory layout with their actual topic folders)
3. Sources section listing which ones they enabled
4. Ingest instructions (steps 0–7)
5. Daily Digest format (full format from the template)
6. Writing rules
7. Conventions

---

### Phase 6: Set up the site

Copy the Astro project from `templates/site/` to `site/` in the repo root.

After copying, update these files:

**site/astro.config.mjs** — replace `<GITHUB_USERNAME>` and `<GITHUB_REPO>`:
```javascript
import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://<github-username>.github.io',
  base: '/<github-repo>',
  trailingSlash: 'ignore',
  build: {
    format: 'directory',
  },
});
```

**site/src/layouts/Base.astro** — replace the wiki name and GitHub link.

The `site/scripts/build-data.mjs` reads `wiki-config.json` from the repo root — no changes needed there.

---

### Phase 7: Set up connectors

Copy `templates/connectors/` to `connectors/` in the repo root.

For each source the user enabled:
- If gmail: explain they need Google OAuth credentials (point to connectors/gmail/README.md)
- If rss: create `connectors/rss/feeds.txt` and ask if they want to add their RSS URLs now
- If huggingface: no setup needed, farmer.py is ready to use

---

### Phase 8: Create .gitignore

Write `.gitignore` to the repo root if it doesn't exist:

```
node_modules/
site/dist/
site/.astro/
connectors/gmail/credentials/
__pycache__/
*.pyc
.env
.DS_Store
```

---

### Phase 9: Final summary

After all files are written, confirm to the user:

```
Bootstrap complete. Here's what was created:

✓ wiki-config.json — your topic configuration
✓ CLAUDE.md — customized for your topics and reading style
✓ wiki/ — empty wiki structure with concept page stubs
✓ site/ — Astro site configured for <username>.github.io/<repo>
✓ connectors/ — farmer scripts for your sources
✓ .gitignore

Next steps:
1. Drop source files into raw/ and run /ingest to build your first wiki pages
2. Run /digest after your first batch of ingests to write your first digest
3. Run /publish when you're ready to deploy the site
4. Set up farmers in connectors/ to automate daily source collection

Your first session: drop 3–5 papers or posts you're excited about into raw/, then /ingest.
```
