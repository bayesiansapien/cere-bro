---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-14T03:50:13.323084+00:00
title: datasette 1.0a29
url: https://simonwillison.net/2026/May/12/datasette/#atom-everything
published: 2026-05-12
author: 
---

# datasette 1.0a29

<p><strong>Release:</strong> <a href="https://github.com/simonw/datasette/releases/tag/1.0a29">datasette 1.0a29</a></p>
        <blockquote>
<ul>
<li>New <code>TokenRestrictions.abbreviated(datasette)</code> <a href="https://docs.datasette.io/en/latest/internals.html#tokenrestrictions">utility method</a> for creating <code>"_r"</code> dictionaries. <a href="https://github.com/simonw/datasette/issues/2695">#2695</a></li>
<li>Table headers and column options are now visible even if a table contains zero rows. <a href="https://github.com/simonw/datasette/issues/2701">#2701</a></li>
<li>Fixed bug with display of column actions dialog on Mobile Safari. <a href="https://github.com/simonw/datasette/issues/2708">#2708</a></li>
<li>Fixed bug where tests could crash with a segfault due to a race condition between <code>Datasette.close()</code> and <code>Database.close()</code>. <a href="https://github.com/simonw/datasette/issues/2709">#2709</a></li>
</ul>
</blockquote>
<p>That segfault bug was <em>gnarly</em>. I added a mechanism to Datasette recently that would automatically close connections at the end of each test, but it turned out that introduced a race condition where an in-flight query could sometimes be executing in a thread against a connection while it was being closed. I ended up solving that by having Codex CLI (with GPT-5.5 xhigh) create <a href="https://github.com/simonw/datasette/issues/2709#issuecomment-4435604727">a minimal Dockerfile</a> that recreated the bug.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/projects">projects</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a></p>
