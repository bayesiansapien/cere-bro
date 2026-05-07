---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-07T06:40:11.401007+00:00
title: datasette-referrer-policy 0.1
url: https://simonwillison.net/2026/May/5/datasette-referrer-policy/#atom-everything
published: 2026-05-05
author: 
---

# datasette-referrer-policy 0.1

<p><strong>Release:</strong> <a href="https://github.com/datasette/datasette-referrer-policy/releases/tag/0.1">datasette-referrer-policy 0.1</a></p>
        <p>The OpenStreetMap tiles on the Datasette <a href="https://datasette.io/global-power-plants/global-power-plants">global-power-plants demo</a> weren't displaying correctly. This turned out to be caused by two bugs.</p>
<p>The first is that the CAPTCHA <a href="https://github.com/simonw/datasette-turnstile">I added</a> to that site a few weeks ago was triggering for the <code>.json</code> fetch requests used by the map plugin, and since those weren't HTML the user was not being asked to solve them. Here's <a href="https://github.com/simonw/datasette.io/commit/23a1c8596b75b2094db46035a3b4280109fb3df3">the fix</a>.</p>
<p>The second was that OpenStreetMap quite reasonably <a href="https://wiki.openstreetmap.org/wiki/Referer">block tile requests</a> from sites that use a <code>Referrer-Policy: no-referrer</code> header.</p>
<p>Datasette does this by default, and I didn't want to change that default on people without warning - so I had Codex + GPT-5.5 <a href="https://gisthost.github.io/?402f2f23ee3dbfa251bf0d216e0224f7">build me</a> a new plugin to help set that header to another value.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/openstreetmap">openstreetmap</a>, <a href="https://simonwillison.net/tags/http">http</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a></p>
