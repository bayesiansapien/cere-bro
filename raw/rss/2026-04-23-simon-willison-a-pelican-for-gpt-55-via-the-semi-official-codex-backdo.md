---
source: farmer/rss
feed: simon-willison
farmed: 2026-04-30T00:00:00+00:00
title: "A pelican for GPT-5.5 via the semi-official Codex backdoor API"
url: https://simonwillison.net/2026/Apr/23/gpt-5-5/#atom-everything
published: 2026-04-23
---

# A pelican for GPT-5.5 via the semi-official Codex backdoor API

<p><a href="https://openai.com/index/introducing-gpt-5-5/">GPT-5.5 is out</a>. It's available in OpenAI Codex and is rolling out to paid ChatGPT subscribers. I've had some preview access and found it to be a fast, effective and highly capable model. As is usually the case these days, it's hard to put into words what's good about it - I ask it to build things and it builds exactly what I ask for!</p>
<p>There's one notable omission from today's release - the API:</p>
<blockquote>
<p>API deployments require different safeguards and we are working closely with partners and customers on the safety and security requirements for serving it at scale. We'll bring GPT‑5.5 and GPT‑5.5 Pro to the API very soon.</p>
</blockquote>
<p>When I run my <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle/">pelican benchmark</a> I always prefer to use an API, to avoid hidden system prompts in ChatGPT or other agent harnesses from impacting the results.</p>
<h4 id="the-openclaw-backdoor">The OpenClaw backdoor</h4>
<p>One of the ongoing tension points in the AI world over the past few months has concerned how agent harnesses like OpenClaw and Pi interact with the APIs provided by the big providers.</p>
<p>Both OpenAI and Anthropic offer popular monthly subscriptions which provide access to their models at a significant discount to their raw API.</p>
<p>OpenClaw integrated directly with this mechanism, and was then <a href="https://www.theverge.com/ai-artificial-intelligence/907074/anthropic-openclaw-claude-subscription-ban">blocked from doing so</a> by Anthropic. This kicked off a whole thing. OpenAI - who recently hired OpenClaw creator Peter Steinberger - saw an opportunity for an easy karma win and announced that OpenClaw was welcome to continue integrating with OpenAI's subscriptions via the same mechanism used by their (open source) Codex CLI tool.</p>
<p>Does this mean <em>anyone</em> can write code that integrates with OpenAI's Codex-specific APIs to hook into those existing subscriptions?</p>
<p>The other day <a href="https://twitter.com/jeremyphoward/status/2046537816834965714">Jeremy Howard asked</a>:</p>
<blockquote>
<p>Anyone know whether OpenAI officially supports the use of the <code>/backend-api/codex/responses</code> endpoint that Pi and Opencode (IIUC) uses?</p>
</blockquote>
<p>It turned out that on March 30th OpenAI's Romain Huet <a href="https://twitter.com/romainhuet/status/2038699202834841962">had tweeted</a>:</p>
<blockquote>
<p>We want people to be able to use Codex, and their ChatGPT subscription, wherever they like! That means in the app, in the terminal, but also in JetBrains, Xcode, OpenCode, Pi, and now Claude Code.</p>
<p>That’s why Codex CLI and Codex app server are open source too! 🙂</p>
</blockquote>
<p>And Peter Steinberger <a href="https://twitter.com/steipete/status/2046775849769148838">replied to Jeremy</a> that:</p>
<blockquote>
<p>OpenAI sub is officially supported.</p>
</blockquote>
<h4 id="llm-openai-via-codex">llm-openai-via-codex</h4>
<p>So... I had Claude Code reverse-engineer the <a href="https://github.com/openai/codex">openai/codex</a> repo, figure out how authentication tokens were stored and build me <a href="https://github.com/simonw/llm-openai-via-codex">llm-openai-via-codex</a>, a new plugin for <a href="https://llm.datasette.io/">LLM</a> which picks up your existing Codex subscription and uses it to run prompts!</p>
<p>(With hindsight I wish I'd used GPT-5.4 or the GPT-5.5 preview, it would have been funnier. I genuinely considered rewriting the project from scratch using Codex and GPT-5.5 for the sake of the joke, but decided not to spend any more time on this!)</p>
<p>Here's how to use it:</p>
<ol>
<li>Install Codex CLI, buy an OpenAI plan, login to Codex</li>
<li>Install LLM: <code>uv tool install llm</code>
</li>
<li>Install the new plugin: <code>llm install llm-openai-via-codex</code>
</li>
<li>Start prompting: <code>llm -m openai-codex/gpt-5.5 'Your prompt goes here'</code>
</li>
</ol>
<p>All existing LLM features should also work - use <code>-a filepath.jpg/URL</code> to attach an image, <code>llm chat -m openai-codex/gpt-5.5</code> to start an ongoing chat, <code>llm logs</code> to view logged conversations and <code>llm --tool ...</code> to <a href="https://llm.datasette.io/en/stable/tools.html">try it out with tool support</a>.</p>
<h4 id="and-some-pelicans">And some pelicans</h4>
<p>Let's generate a pelican!</p>
<div class="highlight highlight-source-shell"><pre>llm install llm-openai-via-codex
llm -m openai-codex/gpt-5.5 <span class="pl-s"><span class="pl-pds">'</span>Generate an SVG of a pelican riding a bicycle<span class="pl-pds">'</span></span></pre></div>
<p>Here's <a href="https://gist.github.com/simonw/edda1d98f7ba07fd95eeff473cb16634">what I got back</a>:</p>
<p><img alt="It is a bit mangled to be honest - good beak, pelican body shapes are slightly weird, legs do at least extend to the pedals, bicycle frame is not quite right." src="https://static.simonwillison.net/static/2026/gpt-5.5-pelican.png" /></p>
<p>I've seen better <a href="https://simonwillison.net/2026/Mar/17/mini-and-nano/#pelicans">from GPT-5.4</a>, so I tagged on <code>-o reasoning_effort xhigh</code> and <a href="https://gist.github.com/simonw/a6168e4165a258e4d664aeae8e602cc5">tried again</a>:</p>
<p>That one took almost four minutes to generate, but I think it's a much better effort.</p>
<p><img alt="Pelican has gradients now, body is much better put together, bicycle is nearly the right shape albeit with one extra bar between pedals and front wheel, clearly a better image overall." src="https://static.simonwillison.net/static/2026/gpt-5.5-pelican-xhigh.png" /></p>
<p>If you compare the SVG code (<a href="https://gist.github.com/simonw/edda1d98f7ba07fd95eeff473cb16634#response">default</a>, <a href="https://gist.github.com/simonw/a6168e4165a258e4d664aeae8e602cc5#response">xhigh</a>) the <code>xhigh</code> one took a very different approach, which is much more CSS-heavy - as demonstrated by those gradients. <code>xhigh</code> used 9,322 reasoning tokens where the default used just 39.</p>
<h4 id="a-few-more-notes-on-gpt-5-5">A few more notes on GPT-5.5</h4>
<p>One of the most notable things about GPT-5.5 is the pricing. Once it goes live in the API it's <a href="https://openai.com/index/introducing-gpt-5-5/#availability-and-pricing">going to be priced</a> at <em>twice</em> the cost of GPT-5.4 - $5 per 1M input tokens and $30 per 1M output tokens, where 5.4 is $2.5 and $15.</p>
<p>GPT-5.5 Pro will be even more: $30 per 1M input tokens and $180 per 1M output tokens.</p>
<p>GPT-5.4 will remain available. At half the price of 5.5 this feels like 5.4 is to 5.5 as Claude Sonnet is to Claude Opus.</p>
<p>Ethan Mollick has a <a href="https://www.oneusefulthing.org/p/sign-of-the-future-gpt-55">detailed review of GPT-5.5</a> where he put it (and GPT-5.5 Pro) through an array of interesting challenges. His verdict: the jagged frontier continues to hold, with GPT-5.5 excellent at some things and challenged by others in a way that remains difficult to predict.</p>
    
        <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/openai">openai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/chatgpt">chatgpt</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/llm">llm</a>, <a href="https://simonwillison.net/tags/llm-pricing">llm-pricing</a>, <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle">pelican-riding-a-bicycle</a>, <a href="https://simonwillison.net/tags/llm-reasoning">llm-reasoning</a>, <a href="https://simonwillison.net/tags/llm-release">llm-release</a>, <a href="https://simonwillison.net/tags/codex-cli">codex-cli</a>, <a href="https://simonwillison.net/tags/gpt">gpt</a></p>