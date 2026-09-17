---
source: farmer/rss
feed: simon-willison
farmed: 2026-09-17T05:26:41.862837+00:00
title: datasette 1.0a40
url: https://simonwillison.net/2026/Sep/16/datasette/
published: 2026-09-16
---

# datasette 1.0a40

<p><strong>Release:</strong> <a href="https://github.com/simonw/datasette/releases/tag/1.0a40">datasette 1.0a40</a></p>
        <p>Same security fix as <a href="https://simonwillison.net/2026/Sep/16/datasette-2/">0.65.5</a>, plus some neat new features and bug fixes:</p>
<ul>
<li>Plugins can now launch and manage <strong>background tasks</strong> using the new <a href="https://docs.datasette.io/en/latest/internals.html#datasette-add-background-task">datasette.add_background_task()</a> method. Thanks, <a href="https://alexgarcia.xyz/">Alex Garcia</a>.</li>
<li>I've migrated Datasette to <a href="https://github.com/pydantic/httpx2">httpx2</a> for features like the internal <code>datasette.client.get()</code> method.</li>
<li>A whole lot of <a href="https://docs.datasette.io/en/latest/changelog.html#a40-2026-09-16">bug fixes</a>, many of them stemming from a recent effort to triage issues for a 1.0 stable release.</li>
</ul>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/security">security</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a></p>
