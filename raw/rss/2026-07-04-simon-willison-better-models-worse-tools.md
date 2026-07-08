---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-08T05:20:41Z
title: Better Models: Worse Tools
url: https://simonwillison.net/2026/Jul/4/better-models-worse-tools/#atom-everything
published: 2026-07-04
author: 
---

# Better Models: Worse Tools

<p><strong><a href="https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/">Better Models: Worse Tools</a></strong></p>
Armin reports on a weird problem he ran into while hacking on Pi:</p>
<blockquote>
<p>The short version is that newer Claude models sometimes call Pi’s edit tool with extra, invented fields in the nested <code>edits[]</code> array. And not Haiku or some small model: Opus 4.8. The edit itself is usually correct but the arguments do not match the schema as the model invents made-up keys and Pi thus rejects the tool call and asks to try again.</p>
<p>That alone is not too surprising as models emit malformed tool calls sometimes. Particularly small ones. What surprised me is that this is getting worse with newer Anthropic models as both Opus 4.8 and Sonnet 5 show it but none of the older models. In other words, the SOTA models of the family are worse at this specific tool schema than their older siblings.</p>
</blockquote>
<p>Armin theorizes that this is because more recent Anthropic models have been specifically trained (presumably via Reinforcement Learning) to better use the edit tools that are baked into Claude Code. This has the unfortunate effect that other coding harnesses, such as Pi, may find that their own custom edit tools are more likely to be used incorrectly.</p>
<p>Claude's edit tool <a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool#str-replace">uses search and replace</a>. OpenAI's Codex <a href="https://developers.openai.com/api/docs/guides/tools-apply-patch">uses an apply_patch mechanism instead</a>, and OpenAI have talked in the past about how their models are trained to use that tool effectively.</p>
<p>Does this mean third-party coding harnesses like Pi should implement multiple edit tools just so they can use the one with the best performance for the underlying model the user has selected?


    <p>Tags: <a href="https://simonwillison.net/tags/armin-ronacher">armin-ronacher</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/openai">openai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/anthropic">anthropic</a>, <a href="https://simonwillison.net/tags/llm-tool-use">llm-tool-use</a>, <a href="https://simonwillison.net/tags/coding-agents">coding-agents</a>, <a href="https://simonwillison.net/tags/pi">pi</a></p>
