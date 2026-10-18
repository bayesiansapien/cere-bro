---
source: farmer/rss
feed: simon-willison
farmed: 2026-10-18T05:07:11.354557+00:00
title: "Inline rendering with document​.currentScript"
url: https://simonwillison.net/2026/Oct/17/document-currentscript/
published: 2026-10-17
author: 
---

# Inline rendering with document​.currentScript

<p><strong><a href="https://leanrada.com/notes/inline-rendering-currentscript/">Inline rendering with document​.currentScript</a></strong></p>
Lean Rada describes a neat trick that takes advantage of the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Document/currentScript">document.currentScript</a> property. You can use that to drop in a tiny inline <code>&lt;script&gt;</code> element that replaces itself when the page loads:</p>
<pre><code>The year is &lt;script&gt;
document.currentScript.replaceWith(
  new Date().getFullYear())&lt;/script&gt;
</code></pre>
<p>If you define a shortcut function like this:</p>
<pre><code>$=(...n)=&gt;document.currentScript.replaceWith(...n)
</code></pre>
<p>You get a tiny template language:</p>
<pre><code>The year is &lt;script&gt;$(new Date().getFullYear())&lt;/script&gt;
</code></pre>


    <p>Tags: <a href="https://simonwillison.net/tags/javascript">javascript</a></p>
