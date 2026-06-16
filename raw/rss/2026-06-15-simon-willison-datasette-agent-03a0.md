---
source: farmer/rss
feed: simon-willison
farmed: 2026-06-16T08:23:58.311844+00:00
title: datasette-agent 0.3a0
url: https://simonwillison.net/2026/Jun/15/datasette-agent/#atom-everything
published: 2026-06-15
author: 
---

# datasette-agent 0.3a0

<p><strong>Release:</strong> <a href="https://github.com/datasette/datasette-agent/releases/tag/0.3a0">datasette-agent 0.3a0</a></p>
        <blockquote>
<ul>
<li>New tool, <code>execute_write_sql</code>, which requests user approval and then writes to a database - taking user permissions into account. <a href="https://github.com/datasette/datasette-agent/issues/27">#27</a></li>
</ul>
</blockquote>
<p>I added a mechanism for asking user approval in <a href="https://simonwillison.net/2026/Jun/10/datasette-agent/">datasette agent 0.2a0</a>. The new <code>execute_write_sql</code> tool can now prompt the user for all kinds of useful operations. Here's an example where I add some pelican sightings to my <code>pelican_sightings</code> table:</p>
<p><img alt="Screenshot of a chat interface showing a write SQL confirmation dialog. User message (blue bubble): &quot;I saw 4 pelicans flying over the harbor&quot;. Collapsed tool section: &quot;► Tool: execute_write_sql&quot;. A yellow-bordered confirmation card reads: &quot;Confirm write SQL batch / Database: pelicans / Statements execute in order. If one statement fails, later statements will not be executed. / Statement 1 / INSERT INTO pelican_sightings (number_of_pelicans, notes) VALUES (:number_of_pelicans, :notes); / number_of_pelicans 4 / notes Flying over the harbor&quot;. A table with columns &quot;Operation, Database, Table, Required permissions&quot; shows row: &quot;insert, pelicans, pelican_sightings&quot; with permission buttons &quot;insert-row&quot;, &quot;update-row&quot;, &quot;delete-row&quot;. Below: &quot;Execute 1 write SQL statement against database 'pelicans'? / Asked by tool: execute_write_sql&quot; with &quot;Yes&quot; (blue) and &quot;No&quot; (gray) buttons." src="https://static.simonwillison.net/static/2026/i-saw-pelicans-agent.jpg" /></p>
<p>The new version also enhances the <code>datasette agent chat</code> terminal mode to support approvals, and adds several new options including <code>--unsafe</code> mode for auto-approving them:</p>
<blockquote>
<ul>
<li><code>datasette agent chat</code> can execute tools that require user approval. <a href="https://github.com/datasette/datasette-agent/issues/30">#30</a></li>
<li>Three new options for <code>datasette agent chat</code> - <code>--root</code> to run as root, <code>--yes</code> to approve all ask user questions, and <code>--unsafe</code> for both.</li>
<li>Tools can now provide plain text alternatives to HTML, for display in the <code>datasette agent chat</code> CLI. <a href="https://github.com/datasette/datasette-agent/issues/31">#31</a></li>
</ul>
</blockquote>
<p>The <code>datasette agent chat content.db -m gpt-5.5 --unsafe</code> command can now be used to chat directly with a specific database <em>and</em> directly modify it through prompts like "create a notes table", "add a note about X" etc.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/projects">projects</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/annotated-release-notes">annotated-release-notes</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/llm-tool-use">llm-tool-use</a>, <a href="https://simonwillison.net/tags/datasette-agent">datasette-agent</a></p>
