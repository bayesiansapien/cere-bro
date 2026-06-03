---
source: farmer/rss
feed: simon-willison
farmed: 2026-06-03T06:42:26.878378+00:00
title: Microsoft's new MAI models
url: https://simonwillison.net/2026/Jun/2/microsofts-new-models/#atom-everything
published: 2026-06-02
author: 
---

# Microsoft's new MAI models

<p>Microsoft <a href="https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/">announced two new text LLMs</a> this morning - <strong><a href="https://microsoft.ai/news/introducing-mai-thinking-1/">MAI-Thinking-1</a></strong> (reasoning, 1T parameters, 35B active, available to "select early partners") and <strong><a href="https://microsoft.ai/news/introducingmai-code-1-flash/">MAI-Code-1-Flash</a></strong> (137B Parameters, 5B active, "purpose-built for GitHub Copilot and VS Code to deliver high performance and lower cost [...] rolling out to GitHub Copilot individual users in Visual Studio Code"). I've not been able to try either of them just yet.</p>
<p><strike>It's very interesting to see Microsoft releasing models with such low parameter counts, especially given how expensive larger models are to access right now. They claim MAI-Thinking-1 "is preferred to Sonnet 4.6 in our blind human side-by-side evaluations", which is impressive for a 35B model seeing as I frequently run models larger than that on my own laptop.</strike> (UPDATE: I got this entirely wrong, see note below.)</p>
<p>Also <a href="https://microsoft.ai/news/introducing-mai-thinking-1/">of note</a>:</p>
<blockquote>
<p>We trained [MAI-Thinking-1] from the ground up on enterprise grade, clean and commercially licensed data, without distillation from third-party models.</p>
</blockquote>
<p>And for <a href="https://microsoft.ai/news/introducingmai-code-1-flash/">MAI-Code-1-Flash</a> as well:</p>
<blockquote>
<p>It is built end-to-end by Microsoft using clean and appropriately licensed data.</p>
</blockquote>
<p>I would <em>very much</em> like to learn more about this "appropriately licensed" data! Could these be the first generally useful code-specialist models that didn't train on an unlicensed dump of the web? (<strong>Update</strong>: the answer is no, see note below.)</p>
<p><strong>Update</strong>: My initial published notes got the size of the models wrong. I misread Microsoft's announcements and interpreted the MoE active parameter count as the total parameter count, but the <a href="https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF">model card for MAI-Code-1-Flash</a> lists it as 137B with 5B active and the <a href="https://microsoft.ai/wp-content/uploads/2026/06/main_20260602_2.pdf">MAI-Thinking-1 technical paper</a> reveals it to be a 1T model with 35B active.</p>
<p>I deeply regret this error.</p>
<p><strong>Update 2</strong>: That technical paper describes the training data in some detail from page 80 onwards. It has the same licensing problems as all of the other major LLMs: it's trained on a crawl of the public web:</p>
<blockquote>
<p>The majority of our web HTML corpus comes from a proprietary crawl. After initial page discovery and selection, approximately 1.2 trillion pages are crawled and parsed. [...] In addition to Microsoft standard policy Sec. 2.4, we apply UT1 block list (Prigent, 2026) to remove adult content and piracy-related domains. In all, this filtering reduces the corpus from 1.2 trillion pages to 794 billion pages. Given the prevalence of AI-generated content on the web, we also score pages with a proprietary AI-content detection model and use manual inspection to identify domains with extensive AI-generated content; those domains are filtered out of the training corpus.</p>
<p>[...]</p>
<p>We process Common Crawl with the same pipeline. [...] After filtering, deduplication, merging with the proprietary web corpus, and a final round of exact-URL and content-level fuzzy deduplication, the Common Crawl portion contains 24.2 billion pages.</p>
</blockquote>
<p>I did not cover this one at all well, which is somewhat ironic since I was at the Microsoft Build conference when I wrote this up! I'm sorry for not digging deeper before publishing my initial notes.</p>

    <p>Tags: <a href="https://simonwillison.net/tags/llm-release">llm-release</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/microsoft">microsoft</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/training-data">training-data</a></p>
