---
source: farmer/rss
feed: simon-willison
farmed: 2026-10-09T06:21:49.945919+00:00
title: "ttok 0.4"
url: https://simonwillison.net/2026/Oct/8/ttok/
published: 2026-10-08
author: 
---

# ttok 0.4

<p><strong>Release:</strong> <a href="https://github.com/simonw/ttok/releases/tag/0.4">ttok 0.4</a></p>
        <p><code>ttok</code> is my CLI tool for counting tokens, using OpenAI's open source <a href="https://github.com/openai/tiktoken">tiktoken</a> library.</p>
<p>It hasn't been in updated in a couple of years, but I finally fixed a Click warning, updated CI, and added a <code>--list-models</code> command to list available models.</p>
<p>It works with <code>uvx</code>, so you can count tokens in anything like this:</p>
<pre><code>cat file.txt | uvx ttok
</code></pre>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/projects">projects</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/openai">openai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/tokenization">tokenization</a></p>
