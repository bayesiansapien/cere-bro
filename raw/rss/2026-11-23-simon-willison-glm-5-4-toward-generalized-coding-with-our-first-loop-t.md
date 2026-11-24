---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-24T05:05:53.707941+00:00
title: "GLM-5.4: Toward Generalized Coding with Our First Loop Transformer"
url: https://simonwillison.net/2026/Nov/23/glm-54/
published: 2026-11-23
author: 
---

# GLM-5.4: Toward Generalized Coding with Our First Loop Transformer

<p><strong><a href="https://z.ai/blog/glm-5.4">GLM-5.4: Toward Generalized Coding with Our First Loop Transformer</a></strong></p>
GLM 5.4 is now available from Chinese AI lab Z.ai. It's their first model to use a looped transformer architecture, which they describe like this:</p>
<blockquote>
<p>In a standard Transformer, each layer runs once per forward pass. In a Loop Transformer, a group of weight-shared layers runs for multiple iterations, refining the hidden states from the previous pass. This gives us a deeper network without increasing the parameter count.</p>
</blockquote>
<p>This is the second mention of looped transformers I've seen in the past week - the first was <a href="https://thinkingmachines.ai/news/inkling-2-mini/">Inkling 2 Mini</a> from Thinking Machines Lab on November 20th, who said:</p>
<blockquote>
<p>Inkling 2 Mini is a looped transformer, running the middle layers of the model three times for every token. This allows the model to apply more reasoning and reach the right answer with fewer tokens, especially on tasks such as agentic coding that depend on reasoning quality.</p>
</blockquote>
<p>GLM 5.4 is not (yet?) available as open weights. I tried it out using the Z.ai API, for which I had to sign up for their <a href="https://docs.z.ai/devpack/overview">Coding Plan subscription</a> because 5.4 cannot currently be accessed through the regular API.</p>
<p>It turns out both coding plan and regular API share the same OpenAI-compatible Responses API (at <code>https://api.z.ai/api/v1</code>), and the API key for the coding plan worked with that and gave me access to the new model.</p>
<p>I built a <a href="https://github.com/simonw/llm-glm">llm-glm plugin</a>, then realized that <a href="https://github.com/irthomasthomas/llm-zai">llm-zai</a> by Tommy Hughes already exists! I've shipped mine purely because <code>llm-zai</code> doesn't yet support the new model, but I'll likely retire mine once that plugin catches up.</p>
<p>Here are <a href="https://tools.simonwillison.net/markdown-svg-renderer?url=https%3A%2F%2Fgist.github.com%2Fsimonw%2Fae838c5a6837ca0a602c180c07ac0887">pelicans for GLM-5.4</a> on low, high, and max. This is the max one:</p>
<p><img alt="It's not great to be honest - the pelican is recognizable, but the bicycle frame has a funny front bar connection post and doesn't look like it would steer." src="https://static.simonwillison.net/static/2026/glm-5.4-max.webp" /></p>
<p>I realized I never ran pelicans for GLM-5.3, so <a href="https://tools.simonwillison.net/markdown-svg-renderer?url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F8826d1366dcc98783c7cbc593f6a6e77">here those are</a> for the same effort levels. They look similar in quality to 5.4.</p>
<p>It's interesting how <a href="https://simonwillison.net/2026/Apr/7/glm-51/">GLM 5.1</a> and <a href="https://simonwillison.net/2026/Jun/17/glm-52/#excellent-pelican-disappointing-opossum">GLM 5.2</a> produced radically different pelicans from other models. The pelicans for 5.3 and 5.4 are much more comparable to those I get from OpenAI or Anthropic models - the previous generations had their own distinctive look.</p>
<p>I made a <a href="https://static.simonwillison.net/static/2026/glm-pelican-comparison.html">comparison grid</a> showing the four generations of GLM pelicans all in one place. The style transition between 5.2 and 5.3 is pretty stark.</p>
<p><img alt="The 5.4 and 5.3 pelicans look similar at all three levels. The 5.2 one is on a cyberpunk bicycle. The 5.1 is much more colorful and animated." src="https://static.simonwillison.net/static/2026/glm-family-4.webp" />


    <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/llm">llm</a>, <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle">pelican-riding-a-bicycle</a>, <a href="https://simonwillison.net/tags/llm-release">llm-release</a>, <a href="https://simonwillison.net/tags/ai-in-china">ai-in-china</a>, <a href="https://simonwillison.net/tags/glm">glm</a></p>
