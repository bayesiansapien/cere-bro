---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-01T10:55:49.212223+00:00
title: "datasette-llm 0.1a9"
url: https://simonwillison.net/2026/Oct/31/datasette-llm/
published: 2026-10-31
author: 
---

# datasette-llm 0.1a9

<p><strong>Release:</strong> <a href="https://github.com/datasette/datasette-llm/releases/tag/0.1a9">datasette-llm 0.1a9</a></p>
        <p>I have some big upgrades to <a href="https://agent.datasette.io/">Datasette Agent</a> in the pipeline, but in the meantime here's a tiny user experience improvement to the underlying <code>datasette-llm</code> plugin. </p>
<p>It now picks up the default model used by <a href="https://llm.datasette.io/">LLM</a>, which means you can start using Datasette Agent without needing to explicitly configure a default model:</p>
<pre><code>uvx --with datasette-agent datasette content.db --internal internal.db
</code></pre>
<p>Previously you would also need to specify a model with <code>-s plugins.datasette-agent.default_model gpt-6-astra</code>.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/llm">llm</a>, <a href="https://simonwillison.net/tags/datasette-agent">datasette-agent</a></p>
