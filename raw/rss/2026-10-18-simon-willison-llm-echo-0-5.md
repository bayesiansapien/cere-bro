---
source: farmer/rss
feed: simon-willison
farmed: 2026-10-19T09:35:55.718862+00:00
title: "llm-echo 0.5"
url: https://simonwillison.net/2026/Oct/18/llm-echo/
published: 2026-10-18
author: 
---

# llm-echo 0.5

<p><strong>Release:</strong> <a href="https://github.com/simonw/llm-echo/releases/tag/0.5">llm-echo 0.5</a></p>
        <p>I'm working towards a new <a href="https://llm.datasette.io/">LLM</a> release, and testing PRs caused me to revisit the <code>llm-echo</code> debug plugin. This plugin provides a "model" which doesn't involve an LLM at all - it just repeats back the prompts that have been fed to it. The new release now updates the simulated token usage counts to take tool calls, system prompts, and reasoning tokens into account.</p>
<p>Example usage:</p>
<pre><code>uvx --with llm-echo llm -m echo 'hi there' -o thinking 1 --usage
</code></pre>
<p>Outputs:</p>
<pre><code>First I consider the prompt, then I decide what to say.
{
  "prompt": "hi there",
  "system": "",
  "attachments": [],
  "stream": true,
  "previous": []
}
Token usage: 2 input, 24 output
</code></pre>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/llm">llm</a></p>
