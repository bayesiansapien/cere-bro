---
source: farmer/rss
feed: simon-willison
farmed: 2026-11-09T14:17:49.617285+00:00
title: "parse_number() as a SQLite extension: C vs Rust"
url: https://simonwillison.net/2026/Nov/8/sqlite-parse-number-c-vs-rust/
published: 2026-11-08
author: 
---

# parse_number() as a SQLite extension: C vs Rust

<p><strong>Research:</strong> <a href="https://github.com/simonw/research/tree/main/sqlite-parse-number-c-vs-rust#readme">parse_number() as a SQLite extension: C vs Rust</a></p>
        <p>I was out walking the dog when I got curious about how easy/difficult it would be to write a SQLite C extension that adds a <code>parse_number()</code> function for turning strings like <code>-$1,234.56</code> or <code>'12.5%'</code> into numeric values that could be summed and sorted.</p>
<p>I fired up regular Claude chat (Opus 5.5) <a href="https://claude.ai/share/7f18f157-6c96-4d49-a1d4-f02403e3b261">and prompted</a>:</p>
<blockquote>
<p><code>I'm thinking about a SQLite custom function 'parse_number(value)' that strips ',', '$', '£' and '%', handles a leading '-', and returns 'NULL' for anything it can’t parse</code></p>
<p><code>Explore the difference between building this as a SQLite extension in C v.s. in Rust - I want to compare performance and code complexity and size of the resulting</code>.so<code>(or whatever) file</code></p>
</blockquote>
<p>This gave me a solid starting point - the Rust extension was 321 KB (using <a href="https://github.com/rusqlite/rusqlite">Rusqlite</a>) and 298 KB (using <a href="https://github.com/asg017/sqlite-loadable-rs">sqlite-loadable-rs</a>), while the C extension was 14 KB. But the Rust extension was faster!</p>
<p>Turns out that's because the Rust equivalent of C's <code>strtod</code> is "twice as fast". So I prompted:</p>
<blockquote>
<p><code>Try writing your own C function for parsing text into a decimal number that catches up to or beats the Rust implementation</code></p>
</blockquote>
<p>And it did, using "Clinger's fast path":</p>
<blockquote>
<p>Net cost per row over 2 million rows, lower is better:</p>
<table>
<thead>
<tr>
<th></th>
<th>first C</th>
<th>new C</th>
<th>rusqlite</th>
<th>sqlite-loadable</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mixed data</td>
<td>67 ns</td>
<td><strong>19 ns</strong></td>
<td>46 ns</td>
<td>41 ns</td>
</tr>
<tr>
<td>Integers only</td>
<td>25 ns</td>
<td><strong>16 ns</strong></td>
<td>36 ns</td>
<td>32 ns</td>
</tr>
<tr>
<td>Decimals only</td>
<td>106 ns</td>
<td><strong>18 ns</strong></td>
<td>55 ns</td>
<td>47 ns</td>
</tr>
</tbody>
</table>
</blockquote>

<p>Finally, I had it rewrite the prototype as a research report to match the others in <a href="https://github.com/simonw/research">simonw/research</a> by prompting this:</p>
<blockquote>
<p><code>Clone simonw/research from GitHub and turn your above investigation into a research report as seen in that repository - you can give me a zip file to download that contains your new folder</code></p>
</blockquote>
<p>Here's <a href="https://github.com/simonw/research/tree/main/sqlite-parse-number-c-vs-rust#readme">the resulting report</a>.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/c">c</a>, <a href="https://simonwillison.net/tags/research">research</a>, <a href="https://simonwillison.net/tags/sqlite">sqlite</a>, <a href="https://simonwillison.net/tags/rust">rust</a>, <a href="https://simonwillison.net/tags/claude">claude</a></p>
