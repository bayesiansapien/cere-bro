---
source: farmer/rss
feed: simon-willison
farmed: 2026-09-04T08:40:42.061393+00:00
title: GPT‑6 Astra
url: https://simonwillison.net/2026/Sep/3/gpt6-astra/
published: 2026-09-03
---

# GPT‑6 Astra

<p><strong><a href="https://openai.com/index/gpt-6-astra/">GPT‑6 Astra</a></strong></p>
GPT-6 Astra is "rolling out today to a limited set of organizations and over the coming days will become available to all ChatGPT Plus, Pro, Business, and Enterprise users, as well as through the OpenAI API and AWS" - I've not tried it yet myself, so I don't have a great deal to say about it yet.</p>
<p>It's going to be API priced at the same rate as Claude Fable 5 and 5.1: $10/million input and $50/million output. This is clearly OpenAI's Fable competitor, and appears to score higher than Fable on most of OpenAI's self-reported benchmarks.</p>
<p>Most impressively, Astra scores 99.9% on the recent (released in March) <a href="https://arcprize.org/arc-agi/3">ARC-AGI 3 benchmark</a> - though notably Fable 5 does not yet have a published result, and the <a href="https://arcprize.org/blog/astra">ARC-AGI blog notes</a> that the 99.9% score was achieved for $19K using OpenAI's custom "Provider Adapter harness", while the default ARC-AGI harness scored 62.7% for $26K.</p>
<blockquote>
<p>The Provider Adapter harness preserves opaque reasoning state between requests and uses compaction for longer conversations, allowing the model to reuse prior work.</p>
</blockquote>
<p>Unsurprisingly, given <a href="https://simonwillison.net/tags/openai-hugging-face-incident/">the recent Hugging Face incident</a>, Astra is a beast at security tasks. It scores 100% on ExploitBench (GPT-5.6 Sol got 78.5%), 42.4% on ExploitGym (Sol got 30.3%), and 99.2% within four attempts on SRE-Bench binary reverse engineering compared to Sol's 68.7%.</p>
<p>It's also better at long context: on OpenAI's eight-needle benchmark it got 100% at 256K–512K tokens and 96.3% at 512K–1M tokens. OpenAI may have vanquished one of the ongoing challenges with long context processing.</p>
<p>It doesn't win at everything though. <a href="https://twitter.com/ArtificialAnlys/status/2095595489031000350">Artificial Analysis</a> note that Astra is still beaten by Fable on their Intelligence Index:</p>
<blockquote>
<p><strong>Sits beside GPT-5.6 Sol in Intelligence</strong>: GPT-6 Astra scores equal to GPT-5.6 Sol in the Index at 61. This is 5 points lower than Claude Fable 5.1 (max with fallback). The model also trails Meta’s newly released Muse Spark 1.3 (max).</p>
</blockquote>
<p>It did better on their Coding Agent Index:</p>
<blockquote>
<p><strong>Leads Coding Agent Index cost efficiency frontier</strong>: At max effort, GPT-6 Astra costs about the same as GPT-5.6 Sol (max) while scoring 2 points higher on the Index. Per task, the model is less than half the cost of Claude Fable 5, for the same score.</p>
</blockquote>
<p>I'll write more about Astra once I get access to it. The API model label once it rolls out will be <code>gpt-6-astra</code>.</p>
<!-- <small>OpenAI's blog keeps throwing 500 errors, but [here's a mirror](https://astratest.codergautam.workers.dev/GPT-6%20Astra_%20A%20new%20generation%20of%20intelligence%20_%20OpenAI) of the post I found [via Hacker News](https://news.ycombinator.com/item?id=49554273#49555070).</small> -->

    <p><small></small>Via <a href="https://news.ycombinator.com/item?id=49554643">Hacker News</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/openai">openai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/llm-release">llm-release</a></p>
