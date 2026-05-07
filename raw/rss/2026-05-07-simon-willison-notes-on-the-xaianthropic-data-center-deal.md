---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-07T21:32:07.379076+00:00
title: Notes on the xAI/Anthropic data center deal
url: https://simonwillison.net/2026/May/7/xai-anthropic/#atom-everything
published: 2026-05-07
author: 
---

# Notes on the xAI/Anthropic data center deal

<p>There weren't a lot of big new announcements from Anthropic at yesterday's Code w/ Claude event, but the biggest by far was the deal they've struck with SpaceX/xAI to use "all of the capacity of their Colossus data center".</p>
<p>As I mentioned in my <a href="https://simonwillison.net/2026/May/6/code-w-claude-2026/">live blog of the keynote</a>, that's the one with the <a href="https://www.politico.com/news/2025/05/06/elon-musk-xai-memphis-gas-turbines-air-pollution-permits-00317582">particularly bad environmental record</a>. The gas turbines installed to power the facility initially ran without Clean Air Act permits or pollution control devices, which they got away with by classifying them as "temporary". Credible reports link it to increases in hospital admissions relating to low air quality.</p>
<p>Andy Masley, one of the most prolific voices pushing back against misleading rhetoric about data centers (see <a href="https://blog.andymasley.com/p/the-ai-water-issue-is-fake">The AI water issue is fake</a> and <a href="https://blog.andymasley.com/p/data-center-land-use-issues-are-fake">Data center land issues are fake</a>), had <a href="https://x.com/andymasley/status/2052070252930826384">this to say</a> about Colossus:</p>
<blockquote>
<p>I would simply not run my computing out of this specific data center</p>
</blockquote>
<p>I get that Anthropic are severely compute-constrained, but in a world where the very existence of "AI data centers" is a red-hot political issue (see recent <a href="https://kutv.com/news/local/amid-boos-box-elder-county-commission-unanimously-approves-plan-for-massive-data-center">news out of Utah</a> for a fresh example), signing up with this particular data center is a really bad look.</p>
<p>There was a lot of initial chatter about how this meant xAI were clearly giving up on their own Grok models, since all of their capacity would be sold to Anthropic instead. That was a misconception - Anthropic are getting Colossus 1, but xAI are keeping their larger Colossus 2 data center for their own work.</p>
<p>As an interesting side note, the night before the Anthropic announcement, xAI sent out a deprecation notice for Grok 4.1 Fast and several other models providing just two weeks' notice before shutdown, reported here <a href="https://twitter.com/xlr8harder/status/2051901091906834439">by @xlr8harder</a> from SpeechMap:</p>
<blockquote>
<p><img alt="Effective May 15, 2026 at 12:00pm PT, the following models will be retired from the xAI API: grok-4-1-fast-reasoning, grok-4-1-fast-non-reasoning, grok-4-fast-reasoning, grok-4-fast-non-reasoning, grok-4-0709, grok-code-fast-1, grok-3, grok-imagine-image-pro. After May 15, 2026, requests to these models will no longer work." src="https://static.simonwillison.net/static/2026/grok-fast-shutdown.png" /></p>
<p>This is terrible @xai. I just spent time and money to migrate to grok 4.1 fast, and you're disabling it with less than two weeks notice, after releasing it in November, with no migration path to a fast/cheap alternative.</p>
<p>I will never depend on one of your products again.</p>
</blockquote>
<p>Here's <a href="https://speechmap.substack.com/p/speechmap-update-xai-loses-top-spot">SpeechMap's detailed explanation</a> of how they selected Grok 4.1 Fast for their project in March.</p>
<p>Were xAI serving those models out of Colossus 1?</p>
<p>xAI owner Elon Musk (who previously delighted in calling Anthropic <a href="https://twitter.com/search?q=from%3Aelonmusk+misanthropic&amp;src=typed_query&amp;f=live">"Misanthropic"</a>) <a href="https://twitter.com/elonmusk/status/2052069691372478511">tweeted</a> the following:</p>
<blockquote>
<p>By way of background for those who care, I spent a lot of time last week with senior members of the Anthropic team to understand what they do to ensure Claude is good for humanity and was impressed. [...]</p>
<p>After that, I was ok leasing Colossus 1 to Anthropic, as SpaceXAI had already moved training to Colossus 2.</p>
</blockquote>
<p>And then <a href="https://twitter.com/elonmusk/status/2052076315306864756">shortly afterwards</a>:</p>
<blockquote>
<p>Just as SpaceX launches hundreds of satellites for competitors with fair terms and pricing, we will provide compute to AI companies that are taking the right steps to ensure it is good for humanity.</p>
<p>We reserve the right to reclaim the compute if their AI engages in actions that harm humanity.</p>
</blockquote>
<p>Presumably the criteria for "harm humanity" are decided by Elon himself. Sounds like a new form of supply chain risk for Anthropic to me!</p>
    
        <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/anthropic">anthropic</a>, <a href="https://simonwillison.net/tags/ai-ethics">ai-ethics</a>, <a href="https://simonwillison.net/tags/ai-energy-usage">ai-energy-usage</a>, <a href="https://simonwillison.net/tags/xai">xai</a>, <a href="https://simonwillison.net/tags/andy-masley">andy-masley</a></p>
