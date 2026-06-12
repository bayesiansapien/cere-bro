// Cerebro Radio podcast RSS feed.
// Submitted ONCE to Spotify for Podcasters at https://podcasters.spotify.com.
// Spotify polls this URL every few hours; new episodes appear in the app
// automatically within 2–4 hours of the cron uploading the m4a to GitHub
// Releases.
//
// Feed format: standard RSS 2.0 + iTunes namespace. Spotify accepts this same
// format Apple uses, so the same XML works if you later submit to Apple.

import type { APIRoute } from 'astro';
import wiki from '../data/wiki.json';

const SHOW = {
  title:       '{{PODCAST_NAME}}',
  subtitle:    'Daily AI research synthesis',
  description: 'A daily deep-dive podcast on AI research. Each episode is automatically generated from the day\'s digest plus every wiki summary it cross-links plus the social-stream syntheses. The hosts identify 2–4 themes from the day\'s material and walk through them as one connected story, not a paper-by-paper roundup.',
  author:      '{{WIKI_NAME}}',
  owner: {
    name:  '{{OWNER_NAME}}',
    email: '{{OWNER_EMAIL}}',
  },
  // Top-level + secondary iTunes categories. Spotify reads <itunes:category>.
  category:    'Technology',
  subcategory: 'Tech News',
  language:    'en-US',
  explicit:    false,
  // The full public URL of the site + feed are derived from Astro.url at request time.
};

const SITE_URL  = 'https://{{GITHUB_USERNAME}}.github.io/{{WIKI_NAME}}';
const FEED_URL  = `${SITE_URL}/podcast.xml`;
const COVER_URL = `${SITE_URL}/podcast-cover.png`;

function esc(s: string): string {
  return String(s ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

function fmtDurationHHMMSS(sec: number | null): string {
  if (!sec || sec < 1) return '00:45:00';
  const h = Math.floor(sec / 3600);
  const m = Math.floor((sec % 3600) / 60);
  const s = sec % 60;
  return `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
}

function fmtRfc822(dateIso: string): string {
  // Episode pubDate. Use 09:00 IST (03:30 UTC) — the cron's nominal time.
  // Spotify wants RFC822 with timezone, e.g. "Mon, 23 May 2026 03:30:00 GMT".
  const d = new Date(`${dateIso}T03:30:00Z`);
  return d.toUTCString();
}

export const GET: APIRoute = () => {
  const episodes = (wiki as any).podcasts ?? [];

  // Episodes that were re-generated AFTER Spotify already ingested them need
  // a bumped GUID so Spotify treats the re-upload as a new episode and refetches
  // the audio. Without this, Spotify caches the first version of the GUID
  // forever and ignores any audio swap on GitHub Releases. Add a "YYYY-MM-DD: N"
  // entry here when a regeneration happens.
  const guidVersions: Record<string, number> = {
  };

  const items = episodes.map((ep: any) => {
    const ver        = guidVersions[ep.date];
    const guid       = ver ? `{{WIKI_NAME}}-radio-${ep.date}-v${ver}` : `{{WIKI_NAME}}-radio-${ep.date}`;
    const enclosure  = `<enclosure url="${esc(ep.audioUrl)}" type="audio/mp4"${ep.audioBytes ? ` length="${ep.audioBytes}"` : ''} />`;
    const itunesDur  = fmtDurationHHMMSS(ep.durationSec);
    const pubDate    = fmtRfc822(ep.date);
    const epTitle    = ep.episodeNumber
      ? `Episode ${ep.episodeNumber} — ${ep.date}`
      : `Episode ${ep.date}`;
    const description = ep.teaser || `Cerebro Radio episode for ${ep.date}.`;
    return `
    <item>
      <title>${esc(epTitle)}</title>
      <description><![CDATA[${description}]]></description>
      <itunes:summary><![CDATA[${description}]]></itunes:summary>
      <itunes:subtitle>${esc(description.slice(0, 150))}</itunes:subtitle>
      <pubDate>${pubDate}</pubDate>
      <guid isPermaLink="false">${esc(guid)}</guid>
      ${enclosure}
      <itunes:duration>${itunesDur}</itunes:duration>
      <itunes:episode>${ep.episodeNumber ?? ''}</itunes:episode>
      <itunes:episodeType>full</itunes:episodeType>
      <itunes:explicit>false</itunes:explicit>
      <link>${esc(SITE_URL + ep.digestUrl)}</link>
    </item>`;
  }).join('\n');

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
     xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
     xmlns:content="http://purl.org/rss/1.0/modules/content/"
     xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>${esc(SHOW.title)}</title>
    <link>${esc(SITE_URL)}</link>
    <atom:link href="${esc(FEED_URL)}" rel="self" type="application/rss+xml" />
    <language>${SHOW.language}</language>
    <copyright>© ${new Date().getFullYear()} ${esc(SHOW.author)}</copyright>
    <description><![CDATA[${SHOW.description}]]></description>
    <itunes:summary><![CDATA[${SHOW.description}]]></itunes:summary>
    <itunes:subtitle>${esc(SHOW.subtitle)}</itunes:subtitle>
    <itunes:author>${esc(SHOW.author)}</itunes:author>
    <itunes:owner>
      <itunes:name>${esc(SHOW.owner.name)}</itunes:name>
      <itunes:email>${esc(SHOW.owner.email)}</itunes:email>
    </itunes:owner>
    <itunes:image href="${esc(COVER_URL)}" />
    <itunes:category text="${esc(SHOW.category)}">
      <itunes:category text="${esc(SHOW.subcategory)}" />
    </itunes:category>
    <itunes:explicit>${SHOW.explicit ? 'true' : 'false'}</itunes:explicit>
    <itunes:type>episodic</itunes:type>
    ${items}
  </channel>
</rss>`;

  return new Response(xml, {
    status: 200,
    headers: { 'Content-Type': 'application/rss+xml; charset=utf-8' },
  });
};
