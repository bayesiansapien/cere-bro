---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-18T03:44:44.080694+00:00
title: datasette-llm-limits 0.1a0
url: https://simonwillison.net/2026/May/15/datasette-llm-limits/#atom-everything
published: 2026-05-15
author: 
---

# datasette-llm-limits 0.1a0

<p><strong>Release:</strong> <a href="https://github.com/datasette/datasette-llm-limits/releases/tag/0.1a0">datasette-llm-limits 0.1a0</a></p>
        <p>This plugin works in conjunction with <a href="https://github.com/datasette/datasette-llm">datasette-llm</a> and <a href="https://github.com/datasette/datasette-llm-accountant">datasette-llm-accountant</a> to let you configure a per-user (or global) spending limit for LLM usage inside of Datasette. Configuration looks something like this:</p>
<pre><span class="pl-ent">plugins</span>:
  <span class="pl-ent">datasette-llm-limits</span>:
    <span class="pl-ent">limits</span>:
      <span class="pl-ent">per-user-daily</span>:
        <span class="pl-ent">scope</span>: <span class="pl-s">actor</span>
        <span class="pl-ent">window</span>: <span class="pl-s">rolling-24h</span>
        <span class="pl-ent">amount_usd</span>: <span class="pl-c1">1.00</span>
</pre>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/llm">llm</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a></p>
