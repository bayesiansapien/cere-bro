---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-23T05:03:44.628677+00:00
title: "Select Styling Specimens"
url: https://simonwillison.net/2026/Nov/22/select-styling/
published: 2026-11-22
author: 
---

# Select Styling Specimens

<p><strong>Tool:</strong> <a href="https://tools.simonwillison.net/select-styling">Select Styling Specimens</a></p>
        <p>I got frustrated at how HTML <code>&lt;select&gt;</code> boxes default to looking different in different browsers, and are (I think) quite ugly in Chrome:</p>
<p><img alt="The same select box in Chrome, Safari, and Firefox, Chrome is white with a black border. Safari is grey with no border. Firefox is gray with a black border. They are all slightly different sizes." src="https://static.simonwillison.net/static/2026/select-firefox-safari-chrome.webp" /></p>
<p>So I had Claude Fable 5.2 <a href="https://claude.ai/share/a82c181c-0ea6-4fec-a659-8de653cb3e7b">build</a> me <a href="https://tools.simonwillison.net/select-styling">this page</a> showing all of the ways they can be styled:</p>
<blockquote>
<p><code>Build an HTML page that shows all of the ways a select box can be styled, I plan to take screenshots in every desktop and mobile browser</code></p>
</blockquote>
<p>After some experimentation I've decided my favorite CSS for select boxes is this:</p>
<div class="highlight highlight-source-css"><pre><span class="pl-ent">select</span> <span class="pl-kos">{</span>
  <span class="pl-c1">appearance</span><span class="pl-kos">:</span> none<span class="pl-kos">;</span>
  <span class="pl-c1">color</span><span class="pl-kos">:</span> <span class="pl-pds"><span class="pl-kos">#</span>1f2933</span><span class="pl-kos">;</span>
  <span class="pl-c1">padding</span><span class="pl-kos">:</span> <span class="pl-c1">0.5<span class="pl-smi">em</span></span> <span class="pl-c1">2.25<span class="pl-smi">em</span></span> <span class="pl-c1">0.5<span class="pl-smi">em</span></span> <span class="pl-c1">0.75<span class="pl-smi">em</span></span><span class="pl-kos">;</span>
  <span class="pl-c1">border</span><span class="pl-kos">:</span> <span class="pl-c1">1<span class="pl-smi">px</span></span> solid <span class="pl-pds"><span class="pl-kos">#</span>c4cbd3</span><span class="pl-kos">;</span>
  <span class="pl-c1">border-radius</span><span class="pl-kos">:</span> <span class="pl-c1">6<span class="pl-smi">px</span></span><span class="pl-kos">;</span>
  <span class="pl-c1">background</span><span class="pl-kos">:</span> <span class="pl-pds"><span class="pl-kos">#</span>fff</span> <span class="pl-en">url</span><span class="pl-kos">(</span><span class="pl-s">"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 8'%3E%3Cpath d='M1 1.5l5 5 5-5' fill='none' stroke='%23667085' stroke-width='1.5'/%3E%3C/svg%3E"</span><span class="pl-kos">)</span> no-repeat right <span class="pl-c1">0.75<span class="pl-smi">em</span></span> center <span class="pl-c1">/</span> <span class="pl-c1">0.75<span class="pl-smi">em</span></span><span class="pl-kos">;</span>
<span class="pl-kos">}</span></pre></div>

<p>Here's what that looks like in the three browsers:</p>
<p><img alt="Now the select box is the same in all three browsers - it has a rounded corner grey border and a grey downward facing arrow in each one." src="https://static.simonwillison.net/static/2026/select-styled-firefox-safari-chrome.webp" /></p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/tools">tools</a>, <a href="https://simonwillison.net/tags/css">css</a>, <a href="https://simonwillison.net/tags/html">html</a></p>
