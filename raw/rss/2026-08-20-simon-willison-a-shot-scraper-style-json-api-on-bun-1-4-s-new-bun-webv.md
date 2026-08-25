---
source: farmer/rss
feed: simon-willison
farmed: 2026-08-25T14:24:43.465337+05:30
title: A shot-scraper-style JSON API on Bun 1.4's new Bun.WebView
url: https://simonwillison.net/2026/Aug/20/bun-webview-json-api/
published: 2026-08-20
---

# A shot-scraper-style JSON API on Bun 1.4's new Bun.WebView

<p><strong>Research:</strong> <a href="https://github.com/simonw/research/tree/main/bun-webview-json-api#readme">A shot-scraper-style JSON API on Bun 1.4&#x27;s new Bun.WebView</a></p>
        <p>Today saw the long awaited <a href="https://bun.com/blog/bun-v1.4">release of Bun 1.4</a>, the first stable version since the infamous Rust rewrite <a href="https://simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/">a few months ago</a>.</p>
<p>Interestingly, the Rust rewrite was downplayed in the release notes, which introduced a bewildering array of new features and claimed 2,900 additional bug fixes:</p>
<blockquote>
<p>Bun 1.4 adds +1,517 tests from the Node.js test suite - our biggest jump in Node.js compatibility since Bun 1.0. Bun v1.4 also fixes over 2,900 issues. It reduces idle CPU usage by 5x, reduces memory usage by up to 35%, and starts 50% faster on Linux. It adds <a href="https://bun.com/blog/bun-v1.4#bun-image"><code>Bun.Image</code></a>, <a href="https://bun.com/blog/bun-v1.4#bun-webview"><code>Bun.WebView</code></a>, <a href="https://bun.com/blog/bun-v1.4#bun-markdown"><code>Bun.markdown</code></a>, <a href="https://bun.com/blog/bun-v1.4#bun-cron"><code>Bun.cron()</code></a>, <a href="https://bun.com/blog/bun-v1.4#bun-terminal"><code>Bun.Terminal</code></a>, <a href="https://bun.com/blog/bun-v1.4#bun-run-parallel"><code>bun run --parallel</code></a>, <a href="https://bun.com/blog/bun-v1.4#bun-test-parallel"><code>bun test --parallel</code></a>, <a href="https://bun.com/blog/bun-v1.4#bun-audit-fix"><code>bun audit fix</code></a>, <a href="https://bun.com/blog/bun-v1.4#bun-dedupe"><code>bun dedupe</code></a>, and <a href="https://bun.com/blog/bun-v1.4#bun-prune"><code>bun prune</code></a>. And it rewrites Bun from Zig to Rust.</p>
</blockquote>
<p>Of these the one that most caught my eye was <code>Bun.WebView</code>, which adds first class support for browser automation to Bun core using either macOS WebKit or control of a local Chromium process via the Chrome DevTools Protocol (CDP).</p>
<p>I had Claude Code for web build a prototype of a web API providing the ability to load a web page and then execute JavaScript against it, inspired by my <a href="https://shot-scraper.datasette.io/en/stable/javascript.html">shot-scraper javascript</a> CLI tool - partly to see how much RAM would be needed by such a service.</p>
<p>Here's <a href="https://github.com/simonw/research/blob/main/bun-webview-json-api/server.ts">that TypeScript server implementation</a>, which appears to need a 192MB-256MB container to run a full Chrome against complex web pages - tested using cgroups.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/browsers">browsers</a>, <a href="https://simonwillison.net/tags/javascript">javascript</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/rust">rust</a>, <a href="https://simonwillison.net/tags/typescript">typescript</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/coding-agents">coding-agents</a>, <a href="https://simonwillison.net/tags/bun">bun</a></p>
