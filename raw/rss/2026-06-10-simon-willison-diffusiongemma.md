---
source: farmer/rss
feed: simon-willison
farmed: 2026-06-12T09:16:55.953613+00:00
title: DiffusionGemma
url: https://simonwillison.net/2026/Jun/10/diffusiongemma/#atom-everything
published: 2026-06-10
author: 
---

# DiffusionGemma

<p><strong><a href="https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/">DiffusionGemma</a></strong></p>
Last May Google briefly released an experimental Gemini Diffusion model. I <a href="https://simonwillison.net/2025/May/21/gemini-diffusion/">tried the preview at the time</a> and recorded it running at 857 tokens/second. It was an exciting model, but Google made no further announcements about it.</p>
<p>That research has returned in the best possible way: as a new open weight (Apache 2 licensed) Gemma model, <a href="https://huggingface.co/google/diffusiongemma-26B-A4B-it">google/diffusiongemma-26B-A4B-it</a>.</p>
<p>NVIDIA are currently <a href="https://build.nvidia.com/google/diffusiongemma-26b-a4b-it">hosting the model for free</a> on their NIM cloud API. I used that API to <a href="https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2Fe5e234a6dc6eef61e209ce1629620042">generate this pelican</a>, which took 4.4s (according to <code>time uv run generate.py</code>) to return 2,409 tokens - so at least 500 tokens/second.</p>
<p><img alt="Flat minimalist illustration of a white pelican with a large orange beak riding a red bicycle with black wheels, against a pale blue background with a green line representing the ground" src="https://static.simonwillison.net/static/2026/diffusiongemma-pelican.png" />

    <p><small></small>Via <a href="https://news.ycombinator.com/item?id=48478471">Hacker News</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/google">google</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/nvidia">nvidia</a>, <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle">pelican-riding-a-bicycle</a>, <a href="https://simonwillison.net/tags/gemma">gemma</a>, <a href="https://simonwillison.net/tags/llm-release">llm-release</a>, <a href="https://simonwillison.net/tags/llm-performance">llm-performance</a></p>
