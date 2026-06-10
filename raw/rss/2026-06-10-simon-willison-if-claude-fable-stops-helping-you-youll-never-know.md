---
source: farmer/rss
feed: simon-willison
farmed: 2026-06-10T06:27:28Z
title: If Claude Fable stops helping you, you'll never know
url: https://simonwillison.net/2026/Jun/10/if-claude-fable-stops-helping-you/#atom-everything
published: 2026-06-10
author: 
---

# If Claude Fable stops helping you, you'll never know

<p><strong><a href="https://jonready.com/blog/posts/claude-fable5-is-allowed-to-sabotage-your-app-if-youre-a-competitor.html">If Claude Fable stops helping you, you&#x27;ll never know</a></strong></p>
Jonathon Ready highlights one of the more eyebrow-raising details from the <a href="https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf">319 page system card</a> for Fable 5 and Mythos 5. Here's a longer excerpt, highlights mine:</p>
<blockquote>
<p>In light of the ability of recent models to <a href="https://www.anthropic.com/institute/recursive-self-improvement">accelerate their own development</a>, we’ve <strong>implemented new interventions</strong> that limit Claude’s effectiveness for requests targeting frontier LLM development (for example, on <strong>building pretraining pipelines, distributed training infrastructure, or ML accelerator design</strong>). Using Claude to develop competing models already violates our <a href="https://www.anthropic.com/legal/consumer-terms">Terms of Service</a>, but enforcing this restriction through our safeguards avoids accelerating the actors most willing to violate these terms.</p>
<p>Unlike our interventions for cybersecurity, biology and chemistry, and distillation attempts, <strong>these safeguards will not be visible to the user</strong>. Fable 5 will not fall back to a different model. Instead, the safeguards will limit effectiveness through methods such as prompt modification, steering vectors, or parameter-efficient fine-tuning (PEFT). These interventions will not affect the vast majority of coding work. We estimate they will impact ~0.03% of traffic, concentrated in fewer than 0.1% of organizations.</p>
</blockquote>
<p>I believe this is the first time Anthropic have announced these kinds of silent interventions. The justification still feels pretty science-fiction to me - the linked article talks about "recursive self-improvement". I'm not at all keen on a model that silently corrupts its replies to questions about "ML accelerator design" purely to slow down research that might conflict with Anthropic's own goals!

    <p><small></small>Via <a href="https://news.ycombinator.com/item?id=48467896">Hacker News</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/anthropic">anthropic</a>, <a href="https://simonwillison.net/tags/claude">claude</a>, <a href="https://simonwillison.net/tags/ai-ethics">ai-ethics</a>, <a href="https://simonwillison.net/tags/claude-mythos">claude-mythos</a></p>
