---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-19T22:17:42.122812+00:00
title: shot-scraper 1.11
url: https://simonwillison.net/2026/Jul/12/shot-scraper/#atom-everything
published: 2026-07-12
---

# shot-scraper 1.11

<p><strong>Release:</strong> <a href="https://github.com/simonw/shot-scraper/releases/tag/1.11">shot-scraper 1.11</a></p>
        <p>Some minor improvements, mainly around command option consistency and making the <code>server:</code> mechanism <a href="https://shot-scraper.datasette.io/en/stable/multi.html#running-a-server-for-the-duration-of-the-session">used by</a> both <code>shot-scraper video</code> and <code>shot-scraper multi</code> work if the server takes longer than a second to start serving traffic.</p>
<blockquote>
<ul>
<li><code>server:</code> processes used by <code>shot-scraper multi</code> and <code>shot-scraper video</code> now wait up to 30 seconds for the target URL to accept connections, polling for port availability and replacing the previous fixed one-second delay. <a href="https://github.com/simonw/shot-scraper/issues/197">#197</a></li>
<li>The <code>shot-scraper</code>, <code>pdf</code>, <code>html</code>, <code>accessibility</code> and <code>har</code> commands now have a <code>--js-file</code> option for loading JavaScript from a local file, standard input or <code>gh:username/script</code>, as an alternative to <code>--javascript</code>which accepts the string of JavaScript directly as an argument. <a href="https://github.com/simonw/shot-scraper/issues/192">#192</a></li>
<li><code>shot-scraper multi</code> supports the equivalent <code>js_file:</code> YAML key. </li>
<li>The <code>shot-scraper javascript</code> and <code>shot-scraper html</code> commands now have a <code>--timeout</code> option for consistency with other commands. <a href="https://github.com/simonw/shot-scraper/issues/118">#118</a></li>
</ul>
</blockquote>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/shot-scraper">shot-scraper</a></p>
