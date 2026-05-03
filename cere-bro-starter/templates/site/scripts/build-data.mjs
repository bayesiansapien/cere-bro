#!/usr/bin/env node
/**
 * Build-time wiki parser.
 * Reads ../wiki/**\/*.md, extracts metadata, generates src/data/wiki.json.
 * Topic colors and tier assignments come from ../../wiki-config.json.
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
const OUT_FILE = path.join(__dirname, '../src/data/wiki.json');
const CONFIG_FILE = path.join(REPO_ROOT, 'wiki-config.json');

// ── Load wiki-config.json ─────────────────────────────────────────────────────

let wikiConfig = { topics: [], industryEnabled: false };
if (fs.existsSync(CONFIG_FILE)) {
  wikiConfig = JSON.parse(fs.readFileSync(CONFIG_FILE, 'utf8'));
}

const TOPIC_COLORS = {};
const TIER_OF_TOPIC = {};
for (const t of wikiConfig.topics ?? []) {
  TOPIC_COLORS[t.key] = t.color;
  TIER_OF_TOPIC[t.key] = t.tier;
}
// Reserved topics
TOPIC_COLORS['daily-digest'] = '#fbbf24';
TIER_OF_TOPIC['daily-digest'] = 0;
if (wikiConfig.industryEnabled) {
  TOPIC_COLORS['ai-industry'] = '#94a3b8';
  TIER_OF_TOPIC['ai-industry'] = 3;
}

// Industry sub-categories (if industry tracking is enabled)
const INDUSTRY_TAGS = wikiConfig.industryEnabled ? [
  {
    key: 'economics',
    label: 'Economics & Cost',
    color: '#10b981',
    keywords: ['valuation', 'arr', 'revenue', 'capex', 'margin', 'billion', 'misallocation', 'capital', 'pricing', 'cost', 'economics', 'profit', '$', 'spending'],
  },
  {
    key: 'regulation',
    label: 'Regulation & Policy',
    color: '#ef4444',
    keywords: ['regulation', 'policy', 'antitrust', 'ftc', 'court', 'legal', 'ban', 'eu ai act', 'white house', 'congress', 'lawsuit', 'sanctions'],
  },
  {
    key: 'infrastructure',
    label: 'Infrastructure & Compute',
    color: '#8b5cf6',
    keywords: ['datacenter', 'gpu', 'chip', 'hardware', 'compute', 'gigawatt', 'memory', 'fab', 'tsmc', 'nvidia', 'capacity', 'silicon'],
  },
  {
    key: 'mergers',
    label: 'M&A & Funding',
    color: '#f59e0b',
    keywords: ['acquisition', 'acquire', 'investment', 'raise', 'funding round', 'ipo', 'merger', 'buyout', 'partnership', 'deal'],
  },
  {
    key: 'products',
    label: 'Products & Launches',
    color: '#3b82f6',
    keywords: ['launch', 'launches', 'release', 'available', 'ships', 'shipped', 'beta', 'preview', 'announcement', 'introduces', 'unveils'],
  },
  {
    key: 'critique',
    label: 'Critique & Risks',
    color: '#94a3b8',
    keywords: ['skeptic', 'critique', 'concern', 'controversy', 'fail', 'criticism', 'risk', 'bubble', 'slop', 'dispute', 'trust'],
  },
] : [];

function classifyIndustry(title, tldr) {
  if (!wikiConfig.industryEnabled) return null;
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

function weekStartUTC(d) {
  if (!d) return null;
  const day = d.getUTCDay();
  const offset = day === 0 ? 6 : day - 1;
  const ws = new Date(d.getTime() - offset * 24 * 60 * 60 * 1000);
  return ws.toISOString().slice(0, 10);
}

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

function lastNMonths(n) {
  const out = [];
  const today = new Date();
  const y = today.getUTCFullYear();
  const m = today.getUTCMonth();
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

// ── File walking and parsing ──────────────────────────────────────────────────

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

function extractDateFromFilename(filename) {
  const m = filename.match(/^(\d{4}-\d{2}-\d{2})/);
  return m ? m[1] : null;
}

function extractTopic(relPath) {
  const parts = relPath.split(path.sep);
  return parts[0];
}

function extractTitle(content, frontmatter) {
  if (frontmatter.title) return frontmatter.title;
  const h1 = content.match(/^#\s+(.+)$/m);
  if (h1) return h1[1].trim();
  return null;
}

function extractTLDR(content) {
  const tldrMatch = content.match(/##\s+TL;DR\s*\n+([\s\S]+?)(?=\n##|\n---|\Z)/);
  if (tldrMatch) return tldrMatch[1].trim().replace(/\n+/g, ' ').slice(0, 400);
  const firstPara = content.match(/^#\s+.+\n+([^\n#].+(?:\n[^\n#].+)*)/m);
  if (firstPara) return firstPara[1].trim().replace(/\n+/g, ' ').slice(0, 400);
  return null;
}

function extractLinks(content, sourcePath) {
  const linkRe = /\[([^\]]+)\]\(([^)]+\.md)\)/g;
  const links = [];
  const sourceDir = path.dirname(sourcePath);
  let m;
  while ((m = linkRe.exec(content)) !== null) {
    const target = m[2];
    if (target.startsWith('http')) continue;
    const absoluteTarget = path.resolve(sourceDir, target);
    const relativeFromWiki = path.relative(WIKI_DIR, absoluteTarget);
    if (!relativeFromWiki.startsWith('..')) links.push(relativeFromWiki);
  }
  return [...new Set(links)];
}

function isSourceSummary(filename) {
  return /^\d{4}-\d{2}-\d{2}/.test(filename);
}

function isConceptPage(filename, topic) {
  return (
    !isSourceSummary(filename) &&
    !['index.md', 'log.md'].includes(filename) &&
    topic !== 'daily-digest'
  );
}

function isDigest(relPath) {
  return relPath.startsWith('daily-digest');
}

function extractTier(content, frontmatter) {
  if (frontmatter.tier) return Number(frontmatter.tier);
  const m = content.match(/\*\*Tier:\*\*\s*(\d)/);
  return m ? Number(m[1]) : null;
}

// ── Main ──────────────────────────────────────────────────────────────────────

function main() {
  if (!fs.existsSync(WIKI_DIR)) {
    console.warn(`Wiki directory not found: ${WIKI_DIR}`);
    console.warn('Building with empty wiki...');
    // Write empty wiki.json so site builds without errors
    const empty = {
      generated: new Date().toISOString(),
      counts: { total: 0, summaries: 0, concepts: 0, digests: 0, industry: 0 },
      topicColors: TOPIC_COLORS,
      topicCounts: {},
      timeline: {},
      digests: [],
      pages: [],
      nodes: [],
      edges: [],
      recentSummaries: [],
      conceptPages: [],
      weeks: lastNWeeks(12),
      months: lastNMonths(12),
      cumulativeWeeks: lastNWeeks(12),
      researchTopics: [],
      researchHeatmap: {},
      researchHeatmapMonthly: {},
      researchCumulative: {},
      researchMomentum: [],
      industryTags: INDUSTRY_TAGS.map(({ keywords, ...rest }) => rest),
      industryHeatmap: {},
      industryHeatmapMonthly: {},
      industryCumulative: {},
      industryMomentum: [],
      industryByTag: {},
    };
    fs.mkdirSync(path.dirname(OUT_FILE), { recursive: true });
    fs.writeFileSync(OUT_FILE, JSON.stringify(empty, null, 2));
    console.log('✓ wiki.json built (empty)');
    return;
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
      html: isDig || isConceptPage(filename, topic) ? marked.parse(content) : null,
      raw: isDig ? content : null,
    };

    if (isDig) {
      digests.push(entry);
    } else {
      pages.push(entry);
    }
  }

  digests.sort((a, b) => (b.date ?? '').localeCompare(a.date ?? ''));

  const timeline = {};
  for (const p of pages) {
    if (!p.date || !p.isSummary) continue;
    if (!timeline[p.date]) timeline[p.date] = {};
    timeline[p.date][p.topic] = (timeline[p.date][p.topic] ?? 0) + 1;
  }

  const N_WEEKS = 12;
  const N_MONTHS = 12;
  const weeks = lastNWeeks(N_WEEKS);
  const months = lastNMonths(N_MONTHS);
  const researchTopics = Object.keys(TOPIC_COLORS).filter(
    (t) => t !== 'ai-industry' && t !== 'daily-digest',
  );

  const allSummaryDates = pages.filter((p) => p.isSummary && p.date).map((p) => p.date).sort();
  const earliestDate = allSummaryDates[0] ?? null;
  const cumulativeWeeks = allWeeks(earliestDate);

  // Research heatmaps
  const researchHeatmap = {};
  const researchHeatmapMonthly = {};
  for (const t of researchTopics) {
    researchHeatmap[t] = Object.fromEntries(weeks.map((w) => [w, 0]));
    researchHeatmapMonthly[t] = Object.fromEntries(months.map((m) => [m, 0]));
  }
  for (const p of pages) {
    if (!p.date || !p.isSummary || !researchTopics.includes(p.topic)) continue;
    const w = weekStartUTC(parseDate(p.date));
    if (researchHeatmap[p.topic][w] !== undefined) researchHeatmap[p.topic][w] += 1;
    const mk = monthKey(parseDate(p.date));
    if (researchHeatmapMonthly[p.topic][mk] !== undefined) researchHeatmapMonthly[p.topic][mk] += 1;
  }

  // Research cumulative
  const researchCumulative = {};
  const researchByWeek = {};
  for (const t of researchTopics) {
    researchCumulative[t] = cumulativeWeeks.map(() => 0);
    researchByWeek[t] = Object.fromEntries(cumulativeWeeks.map((w) => [w, 0]));
  }
  for (const p of pages) {
    if (!p.date || !p.isSummary || !researchTopics.includes(p.topic)) continue;
    const w = weekStartUTC(parseDate(p.date));
    if (researchByWeek[p.topic][w] !== undefined) researchByWeek[p.topic][w] += 1;
  }
  for (const t of researchTopics) {
    let running = 0;
    cumulativeWeeks.forEach((w, i) => { running += researchByWeek[t][w]; researchCumulative[t][i] = running; });
  }

  const thisWeek = weeks[weeks.length - 1];
  const lastWeek = weeks[weeks.length - 2];
  const prevWeek = weeks[weeks.length - 3];

  const researchMomentum = researchTopics.map((t) => ({
    topic: t,
    thisWeek: researchHeatmap[t][thisWeek] ?? 0,
    lastWeek: researchHeatmap[t][lastWeek] ?? 0,
    delta: (researchHeatmap[t][thisWeek] ?? 0) - (researchHeatmap[t][lastWeek] ?? 0),
    trailingAvg: Number((((researchHeatmap[t][lastWeek] ?? 0) + (researchHeatmap[t][prevWeek] ?? 0)) / 2).toFixed(1)),
  }));

  // Industry heatmaps
  const industryCategories = INDUSTRY_TAGS.map((t) => t.key);
  const industryHeatmap = {};
  const industryHeatmapMonthly = {};
  const industryByWeek = {};
  const industryCumulative = {};
  for (const cat of industryCategories) {
    industryHeatmap[cat] = Object.fromEntries(weeks.map((w) => [w, 0]));
    industryHeatmapMonthly[cat] = Object.fromEntries(months.map((m) => [m, 0]));
    industryByWeek[cat] = Object.fromEntries(cumulativeWeeks.map((w) => [w, 0]));
    industryCumulative[cat] = cumulativeWeeks.map(() => 0);
  }
  for (const p of pages) {
    if (!p.date || !p.isSummary || p.topic !== 'ai-industry' || !p.industryTag) continue;
    if (industryHeatmap[p.industryTag] === undefined) continue;
    const w = weekStartUTC(parseDate(p.date));
    if (industryHeatmap[p.industryTag][w] !== undefined) industryHeatmap[p.industryTag][w] += 1;
    const mk = monthKey(parseDate(p.date));
    if (industryHeatmapMonthly[p.industryTag][mk] !== undefined) industryHeatmapMonthly[p.industryTag][mk] += 1;
    if (industryByWeek[p.industryTag][w] !== undefined) industryByWeek[p.industryTag][w] += 1;
  }
  for (const cat of industryCategories) {
    let running = 0;
    cumulativeWeeks.forEach((w, i) => { running += industryByWeek[cat][w]; industryCumulative[cat][i] = running; });
  }

  const industryMomentum = industryCategories.map((cat) => ({
    key: cat,
    label: INDUSTRY_TAGS.find((t) => t.key === cat)?.label ?? cat,
    color: INDUSTRY_TAGS.find((t) => t.key === cat)?.color ?? '#94a3b8',
    thisWeek: industryHeatmap[cat][thisWeek] ?? 0,
    lastWeek: industryHeatmap[cat][lastWeek] ?? 0,
    delta: (industryHeatmap[cat][thisWeek] ?? 0) - (industryHeatmap[cat][lastWeek] ?? 0),
    trailingAvg: Number((((industryHeatmap[cat][lastWeek] ?? 0) + (industryHeatmap[cat][prevWeek] ?? 0)) / 2).toFixed(1)),
  }));

  const industryTotal = pages.filter((p) => p.topic === 'ai-industry' && p.isSummary).length;
  const industryByTag = {};
  for (const p of pages) {
    if (p.topic !== 'ai-industry' || !p.isSummary || !p.industryTag) continue;
    industryByTag[p.industryTag] = (industryByTag[p.industryTag] ?? 0) + 1;
  }

  const topicCounts = {};
  for (const p of pages) {
    if (!p.isSummary) continue;
    topicCounts[p.topic] = (topicCounts[p.topic] ?? 0) + 1;
  }

  const nodeMap = new Map();
  for (const p of pages) {
    nodeMap.set(p.id, { id: p.id, title: p.title, topic: p.topic, tier: p.tier, date: p.date, color: p.color, isSummary: p.isSummary, isConcept: p.isConcept });
  }

  const edges = [];
  for (const p of pages) {
    for (const targetPath of p.links) {
      const targetId = targetPath.replace(/\.md$/, '');
      if (nodeMap.has(targetId)) edges.push({ source: p.id, target: targetId });
    }
  }

  const recentSummaries = pages
    .filter((p) => p.isSummary && p.date)
    .sort((a, b) => (b.date ?? '').localeCompare(a.date ?? ''))
    .slice(0, 20)
    .map((p) => ({ id: p.id, title: p.title, topic: p.topic, date: p.date, color: p.color, tldr: p.tldr }));

  const conceptPages = pages
    .filter((p) => p.isConcept)
    .map((p) => ({ id: p.id, title: p.title, topic: p.topic, color: p.color, tldr: p.tldr }));

  const out = {
    generated: new Date().toISOString(),
    wikiName: wikiConfig.wikiName ?? 'wiki',
    githubUrl: wikiConfig.githubUsername && wikiConfig.githubRepo
      ? `https://github.com/${wikiConfig.githubUsername}/${wikiConfig.githubRepo}`
      : null,
    counts: { total: pages.length, summaries: pages.filter((p) => p.isSummary).length, concepts: pages.filter((p) => p.isConcept).length, digests: digests.length, industry: industryTotal },
    topicColors: TOPIC_COLORS,
    topicCounts,
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
