---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-08T05:20:41Z
title: Open Source AI Gap Map
url: https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything
published: 2026-07-03
author: 
---

# Open Source AI Gap Map

<p><strong><a href="https://map.currentai.org">Open Source AI Gap Map</a></strong></p>
<a href="https://www.currentai.org">Current AI</a> is "a global partnership building a public option for AI", founded as a non-profit at the AI Action Summit in Paris in February 2025 and backed by serious capital ($400m already committed).</p>
<p>They <a href="https://www.currentai.org/blogs/introducing-the-gap-map-v0-1">launched their Gap Map</a> a couple of days ago - an attempt at indexing the current state of open source AI:</p>
<blockquote>
<p>The Gap Map v0.1 details 421 products in depth: 266 software tools and libraries, 85 models, 50 datasets, and 20 hardware projects, produced by 228 organizations. These products are organized into 14 categories across 3 layers of the stack (model components, product / UX, and infrastructure). The remaining 24,400 artifacts constitute the uncategorized long tail of the open source AI ecosystem, and will carry no score until they are researched and cited.</p>
</blockquote>
<p>The map itself is interesting to explore, but I'm more excited about the underlying data - released under an MIT license in the <a href="https://github.com/currentai-org/os-ai-map">currentai-org/os-ai-map</a> GitHub account: 1,184 YAML files plus the notebooks, schemas and other scripts used to help gather them.</p>
<p>Since the files are on GitHub you can use Datasette Lite to explore some of them - here are <a href="https://lite.datasette.io/?csv=https://github.com/currentai-org/os-ai-map/blob/main/warehouse/catalog/goodailist/repos.csv#/data/repos?_sort_desc=stars">16,185 GitHub repos the project is tracking</a> as a CSV file loaded into Datasette Lite.


    <p>Tags: <a href="https://simonwillison.net/tags/open-source">open-source</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/datasette-lite">datasette-lite</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/local-llms">local-llms</a>, <a href="https://simonwillison.net/tags/llms">llms</a></p>
