---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-22T10:11:42.649379+00:00
title: Google I/O, Gemini Spark, Antigravity
url: https://simonwillison.net/2026/May/20/google-io/#atom-everything
published: 2026-05-20
author: 
---

# Google I/O, Gemini Spark, Antigravity

<p>It's hard to find much to write about Google I/O this year because I have a policy of not writing about anything that I can't try out myself, and a lot of the big announcements are "coming soon".</p>
<p>I actually prefer to write about things that are in general availability, because I've had instances in the past where the previews didn't match what was released to the general public later on.</p>
<p>Aside from <a href="https://simonwillison.net/2026/May/19/gemini-35-flash/">Gemini 3.5 Flash</a> the most interesting announcement looks to be Google's upcoming OpenClaw competitor <a href="https://gemini.google/overview/agent/spark/">Gemini Spark</a>, described as "your personal AI agent" which can "connect natively with your favorite Google apps like Gmail, Calendar, Drive, Docs, Sheets, Slides, YouTube, and Google Maps". The FAQ for that also includes this confusing detail:</p>
<blockquote>
<p><strong>What Gemini model does Gemini Spark run on?</strong></p>
<p>Gemini Spark runs on Gemini 3.5 Flash and Antigravity.</p>
</blockquote>
<p>The <a href="https://antigravity.google/">antigravity.google</a> website currently lists Antigravity as a desktop app, a CLI agent tool (written in Go), the <a href="https://github.com/google-antigravity/antigravity-sdk-python">Antigravity SDK</a> (an open source Python wrapper around a bundled closed source Go binary), and the original Antigravity IDE (a VS Code fork).</p>
<p>I guess Gemini Spark, the user-facing hosted agent product, might be running on that Go binary, but I'm not sure why that's worth mentioning in the FAQ!</p>
<p>Naturally I went looking for notes on how Gemini Spark intends to handle the risk of prompt injection. The best information I could find on that was in the <a href="https://cloud.google.com/blog/products/ai-machine-learning/innovations-from-google-io-26-on-google-cloud">Everything Google Cloud customers need to know coming out of Google I/O</a> post aimed at enterprise customers, which includes:</p>
<blockquote>
<p>Spark operates in a fully managed, secure runtime on Google Cloud, meaning you get enterprise-grade security without ever having to manage the underlying infrastructure. Every task executes in a fresh, strictly isolated, ephemeral VM to help ensure data never overlaps between sessions. To protect your enterprise, all traffic routes through our secure Agent Gateway that enforces Data Loss Prevention (DLP) policies, while user credentials remain fully encrypted and are never exposed directly to the agent.</p>
</blockquote>
<p>Given how many people are going to be piping <em>very</em> sensitive data through Gemini Spark in the near future I hope they've made this bullet-proof, or this could be a top candidate for the agent security <a href="https://simonwillison.net/2026/Jan/8/llm-predictions-for-2026/#1-year-a-challenger-disaster-for-coding-agent-security">challenger disaster</a> that we still haven't seen.</p>
<p>Also of note: in <a href="https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/">Transitioning Gemini CLI to Antigravity CLI</a> Google announce that the <a href="https://github.com/google-gemini/gemini-cli">open source Gemini CLI</a> tool (Apache 2.0 licensed TypeScript) will stop working with their AI subscription plans on June 18th, replaced by the new closed source <a href="https://github.com/google-antigravity/antigravity-cli">Antigravity CLI</a>.</p>

    <p>Tags: <a href="https://simonwillison.net/tags/gemini">gemini</a>, <a href="https://simonwillison.net/tags/google">google</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/google-io">google-io</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/prompt-injection">prompt-injection</a></p>
