---
source: farmer/rss
feed: simon-willison
farmed: 2026-10-07T10:46:48.512319+00:00
title: EmbeddingGemma 2
url: https://simonwillison.net/2026/Oct/6/hn-49983751/
published: 2026-10-06
author: 
---

# EmbeddingGemma 2

<p><a href="https://news.ycombinator.com/item?id=49980487#49983751">My comment</a> on <a href="https://news.ycombinator.com/item?id=49980487">EmbeddingGemma 2</a> &mdash; Hacker News.</p><p>I really appreciate that <a href="https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/">EmbeddingGemma 2</a> is under the Apache 2.0 license.</p>
<p>For embedding models in particular, I don't think it makes sense to use a closed, proprietary, hosted-only model.</p>
<p>Most applications of embedding models involve calculating thousands or even millions of embedding vectors and storing them for later comparison.</p>
<p>If your model is proprietary, the vendor is likely someday going to decide to stop offering that model. They'll have a better model to replace it, but you still need to pay to re-calculate those millions of stored existing vectors.</p>
<p>(In April 2024 OpenAI offered to "cover the financial cost of users re-embedding content with these new models" - <a href="https://openai.com/index/gpt-4-api-general-availability/">https://openai.com/index/gpt-4-api-general-availability/</a> - but I don't think that's something we can rely on from every provider.)</p>
<p>Notably, I <em>don't want to host the model myself</em>. I'd much rather pay a provider for a hosted model while knowing that if they ever stop hosting it I can run the open weights version myself - or find another vendor who can do that for me.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/google">google</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/embeddings">embeddings</a>, <a href="https://simonwillison.net/tags/gemma">gemma</a></p>
