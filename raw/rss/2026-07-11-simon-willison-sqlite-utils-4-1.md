---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-19T22:17:42.123020+00:00
title: sqlite-utils 4.1
url: https://simonwillison.net/2026/Jul/11/sqlite-utils/#atom-everything
published: 2026-07-11
---

# sqlite-utils 4.1

<p><strong>Release:</strong> <a href="https://github.com/simonw/sqlite-utils/releases/tag/4.1">sqlite-utils 4.1</a></p>
        <p>The first dot-release since <a href="https://simonwillison.net/2026/Jul/7/sqlite-utils-4/">4.0 a few days ago</a>, introducing a number of minor new features.</p>
<blockquote>
<ul>
<li><code>sqlite-utils insert</code> and <code>sqlite-utils upsert</code> now accept a <code>--code</code> option for <a href="https://sqlite-utils.datasette.io/en/stable/cli.html#cli-insert-code">providing a block of Python code</a> (or a path to a <code>.py</code> file) that defines a <code>rows()</code> function or <code>rows</code> iterable of rows to insert, as an alternative to importing from a file. (<a href="https://github.com/simonw/sqlite-utils/issues/684">#684</a>)</li>
</ul>
</blockquote>
<p><code>sqlite-utils</code> already had features that allow you to pass blocks of Python code as CLI arguments, for example <a href="https://sqlite-utils.datasette.io/en/stable/cli.html#converting-data-in-columns">this one</a> for the <code>sqlite-utils convert</code> command:</p>
<pre><span class="pl-s1">sqlite</span><span class="pl-c1">-</span><span class="pl-s1">utils</span> <span class="pl-s1">convert</span> <span class="pl-s1">content</span>.<span class="pl-c1">db</span> <span class="pl-s1">articles</span> <span class="pl-s1">headline</span> '
<span class="pl-s1">def</span> <span class="pl-en">convert</span>(<span class="pl-s1">value</span>):
    <span class="pl-k">return</span> <span class="pl-s1">value</span>.<span class="pl-c1">upper</span>()'</pre>
<p>Allowing blocks of code to <a href="https://sqlite-utils.datasette.io/en/stable/cli.html#inserting-rows-generated-by-python-code">generate new rows directly</a> was on obvious extension of that pattern:</p>
<pre><span class="pl-s1">sqlite</span><span class="pl-c1">-</span><span class="pl-s1">utils</span> <span class="pl-s1">insert</span> <span class="pl-s1">data</span>.<span class="pl-c1">db</span> <span class="pl-s1">creatures</span> <span class="pl-c1">-</span><span class="pl-c1">-</span><span class="pl-s1">code</span> '
<span class="pl-s1">def</span> <span class="pl-en">rows</span>():
    <span class="pl-k">yield</span> {<span class="pl-s">"id"</span>: <span class="pl-c1">1</span>, <span class="pl-s">"name"</span>: <span class="pl-s">"Cleo"</span>}
    <span class="pl-k">yield</span> {<span class="pl-s">"id"</span>: <span class="pl-c1">2</span>, <span class="pl-s">"name"</span>: <span class="pl-s">"Suna"</span>}
' <span class="pl-c1">-</span><span class="pl-c1">-</span><span class="pl-s1">pk</span> <span class="pl-s1">id</span></pre>

<blockquote>
<ul>
<li><code>sqlite-utils insert</code> and <code>sqlite-utils upsert</code> now accept <code>--type column-name type</code> to <a href="https://sqlite-utils.datasette.io/en/stable/cli.html#cli-insert-csv-tsv-column-types">override the type automatically chosen when the table is created</a>. This is useful for CSV or TSV columns such as ZIP codes that look like integers but should be stored as <code>TEXT</code> to preserve leading zeros. (<a href="https://github.com/simonw/sqlite-utils/issues/131">#131</a>)</li>
</ul>
</blockquote>
<p>A long-standing feature request which turned out to be a <a href="https://github.com/SAY-5/sqlite-utils/commit/d2ac3765ed9f0516bb0cbc2508a5c3907fb6a71a">simple implementation</a>.</p>
<blockquote>
<ul>
<li>New <code>table.drop_index(name)</code> method and <code>sqlite-utils drop-index</code> command for dropping an index by name. Both accept <code>ignore=True</code>/<code>--ignore</code> to ignore a missing index. (<a href="https://github.com/simonw/sqlite-utils/issues/626">#626</a>)</li>
<li><code>sqlite-utils query</code> can now read the SQL query from standard input by passing <code>-</code> in place of the query, for example <code>echo "select * from dogs" | sqlite-utils query dogs.db -</code>. (<a href="https://github.com/simonw/sqlite-utils/issues/765">#765</a>)</li>
</ul>
</blockquote>
<p>Two more small features. I had Codex review all open issues and highlight the easiest ones!</p>
<blockquote>
<ul>
<li><code>sqlite-utils upsert</code> can now infer the primary key of an existing table, so <code>--pk</code> can be omitted when upserting into a table that already has a primary key.</li>
</ul>
</blockquote>
<p>Another Codex suggestion, an obvious missing CLI feature from a Python library improvement that shipped in the 4.0 release.</p>
<blockquote>
<ul>
<li><code>table.transform()</code> and <code>table.transform_sql()</code> now accept <code>strict=True</code> or <code>strict=False</code> to change a table’s <a href="https://www.sqlite.org/stricttables.html">SQLite strict mode</a>. Omitting the option preserves the existing mode. (<a href="https://github.com/simonw/sqlite-utils/issues/787">#787</a>)</li>
<li>The <code>sqlite-utils transform</code> command now accepts <code>--strict</code> and <code>--no-strict</code> to change a table’s strict mode. (<a href="https://github.com/simonw/sqlite-utils/issues/787">#787</a>)</li>
</ul>
</blockquote>
<p>These two were inspired by <a href="https://evanhahn.com/prefer-strict-tables-in-sqlite/">Prefer STRICT tables in SQLite</a> by Evan Hahn, which did the rounds <a href="https://news.ycombinator.com/item?id=48873940">on Hacker News</a> today. Evan pointed out that:</p>
<blockquote>
<p>Unfortunately, I don’t think there’s a way to ALTER a table to make it strict. I think you have to copy the data out of the non-strict table into the strict one.</p>
</blockquote>
<p>That's exactly what the <a href="https://sqlite-utils.datasette.io/en/stable/python-api.html#transforming-a-table">sqlite-utils transform mechanism</a> does, so I extended it to add the ability to switch tables from strict to non-strict and vice-versa.</p>
<p>Here's <a href="https://gist.github.com/simonw/ab8256b81646ad967a601975e206de64">the GPT-5.6 Sol xhigh Codex transcript</a> I used to implement those new strict table features. One of the most useful prompts I ran was this one:</p>
<blockquote>
<p><code>use uv run python -c and manually exercise the new .transform(strict=) option, see if you can find any edge-cases or bugs</code></p>
</blockquote>
<p>Effectively telling the model to manually test its work, outside of the automated tests it had already written. This turned up two minor issues that we then fixed.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/projects">projects</a>, <a href="https://simonwillison.net/tags/python">python</a>, <a href="https://simonwillison.net/tags/sqlite">sqlite</a>, <a href="https://simonwillison.net/tags/sqlite-utils">sqlite-utils</a>, <a href="https://simonwillison.net/tags/annotated-release-notes">annotated-release-notes</a>, <a href="https://simonwillison.net/tags/ai-assisted-programming">ai-assisted-programming</a></p>
