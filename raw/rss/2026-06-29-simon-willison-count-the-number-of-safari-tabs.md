---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-08T05:20:41Z
title: Count the number of Safari tabs
url: https://simonwillison.net/2026/Jun/29/safari-tab-count/#atom-everything
published: 2026-06-29
author: 
---

# Count the number of Safari tabs

<p>Tiniest TIL, using AppleScript to count the number of open browser tabs in Safari:</p>
<pre><code>osascript -e 'tell application "Safari" to count tabs of every window'
</code></pre>
<p><img alt="I ran it in a terminal window and got back 370." src="https://static.simonwillison.net/static/2026/tab-shame.jpg" /></p>

    <p>Tags: <a href="https://simonwillison.net/tags/safari">safari</a>, <a href="https://simonwillison.net/tags/til">til</a>, <a href="https://simonwillison.net/tags/applescript">applescript</a></p>
