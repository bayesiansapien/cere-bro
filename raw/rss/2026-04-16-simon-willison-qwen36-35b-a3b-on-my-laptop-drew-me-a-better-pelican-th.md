---
source: farmer/rss
feed: simon-willison
farmed: 2026-04-17T07:36:43.505254+00:00
title: Qwen3.6-35B-A3B on my laptop drew me a better pelican than Claude Opus 4.7
url: https://simonwillison.net/2026/Apr/16/qwen-beats-opus/#atom-everything
published: 2026-04-16
author: 
---

# Qwen3.6-35B-A3B on my laptop drew me a better pelican than Claude Opus 4.7

<p>For anyone who has been (inadvisably) taking my <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle/">pelican riding a bicycle benchmark</a> seriously as a robust way to test models, here are pelicans from this morning's two big model releases - <a href="https://qwen.ai/blog?id=qwen3.6-35b-a3b">Qwen3.6-35B-A3B from Alibaba</a> and <a href="https://www.anthropic.com/news/claude-opus-4-7">Claude Opus 4.7 from Anthropic</a>.</p>
<p>Here's the Qwen 3.6 pelican, generated using <a href="https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF/blob/main/Qwen3.6-35B-A3B-UD-Q4_K_S.gguf">this 20.9GB Qwen3.6-35B-A3B-UD-Q4_K_S.gguf</a> quantized model by Unsloth, running on my MacBook Pro M5 via <a href="https://lmstudio.ai/">LM Studio</a> (and the <a href="https://github.com/agustif/llm-lmstudio">llm-lmstudio</a> plugin) - <a href="https://gist.github.com/simonw/4389d355d8e162bc6e4547da214f7dd2">transcript here</a>:</p>
<p><img alt="The bicycle frame is the correct shape. There are clouds in the sky. The pelican has a dorky looking pouch. A caption on the ground reads Pelican on a Bicycle!" src="https://static.simonwillison.net/static/2026/Qwen3.6-35B-A3B-UD-Q4_K_S-pelican.png" /></p>
<p>And here's one I got from Anthropic's <a href="https://www.anthropic.com/news/claude-opus-4-7">brand new Claude Opus 4.7</a> (<a href="https://gist.github.com/simonw/afcb19addf3f38eb1996e1ebe749c118">transcript</a>):</p>
<p><img alt="The bicycle frame is entirely the wrong shape. No clouds, a yellow sun. The pelican is looking behind itself, and has a less pronounced pouch than I would like." src="https://static.simonwillison.net/static/2026/opus-4.7-pelican.png" /></p>
<p>I'm giving this one to Qwen 3.6. Opus managed to mess up the bicycle frame!</p>
<p>I tried Opus a second time passing <code>thinking_level: max</code>. It didn't do much better (<a href="https://gist.github.com/simonw/7566e04a81accfb9affda83451c0f363">transcript</a>):</p>
<p><img alt="The bicycle frame is entirely the wrong shape but in a different way. Lines are more bold. Pelican looks a bit more like a pelican." src="https://static.simonwillison.net/static/2026/opus-4.7-pelican-max.png" /></p>

<h4 id="i-dont-think-qwen-are-cheating">I don't think Qwen are cheating</h4>
<p>A lot of people are <a href="https://simonwillison.net/2025/Nov/13/training-for-pelicans-riding-bicycles/">convinced that the labs train for my stupid benchmark</a>. I don't think they do, but honestly this result did give me a little glint of suspicion. So I'm burning one of my secret backup tests - here's what I got from Qwen3.6-35B-A3B and Opus 4.7 for "Generate an SVG of a flamingo riding a unicycle":</p>

<div style="display: flex;">
  <figure style="text-align: center; margin: 0;">
    <figcaption style="margin-bottom: 1em;">Qwen3.6-35B-A3B<br />(<a href="https://gist.github.com/simonw/f1d1ff01c34dda5fdedf684cfc430d92">transcript</a>)</figcaption>
    <img alt="The unicycle spokes are a too long. The pelican has sunglasses, a bowtie and appears to be smoking a cigarette. It has two heart emoji surrounding the caption Flamingo on a Unicycle. It has a lot of charisma." src="https://static.simonwillison.net/static/2026/qwen-flamingo.png" style="height: auto;" />
  </figure>
  <figure style="text-align: center; margin: 0;">
    <figcaption style="margin-bottom: 1em;">Opus 4.7<br />(<a href="https://gist.github.com/simonw/35121ad5dcf23bf860397a103ae88d50">transcript</a>)</figcaption>
    <img alt="The unicycle has a black wheel. The flamingo is a competent if slightly dull vector illustration of a flamingo. It has no flair." src="https://static.simonwillison.net/static/2026/opus-flamingo.png" style="height: auto;" />
  </figure>
</div>


<p>I'm giving this one to Qwen too, partly for the excellent <code>&lt;!-- Sunglasses on flamingo! --&gt;</code> SVG comment.</p>

<h4 id="what-can-we-learn-from-this-">What can we learn from this?</h4>
<p>The pelican benchmark has always been meant as a joke - it's mainly a statement on how obtuse and absurd the task of comparing these models is.</p>
<p>The weird thing about that joke is that, for the most part, there has been a direct correlation between the quality of the pelicans produced and the general usefulness of the models. Those <a href="https://simonwillison.net/2024/Oct/25/pelicans-on-a-bicycle/">first pelicans from October 2024</a> were junk. The <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle/">more recent entries</a> have generally been much, much better - to the point that Gemini 3.1 Pro produces <a href="https://simonwillison.net/2026/Feb/19/gemini-31-pro/">illustrations you could actually use somewhere</a>, provided you had a pressing need to illustrate a pelican riding a bicycle.</p>
<p>Today, even that loose connection to utility has been broken. I have enormous respect for Qwen, but I very much doubt that a 21GB quantized version of their latest model is more powerful or useful than Anthropic's latest proprietary release.</p>
<p>If the thing you need is an SVG illustration of a pelican riding a bicycle though, right now Qwen3.6-35B-A3B running on a laptop is a better bet than Opus 4.7!</p>
    
        <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/local-llms">local-llms</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/anthropic">anthropic</a>, <a href="https://simonwillison.net/tags/claude">claude</a>, <a href="https://simonwillison.net/tags/qwen">qwen</a>, <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle">pelican-riding-a-bicycle</a>, <a href="https://simonwillison.net/tags/llm-release">llm-release</a>, <a href="https://simonwillison.net/tags/lm-studio">lm-studio</a></p>
