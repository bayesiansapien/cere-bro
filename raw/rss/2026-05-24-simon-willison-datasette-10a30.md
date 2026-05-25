---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-25T08:23:54.617769+00:00
title: datasette 1.0a30
url: https://simonwillison.net/2026/May/24/datasette/#atom-everything
published: 2026-05-24
---

# datasette 1.0a30

<p><strong>Release:</strong> <a href="https://github.com/simonw/datasette/releases/tag/1.0a30">datasette 1.0a30</a></p>
        <p>The big new feature in this alpha is a new customizable "Jump to..." menu, described in detail in <a href="https://datasette.io/blog/2026/jump-menu/">The extensible "Jump to" menu in Datasette 1.0a30</a> on the Datasette blog. You can try it out by hitting <code>/</code> on <a href="https://latest.datasette.io/">latest.datasette.io</a> - it looks like this:</p>
<p><img alt="Animated demo - the Jump to menu appears, and as the user types it filters to specific databases and tables and debug options" src="https://static.simonwillison.net/static/2026/menu.gif" /></p>
<p>The new <a href="https://docs.datasette.io/en/latest/plugin_hooks.html#jump-items-sql-datasette-actor-request">jump_items_sql()</a> plugin hook allows plugins to add their own items to the set that's searched by the plugin.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/projects">projects</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/annotated-release-notes">annotated-release-notes</a></p>