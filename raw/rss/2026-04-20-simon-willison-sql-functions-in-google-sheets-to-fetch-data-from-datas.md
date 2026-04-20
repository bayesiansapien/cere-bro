---
source: farmer/rss
feed: simon-willison
farmed: 2026-04-20T09:02:26.487905+00:00
title: SQL functions in Google Sheets to fetch data from Datasette
url: https://simonwillison.net/2026/Apr/20/datasette-sql/#atom-everything
published: 2026-04-20
author: 
---

# SQL functions in Google Sheets to fetch data from Datasette

<p><strong>TIL:</strong> <a href="https://til.simonwillison.net/google-sheets/datasette-sql">SQL functions in Google Sheets to fetch data from Datasette</a></p>
    <p>I put together some notes on patterns for fetching data from a Datasette instance directly into Google Sheets - using the <code>importdata()</code> function, a "named function" that wraps it or a Google Apps Script if you need to send an API token in an HTTP header (not supported by <code>importdata()</code>.)</p>
<p>Here's <a href="https://docs.google.com/spreadsheets/d/14lRV2-AeBmjI3lJbl2apwfC_ncXqL0uSV68lmtzUI7I/edit?gid=0#gid=0">an example sheet</a> demonstrating all three methods.</p>
    
        <p>Tags: <a href="https://simonwillison.net/tags/spreadsheets">spreadsheets</a>, <a href="https://simonwillison.net/tags/datasette">datasette</a>, <a href="https://simonwillison.net/tags/google">google</a></p>
