---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-31T09:24:57.586193+00:00
title: How we contain Claude across products
url: https://simonwillison.net/2026/May/30/how-we-contain-claude/#atom-everything
published: 2026-05-30
author: Simon Willison
---

# How we contain Claude across products

<p><strong><a href="https://www.anthropic.com/engineering/how-we-contain-claude">How we contain Claude across products</a></strong></p>
A complaint I often have about sandboxing products is that they are rarely thoroughly <em>documented</em>, and in the absence of detailed documentation it's hard to know how much I can trust them.</p>
<p>Anthropic just published a fantastic overview of how their various sandbox techniques work across <a href="https://claude.ai/">Claude.ai</a>, Claude Code, and Cowork.</p>
<blockquote>
<p>We constrain where and how an agent can act with process sandboxes, VMs, filesystem boundaries, and egress controls. The goal is to set a hard boundary on what an agent can reach. For example, if credentials never enter the sandbox, they can't be exfiltrated, regardless of whether the cause is a user, a model finding a “creative” path, or an attacker.</p>
</blockquote>
<p>Claude.ai uses gVisor. Claude Code, run locally, uses Seatbelt on macOS and Bubblewrap on Linux. Claude Cowork runs a full VM (Apple's Virtualization framework on macOS, HCS on Windows).</p>
<p>There's a lot in here, including some interesting stories of risks they missed such as the <code>api.anthropic.com/v1/files</code> exfiltration vector <a href="https://simonwillison.net/2026/Jan/14/claude-cowork-exfiltrates-files/">covered here previously</a>.</p>
<p>This reminded me it's time I took another look at Anthropic's open source <a href="https://github.com/anthropic-experimental/sandbox-runtime">srt (Anthropic Sandbox Runtime)</a> tool - it's mature enough know that I'm ready to give it a proper go.


    <p>Tags: <a href="https://simonwillison.net/tags/sandboxing">sandboxing</a>, <a href="https://simonwillison.net/tags/security">security</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/anthropic">anthropic</a>, <a href="https://simonwillison.net/tags/claude">claude</a>, <a href="https://simonwillison.net/tags/claude-code">claude-code</a></p>
