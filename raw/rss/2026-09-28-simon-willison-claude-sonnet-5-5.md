---
source: farmer/rss
feed: simon-willison
farmed: 2026-09-29T05:05:59.181600+00:00
title: Claude Sonnet 5.5
url: https://simonwillison.net/2026/Sep/28/claude-sonnet-5-5/
published: 2026-09-28
author: 
---

# Claude Sonnet 5.5

<p><strong><a href="https://www.anthropic.com/claude-sonnet-5-5">Claude Sonnet 5.5</a></strong></p>
New Sonnet model from Anthropic today. They say it "runs 30%+ faster, and costs up to 30% less for most work" - it's priced the same as Sonnet 5 but appears to beat it on every benchmark, and should be cheaper to run as well.</p>
<p><a href="https://tools.simonwillison.net/markdown-svg-renderer?url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F1d85a9be7f3ecce26e7f1569161a0d01">Here are some pelicans riding bicycles</a>. Sonnet 5.5 suffered from <a href="https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/#claude-opus-5-5-max-over-thinks-to-the-point-of-breaking">the same bug as Opus 5.5</a>: the "max" thinking effort pelican thought for 128,000 tokens (at a cost of $1.28) before running out of tokens and failing to produce an SVG.</p>
<p>Here's the pelican it gave me for thinking effort "xhigh", at a cost of 5.74 cents and taking 41 seconds:</p>
<p><img alt="It's good- correct bicycle frame, legs either side of the frame, feet touching the pedals, chain in the right place, it is wearing a misshapen blue bicycle helmet though." src="https://static.simonwillison.net/static/2026/claude-sonnet-5.5-pelican-xhigh.webp" /></p>
<p>Sonnet 5.5 appears to be almost as good as Opus 5.5 on some coding tasks, including various <a href="https://x.com/claudeai/status/2104674987164782598">viral 3D animation tricks</a>.</p>
<p>The most interesting thing about Sonnet 5.5 is that it's now the model used for the free tier on <a href="https://claude.ai/">claude.ai</a>. OpenAI's ChatGPT free tier uses Luna 5.6, which means Anthropic currently have a much more capable free offering.</p>
<p>I ran this prompt against that free tier:</p>
<blockquote>
<p><code>build me an HTML page that renders a three-dimensional pelican riding a bicycle using WebGL</code></p>
</blockquote>
<p>And got back <a href="https://static.simonwillison.net/static/2026/claude-sonnet-5.5-free-3d-pelican.html">this page</a>, which is a solid effort.</p>
<p>Anthropic's announcement reiterates that Haiku 5.5 will be available "in the coming weeks". I really hope that one is price-competitive with GPT-6 Luna!


    <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/anthropic">anthropic</a>, <a href="https://simonwillison.net/tags/claude">claude</a>, <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle">pelican-riding-a-bicycle</a>, <a href="https://simonwillison.net/tags/llm-release">llm-release</a></p>
