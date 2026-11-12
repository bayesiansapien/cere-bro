---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-12T07:27:43.735870+00:00
title: Gemini Decisions API
url: https://simonwillison.net/2026/Nov/11/gemini-decisions-api/
published: 2026-11-11
author: 
---

# Gemini Decisions API

<p><strong><a href="https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/">Gemini Decisions API</a></strong></p>
Google join <a href="https://simonwillison.net/2026/Sep/21/jev/">Jev</a> and <a href="https://simonwillison.net/2026/Oct/6/llm-openai-decisions/">OpenAI</a> in the decision model category with "Gemini Decision 1". This new model API is almost identical to Jev: it supports the same three types of questions (yes/no, choice, and rubric-scoring) and even reuses Jev's term "Noul" for a yes/no question.</p>
<p>It's priced the same as the GPT-6 Luna decision model: 10 cents per million input tokens, and output is free. Jev remains the cheapest of the three, at 4.2 cents per million.</p>
<p>Jev is text (and JSON) only. OpenAI can handle text and images. Gemini Decision 1 is fully multi-model: it covers text, images, audio, video, and PDFs.</p>
<p>I tested it against video by passing these questions to it along with my <a href="https://simonwillison.net/2026/Nov/10/yonkers-rises/">Yonkers stomping robot</a> video file:</p>
<pre><code>dragon: Does this video have a dragon in it?
robot: Does this video have a robot in it?
france: Is this video set in France?
usa: Is this video set in the USA?
</code></pre>
<p>Jev and OpenAI both return 1.0 or 0.0 for yes/no questions, but Gemini insists on being a little less confident than that:</p>
<div class="highlight highlight-source-json"><pre>{
  <span class="pl-ent">"dragon"</span>: {
    <span class="pl-ent">"type"</span>: <span class="pl-s"><span class="pl-pds">"</span>yes_no<span class="pl-pds">"</span></span>,
    <span class="pl-ent">"probability"</span>: <span class="pl-c1">0.04976021841520312</span>
  },
  <span class="pl-ent">"robot"</span>: {
    <span class="pl-ent">"type"</span>: <span class="pl-s"><span class="pl-pds">"</span>yes_no<span class="pl-pds">"</span></span>,
    <span class="pl-ent">"probability"</span>: <span class="pl-c1">0.9234055387792485</span>
  },
  <span class="pl-ent">"france"</span>: {
    <span class="pl-ent">"type"</span>: <span class="pl-s"><span class="pl-pds">"</span>yes_no<span class="pl-pds">"</span></span>,
    <span class="pl-ent">"probability"</span>: <span class="pl-c1">0.08329171353166241</span>
  },
  <span class="pl-ent">"usa"</span>: {
    <span class="pl-ent">"type"</span>: <span class="pl-s"><span class="pl-pds">"</span>yes_no<span class="pl-pds">"</span></span>,
    <span class="pl-ent">"probability"</span>: <span class="pl-c1">0.9230459995157706</span>
  }
}</pre></div>

    <p><small></small>Via <a href="https://news.ycombinator.com/item?id=50456791">Hacker News</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/gemini">gemini</a>, <a href="https://simonwillison.net/tags/llm-release">llm-release</a>, <a href="https://simonwillison.net/tags/jev">jev</a>, <a href="https://simonwillison.net/tags/decision-models">decision-models</a></p>
