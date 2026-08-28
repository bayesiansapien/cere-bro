---
source: farmer/rss
feed: simon-willison
farmed: 2026-08-28T09:21:34.832205+00:00
title: Qwen3.8-Flash-Next
url: https://simonwillison.net/2026/Aug/26/qwen38-flash-next/
published: 2026-08-26
---

# Qwen3.8-Flash-Next

<p><strong><a href="https://qwen.ai/blog?id=qwen3.8-flash-next">Qwen3.8-Flash-Next</a></strong></p>
Another open weights model from Qwen. This one is "a multimodal MoE model that also serves as an early preview of the architecture used in Qwen4".</p>
<p>It's pretty big: 125B tokens, but only 6B active which means it gets a significant performance boost.</p>
<p>I've been trying it out on a DGX Spark using <a href="https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF">these Unsloth quantized models</a>. I'm still exploring the model - so far I've tried the 72.5GB UD-IQ1_S one (producing <a href="https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2Ff9c69ebdab90d8a45b8de4742cc7b840">these pelicans</a>) and the 78.9GB UD-Q2_K_XL (producing <a href="https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F6ba7cbfc1a9336986703b41f7fccd73a">these</a>).</p>
<p>My favorite so far was this xhigh reasoning effort one from UD-Q2_K_XL:</p>
<p><img alt="Flat vector illustration: a white pelican with an orange beak and orange legs rides a red bicycle along a sandy path, a wicker basket on the handlebars holding a blue fish, with green rolling hills, a small tree and bushes, white clouds and a bright yellow sun in a blue sky behind it" src="https://static.simonwillison.net/static/2026-08-27/IMG_7667.png" />

    <p><small></small>Via <a href="https://news.ycombinator.com/item?id=49448210">Hacker News</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/qwen">qwen</a>, <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle">pelican-riding-a-bicycle</a>, <a href="https://simonwillison.net/tags/ai-in-china">ai-in-china</a>, <a href="https://simonwillison.net/tags/nvidia-spark">nvidia-spark</a></p>
