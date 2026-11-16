---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-16T07:05:39.234236+00:00
title: "datasette 1.0a43"
url: https://simonwillison.net/2026/Nov/15/datasette/
published: 2026-11-15
author: 
---

# datasette 1.0a43

<p><strong>Release:</strong> <a href="https://github.com/simonw/datasette/releases/tag/1.0a43">datasette 1.0a43</a></p>
        <p>I've been leaning hard into Claude Fable 5.2 to help knock things off the <a href="https://github.com/simonw/datasette/milestone/37">1.0 milestone</a>, which is now 53% complete.</p>
<p>The biggest 1.0 item in this release is <a href="https://docs.datasette.io/en/latest/plugin_hooks.html#plugin-register-output-renderer-streaming">streaming support for output renderers</a> - the built-in TSV and CSV export mechanisms now use this as well, and plugins can register themselves as capable of streaming every row in a table in one go via the new <a href="https://docs.datasette.io/en/latest/internals.html#internals-response-stream">Response.stream()</a> method.</p>
<p>There are a couple of security fixes, one of which I deemed <a href="https://github.com/simonw/datasette/security/advisories/GHSA-mw6v-83vp-7c4c">deserving of a GitHub advisory</a>: private stored queries could be exposed, granting access to the title and SQL of the query (but not allowing that query to be executed).</p>
<p>There are dozens of smaller improvements. The row page JSON representation <a href="https://docs.datasette.io/en/latest/json_api.html#json-api-row">finally has a design suitable for 1.0</a>. A new <code>&lt;datasette-copy-button&gt;</code> Web Component provides copy-schema in various places. JSON in columns on the row page can be pretty-printed. There's a new <a href="https://docs.datasette.io/en/latest/javascript_plugins.html#javascript-plugins-modal-confirm">DatasetteModal.confirm()</a> JavaScript utility method. Plus dozens of bug fixes, including contributions by <a href="https://github.com/PDGGK">Zihan Dai</a>, <a href="https://github.com/peterolkhov">Peter Olkhovets</a>, <a href="https://github.com/IlyaKhalafi">Ilya Khalafi</a>, and <a href="https://github.com/AnkitaAdvitot">Ankita Advitot</a>.</p>
<p>The feature I'm most excited about is a pretty tiny one: I've added CSS multi-page view transitions to Datasette! <a href="https://github.com/simonw/datasette/commit/7da8a85ea77786edef975a4066bbadfab0966a0c">Here's the commit</a> - key CSS is as follows:</p>
<div class="highlight highlight-source-css"><pre><span class="pl-c">/* Enable cross-document view transitions,</span>
<span class="pl-c">   for anyone without prefers-reduced-motion */</span>
<span class="pl-k">@media</span> <span class="pl-kos">(</span><span class="pl-c1">prefers-reduced-motion</span><span class="pl-kos">:</span> no-preference<span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">@view-transition</span> <span class="pl-kos">{</span>
        <span class="pl-c1">navigation</span><span class="pl-kos">:</span> auto<span class="pl-kos">;</span>
    <span class="pl-kos">}</span>
<span class="pl-kos">}</span>
<span class="pl-c">/* .facet-results should morph from old position to new */</span>
<span class="pl-ent">html</span><span class="pl-kos">:</span><span class="pl-c1">active-view-transition</span> <span class="pl-kos">.</span><span class="pl-c1">content</span> <span class="pl-c1">&gt;</span> <span class="pl-kos">.</span><span class="pl-c1">facet-results</span> <span class="pl-kos">{</span>
    <span class="pl-c1">view-transition-name</span><span class="pl-kos">:</span> facet-results<span class="pl-kos">;</span>
<span class="pl-kos">}</span>
<span class="pl-c">/* So should a .table-wrapper, provided it contains .rows-and-columns */</span>
<span class="pl-ent">html</span><span class="pl-kos">:</span><span class="pl-c1">active-view-transition</span> <span class="pl-kos">.</span><span class="pl-c1">table-wrapper</span><span class="pl-kos">:</span><span class="pl-c1">has</span><span class="pl-kos">(</span><span class="pl-c1">&gt;</span> <span class="pl-ent">table</span><span class="pl-kos">.</span><span class="pl-c1">rows-and-columns</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-c1">view-transition-name</span><span class="pl-kos">:</span> rows-table<span class="pl-kos">;</span>
<span class="pl-kos">}</span></pre></div>

<p>With that in place, navigations within Datasette - still staunchly a multi-page application - feel more like an SPA. This works on Safari and Chrome at the moment and I believe supports for Firefox is due to land in <a href="https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/162#changes_for_web_developers">Firefox 162</a> on December 8th 2026 (seeing as they are no longer feature-flagged in Firefox Nightly.)</p>
<video controls="controls" height="720" poster="https://static.simonwillison.net/static/cors-allow/2026/css-transitions-datasette.webp" preload="none" width="930">
  <source src="https://static.simonwillison.net/static/cors-allow/2026/css-transitions-datasette.mp4" type="video/mp4" />
</video>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/security">security</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/css">css</a>, <a href="https://simonwillison.net/tags/browsers">browsers</a>, <a href="https://simonwillison.net/tags/annotated-release-notes">annotated-release-notes</a>, <a href="https://simonwillison.net/tags/firefox">firefox</a>, <a href="https://simonwillison.net/tags/javascript">javascript</a>, <a href="https://simonwillison.net/tags/safari">safari</a>, <a href="https://simonwillison.net/tags/chrome">chrome</a></p>
