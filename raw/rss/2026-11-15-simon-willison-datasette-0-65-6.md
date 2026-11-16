---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-16T07:05:39.234236+00:00
title: "datasette 0.65.6"
url: https://simonwillison.net/2026/Nov/15/datasette-2/
published: 2026-11-15
author: 
---

# datasette 0.65.6

<p><strong>Release:</strong> <a href="https://github.com/simonw/datasette/releases/tag/0.65.6">datasette 0.65.6</a></p>
        <p>I backported a minor security fix from 1.0a43:</p>
<blockquote>
<p>Fixed a security issue where a database registered using <code>add_database(db, name=..., route=...)</code> with a route that differs from its name could be downloaded from <code>/&lt;route&gt;.db</code> by actors who were denied access to it. [...]</p>
</blockquote>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/security">security</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a></p>
