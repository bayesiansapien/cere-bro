---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-08T05:20:41Z
title: What's new in Claude Sonnet 5
url: https://simonwillison.net/2026/Jun/30/claude-sonnet-5/#atom-everything
published: 2026-06-30
author: 
---

# What's new in Claude Sonnet 5

<p><strong><a href="https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5">What&#x27;s new in Claude Sonnet 5</a></strong></p>
Claude Sonnet 5 came out <a href="https://www.anthropic.com/news/claude-sonnet-5">this morning</a>. I always head straight for the "what's new" developer docs because they tend to have more actionable information than the official announcement post.</p>
<p>Anthropic say of Sonnet 5 that "its performance is close to that of Opus 4.8, but at lower prices". The <a href="https://www-cdn.anthropic.com/9e6a1044980d8c4ed85669faf9c2a8342e2e9f1e/Claude%20Sonnet%205%20System%20Card.pdf">system card</a> helps explain how they were able to release the model without being blocked by the US government:</p>
<blockquote>
<p>Sonnet 5 is significantly less capable at cyber tasks than Mythos 5: its safeguards are thus similar to those we apply to Opus 4.7 and Opus 4.8 (models that are more capable than Sonnet 5 but much less capable than Mythos 5).</p>
</blockquote>
<p>Of note from the "what's new" API changes:</p>
<ul>
<li>Sampling parameters <code>temperature</code>, <code>top_p</code>, <code>top_k</code> are no longer supported.</li>
<li>It has a 1 million token context window and 128,000 maximum output tokens.</li>
<li>It features "the same set of tools and platform features as Claude Sonnet 4.6"</li>
<li>Adaptive thinking is on by default, unless you specify <code>"thinking": {type: "disabled"}</code>.</li>
<li>The pricing is the same as Sonnet 4.6: $3/million input, $15/million input, with an introductory discount to $2/$10 until 31st August. But...</li>
<li>The model has a new tokenizer, where "The same input text produces approximately 30% more tokens than on Claude Sonnet 4.6." - effectively a 30% price increase.</li>
</ul>
<p>I used my <a href="https://tools.simonwillison.net/claude-token-counter">Claude Token Counter</a> tool to try out the new tokenizer. Here are my results for several larger documents:</p>
<table>
  <thead>
    <tr>
      <th>Document</th>
      <th>Sonnet 4.6</th>
      <th>Opus 4.7</th>
      <th>Sonnet 5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://github.com/simonw/udhr-markdown/blob/main/declarations/eng.md">Universal Declaration of Human Rights (English)</a></td>
      <td><b>2,356</b></td>
      <td><b>3,347</b><br />1.42x</td>
      <td><b>3,341</b><br />1.42x</td>
    </tr>
    <tr>
      <td><a href="https://github.com/simonw/udhr-markdown/blob/main/declarations/spa.md">Universal Declaration of Human Rights (Spanish)</a></td>
      <td><b>3,572</b></td>
      <td><b>4,753</b><br />1.33x</td>
      <td><b>4,747</b><br />1.33x</td>
    </tr>
    <tr>
      <td><a href="https://github.com/simonw/udhr-markdown/blob/main/declarations/cmn_hans.md">Universal Declaration of Human Rights (Chinese, Mandarin Simplified)</a></td>
      <td><b>3,334</b></td>
      <td><b>3,366</b><br />1.01x</td>
      <td><b>3,360</b><br />1.01x</td>
    </tr>
    <tr>
      <td><a href="https://github.com/simonw/sqlite-utils/blob/79117b9d110d72f46dab5fe2cda412ff4789ab55/sqlite_utils/db.py">sqlite_utils/db.py</a> (4,279 lines of Python)</td>
      <td><b>44,014</b></td>
      <td><b>56,118</b><br />1.28x</td>
      <td><b>56,113</b><br />1.27x</td>
    </tr>
  </tbody>
</table>

<p>So the new token is roughly 1.4x times more expensive for English, 1.33x for Spanish, 1.28x for Python code and effectively the same cost for Simplified Mandarin.</p>
<p>Here's <a href="https://gist.github.com/simonw/a89e756b621a31e8ffc210e3428efa77">the pelican</a>. It's nothing to write home about. Sonnet 5 thinks it looks like a goose.</p>
<p><img alt="Illustration of a white goose riding a bicycle, with one wing extended forward to grip the handlebar, set against a plain white background with a brown ground line." src="https://static.simonwillison.net/static/2026/sonnet-5-pelican.png" />

    <p><small></small>Via <a href="https://news.ycombinator.com/item?id=48736605">Hacker News</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/anthropic">anthropic</a>, <a href="https://simonwillison.net/tags/claude">claude</a>, <a href="https://simonwillison.net/tags/llm-pricing">llm-pricing</a>, <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle">pelican-riding-a-bicycle</a>, <a href="https://simonwillison.net/tags/llm-release">llm-release</a></p>
