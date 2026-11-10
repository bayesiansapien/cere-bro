---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-10T05:05:47.760962+00:00
title: "llm-anthropic 0.31"
url: https://simonwillison.net/2026/Nov/9/llm-anthropic/
published: 2026-11-09
author: 
---

# llm-anthropic 0.31

<p><strong>Release:</strong> <a href="https://github.com/simonw/llm-anthropic/releases/tag/0.31">llm-anthropic 0.31</a></p>
        <p>Anthropic <a href="https://www.anthropic.com/claude-fable-and-mythos-5-2">released Fable 5.2 and Mythos 5.2</a> today. I've added them to <code>llm-anthropic</code>, so you can now run prompts through Fable 5.2 like this:</p>
<pre><code>uv tool install llm
llm install llm-anthropic
llm keys set anthropic
# paste key here
llm -m claude-fable-5.2 "Generate an SVG of a pelican riding a bicycle"
</code></pre>
<p>I ran pelicans at all five reasoning levels - <code>low</code>, <code>medium</code>, <code>high</code>, <code>xhigh</code>, and <code>max</code>. You can <a href="https://tools.simonwillison.net/markdown-svg-renderer?url=https%3A%2F%2Fgist.github.com%2Fsimonw%2Fbcd1a1bf38b929b0bbbae2e38b808e97">see them all here</a> - here's the best result I got, from <code>xhigh</code>:</p>
<p><img alt="It's good - legs the right side of the bicycle, good frame, nice pouch, weird little fingers on the handlebars. The pouch looks slightly misaligned with the top of the beak." src="https://static.simonwillison.net/static/2026/fable-5.2-xhigh.avif" /></p>
<p><code>max</code> failed to return an image at all, running out of tokens after spending 128,000 <a href="https://tools.simonwillison.net/markdown-svg-renderer?url=https%3A%2F%2Fgist.github.com%2Fsimonw%2Fbcd1a1bf38b929b0bbbae2e38b808e97#reasoning-2">thinking about them</a>. That's the same bug that I saw with <a href="https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/#claude-opus-5-5-max-over-thinks-to-the-point-of-breaking">Opus 5.5</a> - but it's new for the Fable series, both <a href="https://simonwillison.net/2026/Jun/9/claude-fable-5/#and-some-pelicans">Fable 5</a> and <a href="https://simonwillison.net/2026/Sep/1/claude-fable-5-1/#max">Fable 5.1</a> returned max effort pelicans just fine.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/llm">llm</a>, <a href="https://simonwillison.net/tags/anthropic">anthropic</a>, <a href="https://simonwillison.net/tags/claude">claude</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle">pelican-riding-a-bicycle</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/claude-mythos-fable">claude-mythos-fable</a></p>
