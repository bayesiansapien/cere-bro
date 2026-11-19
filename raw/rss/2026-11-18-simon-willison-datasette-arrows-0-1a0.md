---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-19T05:43:16.598167+00:00
title: "datasette-arrows 0.1a0"
url: https://simonwillison.net/2026/Nov/18/datasette-arrows/
published: 2026-11-18
author: 
---

# datasette-arrows 0.1a0

<p><strong>Release:</strong> <a href="https://github.com/datasette/datasette-arrows/releases/tag/0.1a0">datasette-arrows 0.1a0</a></p>
        <p><a href="https://docs.datasette.io/en/latest/changelog.html#a43-2026-11-15">Datasette 1.0a43</a> added the ability for plugins to implement streaming export formats. Datasette core supports streaming CSV and TSV - you can export millions of lines of data from a table without needing to load it all into memory, because those two file formats support streaming data in chunks. The <a href="https://docs.datasette.io/en/latest/plugin_hooks.html#register-output-renderer-datasette">register_output_renderer()</a> plugin hook can now be used to implement the same pattern for other formats.</p>
<p>I've learned never to release a new plugin feature without accompanying it with a plugin that uses it.</p>
<p>Claude Fable 5.2 suggested the <a href="https://arrow.apache.org/docs/python/ipc.html">Apache Arrow streaming</a> format as a good option, and built this plugin in almost a single shot.</p>
<p>Add the plugin to Datasette (<code>datasette install datasette-arrows</code>) and the export dialog gains this new Arrow option:</p>
<p><img alt="Export data modal for the threads table. The TSV and CSV exports are now joined by Arrow, showing &quot;All 927 rows&quot; and the text Apache Arrow IPC stream, for DuckDB, pandas, Polars and other tools. There is a Download button and a Copy URL button." src="https://static.simonwillison.net/static/2026/arrow-export-dialog.webp" /></p>
<p>This screenshot is from Datasette's <code>main</code> branch - the most recent release doesn't yet group streaming formats such as Arrow with the TSV and CSV in the "All rows in this table" section, but that's coming in the next alpha release.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/projects">projects</a></p>
