---
source: farmer/rss
feed: simon-willison
farmed: 2026-10-07T10:46:48.512319+00:00
title: Mistral Large 4
url: https://simonwillison.net/2026/Oct/6/hn-49982139/
published: 2026-10-06
author: 
---

# Mistral Large 4

<p><a href="https://news.ycombinator.com/item?id=49977979#49982139">My comment</a> on <a href="https://news.ycombinator.com/item?id=49977979">Mistral Large 4</a> &mdash; Hacker News.</p><blockquote>
<p><a href="https://news.ycombinator.com/item?id=49977979#49979658">wren6991</a>: The benchmark is saturated. Frontier models are tested with an armadillo in fishnet tights jaywalking on Mars.</p>
</blockquote>
<p>OK well I couldn't resist this one:</p>
<pre><code>llm -m claude-opus-5.5 'Generate an SVG of an armadillo in fishnet tights jaywalking on Mars'
llm -m gpt-6.1-sol 'Generate an SVG of an armadillo in fishnet tights jaywalking on Mars'
llm -m gemini-3.8-flash 'Generate an SVG of an armadillo in fishnet tights jaywalking on Mars'
llm -m mistral/mistral-large-4 'Generate an SVG of an armadillo in fishnet tights jaywalking on Mars'
</code></pre>
<p>Default reasoning levels for each: <a href="https://tools.simonwillison.net/markdown-svg-renderer?url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F18c9f7fc3b3705cf88514cb9170ec246">https://tools.simonwillison.net/markdown-svg-renderer?url=ht...</a></p>
