---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-19T22:17:42.122549+00:00
title: DOOMQL
url: https://simonwillison.net/2026/Jul/13/doomql/#atom-everything
published: 2026-07-13
---

# DOOMQL

<p><strong><a href="https://github.com/petergpt/doomql">DOOMQL</a></strong></p>
Peter Gostev built this using GPT-5.6 Sol. This is a <em>lot</em> of fun: </p>
<blockquote>
<p>DOOMQL started with a deliberately unreasonable question: what if SQLite were the game engine, not merely the place where a game stores data?</p>
<p>The result is a small, original Doom-like game in which SQL owns movement, collision, enemies, combat, progression and every RGB pixel on screen.</p>
</blockquote>
<p>It's implemented as a Python terminal script - I tried it out like this:</p>
<pre><code>cd /tmp
git clone https://github.com/petergpt/doomql
cd doomql
uv run host/doomql.py
</code></pre>
<p><img alt="Screenshot of a macOS terminal window titled &quot;doomql — python3.14 ◂ uv run host/doomql.py — 134×31&quot; showing a retro Doom-style game rendered as text-mode pixel art. The scene is a pixelated first-person corridor with gray paneled walls, dark red doors on the far left and right, a floating cyan-and-gold coin pickup on the right side, a white crosshair near the center, and a dark weapon barrel rising from the bottom center. A status bar below the scene reads &quot;HP 100/100 AMMO 037 SCORE 00225 INDEX MISSING TICK 0028450&quot;, followed by an orange line &quot;FIND THE INDEX TOKEN&quot; and a cyan controls line &quot;WASD MOVE J/L OR ARROWS TURN SPACE FIRE E USE P PAUSE CTRL-C EXIT&quot;." src="https://static.simonwillison.net/static/2026/doomql-window.png" /></p>
<p>Here's <a href="https://github.com/petergpt/doomql/blob/main/sql/003_render.sql">the huge SQL query</a> that implements a full ray tracer in SQLite using a recursive CTE.</p>
<p>Running the above script creates a <code>/tmp/doomql/.doomql/doomql.sqlite</code> SQLite database, which you can explore using Datasette like this:</p>
<pre><code>uvx --prerelease=allow  --with datasette-apps datasette \
  /tmp/doomql/.doomql/doomql.sqlite \
  -p 4444 --root --secret 1 --internal internal.db
</code></pre>
<p>The <code>--with datasette-apps</code> option installs the new <a href="https://simonwillison.net/2026/Jun/18/datasette-apps/">Datasette Apps</a> plugin, which supports creating custom HTML+JavaScript apps that can run SQL queries directly within the Datasette interface.</p>
<p>I created a new app, pasted the copy-paste prompt into Claude chat (Fable 5) <a href="https://claude.ai/share/c793280c-2ef1-4555-a7c2-31281abfdf78">and told it</a>:</p>
<blockquote>
<p><code>Build an app that displays the current state of the screen using the frame_pixels view with its x, y, r, g, b columns. have it refresh once a second.</code></p>
</blockquote>
<p>This got me a working HTML+JavaScript app inside Datasette that could reflect the current state while I played the game in my terminal. Then I added:</p>
<blockquote>
<p><code>add a minimap</code></p>
</blockquote>
<p>And now my Datasette App looks like this:</p>
<p><img alt="Screenshot of a dark-themed web app running a retro Doom-style game rendered from SQL queries. The page header reads &quot;DOOMQL&quot; with buttons &quot;All apps&quot;, &quot;Edit app&quot;, &quot;Pin&quot;, and &quot;Full screen&quot;. Inside the game panel, the title &quot;DOOMQL&quot; sits above the subtitle &quot;auto-refreshing once a second · frame and tactical map straight from SQL&quot;. The left side shows a pixelated first-person corridor view with gray walls, dark red doors, a floating cyan-and-gold coin pickup, a white crosshair, and a weapon barrel at bottom center. A status bar below reads &quot;HP 100/100 AMMO 037 SCORE 00225 INDEX MISSING TICK 0027847&quot;. On the right, a panel titled &quot;TACTICAL MAP&quot; shows a top-down grid map with a player triangle, a red enemy circle, yellow pickup dots, red wall markers, and a green exit square, with a legend reading &quot;you&quot;, &quot;enemy&quot;, &quot;pickup&quot;, &quot;locked door&quot;, &quot;door&quot;, &quot;exit&quot;. Below the game view, an orange banner reads &quot;FIND THE INDEX TOKEN&quot;, followed by the cyan line &quot;READ-ONLY VIEWER · SELECT x, y, r, g, b FROM frame_pixels&quot;. At the bottom, a green &quot;RUNNING&quot; badge appears beside the stats &quot;160×54 · 8,640 pixels · 3 hostiles · query 89 ms · refreshing every 1 s&quot;." src="https://static.simonwillison.net/static/2026/doomql-datasette-app.png" /></p>
<p>Here's <a href="https://gist.github.com/simonw/7c78184476fccd4b70b02f7f9048dffa">the HTML app code</a> - paste that into your own Datasette instance (using the <code>uvx --with datasette-apps</code> recipe from above) to try it yourself.

    <p><small></small>Via <a href="https://twitter.com/petergostev/status/2076692164310884468">@petergostev</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/games">games</a>, <a href="https://simonwillison.net/tags/sql">sql</a>, <a href="https://simonwillison.net/tags/sqlite">sqlite</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/ai-assisted-programming">ai-assisted-programming</a>, <a href="https://simonwillison.net/tags/gpt">gpt</a>, <a href="https://simonwillison.net/tags/datasette-apps">datasette-apps</a></p>
