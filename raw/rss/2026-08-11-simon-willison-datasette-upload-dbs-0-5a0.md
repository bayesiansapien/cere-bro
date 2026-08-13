---
source: farmer/rss
feed: simon-willison
farmed: 2026-08-13T03:38:27.722273+00:00
title: datasette-upload-dbs 0.5a0
url: https://simonwillison.net/2026/Aug/11/datasette-upload-dbs/
published: 2026-08-11
---

# datasette-upload-dbs 0.5a0

<p><strong>Release:</strong> <a href="https://github.com/simonw/datasette-upload-dbs/releases/tag/0.5a0">datasette-upload-dbs 0.5a0</a></p>
        <p>This plugin has been around for a while - it lets users upload a brand new SQLite database to a hosted Datasette instance, at which point that database will start being served by that instance.</p>
<p>It can also be used to atomically swap a database with a more recent version. The uploaded database is saved to a file, verified, then swapped in so <code>/name</code> starts serving the new one.</p>
<p>The new release adds a formalized API, so you can replace an existing database (or add a new one) like this:</p>
<pre><code>curl -X POST \
  -H "Authorization: Bearer $API_TOKEN" \
  -H "Accept: application/json" \
  -F "db=@content.db" \
  -F "db_name=content" \
  https://your-instance.example.com/-/upload-dbs
</code></pre>
<p>This means you can build fresh databases in an environment such as GitHub Actions and swap them in production as soon as that build has completed.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/datasette">datasette</a></p>
