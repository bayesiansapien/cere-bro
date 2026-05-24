---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-24T06:15:57.058804+00:00
title: On the <dl>
url: https://simonwillison.net/2026/May/23/on-the-dl/#atom-everything
published: 2026-05-23
author: 
---

# On the <dl>

<p><strong><a href="https://benmyers.dev/blog/on-the-dl/">On the &lt;dl&gt;</a></strong></p>
I learned a few new-to-me things about the <code>&lt;dl&gt;</code> element from this article by Ben Meyer:</p>
<ol>
<li>A <code>&lt;dt&gt;</code> can be followed by <em>multiple</em> <code>&lt;dd&gt;</code></li>
<li>You can optionally group the <code>&lt;dt&gt;</code> and <code>&lt;dd&gt;</code> elements in a <code>&lt;div&gt;</code> for styling - but only a <code>&lt;div&gt;</code>.</li>
<li>You can label them using ARIA.</li>
<li>They've been called "description lists", not "definition lists", since <a href="https://www.w3.org/TR/2008/WD-html5-20080122/#the-dl">an HTML5 draft in 2008</a>.</li>
</ol>
<p>So this is valid:</p>
<pre><span class="pl-kos">&lt;</span><span class="pl-ent">h2</span> <span class="pl-c1">id</span>="<span class="pl-s">credits</span>"<span class="pl-kos">&gt;</span>Credits<span class="pl-kos">&lt;/</span><span class="pl-ent">h2</span><span class="pl-kos">&gt;</span>
<span class="pl-kos">&lt;</span><span class="pl-ent">dl</span> <span class="pl-c1">aria-labelledby</span>="<span class="pl-s">credits</span>"<span class="pl-kos">&gt;</span>
  <span class="pl-kos">&lt;</span><span class="pl-ent">div</span><span class="pl-kos">&gt;</span>
    <span class="pl-kos">&lt;</span><span class="pl-ent">dt</span><span class="pl-kos">&gt;</span>Author<span class="pl-kos">&lt;/</span><span class="pl-ent">dt</span><span class="pl-kos">&gt;</span>
    <span class="pl-kos">&lt;</span><span class="pl-ent">dd</span><span class="pl-kos">&gt;</span>Jeffrey Zeldman<span class="pl-kos">&lt;/</span><span class="pl-ent">dd</span><span class="pl-kos">&gt;</span>
    <span class="pl-kos">&lt;</span><span class="pl-ent">dd</span><span class="pl-kos">&gt;</span>Ethan Marcotte<span class="pl-kos">&lt;/</span><span class="pl-ent">dd</span><span class="pl-kos">&gt;</span>
  <span class="pl-kos">&lt;/</span><span class="pl-ent">div</span><span class="pl-kos">&gt;</span>
<span class="pl-kos">&lt;/</span><span class="pl-ent">dl</span><span class="pl-kos">&gt;</span></pre>

<p>Here's a useful note from Adrian Roselli on <a href="https://adrianroselli.com/2025/01/updated-brief-note-on-description-list-support.html">screen reader support for description lists</a>.

    <p><small></small>Via <a href="https://news.ycombinator.com/item?id=48247325">Hacker News</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/css">css</a>, <a href="https://simonwillison.net/tags/html">html</a>, <a href="https://simonwillison.net/tags/screen-readers">screen-readers</a>, <a href="https://simonwillison.net/tags/web-standards">web-standards</a></p>
