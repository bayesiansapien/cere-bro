---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-03T09:29:03.787316+00:00
title: llm 0.37
url: https://simonwillison.net/2026/Nov/2/llm/
published: 2026-11-02
author: 
---

# llm 0.37

<p><strong>Release:</strong> <a href="https://github.com/simonw/llm/releases/tag/0.37">llm 0.37</a></p>
        <p>There's a <em>lot</em> of stuff in this new release of my LLM CLI tool and Python library, representing around two months of accumulated features and fixes.</p>
<p>I added <code>gpt-6.1-sol</code> and <code>gpt-6.1-terra</code>, plus a new <a href="https://llm.datasette.io/en/stable/other-models.html#configure-an-openai-compatible-model">llm openai endpoint add</a> command to make it easier to configure additional models that use OpenAI-compatible endpoints.</p>
<p>I switched the default model (if you have not set your own default) to <code>gpt-6-luna</code> - half the price of the previous default, <code>gpt-5.6-luna</code>.</p>
<p>LLM's support for embeddings now accepts that different binary content may have different content-type - necessary for models like <a href="https://deepmind.google/models/gemini/embedding/">Gemini Embedding 2</a>, which can embed text, audio, images, and video.</p>
<p>A lot of open source maintainers complain about a flood of AI-assisted PRs. LLM is my project that has been most affected by this and, to be honest, I'm not finding it to be a problem. That's mainly because I have Opus 5.5 or GPT-6 Astra help me with triage to spot the most useful fixes!</p>
<p>This release includes fixes from 12 authors - almost all AI-assisted - and the burden of reviewing them wasn't nearly as great as I expected. I really see them as bug reports with attached examples - sometimes I land them, sometimes I implement my own fix.</p>
<p>So thanks to <a href="https://github.com/0d00ciallo0721">0d00ciallo0721</a>, <a href="https://github.com/ac1982">ac1982</a>, <a href="https://github.com/allenflux">Allen Flux</a>, <a href="https://github.com/bianyh">Bian Yuhan</a>, <a href="https://github.com/porkedchop">Bishop Kammeraad</a>, <a href="https://github.com/feiiiiii5">Chen Yufeiyang</a>, <a href="https://github.com/chrikrah">Christopher Krah</a>, <a href="https://github.com/ethanstoner">Ethan Stoner</a>, <a href="https://github.com/er-s-an">Jiachen Xie</a>, <a href="https://github.com/Pajimo">Olamide Faniyan</a>, <a href="https://github.com/sharatchandrasai999-sketch">Sharat Chandra Sai Boddu</a>, <a href="https://github.com/nosmile99">nosmile99</a> for helping out with (or spending tokens on) this release!</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/open-source">open-source</a>, <a href="https://simonwillison.net/tags/projects">projects</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/annotated-release-notes">annotated-release-notes</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/embeddings">embeddings</a>, <a href="https://simonwillison.net/tags/llm">llm</a></p>
