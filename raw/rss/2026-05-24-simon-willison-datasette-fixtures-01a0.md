---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-25T08:23:54.617769+00:00
title: datasette-fixtures 0.1a0
url: https://simonwillison.net/2026/May/24/datasette-fixtures/#atom-everything
published: 2026-05-24
---

# datasette-fixtures 0.1a0

<p><strong>Release:</strong> <a href="https://github.com/datasette/datasette-fixtures/releases/tag/0.1a0">datasette-fixtures 0.1a0</a></p>
        <p>One of the smaller features in <a href="https://docs.datasette.io/en/latest/changelog.html#a30-2026-05-24">Datasette 1.0a30</a> is this:</p>
<blockquote>
<p>New documented <a href="https://docs.datasette.io/en/latest/testing_plugins.html#datasette-fixtures-populate-fixture-database">datasette.fixtures.populate_fixture_database(conn)</a> helper for creating the fixture database tables used by Datasette's own tests, intended for plugin test suites.</p>
</blockquote>
<p>This new plugin takes advantage of that API. You can try it out using <code>uvx</code> without even installing Datasette like this:</p>
<pre>uvx --prerelease=allow \
  --with datasette-fixtures datasette \
  --get /fixtures/roadside_attractions.json</pre>
<p>Which outputs:</p>
<pre>{
  <span class="pl-ent">"ok"</span>: <span class="pl-c1">true</span>,
  <span class="pl-ent">"next"</span>: <span class="pl-c1">null</span>,
  <span class="pl-ent">"rows"</span>: [
    {<span class="pl-ent">"pk"</span>: <span class="pl-c1">1</span>, <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>The Mystery Spot<span class="pl-pds">"</span></span>, <span class="pl-ent">"address"</span>: <span class="pl-s"><span class="pl-pds">"</span>465 Mystery Spot Road, Santa Cruz, CA 95065<span class="pl-pds">"</span></span>, <span class="pl-ent">"url"</span>: <span class="pl-s"><span class="pl-pds">"</span>https://www.mysteryspot.com/<span class="pl-pds">"</span></span>, <span class="pl-ent">"latitude"</span>: <span class="pl-c1">37.0167</span>, <span class="pl-ent">"longitude"</span>: <span class="pl-c1">-122.0024</span>},
    {<span class="pl-ent">"pk"</span>: <span class="pl-c1">2</span>, <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Winchester Mystery House<span class="pl-pds">"</span></span>, <span class="pl-ent">"address"</span>: <span class="pl-s"><span class="pl-pds">"</span>525 South Winchester Boulevard, San Jose, CA 95128<span class="pl-pds">"</span></span>, <span class="pl-ent">"url"</span>: <span class="pl-s"><span class="pl-pds">"</span>https://winchestermysteryhouse.com/<span class="pl-pds">"</span></span>, <span class="pl-ent">"latitude"</span>: <span class="pl-c1">37.3184</span>, <span class="pl-ent">"longitude"</span>: <span class="pl-c1">-121.9511</span>},
    {<span class="pl-ent">"pk"</span>: <span class="pl-c1">3</span>, <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Burlingame Museum of PEZ Memorabilia<span class="pl-pds">"</span></span>, <span class="pl-ent">"address"</span>: <span class="pl-s"><span class="pl-pds">"</span>214 California Drive, Burlingame, CA 94010<span class="pl-pds">"</span></span>, <span class="pl-ent">"url"</span>: <span class="pl-c1">null</span>, <span class="pl-ent">"latitude"</span>: <span class="pl-c1">37.5793</span>, <span class="pl-ent">"longitude"</span>: <span class="pl-c1">-122.3442</span>},
    {<span class="pl-ent">"pk"</span>: <span class="pl-c1">4</span>, <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Bigfoot Discovery Museum<span class="pl-pds">"</span></span>, <span class="pl-ent">"address"</span>: <span class="pl-s"><span class="pl-pds">"</span>5497 Highway 9, Felton, CA 95018<span class="pl-pds">"</span></span>, <span class="pl-ent">"url"</span>: <span class="pl-s"><span class="pl-pds">"</span>https://www.bigfootdiscoveryproject.com/<span class="pl-pds">"</span></span>, <span class="pl-ent">"latitude"</span>: <span class="pl-c1">37.0414</span>, <span class="pl-ent">"longitude"</span>: <span class="pl-c1">-122.0725</span>}
  ],
  <span class="pl-ent">"truncated"</span>: <span class="pl-c1">false</span>
}</pre>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/uv">uv</a></p>