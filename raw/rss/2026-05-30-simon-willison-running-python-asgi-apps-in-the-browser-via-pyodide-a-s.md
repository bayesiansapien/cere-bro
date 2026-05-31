---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-31T09:24:57.586193+00:00
title: Running Python ASGI apps in the browser via Pyodide + a service worker
url: https://simonwillison.net/2026/May/30/pyodide-asgi-browser/#atom-everything
published: 2026-05-30
author: Simon Willison
---

# Running Python ASGI apps in the browser via Pyodide + a service worker

<p><strong>Research:</strong> <a href="https://github.com/simonw/research/tree/main/pyodide-asgi-browser#readme">Running Python ASGI apps in the browser via Pyodide + a service worker</a></p>
        <p><a href="https://lite.datasette.io/">Datasette Lite</a> is my version of Datasette that runs entirely in the browser using Pyodide in WebAssembly.</p>
<p>When I first built it <a href="https://simonwillison.net/2022/May/4/datasette-lite/">four years ago</a> I used Web Workers and code that intercepts navigation operations and fetches the generated HTML by running the Python app.</p>
<p>This worked, but had the disadvantage that any JavaScript in <code>&lt;script&gt;</code> tags would not be executed - breaking some Datasette functionality and a whole lot of Datasette plugins.</p>
<p>This morning I <a href="https://github.com/simonw/research/pull/112">set Claude Opus 4.8 the task</a> (in Claude Code for web) of figuring out how to run Python ASGI apps in Pyodide using Service Workers instead, and it seems to work! Here's a <a href="https://simonw.github.io/research/pyodide-asgi-browser/">basic ASGI FastCGI demo</a> and here's <a href="https://simonw.github.io/research/pyodide-asgi-browser/datasette.html">a demo that runs Datasette 1.0a31</a>.</p>
<p>I'm still getting my head around exactly how it works, but once I've done that I plan to upgrade Datasette Lite itself.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/javascript">javascript</a>, <a href="https://simonwillison.net/tags/python">python</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/asgi">asgi</a>, <a href="https://simonwillison.net/tags/service-workers">service-workers</a>, <a href="https://simonwillison.net/tags/pyodide">pyodide</a>, <a href="https://simonwillison.net/tags/datasette-lite">datasette-lite</a>, <a href="https://simonwillison.net/tags/claude-code">claude-code</a></p>
