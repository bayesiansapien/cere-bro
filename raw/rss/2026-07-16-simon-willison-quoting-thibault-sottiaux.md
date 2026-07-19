---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-19T22:17:42.121346+00:00
title: Quoting Thibault Sottiaux
url: https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything
published: 2026-07-16
---

# Quoting Thibault Sottiaux

<blockquote cite="https://twitter.com/thsottiaux/status/2077630111499882637"><p>On file deletions. We’ve investigated a handful of reports where GPT-5.6 unexpectedly deleted files. </p>
<p>What we have  found is that this most commonly occurs when:</p>
<ul>
<li>Full access mode is enabled and codex is run without sandboxing protections, including without auto review being enabled</li>
<li>The model attempts  to override the $HOME env var to define a temporary directory.</li>
<li>The model makes an honest mistake and mistakenly deletes $HOME instead.</li>
</ul></blockquote>
<p class="cite">&mdash; <a href="https://twitter.com/thsottiaux/status/2077630111499882637">Thibault Sottiaux</a>, describing a pretty gnarly Codex bug</p>

    <p>Tags: <a href="https://simonwillison.net/tags/codex">codex</a>, <a href="https://simonwillison.net/tags/coding-agents">coding-agents</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a></p>
