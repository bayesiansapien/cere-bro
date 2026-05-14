---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-14T03:50:13.323453+00:00
title: llm 0.32a2
url: https://simonwillison.net/2026/May/12/llm/#atom-everything
published: 2026-05-12
author: 
---

# llm 0.32a2

<p><strong>Release:</strong> <a href="https://github.com/simonw/llm/releases/tag/0.32a2">llm 0.32a2</a></p>
        <p>A bunch of useful stuff in this <a href="https://llm.datasette.io/">LLM</a> alpha, but the most important detail is this one:</p>
<blockquote>
<p>Most reasoning-capable OpenAI models now use the <a href="https://platform.openai.com/docs/api-reference/responses"><code>/v1/responses</code></a> endpoint instead of <code>/v1/chat/completions</code>. This enables interleaved reasoning across tool calls for GPT-5 class models. <a href="https://github.com/simonw/llm/pull/1435">#1435</a></p>
</blockquote>
<p>This means you can now see the summarized reasoning tokens when you run prompts against an OpenAI model, displayed in a different color to standard error. Use the <code>-R</code> or <code>--hide-reasoning</code> flags if you don't want to see that.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/llm">llm</a>, <a href="https://simonwillison.net/tags/projects">projects</a>, <a href="https://simonwillison.net/tags/openai">openai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/annotated-release-notes">annotated-release-notes</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a></p>
