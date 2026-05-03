# cere-bro skills package — parked plan

**Status:** parked for later. Not active work.

**Goal:** package the cere-bro workflow as a Claude Code plugin so teammates can install it and bootstrap their own research wiki without rebuilding the workflow from scratch.

---

## Skill decomposition

Five skills cover the entire workflow. Each is independently usable.

### 1. `cere-bro:bootstrap`
Initializes a new wiki directory.
- Creates directory layout: `raw/{huggingface,rss,gmail}/`, `wiki/<topic>/`, `wiki/daily-digest/YYYY-MM/`, `connectors/`, `site/`
- Prompts user for *their* Tier 1/2/3/4 topics (don't hardcode Amit's routing/KV/distillation/GPU)
- Generates a customized `CLAUDE.md` from a template, filled with their tier hierarchy
- Creates empty concept page stubs for their declared Tier 1 topics
- Creates `wiki/index.md` and `wiki/log.md` skeletons

### 2. `cere-bro:ingest`
Processes a single raw source into the wiki.
- Input: a path to a `raw/**/*.md` file, or auto-discover the latest unprocessed
- Reads relevant concept pages first (knowledge synthesis rule from CLAUDE.md)
- Writes summary page in `wiki/<topic>/<date>-<slug>.md`
- Updates concept pages — adds new evidence, contradictions, refinements
- Updates `index.md` and appends to `log.md`
- Surfaces cross-paper patterns ("3rd paper this month doing X")

### 3. `cere-bro:digest`
Writes the daily digest.
- Input: a date (YYYY-MM-DD), or default to today
- Reads ALL three raw source dirs (huggingface, rss, gmail) for that date — uses most recent if exact date missing (matches CLAUDE.md step 0b)
- Reads relevant concept pages + last 5–7 digests for context
- Writes `wiki/daily-digest/YYYY-MM/YYYY-MM-DD.md` in the newsletter format from CLAUDE.md
- Hits all the structural sections: TL;DR, Big Picture, Deep Dives, Industry Pulse, Connecting the Dots, Worth Watching, Quick Hits

### 4. `cere-bro:publish`
Sets up the Astro site portal.
- Clones the `site/` template structure
- Configures `astro.config.mjs` with their GitHub username + repo name (base path)
- Adds `.github/workflows/deploy-pages.yml`
- Reminds them to: make repo public, enable Pages from Actions, push
- Optional: walks them through custom domain setup

### 5. `cere-bro:lint`
Health check on an existing wiki.
- Flags orphan summary pages (no links to any concept page)
- Identifies concepts mentioned in ≥3 sources but lacking their own page
- Finds concept pages not updated across ≥3 ingests in their area
- Checks `index.md` for missing or stale entries
- Suggests sources/topics worth investigating next

---

## Distribution

Package as a **Claude Code plugin** (the bundle format that includes skills + slash commands).

### Repo structure
```
cere-bro-plugin/
├── plugin.json                # Manifest: name, version, author
├── README.md                  # Installation + usage walkthrough
├── skills/
│   ├── bootstrap/SKILL.md
│   ├── ingest/SKILL.md
│   ├── digest/SKILL.md
│   ├── publish/SKILL.md
│   └── lint/SKILL.md
├── commands/                  # /cere-bro:* slash commands
│   ├── bootstrap.md
│   ├── ingest.md
│   └── digest.md
└── templates/                 # Resources skills copy from
    ├── CLAUDE.md.template     # With {{TIER_1_TOPICS}} etc placeholders
    ├── site/                  # Astro template
    └── connectors/            # Farmer Python scripts (template, no creds)
```

### Teammate install + use flow
```bash
# One-time install
/plugin install github:bayesiansapien/cere-bro-plugin

# In a new project directory
cd ~/my-research-wiki
/cere-bro:bootstrap

# After dropping a paper or RSS file into raw/
/cere-bro:ingest

# At end of day
/cere-bro:digest

# Set up the public site
/cere-bro:publish
```

The same skills produce different wikis for different users because each user's `CLAUDE.md` (written by `bootstrap`) encodes their personal attention hierarchy.

---

## What needs to be extracted from current cere-bro

When building the plugin, pull these patterns from the live repo:

| Source in cere-bro | Goes into |
|--------------------|-----------|
| `CLAUDE.md` (steps 0–7, knowledge synthesis rules, daily digest format) | `templates/CLAUDE.md.template` (parameterized) + `skills/*/SKILL.md` instructions |
| `connectors/gmail/`, RSS / HF farmer scripts | `templates/connectors/` |
| `site/` (Astro structure) | `templates/site/` |
| `.github/workflows/deploy-pages.yml` | `templates/site/.github/workflows/` |

---

## Effort estimate
~2–3 focused hours when picked up. Most of the work is extraction, not invention — the patterns already exist in the live cere-bro and just need to be parameterized and packaged.

## When to revisit
After cere-bro itself feels solid — the wiki workflow is stable, the site is polished, the user is confident in the daily flow. No point packaging an unfinished workflow.
