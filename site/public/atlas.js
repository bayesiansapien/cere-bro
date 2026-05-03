// Atlas visualization — timeline, donut, network graph
// Reads JSON from inline <script id="atlas-data">

import Chart from 'https://esm.sh/chart.js@4.4.0/auto';
import * as d3 from 'https://esm.sh/d3@7';

const data = JSON.parse(document.getElementById('atlas-data').textContent);
const { topicColors, topicCounts, timeline, nodes, edges } = data;

// Resolve URL with base path
const base = document.querySelector('a.brand')?.getAttribute('href') ?? '/';
const url = (p) => `${base.replace(/\/$/, '')}/${p.replace(/^\//, '')}`;

// ── Timeline (stacked bar chart) ──────────────────────────────────────────────
{
  const dates = Object.keys(timeline).sort();
  const topics = Object.keys(topicCounts).sort();

  const datasets = topics.map((topic) => ({
    label: topic,
    backgroundColor: topicColors[topic] ?? '#94a3b8',
    borderColor: topicColors[topic] ?? '#94a3b8',
    data: dates.map((d) => timeline[d]?.[topic] ?? 0),
    stack: 'all',
  }));

  const ctx = document.getElementById('timeline-chart');
  if (ctx) {
    new Chart(ctx, {
      type: 'bar',
      data: { labels: dates, datasets },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            mode: 'index',
            intersect: false,
            backgroundColor: '#16161f',
            borderColor: '#34343f',
            borderWidth: 1,
            titleColor: '#e5e7eb',
            bodyColor: '#94a3b8',
          },
        },
        scales: {
          x: {
            stacked: true,
            grid: { color: '#24242f' },
            ticks: { color: '#64748b', font: { family: 'JetBrains Mono', size: 10 } },
          },
          y: {
            stacked: true,
            grid: { color: '#24242f' },
            ticks: { color: '#64748b', precision: 0 },
            title: { display: true, text: 'pages added', color: '#94a3b8' },
          },
        },
      },
    });
  }

  // Custom legend
  const legend = document.getElementById('legend-timeline');
  if (legend) {
    legend.innerHTML = topics
      .map(
        (t) =>
          `<div class="legend-item"><span class="legend-swatch" style="background:${topicColors[t] ?? '#94a3b8'}"></span>${t}</div>`,
      )
      .join('');
  }
}

// ── Donut: topic distribution ─────────────────────────────────────────────────
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
        return `<div style="display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid #24242f">
          <span style="width:12px;height:12px;border-radius:3px;background:${color};display:inline-block"></span>
          <a href="${url(t)}/" style="flex:1;color:#e5e7eb;border:none">${t}</a>
          <span style="font-family:JetBrains Mono;color:#94a3b8;font-size:.85rem">${c}</span>
          <span style="font-family:JetBrains Mono;color:#64748b;font-size:.75rem;width:36px;text-align:right">${pct}%</span>
        </div>`;
      })
      .join('');
  }
}

// ── Network graph (D3 force-directed) ─────────────────────────────────────────
{
  const container = document.getElementById('network');
  const tooltip = document.getElementById('network-tooltip');
  if (!container) {
    console.warn('Network container missing');
  } else {
    const width = container.clientWidth;
    const height = container.clientHeight || 600;

    const svg = d3
      .select(container)
      .append('svg')
      .attr('width', width)
      .attr('height', height)
      .attr('viewBox', [0, 0, width, height]);

    const g = svg.append('g');

    // Zoom + pan
    svg.call(
      d3.zoom().scaleExtent([0.2, 4]).on('zoom', (event) => {
        g.attr('transform', event.transform);
      }),
    );

    // Filter to nodes that participate in the graph (have at least one edge)
    const connectedIds = new Set();
    edges.forEach((e) => {
      connectedIds.add(e.source);
      connectedIds.add(e.target);
    });
    const visibleNodes = nodes.filter((n) => connectedIds.has(n.id));
    const nodeMap = new Map(visibleNodes.map((n) => [n.id, n]));
    const visibleEdges = edges
      .filter((e) => nodeMap.has(e.source) && nodeMap.has(e.target))
      .map((e) => ({ source: e.source, target: e.target }));

    const sim = d3
      .forceSimulation(visibleNodes)
      .force(
        'link',
        d3
          .forceLink(visibleEdges)
          .id((d) => d.id)
          .distance(60)
          .strength(0.4),
      )
      .force('charge', d3.forceManyBody().strength(-180))
      .force('center', d3.forceCenter(width / 2, height / 2))
      .force('collide', d3.forceCollide().radius(12));

    const link = g
      .append('g')
      .attr('stroke', '#34343f')
      .attr('stroke-opacity', 0.55)
      .attr('stroke-width', 1)
      .selectAll('line')
      .data(visibleEdges)
      .join('line');

    const node = g
      .append('g')
      .selectAll('circle')
      .data(visibleNodes)
      .join('circle')
      .attr('r', (d) => (d.isConcept ? 9 : 6))
      .attr('fill', (d) => d.color)
      .attr('stroke', '#0a0a0f')
      .attr('stroke-width', 1.5)
      .style('cursor', 'pointer')
      .call(
        d3
          .drag()
          .on('start', (event, d) => {
            if (!event.active) sim.alphaTarget(0.3).restart();
            d.fx = d.x;
            d.fy = d.y;
          })
          .on('drag', (event, d) => {
            d.fx = event.x;
            d.fy = event.y;
          })
          .on('end', (event, d) => {
            if (!event.active) sim.alphaTarget(0);
            d.fx = null;
            d.fy = null;
          }),
      )
      .on('mouseenter', (event, d) => {
        tooltip.style.display = 'block';
        tooltip.innerHTML = `
          <div style="font-weight:600;margin-bottom:4px">${d.title}</div>
          <div style="color:${d.color};font-size:.7rem;text-transform:uppercase;letter-spacing:.05em">${d.topic}${d.date ? ' · ' + d.date : ''}</div>
        `;
      })
      .on('mousemove', (event) => {
        tooltip.style.left = event.clientX + 14 + 'px';
        tooltip.style.top = event.clientY + 14 + 'px';
      })
      .on('mouseleave', () => {
        tooltip.style.display = 'none';
      })
      .on('click', (event, d) => {
        window.location.href = url(d.id);
      });

    sim.on('tick', () => {
      link
        .attr('x1', (d) => d.source.x)
        .attr('y1', (d) => d.source.y)
        .attr('x2', (d) => d.target.x)
        .attr('y2', (d) => d.target.y);
      node.attr('cx', (d) => d.x).attr('cy', (d) => d.y);
    });

    // Legend
    const legend = document.getElementById('legend-network');
    if (legend) {
      legend.innerHTML = Object.entries(topicColors)
        .map(
          ([t, c]) =>
            `<div class="legend-item"><span class="legend-swatch" style="background:${c}"></span>${t}</div>`,
        )
        .join('');
    }
  }
}
