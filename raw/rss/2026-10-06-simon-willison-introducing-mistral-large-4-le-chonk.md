---
source: farmer/rss
feed: simon-willison
farmed: 2026-10-07T10:46:48.512319+00:00
title: Introducing Mistral Large 4: Le chonk
url: https://simonwillison.net/2026/Oct/6/le-chonk/
published: 2026-10-06
author: 
---

# Introducing Mistral Large 4: Le chonk

<p><strong><a href="https://mistral.ai/news/mistral-large-4/">Introducing Mistral Large 4: Le chonk</a></strong></p>
Mistral are back in the game. Today they're releasing a preview of Mistral Large 4, a 1 trillion parameter, 49 billion active parameter model trained on their own cluster of 3,800 NVIDIA Grace Blackwell GPUs.</p>
<p>The preview is available via their API. They promise to release the open weights model at the "end of this month".</p>
<p>The model only supports two reasoning levels - "none" and "high" - via the Mistral API. Here are <a href="https://tools.simonwillison.net/markdown-svg-renderer?url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F0db8b8196e57711b352f6c5857cf5b35">both pelicans</a> - the "high" one looks better, though surprisingly it only used 2,717 output tokens compared to "none" which used 3,275:</p>
<p><img alt="It's good. The pouch is great, the bicycle frame is the right size, it has feet on pedals. Both pedals appear in front of the frame though. Nice gradients." src="https://static.simonwillison.net/static/2026-10-06/mistral-large-4-pelican.webp" /></p>
<p>On Artificial Analysis <a href="https://artificialanalysis.ai/models/mistral-large-4">it scores 38</a>, just behind DeepSeek 4.1 Flash, which is a 552B model. It's a <em>huge</em> improvement on last December's Mistral Large 3, which drew <a href="https://tools.simonwillison.net/markdown-svg-renderer?url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F0df5e656291d5a7a1bf012fabc9edc3f#response-1">this terrible pelican</a> and <a href="https://artificialanalysis.ai/models/mistral-large-3">scored 9 on AA</a>.</p>
<p>It's certainly not a Fable-class model, but it's great to see Mistral put out a model that's back to being maybe about 6 months behind the frontier.

    <p><small></small>Via <a href="https://news.ycombinator.com/item?id=49977979">Hacker News</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/mistral">mistral</a>, <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle">pelican-riding-a-bicycle</a>, <a href="https://simonwillison.net/tags/llm-release">llm-release</a></p>
