---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-20T09:55:45.157030+00:00
title: Gemini 3.5 Flash: more expensive, but Google plan to use it for everything
url: https://simonwillison.net/2026/May/19/gemini-35-flash/#atom-everything
published: 2026-05-19
author: 
---

# Gemini 3.5 Flash: more expensive, but Google plan to use it for everything

<p>Today at Google I/O, Google <a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/">released Gemini 3.5 Flash</a>. This one skipped the <code>-preview</code> modifier and went straight to general availability, and Google appear to be using it for a whole lot of their key products:</p>
<blockquote>
<p>3.5 Flash is available today to billions of people globally:</p>
<ul>
<li>For everyone via the Gemini app and AI Mode in <a href="https://blog.google/products-and-platforms/products/search/search-io-2026">Google Search</a>
</li>
<li>For developers in our agent-first development platform Google Antigravity and Gemini API in Google AI Studio and Android Studio</li>
<li>For enterprises in Gemini Enterprise Agent Platform and Gemini Enterprise.</li>
</ul>
</blockquote>
<p>As usual with Gemini, the most interesting details are tucked away in the <a href="https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5">What's new in Gemini 3.5 Flash</a> developer documentation. It mostly has the same set of platform features as the previous Gemini 3.x series, albeit with no <a href="https://ai.google.dev/gemini-api/docs/computer-use">computer use</a>. The model ID is <code>gemini-3.5-flash</code>. The knowledge cut-off is January 2025, and it supports 1,048,576 input tokens and 65,536 maximum output tokens.</p>
<p>Google are also pushing a new <a href="https://ai.google.dev/gemini-api/docs/interactions">Interactions API</a>, currently in beta, which looks to me like their version of the patterns introduced by <a href="https://developers.openai.com/api/reference/responses/overview">OpenAI Responses</a> - in particular server-side history management.</p>
<h4 id="the-price-has-gone-up">The price has gone up</h4>
<p>Gemini 3.5 Flash is accompanied by a notable price bump. The previous models in the "Flash" family were <a href="https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview">Gemini 3 Flash Preview</a> and <a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite">Gemini 3.1 Flash-Lite</a>. The new 3.5 Flash is 3x the price of 3 Flash Preview and 6x the price of 3.1 Flash-Lite (see <a href="https://www.llm-prices.com/#sel=gemini-3-flash-preview%2Cgemini-3.5-flash%2Cgemini-3.1-flash-lite-preview">price comparison here</a>).</p>
<p>At $1.50/million input and $9/million output it's getting close in price to Google's Gemini 3.1 Pro, which is $2 and $12.</p>
<p>The Gemini team promise that 3.5 Pro will roll out "next month" - presumably at an even higher price.</p>
<p>This fits a trend: OpenAI's GPT-5.5 was 2x the price of GPT-5.4, and Claude Opus 4.7 is around 1.46x the price of 4.6 when you take the <a href="https://simonwillison.net/2026/Apr/20/claude-token-counts/">new tokenizer into account</a>.</p>
<p>Given the price increase it's interesting to see Google roll it out for so many of their own free-to-consumer products. It feels like all three of the major AI labs are starting to probe the price tolerance of their API customers.</p>
<p>Artificial Analysis publish the cost to run their proprietary benchmark against models, which is a useful way to take things like tokenization and increased volume of reasoning tokens into account. Some numbers worth comparing:</p>
<ul>
<li>
<a href="https://artificialanalysis.ai/models/gemini-3-5-flash">Gemini 3.5 Flash (high)</a>: $1,551.60</li>
<li>
<a href="https://artificialanalysis.ai/models/gemini-3-1-pro-preview">Gemini 3.1 Pro Preview</a>: $892.28</li>
<li>
<a href="https://artificialanalysis.ai/models/gemini-3-flash-reasoning">Gemini 3 Flash Preview (Reasoning)</a>: $278.26</li>
<li>
<a href="https://artificialanalysis.ai/models/gemini-3-1-flash-lite-preview">Gemini 3.1 Flash-Lite Preview</a>: $93.60</li>
</ul>
<p>Running the benchmark for 3.5 Flash (high) cost significantly more than 3.1 Pro Preview!</p>
<p>Here are some numbers from other vendors:</p>
<ul>
<li>
<a href="https://artificialanalysis.ai/models/claude-opus-4-7">Claude Opus 4.7 (Adaptive Reasoning, Max Effort)</a>: $5,117.14</li>
<li>
<a href="https://artificialanalysis.ai/models/claude-opus-4-7-non-reasoning">Claude Opus 4.7 (Non-reasoning, High Effort)</a>: $1,217.23</li>
<li>
<a href="https://artificialanalysis.ai/models/gpt-5-5">GPT-5.5 (xhigh)</a>: $3,357.00</li>
<li>
<a href="https://artificialanalysis.ai/models/gpt-5-5-medium">GPT-5.5 (medium)</a>: $1,199.14</li>
</ul>
<h4 id="a-pelican-on-a-bicycle">A pelican on a bicycle</h4>
<p>I ran "Generate an SVG of a pelican riding a bicycle" <a href="https://gist.github.com/simonw/09cc5a5545d7e75b33b75ffa92a34601">against the Gemini API</a> and got back this pelican, which is a <em>lot</em>:</p>
<p><img alt="Black background, bats in the sky against a stylized moon. Pelican is funky looking. Very good beak. Bicycle frame is a bit twisted, and the bar from pedals to back wheel is missing. Bike lamp illuminates the road in front. Quite stylish." src="https://static.simonwillison.net/static/2026/gemini-3.5-flash.png" /></p>
<p>From the code comments: <code>&lt;!-- Pelican Eye / Sunglasses (Cool Retro Aviators) --&gt;</code></p>
<p><a href="https://news.ycombinator.com/item?id=48196570#48198275">hedgehog on Hacker News</a>:</p>
<blockquote>
<p>That pelican looks like it's in Miami for a crypto conference.</p>
</blockquote>
<p>That one cost me 11 input tokens and 14,403 output tokens, for a total cost of <a href="https://www.llm-prices.com/#it=11&amp;ot=14403&amp;sel=gemini-3.5-flash">just under 13 cents</a>.</p>
    
        <p>Tags: <a href="https://simonwillison.net/tags/google">google</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/gemini">gemini</a>, <a href="https://simonwillison.net/tags/llm-pricing">llm-pricing</a>, <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle">pelican-riding-a-bicycle</a>, <a href="https://simonwillison.net/tags/llm-release">llm-release</a></p>
