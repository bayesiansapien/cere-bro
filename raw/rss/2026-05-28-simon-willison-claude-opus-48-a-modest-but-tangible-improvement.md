---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-29T09:54:51.177770+00:00
title: Claude Opus 4.8: "a modest but tangible improvement"
url: https://simonwillison.net/2026/May/28/claude-opus-4-8/#atom-everything
published: 2026-05-28
author: 
---

# Claude Opus 4.8: "a modest but tangible improvement"

<p>Anthropic shipped <a href="https://www.anthropic.com/news/claude-opus-4-8">Claude Opus 4.8</a> today. My favourite thing about it is this note in the release announcement:</p>
<blockquote>
<p>Users will find Opus 4.8 to be a modest but tangible improvement on its predecessor. There’s still more to be done: we’re working on developing and releasing models that provide many of the same capabilities as Opus at a lower cost.</p>
</blockquote>
<p>It's so refreshing to see an AI lab honestly describe a release as a minor incremental improvement over the previous model!</p>
<p>Honesty seems to be a theme. Here's my other favorite note from that announcement:</p>
<blockquote>
<p>One of the most prominent improvements in Opus 4.8 is its <em>honesty</em>. We train all our models to be honest---for instance, to avoid making claims that they can't support. But a general problem with AI models is that they sometimes jump to conclusions, confidently claiming to have made progress in their work despite the evidence being thin. Early testers report that Opus 4.8 is more likely to flag uncertainties about its work and less likely to make unsupported claims. This is borne out in <a href="https://www.anthropic.com/claude-opus-4-8-system-card">our evaluations</a>, which show that Opus 4.8 is around four times less likely than its predecessor to allow flaws in code it has written to pass unremarked.</p>
</blockquote>
<p>That linked system card includes the following:</p>
<blockquote>
<p>Claude Opus 4.8 had the lowest incorrect-rate of the six models on every benchmark—the most direct measure of factual hallucination. It achieved this mainly by abstaining on questions about which it was uncertain rather than by answering more questions correctly.</p>
</blockquote>
<h4 id="model-characteristics">Model characteristics</h4>
<p>Not much has changed since 4.7.</p>
<p>It's priced the same as Opus 4.5/4.6/4.7 - $5/million input and $25 per million output. "Fast mode" is twice that price, which is a significant reduction from their previous models - fast mode on 4.6/4.7 remains at $30/$150. Note that <a href="https://platform.claude.com/docs/en/build-with-claude/fast-mode">fast mode</a> is only available to organizations that are part of the research preview, "Contact your account manager to request access".</p>
<p>Both the reliable knowledge cutoff and the training data cutoff are January 2026, the same as for 4.7.</p>
<p>The context window is still 1,000,000 tokens, and the max output is 128,000 tokens.</p>
<p>The <a href="https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8">What's new in Claude Opus 4.8</a> document has some of the more interesting details. These caught my eye:</p>
<blockquote>
<p><strong>Mid-conversation system messages</strong>. Claude Opus 4.8 accepts <code>role: "system"</code> messages immediately after a user turn in the <code>messages</code> array (subject to <a href="https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#limitations">placement rules</a>). This lets you append updated instructions later in a long-running conversation without restating the full system prompt, which preserves <a href="https://platform.claude.com/docs/en/build-with-claude/prompt-caching">prompt cache</a> hits on the earlier turns and reduces input cost on agentic loops.</p>
</blockquote>
<p>See also <a href="https://github.com/anthropics/anthropic-sdk-python/commit/2b826760101664ef89db42132932f53ba97c894d#diff-a947c9c02eab58e8ddbe799a11832d533836d242e07c7251997f8543f0981f2f">this update</a> to the Anthropic Python SDK. Being able to steer the system prompt mid-conversation sounds really powerful. I was worried this would be incompatible with the abstraction provided by my own <a href="https://llm.datasette.io/en/stable/python-api.html#system-prompts">LLM library</a>, which expects a single system prompt per conversation... but it turns out my recent <a href="https://simonwillison.net/2026/Apr/29/llm/">redesign</a> should handle that <a href="https://github.com/simonw/llm-anthropic/issues/73">just fine</a>.</p>
<blockquote>
<p><strong>Lower prompt cache minimum</strong>. The minimum cacheable prompt length on Claude Opus 4.8 is 1,024 tokens, lower than on Claude Opus 4.7.</p>
</blockquote>
<p>I checked and 4.7's minimum <a href="https://platform.claude.com/docs/en/build-with-claude/prompt-caching#cache-limitations">was 4,096</a>.</p>
<h4 id="and-some-pelicans">And some pelicans</h4>
<p>Here are <a href="https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2Ffea4f7546626d627862dc241a4e3a86a">pelicans riding bicycles</a> for all five thinking levels, <code>low</code>, <code>medium</code>, <code>high</code>, <code>xhigh</code>, and <code>max</code>:</p>

<div>
    <figure style="margin: 0; text-align: center;">
        <img alt="Flat-style cartoon illustration of a white duck with an orange beak and legs riding a black bicycle, its feet on the pedals, against a blue sky and green grass background." src="https://static.simonwillison.net/static/2026/claude-opus-4.8-low.png" style="width: 100%; height: auto; border: 1px solid #ccc;" />
        <figcaption style="font-family: system-ui, sans-serif; font-weight: bold;">
            <a href="https://gist.github.com/simonw/fea4f7546626d627862dc241a4e3a86a#response">low</a>
        </figcaption>
    </figure>
    <figure style="margin: 0; text-align: center;">
        <img alt="Flat-style illustration of a white egret or heron with an orange beak and legs riding a black bicycle, against a blue sky and green grass background." src="https://static.simonwillison.net/static/2026/claude-opus-4.8-medium.png" style="width: 100%; height: auto; border: 1px solid #ccc;" />
        <figcaption style="font-family: system-ui, sans-serif; font-weight: bold;">
            <a href="https://gist.github.com/simonw/fea4f7546626d627862dc241a4e3a86a#response-1">medium</a>
        </figcaption>
    </figure>
    <figure style="margin: 0; text-align: center;">
        <img alt="Cartoon illustration of a white duck with an orange beak riding a black bicycle, against a light blue sky with a pale yellow sun in the upper left and a green ground line at the bottom." src="https://static.simonwillison.net/static/2026/claude-opus-4.8-high.png" style="width: 100%; height: auto; border: 1px solid #ccc;" />
        <figcaption style="font-family: system-ui, sans-serif; font-weight: bold;">
            <a href="https://gist.github.com/simonw/fea4f7546626d627862dc241a4e3a86a#response-2">high</a>
        </figcaption>
    </figure>
    <figure style="margin: 0; text-align: center;">
        <img alt="Cartoon illustration of a white pelican with an orange beak riding a black bicycle, its orange legs extending down to the pedals, against a blue sky with a yellow sun and green ground." src="https://static.simonwillison.net/static/2026/claude-opus-4.8-xhigh.png" style="width: 100%; height: auto; border: 1px solid #ccc;" />
        <figcaption style="font-family: system-ui, sans-serif; font-weight: bold;">
            <a href="https://gist.github.com/simonw/fea4f7546626d627862dc241a4e3a86a#response-3">xhigh</a>
        </figcaption>
    </figure>
    <figure style="margin: 0; text-align: center;">
        <img alt="Cartoon illustration of a white pelican with an orange beak riding a red bicycle on green grass, against a light blue sky with a fluffy white cloud and a yellow sun." src="https://static.simonwillison.net/static/2026/claude-opus-4.8-max.png" style="width: 100%; height: auto; border: 1px solid #ccc;" />
        <figcaption style="font-family: system-ui, sans-serif; font-weight: bold;"><a href="https://gist.github.com/simonw/fea4f7546626d627862dc241a4e3a86a#response-4">max</a></figcaption>
    </figure>
</div>


<p>This time I ran them using the <a href="https://llm.datasette.io/en/stable/usage.html">LLM CLI</a>, exported the logs to Markdown and then had Claude Opus 4.8 <a href="https://github.com/simonw/tools/commit/71e4944766b577a327ff048cc63b739ba4cbade9">build me</a> an HTML tool that could render that Markdown with the <code>svg</code> fenced code blocks displayed as SVGs on the page.</p>

<p>(I later had GPT-5.5 xhigh in Codex <a href="https://gist.github.com/simonw/bb5a267f8144dfe4e92e50a014e49e98">update that code</a> to remove any XSS holes. I'm sure Claude could have done that if I'd asked, but GPT-5.5 is my code security blanket at the moment.)</p>

<p>The max one  was clearly the best, but it did take 25 input, 17,167 output tokens for a total cost of <a href="https://www.llm-prices.com/#it=25&amp;ot=17167&amp;ic=5&amp;oc=25&amp;sel=claude-opus-4-5">43 cents</a>!</p>
    
        <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/anthropic">anthropic</a>, <a href="https://simonwillison.net/tags/claude">claude</a>, <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle">pelican-riding-a-bicycle</a>, <a href="https://simonwillison.net/tags/llm-release">llm-release</a></p>
