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
