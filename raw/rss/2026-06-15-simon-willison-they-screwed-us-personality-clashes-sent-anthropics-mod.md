---
source: farmer/rss
feed: simon-willison
farmed: 2026-06-16T08:23:58.311935+00:00
title: "They screwed us": Personality clashes sent Anthropic's models offline
url: https://simonwillison.net/2026/Jun/15/axios-clashes-anthropics/#atom-everything
published: 2026-06-15
author: 
---

# "They screwed us": Personality clashes sent Anthropic's models offline

<p><strong><a href="https://www.axios.com/2026/06/15/anthropic-white-house-fable-mythos">&quot;They screwed us&quot;: Personality clashes sent Anthropic&#x27;s models offline</a></strong></p>
Lots of "source familiar with the administration's thinking" and "source close to Anthropic" in this Axios piece, which is the best collection of behind-the-scenes gossip I've seen about the US government <a href="https://simonwillison.net/2026/Jun/13/us-government-directive-to-suspend-access/">export control Mythos/Fable story</a> so far.</p>
<p>Logan Graham (<a href="https://logangraham.xyz">I lead the Frontier Red Team at Anthropic</a>), Dave Orr (Head of Safeguards, previously a Director of Engineering at Google DeepMind), and blog favorite <a href="https://simonwillison.net/tags/nicholas-carlini/">Nicholas Carlini</a> are reported to be meeting with the Commerce Department today in D.C. Good luck to them!</p>
<p>(I just noticed Logan was "Special Adviser to the Prime Minister" in the Boris Johnson era, covering AI, science, and technology policy - so significant political experience.)</p>
<p>This closing notes doesn't give me much optimism that we'll be getting Fable back any time soon:</p>
<blockquote>
<p><strong>The bottom line</strong>: One option is to make sure Anthropic's models can't be jailbroken — though perfect jailbreak resistance <a href="https://www.anthropic.com/news/fable-mythos-access">may be</a> impossible.</p>
<p>Absent that, a source familiar with the administration's thinking said it may simply come down to an attitude fix where, instead of feeling dismissed, "everyone feels safe, secure and happy."</p>
</blockquote>
<p>This made me wonder if Anthropic ever successfully addressed the class of attacks described in the <a href="https://llm-attacks.org/">Universal and Transferable Adversarial Attacks on Aligned Language Models</a> paper from 2023.</p>
<p>It looks like their <a href="https://www.anthropic.com/research/next-generation-constitutional-classifiers">Constitutional Classifiers</a> work (that post is from January this year) is relevant to that. They continue to claim that no "universal jailbreak" has been found against Claude Mythos, <a href="https://www.anthropic.com/news/fable-mythos-access">classifying the jailbreak</a> that triggered the US government response as "a potential narrow, non-universal jailbreak".


    <p>Tags: <a href="https://simonwillison.net/tags/jailbreaking">jailbreaking</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/anthropic">anthropic</a>, <a href="https://simonwillison.net/tags/claude">claude</a>, <a href="https://simonwillison.net/tags/nicholas-carlini">nicholas-carlini</a>, <a href="https://simonwillison.net/tags/ai-ethics">ai-ethics</a>, <a href="https://simonwillison.net/tags/claude-mythos">claude-mythos</a></p>
