---
source: farmer/rss
feed: simon-willison
farmed: 2026-06-12T09:16:55.953413+00:00
title: datasette-agent 0.2a0
url: https://simonwillison.net/2026/Jun/10/datasette-agent/#atom-everything
published: 2026-06-10
author: 
---

# datasette-agent 0.2a0

<p><strong>Release:</strong> <a href="https://github.com/datasette/datasette-agent/releases/tag/0.2a0">datasette-agent 0.2a0</a></p>
        <p>Highlights from the release notes:</p>
<blockquote>
<ul>
<li>Tools can now ask the user questions mid-execution. Tools that declare a <code>context</code> parameter receive a <code>ToolContext</code> object, and <code>await context.ask_user(...)</code> can ask a yes/no, multiple-choice (<code>options=[...]</code>) or free-text (<code>free_text=True</code>) question. While a question is unanswered the agent turn suspends: the question renders as a form in the chat UI and persists to the internal database, so suspended conversations survive a server restart. Once answered, the tool re-executes from the top with stored answers replayed, so call <code>ask_user()</code> before performing side effects. <a href="https://github.com/datasette/datasette-agent/pull/20">#20</a></li>
<li>New built-in <code>save_query</code> tool: the agent can save SQL it has written as a <a href="https://docs.datasette.io/en/latest/sql_queries.html#saved-queries">Datasette stored query</a>. Saving always requires human approval - the agent shows the full SQL plus the proposed name, database and visibility, and nothing is stored until you click Yes. <a href="https://github.com/datasette/datasette-agent/pull/20">#20</a></li>
</ul>
</blockquote>
<p>The <code>ask_user()</code> feature was enabled by the new LLM alpha I <a href="https://simonwillison.net/2026/Jun/9/claude-fable-5/#adding-features-to-datasette-agent-and-llm-using-claude-code">built yesterday</a> with the help of Claude Fable 5.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/datasette-agent">datasette-agent</a></p>
