---
source: farmer/rss
feed: simon-willison
farmed: 2026-04-17T07:36:43.505217+00:00
title: datasette 1.0a28
url: https://simonwillison.net/2026/Apr/17/datasette/#atom-everything
published: 2026-04-17
author: 
---

# datasette 1.0a28

<p><strong>Release:</strong> <a href="https://github.com/simonw/datasette/releases/tag/1.0a28">datasette 1.0a28</a></p>
    <p>I was upgrading Datasette Cloud to <a href="https://simonwillison.net/2026/Apr/15/datasette/">1.0a27</a> and discovered a nasty collection of accidental breakages caused by changes in that alpha. This new alpha addresses those directly:</p>
<blockquote>
<ul>
<li>Fixed a compatibility bug introduced in 1.0a27 where <code>execute_write_fn()</code> callbacks with a parameter name other than <code>conn</code> were seeing errors. (<a href="https://github.com/simonw/datasette/issues/2691">#2691</a>)</li>
<li>The <a href="https://docs.datasette.io/en/latest/internals.html#database-close">database.close()</a> method now also shuts down the write connection for that database.</li>
<li>New <a href="https://docs.datasette.io/en/latest/internals.html#datasette-close">datasette.close()</a> method for closing down all databases and resources associated with a Datasette instance. This is called automatically when the server shuts down. (<a href="https://github.com/simonw/datasette/pull/2693">#2693</a>)</li>
<li>Datasette now includes a pytest plugin which automatically calls <code>datasette.close()</code> on temporary instances created in function-scoped fixtures and during tests. See <a href="https://docs.datasette.io/en/latest/testing_plugins.html#testing-plugins-autoclose">Automatic cleanup of Datasette instances</a> for details. This helps avoid running out of file descriptors in plugin test suites that were written before the <code>Database(is_temp_disk=True)</code> feature introduced in Datasette 1.0a27. (<a href="https://github.com/simonw/datasette/issues/2692">#2692</a>)</li>
</ul>
</blockquote>
<p>Most of the changes in this release were implemented using Claude Code and the newly released Claude Opus 4.7.</p>
    
        <p>Tags: <a href="https://simonwillison.net/tags/datasette">datasette</a></p>
