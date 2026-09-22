---
source: farmer/rss
feed: simon-willison
farmed: 2026-09-22T07:29:05.680216+00:00
title: Cloudflare Python Workers are now generally available
url: https://simonwillison.net/2026/Sep/21/cloudflare-python-worker/
published: 2026-09-21
author: 
---

# Cloudflare Python Workers are now generally available


    
<p><strong><a href="https://blog.cloudflare.com/python-workers-ga/">Cloudflare Python Workers are now generally available</a></strong></p>
After a two year preview, Cloudflare's support for running Python code in their server-side Workers platform is now stable: "Python is now a first-class, fully supported language on the Cloudflare Developer Platform".</p>
<p>A neat thing about this is how it works. Cloudflare are running Python compiled to WebAssembly via Pyodide in their V8-based <a href="https://github.com/cloudflare/workerd">workerd</a> runtime.</p>
<p>This comes with some limitations, <a href="https://developers.cloudflare.com/workers/languages/python/stdlib/">documented here</a> - most notably both <code>multiprocessing</code> and <code>threading</code> are non-functional in the WebAssembly VM.</p>
<p>One particularly interesting detail of this is the local development environment story - their <a href="https://developers.cloudflare.com/workers/languages/python/#the-pywrangler-cli-tool">pywrangler</a> development tool (confusingly packaged as <a href="https://pypi.org/project/workers-py/">workers-py</a> on PyPI) runs a full local simulation of their stack, including executing code with Pyodide in WebAssembly in V8 in a 123MB <code>workerd</code> binary, which for me ended up in <code>node_modules/@cloudflare/workerd-darwin-arm64/bin/workerd</code>.</p>
<p>Python Workers represent a significant investment in the wider Python ecosystem by Cloudflare. The release announcement is credited to Gyeongjae Choi, Dominik Picheta, and Hood Chatham - Gyeongjae and Hood are both Pyodide core maintainers.

    <p><small></small>Via <a href="https://news.ycombinator.com/item?id=49787142">Hacker News</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/python">python</a>, <a href="https://simonwillison.net/tags/cloudflare">cloudflare</a>, <a href="https://simonwillison.net/tags/webassembly">webassembly</a>, <a href="https://simonwillison.net/tags/pyodide">pyodide</a></p>




