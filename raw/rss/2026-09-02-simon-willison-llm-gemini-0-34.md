---
source: farmer/rss
feed: simon-willison
farmed: 2026-09-03T11:32:34.863388+00:00
title: llm-gemini 0.34
url: https://simonwillison.net/2026/Sep/2/llm-gemini/
published: 2026-09-02
author: 
---

# llm-gemini 0.34

<p><strong>Release:</strong> <a href="https://github.com/simonw/llm-gemini/releases/tag/0.34">llm-gemini 0.34</a></p>
        <blockquote>
<ul>
<li>New model <code>gemini-3.8-flash</code> for <a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/">Gemini 3.8 Flash</a>, with low, medium and high thinking levels. <a href="https://github.com/simonw/llm-gemini/issues/146">#146</a></li>
<li>Fixed async responses failing to record the resolved model version. Thanks, <a href="https://github.com/c-tonneslan">Charlie Tonneslan</a>. <a href="https://github.com/simonw/llm-gemini/pull/137">#137</a></li>
</ul>
</blockquote>
<p>Google released <a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/">Gemini 3.8 Flash</a> (and 3.8 Flash Cyber, but that's available to "trusted defenders" only) today.</p>
<p>Here are <a href="https://tools.simonwillison.net/markdown-svg-renderer?url=https%3A%2F%2Fgist.github.com%2Fsimonw%2Ff8820ce47db87490734117e9be4984c3">the pelicans</a> for high, medium, and low. This is high:</p>
<p><img alt="Description by Gemini 3.8 Flash: Digital illustration of a cartoon pelican wearing a red and white polka-dot scarf riding a teal cruiser bicycle along a wooden boardwalk by the beach, with a small blue fish in the front basket and a glowing sun over the ocean." src="https://static.simonwillison.net/static/2026-09-02/image.jpg" /></p>
<p>For comparison, here are the same pelicans <a href="https://tools.simonwillison.net/markdown-svg-renderer.html?url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F6779a22d5e7bb6bdf29936f1600a5259">generated using Gemini 3.7 Flash</a>.</p>
<p>Something I appreciate about Gemini Flash is that it's fast, cheap, and competent at things like HTML and JavaScript. I was messing around with it and prompted "make me a cool thing in html" and <a href="https://tools.simonwillison.net/markdown-svg-renderer?url=https%3A%2F%2Fgist.github.com%2Fsimonw%2Fb6149a49d327164d67d62c3d12992e48#how-to-use-it">it built this</a>, which is certainly a cool thing in HTML! Took 13 seconds, cost 1.8 cents.</p>
<p><video controls="controls" height="370" poster="https://static.simonwillison.net/static/2026/cosmic-gemma.jpg" preload="none" style="display: block; width: 100%; height: auto;" width="854">
    <source src="https://static.simonwillison.net/static/2026/cosmic-gemma.mp4" type="video/mp4" />
    Your browser does not support HTML5 video.
  </video>
</p>

<p>If you click through to <a href="https://tools.simonwillison.net/markdown-svg-renderer?url=https%3A%2F%2Fgist.github.com%2Fsimonw%2Fb6149a49d327164d67d62c3d12992e48#how-to-use-it">the demo</a> you'll see one more thing I built with Gemini 3.8 Flash.</p>
<p>My <a href="https://tools.simonwillison.net/markdown-svg-renderer">markdown-svg-renderer tool</a> lets me feed in the URL to a Gist with Markdown in and renders that markdown with fenced code blocks for SVG correctly rendered.</p>
<p>I used Gemini 3.8 Flash (with my <em>very</em> basic <a href="https://github.com/simonw/llm-coding-agent">llm-coding-agent</a> coding agent plugin) to add support for HTML as well, so now any HTML blocks in the Markdown are rendered using a sandboxed iframe. <a href="https://gist.github.com/simonw/3e36b98292dfdc1b3baff158faa743f7">Here's the transcript</a>.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/llm">llm</a>, <a href="https://simonwillison.net/tags/gemini">gemini</a>, <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle">pelican-riding-a-bicycle</a>, <a href="https://simonwillison.net/tags/llm-release">llm-release</a></p>
