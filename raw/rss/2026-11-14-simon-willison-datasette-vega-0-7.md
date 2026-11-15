---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-15T06:33:59.911718+00:00
title: "datasette-vega 0.7"
url: https://simonwillison.net/2026/Nov/14/datasette-vega/
published: 2026-11-14
author: 
---

# datasette-vega 0.7

<p><strong>Release:</strong> <a href="https://github.com/simonw/datasette-vega/releases/tag/0.7">datasette-vega 0.7</a></p>
        <p>A new release of Datasette's longest untouched plugin, for rendering charts (using <a href="https://vega.github.io/vega-lite/">Vega-Lite</a>) against data in a table or custom query. The last release was in July 2018!</p>
<p>I finally bumped it for compatibility with the latest Datasette alphas, plus some cosmetic tweaks to make it work better with <a href="https://lite.datasette.io/">Datasette Lite</a>.</p>
<p>(Datasette Lite just gained the ability to run JavaScript plugins like this! I'll write more about that soon.)</p>
<p>Since it works with Datasette Lite, the live demo in the README now <a href="https://lite.datasette.io/?install=datasette-vega&amp;csv=https%3A%2F%2Fraw.githubusercontent.com%2Ffivethirtyeight%2Fdata%2Fmaster%2Fairline-safety%2Fairline-safety.csv#/data/airline-safety?_size=max#g.mark=bar&amp;g.x_column=airline&amp;g.x_type=ordinal&amp;g.y_column=fatalities_00_14&amp;g.y_type=quantitative">links to this demo on Datasette Lite</a>.</p>
<p><img alt="Screenshot of a charting tool. A panel headed &quot;Charting options&quot; has radio buttons for &quot;Bar&quot; (selected), &quot;Line&quot; and &quot;Scatter&quot;. Below are select menus: &quot;X column&quot; set to &quot;airline&quot; with &quot;Type&quot; set to &quot;Label&quot;, and &quot;Y column&quot; set to &quot;fatalities_00_14&quot; with &quot;Type&quot; set to &quot;Numeric&quot;. A &quot;Swap X and Y&quot; button sits beneath those, followed by &quot;Color&quot; and &quot;Size&quot; menus both set to &quot;-- none --&quot;. Underneath the panel is a blue bar chart with airline names along the X axis and fatalities_00_14 on the Y axis, running from 0 to 550 - most airlines have no bar, a handful have bars, and Malaysia Airlines is the tallest." src="https://static.simonwillison.net/static/2026/datasette-vega.webp" /></p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/visualisation">visualisation</a>, <a href="https://simonwillison.net/tags/datasette-lite">datasette-lite</a></p>
