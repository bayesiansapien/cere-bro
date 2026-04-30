---
source: farmer/rss
feed: simon-willison
farmed: 2026-04-30T00:00:00+00:00
title: "llm 0.31"
url: https://simonwillison.net/2026/Apr/24/llm/#atom-everything
published: 2026-04-24
---

# llm 0.31

<p><strong>Release:</strong> <a href="https://github.com/simonw/llm/releases/tag/0.31">llm 0.31</a></p>
    <blockquote>
<ul>
<li>New GPT-5.5 OpenAI model: <code>llm -m gpt-5.5</code>. <a href="https://github.com/simonw/llm/issues/1418">#1418</a></li>
<li>New option to set the <a href="https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_new_params_and_tools#1-verbosity-parameter">text verbosity level</a> for GPT-5+ OpenAI models: <code>-o verbosity low</code>. Values are <code>low</code>, <code>medium</code>, <code>high</code>.</li>
<li>New option for setting the <a href="https://developers.openai.com/api/docs/guides/images-vision#choose-an-image-detail-level">image detail level</a> used for image attachments to OpenAI models: <code>-o image_detail low</code> - values are <code>low</code>, <code>high</code> and <code>auto</code>, and GPT-5.4 and 5.5 also accept <code>original</code>.</li>
<li>Models listed in <code>extra-openai-models.yaml</code> are now also registered as asynchronous. <a href="https://github.com/simonw/llm/issues/1395">#1395</a></li>
</ul>
</blockquote>
    
        <p>Tags: <a href="https://simonwillison.net/tags/gpt">gpt</a>, <a href="https://simonwillison.net/tags/openai">openai</a>, <a href="https://simonwillison.net/tags/llm">llm</a></p>