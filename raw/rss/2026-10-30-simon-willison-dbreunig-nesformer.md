---
source: farmer/rss
feed: simon-willison
farmed: 2026-10-31T08:06:40.307181+00:00
title: "dbreunig/nesformer"
url: https://simonwillison.net/2026/Oct/30/nesformer/
published: 2026-10-30
author: 
---

# dbreunig/nesformer

<p><strong><a href="https://github.com/dbreunig/nesformer">dbreunig/nesformer</a></strong></p>
Inspired by <a href="https://divagr.com/blog/qwenputer">qwenputer</a> by Divyansh Agrawal, Drew Breunig baked a working emulator for a Nintendo Entertainment System 6502 CPU into the weights of Qwen3.5-4B. You can now play NES ROMs such as Super Mario Bros (very slowly) running inside Qwen!</p>
<p>In <a href="https://news.ycombinator.com/item?id=50306442#50307402">a comment on Hacker News</a> Drew reveals the Opus 5.5 prompts he used to build this system:</p>
<blockquote>
<p><code>Read this article and any relevant source code: https://divagr.com/blog/qwenputer. Then explore if you could emulate the chip and ram in a Nintendo Entertainment System (as people do today with FPGAs in MISTRs) using this technique. If so, what size model would you have to build and if you could use smaller faster ones, could you get it to be at the standard clockspeed.</code></p>
</blockquote>
<p>Followed by:</p>
<blockquote>
<p><code>I think we should build it! Just for fun. It's okay if it's not fast. We want to be able to have the weights, and a cli to run them that we can point at a ROM.</code></p>
</blockquote>
<p>Apparently Opus found and then used <a href="https://github.com/christopherpow/nes-test-roms/blob/master/other/nestest.txt">this collection of conformance tests</a> for the NES CPU released 15 years ago by Christopher Pow.

    <p><small></small>Via <a href="https://news.ycombinator.com/item?id=50306442">Hacker News</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/games">games</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/drew-breunig">drew-breunig</a>, <a href="https://simonwillison.net/tags/qwen">qwen</a>, <a href="https://simonwillison.net/tags/conformance-suites">conformance-suites</a></p>
