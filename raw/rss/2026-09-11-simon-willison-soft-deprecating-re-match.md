---
source: farmer/rss
feed: simon-willison
farmed: 2026-09-11T16:28:34.505966+00:00
title: Soft-deprecating re.match()
url: https://simonwillison.net/2026/Sep/11/soft-deprecating-re-match/
published: 2026-09-11
---

# Soft-deprecating re.match()

<p><strong><a href="https://hugovk.dev/blog/2026/soft-deprecating-re.match/">Soft-deprecating re.match()</a></strong></p>
Python has a concept of <a href="https://peps.python.org/pep-0387/#soft-deprecation">soft deprecation</a>, where APIs are marked as "should no longer be used to write new code" without any promise/threat to remove them in the future.</p>
<p>Python 3.15 release manager Hugo van Kemenade describes how in the upcoming 3.15 release soft deprecation has come for the venerable but deeply confusing <code>re.match()</code> function. It's now available with the much clearer alternative <code>re.prefixmatch()</code> name - reflecting how it anchors at the beginning of the string but not the end.</p>
<p>Most of the time you probably want <code>re.search()</code> (match this pattern anywhere in the string) or <code>re.fullmatch()</code> (match the entire string) instead.

    <p><small></small>Via <a href="https://lobste.rs/s/u7dr96/soft_deprecating_re_match">Lobste.rs</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/python">python</a>, <a href="https://simonwillison.net/tags/regular-expressions">regular-expressions</a></p>
