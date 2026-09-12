---
source: farmer/rss
feed: simon-willison
farmed: 2026-09-12T06:07:20.700645+00:00
title: So you want to use OpenRouter?
url: https://simonwillison.net/2026/Sep/11/so-you-want-to-use-openrouter/
published: 2026-09-11
---

# So you want to use OpenRouter?

<p><strong><a href="https://mmoustafa.com/blog/so-you-want-to-use-openrouter/">So you want to use OpenRouter?</a></strong></p>
One of OpenRouter's selling points is that it "handles fallbacks automatically and picks the most cost-effective option for each request", so you can call a single API endpoint for a model and get routed to the best available backend provider.</p>
<p>Mohamed Moustafa points out a whole set of ways that this can cause you problems. Different providers run different serving software with different optimizations and settings, which means that the same OpenRouter endpoint can serve model requests that behave in different ways.</p>
<p>Some providers even lack vision capability for vision models, and the way the reasoning effort option is processed can differ as well.</p>
<p>Thankfully you can control which provider is routed to using <a href="https://openrouter.ai/docs/guides/routing/provider-selection#allowing-only-specific-providers">the provider.only option</a>. The <a href="https://openrouter.ai/docs/api/api-reference/endpoints/list-all-endpoints-for-a-model">/endpoints method</a> returns the list of available providers for a specific model ID.

    <p><small></small>Via <a href="https://news.ycombinator.com/item?id=49621546">Hacker News</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/openrouter">openrouter</a></p>
