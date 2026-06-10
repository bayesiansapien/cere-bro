---
source: farmer/rss
feed: simon-willison
farmed: 2026-06-10T06:27:28Z
title: Setting a custom price for a model in AgentsView
url: https://simonwillison.net/2026/Jun/9/agentsview-custom-model-price/#atom-everything
published: 2026-06-09
author: 
---

# Setting a custom price for a model in AgentsView

<p><strong>TIL:</strong> <a href="https://til.simonwillison.net/llms/agentsview-custom-model-price">Setting a custom price for a model in AgentsView</a></p>
        <p>I've been really enjoying <a href="https://agentsview.io/">AgentsView</a> by Wes McKinney as a tool for exploring my token usage across different coding agents running on my laptop.</p>
<p>Claude Fable 5 came out today and wasn't yet included in the pricing database AgentsView uses. I used Fable to reverse-engineer AgentsView and figured out this recipe for setting custom prices.</p>
<p>Here's my Claude Fable 5 usage for today so far, plotted by AgentsView as a treemap across my different local projects:</p>
<p><img alt="Screenshot of a cost analytics dashboard. Cost Attribution - Click to hide from chart - toggle buttons for Project / Model / Agent and Treemap / List. A treemap shows a large red block: prod_datasette_agent $74.06 89.3%, then blue: cloud $3.98 4.8%, teal: datasette $2.81 3.4%, pink: money $1.92 2.3%, and a thin orange sliver. A legend lists 1 prod_datasette_agent $74.06, 2 cloud $3.98, 3 datasette $2.81, 4 money $1.92, 5 simon $0.15. Below left, Top Sessions by Cost: 1 Claude - Review ./datasette-agent and ./datasette-apps - we are going to a... - prod_datasette_agent · 08a1f374-0e77-420f-be2d-af805d67e8aa - 55.9M $74.06; 2 Claude - issues.db is a copy of the Datasette issues database. There are a... - datasette · 8caa2d2d-b91f-43b3-bf3a-4268995b6011 - 826.8k $2.81; 3 Claude - Consult fly-docs and then look at datasette.cloud (which launche... - cloud · bfcacc70-09d7-4b27-aaec-4bb8accd9fec - 924.7k $2.61; 4 Claude - simonwillisonblog.db is a copy of my blog, plus all my software re... - money · 0c0fb9dc-6347-4e1b-9307-3709a7cdf0c8 - 542.9k $1.92; 5 Claude - Look in datasette.cloud and figure out all remaining steps and dec... - cloud · 45963b5f-608a-4caa-ad6b-6ae81e1dbf0d - 455k $1.37; 6 Claude - simon - simon · deeccb5d-9e90-4b1e-bfe6-c2b271e1b1d4 - 26.4k $0.15. Below right, Cache Efficiency with horizontal bars: Cache Reads 57.6M (nearly full green bar), Cache Writes 769.3K, Uncached Input 64.4K, Output 300.9K (all tiny bars), and a green highlighted note: $516.62 saved vs uncached." src="https://static.simonwillison.net/static/2026/agentsview-fable.jpg" /></p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/llm-pricing">llm-pricing</a>, <a href="https://simonwillison.net/tags/claude-mythos">claude-mythos</a></p>
