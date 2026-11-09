---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-09T14:17:49.617285+00:00
title: "datasette #3046: Don't serve link: rel=next HTTP headers to Firefox for HTML pages"
url: https://simonwillison.net/2026/Nov/7/link-rel-next/
published: 2026-11-07
author: 
---

# datasette #3046: Don't serve link: rel=next HTTP headers to Firefox for HTML pages

<p><strong><a href="https://github.com/simonw/datasette/issues/3046">datasette #3046: Don&#x27;t serve link: rel=next HTTP headers to Firefox for HTML pages</a></strong></p>
I was looking at the Firefox network panel today when I noticed that requests to a Datasette table page were triggering an <a href="https://developer.mozilla.org/en-US/docs/Glossary/Prefetch">HTTP prefetch</a> to the next page of rows in that table.</p>
<p>This was happening because Datasette pages serve an HTTP <code>link</code> header like this:</p>
<p><code>link: &lt;https://latest.datasette.io/fixtures/compound_three_primary_keys?_next=a%2Cd%2Cv&gt;; rel="next"</code></p>
<p>This is bad. A tiny fraction of the visitors to one of those pages will click the "next" link, which means for everyone else their browser is fetching unnecessary data and the Datasette server is having to render an entire page that then gets thrown away.</p>
<p>I dug in and learned that Firefox has <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=175418">an issue</a> that has been open for 24 years about this behavior...</p>
<p>And one of the early comments on that issue links to <a href="https://simonwillison.net/2002/Oct/17/mozillaPrefetching/">my blog post from 2002</a> complaining about this feature. I hadn't just forgotten that I had written about it, I had forgotten the feature entirely!


    <p>Tags: <a href="https://simonwillison.net/tags/firefox">firefox</a>, <a href="https://simonwillison.net/tags/html">html</a>, <a href="https://simonwillison.net/tags/mozilla">mozilla</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a></p>
