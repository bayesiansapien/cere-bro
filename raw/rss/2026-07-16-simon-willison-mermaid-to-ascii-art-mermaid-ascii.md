---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-19T22:17:42.121592+00:00
title: Mermaid to ASCII art (mermaid-ascii)
url: https://simonwillison.net/2026/Jul/16/mermaid-ascii/#atom-everything
published: 2026-07-16
---

# Mermaid to ASCII art (mermaid-ascii)

<p><strong>Tool:</strong> <a href="https://tools.simonwillison.net/mermaid-ascii">Mermaid to ASCII art (mermaid-ascii)</a></p>
        <p>After building the <a href="https://simonwillison.net/2026/Jul/16/grok-mermaid/">Mermaid to ASCII tool based on Grok Build's Rust code</a> I learned that there's an older, more fully-featured Go library called <a href="https://github.com/AlexanderGrooff/mermaid-ascii">AlexanderGrooff/mermaid-ascii</a> that implements a similar pattern, so I had Claude Fable 5 compile that one to WebAssembly as well so I could compare the two.</p>
<p>This one includes support for colors!</p>
<p><img alt="Screenshot of a Mermaid diagram editor web app. A row of tab buttons reads: Flowchart, Multiple links, Subgraphs, Multi-line labels, Colors (selected, highlighted blue), Sequence, Alt fragment, Loop + note, Parallel. Below is a text input area containing: &quot;graph LR / Build:::good --&gt; Test:::good / Test --&gt; Deploy:::warn / Deploy --&gt; Rollback:::bad / classDef good color:#3fb950 / classDef warn color:#e3b341 / classDef bad color:#ff7b72&quot;. A control row shows an unchecked &quot;ASCII only&quot; checkbox, &quot;Padding X: 5&quot;, &quot;Padding Y: 5&quot;, &quot;Box padding: 1&quot;, and buttons &quot;Copy as text&quot; and &quot;Copy link to this diagram&quot;. At the bottom on a black background is the rendered left-to-right flowchart with four connected boxes: &quot;Build&quot; (green text), &quot;Test&quot; (green text), &quot;Deploy&quot; (yellow text), &quot;Rollback&quot; (red text), each linked by arrows." src="https://static.simonwillison.net/static/2026/mermaid-ascii.webp" /></p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/go">go</a>, <a href="https://simonwillison.net/tags/tools">tools</a>, <a href="https://simonwillison.net/tags/webassembly">webassembly</a>, <a href="https://simonwillison.net/tags/mermaid">mermaid</a></p>
