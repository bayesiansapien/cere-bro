---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-01T10:55:49.212223+00:00
title: "How We Took Over ChatGPT Accounts"
url: https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/
published: 2026-10-31
author: 
---

# How We Took Over ChatGPT Accounts

<p><strong><a href="https://www.parameter.ai/labs/we-found-a-gap-at-openai">How We Took Over ChatGPT Accounts</a></strong></p>
Parameter Labs describe an exploit they found against ChatGPT's implementation of the artifacts pattern (OpenAI used to call this "Canvas" but it looks like the latest revision is called <a href="https://help.openai.com/en/articles/20001246-working-with-writing-blocks-and-code-blocks-in-chatgpt">HTML previews</a>), where interactive custom HTML apps are displayed in a sandboxed iframe.</p>
<p>It's important that HTML in these stays tightly sandboxed to avoid untrusted code interacting with OpenAI APIs and accessing private data.</p>
<p>Parameter found quite a complex attack chain. OpenAI use the MathLive JavaScript library as part of their graph support, and that library includes <a href="https://mathlive.io/mathfield/virtual-keyboard/">its own virtual keyboard</a>, which can be triggered in the parent page via <code>postMessage()</code> from the sandboxed iframe.</p>
<p>That message receiving code uses <code>innerHTML</code>, so anything that sends a message can add custom HTML to the parent - and there was no mechanism to prevent other sandboxed frames, including HTML preview frames, from calling that method.</p>
<p>This meant untrusted code in an iframe could insert HTML, and while <code>innerHTML</code> doesn't directly execute script elements it could be used to inject a new iframe <em>without</em> sandbox restrictions.</p>
<p>OpenAI’s CSP rules blocked inline scripts entirely, and only allowed script loading from a handful of domains, but one of those was YouTube - and the YouTube oEmbed endpoint could be used to reflect JavaScript back in a way that executed it.</p>
<p>Once the attack had JavaScript execution on ChatGPT, it was trivial to fetch private user data from APIs and exfiltrate it via an image reference.</p>
<p>The end result: you could create a ChatGPT share URL which, when visited by another signed-in user, could exfiltrate their private data or take actions on their behalf.</p>
<p>OpenAI closed the hole and paid out a $5,000 bug bounty, which I think was a bit cheap for a vulnerability this serious.

    <p><small></small>Via <a href="https://news.ycombinator.com/item?id=50314699">Hacker News</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/iframes">iframes</a>, <a href="https://simonwillison.net/tags/javascript">javascript</a>, <a href="https://simonwillison.net/tags/sandboxing">sandboxing</a>, <a href="https://simonwillison.net/tags/security">security</a>, <a href="https://simonwillison.net/tags/xss">xss</a>, <a href="https://simonwillison.net/tags/openai">openai</a>, <a href="https://simonwillison.net/tags/chatgpt">chatgpt</a>, <a href="https://simonwillison.net/tags/content-security-policy">content-security-policy</a></p>
