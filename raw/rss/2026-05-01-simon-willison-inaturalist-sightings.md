---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-02T06:18:28Z
title: iNaturalist Sightings
url: https://simonwillison.net/2026/May/1/inat-sightings/#atom-everything
published: 2026-05-01
author: 
---

# iNaturalist Sightings

<p><strong>Tool:</strong> <a href="https://tools.simonwillison.net/inat-sightings">iNaturalist Sightings</a></p>
        <p>I wanted to see my <a href="https://www.inaturalist.org">iNaturalist</a> observations - across two separate accounts - grouped by when they occurred. I'm camping this weekend so I built this entirely on my phone using Claude Code for web.</p>
<p>I started by building an <a href="https://github.com/simonw/inaturalist-clumper">inaturalist-clumper</a> Python CLI for fetching and "clumping" observations - by default clumps use observations within 2 hours and 5km of each other.</p>
<p>Then I setup <a href="https://github.com/simonw/inaturalist-clumps">simonw/inaturalist-clumps</a> as a <a href="https://simonwillison.net/series/git-scraping/">Git scraping</a> repository to run that tool and record the result to <a href="https://github.com/simonw/inaturalist-clumps/blob/main/clumps.json">clumps.json</a>.</p>
<p>That JSON file is hosted on GitHub, which means it can be fetched by JavaScript using CORS.</p>
<p>Finally I ran this prompt against my <a href="https://github.com/simonw/tools">simonw/tools</a> repo:</p>
<blockquote>
<p><code>Build inat-sightings.html - an app that does a fetch() against https://raw.githubusercontent.com/simonw/inaturalist-clumps/refs/heads/main/clumps.json and then displays all of the observations on one page using the https://static.inaturalist.org/photos/538073008/small.jpg small.jpg URLs for the thumbnails - with loading=lazy - but when a thumbnail is clicked showing the large.jpg in an HTML modal. Both small and large should include the common species names if available</code></p>
</blockquote>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/tools">tools</a>, <a href="https://simonwillison.net/tags/claude-code">claude-code</a>, <a href="https://simonwillison.net/tags/inaturalist">inaturalist</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a></p>
