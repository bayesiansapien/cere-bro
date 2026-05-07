---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-07T06:40:11.401321+00:00
title: llm-echo 0.5a0
url: https://simonwillison.net/2026/May/5/llm-echo/#atom-everything
published: 2026-05-05
author: 
---

# llm-echo 0.5a0

<p><strong>Release:</strong> <a href="https://github.com/simonw/llm-echo/releases/tag/0.5a0">llm-echo 0.5a0</a></p>
        <blockquote>
<ul>
<li>New <code>-o thinking 1</code> option to help test against <a href="https://llm.datasette.io/en/latest/changelog.html#a0-2026-04-28">LLM 0.32a0</a> and higher.</li>
</ul>
</blockquote>
<p>This plugin provides a fake model called "echo" for LLM which doesn't run an LLM at all - it's useful for writing automated tests. You can now do this:</p>
<pre><code>uvx --with llm==0.32a1 --with llm-echo==0.5a0 llm -m echo hi -o thinking 1
</code></pre>
<p>This will fake a reasoning block to standard error before returning JSON echoing the prompt.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/llm">llm</a></p>
