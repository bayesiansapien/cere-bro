---
source: farmer/rss
feed: simon-willison
farmed: 2026-10-27T05:06:37.706891+00:00
title: "GPT-6.1 Terra"
url: https://simonwillison.net/2026/Oct/26/gpt-61-terra/
published: 2026-10-26
author: 
---

# GPT-6.1 Terra

<p><strong><a href="https://openai.com/index/introducing-gpt-6-1-terra/">GPT-6.1 Terra</a></strong></p>
It's always interesting to note which aspects of a new model are emphasized in the release announcement.</p>
<p>In the case of GPT-6.1 Terra, OpenAI went with visual reasoning and computer use:</p>
<blockquote>
<p>We’re introducing <strong>GPT-6.1 Terra</strong>, a fast, efficient model that combines detailed visual reasoning and precise computer use alongside clearer, more natural writing. A significant step up from GPT‑5.6 Terra, it excels at the communication and computer-based tasks that fill the workday, from drafting proposals and interpreting technical drawings to filling out forms and editing videos.</p>
</blockquote>
<p>Terra sits in the same position as Sonnet in the Anthropic model collection - not the cheapest or the most expensive, making it harder to decide when to use it.</p>
<p>Computer use is a good example of a task that benefits from a less expensive model, since you might put it to work on automated, repetitive tasks.</p>
<p>OpenAI's Ted Sanders provided some useful advice in <a href="https://news.ycombinator.com/item?id=50248124#50249160">a comment</a> on Hacker News:</p>
<blockquote>
<p>In the case of GPT-6.1 Terra, I'd say Terra is probably better than Astra and Sol at technical communication, similar on vision and computer use (but much faster!), and a bit worse on most other things. For API developers, it's a nice midrange option if you want something cheaper than Sol but a lot smarter than Luna (especially for vision / computer use / communication). For subscribers, it's not a bombshell release - if you're hitting usage limits, maybe it helps you go a bit further, and if you want clearer communication or faster computer use, it can be a nice option to select.</p>
</blockquote>
<p>Here are <a href="https://tools.simonwillison.net/markdown-svg-renderer?url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F855d951d12c68eccca5374cd7d4f834e">the pelicans</a> for the different reasoning levels. This pelican <a href="https://tools.simonwillison.net/markdown-svg-renderer?url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F855d951d12c68eccca5374cd7d4f834e#reasoning-2">for "max"</a> cost <a href="https://www.llm-prices.com/#it=16&amp;ot=22629&amp;sel=gpt-6.1-terra">11.3161 cents</a> and took 4 minutes and 11 seconds:</p>
<p><img alt="It's a good pelican and a good bicycle - correctly shaped frame, feet n pedals either side of the frame, has the same color scheme as the others in the GPT-6 and GPT-6.1 families." src="https://static.simonwillison.net/static/2026-10-26/terra-max.webp" /></p>
<p>Here's <a href="https://static.simonwillison.net/static/2026/openai-pelicans-october-2026.html">a new comparison grid</a> showing pelicans for every reasoning level of OpenAI's current frontier lineup: GPT-6 Astra, GPT-6.1 Sol, GPT-6.1 Terra, and GPT-6 Luna.</p>
<p>GPT-6.1 Terra is priced at $1/million input tokens and $5/million output - almost half the price of GPT-5.6 Terra and GPT-6.1 Sol, and around 10x the price of GPT-6 Luna.

    <p><small></small>Via <a href="https://news.ycombinator.com/item?id=50248124">Hacker News</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/openai">openai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/llm-pricing">llm-pricing</a>, <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle">pelican-riding-a-bicycle</a>, <a href="https://simonwillison.net/tags/llm-release">llm-release</a>, <a href="https://simonwillison.net/tags/gpt">gpt</a></p>
