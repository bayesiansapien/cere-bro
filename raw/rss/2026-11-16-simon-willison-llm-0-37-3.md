---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-17T08:29:07.808283+00:00
title: "llm 0.37.3"
url: https://simonwillison.net/2026/Nov/16/llm/
published: 2026-11-16
author: 
---

# llm 0.37.3

<p><strong>Release:</strong> <a href="https://github.com/simonw/llm/releases/tag/0.37.3">llm 0.37.3</a></p>
        <p>A bug fix release for <a href="https://llm.datasette.io">LLM</a>, mainly to cover a problem with the most recent Homebrew package of the software.</p>
<p>Homebrew now ships the latest SQLite, <a href="https://www.sqlite.org/releaselog/3_54_1.html">3.54.1</a>, which includes <a href="https://sqlite.org/bugs/info/2026-10-12T13:52:22Z">a fix</a> that <a href="https://github.com/simonw/llm/issues/1879">broke LLM's logging code</a>.</p>
<p>Short version: in SQLite 3.54.0 the following SQL:</p>
<pre><code>select json_object('a', (select json_array(1)))
</code></pre>
<p>Returns this:</p>
<pre><code>{"a":[1]}
</code></pre>
<p>But in 3.54.1 the same query returns this:</p>
<pre><code>{"a":"[1]"}
</code></pre>
<p>According <a href="https://sqlite.org/forum/forumpost/dff1a343157e422f">to D. Richard Hipp</a>:</p>
<blockquote>
<p>That was a bug fix. Per the documentation, (SELECT json_array(...)) returns SQL text, not JSON. Hence the 3.54.1 behavior is correct and 3.54.0 was a bug.</p>
</blockquote>
<p>The workaround looks like this:</p>
<pre><code>select json_object('a', json((select json_array(1))))
</code></pre>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/llm">llm</a>, <a href="https://simonwillison.net/tags/webassembly">webassembly</a>, <a href="https://simonwillison.net/tags/sqlite">sqlite</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/d-richard-hipp">d-richard-hipp</a></p>
