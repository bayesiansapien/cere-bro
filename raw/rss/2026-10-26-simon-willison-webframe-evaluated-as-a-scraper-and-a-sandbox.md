---
source: farmer/rss
feed: simon-willison
farmed: 2026-10-27T05:06:37.706891+00:00
title: "webframe: evaluated as a scraper and a sandbox"
url: https://simonwillison.net/2026/Oct/26/webframe-evaluation/
published: 2026-10-26
author: 
---

# webframe: evaluated as a scraper and a sandbox

<p><strong>Research:</strong> <a href="https://github.com/simonw/research/tree/main/webframe-evaluation#readme">webframe: evaluated as a scraper and a sandbox</a></p>
        <p><a href="https://github.com/tractordev/webframe">webframe</a> is a neat little project from Jeff Lindsay which lets you "run a web page like a program" - you point it at a URL or file and it executes it in a hidden headless web view and outputs <code>console.log()</code> to standard output and any exceptions to standard error.</p>
<p>It's written in Go on top of the <a href="https://github.com/crgimenes/glaze">glaze</a> library, which provides access to a system browser ("WKWebView on macOS, WebKitGTK on Linux, WebView2 on Windows") so it doesn't need to bundle its own browser engine.</p>
<p>It reminds me of my own <a href="https://shot-scraper.datasette.io/en/stable/javascript.html">shot-scraper javascript</a> tool, albeit in a much smaller package that doesn't depend on Playwright.</p>
<p>I had Claude Opus 5.5 <a href="https://claude.ai/code/cshk_01MX3aJH8vDGmGSj1xH9BYhj2HviVvLDaJbiELHyDoReYT">put it through its paces</a> and prepare a research report for me. Here's the prompt I used:</p>
<blockquote>
<p><code>Explore https://github.com/tractordev/webframe try running it and put it though its paces, build a few exploratory prototypes, then evaluate it as a potential sandboxing tool and as a tool for scraping web pages using the same patterns encouraged by the "shot-scraper JavaScript" command (see simonw/shot-scraper on GitHub, docs directory)</code></p>
</blockquote>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/browsers">browsers</a>, <a href="https://simonwillison.net/tags/go">go</a>, <a href="https://simonwillison.net/tags/javascript">javascript</a>, <a href="https://simonwillison.net/tags/jeff-lindsay">jeff-lindsay</a>, <a href="https://simonwillison.net/tags/shot-scraper">shot-scraper</a></p>
