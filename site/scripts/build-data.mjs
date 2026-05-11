#!/usr/bin/env node
/**
 * Build-time wiki parser.
 * Reads ../wiki/**\/*.md, extracts metadata, generates src/data/wiki.json.
 * Pages and visualizations consume this single JSON.
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import matter from 'gray-matter';
import { marked } from 'marked';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const REPO_ROOT = path.resolve(__dirname, '../..');
const WIKI_DIR = path.join(REPO_ROOT, 'wiki');
const TWITTER_RAW_DIR = path.join(REPO_ROOT, 'raw', 'twitter');
const OUT_FILE = path.join(__dirname, '../src/data/wiki.json');

// Topic colors — one canonical palette
const TOPIC_COLORS = {
  'ai-routing':             '#f59e0b', // amber — Tier 1
  'inference-efficiency':   '#10b981', // emerald — Tier 1
  'hardware':               '#8b5cf6', // violet — Tier 1
  'llms-foundation-models': '#3b82f6', // blue — Tier 2
  'agentic-systems':        '#ec4899', // pink — Tier 2
  'responsible-ai':         '#f43f5e', // rose — Tier 2 (alignment, interpretability, safety)
  'vision-audio-video':     '#06b6d4', // cyan — Tier 3
  'ai-industry':            '#64748b', // slate — industry
  'daily-digest':           '#fbbf24', // gold — digests
};

const TIER_OF_TOPIC = {
  'ai-routing': 1,
  'inference-efficiency': 1,
  'hardware': 1,
  'llms-foundation-models': 2,
  'agentic-systems': 2,
  'responsible-ai': 2,
  'vision-audio-video': 3,
  'ai-industry': 3,
  'daily-digest': 0,
};

// AI industry sub-categories — auto-tagged from title + tldr keywords.
// Order matters: first match wins. Categories are designed to be MUTUALLY
// EXCLUSIVE: a discrete capital event is "deals", an ongoing market dynamic
// is "markets", a chip/datacenter buildout is "infrastructure".
const INDUSTRY_TAGS = [
  {
    key: 'deals',
    label: 'Funding & M&A',
    color: '#f59e0b',
    // Discrete capital events: M&A, fundraising rounds, IPOs, joint ventures
    keywords: ['acquisition', 'acquire', 'acquires', 'merger', 'buyout', 'funding round', 'series a', 'series b', 'series c', 'series d', 'raise', 'raises', 'raised', 'ipo', 'joint venture', 'partnership', 'spinoff', 'divestiture', 'deal', 'closes round'],
  },
  {
    key: 'markets',
    label: 'Revenue & Valuations',
    color: '#10b981',
    // Ongoing business / market dynamics: revenue, valuations, pricing, costs
    keywords: ['valuation', 'arr', 'revenue', 'capex', 'opex', 'margin', 'billion', 'misallocation', 'capital allocation', 'pricing', 'price hike', 'cost', 'economics', 'value capture', 'profit', 'profitability', 'spending', 'unit economics', 'demand', 'monetization', 'tam', 'market size'],
  },
  {
    key: 'regulation',
    label: 'Regulation & Policy',
    color: '#ef4444',
    keywords: ['regulation', 'policy', 'antitrust', 'pentagon', 'ftc', 'court', 'legal', 'ban', 'eu ai act', 'white house', 'congress', 'classified', 'sanctions', 'lawsuit', 'subpoena'],
  },
  {
    key: 'infrastructure',
    label: 'Infrastructure & Compute',
    color: '#8b5cf6',
    // Physical buildout: datacenters, chips, GPUs, fabs
    keywords: ['datacenter', 'data center', 'gpu', 'chip', 'hardware', 'compute', 'gigawatt', 'memory', 'fab', 'tsmc', 'reliability', 'capacity', 'silicon', 'h100', 'b200', 'blackwell', 'hopper'],
  },
  {
    key: 'products',
    label: 'Products & Launches',
    color: '#3b82f6',
    keywords: ['launch', 'launches', 'release', 'released', 'available', 'ships', 'shipped', 'beta', 'preview', 'announcement', 'introduces', 'unveils', 'connector', 'creative work', 'rolls out'],
  },
  {
    key: 'risks',
    label: 'Critique & Risks',
    color: '#94a3b8',
    keywords: ['skeptic', 'critique', 'concern', 'controversy', 'fail', 'failure', 'criticism', 'risk', 'bubble', 'slop', 'dispute', 'trust', 'incident', 'breach', 'vulnerability'],
  },
];

function classifyIndustry(title, tldr) {
  const text = `${title ?? ''} ${tldr ?? ''}`.toLowerCase();
  for (const tag of INDUSTRY_TAGS) {
    if (tag.keywords.some((k) => text.includes(k))) return tag.key;
  }
  return 'other';
}

// ── Date helpers ──────────────────────────────────────────────────────────────

function parseDate(iso) {
  if (!iso) return null;
  return new Date(iso + 'T00:00:00Z');
}

// ISO week starting Monday — return YYYY-MM-DD of the Monday of that week
function weekStartUTC(d) {
  if (!d) return null;
  const day = d.getUTCDay(); // 0 = Sun
  const offset = day === 0 ? 6 : day - 1;
  const ws = new Date(d.getTime() - offset * 24 * 60 * 60 * 1000);
  return ws.toISOString().slice(0, 10);
}

// Build last-N-weeks ordered list of week start dates (oldest first)
function lastNWeeks(n) {
  const today = new Date();
  today.setUTCHours(0, 0, 0, 0);
  const thisMonday = weekStartUTC(today);
  const out = [];
  const start = new Date(thisMonday + 'T00:00:00Z');
  for (let i = n - 1; i >= 0; i--) {
    const d = new Date(start.getTime() - i * 7 * 24 * 60 * 60 * 1000);
    out.push(d.toISOString().slice(0, 10));
  }
  return out;
}

// Build last-N-months as YYYY-MM strings (oldest first, current month last)
function lastNMonths(n) {
  const out = [];
  const today = new Date();
  const y = today.getUTCFullYear();
  const m = today.getUTCMonth(); // 0-indexed
  for (let i = n - 1; i >= 0; i--) {
    const d = new Date(Date.UTC(y, m - i, 1));
    const key = `${d.getUTCFullYear()}-${String(d.getUTCMonth() + 1).padStart(2, '0')}`;
    out.push(key);
  }
  return out;
}

function monthKey(d) {
  if (!d) return null;
  return `${d.getUTCFullYear()}-${String(d.getUTCMonth() + 1).padStart(2, '0')}`;
}

// Build full set of weeks spanning earliest paper date → today
function allWeeks(earliestISO) {
  if (!earliestISO) return lastNWeeks(12);
  const earliest = parseDate(earliestISO);
  const earliestMonday = weekStartUTC(earliest);
  const todayMonday = weekStartUTC(new Date());
  const start = new Date(earliestMonday + 'T00:00:00Z');
  const end = new Date(todayMonday + 'T00:00:00Z');
  const out = [];
  for (let d = start; d.getTime() <= end.getTime(); d = new Date(d.getTime() + 7 * 24 * 60 * 60 * 1000)) {
    out.push(d.toISOString().slice(0, 10));
  }
  return out;
}

function walk(dir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  const files = [];
  for (const e of entries) {
    const p = path.join(dir, e.name);
    // Skip podcast folders entirely — episode notes are Substack drafts, not
    // wiki content. They live in the repo alongside the audio for convenience
    // but should not appear in the digest list or sitemap.
    if (e.isDirectory() && e.name === 'podcasts') continue;
    if (e.isDirectory()) files.push(...walk(p));
    else if (e.isFile() && p.endsWith('.md')) files.push(p);
  }
  return files;
}

function extractDateFromFilename(filename) {
  const m = filename.match(/^(\d{4}-\d{2}-\d{2})/);
  return m ? m[1] : null;
}

function extractTopic(relPath) {
  const parts = relPath.split(path.sep);
  return parts[0]; // first directory under wiki/
}

function extractTitle(content, frontmatter) {
  if (frontmatter.title) return frontmatter.title;
  const h1 = content.match(/^#\s+(.+)$/m);
  if (h1) return h1[1].trim();
  return null;
}

function extractTLDR(content) {
  // Look for a TL;DR section or the first non-heading paragraph
  const tldrMatch = content.match(/##\s+TL;DR\s*\n+([\s\S]+?)(?=\n##|\n---|\Z)/);
  if (tldrMatch) {
    return tldrMatch[1].trim().replace(/\n+/g, ' ').slice(0, 400);
  }
  // First paragraph after H1
  const firstPara = content.match(/^#\s+.+\n+([^\n#].+(?:\n[^\n#].+)*)/m);
  if (firstPara) {
    return firstPara[1].trim().replace(/\n+/g, ' ').slice(0, 400);
  }
  return null;
}

function extractLinks(content, sourcePath) {
  // Match markdown links [text](path.md) — only internal wiki links
  const linkRe = /\[([^\]]+)\]\(([^)]+\.md)\)/g;
  const links = [];
  const sourceDir = path.dirname(sourcePath);
  let m;
  while ((m = linkRe.exec(content)) !== null) {
    const target = m[2];
    // Skip external links
    if (target.startsWith('http')) continue;
    // Resolve relative
    const absoluteTarget = path.resolve(sourceDir, target);
    const relativeFromWiki = path.relative(WIKI_DIR, absoluteTarget);
    if (!relativeFromWiki.startsWith('..')) {
      links.push(relativeFromWiki);
    }
  }
  return [...new Set(links)];
}

function isSourceSummary(filename) {
  // Source summary pages start with a date prefix
  return /^\d{4}-\d{2}-\d{2}/.test(filename);
}

function isConceptPage(filename, topic) {
  // Concept pages don't have a date prefix and aren't index/log
  return (
    !isSourceSummary(filename) &&
    !['index.md', 'log.md'].includes(filename) &&
    topic !== 'daily-digest'
  );
}

function isDigest(relPath) {
  return relPath.startsWith('daily-digest');
}

// ── Social stream (Twitter/X) topic inference ─────────────────────────────────

const TWEET_TOPIC_RULES = [
  { topic: 'responsible-ai',        kws: ['interpretability', 'alignment', 'safety', 'jailbreak', 'red team', 'red-team', 'mech interp', 'circuit', 'feature steering', 'activation steering', 'refusal', 'sycophancy', 'rlhf', 'constitutional ai', 'rlaif', 'governance', 'oversight'] },
  { topic: 'ai-routing',            kws: ['routing', 'router', 'mixture of experts', 'moe', 'speculative decoding'] },
  { topic: 'inference-efficiency',  kws: ['kv cache', 'quantization', 'distillation', 'pruning', 'inference', 'throughput', 'latency', 'batching', 'kernel', 'flashattention', 'training efficiency'] },
  { topic: 'hardware',              kws: ['h100', 'b200', 'blackwell', 'hopper', 'gpu', 'cuda', 'tpu', 'chip', 'semiconductor', 'silicon', 'nvda', 'nvidia hardware', 'data center'] },
  { topic: 'llms-foundation-models',kws: ['llm', 'language model', 'foundation model', 'gpt', 'claude', 'gemini', 'llama', 'mistral', 'grok', 'reasoning model', 'o1', 'o3', 'benchmark'] },
  { topic: 'agentic-systems',       kws: ['agent', 'tool use', 'agentic', 'coding agent', 'cursor', 'claude code'] },
  { topic: 'vision-audio-video',    kws: ['multimodal', 'vision-language', 'image generation', 'diffusion', 'text-to-image', 'video generation', 'speech', 'audio generation', 'vlm', 'vision model'] },
];

function inferTweetTopic(text) {
  const t = (text || '').toLowerCase();
  for (const { topic, kws } of TWEET_TOPIC_RULES) {
    if (kws.some((k) => t.includes(k))) return topic;
  }
  return 'ai-industry';
}

function rewriteMarkdownLinks(html, sourceWikiPath, baseUrl = '/cere-bro') {
  // Synthesis files reference other wiki pages via relative `.md` links.
  // Convert those to absolute Astro routes (no `.md`, with base prefix).
  // sourceWikiPath: wiki-root-relative dir of the source file (e.g. 'social-stream/2026-05')
  return html.replace(/href="([^"]+\.md)"/g, (match, href) => {
    if (/^https?:/.test(href)) return match; // external
    if (href.startsWith('/')) return match;   // already absolute
    const resolved = path.posix.normalize(path.posix.join(sourceWikiPath, href));
    const slug = resolved.replace(/\.md$/, '');
    // Daily digests have a dedicated route at /digests/{date}/, not the
    // generic [...slug] wiki route. Detect daily-digest/YYYY-MM/YYYY-MM-DD
    // paths and rewrite to the digest route.
    const digestMatch = slug.match(/^daily-digest\/\d{4}-\d{2}\/(\d{4}-\d{2}-\d{2})$/);
    if (digestMatch) return `href="${baseUrl}/digests/${digestMatch[1]}/"`;
    return `href="${baseUrl}/${slug}/"`;
  });
}

function loadSocialSyntheses() {
  // Two file shapes under wiki/social-stream/YYYY-MM/:
  //   YYYY-MM-DD-<slot>.md  → per-slot synthesis (morning/afternoon/evening/night)
  //   YYYY-MM-DD.md         → daily roll-up (written by midnight cron)
  // Returned as { slotsByKey: {date-slot: html}, rollupsByDate: {date: html} }
  const root = path.join(WIKI_DIR, 'social-stream');
  const slotsByKey = {};
  const rollupsByDate = {};
  if (!fs.existsSync(root)) return { slotsByKey, rollupsByDate };
  const months = fs.readdirSync(root).filter((f) =>
    fs.statSync(path.join(root, f)).isDirectory()
  );
  for (const month of months) {
    const monthDir = path.join(root, month);
    const sourceDir = `social-stream/${month}`;
    for (const fname of fs.readdirSync(monthDir)) {
      const slotMatch = fname.match(/^(\d{4}-\d{2}-\d{2})-(night|morning|afternoon|evening)\.md$/);
      const rollupMatch = fname.match(/^(\d{4}-\d{2}-\d{2})\.md$/);
      const raw = fs.readFileSync(path.join(monthDir, fname), 'utf8');
      const { content } = matter(raw);
      const html = rewriteMarkdownLinks(marked.parse(content), sourceDir);
      if (slotMatch) {
        const [, date, slot] = slotMatch;
        slotsByKey[`${date}-${slot}`] = html;
      } else if (rollupMatch) {
        const [, date] = rollupMatch;
        rollupsByDate[date] = html;
      }
    }
  }
  return { slotsByKey, rollupsByDate };
}

function parseSocialStream() {
  if (!fs.existsSync(TWITTER_RAW_DIR)) return [];
  const files = fs.readdirSync(TWITTER_RAW_DIR)
    .filter((f) => f.endsWith('.json'))
    .sort()
    .reverse(); // newest first

  const { slotsByKey, rollupsByDate } = loadSocialSyntheses();
  const slots = [];
  for (const fname of files) {
    try {
      const raw = JSON.parse(fs.readFileSync(path.join(TWITTER_RAW_DIR, fname), 'utf8'));

      // Flatten all tweets with inferred topic
      const allTweets = [
        ...raw.curated.map((t) => ({
          ...t,
          isCurated: true,
          topic: inferTweetTopic(t.text + ' ' + (t.articles?.[0]?.content ?? '')),
          importance: 'high', // curated retweets are always high
        })),
        ...raw.ai_feed.flatMap((feed) =>
          feed.tweets.map((t) => ({
            ...t,
            org: feed.org,
            focus: feed.focus,
            isCurated: false,
            topic: inferTweetTopic(t.text + ' ' + (t.articles?.[0]?.content ?? '')),
            importance: t.articles?.length > 0 ? 'medium' : 'normal',
          }))
        ),
      ];

      slots.push({
        date:       raw.date,
        slot:       raw.slot,
        scrapedIst: raw.scraped_ist,
        lookbackH:  raw.lookback_h,
        synthesisHtml: slotsByKey[`${raw.date}-${raw.slot}`] ?? null,
        curated:    raw.curated.map((t) => ({
          ...t,
          isCurated: true,
          topic: inferTweetTopic(t.text + ' ' + (t.articles?.[0]?.content ?? '')),
          importance: 'high',
        })),
        aiFeed: raw.ai_feed.map((feed) => ({
          handle: feed.handle,
          org:    feed.org,
          focus:  feed.focus,
          tweets: feed.tweets.map((t) => ({
            ...t,
            isCurated: false,
            topic: inferTweetTopic(t.text + ' ' + (t.articles?.[0]?.content ?? '')),
            importance: t.articles?.length > 0 ? 'medium' : 'normal',
          })),
        })),
        topicBreakdown: allTweets.reduce((acc, t) => {
          acc[t.topic] = (acc[t.topic] ?? 0) + 1;
          return acc;
        }, {}),
        counts: { total: allTweets.length, curated: raw.curated.length },
      });
    } catch (e) {
      console.warn(`  WARN: Failed to parse ${fname}: ${e.message}`);
    }
  }
  return { slots, rollupsByDate };
}

function extractTier(content, frontmatter) {
  if (frontmatter.tier) return Number(frontmatter.tier);
  // Look for "**Tier:** N" in content
  const m = content.match(/\*\*Tier:\*\*\s*(\d)/);
  return m ? Number(m[1]) : null;
}

function main() {
  if (!fs.existsSync(WIKI_DIR)) {
    console.error(`Wiki directory not found: ${WIKI_DIR}`);
    process.exit(1);
  }

  const allFiles = walk(WIKI_DIR);
  const pages = [];
  const digests = [];

  for (const filePath of allFiles) {
    const relPath = path.relative(WIKI_DIR, filePath);
    const filename = path.basename(filePath);
    const topic = extractTopic(relPath);

    const raw = fs.readFileSync(filePath, 'utf8');
    const { data: frontmatter, content } = matter(raw);

    const isDig = isDigest(relPath);
    const date = extractDateFromFilename(filename);
    const title = extractTitle(content, frontmatter) ?? filename.replace('.md', '');
    const tldr = extractTLDR(content);
    const links = extractLinks(content, filePath);
    const tier =
      extractTier(content, frontmatter) ??
      (TIER_OF_TOPIC[topic] !== undefined ? TIER_OF_TOPIC[topic] : null);

    const industryTag = topic === 'ai-industry' ? classifyIndustry(title, tldr) : null;

    const entry = {
      id: relPath.replace(/\\/g, '/').replace(/\.md$/, ''),
      path: relPath.replace(/\\/g, '/'),
      filename,
      topic,
      tier,
      date,
      title,
      tldr,
      links,
      industryTag,
      isSummary: isSourceSummary(filename),
      isConcept: isConceptPage(filename, topic),
      isDigest: isDig,
      color: TOPIC_COLORS[topic] ?? '#94a3b8',
      // Render full markdown to HTML for digest pages and concept pages.
      // Rewrite relative `.md` links into clean Astro URLs so they don't 404.
      html: (isDig || isConceptPage(filename, topic))
        ? rewriteMarkdownLinks(marked.parse(content), path.posix.dirname(relPath.replace(/\\/g, '/')))
        : null,
      raw: isDig ? content : null,
    };

    if (isDig) {
      digests.push(entry);
    } else {
      pages.push(entry);
    }
  }

  // Sort digests reverse-chronologically
  digests.sort((a, b) => (b.date ?? '').localeCompare(a.date ?? ''));

  // Build topic timeline: papers per topic per date (legacy, daily)
  const timeline = {};
  for (const p of pages) {
    if (!p.date || !p.isSummary) continue;
    if (!timeline[p.date]) timeline[p.date] = {};
    timeline[p.date][p.topic] = (timeline[p.date][p.topic] ?? 0) + 1;
  }

  // Weekly heatmap data — last 12 weeks, papers per topic per week
  const N_WEEKS = 12;
  const N_MONTHS = 12;
  const weeks = lastNWeeks(N_WEEKS);
  const months = lastNMonths(N_MONTHS);
  const researchTopics = Object.keys(TOPIC_COLORS).filter(
    (t) => t !== 'ai-industry' && t !== 'daily-digest',
  );

  // earliest summary date (for cumulative time series)
  const allSummaryDates = pages
    .filter((p) => p.isSummary && p.date)
    .map((p) => p.date)
    .sort();
  const earliestDate = allSummaryDates[0] ?? null;
  const cumulativeWeeks = allWeeks(earliestDate);

  // research heatmap (weekly): topic -> week -> count
  const researchHeatmap = {};
  for (const t of researchTopics) {
    researchHeatmap[t] = {};
    for (const w of weeks) researchHeatmap[t][w] = 0;
  }
  for (const p of pages) {
    if (!p.date || !p.isSummary) continue;
    if (!researchTopics.includes(p.topic)) continue;
    const w = weekStartUTC(parseDate(p.date));
    if (researchHeatmap[p.topic][w] !== undefined) {
      researchHeatmap[p.topic][w] += 1;
    }
  }

  // research heatmap (monthly): topic -> month -> count
  const researchHeatmapMonthly = {};
  for (const t of researchTopics) {
    researchHeatmapMonthly[t] = {};
    for (const m of months) researchHeatmapMonthly[t][m] = 0;
  }
  for (const p of pages) {
    if (!p.date || !p.isSummary) continue;
    if (!researchTopics.includes(p.topic)) continue;
    const mk = monthKey(parseDate(p.date));
    if (researchHeatmapMonthly[p.topic][mk] !== undefined) {
      researchHeatmapMonthly[p.topic][mk] += 1;
    }
  }

  // research cumulative time series (weekly granularity, full history)
  const researchCumulative = {};
  for (const t of researchTopics) {
    researchCumulative[t] = cumulativeWeeks.map(() => 0);
  }
  // First, count per topic per week across full history
  const researchByWeek = {};
  for (const t of researchTopics) {
    researchByWeek[t] = {};
    for (const w of cumulativeWeeks) researchByWeek[t][w] = 0;
  }
  for (const p of pages) {
    if (!p.date || !p.isSummary) continue;
    if (!researchTopics.includes(p.topic)) continue;
    const w = weekStartUTC(parseDate(p.date));
    if (researchByWeek[p.topic][w] !== undefined) {
      researchByWeek[p.topic][w] += 1;
    }
  }
  // Then accumulate
  for (const t of researchTopics) {
    let running = 0;
    cumulativeWeeks.forEach((w, i) => {
      running += researchByWeek[t][w];
      researchCumulative[t][i] = running;
    });
  }

  // research momentum: this-week vs prior-week count
  const thisWeek = weeks[weeks.length - 1];
  const lastWeek = weeks[weeks.length - 2];
  const prevWeek = weeks[weeks.length - 3];

  const researchMomentum = researchTopics.map((t) => {
    const tw = researchHeatmap[t][thisWeek] ?? 0;
    const lw = researchHeatmap[t][lastWeek] ?? 0;
    const pw = researchHeatmap[t][prevWeek] ?? 0;
    // Compare last 7-day total vs prior 14-day average per week
    const recent = tw;
    const trailing = (lw + pw) / 2;
    return {
      topic: t,
      thisWeek: tw,
      lastWeek: lw,
      delta: tw - lw,
      trailingAvg: Number(trailing.toFixed(1)),
    };
  });

  // industry heatmap (weekly): sub-category -> week -> count
  const industryCategories = INDUSTRY_TAGS.map((t) => t.key);
  const industryHeatmap = {};
  for (const cat of industryCategories) {
    industryHeatmap[cat] = {};
    for (const w of weeks) industryHeatmap[cat][w] = 0;
  }
  for (const p of pages) {
    if (!p.date || !p.isSummary) continue;
    if (p.topic !== 'ai-industry' || !p.industryTag) continue;
    if (industryHeatmap[p.industryTag] === undefined) continue;
    const w = weekStartUTC(parseDate(p.date));
    if (industryHeatmap[p.industryTag][w] !== undefined) {
      industryHeatmap[p.industryTag][w] += 1;
    }
  }

  // industry heatmap (monthly): sub-category -> month -> count
  const industryHeatmapMonthly = {};
  for (const cat of industryCategories) {
    industryHeatmapMonthly[cat] = {};
    for (const m of months) industryHeatmapMonthly[cat][m] = 0;
  }
  for (const p of pages) {
    if (!p.date || !p.isSummary) continue;
    if (p.topic !== 'ai-industry' || !p.industryTag) continue;
    if (industryHeatmapMonthly[p.industryTag] === undefined) continue;
    const mk = monthKey(parseDate(p.date));
    if (industryHeatmapMonthly[p.industryTag][mk] !== undefined) {
      industryHeatmapMonthly[p.industryTag][mk] += 1;
    }
  }

  // industry cumulative
  const industryCumulative = {};
  const industryByWeek = {};
  for (const cat of industryCategories) {
    industryCumulative[cat] = cumulativeWeeks.map(() => 0);
    industryByWeek[cat] = {};
    for (const w of cumulativeWeeks) industryByWeek[cat][w] = 0;
  }
  for (const p of pages) {
    if (!p.date || !p.isSummary) continue;
    if (p.topic !== 'ai-industry' || !p.industryTag) continue;
    if (industryByWeek[p.industryTag] === undefined) continue;
    const w = weekStartUTC(parseDate(p.date));
    if (industryByWeek[p.industryTag][w] !== undefined) {
      industryByWeek[p.industryTag][w] += 1;
    }
  }
  for (const cat of industryCategories) {
    let running = 0;
    cumulativeWeeks.forEach((w, i) => {
      running += industryByWeek[cat][w];
      industryCumulative[cat][i] = running;
    });
  }

  const industryMomentum = industryCategories.map((cat) => {
    const tw = industryHeatmap[cat][thisWeek] ?? 0;
    const lw = industryHeatmap[cat][lastWeek] ?? 0;
    const pw = industryHeatmap[cat][prevWeek] ?? 0;
    return {
      key: cat,
      label: INDUSTRY_TAGS.find((t) => t.key === cat)?.label ?? cat,
      color: INDUSTRY_TAGS.find((t) => t.key === cat)?.color ?? '#94a3b8',
      thisWeek: tw,
      lastWeek: lw,
      delta: tw - lw,
      trailingAvg: Number(((lw + pw) / 2).toFixed(1)),
    };
  });

  const industryTotal = pages.filter(
    (p) => p.topic === 'ai-industry' && p.isSummary,
  ).length;
  const industryByTag = {};
  for (const p of pages) {
    if (p.topic !== 'ai-industry' || !p.isSummary || !p.industryTag) continue;
    industryByTag[p.industryTag] = (industryByTag[p.industryTag] ?? 0) + 1;
  }

  // Topic distribution: count of summary pages per topic.
  // Exclude social-stream synthesis pages — those represent slot-level
  // summaries of tweets, not standalone research items, so their tweet
  // counts get folded in below via socialSlots/topicBreakdown instead.
  const topicCounts = {};
  for (const p of pages) {
    if (!p.isSummary) continue;
    if (p.topic === 'social-stream') continue;
    topicCounts[p.topic] = (topicCounts[p.topic] ?? 0) + 1;
  }

  // Social stream — Twitter/X slot data.
  // Tweets are distributed across the existing topics via inferTweetTopic,
  // and their counts get folded into topicCounts directly so there's no
  // separate "social stream" display in Atlas.
  const { slots: socialSlots, rollupsByDate: socialRollups } = parseSocialStream();
  let socialTotalTweets = 0;
  for (const s of socialSlots) {
    socialTotalTweets += s.counts.total;
    for (const [topic, n] of Object.entries(s.topicBreakdown)) {
      topicCounts[topic] = (topicCounts[topic] ?? 0) + n;
    }
  }
  // Build a list of dated roll-ups for the [date] route + Media Live history
  const socialRollupList = Object.keys(socialRollups)
    .sort()
    .reverse()
    .map((date) => ({ date, html: socialRollups[date] }));

  // Build graph nodes + edges from cross-references.
  // Skip wiki/index.md and wiki/log.md — those are excluded from the
  // [...slug] route, so any back/out-link to them would 404 in the sidebar.
  const META_PAGES = new Set(['index', 'log']);
  const nodeMap = new Map();
  for (const p of pages) {
    if (META_PAGES.has(p.id)) continue;
    nodeMap.set(p.id, {
      id: p.id,
      title: p.title,
      topic: p.topic,
      tier: p.tier,
      date: p.date,
      color: p.color,
      isSummary: p.isSummary,
      isConcept: p.isConcept,
    });
  }

  const edges = [];
  for (const p of pages) {
    if (META_PAGES.has(p.id)) continue;
    for (const targetPath of p.links) {
      const targetId = targetPath.replace(/\.md$/, '');
      if (META_PAGES.has(targetId)) continue;
      if (nodeMap.has(targetId)) {
        edges.push({ source: p.id, target: targetId });
      }
    }
  }

  // Recent activity for sidebar
  const recentSummaries = pages
    .filter((p) => p.isSummary && p.date)
    .sort((a, b) => (b.date ?? '').localeCompare(a.date ?? ''))
    .slice(0, 20)
    .map((p) => ({
      id: p.id,
      title: p.title,
      topic: p.topic,
      date: p.date,
      color: p.color,
      tldr: p.tldr,
    }));

  const conceptPages = pages
    .filter((p) => p.isConcept)
    .map((p) => ({
      id: p.id,
      title: p.title,
      topic: p.topic,
      color: p.color,
      tldr: p.tldr,
    }));

  const out = {
    generated: new Date().toISOString(),
    counts: {
      total: pages.length,
      summaries: pages.filter((p) => p.isSummary).length,
      concepts: pages.filter((p) => p.isConcept).length,
      digests: digests.length,
      industry: industryTotal,
      socialTweets: socialTotalTweets,
      socialSlots: socialSlots.length,
    },
    topicColors: TOPIC_COLORS,
    topicCounts,
    socialSlots,
    socialRollups: socialRollupList,
    timeline,
    digests,
    pages,
    nodes: [...nodeMap.values()],
    edges,
    recentSummaries,
    conceptPages,
    weeks,
    months,
    cumulativeWeeks,
    researchTopics,
    researchHeatmap,
    researchHeatmapMonthly,
    researchCumulative,
    researchMomentum,
    industryTags: INDUSTRY_TAGS.map(({ keywords, ...rest }) => rest),
    industryHeatmap,
    industryHeatmapMonthly,
    industryCumulative,
    industryMomentum,
    industryByTag,
  };

  fs.mkdirSync(path.dirname(OUT_FILE), { recursive: true });
  fs.writeFileSync(OUT_FILE, JSON.stringify(out, null, 2));

  console.log(`✓ wiki.json built`);
  console.log(`  ${out.counts.total} pages (${out.counts.summaries} summaries, ${out.counts.concepts} concepts)`);
  console.log(`  ${out.counts.digests} digests`);
  console.log(`  ${edges.length} cross-references`);
  console.log(`  output: ${path.relative(REPO_ROOT, OUT_FILE)}`);
}

main();
