---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-12T07:27:43.736314+00:00
title: llm 0.37.2
url: https://simonwillison.net/2026/Nov/11/llm/
published: 2026-11-11
author: 
---

# llm 0.37.2

<p><strong>Release:</strong> <a href="https://github.com/simonw/llm/releases/tag/0.37.2">llm 0.37.2</a></p>
        <p>Fixes a security issue reported by <a href="https://github.com/BluePlexus">Daniel de Araujo</a> in <a href="https://github.com/simonw/llm/security/advisories/GHSA-v9h7-jj4g-f862">GHSA-v9h7-jj4g-f862</a> and <a href="https://github.com/simonw/llm/security/advisories/GHSA-r639-rr7r-x72w">GHSA-r639-rr7r-x72w</a>.</p>
<p>LLM has a mechanism called <a href="https://llm.datasette.io/en/stable/other-models.html#configure-an-openai-compatible-model">extra-openai-models.yaml</a> - now managed by the new-in-0.37 <a href="https://llm.datasette.io/en/stable/other-models.html#openai-endpoint-add">llm openai endpoint add</a> command - for using LLM with OpenAI-compatible API endpoints from other providers.</p>
<p>Daniel reported two ways this could accidentally send your configured OpenAI API key to one of those providers: if the key named by <code>api_key_name</code> had never been stored, or if a <code>responses: true</code> model was run with <code>-o chat_completions 1</code>.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/projects">projects</a>, <a href="https://simonwillison.net/tags/security">security</a>, <a href="https://simonwillison.net/tags/llm">llm</a>, <a href="https://simonwillison.net/tags/releases">releases</a></p>
