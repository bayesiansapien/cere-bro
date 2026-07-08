---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-08T05:20:41Z
title: github-code Web Component
url: https://simonwillison.net/2026/Jul/7/github-code-component/#atom-everything
published: 2026-07-07
author: 
---

# github-code Web Component

<p><strong>Tool:</strong> <a href="https://tools.simonwillison.net/github-code-component">github-code Web Component</a></p>
        <p>An experimental Web Component built using GPT-5.5 and <a href="https://gist.github.com/simonw/0e3db21947b5ae7e29e8a4f69a0b0617">the following prompt</a>:</p>
<blockquote>
<p><code>let's build a Web Component for embedding code from GitHub</code></p>
<p><code>&lt;github-code href="https://github.com/simonw/sqlite-ast/blob/437c759129154f05296324a7f82aa1246340dd14/sqlite_ast/parser.py#L9-L18"&gt;&lt;/github-code&gt;</code></p>
<p><code>It takes URLs like that, converts them to https://raw.githubusercontent.com/simonw/sqlite-ast/437c759129154f05296324a7f82aa1246340dd14/sqlite_ast/parser.py, then uses fetch() to fetch them and displays the specified range of lines - with line numbers, no syntax highlighting though</code></p>
<p><code>Show me a preview web browser so I can see your work</code></p>
</blockquote>
<p>Here's what it looks like embedded on this page:</p>
<p></p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/github">github</a>, <a href="https://simonwillison.net/tags/web-components">web-components</a>, <a href="https://simonwillison.net/tags/gpt">gpt</a></p>
