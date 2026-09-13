---
source: farmer/rss
feed: simon-willison
farmed: 2026-09-13T07:27:09.178245+00:00
title: Generating running routes with GPT-6 Astra and ChatGPT Work
url: https://simonwillison.net/2026/Sep/12/astra-running-routes/
published: 2026-09-12
---

# Generating running routes with GPT-6 Astra and ChatGPT Work

<p>Here's a neat thing I had <a href="https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/">ChatGPT Work</a> with GPT-6 Astra (Max) do this morning:</p>
<blockquote>
<p><code>I live at &lt;my address&gt;. Figure out 5K and 10K running routes from me that loop from my house. Use OSM data.</code></p>
</blockquote>
<p>It worked for 27 minutes and produced exactly what I'd asked for, as both an embedded visualization and downloadable GPX file and GeoJSON files. Here's that 5K route:</p>
<p><img alt="Map screenshot showing a blue route line over a light grey street map. Text: El Granada harbor loop 5.1 km. N ↑ (top right). Street labels along the route: Carmel Avenue, Paloma Avenue, San Carlos Avenue, Avenue Granada, Capistrano Road, Francisco Street, Coastal Trail. The loop runs from the harbor at the bottom left, north along Avenue Granada and Paloma Avenue to a northern point near Carmel Avenue, then east along San Carlos Avenue and south down Francisco Street to the far right, before returning west along the Coastal Trail beside the coastline. Footer: Map data © OpenStreetMap contributors. Give feedback." src="https://static.simonwillison.net/static/2026/5k-route.webp" /></p>
<p>When I asked it how it had created the route, it replied:</p>
<blockquote>
<p>I used <strong>Nominatim to locate the address</strong> and <strong>Overpass to download local OpenStreetMap roads and trails</strong>, then calculated the loops locally.</p>
</blockquote>
<p>Frustratingly, the actual code it ran and exact details of what it did weren't visible to me in the ChatGPT UI. I see this lack of transparency is an anti-feature.</p>
<p>By the time I thought to ask for a copy of the Python code it had used, ChatGPT was unable to provide it. This appears to be because the thread had been compacted. I think any LLM system that uses compaction needs to both preserve the pre-compacted text and make that text available via agent tool calls, to protect against this kind of problem.</p>
<p>As for displaying the map to me, that used the <a href="https://codex-tool-reference.simonw.chatgpt.site/skills/visualize">visualize skill</a>. It created a file called <code>/workspace/el-granada-5k-share.html</code> to embed directly into the ChatGPT UI.</p>
<p>Here's <a href="https://gist.github.com/simonw/ea652573c8ff5378b218cb10c8c5a480">a copy of that HTML</a>, which starts like this:</p>
<div class="highlight highlight-text-html-basic"><pre><span class="pl-kos">&lt;</span><span class="pl-ent">div</span> <span class="pl-c1">id</span>="<span class="pl-s">eg-share-loop</span>"<span class="pl-kos">&gt;</span>
  <span class="pl-kos">&lt;</span><span class="pl-ent">div</span> <span class="pl-c1">class</span>="<span class="pl-s">viz-row</span>"<span class="pl-kos">&gt;</span><span class="pl-kos">&lt;</span><span class="pl-ent">h3</span><span class="pl-kos">&gt;</span>El Granada harbor loop<span class="pl-kos">&lt;/</span><span class="pl-ent">h3</span><span class="pl-kos">&gt;</span><span class="pl-kos">&lt;</span><span class="pl-ent">span</span> <span class="pl-c1">class</span>="<span class="pl-s">text-small</span>"<span class="pl-kos">&gt;</span>5.1 km<span class="pl-kos">&lt;/</span><span class="pl-ent">span</span><span class="pl-kos">&gt;</span><span class="pl-kos">&lt;/</span><span class="pl-ent">div</span><span class="pl-kos">&gt;</span>
  <span class="pl-kos">&lt;</span><span class="pl-ent">div</span> <span class="pl-c1">id</span>="<span class="pl-s">eg-share-stage</span>"<span class="pl-kos">&gt;</span><span class="pl-kos">&lt;/</span><span class="pl-ent">div</span><span class="pl-kos">&gt;</span>
  <span class="pl-kos">&lt;</span><span class="pl-ent">div</span> <span class="pl-c1">class</span>="<span class="pl-s">text-small text-muted</span>"<span class="pl-kos">&gt;</span>Map data © <span class="pl-kos">&lt;</span><span class="pl-ent">a</span> <span class="pl-c1">href</span>="<span class="pl-s">https://www.openstreetmap.org/copyright</span>" <span class="pl-c1">target</span>="<span class="pl-s">_blank</span>" <span class="pl-c1">rel</span>="<span class="pl-s">noopener</span>"<span class="pl-kos">&gt;</span>OpenStreetMap contributors<span class="pl-kos">&lt;/</span><span class="pl-ent">a</span><span class="pl-kos">&gt;</span><span class="pl-kos">&lt;/</span><span class="pl-ent">div</span><span class="pl-kos">&gt;</span>
  <span class="pl-kos">&lt;</span><span class="pl-ent">style</span><span class="pl-kos">&gt;</span>
    <span class="pl-kos">#</span><span class="pl-c1">eg-share-loop</span> { <span class="pl-c1">width</span><span class="pl-kos">:</span><span class="pl-c1">100<span class="pl-smi">%</span></span>; }
    <span class="pl-kos">#</span><span class="pl-c1">eg-share-loop</span> <span class="pl-kos">#</span><span class="pl-c1">eg-share-stage</span> { <span class="pl-c1">width</span><span class="pl-kos">:</span><span class="pl-c1">100<span class="pl-smi">%</span></span>; <span class="pl-c1">margin</span><span class="pl-kos">:</span><span class="pl-c1">8<span class="pl-smi">px</span></span> <span class="pl-c1">0</span>; }
    <span class="pl-kos">#</span><span class="pl-c1">eg-share-loop</span> .<span class="pl-c1">eg-share-map</span> { <span class="pl-c1">display</span><span class="pl-kos">:</span>block; <span class="pl-c1">width</span><span class="pl-kos">:</span><span class="pl-c1">100<span class="pl-smi">%</span></span>; <span class="pl-c1">touch-action</span><span class="pl-kos">:</span>none; }
    <span class="pl-kos">#</span><span class="pl-c1">eg-share-loop</span> .<span class="pl-c1">eg-share-map</span> <span class="pl-ent">text</span> { <span class="pl-c1">fill</span><span class="pl-kos">:</span><span class="pl-en">var</span>(<span class="pl-s1">--foreground</span>); <span class="pl-c1">font-size</span><span class="pl-kos">:</span><span class="pl-c1">12<span class="pl-smi">px</span></span>; <span class="pl-c1">font-weight</span><span class="pl-kos">:</span><span class="pl-c1">400</span>; }
    <span class="pl-kos">#</span><span class="pl-c1">eg-share-loop</span> .<span class="pl-c1">eg-share-label</span> { <span class="pl-c1">paint-order</span><span class="pl-kos">:</span>stroke; <span class="pl-c1">stroke</span><span class="pl-kos">:</span><span class="pl-en">var</span>(<span class="pl-s1">--background</span>); <span class="pl-c1">stroke-width</span><span class="pl-kos">:</span><span class="pl-c1">3<span class="pl-smi">px</span></span>; <span class="pl-c1">stroke-linejoin</span><span class="pl-kos">:</span>round; }
  <span class="pl-kos">&lt;/</span><span class="pl-ent">style</span><span class="pl-kos">&gt;</span>
  <span class="pl-kos">&lt;</span><span class="pl-ent">script</span> <span class="pl-c1">type</span>="<span class="pl-s">application/json</span>" <span class="pl-c1">id</span>="<span class="pl-s">eg-share-data</span>"<span class="pl-kos">&gt;</span><span class="pl-kos">{</span><span class="pl-s">"route"</span>:<span class="pl-kos">{</span><span class="pl-s">"type"</span>:<span class="pl-s">"LineString"</span><span class="pl-kos">,</span><span class="pl-s">"coordinates"</span>:<span class="pl-kos">[</span><span class="pl-kos">[</span><span class="pl-c1">-</span><span class="pl-c1">122.467425</span><span class="pl-kos">,</span><span class="pl-c1">37.4997753</span><span class="pl-kos">]</span> <span class="pl-kos">.</span><span class="pl-kos">.</span><span class="pl-kos">.</span><span class="pl-kos">&lt;/</span><span class="pl-ent">script</span><span class="pl-kos">&gt;</span>
  <span class="pl-kos">&lt;</span><span class="pl-ent">script</span> <span class="pl-c1">src</span>="<span class="pl-s">https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js</span>"<span class="pl-kos">&gt;</span><span class="pl-kos">&lt;/</span><span class="pl-ent">script</span><span class="pl-kos">&gt;</span>
  <span class="pl-kos">&lt;</span><span class="pl-ent">script</span><span class="pl-kos">&gt;</span>
  (() =&gt; {
    const root=document.getElementById('eg-share-loop');</pre></div>

<p>The <code>&lt;script type="application/json"&gt;</code> element contains the full geometry needed to render both the running route and the map itself, using D3, which is loaded from an allow-listed CDN location described in this section of <a href="https://codex-tool-reference.simonw.chatgpt.site/skills/visualize">the visualize skill</a>:</p>
<blockquote>
<h3 id="external-resources">External resources</h3>
<ul>
<li>The CSP allows only <code>cdnjs.cloudflare.com</code>, <code>esm.sh</code>, <code>cdn.jsdelivr.net</code>, <code>unpkg.com</code>, <code>fonts.googleapis.com</code>, <code>fonts.gstatic.com</code>, and <code>fonts.bunny.net</code>. Other origins are blocked and fail silently.</li>
</ul>
</blockquote>
    
        <p>Tags: <a href="https://simonwillison.net/tags/geospatial">geospatial</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/d3">d3</a>, <a href="https://simonwillison.net/tags/openai">openai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/chatgpt">chatgpt</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/skills">skills</a>, <a href="https://simonwillison.net/tags/gpt-6-astra">gpt-6-astra</a></p>
