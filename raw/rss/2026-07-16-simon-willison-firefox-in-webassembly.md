---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-19T22:17:42.118636+00:00
title: Firefox in WebAssembly
url: https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything
published: 2026-07-16
---

# Firefox in WebAssembly

<p><strong><a href="https://developer.puter.com/labs/firefox-wasm/">Firefox in WebAssembly</a></strong></p>
This is absurdly cool: Puter compiled Firefox to WebAssembly such that the whole browser runs in another browser.</p>
<p>Here's my blog, running in Firefox, running in WebAssembly, running in Chrome:</p>
<p><img alt="A Chrome window. The tab has the Firefox UI and has loaded my blog. On the right is the Chrome network panel showing that it loaded resources that include a 233MB gecko.wasm and an 18MB chrome-assets.tar.zst" src="https://static.simonwillison.net/static/2026/firefox-wasm.webp" /></p>
<p>They chose Firefox/Gecko because it has strong single-process support. The project used an estimated $25,000 worth of Claude Opus and Fable tokens, but took advantage of a Claude Max subscription plan so cost much less in actual dollars.</p>
<p>The demo funnels all traffic over a WebSocket protocol (using the <a href="https://github.com/MercuryWorkshop/wisp-protocol">Wisp protocol</a>) through Puter's server - a requirement to get this kind of thing to work because code running in browsers can't open arbitrary network connections.</p>
<p>(That proxying sounds expensive! The team <a href="https://news.ycombinator.com/item?id=48926939#48936563">had to scale the servers up</a> to handle the traffic during the Hacker News conversation about the project.)</p>
<p>Puter claim this supports end-to-end encryption and that looks to be true - I inspected the WebSocket messages and traffic to my own HTTPS site was encrypted whereas requests and responses to <code>http://www.example.com/</code> were in cleartext.</p>
<p><a href="https://github.com/HeyPuter/firefox-wasm">Here's the repo</a> for <code>firefox-wasm</code>. <a href="https://github.com/theogbob/WebkitWasm">theogbob/WebkitWasm</a> is a similar project that compiles WebKit to WASM, but that one doesn't currently have an accessible online demo.

    <p><small></small>Via <a href="https://news.ycombinator.com/item?id=48926939">Hacker News</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/browsers">browsers</a>, <a href="https://simonwillison.net/tags/firefox">firefox</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/webassembly">webassembly</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/ai-assisted-programming">ai-assisted-programming</a>, <a href="https://simonwillison.net/tags/claude">claude</a>, <a href="https://simonwillison.net/tags/claude-mythos-fable">claude-mythos-fable</a></p>
