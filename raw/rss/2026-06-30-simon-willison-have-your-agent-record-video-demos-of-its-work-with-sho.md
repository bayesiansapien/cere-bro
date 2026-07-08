---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-08T05:20:41Z
title: Have your agent record video demos of its work with shot-scraper video
url: https://simonwillison.net/2026/Jun/30/shot-scraper-video/#atom-everything
published: 2026-06-30
author: 
---

# Have your agent record video demos of its work with shot-scraper video

<p><a href="https://shot-scraper.datasette.io/en/stable/video.html">shot-scraper video</a> is a new command introduced in today's <a href="https://github.com/simonw/shot-scraper/releases/tag/1.10">shot-scraper 1.10</a> release which accepts a <code>storyboard.yml</code> file defining a routine to run against a web application and uses Playwright to record a video of that routine. I've written before about the importance of <a href="https://simonwillison.net/2026/Feb/10/showboat-and-rodney/#proving-code-actually-works">having coding agents produce demos</a> of their work; this is my latest attempt at enabling them to do that.</p>
<p>Here's an example video created using <code>shot-scraper video</code>, exercising a <a href="https://github.com/simonw/datasette/pull/2813">still in development</a> feature adding the ability to create new tables in Datasette from pasted CSV, TSV or JSON data:</p>
<div style="margin-bottom: 0.4em;">
    <video controls="controls" loop="loop" poster="https://static.simonwillison.net/static/2026/datasette-bulk-insert-demo.jpg" preload="none" style="width: 100%; height: auto;">
        <source src="https://static.simonwillison.net/static/2026/datasette-bulk-insert-demo.mp4" type="video/mp4" />
    </video>
</div>
<p>That video was created by running this command:</p>
<div class="highlight highlight-source-shell"><pre>shot-scraper video datasette-bulk-insert-storyboard.yml \
  --auth datasette-demo-auth.json --mp4</pre></div>
<p>(That <code>--auth</code> JSON file <a href="https://gist.github.com/simonw/287b26aff53fcb72942b19f5b69d7e5c">contains a cookie</a>, as <a href="https://shot-scraper.datasette.io/en/stable/authentication.html">described here</a> in the documentation.)</p>
<p>Here's the <code>datasette-bulk-insert-storyboard.yml</code> file:</p>
<div class="highlight highlight-source-yaml"><pre><span class="pl-ent">output</span>: <span class="pl-s">/tmp/datasette-bulk-insert-demo.webm</span>
<span class="pl-ent">server</span>:
  - <span class="pl-s">uv</span>
  - <span class="pl-s">--directory</span>
  - <span class="pl-s">/Users/simon/Dropbox/dev/datasette</span>
  - <span class="pl-s">run</span>
  - <span class="pl-s">datasette</span>
  - <span class="pl-s">-p</span>
  - <span class="pl-c1">6419</span>
  - <span class="pl-s">--root</span>
  - <span class="pl-s">--secret</span>
  - <span class="pl-s"><span class="pl-pds">"</span>1<span class="pl-pds">"</span></span>
  - <span class="pl-s">/tmp/demo.db</span>
<span class="pl-ent">url</span>: <span class="pl-s">http://127.0.0.1:6419/demo/tasks</span>
<span class="pl-ent">viewport</span>:
  <span class="pl-ent">width</span>: <span class="pl-c1">1280</span>
  <span class="pl-ent">height</span>: <span class="pl-c1">720</span>
<span class="pl-ent">cursor</span>: <span class="pl-c1">true</span>
<span class="pl-ent">wait_for</span>: <span class="pl-s"><span class="pl-pds">'</span>button[data-table-action="insert-row"]<span class="pl-pds">'</span></span>
<span class="pl-ent">javascript</span>: <span class="pl-s">|</span>
<span class="pl-s">  (() =&gt; {</span>
<span class="pl-s">    let clipboardText = "";</span>
<span class="pl-s">    Object.defineProperty(navigator, "clipboard", {</span>
<span class="pl-s">      configurable: true,</span>
<span class="pl-s">      get: () =&gt; ({</span>
<span class="pl-s">        writeText: async (text) =&gt; {</span>
<span class="pl-s">          clipboardText = String(text);</span>
<span class="pl-s">        },</span>
<span class="pl-s">        readText: async () =&gt; clipboardText,</span>
<span class="pl-s">      }),</span>
<span class="pl-s">    });</span>
<span class="pl-s">  })();</span>
<span class="pl-s"></span><span class="pl-ent">scenes</span>:
  - <span class="pl-ent">name</span>: <span class="pl-s">Bulk insert existing table rows</span>
    <span class="pl-ent">do</span>:
      - <span class="pl-ent">pause</span>: <span class="pl-c1">0.8</span>
      - <span class="pl-ent">click</span>: <span class="pl-s"><span class="pl-pds">'</span>button[data-table-action="insert-row"]<span class="pl-pds">'</span></span>
      - <span class="pl-ent">wait_for</span>: <span class="pl-s"><span class="pl-pds">"</span>#row-edit-dialog[open]<span class="pl-pds">"</span></span>
      - <span class="pl-ent">pause</span>: <span class="pl-c1">0.5</span>
      - <span class="pl-ent">click</span>: <span class="pl-s"><span class="pl-pds">"</span>.row-edit-bulk-insert<span class="pl-pds">"</span></span>
      - <span class="pl-ent">wait_for</span>: <span class="pl-s"><span class="pl-pds">"</span>.row-edit-bulk-textarea<span class="pl-pds">"</span></span>
      - <span class="pl-ent">pause</span>: <span class="pl-c1">0.5</span>
      - <span class="pl-ent">click</span>: <span class="pl-s"><span class="pl-pds">"</span>.row-edit-copy-template<span class="pl-pds">"</span></span>
      - <span class="pl-ent">wait_for</span>: <span class="pl-s"><span class="pl-pds">"</span>text=Copied<span class="pl-pds">"</span></span>
      - <span class="pl-ent">pause</span>: <span class="pl-c1">0.8</span>
      - <span class="pl-ent">fill</span>:
          <span class="pl-ent">into</span>: <span class="pl-s"><span class="pl-pds">"</span>.row-edit-bulk-textarea<span class="pl-pds">"</span></span>
          <span class="pl-ent">text</span>: <span class="pl-s">|</span>
<span class="pl-s">            title,owner,status,priority,notes</span>
<span class="pl-s">            Prepare release video,Ana,doing,1,Recorded with shot-scraper</span>
<span class="pl-s">            Check pasted CSV import,Ben,review,3,Previewed before inserting</span>
<span class="pl-s">            Share the branch demo,Chen,queued,2,Bulk insert creates three rows</span>
<span class="pl-s"></span>      - <span class="pl-ent">pause</span>: <span class="pl-c1">0.8</span>
      - <span class="pl-ent">click</span>: <span class="pl-s"><span class="pl-pds">"</span>.row-edit-save<span class="pl-pds">"</span></span>
      - <span class="pl-ent">wait_for</span>: <span class="pl-s"><span class="pl-pds">"</span>text=Previewing 3 rows.<span class="pl-pds">"</span></span>
      - <span class="pl-ent">pause</span>: <span class="pl-c1">1.2</span>
      - <span class="pl-ent">click</span>: <span class="pl-s"><span class="pl-pds">"</span>.row-edit-save<span class="pl-pds">"</span></span>
      - <span class="pl-ent">wait_for</span>: <span class="pl-s"><span class="pl-pds">"</span>text=3 rows inserted.<span class="pl-pds">"</span></span>
      - <span class="pl-ent">pause</span>: <span class="pl-c1">1.0</span>
      - <span class="pl-ent">click</span>: <span class="pl-s"><span class="pl-pds">"</span>.row-edit-cancel<span class="pl-pds">"</span></span>
      - <span class="pl-ent">wait_for</span>: <span class="pl-s"><span class="pl-pds">"</span>text=Prepare release video<span class="pl-pds">"</span></span>
      - <span class="pl-ent">pause</span>: <span class="pl-c1">1.0</span>
  - <span class="pl-ent">name</span>: <span class="pl-s">Create a table from pasted CSV</span>
    <span class="pl-ent">open</span>: <span class="pl-s">http://127.0.0.1:6419/demo</span>
    <span class="pl-ent">wait_for</span>: <span class="pl-s"><span class="pl-pds">'</span>details.actions-menu-links summary<span class="pl-pds">'</span></span>
    <span class="pl-ent">do</span>:
      - <span class="pl-ent">pause</span>: <span class="pl-c1">0.8</span>
      - <span class="pl-ent">click</span>: <span class="pl-s"><span class="pl-pds">'</span>details.actions-menu-links summary<span class="pl-pds">'</span></span>
      - <span class="pl-ent">click</span>: <span class="pl-s"><span class="pl-pds">'</span>button[data-database-action="create-table"]<span class="pl-pds">'</span></span>
      - <span class="pl-ent">wait_for</span>: <span class="pl-s"><span class="pl-pds">"</span>#table-create-dialog[open]<span class="pl-pds">"</span></span>
      - <span class="pl-ent">pause</span>: <span class="pl-c1">0.5</span>
      - <span class="pl-ent">fill</span>:
          <span class="pl-ent">into</span>: <span class="pl-s"><span class="pl-pds">"</span>.table-create-table-name<span class="pl-pds">"</span></span>
          <span class="pl-ent">text</span>: <span class="pl-s"><span class="pl-pds">"</span>launch_metrics<span class="pl-pds">"</span></span>
      - <span class="pl-ent">click</span>: <span class="pl-s"><span class="pl-pds">"</span>.table-create-from-data<span class="pl-pds">"</span></span>
      - <span class="pl-ent">wait_for</span>: <span class="pl-s"><span class="pl-pds">"</span>.table-create-data-textarea<span class="pl-pds">"</span></span>
      - <span class="pl-ent">pause</span>: <span class="pl-c1">0.5</span>
      - <span class="pl-ent">fill</span>:
          <span class="pl-ent">into</span>: <span class="pl-s"><span class="pl-pds">"</span>.table-create-data-textarea<span class="pl-pds">"</span></span>
          <span class="pl-ent">text</span>: <span class="pl-s">|</span>
<span class="pl-s">            metric_id,name,score,recorded_on</span>
<span class="pl-s">            m001,Activation rate,87.5,2026-06-29</span>
<span class="pl-s">            m002,Retention check,72.25,2026-06-30</span>
<span class="pl-s">            m003,CSV import health,95,2026-07-01</span>
<span class="pl-s"></span>      - <span class="pl-ent">pause</span>: <span class="pl-c1">0.8</span>
      - <span class="pl-ent">click</span>: <span class="pl-s"><span class="pl-pds">"</span>.table-create-save<span class="pl-pds">"</span></span>
      - <span class="pl-ent">wait_for</span>: <span class="pl-s"><span class="pl-pds">"</span>text=Previewing 3 rows.<span class="pl-pds">"</span></span>
      - <span class="pl-ent">pause</span>: <span class="pl-c1">1.2</span>
      - <span class="pl-ent">click</span>: <span class="pl-s"><span class="pl-pds">"</span>.table-create-save<span class="pl-pds">"</span></span>
      - <span class="pl-ent">wait_for_url</span>: <span class="pl-s"><span class="pl-pds">"</span>**/demo/launch_metrics<span class="pl-pds">"</span></span>
      - <span class="pl-ent">wait_for</span>: <span class="pl-s"><span class="pl-pds">"</span>text=Activation rate<span class="pl-pds">"</span></span>
      - <span class="pl-ent">pause</span>: <span class="pl-c1">1.2</span></pre></div>
<p>The <a href="https://shot-scraper.datasette.io/en/stable/video.html">video command documentation</a> includes simpler examples, but for the purpose of this post I thought I'd go with something more comprehensive.</p>
<p>That demo YAML storyboard was constructed entirely by GPT-5.5 xhigh running in Codex Desktop, using the following prompt run inside my <code>~/dev/datasette</code> checkout of <a href="https://github.com/simonw/datasette/commits/b759ea548606bc9bf9a4bf0e33e2d57ead7e0ab8/">this branch</a>:</p>
<blockquote>
<p><code>Review the changes on this branch.</code></p>
<p><code>cd to ~/dev/shot-scraper and run the command "uv run shot-scraper video --help"</code></p>
<p><code>Now use that new video command to record a video demo of the new features from this branch, including running a "uv run datasette -p 6419 --root --secret 1 /tmp/demo.db" development server so you can record the video against a demo DB that you first create.</code></p>
</blockquote>
<p>Now that I've released the feature the prompt could say "<code>run uvx shot-scraper video --help</code>" instead and it should achieve the same result.</p>
<p>I really like this pattern where the <code>--help</code> output for a command provides enough detail that a coding agent can use it - it works kind of like bundling a <code>SKILL.md</code> file directly inside the tool. I used the same pattern for <a href="https://simonwillison.net/2026/Feb/10/showboat-and-rodney/">showboat and rodney</a>.</p>
<h4 id="how-i-built-this">How I built this</h4>
<p><code>shot-scraper video</code> started as an experimental prototype. <code>shot-scraper</code> is built on top of <a href="https://playwright.dev/">Playwright</a>, and the key feature it needed was for Playwright to be able to record video of browser sessions with enough control to create the desired demo.</p>
<p>I first tried this a few years ago and found that the Playwright-produced videos included additional chrome that was useful for debugging a test failure but unwanted for a product demo.</p>
<p>They fixed that a while ago, but there were still some minor blockers. In particular I was getting <a href="https://github.com/simonw/shot-scraper/pull/194/changes/c2f3b3a52ba84f2adcf3ad6da4d39c2570328584#issuecomment-4724459369">a few white frames at the start of the videos</a>, since the recording mechanism kicked in before the first URL was loaded by the browser.</p>
<p>Playwright 1.59 added a new <a href="https://playwright.dev/python/docs/api/class-screencast">screencast mechanism</a> providing much more finely grained control over video recording. This was very nearly what I needed, but the resulting videos were fixed at 800px wide.</p>
<p>I found a <a href="https://github.com/microsoft/playwright/pull/41183">landed PR fixing that</a> but it wasn't yet in a release. Then yesterday they shipped it in <a href="https://github.com/microsoft/playwright-python/releases/tag/v1.61.0">playwright-python 1.61.0</a> and I was finally unblocked to finish implementing the feature!</p>
<p>The code itself was all written by GPT-5.5 xhigh in Codex Desktop. I had it write the documentation as well which gave me a very useful frame for reviewing the design - much of the iteration on the feature came from reviewing that documentation, spotting things that were redundant, inconsistent or confusing, and requesting (or dictating) a better design.</p>
<p>The YAML format itself was mostly defined by the coding agent. I had it <a href="https://github.com/simonw/shot-scraper/blob/1.10/shot_scraper/video.py#L24">use Pydantic</a> to both define and validate the format, partly to make the design easier to review.</p>
<p>This is a great example of the kind of feature that I almost certainly wouldn't have taken on without coding agent support. I filed the <a href="https://github.com/simonw/shot-scraper/issues/142">original issue</a> in February 2024, and had difficulty finding the necessary time to solve this in amongst all of my other projects.</p>
    
        <p>Tags: <a href="https://simonwillison.net/tags/projects">projects</a>, <a href="https://simonwillison.net/tags/python">python</a>, <a href="https://simonwillison.net/tags/yaml">yaml</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/playwright">playwright</a>, <a href="https://simonwillison.net/tags/shot-scraper">shot-scraper</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/pydantic">pydantic</a>, <a href="https://simonwillison.net/tags/coding-agents">coding-agents</a>, <a href="https://simonwillison.net/tags/agentic-engineering">agentic-engineering</a></p>
