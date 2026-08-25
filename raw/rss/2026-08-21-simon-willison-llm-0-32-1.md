---
source: farmer/rss
feed: simon-willison
farmed: 2026-08-25T14:24:43.464937+05:30
title: llm 0.32.1
url: https://simonwillison.net/2026/Aug/21/llm/
published: 2026-08-21
---

# llm 0.32.1

<p><strong>Release:</strong> <a href="https://github.com/simonw/llm/releases/tag/0.32.1">llm 0.32.1</a></p>
        <p>Fresh installs of LLM stopped working the other day because the OpenAI Python library dropped its usage of <code>httpx</code>, and it turned out LLM depended on that library but only installed it via a transitive <code>openai</code> dependency.</p>
<p>This dot-release fixes that for the moment by pinning to <code>openai&lt;3</code>, and a soon-to-drop 0.33 release will switch from <code>httpx</code> to <a href="https://github.com/pydantic/httpx2">httpx2</a>.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/httpx">httpx</a>, <a href="https://simonwillison.net/tags/openai">openai</a>, <a href="https://simonwillison.net/tags/llm">llm</a></p>
