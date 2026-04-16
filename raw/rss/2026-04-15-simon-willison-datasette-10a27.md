---
source: farmer/rss
feed: simon-willison
farmed: 2026-04-16T05:26:21Z
title: "datasette 1.0a27"
url: https://simonwillison.net/2026/Apr/15/datasette/#atom-everything
published: 2026-04-15
author: 
---

# datasette 1.0a27

**Source:** [simon-willison](https://simonwillison.net/2026/Apr/15/datasette/#atom-everything)
**Published:** 2026-04-15

<p><strong>Release:</strong> <a href="https://github.com/simonw/datasette/releases/tag/1.0a27">datasette 1.0a27</a></p>
    <p>Two major changes in this new Datasette alpha. I covered the first of those <a href="https://simonwillison.net/2026/Apr/14/replace-token-based-csrf/">in detail yesterday</a> - Datasette no longer uses Django-style CSRF form tokens, instead using modern browser headers <a href="https://words.filippo.io/csrf">as described by Filippo Valsorda</a>.</p>
<p>The second big change is that Datasette now fires a new <a href="https://docs.datasette.io/en/latest/events.html#datasette.events.RenameTableEvent">RenameTableEvent</a> any time a table is renamed during a SQLite transaction. This is useful because some plugins (like <a href="https://github.com/datasette/datasette-comments">datasette-comments</a>) attach additional data to table records by name, so a renamed table requires them to react in appropriate ways.</p>
<p>Here are the rest of the changes in the alpha:</p>
<blockquote>
<ul>
<li>New <a href="https://docs.datasette.io/en/latest/internals.html#internals-datasette-client-actor">actor= parameter</a> for <code>datasette.client</code> methods, allowing internal requests to be made as a specific actor. This is particularly useful for writing automated tests. (<a href="https://github.com/simonw/datasette/pull/2688">#2688</a>)</li>
<li>New <code>Database(is_temp_disk=True)</code> option, used internally for the internal database. This helps resolve intermittent database locked errors caused by the internal database being in-memory as opposed to on-disk. (<a href="https://github.com/simonw/datasette/issues/2683">#2683</a>) (<a href="https://github.com/simonw/datasette/pull/2684">#2684</a>)</li>
<li>The <code>/&lt;database&gt;/&lt;table&gt;/-/upsert</code> API (<a href="https://docs.datasette.io/en/latest/json_api.html#tableupsertview">docs</a>) now rejects rows with <code>null</code> primary key values. (<a href="https://github.com/simonw/datasette/issues/1936">#1936</a>)</li>
<li>Improved example in the API explorer for the <code>/-/upsert</code> endpoint (<a href="https://docs.datasette.io/en/latest/json_api.html#tableupsertview">docs</a>). (<a href="https://github.com/simonw/datasette/issues/1936">#1936</a>)</li>
<li>The <code>/&lt;database&gt;.json</code> endpoint now includes an <code>"ok": true</code> key, for consistency with other JSON API responses.</li>
<li><a href="https://docs.datasette.io/en/latest/internals.html#internals-utils-call-with-supported-arguments">call_with_supported_arguments()</a> is now documented as a supported public API. (<a href="https://github.com/simonw/datasette/pull/2678">#2678</a>)</li>
</ul>
</blockquote>
    
        <p>Tags: <a href="https://simonwillison.net/tags/annotated-release-notes">annotated-release-notes</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/python">python</a></p>
