---
source: farmer/rss
feed: simon-willison
farmed: 2026-06-08T09:22:21Z
title: datasette-agent-edit 0.1a0
url: https://simonwillison.net/2026/Jun/7/datasette-agent-edit/#atom-everything
published: 2026-06-07
author: 
---

# datasette-agent-edit 0.1a0

<p><strong>Release:</strong> <a href="https://github.com/datasette/datasette-agent-edit/releases/tag/0.1a0">datasette-agent-edit 0.1a0</a></p>
        <p>I'm planning several plugins for <a href="https://agent.datasette.io/">Datasette Agent</a> which can make edits to existing pieces of text - things like collaborative Markdown editing, updating large SQL queries, and editing SVG files.</p>
<p>Agentic editing of text is a little tricky to get right. My favorite published design for this is for the <a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool#use-the-text-editor-tool">Claude text editor</a>, which implements the following tools:</p>
<ul>
<li><code>view</code> - view sections of a file, with line numbers added to every line.</li>
<li><code>str_replace</code> - find an exact <code>old_str</code> and replace it with <code>new_str</code> - fail if the original string is not unique</li>
<li><code>insert</code> - insert the specified text after the specified line number</li>
</ul>
<p>Rather than recreate these patterns for every plugin that needs them I decided to create this base plugin, <code>datasette-agent-edit</code>, which implements the core tools in a way that allows them to be adapted for other plugins.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/llm-tool-use">llm-tool-use</a>, <a href="https://simonwillison.net/tags/datasette-agent">datasette-agent</a></p>
