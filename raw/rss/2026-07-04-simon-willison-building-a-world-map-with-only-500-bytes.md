---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-08T05:20:41Z
title: Building a World Map with only 500 bytes
url: https://simonwillison.net/2026/Jul/4/building-a-world-map-with-only-500-bytes/#atom-everything
published: 2026-07-04
author: 
---

# Building a World Map with only 500 bytes

<p><strong><a href="https://www.experimentlog.com/blog/building-a-world-map-with-only-500-bytes">Building a World Map with only 500 bytes</a></strong></p>
Iwo Kadziela (assisted by Codex) figured out a way to generate a credible ASCII world map using 445 bytes of data:</p>
<p><img alt="A map of the world rendered as black asterisk ASCII characters, it looks very good" src="https://static.simonwillison.net/static/2026/world-map-ascii.png" /></p>
<p>The key trick is to use deflate compression, which is then wired together using this neat snippet of JavaScript. I didn't know you could use <code>fetch()</code> with <code>data:</code> URIs like this:</p>
<pre><code>fetch('data:;base64,1ZpLsgIxCEXnrM...==').then(
  r =&gt; r.body.pipeThrough(new DecompressionStream('deflate-raw'))
).then(
  s =&gt; new Response(s).text()
).then(
  t =&gt; b.innerHTML = '&lt;pre style=font-size:.65vw&gt;' + t
)
</code></pre>

    <p><small></small>Via <a href="https://news.ycombinator.com/item?id=48747762">Hacker News</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/ascii-art">ascii-art</a>, <a href="https://simonwillison.net/tags/data-urls">data-urls</a>, <a href="https://simonwillison.net/tags/javascript">javascript</a></p>
