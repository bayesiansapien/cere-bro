---
source: farmer/rss
feed: simon-willison
farmed: 2026-09-21T05:24:13.161313+00:00
title: llm-keys-ui 0.1
url: https://simonwillison.net/2026/Sep/20/llm-keys-ui/
published: 2026-09-20
---

# llm-keys-ui 0.1

<p><strong>Release:</strong> <a href="https://github.com/simonw/llm-keys-ui/releases/tag/0.1">llm-keys-ui 0.1</a></p>
        <p>This plugin solves a very specific problem.</p>
<p>I've started using <a href="https://learn.chatgpt.com/docs/remote">Codex Remote</a> to run coding agents on various machines while controlling them from my phone. </p>
<p>Sometimes I use those machines to hack on LLM projects, and occasionally that means I need to configure an API key.</p>
<p>I don't like pasting API keys into agent sessions, so I wanted a way to get those keys onto a machine without pasting them into the ChatGPT app directly.</p>
<p>With this plugin, I can tell Codex to run:</p>
<pre><code>uvx --with llm-keys-ui llm keys-ui --all
</code></pre>
<p>Then have it tell me the URL - including local network or Tailscale device IPs - for an interface to save additional API keys.</p>
<p>Then later it can use a command like <code>llm keys get anthropic</code> as part of a shell command when it needs to use a key.</p>
<div>
  <img alt="Chat conversation requesting uvx --with llm-keys-ui llm keys-ui --all, with a response listing four server URLs on port 8010 and confirming the server is still running." src="https://static.simonwillison.net/static/2026-09-20/IMG_8166.jpeg" style="display: block; width: 100%; height: auto;" />
  <img alt="LLM keys web interface listing anthropic, openai, openrouter, and qwen-dummy as stored keys, with a form containing Key name and New value fields and a Save key button. Existing key values are never displayed." src="https://static.simonwillison.net/static/2026-09-20/IMG_8167.jpeg" style="display: block; width: 100%; height: auto;" />
</div>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/llm">llm</a>, <a href="https://simonwillison.net/tags/coding-agents">coding-agents</a>, <a href="https://simonwillison.net/tags/codex">codex</a></p>
