---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-14T05:10:40.494064+00:00
title: "datasette-cluster-map 0.19"
url: https://simonwillison.net/2026/Nov/13/datasette-cluster-map/
published: 2026-11-13
author: 
---

# datasette-cluster-map 0.19

<p><strong>Release:</strong> <a href="https://github.com/simonw/datasette-cluster-map/releases/tag/0.19">datasette-cluster-map 0.19</a></p>
        <p>One of the oldest Datasette plugins, and still one of my favorites. It now works with Datasette 1.0a42, and depends on <a href="https://simonwillison.net/2026/Nov/13/datasette-leaflet/">the new datasette-leaflet</a> to ensure OpenStreetMap tiles are requested with a referrer header.</p>
<p>Here's <a href="https://datasette.io/global-power-plants/global-power-plants?owner=Pacific+Gas+%26+Electric+Co.">a map of power plants owned by California's PG&amp;E</a>, also demonstrating Datasette's recently <a href="https://github.com/simonw/datasette/pull/3032">redesigned facets</a>:</p>
<p><img alt="Screenshot of a faceted map interface. Three facet panels at the top: &quot;country_long 1&quot; with United States of America 81 selected; &quot;owner 1&quot; with Pacific Gas &amp; Electric Co. 81 selected; &quot;primary_fuel 5&quot; listing Hydro 63, Solar 10, Gas 5, Storage 2, Nuclear 1. Each primary_fuel row has a pale blue horizontal bar behind its label, sized in proportion to its count: Hydro's bar fills most of the row width, Solar's is a short sliver, Gas's is shorter still, and Storage and Nuclear have only a thin strip at the left edge. Below is a Leaflet map with + and − zoom controls showing California and Nevada, with marker clusters across northern and central California: 9 near Redding, 21 near Chico, 2 to the west of Chico, 13 northeast of Sacramento, 7 east of Stockton, 6 at Oakland, 10 at Fresno, 9 west of Visalia, 2 north of Bakersfield, plus two individual blue pin markers on the coast, one in the far north and one north of Santa Maria. Attribution: Leaflet | © OpenStreetMap contributors" src="https://static.simonwillison.net/static/2026/power-plants-pge.webp" /></p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/geospatial">geospatial</a>, <a href="https://simonwillison.net/tags/openstreetmap">openstreetmap</a></p>
