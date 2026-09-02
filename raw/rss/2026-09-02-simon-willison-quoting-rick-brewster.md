---
source: farmer/rss
feed: simon-willison
farmed: 2026-09-02T08:03:45.430309+00:00
title: Quoting Rick Brewster
url: https://simonwillison.net/2026/Sep/2/rick-brewster/
published: 2026-09-02
---

# Quoting Rick Brewster

<blockquote cite="https://forums.paint.net/topic/134563-🍷-extremely-experimental-winelinux-support-how-to-get-started/"><p>Direct2D has always been the biggest hurdle for Paint.NET on WINE, and it's clear that it will never be completed enough for Paint.NET's use. And I can't just "disable" the use of Direct2D. So, instead, <strong>Paint.NET now has an internal, from-scratch, clean-room reverse-engineered rewrite of Direct2D that it uses on WINE</strong> (triggered by using <strong>/wine</strong>). It lives in <strong>PaintDotNet.Windows.Direct2D1.Managed.dll</strong>. This was written by our good friend <a href="https://claude.ai/">Claude</a>, without whom this would NOT have been possible and would NEVER have happened. [...]</p>
<p>Most of this code is, as they say, "vibe coded." By that I mean that it has not been thoroughly reviewed, it's more "trust me bro" style. I cannot possibly review 180,000 lines of code, it's just way way <em>way</em> too much. For reference, the rest of Paint.NET is about 700,000 lines of code and I've been working on it for over 20 years. [...]</p>
<p>At times, Claude was working with the fury of 10 freshly unshackled Einstein genius-level 10x coders. And other times ... well, not so much. I had to babysit Claude quite a bit to make sure it did resource management correctly (for awhile it just wasn't doing the COM equivalent of AddRef() for reference counted objects, oops). I had to slap it a few times when I found some really bad design or architecture decisions. And I was also impressed at some rather clever and tireless reverse engineering work it did to figure out all the formulas needed for implementing Direct2D's built-in effects library.</p></blockquote>
<p class="cite">&mdash; <a href="https://forums.paint.net/topic/134563-🍷-extremely-experimental-winelinux-support-how-to-get-started/">Rick Brewster</a>, author of Paint.NET</p>

    <p>Tags: <a href="https://simonwillison.net/tags/reverse-engineering">reverse-engineering</a>, <a href="https://simonwillison.net/tags/coding-agents">coding-agents</a>, <a href="https://simonwillison.net/tags/claude">claude</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/dotnet">dotnet</a>, <a href="https://simonwillison.net/tags/linux">linux</a>, <a href="https://simonwillison.net/tags/vibe-coding">vibe-coding</a></p>
