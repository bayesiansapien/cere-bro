---
source: farmer/rss
feed: simon-willison
farmed: 2026-08-25T14:24:43.464848+05:30
title: llm 0.33
url: https://simonwillison.net/2026/Aug/22/llm/
published: 2026-08-22
---

# llm 0.33

<p><strong>Release:</strong> <a href="https://github.com/simonw/llm/releases/tag/0.33">llm 0.33</a></p>
        <p>My highlights from this release:</p>
<blockquote>
<ul>
<li>Upgraded to the OpenAI Python library 3.x and switched the HTTP client dependency from <code>httpx</code> to <code>httpx2</code>. <a href="https://github.com/simonw/llm/issues/1608">#1608</a>, <a href="https://github.com/simonw/llm/pull/1631">#1631</a></li>
</ul>
</blockquote>
<p>I shipped a quick <a href="https://simonwillison.net/2026/Aug/21/llm/">0.32.1 fix</a> for this yesterday, but this is the more comprehensive fix.</p>
<blockquote>
<ul>
<li><code>llm embed</code> and <code>llm embed-multi</code> now accept <code>--key</code>. The Python <code>EmbeddingModel.embed()</code>, <code>EmbeddingModel.embed_multi()</code>, <code>Collection.embed()</code> and <code>Collection.embed_multi()</code> methods accept <code>key=</code> too, passing the resolved per-call key to embedding plugins without changing shared model state. Existing plugins that read <code>self.key</code> continue to work through a compatibility fallback. Thanks, <a href="https://github.com/ChrisJr404">ChrisJr404</a>. <a href="https://github.com/simonw/llm/issues/757">#757</a>, <a href="https://github.com/simonw/llm/pull/1620">#1620</a></li>
</ul>
</blockquote>
<p>The embedding models now use the same pattern for keys that regular LLM models do.</p>
<blockquote>
<ul>
<li><code>llm prompt -t/--template</code> can now be repeated to combine templates in order. This allows model configuration and options from one template to be used with a prompt from another.</li>
</ul>
</blockquote>
<p>This unlocks a neat pattern where you can create templates that package a model with a set of default options:</p>
<pre><code>llm -m gpt-5.6-luna -o reasoning_effort high --save lhigh
llm "Generate an SVG of a pelican riding a bicycle" --save pelican
# Combine and run the templates
llm -t lhigh -t pelican
</code></pre>
<blockquote>
<ul>
<li>Reasoning-capable Responses API models now support a <code>reasoning_summary</code> option with <code>auto</code>, <code>concise</code>, and <code>detailed</code> values. This can be used with <a href="https://llm.datasette.io/en/stable/other-models.html#openai-endpoint">llm openai endpoint --responses</a>. <a href="https://github.com/simonw/llm/issues/1600">#1600</a></li>
</ul>
</blockquote>
<p>This is particularly useful for exercising different models that provide their own imitation of the OpenAI Responses API.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/annotated-release-notes">annotated-release-notes</a>, <a href="https://simonwillison.net/tags/llm">llm</a></p>
