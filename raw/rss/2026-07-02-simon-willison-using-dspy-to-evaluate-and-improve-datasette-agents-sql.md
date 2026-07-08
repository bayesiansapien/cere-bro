---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-08T05:20:41Z
title: Using DSPy to evaluate and improve Datasette Agent's SQL system prompts
url: https://simonwillison.net/2026/Jul/2/dspy-datasette-agent-prompts/#atom-everything
published: 2026-07-02
author: 
---

# Using DSPy to evaluate and improve Datasette Agent's SQL system prompts

<p><strong>Research:</strong> <a href="https://github.com/simonw/research/tree/main/dspy-datasette-agent-prompts#readme">Using DSPy to evaluate and improve Datasette Agent&#x27;s SQL system prompts</a></p>
        <p>One of this morning's AIE keynotes covered <a href="https://github.com/stanfordnlp/dspy">dspy</a>, which reminded me I've been meaning to see if it could help me improve the system prompt used by <a href="https://agent.datasette.io">Datasette Agent</a> - so I fired off an asynchronous research task in Claude Code for web using Claude Fable 5:</p>
<blockquote>
<p><code>Pip install the latest Datasette alpha and datasette-agent and dspy - then figure out how to use dspy to evaluate and improve the main system prompts used by Datasette Agent for the feature where it can execute read only SQL queries to answer user questions about data.</code></p>
</blockquote>
<p>Fable chose to test using GPT 4.1 mini and nano, and identified several promising looking directions for improvements. I particularly like this one:</p>
<blockquote>
<p>The schema listing gives only table names; the "don't call describe_table if you already have the information" advice caused column-name guessing (page_count, o.order_id, first_name) and error-retry loops in baseline traces. Either include column names in the prompt's schema listing or soften that advice.</p>
</blockquote>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/evals">evals</a>, <a href="https://simonwillison.net/tags/dspy">dspy</a>, <a href="https://simonwillison.net/tags/datasette-agent">datasette-agent</a>, <a href="https://simonwillison.net/tags/claude-mythos-fable">claude-mythos-fable</a></p>
