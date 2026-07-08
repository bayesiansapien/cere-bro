---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-08T05:20:41Z
title: Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding
url: https://simonwillison.net/2026/Jun/29/ornith/#atom-everything
published: 2026-06-29
author: 
---

# Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding

<p><strong><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding</a></strong></p>
This is an interesting new open weights (MIT licensed) model, the first model release from DeepReinforce.</p>
<blockquote>
<p>[...] with variants including 9B Dense, 31B Dense, 35B MoE, and 397B MoE. Built on top of pretrained Gemma 4 and Qwen 3.5, it achieves state-of-the-art performance among open-source models of comparable size on coding benchmarks.</p>
</blockquote>
<p>As far as I can tell the licenses of those underlying models is compatible with being used in this way - Gemma 4 is Apache 2.0 licensed (and not bound by the janky additional <a href="https://ai.google.dev/gemma/terms">Gemma Terms of Use</a> that afflicted the previous Gemma models) and Qwen 3.5 is Apache 2.0 licensed as well.</p>
<p>I've been running the model using LM Studio and the <a href="https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF">ornith-1.0-35b-Q4_K_M.gguf</a> (20GB) GGUF, hooked up to <a href="https://pi.dev/">Pi</a>. Initial impressions are very good - it seems to be able to run the agent harness over many tool calls in a proficient way.</p>
<p>Here's <a href="https://gisthost.github.io/?35da4d9ce7f0c27124c67655a0dc9e5d">a terminal session</a> where I asked it to "find the code that decodes the actor cookie" and then "find the code that opens the insert dialog when thebutton is clicked" against a Datasette checkout, which it handled with ease.</p>
<p>I also had it <a href="https://gist.github.com/simonw/1869e1bbcafe5bcad0f26351f6a978a6">draw this pelican</a>, which came out at 103 tokens/second:</p>
<p><img alt="Cartoon illustration of a white pelican (albeit slightly mangled) with a large orange beak riding a red bicycle across green hills. The scene has a blue sky with a yellow sun and three white clouds, and small grass tufts dot the foreground." src="https://static.simonwillison.net/static/2024/ornith-1-pelican.png" /></p>
<p>It's a little bit mangled but the pelican is clearly a pelican.</p>
<p>I couldn't find much information about DeepReinforce themselves. The earliest paper I could find from the was <a href="https://arxiv.org/abs/2507.14111">CUDA-L1: Improving CUDA Optimization via Contrastive Reinforcement Learning</a> from June 2025.


    <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/local-llms">local-llms</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/qwen">qwen</a>, <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle">pelican-riding-a-bicycle</a>, <a href="https://simonwillison.net/tags/gemma">gemma</a>, <a href="https://simonwillison.net/tags/llm-release">llm-release</a>, <a href="https://simonwillison.net/tags/lm-studio">lm-studio</a></p>
