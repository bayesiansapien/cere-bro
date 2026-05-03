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
const OUT_FILE = path.join(__dirname, '../src/data/wiki.json');

// Topic colors — one canonical palette
const TOPIC_COLORS = {
  'ai-routing':            '#f59e0b', // amber — Tier 1
  'inference-efficiency':  '#10b981', // emerald — Tier 1
  'hardware':              '#8b5cf6', // violet — Tier 1
  'llms-foundation-models': '#3b82f6', // blue — Tier 2
  'agents-tool-use':       '#ec4899', // pink — Tier 2
  'multimodal':            '#06b6d4', // cyan — Tier 3
  'ai-industry':           '#64748b', // slate — industry
  'daily-digest':          '#fbbf24', // gold — digests
};

const TIER_OF_TOPIC = {
  'ai-routing': 1,
  'inference-efficiency': 1,
  'hardware': 1,
  'llms-foundation-models': 2,
  'agents-tool-use': 2,
  'multimodal': 3,
  'ai-industry': 3,
  'daily-digest': 0,
};

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
      isSummary: isSourceSummary(filename),
      isConcept: isConceptPage(filename, topic),
      isDigest: isDig,
      color: TOPIC_COLORS[topic] ?? '#94a3b8',
      // Render full markdown to HTML for digest pages and concept pages
      html: isDig || isConceptPage(filename, topic) ? marked.parse(content) : null,
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

  // Build topic timeline: papers per topic per date
  const timeline = {};
  for (const p of pages) {
    if (!p.date || !p.isSummary) continue;
    if (!timeline[p.date]) timeline[p.date] = {};
    timeline[p.date][p.topic] = (timeline[p.date][p.topic] ?? 0) + 1;
  }

  // Topic distribution: count of summary pages per topic
  const topicCounts = {};
  for (const p of pages) {
    if (!p.isSummary) continue;
    topicCounts[p.topic] = (topicCounts[p.topic] ?? 0) + 1;
  }

  // Build graph nodes + edges from cross-references
  const nodeMap = new Map();
  for (const p of pages) {
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
    for (const targetPath of p.links) {
      const targetId = targetPath.replace(/\.md$/, '');
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
    },
    topicColors: TOPIC_COLORS,
    topicCounts,
    timeline,
    digests,
    pages,
    nodes: [...nodeMap.values()],
    edges,
    recentSummaries,
    conceptPages,
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
