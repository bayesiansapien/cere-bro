---
source: farmer/rss
feed: simon-willison
farmed: 2026-06-12T09:05:53.929564+00:00
title: datasette 1.0a33
url: https://simonwillison.net/2026/Jun/11/datasette/#atom-everything
published: 2026-06-11
author: 
---

# datasette 1.0a33

<p><strong>Release:</strong> <a href="https://github.com/simonw/datasette/releases/tag/1.0a33">datasette 1.0a33</a></p>
        <p>This alpha is a significant step on the road to a stable 1.0, finally extending the <code>?_extra=</code> pattern I introduced <a href="https://docs.datasette.io/en/1.0a3/changelog.html#a3-2023-08-09">in Datasette 1.0a3</a> to cover queries and rows in addition to tables. That pattern is also <a href="https://docs.datasette.io/en/latest/json_api.html#expanding-json-responses">now documented</a>!</p>
<p>I wrote a whole lot more about the new release on the Datasette project blog: <strong><a href="http://datasette.io/blog/2026/api-extras/">Datasette 1.0a33 with JSON extras in the API</a></strong>.</p>
<p>Because API explorer tools are almost free to build now I had Claude Fable 5 in Claude Code (for <a href="https://gist.github.com/simonw/d8bf1a8f36e28fbd595cede946e0ab6d">the plan</a>) and GPT-5.5 xhigh in Codex Desktop (for <a href="https://gist.github.com/simonw/12d5e09797072a6807d7b9cfcc8ff6b7">the implementation</a>) build me this <a href="https://tools.simonwillison.net/datasette-extras-explorer">custom extras API explorer</a> to help demonstrate the feature:</p>
<p><img alt="Screenshot of a web application titled &quot;Datasette extras explorer&quot;. A URL input field contains https://latest.datasette.io/fixtures/facetable.json with a teal Explore button next to it. Below, a left panel labeled EXTRAS (30) lists checkboxes: all_columns - All columns in the table, regardless of _col/_nocol filtering; column_types - Column type assignments for this table; columns (checked) - Column names returned by this query; count - Total count of rows matching these filters; count_sql - SQL query used to calculate the total count; custom_table_templates - Custom template names considered for this table; database - Database name; database_color - Color assigned to the database. A right panel labeled RESPONSE shows GET /fixtures/fac… with Copy JSON and Copy URL buttons, then a dark JSON viewer showing 200 - 9.9 KB - 114ms and JSON: &quot;ok&quot;: true, &quot;next&quot;: null, &quot;columns&quot;: (highlighted array) &quot;pk&quot;, &quot;created&quot;, &quot;planet_int&quot;, &quot;on_earth&quot;, &quot;state&quot;, &quot;_city_id&quot;, &quot;_neighborhood&quot;, &quot;tags&quot;, &quot;complex_array&quot;, &quot;distinct_some_null&quot;, &quot;n&quot;, &quot;rows&quot;: list of objects." src="https://static.simonwillison.net/static/2026/extras-explorer.png" /></p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/projects">projects</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/annotated-release-notes">annotated-release-notes</a>, <a href="https://simonwillison.net/tags/ai-assisted-programming">ai-assisted-programming</a></p>
