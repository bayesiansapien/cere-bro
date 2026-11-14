---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-14T05:10:40.494064+00:00
title: "datasette-leaflet 0.3"
url: https://simonwillison.net/2026/Nov/13/datasette-leaflet/
published: 2026-11-13
author: 
---

# datasette-leaflet 0.3

<p><strong>Release:</strong> <a href="https://github.com/simonw/datasette-leaflet/releases/tag/0.3">datasette-leaflet 0.3</a></p>
        <p>OpenStreetMap have a very reasonable policy that hits to their hosted tile server <a href="https://wiki.openstreetmap.org/wiki/Referer">should send a referrer header</a>. Datasette table pages used the <code>Referrer-Policy: no-referrer</code> HTTP header, causing plugins that loaded tiles from OpenStreetMap to violate that policy.</p>
<p><code>datasette-leaflet</code> is the plugin that loads a bundled Leaflet so other Datasette plugins can depend on it. It now sets the referrer policy on the tile requests themselves to <code>strict-origin-when-cross-origin</code>, passing the host but not the full path to the page.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/leaflet">leaflet</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/openstreetmap">openstreetmap</a></p>
