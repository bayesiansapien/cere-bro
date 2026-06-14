---
source: farmer/rss
feed: simon-willison
farmed: 2026-06-14T08:36:29.662381+00:00
title: Mapping SQLite result columns back to their source `table.column`
url: https://simonwillison.net/2026/Jun/13/sqlite-column-provenance/#atom-everything
published: 2026-06-13
author: 
---

# Mapping SQLite result columns back to their source `table.column`

<p><strong>Research:</strong> <a href="https://github.com/simonw/research/tree/main/sqlite-column-provenance#readme">Mapping SQLite result columns back to their source `table.column`</a></p>
        <p>It would be neat if arbitrary SQL queries in <a href="https://datasette.io/">Datasette</a> could be rendered with additional information based on which columns from which tables were included in the results.</p>
<p>To build that, we would need to be able to look at a SQL query like <code>select users.name, orders.total from users join orders on orders.user_id = users.id</code> and programmatically identify the <code>table.column</code> for each result - navigating not just joins but also more complex syntax like CTEs.</p>
<p>I decided to set Claude Code (Opus 4.8, since Fable is currently <a href="https://simonwillison.net/2026/Jun/13/us-government-directive-to-suspend-access/">banned by the US government</a>) on the problem. It found several promising solutions - one using <a href="https://github.com/rogerbinns/apsw">apsw</a>, another that uses <code>ctypes</code> to access the SQLite <code>sqlite3_column_table_name()</code> <a href="https://sqlite.org/c3ref/column_database_name.html">C function</a> (which is not otherwise exposed to Python), and one using clever interrogation of the output of <code>EXPLAIN</code>.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/python">python</a>, <a href="https://simonwillison.net/tags/sqlite">sqlite</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a></p>
