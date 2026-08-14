---
source: farmer/rss
feed: simon-willison
farmed: 2026-08-14T05:50:10.573014+00:00
title: llm-gemini 0.33
url: https://simonwillison.net/2026/Aug/13/llm-gemini/
published: 2026-08-13
---

# llm-gemini 0.33

<p><strong>Release:</strong> <a href="https://github.com/simonw/llm-gemini/releases/tag/0.33">llm-gemini 0.33</a></p>
        <p>It's been a while since the last <code>llm-gemini</code> release. This version of the plugin adds support for today's <a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/">Gemini 3.7 Flash</a> release, plus <code>gemini-3.6-flash</code>, <code>gemini-3.5-flash-lite</code> and two embedding models <code>gemini-embedding-2</code> and <code>gemini-embedding-001</code>.</p>
<p>The plugin is also upgraded for compatibility with LLM 0.32, which means you can now see reasoning traces and you can also enable server-side tools using this pattern:</p>
<pre><code>llm -m gemini-3.7-flash -T CodeExecution \
  'use python to calculate (factorial of 13) * 3'
</code></pre>
<p>I had Gemini 3.7 Flash <a href="https://tools.simonwillison.net/markdown-svg-renderer.html#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F6779a22d5e7bb6bdf29936f1600a5259">draw me some pelicans riding bicycles</a> at high, medium, and low thinking efforts (minimal, which was an option in 3.6 Flash, has been removed in 3.7.) Here's the high level one, which is pretty great:</p>
<p><img alt="This pelican has  a very cool curved green bicycle, a fish in its basket, a lovely red and white spotted scarf and a captain's hat" src="https://static.simonwillison.net/static/2026/gemini-3.7-flash-high-pelican.jpg" /></p>
<p>One catch though: the pelican I showed here was rendered with Safari. Both Firefox and Chrome render it differently, due to Safari being more tolerant of empty SVG <code>&lt;filter&gt;</code> elements than those other two browsers.</p>
<p>They still display the bicycle, but the pelican is missing entirely!</p>
<p><img alt="The same image except the pelican is entirely missing - it's just the bicycle." src="https://static.simonwillison.net/static/2026/broken-pelican-safari.jpg" /></p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/google">google</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/llm">llm</a>, <a href="https://simonwillison.net/tags/gemini">gemini</a>, <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle">pelican-riding-a-bicycle</a>, <a href="https://simonwillison.net/tags/llm-release">llm-release</a></p>
