---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-19T22:17:42.122473+00:00
title: Using uvx in GitHub Actions in a cache-friendly way
url: https://simonwillison.net/2026/Jul/14/uvx-github-actions-cache/#atom-everything
published: 2026-07-14
---

# Using uvx in GitHub Actions in a cache-friendly way

<p><strong>TIL:</strong> <a href="https://til.simonwillison.net/github-actions/uvx-github-actions-cache">Using uvx in GitHub Actions in a cache-friendly way</a></p>
        <p>I finally found a cache-friendly recipe for using <code>uvx tool-name</code> in GitHub Actions workflows that I like.</p>
<p>The trick is setting a <code>UV_EXCLUDE_NEWER: "2026-07-12"</code> environment variable at the start of the workflow and then using that as part of the GitHub Actions cache key. This means any <code>uvx tool-name</code> commands will resolve to the most recent version as-of that date, and you can bust the cache and upgrade the tools by bumping the date in the future.</p>
<p>My goal here is to use Python tools in GitHub Actions without every run of the workflow hitting PyPI to download a fresh copy of the tool and its dependencies.</p>
<p><strong>Update</strong>: Here's an existing <a href="https://github.com/astral-sh/setup-uv/issues/745">issue</a> against the <code>astral-sh/setup-uv</code> repository requesting that they switch the default to cache rather than purge wheels from PyPI.</p>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/packaging">packaging</a>, <a href="https://simonwillison.net/tags/pypi">pypi</a>, <a href="https://simonwillison.net/tags/python">python</a>, <a href="https://simonwillison.net/tags/github-actions">github-actions</a>, <a href="https://simonwillison.net/tags/uv">uv</a></p>
