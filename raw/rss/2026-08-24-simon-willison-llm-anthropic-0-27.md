---
source: farmer/rss
feed: simon-willison
farmed: 2026-08-25T14:24:43.464552+05:30
title: llm-anthropic 0.27
url: https://simonwillison.net/2026/Aug/24/llm-anthropic/
published: 2026-08-24
---

# llm-anthropic 0.27

<p><strong>Release:</strong> <a href="https://github.com/simonw/llm-anthropic/releases/tag/0.27">llm-anthropic 0.27</a></p>
        <p>This release of the Anthropic plugin for <a href="https://llm.datasette.io/">LLM</a> mainly provides compatibility with the recently released <a href="https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.0.0">anthropic v1.0.0</a> Python library, which switches from <code>httpx</code> to <a href="https://github.com/pydantic/httpx2">httpx2</a>. OpenAI made the same change in their <a href="https://github.com/openai/openai-python/releases/tag/v3.0.0">v3.0.0 release</a> two weeks ago.</p>
<p>Anthropic provide this <a href="https://github.com/anthropics/anthropic-sdk-python/blob/v1.0.0/MIGRATION.md">migration guide</a> for upgrading to 1.0, so I prompted Fable 5 in Claude Code with:</p>
<blockquote>
<p><code>Upgrade to anthropic&gt;=1 - read https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/refs/heads/main/MIGRATION.md and get the tests passing</code></p>
</blockquote>
<p>Here's <a href="https://github.com/simonw/llm-anthropic/pull/84">the resulting PR</a>.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/python">python</a>, <a href="https://simonwillison.net/tags/httpx">httpx</a>, <a href="https://simonwillison.net/tags/llm">llm</a>, <a href="https://simonwillison.net/tags/anthropic">anthropic</a>, <a href="https://simonwillison.net/tags/claude">claude</a></p>
