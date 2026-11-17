// Atlas visualizations — donut, heatmaps (week/month), cumulative line, momentum strips
import Chart from 'https://esm.sh/chart.js@4.4.0/auto';

const data = JSON.parse(document.getElementById('atlas-data').textContent);
const {
  topicColors,
  topicCounts,
  weeks,
  months,
  cumulativeWeeks,
  researchTopics,
  researchHeatmap,
  researchHeatmapMonthly,
  researchCumulative,
  researchMomentum,
  industryTags,
  industryHeatmap,
  industryHeatmapMonthly,
  industryCumulative,
  industryMomentum,
  tierKeys,
  tierColors,
  tierLabels,
  tierCounts,
  tierTopicBreakdown,
  tierConceptBreakdown,
  tierByWeek,
  sourceKeys,
  sourceLabels,
  tierBySource,
} = data;

const base = document.querySelector('a.brand')?.getAttribute('href') ?? '/';
const url = (p) => `${base.replace(/\/$/, '')}/${p.replace(/^\//, '')}`;

const MONTH_NAMES = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
function fmtWeek(iso) {
  const [, m, d] = iso.split('-').map(Number);
  return `${MONTH_NAMES[m - 1]} ${d}`;
}
function fmtMonth(iso) {
  const [y, m] = iso.split('-').map(Number);
  return `${MONTH_NAMES[m - 1]} '${String(y).slice(2)}`;
}
const topicHref = (t) => url(t);

// Pretty labels for slug-form topic keys
const TOPIC_LABEL = {
  'ai-routing':             'Routing',
  'inference-efficiency':   'Inference / Efficiency',
  'hardware':               'Hardware',
  'llms-foundation-models': 'LLMs & Foundation Models',
  'agentic-systems':        'Agentic Systems',
  'responsible-ai':         'Responsible AI',
  'vision-audio-video':     'Vision / Audio / Video',
  'ai-industry':            'Industry',
  'daily-digest':           'Daily Digest',
};
const labelOf = (t) => TOPIC_LABEL[t] ?? t;

// ── Topic distribution donut ──────────────────────────────────────────────────
{
  const topics = Object.entries(topicCounts)
    .filter(([t]) => t !== 'ai-industry')
    .sort((a, b) => b[1] - a[1]);

  const ctx = document.getElementById('donut-chart');
  if (ctx) {
    new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: topics.map(([t]) => labelOf(t)),
        datasets: [
          {
            data: topics.map(([, c]) => c),
            backgroundColor: topics.map(([t]) => topicColors[t] ?? '#94a3b8'),
            borderColor: '#0a0a0f',
            borderWidth: 2,
            hoverOffset: 8,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        cutout: '60%',
        plugins: {
          legend: { display: false },
          tooltip: {
            backgroundColor: '#16161f',
            borderColor: '#34343f',
            borderWidth: 1,
            titleColor: '#e5e7eb',
            bodyColor: '#94a3b8',
            callbacks: { label: (ctx) => `${ctx.label}: ${ctx.parsed} pages` },
          },
        },
      },
    });
  }

  const list = document.getElementById('topic-list');
  if (list) {
    const total = topics.reduce((s, [, c]) => s + c, 0);
    list.innerHTML = topics
      .map(([t, c]) => {
        const pct = ((c / total) * 100).toFixed(0);
        const color = topicColors[t] ?? '#94a3b8';
        return `<div class="topic-row">
          <span class="topic-swatch" style="background:${color}"></span>
          <a href="${topicHref(t)}/" class="topic-name">${labelOf(t)}</a>
          <span class="topic-count">${c}</span>
          <span class="topic-pct">${pct}%</span>
        </div>`;
      })
      .join('');
  }
}

// ── Heatmap rendering (parameterized by buckets) ──────────────────────────────

function renderHeatmap(container, rows, buckets, getCount, getColor, getLabel, fmtBucket, nCols) {
  if (!container) return;
  container.innerHTML = '';

  let globalMax = 0;
  for (const row of rows) {
    for (const b of buckets) {
      const c = getCount(row, b);
      if (c > globalMax) globalMax = c;
    }
  }
  if (globalMax === 0) globalMax = 1;

  const wrapper = document.createElement('div');
  wrapper.className = 'heatmap-wrapper';
  wrapper.style.setProperty('--cols', nCols);

  const header = document.createElement('div');
  header.className = 'heatmap-row heatmap-header';
  header.innerHTML = '<div class="heatmap-label heatmap-corner"></div>' +
    buckets.map((b) => `<div class="heatmap-week-label">${fmtBucket(b)}</div>`).join('');
  wrapper.appendChild(header);

  for (const row of rows) {
    const rowEl = document.createElement('div');
    rowEl.className = 'heatmap-row';
    const color = getColor(row);
    const label = getLabel(row);
    const labelEl = `<div class="heatmap-label" style="border-left-color:${color}">${label}</div>`;
    const cells = buckets
      .map((b) => {
        const c = getCount(row, b);
        const opacity = c === 0 ? 0.06 : 0.25 + (c / globalMax) * 0.75;
        const display = c > 0 ? c : '';
        return `<div class="heatmap-cell" style="background:${color}; opacity:${opacity}" title="${label} — ${fmtBucket(b)}: ${c} paper${c === 1 ? '' : 's'}">${display}</div>`;
      })
      .join('');
    rowEl.innerHTML = labelEl + cells;
    wrapper.appendChild(rowEl);
  }

  container.appendChild(wrapper);
}

// Research heatmaps — weekly and monthly
renderHeatmap(
  document.getElementById('research-heatmap-week'),
  researchTopics,
  weeks,
  (t, b) => researchHeatmap[t]?.[b] ?? 0,
  (t) => topicColors[t] ?? '#94a3b8',
  labelOf,
  fmtWeek,
  weeks.length,
);
renderHeatmap(
  document.getElementById('research-heatmap-month'),
  researchTopics,
  months,
  (t, b) => researchHeatmapMonthly[t]?.[b] ?? 0,
  (t) => topicColors[t] ?? '#94a3b8',
  labelOf,
  fmtMonth,
  months.length,
);

// Industry heatmaps — weekly and monthly
renderHeatmap(
  document.getElementById('industry-heatmap-week'),
  industryTags,
  weeks,
  (tag, b) => industryHeatmap[tag.key]?.[b] ?? 0,
  (tag) => tag.color,
  (tag) => tag.label,
  fmtWeek,
  weeks.length,
);
renderHeatmap(
  document.getElementById('industry-heatmap-month'),
  industryTags,
  months,
  (tag, b) => industryHeatmapMonthly[tag.key]?.[b] ?? 0,
  (tag) => tag.color,
  (tag) => tag.label,
  fmtMonth,
  months.length,
);

// ── Cumulative stacked-area charts ────────────────────────────────────────────

function renderCumulative(canvasId, weeksArr, dataByKey, colorByKey, labelByKey) {
  const ctx = document.getElementById(canvasId);
  if (!ctx) return;
  const labels = weeksArr.map(fmtWeek);
  const datasets = Object.keys(dataByKey).map((key) => ({
    label: labelByKey(key),
    data: dataByKey[key],
    borderColor: colorByKey(key),
    backgroundColor: colorByKey(key) + 'CC',
    fill: true,
    tension: 0.25,
    pointRadius: 0,
    pointHoverRadius: 4,
    borderWidth: 1.5,
  }));
  new Chart(ctx, {
    type: 'line',
    data: { labels, datasets },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      interaction: { mode: 'index', intersect: false },
      plugins: {
        legend: {
          display: true,
          position: 'bottom',
          labels: {
            color: '#94a3b8',
            font: { family: 'Inter', size: 11 },
            boxWidth: 12,
            padding: 12,
          },
        },
        tooltip: {
          backgroundColor: '#16161f',
          borderColor: '#34343f',
          borderWidth: 1,
          titleColor: '#e5e7eb',
          bodyColor: '#94a3b8',
          itemSort: (a, b) => b.parsed.y - a.parsed.y,
        },
      },
      scales: {
        x: {
          grid: { color: '#24242f' },
          ticks: {
            color: '#64748b',
            font: { family: 'JetBrains Mono', size: 10 },
            maxRotation: 0,
            autoSkip: true,
            maxTicksLimit: 12,
          },
        },
        y: {
          stacked: true,
          grid: { color: '#24242f' },
          ticks: { color: '#64748b', precision: 0 },
          title: { display: true, text: 'cumulative pages', color: '#94a3b8' },
        },
      },
    },
  });
}

renderCumulative(
  'research-cumulative',
  cumulativeWeeks,
  researchCumulative,
  (k) => topicColors[k] ?? '#94a3b8',
  labelOf,
);

const industryDataByKey = {};
const industryColorByKey = {};
const industryLabelByKey = {};
for (const tag of industryTags) {
  industryDataByKey[tag.key] = industryCumulative[tag.key];
  industryColorByKey[tag.key] = tag.color;
  industryLabelByKey[tag.key] = tag.label;
}
renderCumulative(
  'industry-cumulative',
  cumulativeWeeks,
  industryDataByKey,
  (k) => industryColorByKey[k],
  (k) => industryLabelByKey[k],
);

// ── View toggles (Week / Month / All-time) ────────────────────────────────────
document.querySelectorAll('.view-toggle').forEach((toggle) => {
  const group = toggle.getAttribute('data-view-group');
  toggle.addEventListener('click', (e) => {
    const btn = e.target.closest('.view-btn');
    if (!btn) return;
    const view = btn.getAttribute('data-view');
    toggle.querySelectorAll('.view-btn').forEach((b) => b.classList.toggle('active', b === btn));
    document.querySelectorAll(`[data-view-pane^="${group}-"]`).forEach((pane) => {
      pane.classList.toggle('hidden', pane.getAttribute('data-view-pane') !== `${group}-${view}`);
    });
  });
});

// ── Momentum strips ───────────────────────────────────────────────────────────

function renderMomentum(container, items, getName, getColor, getDelta, getThisWeek, ascending) {
  if (!container) return;

  const sorted = [...items].sort((a, b) =>
    ascending ? getDelta(a) - getDelta(b) : getDelta(b) - getDelta(a),
  );
  const filtered = sorted.filter((it) => (ascending ? getDelta(it) < 0 : getDelta(it) > 0));
  const fallback = sorted.slice(0, 3);
  const top = (filtered.length > 0 ? filtered : fallback).slice(0, 5);

  if (top.length === 0) {
    container.innerHTML = '<div class="momentum-empty">No movement this week.</div>';
    return;
  }

  container.innerHTML = top
    .map((it) => {
      const name = getName(it);
      const color = getColor(it);
      const delta = getDelta(it);
      const tw = getThisWeek(it);
      const sign = delta > 0 ? '+' : '';
      const arrow = delta > 0 ? '↑' : delta < 0 ? '↓' : '·';
      const cls = delta > 0 ? 'up' : delta < 0 ? 'down' : 'flat';
      return `<div class="momentum-item">
        <span class="momentum-swatch" style="background:${color}"></span>
        <span class="momentum-name">${name}</span>
        <span class="momentum-count">${tw} this week</span>
        <span class="momentum-delta ${cls}">${arrow} ${sign}${delta}</span>
      </div>`;
    })
    .join('');
}

renderMomentum(document.getElementById('research-rising'), researchMomentum, (m) => labelOf(m.topic), (m) => topicColors[m.topic] ?? '#94a3b8', (m) => m.delta, (m) => m.thisWeek, false);
renderMomentum(document.getElementById('research-cooling'), researchMomentum, (m) => labelOf(m.topic), (m) => topicColors[m.topic] ?? '#94a3b8', (m) => m.delta, (m) => m.thisWeek, true);
renderMomentum(document.getElementById('industry-rising'), industryMomentum, (m) => m.label, (m) => m.color, (m) => m.delta, (m) => m.thisWeek, false);
renderMomentum(document.getElementById('industry-cooling'), industryMomentum, (m) => m.label, (m) => m.color, (m) => m.delta, (m) => m.thisWeek, true);

// ────────────────────────────────────────────────────────────────────────────
// ATTENTION TIER VISUALIZATIONS
// ────────────────────────────────────────────────────────────────────────────

// (1) Tier donut — composition of summary pages by tier
if (tierKeys && tierCounts) {
  const tierDonutEl = document.getElementById('tier-donut');
  if (tierDonutEl) {
    // Filter out unknown if it has zero count, otherwise keep it visible
    const ks = tierKeys.filter((k) => tierCounts[k] > 0);
    const total = ks.reduce((sum, k) => sum + tierCounts[k], 0);
    new Chart(tierDonutEl, {
      type: 'doughnut',
      data: {
        labels: ks.map((k) => tierLabels[k]),
        datasets: [{
          data: ks.map((k) => tierCounts[k]),
          backgroundColor: ks.map((k) => tierColors[k]),
          borderColor: '#0b0d10',
          borderWidth: 2,
          hoverOffset: 8,
        }],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        cutout: '60%',
        plugins: {
          legend: {
            position: 'bottom',
            labels: { color: '#94a3b8', boxWidth: 14, padding: 12 },
          },
          tooltip: {
            callbacks: {
              label: (ctx) => {
                const v = ctx.parsed;
                const pct = total ? Math.round((v / total) * 100) : 0;
                return `${ctx.label}: ${v} pages (${pct}%)`;
              },
            },
          },
        },
      },
    });
  }
}

// (1b) Tier topic breakdown — list view, showing topics under each tier
//     plus concept-page vs summary ratio (synthesis depth)
if (tierKeys && tierTopicBreakdown) {
  const el = document.getElementById('tier-topic-breakdown');
  if (el) {
    const ks = tierKeys.filter((k) => tierCounts[k] > 0);
    el.innerHTML = ks.map((k) => {
      const topics = tierTopicBreakdown[k] || {};
      const topicList = Object.entries(topics)
        .sort(([, a], [, b]) => b - a)
        .map(([t, n]) => {
          const color = topicColors[t] ?? '#94a3b8';
          return `<li>
            <span class="momentum-swatch" style="background:${color}"></span>
            <span class="momentum-name">${labelOf(t)}</span>
            <span class="momentum-count">${n}</span>
          </li>`;
        })
        .join('');
      const cb = tierConceptBreakdown?.[k] ?? { summaries: 0, concepts: 0 };
      const synthRatio = cb.summaries
        ? Math.round((cb.concepts / cb.summaries) * 100)
        : 0;
      return `<div class="tier-block" style="margin-bottom: 18px">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:6px">
          <strong style="color:${tierColors[k]}">${tierLabels[k]}</strong>
          <span style="color:#64748b; font-size:0.85em">${cb.summaries} summaries · ${cb.concepts} concept pages</span>
        </div>
        <ul style="list-style:none; padding:0; margin:0">${topicList}</ul>
      </div>`;
    }).join('');
  }
}

// (2) Tier momentum — stacked area chart, weekly composition over last 12 weeks
if (tierKeys && tierByWeek && weeks) {
  const el = document.getElementById('tier-momentum');
  if (el) {
    const ks = tierKeys.filter((k) => k !== 'unknown' || tierCounts[k] > 0);
    new Chart(el, {
      type: 'line',
      data: {
        labels: weeks.map(fmtWeek),
        datasets: ks.map((k) => ({
          label: tierLabels[k],
          data: weeks.map((w) => tierByWeek[k]?.[w] ?? 0),
          backgroundColor: tierColors[k] + '88',
          borderColor: tierColors[k],
          borderWidth: 2,
          fill: true,
          tension: 0.3,
          pointRadius: 2,
          pointHoverRadius: 5,
        })),
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        interaction: { mode: 'index', intersect: false },
        scales: {
          x: {
            stacked: true,
            grid: { color: '#1f2937' },
            ticks: { color: '#94a3b8' },
          },
          y: {
            stacked: true,
            beginAtZero: true,
            grid: { color: '#1f2937' },
            ticks: { color: '#94a3b8' },
            title: { display: true, text: 'summary pages per week', color: '#64748b' },
          },
        },
        plugins: {
          legend: {
            position: 'top',
            labels: { color: '#94a3b8', boxWidth: 14, padding: 12 },
          },
          tooltip: {
            callbacks: {
              label: (ctx) => `${ctx.dataset.label}: ${ctx.parsed.y}`,
            },
          },
        },
      },
    });
  }
}

// (3) Tier × Source heatmap — rendered as a simple HTML grid
if (sourceKeys && tierBySource && tierKeys) {
  const el = document.getElementById('tier-source-heatmap');
  if (el) {
    const tks = tierKeys.filter((k) => k !== 'unknown' || tierCounts[k] > 0);
    // Find max for normalization
    let max = 0;
    for (const s of sourceKeys) {
      for (const k of tks) {
        max = Math.max(max, tierBySource[s]?.[k] ?? 0);
      }
    }
    // Filter out source rows that are entirely empty
    const visibleSources = sourceKeys.filter((s) =>
      tks.some((k) => (tierBySource[s]?.[k] ?? 0) > 0),
    );

    const intensity = (v) => (max > 0 ? Math.min(1, v / max) : 0);
    const cellColor = (v, k) => {
      const a = intensity(v);
      if (a === 0) return '#0f1318';
      // Tint with the tier's color, scaled by intensity
      return `${tierColors[k]}${Math.round(48 + a * 207).toString(16).padStart(2, '0')}`;
    };

    const header = `<div class="tier-hm-row tier-hm-header">
      <div class="tier-hm-source-label"></div>
      ${tks.map((k) => `<div class="tier-hm-cell tier-hm-col-label" style="color:${tierColors[k]}">${k === 'unknown' ? 'Untagged' : 'Tier ' + k}</div>`).join('')}
    </div>`;
    const rows = visibleSources.map((s) => {
      const cells = tks.map((k) => {
        const v = tierBySource[s]?.[k] ?? 0;
        return `<div class="tier-hm-cell" style="background:${cellColor(v, k)}" title="${sourceLabels[s]} → ${tierLabels[k]}: ${v} pages">${v || ''}</div>`;
      }).join('');
      return `<div class="tier-hm-row">
        <div class="tier-hm-source-label">${sourceLabels[s]}</div>
        ${cells}
      </div>`;
    }).join('');
    el.innerHTML = `<div class="tier-hm">${header}${rows}</div>`;
  }
}

// ────────────────────────────────────────────────────────────────────────────
// RESEARCH THEMES — map, emerging/cooling, area breakdown
// ────────────────────────────────────────────────────────────────────────────
const { themes = [], themeEdges = [], weeks12 = [] } = data;
const themeById = Object.fromEntries(themes.map((t) => [t.id, t]));
const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);

function sparkline(vals, color, w = 90, h = 22) {
  const max = Math.max(1, ...vals);
  const step = vals.length > 1 ? w / (vals.length - 1) : w;
  const pts = vals.map((v, i) => `${(i * step).toFixed(1)},${(h - 2 - (v / max) * (h - 4)).toFixed(1)}`).join(' ');
  return `<svg class="spark" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" aria-hidden="true"><polyline fill="none" stroke="${color}" stroke-width="1.6" points="${pts}"/></svg>`;
}

function showTheme(id) {
  const t = themeById[id];
  const el = document.getElementById('theme-panel');
  if (!t || !el) return;
  const related = themeEdges
    .filter((e) => e.a === id || e.b === id)
    .map((e) => ({ other: e.a === id ? e.b : e.a, w: e.w }))
    .sort((a, b) => b.w - a.w).slice(0, 5)
    .map((r) => `<button class="theme-chip" data-theme="${r.other}" style="border-color:${themeById[r.other]?.color}">${esc(themeById[r.other]?.label)} · ${r.w}</button>`).join('');
  el.innerHTML = `
    <div class="theme-panel-head" style="border-left:4px solid ${t.color}">
      <h3>${esc(t.label)}</h3>
      <div class="card-sub">${esc(t.desc)}</div>
    </div>
    <div class="theme-stats">
      <span><strong>${t.count}</strong> papers</span>
      <span><strong>${t.recent}</strong> in last 4 weeks</span>
      ${sparkline(t.weekly, t.color, 110, 26)}
    </div>
    ${related ? `<div class="theme-sub">Often appears with</div><div class="theme-chips">${related}</div>` : ''}
    <div class="theme-sub">Recent papers</div>
    <ul class="theme-papers">${t.papers.map((p) => `<li><a href="${url(p.id)}/">${esc(p.title)}</a><span>${p.date ?? ''}</span></li>`).join('')}</ul>`;
  el.querySelectorAll('.theme-chip').forEach((b) => b.addEventListener('click', () => selectTheme(b.dataset.theme)));
}

let selectTheme = showTheme;

// (T1) Theme map: force layout, bubble = paper count, line = co-occurrence
if (themes.length && document.getElementById('theme-map')) {
  const d3 = await import('https://esm.sh/d3@7.9.0');
  const host = document.getElementById('theme-map');
  const W = host.clientWidth || 700;
  const H = Math.max(460, Math.min(680, W * 0.82));
  const nodes = themes.filter((t) => t.count > 0).map((t) => ({ ...t }));
  const ids = new Set(nodes.map((n) => n.id));
  const maxW = Math.max(1, ...themeEdges.map((e) => e.w));
  const links = themeEdges.filter((e) => ids.has(e.a) && ids.has(e.b))
    .map((e) => ({ source: e.a, target: e.b, w: e.w }));
  const r = d3.scaleSqrt().domain([0, d3.max(nodes, (n) => n.count)]).range([6, Math.min(46, W / 14)]);

  const svg = d3.select(host).append('svg').attr('viewBox', `0 0 ${W} ${H}`).attr('width', '100%').attr('height', H);
  const link = svg.append('g').selectAll('line').data(links).join('line')
    .attr('stroke', '#475569').attr('stroke-opacity', (d) => 0.15 + 0.6 * (d.w / maxW))
    .attr('stroke-width', (d) => 0.5 + 3 * (d.w / maxW));
  const node = svg.append('g').selectAll('g').data(nodes).join('g').attr('class', 'theme-node').style('cursor', 'pointer');
  node.append('circle').attr('r', (d) => r(d.count)).attr('fill', (d) => d.color).attr('fill-opacity', 0.85)
    .attr('stroke', '#0a0a0f').attr('stroke-width', 1.5);
  const maxCount = d3.max(nodes, (n) => n.count);
  node.append('text').text((d) => d.label).attr('text-anchor', 'middle')
    .attr('dy', (d) => r(d.count) + 11).attr('fill', '#cbd5e1').attr('font-size', 10)
    .attr('paint-order', 'stroke').attr('stroke', '#16161f').attr('stroke-width', 3)
    .attr('opacity', (d) => (d.count >= maxCount * 0.18 || d.tier === 1 ? 1 : 0))
    .attr('pointer-events', 'none');
  node.on('mouseenter', function () { d3.select(this).select('text').attr('opacity', 1); })
    .on('mouseleave', function (_, d) { d3.select(this).select('text').attr('opacity', d.count >= maxCount * 0.18 || d.tier === 1 ? 1 : 0); });
  node.append('title').text((d) => `${d.label}: ${d.count} papers, ${d.recent} in last 4 weeks`);

  selectTheme = (id) => {
    node.select('circle').attr('stroke', (d) => (d.id === id ? '#fff' : '#0a0a0f')).attr('stroke-width', (d) => (d.id === id ? 3 : 1.5));
    link.attr('stroke', (d) => (d.source.id === id || d.target.id === id ? '#e2e8f0' : '#475569'));
    showTheme(id);
  };
  node.on('click', (_, d) => selectTheme(d.id));

  // Each area gets an anchor on a ring, so its themes cluster together and
  // the co-occurrence lines show which areas bleed into each other.
  const areaList = [...new Set(nodes.map((n) => n.area))];
  const anchor = Object.fromEntries(areaList.map((a, i) => {
    const ang = (2 * Math.PI * i) / areaList.length - Math.PI / 2;
    return [a, { x: W / 2 + Math.cos(ang) * W * 0.3, y: H / 2 + Math.sin(ang) * H * 0.32 }];
  }));
  const sim = d3.forceSimulation(nodes)
    .force('link', d3.forceLink(links).id((d) => d.id).distance(110).strength((d) => 0.02 + 0.15 * (d.w / maxW)))
    .force('charge', d3.forceManyBody().strength(-220))
    .force('collide', d3.forceCollide().radius((d) => r(d.count) + 18))
    .force('x', d3.forceX((d) => anchor[d.area].x).strength(0.18))
    .force('y', d3.forceY((d) => anchor[d.area].y).strength(0.18))
    .on('tick', () => {
      nodes.forEach((d) => { d.x = Math.max(r(d.count), Math.min(W - r(d.count), d.x)); d.y = Math.max(r(d.count), Math.min(H - r(d.count) - 14, d.y)); });
      link.attr('x1', (d) => d.source.x).attr('y1', (d) => d.source.y).attr('x2', (d) => d.target.x).attr('y2', (d) => d.target.y);
      node.attr('transform', (d) => `translate(${d.x},${d.y})`);
    });
  node.call(d3.drag()
    .on('start', (e, d) => { if (!e.active) sim.alphaTarget(0.2).restart(); d.fx = d.x; d.fy = d.y; })
    .on('drag', (e, d) => { d.fx = e.x; d.fy = e.y; })
    .on('end', (e, d) => { if (!e.active) sim.alphaTarget(0); d.fx = null; d.fy = null; }));

  const top = [...nodes].filter((n) => n.tier === 1).sort((a, b) => b.recent - a.recent)[0];
  if (top) selectTheme(top.id);
}

// (T2) Emerging / cooling: last 4 weeks vs the 4 before
function themeRows(list, up) {
  return list.map((t) => {
    const d = t.recent - t.prior;
    return `<div class="momentum-item theme-row" data-theme="${t.id}">
      <span class="momentum-swatch" style="background:${t.color}"></span>
      <span class="momentum-name">${esc(t.label)}</span>
      ${sparkline(t.weekly, t.color, 70, 18)}
      <span class="momentum-count">${t.recent} vs ${t.prior}</span>
      <span class="momentum-delta ${up ? 'up' : 'down'}">${up ? '↑' : '↓'} ${d > 0 ? '+' : ''}${d}</span>
    </div>`;
  }).join('') || '<p class="card-sub">Nothing notable.</p>';
}
{
  const live = themes.filter((t) => t.recent + t.prior >= 4);
  // Score = change scaled by sqrt of the base, so both a big theme moving a lot and a
  // small theme genuinely taking off rank, but a 4-vs-0 blip does not top the list.
  const score = (t) => (t.recent - t.prior) / Math.sqrt(t.prior + 4);
  const rising = live.filter((t) => t.recent > t.prior).sort((a, b) => score(b) - score(a)).slice(0, 8);
  const cooling = live.filter((t) => t.recent < t.prior).sort((a, b) => score(a) - score(b)).slice(0, 8);
  const re = document.getElementById('theme-rising');
  const co = document.getElementById('theme-cooling');
  if (re) re.innerHTML = themeRows(rising, true);
  if (co) co.innerHTML = themeRows(cooling, false);
}

// (T3) Themes grouped by area
{
  const el = document.getElementById('theme-areas');
  if (el && themes.length) {
    const areas = [...new Set(themes.map((t) => t.area))];
    el.innerHTML = areas.map((a) => {
      const ts = themes.filter((t) => t.area === a).sort((x, y) => y.count - x.count);
      const max = Math.max(1, ...ts.map((t) => t.count));
      return `<div class="chart-card theme-area">
        <h3 class="card-title" style="color:${topicColors[a] ?? '#94a3b8'}">${labelOf(a)}</h3>
        ${ts.map((t) => `<div class="theme-bar-row theme-row" data-theme="${t.id}">
          <span class="theme-bar-label">${esc(t.label)}</span>
          <span class="theme-bar"><span style="width:${(100 * t.count / max).toFixed(0)}%;background:${t.color}"></span></span>
          <span class="momentum-count">${t.count}</span>
          ${sparkline(t.weekly, t.color, 60, 16)}
        </div>`).join('')}
      </div>`;
    }).join('');
  }
}

document.querySelectorAll('.theme-row').forEach((row) => row.addEventListener('click', () => {
  selectTheme(row.dataset.theme);
  document.getElementById('theme-map')?.scrollIntoView({ behavior: 'smooth', block: 'center' });
}));
