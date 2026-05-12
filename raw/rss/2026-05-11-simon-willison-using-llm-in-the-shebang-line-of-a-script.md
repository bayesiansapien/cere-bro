---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-12T03:32:06.514886+00:00
title: Using LLM in the shebang line of a script
url: https://simonwillison.net/2026/May/11/llm-shebang/#atom-everything
published: 2026-05-11
author: 
---

# Using LLM in the shebang line of a script

<p><strong>TIL:</strong> <a href="https://til.simonwillison.net/llms/llm-shebang">Using LLM in the shebang line of a script</a></p>
        <p>Kim_Bruning <a href="https://news.ycombinator.com/item?id=48073246#48090590">on Hacker News</a>:</p>
<blockquote>
<p>But seriously, you can put a shebang on an english text file now (if you're sufficiently brave) [...]</p>
</blockquote>
<p>This inspired me to look at patterns for doing exactly that with <a href="https://llm.datasette.io/en/stable/">LLM</a>. Here's the simplest, which takes advantage of <a href="https://llm.datasette.io/en/stable/fragments.html">LLM fragments</a>:</p>
<pre><code>#!/usr/bin/env -S llm -f
Generate an SVG of a pelican riding a bicycle
</code></pre>
<p>But you can also incorporate <a href="https://llm.datasette.io/en/stable/tools.html">tool calls</a> using the <code>-T name_of_tool</code> option:</p>
<pre><code>#!/usr/bin/env -S llm -T llm_time -f
Write a haiku that mentions the exact current time
</code></pre>
<p>Or even execute YAML templates directly that define extra tools as Python functions:</p>
<pre><span class="pl-c"><span class="pl-c">#</span>!/usr/bin/env -S llm -t</span>
<span class="pl-ent">model</span>: <span class="pl-s">gpt-5.4-mini</span>
<span class="pl-ent">system</span>: <span class="pl-s">|</span>
<span class="pl-s">  Use tools to run calculations</span>
<span class="pl-s"></span><span class="pl-ent">functions</span>: <span class="pl-s">|</span>
<span class="pl-s">  def add(a: int, b: int) -&gt; int:</span>
<span class="pl-s">      return a + b</span>
<span class="pl-s">  def multiply(a: int, b: int) -&gt; int:</span>
<span class="pl-s">      return a * b</span></pre>

<p>Then:</p>
<pre><code>./calc.sh 'what is 2344 * 5252 + 134' --td
</code></pre>
<p>Which outputs (thanks to that <code>--td</code> tools debug option):</p>
<pre><code>Tool call: multiply({'a': 2344, 'b': 5252})
  12310688

Tool call: add({'a': 12310688, 'b': 134})
  12310822

2344 × 5252 + 134 = **12,310,822**
</code></pre>
<p>Read the full TIL for <a href="https://til.simonwillison.net/llms/llm-shebang#templates-with-tools">a more complex example</a> that uses the Datasette SQL API to answer questions about content on my blog.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/llm">llm</a>, <a href="https://simonwillison.net/tags/llm-tool-use">llm-tool-use</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a></p>
