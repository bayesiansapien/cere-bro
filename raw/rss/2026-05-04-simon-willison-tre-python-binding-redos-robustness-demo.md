---
source: farmer/rss
feed: simon-willison
farmed: 2026-05-05T03:30:47.125182+00:00
title: TRE Python binding — ReDoS robustness demo
url: https://simonwillison.net/2026/May/4/tre-python-binding/#atom-everything
published: 2026-05-04
author: 
---

# TRE Python binding — ReDoS robustness demo

<p><strong>Research:</strong> <a href="https://github.com/simonw/research/tree/main/tre-python-binding#readme">TRE Python binding — ReDoS robustness demo</a></p>
        <p>If it's <a href="https://simonwillison.net/2026/May/4/redis-array/">good enough for antirez</a> to add to Redis I figured Ville Laurikari's <a href="https://github.com/laurikari/tre/">TRE</a> regular expression engine was worth exploring in a little more detail.</p>
<p>I had Claude Code build an experimental Python binding (it used <code>ctypes</code>) and try some malicious regular expression attacks against the library. TRE handles those much better than Python's standard library implementation, thanks mainly to the lack of support for backtracking.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/security">security</a>, <a href="https://simonwillison.net/tags/python">python</a>, <a href="https://simonwillison.net/tags/regular-expressions">regular-expressions</a>, <a href="https://simonwillison.net/tags/c">c</a>, <a href="https://simonwillison.net/tags/ctypes">ctypes</a></p>
