---
source: farmer/rss
feed: simon-willison
farmed: 2026-09-14T06:17:27.915813+00:00
title: shot-scraper 1.12
url: https://simonwillison.net/2026/Sep/13/shot-scraper/
published: 2026-09-13
author: 
---

# shot-scraper 1.12

<p><strong>Release:</strong> <a href="https://github.com/simonw/shot-scraper/releases/tag/1.12">shot-scraper 1.12</a></p>
        <p>I've added WebP support to my <a href="https://shot-scraper.datasette.io/">shot-scraper</a> screenshot automation tool. You can now take a WebP screenshot of a web page like this:</p>
<pre><code>shot-scraper https://simonwillison.net -o screenshot.webp --quality 80
</code></pre>
<p>The <code>--quality</code> option sets the quality - without that option the WebP file will be lossless.</p>
<p>In my experience WebP screenshots are almost always significantly smaller in file size than their JPEG or PNG equivalents. See <a href="https://github.com/simonw/shot-scraper/pull/210">the PR</a> for some examples.</p>
<p>I shipped this feature so I could use it to generate the screenshot <a href="https://simonwillison.net/2026/Sep/14/commit-rewriter/">for my new commit-rewriter tool</a>.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/playwright">playwright</a>, <a href="https://simonwillison.net/tags/shot-scraper">shot-scraper</a></p>
