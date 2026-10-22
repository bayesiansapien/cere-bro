---
source: farmer/rss
feed: simon-willison
farmed: 2026-10-22T07:28:59.709838+00:00
title: "eMudhra Intermediate CA Compromise"
url: https://simonwillison.net/2026/Oct/20/emudhra-certificates/
published: 2026-10-20
author: 
---

# eMudhra Intermediate CA Compromise

<p><strong><a href="https://emudhra.we-have-a-problem.com">eMudhra Intermediate CA Compromise</a></strong></p>
This is very, very bad news:</p>
<blockquote>
<p>The private keys of eight eMudhra intermediate CA certificates have been compromised. They chain to roots trusted by the Mozilla, Microsoft, Apple and Chrome root programs and by many downstream trust stores.</p>
</blockquote>
<p>Any software that bundles a list of trusted certificates needs to be updated. This site is tracking software updates <a href="https://github.com/galadran/we-have-a-problem.com">via this GitHub repository</a> - Linux distros need to update their <code>ca-certificates</code> packages.</p>
<p>In Python world <a href="https://github.com/astral-sh/uv/releases/tag/0.13.4">uv 0.13.4</a> and <a href="https://github.com/pypa/pip/releases/tag/26.2.2">pip 26.2.2</a> and <a href="https://github.com/certifi/python-certifi/releases/tag/2026.10.19">certifi 2026.10.19</a> have been released with upgraded certificate lists.


    <p>Tags: <a href="https://simonwillison.net/tags/encryption">encryption</a>, <a href="https://simonwillison.net/tags/https">https</a>, <a href="https://simonwillison.net/tags/pip">pip</a>, <a href="https://simonwillison.net/tags/python">python</a>, <a href="https://simonwillison.net/tags/security">security</a>, <a href="https://simonwillison.net/tags/uv">uv</a></p>
