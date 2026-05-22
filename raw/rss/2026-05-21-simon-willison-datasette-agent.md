---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-22T10:11:42.649379+00:00
title: Datasette Agent
url: https://simonwillison.net/2026/May/21/datasette-agent/#atom-everything
published: 2026-05-21
author: 
---

# Datasette Agent

<p>We just <a href="https://datasette.io/blog/2026/datasette-agent/">announced the first release of Datasette Agent</a>, a new extensible AI assistant for Datasette. I've been working on my <a href="https://llm.datasette.io/">LLM</a> Python library for just over three years now, and Datasette Agent represents the moment that LLM and <a href="https://datasette.io/">Datasette</a> finally come together. I'm really excited about it!</p>
<p>Datasette Agent provides a conversational interface for asking questions of the data you have stored in Datasette. Add the <a href="https://github.com/datasette/datasette-agent-charts">datasette-agent-charts</a> plugin and it can generate charts of your data as well.</p>
<h4 id="the-demo">The demo</h4>
<p>The <a href="https://simonwillison.net/atom/everything/">announcement post</a> (on the new Datasette project blog) includes this <a href="https://www.youtube.com/watch?v=AFZKp6hbFjI">demo video</a>:</p>

 


<p>I recorded the video against the new <a href="https://agent.datasette.io/">agent.datasette.io</a> live demo instance, which runs Datasette Agent against example databases including the classic <a href="https://datasette.io/global-power-plants">global-power-plants</a> by <a href="https://www.wri.org/research/global-database-power-plants">WRI</a>, and a copy of the <a href="https://datasette.simonwillison.net/">Datasette backup</a> of my blog.</p>
<p>The live demo runs on <a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite">Gemini 3.1 Flash-Lite</a> - it's cheap, fast and has no trouble writing SQLite queries.</p>
<p>A question I asked in the demo was:</p>
<blockquote>
<p>when did Simon most recently see a pelican?</p>
</blockquote>
<p>Which ran <a href="https://datasette.simonwillison.net/simonwillisonblog?sql=SELECT+title%2C+commentary%2C+created+FROM+blog_beat+WHERE+beat_type+%3D+%27sighting%27+AND+%28title+LIKE+%27%25pelican%25%27+OR+commentary+LIKE+%27%25pelican%25%27%29+ORDER+BY+created+DESC+LIMIT+5">this SQL query</a>:</p>
<div class="highlight highlight-source-sql"><pre><span class="pl-k">SELECT</span>
  title, commentary, created
<span class="pl-k">FROM</span>
  blog_beat
<span class="pl-k">WHERE</span>
  beat_type <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">'</span>sighting<span class="pl-pds">'</span></span>
  <span class="pl-k">AND</span> (title <span class="pl-k">LIKE</span> <span class="pl-s"><span class="pl-pds">'</span>%pelican%<span class="pl-pds">'</span></span> <span class="pl-k">OR</span> commentary <span class="pl-k">LIKE</span> <span class="pl-s"><span class="pl-pds">'</span>%pelican%<span class="pl-pds">'</span></span>)
<span class="pl-k">ORDER BY</span>
  created <span class="pl-k">DESC</span>
<span class="pl-k">LIMIT</span>
  <span class="pl-c1">5</span></pre></div>
<p>And replied:</p>
<blockquote>
<p>The most recent sighting of a pelican by Simon was recorded on <strong>May 20, 2026</strong>.</p>
<p>The observation included a California Brown Pelican, along with a Common Loon, Canada Goose, Striped Shore Crab, and a California Sea Lion.</p>
</blockquote>
<p>Here's <a href="https://simonwillison.net/2026/May/20/sighting-363395265/">that sighting on my blog</a>, and the <a href="https://gist.github.com/simonw/a46d17b69659a4866adb1d868280091d">Markdown export</a> of the full conversation transcript.</p>
<h4 id="the-plugins">The plugins</h4>
<p>My favorite feature of Datasette Agent is that, like the rest of Datasette, it's extensible using plugins.</p>
<p>We've shipped three plugins so far:</p>
<ul>
<li>
<a href="https://github.com/datasette/datasette-agent-charts">datasette-agent-charts</a>, shown in the video, adds charts to Datasette Agent, powered by <a href="https://observablehq.com/plot/">Observable Plot</a>.</li>
<li>
<a href="https://github.com/datasette/datasette-agent-openai-imagegen">datasette-agent-openai-imagegen</a> adds an image generation tool to Datasette Agent using <a href="https://openai.com/index/introducing-chatgpt-images-2-0/">ChatGPT Images 2.0</a>.</li>
<li>
<a href="https://github.com/datasette/datasette-agent-sprites">datasette-agent-sprites</a> provides tools for executing code in a <a href="https://sprites.dev/">Fly Sprites</a> persistent sandbox.</li>
</ul>
<p>Building plugins is <em>really fun</em>. I have a bunch more prototypes that aren't quite alpha-quality yet.</p>
<p>Claude Code and OpenAI Codex are both proving excellent at writing plugins - just point them at a checkout of the <a href="https://github.com/datasette/datasette-agent">datasette-agent repo</a> for reference and tell them what you want to build!</p>
<h4 id="running-it-against-local-models">Running it against local models</h4>
<p>I've also been having fun running the new plugin against local models. Here's a <code>uv</code> one-liner to run the plugin against <a href="https://huggingface.co/google/gemma-4-26B-A4B">gemma-4-26b-a4b</a> in <a href="https://lmstudio.ai">LM Studio</a> on a Mac:</p>
<div class="highlight highlight-source-shell"><pre>uvx --prerelease=allow \
  --with datasette-agent --with llm-lmstudio \
  datasette --internal internal.db --root \
  -s plugins.datasette-llm.default_model lmstudio/google/gemma-4-26b-a4b \
  data.db</pre></div>
<p>Datasette Agent needs reliable tool calls and the ability for a model to produce SQL queries that run against SQLite. The open weight models released in the past six months are increasingly able to handle that.</p>
<h4 id="what-s-next">What's next</h4>
<p>Datasette Agent opens up <em>so many</em> opportunities for the LLM and Datasette ecosystem in general.</p>
<p>It's already informed <a href="https://simonwillison.net/2026/Apr/29/llm/">the major LLM 0.32a0 refactor</a> which I'm nearly ready to roll into a stable release, maybe with some additional "LLM agent" abstractions extracte from Datasette Agent itself.</p>
<p>I've been exploring my own take on the Claude Artifacts, which is shaping up nicely as a plugin.</p>
<p>I'm excited to use Datasette Agent to build my own <a href="https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.013.jpeg">Claw</a> - a personal AI assistant built around data imported from different parts of my digital life, which is a neat excuse to revisit my older <a href="https://dogsheep.github.io">Dogsheep</a> family of tools.</p>
<p>We'll also be rolling out Datasette Agent for users of <a href="https://datasette.cloud/">Datasette Cloud</a>.</p>
<p>Join our <a href="https://discord.gg/hdxyusUFv">#datasette-agent Discord channel</a> if you'd like to talk about the project.</p>
    
        <p>Tags: <a href="https://simonwillison.net/tags/projects">projects</a>, <a href="https://simonwillison.net/tags/sqlite">sqlite</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/llm">llm</a>, <a href="https://simonwillison.net/tags/uv">uv</a>, <a href="https://simonwillison.net/tags/datasette-agent">datasette-agent</a></p>
