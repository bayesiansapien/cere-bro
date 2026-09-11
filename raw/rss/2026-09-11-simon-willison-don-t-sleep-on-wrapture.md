---
source: farmer/rss
feed: simon-willison
farmed: 2026-09-11T16:28:34.506045+00:00
title: Don't sleep on wrapture
url: https://simonwillison.net/2026/Sep/11/wrapture/
published: 2026-09-11
---

# Don't sleep on wrapture

<p>Graham Dumpleton's new monkey patching package <a href="https://wrapture.readthedocs.io/">wrapture</a> is shaping up to be an indispensable tool for Python developers. I'm not sure why I've seen so little buzz about it!</p>
<p>Graham has been posting new tutorials for it almost daily since <a href="https://simonwillison.net/2026/Aug/31/introducing-wrapture/">the initial release</a> on August 31st. Here's everything he's published so far:</p>
<ul>
<li><a href="https://grahamdumpleton.me/posts/2026/08/introducing-wrapture/">Introducing wrapture</a> - a new monkey patching library that serves both testing and observability (think New Relic style tracing) at the same time.</li>
<li><a href="https://grahamdumpleton.me/posts/2026/09/unit-testing-with-wrapture/">Unit testing with wrapture</a> - how to use it for the same kinds of thing as <code>unittest.mock</code>.</li>
<li><a href="https://grahamdumpleton.me/posts/2026/09/recording-calls-with-wrapture/">Recording calls with wrapture</a>  - recording method calls as timelines and processing and displaying them as trees.</li>
<li><a href="https://grahamdumpleton.me/posts/2026/09/phased-behaviour-in-wrapture/">Phased behaviour in wrapture</a>  - arranging patched methods to change behavior across multiple calls.</li>
<li><a href="https://grahamdumpleton.me/posts/2026/09/beyond-callables-in-wrapture/">Beyond callables in wrapture</a> - monkey patching attributes, dictionaries, generators.</li>
<li><a href="https://grahamdumpleton.me/posts/2026/09/live-tracing-with-wrapture/">Live tracing with wrapture</a>  - tracing a live application to see exactly how it works.</li>
<li><a href="https://grahamdumpleton.me/posts/2026/09/zero-code-tracing-with-wrapture/">Zero-code tracing with wrapture</a>  - configuring tracing in a separate TOML file without modifying Python code at all.</li>
<li><a href="https://grahamdumpleton.me/posts/2026/09/tracing-flask-with-wrapture/">Tracing Flask with wrapture</a>  - using the separate <a href="https://github.com/GrahamDumpleton/wrapture-instrumentation">wrapture-instrumenation</a> package to instrument a Flask application. That package also provides instrumentation for <code>aiohttp.client</code>, <code>aiohttp.web</code>, <code>django</code>, <code>fastapi</code>, <code>flask</code>, <code>grpc</code>, <code>http.client</code>, <code>httpx</code>, <code>jinja2</code>, <code>requests</code>, <code>sqlalchemy</code>, <code>sqlite3</code>, <code>starlette</code>, <code>urllib.request</code>, <code>urllib3</code>, <code>uvicorn</code>, <code>werkzeug.serving</code>, <code>wsgiref.simple_server</code>, <code>xmlrpc.client</code>, <code>xmlrpc.server</code>.</li>
<li><a href="https://grahamdumpleton.me/posts/2026/09/finding-slow-code-with-wrapture/">Finding slow code with wrapture</a> - wrapture's tools for recording timing information, both individually and aggregated across multiple calls.</li>
<li><a href="https://grahamdumpleton.me/posts/2026/09/opentelemetry-export-in-wrapture/">OpenTelemetry export in wrapture</a> - exporting traces to OpenTelemetry.</li>
</ul>
<p>Graham also has a <a href="https://github.com/GrahamDumpleton/wrapture-workshops">set of interactive workshops</a> for wrapture, implemented as JupyterLab notebooks.</p>
<p>Wrapture is still alpha software but it's already very usable - especially given you can configure and try it out with a TOML file without modifying any Python code at all.</p>
<p>This feels like one of those Swiss Army Knife packages that, once mastered, will provide value against all sorts of problems for years to come.</p>

    <p>Tags: <a href="https://simonwillison.net/tags/graham-dumpleton">graham-dumpleton</a>, <a href="https://simonwillison.net/tags/open-source">open-source</a>, <a href="https://simonwillison.net/tags/testing">testing</a>, <a href="https://simonwillison.net/tags/python">python</a>, <a href="https://simonwillison.net/tags/observability">observability</a>, <a href="https://simonwillison.net/tags/monkey-patching">monkey-patching</a></p>
