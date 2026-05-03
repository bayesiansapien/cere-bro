// Atlas visualizations — donut, research heatmap, industry heatmap, momentum strips
import Chart from 'https://esm.sh/chart.js@4.4.0/auto';

const data = JSON.parse(document.getElementById('atlas-data').textContent);
const {
  topicColors,
  topicCounts,
  weeks,
  researchTopics,
  researchHeatmap,
  researchMomentum,
  industryTags,
  industryHeatmap,
  industryMomentum,
} = data;

const base = document.querySelector('a.brand')?.getAttribute('href') ?? '/';
const url = (p) => `${base.replace(/\/$/, '')}/${p.replace(/^\//, '')}`;

// Format week start ("2026-04-27") → "Apr 27"
function fmtWeek(iso) {
  const [, m, d] = iso.split('-').map(Number);
  const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  return `${months[m - 1]} ${d}`;
}

// Slug-ify topic name for URL
function topicHref(t) {
  return url(t);
}

// ── Topic distribution donut ──────────────────────────────────────────────────
{
  const topics = Object.entries(topicCounts).sort((a, b) => b[1] - a[1]);

  const ctx = document.getElementById('donut-chart');
  if (ctx) {
    new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: topics.map(([t]) => t),
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
            callbacks: {
              label: (ctx) => `${ctx.label}: ${ctx.parsed} pages`,
            },
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
          <a href="${topicHref(t)}/" class="topic-name">${t}</a>
          <span class="topic-count">${c}</span>
          <span class="topic-pct">${pct}%</span>
        </div>`;
      })
      .join('');
  }
}

// ── Heatmap rendering (shared for research + industry) ────────────────────────

function renderHeatmap(container, rows, weeks, getCount, getColor, getLabel, getKey) {
  if (!container) return;
  container.innerHTML = '';

  // Compute global max for opacity scaling
  let globalMax = 0;
  for (const row of rows) {
    for (const w of weeks) {
      const c = getCount(row, w);
      if (c > globalMax) globalMax = c;
    }
  }
  if (globalMax === 0) globalMax = 1;

  const wrapper = document.createElement('div');
  wrapper.className = 'heatmap-wrapper';

  // Top row: week labels
  const header = document.createElement('div');
  header.className = 'heatmap-row heatmap-header';
  header.innerHTML = '<div class="heatmap-label heatmap-corner"></div>' +
    weeks.map((w) => `<div class="heatmap-week-label">${fmtWeek(w)}</div>`).join('');
  wrapper.appendChild(header);

  // Data rows
  for (const row of rows) {
    const rowEl = document.createElement('div');
    rowEl.className = 'heatmap-row';
    const color = getColor(row);
    const label = getLabel(row);
    const labelEl = `<div class="heatmap-label" style="border-left-color:${color}">${label}</div>`;
    const cells = weeks
      .map((w) => {
        const c = getCount(row, w);
        const opacity = c === 0 ? 0.06 : 0.25 + (c / globalMax) * 0.75;
        const display = c > 0 ? c : '';
        return `<div class="heatmap-cell" style="background:${color}; opacity:${opacity}" title="${label} — ${fmtWeek(w)}: ${c} paper${c === 1 ? '' : 's'}">${display}</div>`;
      })
      .join('');
    rowEl.innerHTML = labelEl + cells;
    wrapper.appendChild(rowEl);
  }

  container.appendChild(wrapper);
}

// ── Research heatmap ──────────────────────────────────────────────────────────
renderHeatmap(
  document.getElementById('research-heatmap'),
  researchTopics,
  weeks,
  (topic, week) => researchHeatmap[topic]?.[week] ?? 0,
  (topic) => topicColors[topic] ?? '#94a3b8',
  (topic) => topic,
);

// ── Industry heatmap ──────────────────────────────────────────────────────────
renderHeatmap(
  document.getElementById('industry-heatmap'),
  industryTags,
  weeks,
  (tag, week) => industryHeatmap[tag.key]?.[week] ?? 0,
  (tag) => tag.color,
  (tag) => tag.label,
);

// ── Momentum strips ───────────────────────────────────────────────────────────

function renderMomentum(container, items, getName, getColor, getDelta, getThisWeek, ascending) {
  if (!container) return;

  const sorted = [...items].sort((a, b) =>
    ascending ? getDelta(a) - getDelta(b) : getDelta(b) - getDelta(a),
  );

  // Filter: only show non-zero deltas; if all zero, show top by thisWeek
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

// Research momentum
renderMomentum(
  document.getElementById('research-rising'),
  researchMomentum,
  (m) => m.topic,
  (m) => topicColors[m.topic] ?? '#94a3b8',
  (m) => m.delta,
  (m) => m.thisWeek,
  false,
);

renderMomentum(
  document.getElementById('research-cooling'),
  researchMomentum,
  (m) => m.topic,
  (m) => topicColors[m.topic] ?? '#94a3b8',
  (m) => m.delta,
  (m) => m.thisWeek,
  true,
);

// Industry momentum
renderMomentum(
  document.getElementById('industry-rising'),
  industryMomentum,
  (m) => m.label,
  (m) => m.color,
  (m) => m.delta,
  (m) => m.thisWeek,
  false,
);

renderMomentum(
  document.getElementById('industry-cooling'),
  industryMomentum,
  (m) => m.label,
  (m) => m.color,
  (m) => m.delta,
  (m) => m.thisWeek,
  true,
);
