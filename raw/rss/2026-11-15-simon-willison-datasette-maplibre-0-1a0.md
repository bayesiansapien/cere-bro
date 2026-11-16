---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-16T07:05:39.234236+00:00
title: "datasette-maplibre 0.1a0"
url: https://simonwillison.net/2026/Nov/15/datasette-maplibre/
published: 2026-11-15
author: 
---

# datasette-maplibre 0.1a0

<p><strong>Release:</strong> <a href="https://github.com/datasette/datasette-maplibre/releases/tag/0.1a0">datasette-maplibre 0.1a0</a></p>
        <p>The first new Datasette geospatial plugin in quite a while! This one combines the excellent <a href="https://maplibre.org/maplibre-gl-js/docs/">MapLibre GL</a> library with <a href="https://openfreemap.org">OpenFreeMap</a>, the free vector map server operated by Zsolt Ero (you should <a href="https://github.com/sponsors/hyperknot">sponsor Zsolt on GitHub</a>.)</p>
<p>I built most of this with a single prompt to Claude Fable 5.2:</p>
<blockquote>
<p><code>Look at datasette-cluster-map and datasette-leaflet-geojson plugins, then look at ~/dev/tools/openfreemap-demo.html - then build a brand new Datasette plugin that uses maplibreGL and openfreemap and combines the features of those other two plugins - but be creative and think outside the box for other useful features the plugin might have</code></p>
</blockquote>
<p>"Be creative and think outside the box" resulted in a few neat ideas - my favorite is that it displays SVG previews of GeoJSON shapes, then loads a WebGL preview only when they scroll into view.</p>
<p>I also had Claude build a comprehensive demo which works in the latest Datasette Lite, so you can <a href="https://lite.datasette.io/?install=datasette-maplibre&amp;url=https://gist.githubusercontent.com/simonw/39fa5d399465766039549912e2b3d291/raw/f6dfba99a75cbb8b5d9386223220eb52272767ee/demo.db&amp;metadata=https://gist.githubusercontent.com/simonw/39fa5d399465766039549912e2b3d291/raw/f6dfba99a75cbb8b5d9386223220eb52272767ee/metadata.yml">visit this link</a> to load the plugin and a demo database in your browser via Pyodide and WebAssembly.</p>
<p>I like <a href="https://lite.datasette.io/?install=datasette-maplibre&amp;url=https://gist.githubusercontent.com/simonw/39fa5d399465766039549912e2b3d291/raw/f6dfba99a75cbb8b5d9386223220eb52272767ee/demo.db&amp;metadata=https://gist.githubusercontent.com/simonw/39fa5d399465766039549912e2b3d291/raw/f6dfba99a75cbb8b5d9386223220eb52272767ee/metadata.yml#/demo/capitals_and_countries%23map=0/4.2/180&amp;color=continent">this demo page</a> showing both GeoJSON shapes and lat/lon points on the same map:</p>
<p><img alt="Screenshot of a web map interface. Toolbar: &quot;View&quot; set to &quot;Clusters&quot;, &quot;Colour by&quot; set to &quot;continent&quot;, plus &quot;Filter to this area&quot; and &quot;Download GeoJSON&quot; buttons. A world map shows countries outlined and shaded by continent, with coloured dots and numbered cluster circles. A popup for a point in South America reads: capital Caracas, country Venezuela, continent South America, capital_population 2985000, latitude 10.502944, longitude -66.918983. Legend: Africa (52), Asia (45), Europe (39), North America (16), South America (13), Oceania (6). Text: &quot;All 171 rows are on the map&quot;. Below, a table with columns country, continent, capital_population, latitude, longitude, boundary. First row: Afghanistan, Asia, 3277000, 34.518636, 69.181314, with a small map in the boundary column showing Afghanistan outlined and shaded in blue." src="https://static.simonwillison.net/static/cors-allow/2026/datasette-maplibre.webp" /></p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/visualization">visualization</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/datasette-lite">datasette-lite</a>, <a href="https://simonwillison.net/tags/claude-mythos-fable">claude-mythos-fable</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/geospatial">geospatial</a>, <a href="https://simonwillison.net/tags/openstreetmap">openstreetmap</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a></p>
