---
source: farmer/rss
feed: simon-willison
farmed: 2026-08-25T14:24:43.465259+05:30
title: ChatGPT search now uses the site:operator at scale
url: https://simonwillison.net/2026/Aug/20/chatgpt-search-now-uses-the-siteoperator-at-scale/
published: 2026-08-20
---

# ChatGPT search now uses the site:operator at scale

<p><strong><a href="https://promptwatch.com/data/chatgpt-site-operator-fanouts">ChatGPT search now uses the site:operator at scale</a></strong></p>
Promptwatch is part of the emerging "GEO" space, for Generative Engine Optimization - the chatbot version of SEO, where companies offer tools and consulting to help your site increase its presence in replies to prompts inside tools like ChatGPT.</p>
<p>The Promptwatch product uses automation to track responses to prompts across end-user chat products like ChatGPT, Claude, and Gemini. They publish aggregate reports on this as part of their own content marketing strategy, which do seem to provide credible hints as to otherwise invisible design changes to those products.</p>
<p>Their own tracking shows a notable change aligned with the GPT-5.6 rollout earlier this month:</p>
<blockquote>
<p>The percentage of all ChatGPT Search fanout queries that contain the site:operator, per day. The share hovered between 0.3% and 0.5% for weeks, dipped briefly to 0.15% on August 3 to 5 (consistent with a staged rollout or pre-launch experiment), then jumped to 16-17% on August 8.</p>
</blockquote>
<p>It's important to note that these figures only reflect the prompts for which they have automated tracking enabled.</p>
<p>This corresponds to OpenAI's somewhat vague <a href="https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/">August 6th announcement</a>:</p>
<blockquote>
<p>For Plus and Pro users, we’re updating GPT‑5.6 Sol in Chat to be more reliable with facts and provide more focused answers.</p>
</blockquote>
<p>Once again I am hampered by OpenAI's decision to actively obscure their system prompts, but from poking at ChatGPT I believe their latest search tool has a shape like <code>search(query, recency, domains)</code> rather than encouraging a <code>site:</code> operator directly.</p>
<p>In <a href="https://promptwatch.com/data/reddit-citations-are-dropping-in-chatgpt">a follow-up</a> on August 18th Promptwatch reported that ChatGPT appeared to have greatly reduced the likelihood of Reddit being used in those searches. My own attempts to ascertain if the system prompt has been updated to discourage Reddit sourcing have been unsuccessful - the <a href="https://github.com/asgeirtj/system_prompts_leaks/commits/main/OpenAI">most thorough leaked system prompt</a> collection I know of doesn't yet show any relevant changes.


    <p>Tags: <a href="https://simonwillison.net/tags/reddit">reddit</a>, <a href="https://simonwillison.net/tags/seo">seo</a>, <a href="https://simonwillison.net/tags/openai">openai</a>, <a href="https://simonwillison.net/tags/chatgpt">chatgpt</a>, <a href="https://simonwillison.net/tags/ai-assisted-search">ai-assisted-search</a>, <a href="https://simonwillison.net/tags/system-prompts">system-prompts</a></p>
