---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-15T03:32:14.759199+00:00
title: datasette-ip-rate-limit 0.1a0
url: https://simonwillison.net/2026/May/14/datasette-ip-rate-limit/#atom-everything
published: 2026-05-14
author: Simon Willison
---

# datasette-ip-rate-limit 0.1a0

<p><strong>Release:</strong> <a href="https://github.com/datasette/datasette-ip-rate-limit/releases/tag/0.1a0">datasette-ip-rate-limit 0.1a0</a></p>
        <p>The <a href="https://datasette.io/">datasette.io</a> site was being hammered by poorly-behaved crawlers, so I had Codex (GPT-5.5 xhigh) build a configurable rate limiting plugin to block IPs that were hammering specific areas of the site too quickly.</p>
<p>Here's <a href="https://github.com/simonw/datasette.io/blob/b6022bf9987661b94a26d3143028193a6cabfdcf/datasette.yml#L103-L116">the production configuration</a> I'm using on that site for the new plugin:</p>
<pre>  <span class="pl-ent">datasette-ip-rate-limit</span>:
    <span class="pl-ent">header</span>: <span class="pl-s">Fly-Client-IP</span>
    <span class="pl-ent">max_keys</span>: <span class="pl-c1">10000</span>
    <span class="pl-ent">exempt_paths</span>:
    - <span class="pl-s"><span class="pl-pds">"</span>/static/*<span class="pl-pds">"</span></span>
    - <span class="pl-s"><span class="pl-pds">"</span>/-/turnstile*<span class="pl-pds">"</span></span>
    <span class="pl-ent">rules</span>:
    - <span class="pl-ent">name</span>: <span class="pl-s">demo-databases</span>
      <span class="pl-ent">paths</span>:
      - <span class="pl-s"><span class="pl-pds">"</span>/global-power-plants/*<span class="pl-pds">"</span></span>
      - <span class="pl-s"><span class="pl-pds">"</span>/legislators/*<span class="pl-pds">"</span></span>
      <span class="pl-ent">window_seconds</span>: <span class="pl-c1">60</span>
      <span class="pl-ent">max_requests</span>: <span class="pl-c1">60</span>
      <span class="pl-ent">block_seconds</span>: <span class="pl-c1">20</span></pre>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/rate-limiting">rate-limiting</a>, <a href="https://simonwillison.net/tags/codex">codex</a></p>
