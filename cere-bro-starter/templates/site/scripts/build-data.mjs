#!/usr/bin/env node
/**
 * Build-time wiki parser.
 * Reads ../../wiki/**\/*.md, generates src/data/wiki.json that the Astro
 * pages consume. Topic colors, tier assignments, and topic-keyword rules
 * come from ../../wiki-config.json — bootstrap personalizes them per-user.
 *
 * Features implemented:
 *   - Per-topic configuration via wiki-config.json
 *   - Source summary, concept page, daily digest, social-stream synthesis,
 *     daily roll-up parsing
 *   - Markdown link rewriting (.md → clean Astro routes)
 *   - Twitter raw JSON ingestion (Media Live tab)
 *   - Tweet topic inference using user-defined keywords (or fallback)
 *   - Industry taxonomy (when enabled in wiki-config)
 *   - Tweet counts folded into topic distribution
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import matter from 'gray-matter';
import { marked } from 'marked';

const __filename = fileURLToPath(import.meta.url);
const __dirname  = path.dirname(__filename);
const REPO_ROOT  = path.resolve(__dirname, '../..');
const WIKI_DIR   = path.join(REPO_ROOT, 'wiki');
const TWITTER_RAW_DIR = path.join(REPO_ROOT, 'raw', 'twitter');
const OUT_FILE   = path.join(__dirname, '../src/data/wiki.json');
const CONFIG_FILE = path.join(REPO_ROOT, 'wiki-config.json');

let wikiConfig = { topics: [], industryEnabled: false, baseUrl: '/' };
if (fs.existsSync(CONFIG_FILE)) {
  wikiConfig = JSON.parse(fs.readFileSync(CONFIG_FILE, 'utf8'));
}

const BASE_URL = wikiConfig.baseUrl ?? '/';

const TOPIC_COLORS  = {};
const TIER_OF_TOPIC = {};
const TOPIC_KEYWORDS = {};
for (const t of wikiConfig.topics ?? []) {
  TOPIC_COLORS[t.key]   = t.color;
  TIER_OF_TOPIC[t.key]  = t.tier;
  TOPIC_KEYWORDS[t.key] = (t.keywords ?? []).map((k) => String(k).toLowerCase());
}
TOPIC_COLORS['daily-digest']  = '#fbbf24';
TIER_OF_TOPIC['daily-digest'] = 0;
TOPIC_COLORS['social-stream'] = '#a855f7';
TIER_OF_TOPIC['social-stream'] = 0;
if (wikiConfig.industryEnabled) {
  TOPIC_COLORS['ai-industry']  = '#64748b';
  TIER_OF_TOPIC['ai-industry'] = 3;
}

const INDUSTRY_TAGS = wikiConfig.industryEnabled ? [
  { key: 'deals',          label: 'Funding & M&A',           color: '#f59e0b',
    keywords: ['acquisition', 'acquire', 'acquires', 'merger', 'buyout', 'funding round', 'series a', 'series b', 'series c', 'series d', 'raise', 'raises', 'raised', 'ipo', 'joint venture', 'partnership', 'spinoff', 'divestiture', 'deal', 'closes round'] },
  { key: 'markets',        label: 'Revenue & Valuations',    color: '#10b981',
    keywords: ['valuation', 'arr', 'revenue', 'capex', 'opex', 'margin', 'billion', 'misallocation', 'capital allocation', 'pricing', 'price hike', 'cost', 'economics', 'value capture', 'profit', 'profitability', 'spending', 'unit economics', 'demand', 'monetization', 'tam', 'market size'] },
  { key: 'regulation',     label: 'Regulation & Policy',     color: '#ef4444',
    keywords: ['regulation', 'policy', 'antitrust', 'pentagon', 'ftc', 'court', 'legal', 'ban', 'eu ai act', 'white house', 'congress', 'classified', 'sanctions', 'lawsuit', 'subpoena'] },
  { key: 'infrastructure', label: 'Infrastructure & Compute', color: '#8b5cf6',
    keywords: ['datacenter', 'data center', 'gpu', 'chip', 'hardware', 'compute', 'gigawatt', 'memory', 'fab', 'tsmc', 'reliability', 'capacity', 'silicon', 'h100', 'b200', 'blackwell', 'hopper'] },
  { key: 'products',       label: 'Products & Launches',     color: '#3b82f6',
    keywords: ['launch', 'launches', 'release', 'released', 'available', 'ships', 'shipped', 'beta', 'preview', 'announcement', 'introduces', 'unveils', 'connector', 'creative work', 'rolls out'] },
  { key: 'risks',          label: 'Critique & Risks',        color: '#94a3b8',
    keywords: ['skeptic', 'critique', 'concern', 'controversy', 'fail', 'failure', 'criticism', 'risk', 'bubble', 'slop', 'dispute', 'trust', 'incident', 'breach', 'vulnerability'] },
] : [];

function classifyIndustry(title, tldr) {
  if (!wikiConfig.industryEnabled) return null;
  const text = `${title ?? ''} ${tldr ?? ''}`.toLowerCase();
  for (const tag of INDUSTRY_TAGS) if (tag.keywords.some((k) => text.includes(k))) return tag.key;
  return 'other';
}

function parseDate(iso) { return iso ? new Date(iso + 'T00:00:00Z') : null; }
function weekStartUTC(d) {
  if (!d) return null;
  const day = d.getUTCDay();
  const offset = day === 0 ? 6 : day - 1;
  return new Date(d.getTime() - offset * 24 * 60 * 60 * 1000).toISOString().slice(0, 10);
}
function lastNWeeks(n) {
  const today = new Date(); today.setUTCHours(0, 0, 0, 0);
  const start = new Date(weekStartUTC(today) + 'T00:00:00Z');
  const out = [];
  for (let i = n - 1; i >= 0; i--) out.push(new Date(start.getTime() - i * 7 * 24 * 60 * 60 * 1000).toISOString().slice(0, 10));
  return out;
}
function lastNMonths(n) {
  const out = [], today = new Date(), y = today.getUTCFullYear(), m = today.getUTCMonth();
  for (let i = n - 1; i >= 0; i--) {
    const d = new Date(Date.UTC(y, m - i, 1));
    out.push(`${d.getUTCFullYear()}-${String(d.getUTCMonth() + 1).padStart(2, '0')}`);
  }
  return out;
}
function monthKey(d) { return d ? `${d.getUTCFullYear()}-${String(d.getUTCMonth() + 1).padStart(2, '0')}` : null; }
function allWeeks(earliestISO) {
  if (!earliestISO) return lastNWeeks(12);
  const start = new Date(weekStartUTC(parseDate(earliestISO)) + 'T00:00:00Z');
  const end   = new Date(weekStartUTC(new Date()) + 'T00:00:00Z');
  const out = [];
  for (let d = start; d.getTime() <= end.getTime(); d = new Date(d.getTime() + 7 * 24 * 60 * 60 * 1000)) {
    out.push(d.toISOString().slice(0, 10));
  }
  return out;
}

function inferTweetTopic(text) {
  const t = (text || '').toLowerCase();
  for (const topic of Object.keys(TOPIC_KEYWORDS)) {
    const kws = TOPIC_KEYWORDS[topic];
    const checkList = kws.length > 0 ? kws : [topic.replace(/-/g, ' ')];
    if (checkList.some((k) => t.includes(k))) return topic;
  }
  return wikiConfig.industryEnabled ? 'ai-industry' : (Object.keys(TOPIC_COLORS)[0] ?? 'general');
}

function rewriteMarkdownLinks(html, sourceWikiPath) {
  return html.replace(/href="([^"]+\.md)"/g, (match, href) => {
    if (/^https?:/.test(href)) return match;
    if (href.startsWith('/')) return match;
    const resolved = path.posix.normalize(path.posix.join(sourceWikiPath, href));
    const slug = resolved.replace(/\.md$/, '');
    const digestMatch = slug.match(/^daily-digest\/\d{4}-\d{2}\/(\d{4}-\d{2}-\d{2})$/);
    if (digestMatch) return `href="${BASE_URL.replace(/\/$/, '')}/digests/${digestMatch[1]}/"`;
    return `href="${BASE_URL.replace(/\/$/, '')}/${slug}/"`;
  });
}

function walk(dir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  const files = [];
  for (const e of entries) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) files.push(...walk(p));
    else if (e.isFile() && p.endsWith('.md')) files.push(p);
  }
  return files;
}
function extractDateFromFilename(fn) { const m = fn.match(/^(\d{4}-\d{2}-\d{2})/); return m ? m[1] : null; }
function extractTopic(relPath) { return relPath.split(path.sep)[0]; }
function extractTitle(content, fm) {
  if (fm.title) return fm.title;
  const h1 = content.match(/^#\s+(.+)$/m);
  return h1 ? h1[1].trim() : null;
}
function extractTLDR(content) {
  const tl = content.match(/##\s+TL;DR\s*\n+([\s\S]+?)(?=\n##|\n---|\Z)/);
  if (tl) return tl[1].trim().replace(/\n+/g, ' ').slice(0, 400);
  const fp = content.match(/^#\s+.+\n+([^\n#].+(?:\n[^\n#].+)*)/m);
  return fp ? fp[1].trim().replace(/\n+/g, ' ').slice(0, 400) : null;
}
function extractLinks(content, sourcePath) {
  const re = /\[([^\]]+)\]\(([^)]+\.md)\)/g;
  const out = [];
  const sourceDir = path.dirname(sourcePath);
  let m;
  while ((m = re.exec(content)) !== null) {
    if (m[2].startsWith('http')) continue;
    const abs = path.resolve(sourceDir, m[2]);
    const rel = path.relative(WIKI_DIR, abs);
    if (!rel.startsWith('..')) out.push(rel);
  }
  return [...new Set(out)];
}
function isSourceSummary(fn) { return /^\d{4}-\d{2}-\d{2}/.test(fn); }
function isConceptPage(fn, topic) {
  return !isSourceSummary(fn) && !['index.md', 'log.md'].includes(fn) && topic !== 'daily-digest' && topic !== 'social-stream';
}
function isDigest(relPath) { return relPath.startsWith('daily-digest'); }
function extractTier(content, fm) {
  if (fm.tier) return Number(fm.tier);
  const m = content.match(/\*\*Tier:\*\*\s*(\d)/);
  return m ? Number(m[1]) : null;
}

function loadSocialSyntheses() {
  const root = path.join(WIKI_DIR, 'social-stream');
  const slotsByKey = {};
  const rollupsByDate = {};
  if (!fs.existsSync(root)) return { slotsByKey, rollupsByDate };
  for (const month of fs.readdirSync(root).filter((f) => fs.statSync(path.join(root, f)).isDirectory())) {
    const monthDir = path.join(root, month);
    const sourceDir = `social-stream/${month}`;
    for (const fname of fs.readdirSync(monthDir)) {
      const slotMatch = fname.match(/^(\d{4}-\d{2}-\d{2})-(night|morning|afternoon|evening)\.md$/);
      const rollupMatch = fname.match(/^(\d{4}-\d{2}-\d{2})\.md$/);
      const raw = fs.readFileSync(path.join(monthDir, fname), 'utf8');
      const { content } = matter(raw);
      const html = rewriteMarkdownLinks(marked.parse(content), sourceDir);
      if (slotMatch) slotsByKey[`${slotMatch[1]}-${slotMatch[2]}`] = html;
      else if (rollupMatch) rollupsByDate[rollupMatch[1]] = html;
    }
  }
  return { slotsByKey, rollupsByDate };
}

function parseSocialStream() {
  if (!fs.existsSync(TWITTER_RAW_DIR)) return { slots: [], rollupsByDate: {} };
  const files = fs.readdirSync(TWITTER_RAW_DIR).filter((f) => f.endsWith('.json')).sort().reverse();
  const { slotsByKey, rollupsByDate } = loadSocialSyntheses();
  const slots = [];
  for (const fname of files) {
    try {
      const raw = JSON.parse(fs.readFileSync(path.join(TWITTER_RAW_DIR, fname), 'utf8'));
      const allTweets = [
        ...raw.curated.map((t) => ({ ...t, isCurated: true,  topic: inferTweetTopic(t.text + ' ' + (t.articles?.[0]?.content ?? '')), importance: 'high' })),
        ...raw.ai_feed.flatMap((feed) => feed.tweets.map((t) => ({ ...t, org: feed.org, isCurated: false, topic: inferTweetTopic(t.text + ' ' + (t.articles?.[0]?.content ?? '')), importance: t.articles?.length > 0 ? 'medium' : 'normal' }))),
      ];
      slots.push({
        date: raw.date, slot: raw.slot, scrapedIst: raw.scraped_ist, lookbackH: raw.lookback_h,
        synthesisHtml: slotsByKey[`${raw.date}-${raw.slot}`] ?? null,
        curated: raw.curated.map((t) => ({ ...t, isCurated: true, topic: inferTweetTopic(t.text + ' ' + (t.articles?.[0]?.content ?? '')), importance: 'high' })),
        aiFeed: raw.ai_feed.map((feed) => ({
          handle: feed.handle, org: feed.org, focus: feed.focus,
          tweets: feed.tweets.map((t) => ({ ...t, isCurated: false, topic: inferTweetTopic(t.text + ' ' + (t.articles?.[0]?.content ?? '')), importance: t.articles?.length > 0 ? 'medium' : 'normal' })),
        })),
        topicBreakdown: allTweets.reduce((acc, t) => { acc[t.topic] = (acc[t.topic] ?? 0) + 1; return acc; }, {}),
        counts: { total: allTweets.length, curated: raw.curated.length },
      });
    } catch (e) { console.warn(`  WARN: Failed to parse ${fname}: ${e.message}`); }
  }
  return { slots, rollupsByDate };
}

function main() {
  if (!fs.existsSync(WIKI_DIR)) { console.error(`Wiki directory not found: ${WIKI_DIR}`); process.exit(1); }

  const allFiles = walk(WIKI_DIR);
  const pages = [], digests = [];
  const META_PAGES = new Set(['index', 'log']);

  for (const filePath of allFiles) {
    const relPath = path.relative(WIKI_DIR, filePath);
    const filename = path.basename(filePath);
    const topic = extractTopic(relPath);
    const raw = fs.readFileSync(filePath, 'utf8');
    const { data: fm, content } = matter(raw);
    const isDig = isDigest(relPath);
    const date = extractDateFromFilename(filename);
    const title = extractTitle(content, fm) ?? filename.replace('.md', '');
    const tldr = extractTLDR(content);
    const links = extractLinks(content, filePath);
    const tier = extractTier(content, fm) ?? (TIER_OF_TOPIC[topic] !== undefined ? TIER_OF_TOPIC[topic] : null);
    const industryTag = topic === 'ai-industry' ? classifyIndustry(title, tldr) : null;
    const sourceDir = path.posix.dirname(relPath.replace(/\\/g, '/'));
    const id = relPath.replace(/\\/g, '/').replace(/\.md$/, '');
    const html = (isDig || isConceptPage(filename, topic))
      ? rewriteMarkdownLinks(marked.parse(content), sourceDir) : null;

    const entry = {
      id, path: relPath.replace(/\\/g, '/'), filename, topic, tier, date, title, tldr, links, industryTag,
      isSummary: isSourceSummary(filename),
      isConcept: isConceptPage(filename, topic),
      isDigest: isDig,
      color: TOPIC_COLORS[topic] ?? '#94a3b8',
      html, raw: isDig ? content : null,
    };
    if (isDig) digests.push(entry); else pages.push(entry);
  }

  digests.sort((a, b) => (b.date ?? '').localeCompare(a.date ?? ''));

  const topicCounts = {};
  for (const p of pages) {
    if (!p.isSummary) continue;
    if (p.topic === 'social-stream') continue;
    topicCounts[p.topic] = (topicCounts[p.topic] ?? 0) + 1;
  }

  const { slots: socialSlots, rollupsByDate } = parseSocialStream();
  let socialTotalTweets = 0;
  for (const s of socialSlots) {
    socialTotalTweets += s.counts.total;
    for (const [topic, n] of Object.entries(s.topicBreakdown)) topicCounts[topic] = (topicCounts[topic] ?? 0) + n;
  }
  const socialRollupList = Object.keys(rollupsByDate).sort().reverse().map((date) => ({ date, html: rollupsByDate[date] }));

  const N_WEEKS = 12, N_MONTHS = 12;
  const weeks = lastNWeeks(N_WEEKS);
  const months = lastNMonths(N_MONTHS);
  const researchTopics = Object.keys(TOPIC_COLORS).filter((t) => !['ai-industry','daily-digest','social-stream'].includes(t));
  const allSummaryDates = pages.filter((p) => p.isSummary && p.date).map((p) => p.date).sort();
  const cumulativeWeeks = allWeeks(allSummaryDates[0] ?? null);

  const researchHeatmap = {}, researchHeatmapMonthly = {}, researchByWeek = {};
  for (const t of researchTopics) {
    researchHeatmap[t] = Object.fromEntries(weeks.map((w) => [w, 0]));
    researchHeatmapMonthly[t] = Object.fromEntries(months.map((m) => [m, 0]));
    researchByWeek[t] = Object.fromEntries(cumulativeWeeks.map((w) => [w, 0]));
  }
  for (const p of pages) {
    if (!p.date || !p.isSummary || !researchTopics.includes(p.topic)) continue;
    const w = weekStartUTC(parseDate(p.date));
    const mk = monthKey(parseDate(p.date));
    if (researchHeatmap[p.topic][w] !== undefined) researchHeatmap[p.topic][w] += 1;
    if (researchHeatmapMonthly[p.topic][mk] !== undefined) researchHeatmapMonthly[p.topic][mk] += 1;
    if (researchByWeek[p.topic][w] !== undefined) researchByWeek[p.topic][w] += 1;
  }
  const researchCumulative = {};
  for (const t of researchTopics) {
    let r = 0;
    researchCumulative[t] = cumulativeWeeks.map((w) => (r += researchByWeek[t][w]));
  }
  const thisWeek = weeks[weeks.length - 1], lastWeek = weeks[weeks.length - 2], prevWeek = weeks[weeks.length - 3];
  const researchMomentum = researchTopics.map((t) => {
    const tw = researchHeatmap[t][thisWeek] ?? 0, lw = researchHeatmap[t][lastWeek] ?? 0, pw = researchHeatmap[t][prevWeek] ?? 0;
    return { topic: t, thisWeek: tw, lastWeek: lw, delta: tw - lw, trailingAvg: Number(((lw + pw) / 2).toFixed(1)) };
  });

  const industryCategories = INDUSTRY_TAGS.map((t) => t.key);
  const industryHeatmap = {}, industryHeatmapMonthly = {}, industryByWeek = {};
  for (const cat of industryCategories) {
    industryHeatmap[cat] = Object.fromEntries(weeks.map((w) => [w, 0]));
    industryHeatmapMonthly[cat] = Object.fromEntries(months.map((m) => [m, 0]));
    industryByWeek[cat] = Object.fromEntries(cumulativeWeeks.map((w) => [w, 0]));
  }
  for (const p of pages) {
    if (!p.date || !p.isSummary || p.topic !== 'ai-industry' || !p.industryTag) continue;
    if (industryHeatmap[p.industryTag] === undefined) continue;
    const w = weekStartUTC(parseDate(p.date));
    const mk = monthKey(parseDate(p.date));
    if (industryHeatmap[p.industryTag][w] !== undefined) industryHeatmap[p.industryTag][w] += 1;
    if (industryHeatmapMonthly[p.industryTag][mk] !== undefined) industryHeatmapMonthly[p.industryTag][mk] += 1;
    if (industryByWeek[p.industryTag][w] !== undefined) industryByWeek[p.industryTag][w] += 1;
  }
  const industryCumulative = {};
  for (const cat of industryCategories) {
    let r = 0;
    industryCumulative[cat] = cumulativeWeeks.map((w) => (r += industryByWeek[cat][w]));
  }
  const industryMomentum = industryCategories.map((cat) => {
    const tw = industryHeatmap[cat][thisWeek] ?? 0, lw = industryHeatmap[cat][lastWeek] ?? 0, pw = industryHeatmap[cat][prevWeek] ?? 0;
    const tag = INDUSTRY_TAGS.find((t) => t.key === cat);
    return { key: cat, label: tag?.label ?? cat, color: tag?.color ?? '#94a3b8', thisWeek: tw, lastWeek: lw, delta: tw - lw, trailingAvg: Number(((lw + pw) / 2).toFixed(1)) };
  });
  const industryTotal = pages.filter((p) => p.topic === 'ai-industry' && p.isSummary).length;
  const industryByTag = {};
  for (const p of pages) {
    if (p.topic !== 'ai-industry' || !p.isSummary || !p.industryTag) continue;
    industryByTag[p.industryTag] = (industryByTag[p.industryTag] ?? 0) + 1;
  }

  const nodeMap = new Map();
  for (const p of pages) {
    if (META_PAGES.has(p.id)) continue;
    nodeMap.set(p.id, { id: p.id, title: p.title, topic: p.topic, tier: p.tier, date: p.date, color: p.color, isSummary: p.isSummary, isConcept: p.isConcept });
  }
  const edges = [];
  for (const p of pages) {
    if (META_PAGES.has(p.id)) continue;
    for (const targetPath of p.links) {
      const targetId = targetPath.replace(/\.md$/, '');
      if (META_PAGES.has(targetId)) continue;
      if (nodeMap.has(targetId)) edges.push({ source: p.id, target: targetId });
    }
  }

  const recentSummaries = pages.filter((p) => p.isSummary && p.date)
    .sort((a, b) => (b.date ?? '').localeCompare(a.date ?? ''))
    .slice(0, 20)
    .map((p) => ({ id: p.id, title: p.title, topic: p.topic, date: p.date, color: p.color, tldr: p.tldr }));
  const conceptPages = pages.filter((p) => p.isConcept)
    .map((p) => ({ id: p.id, title: p.title, topic: p.topic, color: p.color, tldr: p.tldr }));

  const out = {
    generated: new Date().toISOString(),
    counts: {
      total: pages.length, summaries: pages.filter((p) => p.isSummary).length, concepts: pages.filter((p) => p.isConcept).length,
      digests: digests.length, industry: industryTotal,
      socialTweets: socialTotalTweets, socialSlots: socialSlots.length,
    },
    topicColors: TOPIC_COLORS, topicCounts,
    socialSlots, socialRollups: socialRollupList,
    timeline: {}, digests, pages,
    nodes: [...nodeMap.values()], edges,
    recentSummaries, conceptPages,
    weeks, months, cumulativeWeeks,
    researchTopics, researchHeatmap, researchHeatmapMonthly, researchCumulative, researchMomentum,
    industryTags: INDUSTRY_TAGS.map(({ keywords, ...rest }) => rest),
    industryHeatmap, industryHeatmapMonthly, industryCumulative, industryMomentum, industryByTag,
  };

  fs.mkdirSync(path.dirname(OUT_FILE), { recursive: true });
  fs.writeFileSync(OUT_FILE, JSON.stringify(out, null, 2));
  console.log(`✓ wiki.json built`);
  console.log(`  ${out.counts.total} pages (${out.counts.summaries} summaries, ${out.counts.concepts} concepts, ${out.counts.digests} digests)`);
  console.log(`  ${edges.length} cross-references | ${out.counts.socialTweets} tweets across ${out.counts.socialSlots} slots`);
  console.log(`  output: ${path.relative(REPO_ROOT, OUT_FILE)}`);
}

main();
